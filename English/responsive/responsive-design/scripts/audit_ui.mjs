#!/usr/bin/env node
/**
 * Reusable Playwright browser UI audit for PivotUI responsive & interaction checks.
 *
 * Usage:
 *   node scripts/audit_ui.mjs <url-or-html-file> [--viewports 1440x900,768x900,375x812] [--json]
 *
 * Requires an existing Playwright installation (resolves from local node_modules
 * or PLAYWRIGHT_MODULE environment variable) and an installed Chromium/Edge/Chrome
 * browser (or PLAYWRIGHT_EXECUTABLE / Playwright bundled chromium).
 */

import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);

function loadPlaywright() {
  const candidates = [];
  if (process.env.PLAYWRIGHT_MODULE) candidates.push(process.env.PLAYWRIGHT_MODULE);
  candidates.push('playwright');
  for (const mod of candidates) {
    try {
      return require(mod);
    } catch {
      // try next
    }
  }
  throw new Error('Playwright module not found. Install playwright or set PLAYWRIGHT_MODULE.');
}

function findBrowserExecutable() {
  if (process.env.PLAYWRIGHT_EXECUTABLE && fs.existsSync(process.env.PLAYWRIGHT_EXECUTABLE)) {
    return process.env.PLAYWRIGHT_EXECUTABLE;
  }
  const winPaths = [
    'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
    'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe',
    'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
  ];
  const unixPaths = [
    '/usr/bin/chromium',
    '/usr/bin/chromium-browser',
    '/usr/bin/google-chrome',
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
  ];
  for (const candidate of process.platform === 'win32' ? winPaths : unixPaths) {
    if (fs.existsSync(candidate)) return candidate;
  }
  return undefined;
}

function parseArgs(argv) {
  const opts = { target: null, viewports: ['1440x900', '768x900', '375x812'], asJson: false, maxTabs: 25 };
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === '--json') opts.asJson = true;
    else if (arg === '--viewports') opts.viewports = (argv[++i] || '').split(',').filter(Boolean);
    else if (arg === '--max-tabs') opts.maxTabs = Number(argv[++i] || 25);
    else if (arg === '--help' || arg === '-h') return { help: true };
    else if (!opts.target) opts.target = arg;
    else throw new Error(`Unexpected argument: ${arg}`);
  }
  if (!opts.target) throw new Error('Target URL or HTML file path is required.');
  return opts;
}

function toTargetUrl(target) {
  if (/^https?:\/\//i.test(target) || /^file:\/\//i.test(target)) return target;
  const resolved = path.resolve(target);
  if (!fs.existsSync(resolved)) throw new Error(`File not found: ${resolved}`);
  return pathToFileURL(resolved).href;
}

async function auditViewport(page, label, width, height, maxTabs) {
  await page.setViewportSize({ width, height });
  await page.waitForTimeout(150);

  const staticAudit = await page.evaluate((isNarrow) => {
    const doc = document.documentElement;
    const viewportW = doc.clientWidth;
    const scrollW = Math.max(doc.scrollWidth, document.body ? document.body.scrollWidth : 0);
    const overflowing = [];
    const unnamedControls = [];
    const smallTouchTargets = [];

    for (const el of document.querySelectorAll('*')) {
      const style = getComputedStyle(el);
      if (style.display === 'none' || style.visibility === 'hidden') continue;
      const rect = el.getBoundingClientRect();
      if (rect.width === 0 && rect.height === 0) continue;

      if (rect.right > viewportW + 1.5) {
        // Ignore elements safely clipped inside a local horizontal scroll container
        let p = el.parentElement;
        let locallyScrolled = false;
        while (p && p !== doc) {
          const ps = getComputedStyle(p);
          if (ps.overflowX === 'auto' || ps.overflowX === 'scroll') {
            locallyScrolled = true;
            break;
          }
          p = p.parentElement;
        }
        if (!locallyScrolled && overflowing.length < 10) {
          overflowing.push({
            tag: el.tagName.toLowerCase(),
            id: el.id || undefined,
            className: typeof el.className === 'string' ? el.className.slice(0, 60) : undefined,
            right: Math.round(rect.right),
            viewportW,
          });
        }
      }

      const isInteractive =
        el.matches('button, a[href], input:not([type="hidden"]), select, textarea, [role="button"], [role="link"]');
      if (isInteractive) {
        const text = (el.textContent || '').trim();
        const aria = (el.getAttribute('aria-label') || el.getAttribute('aria-labelledby') || el.getAttribute('title') || '').trim();
        const inputLabel = (el.id ? document.querySelector(`label[for="${CSS.escape(el.id)}"]`) : null) || el.closest('label');
        if (!text && !aria && !inputLabel && !(el.tagName === 'INPUT' && el.getAttribute('placeholder'))) {
          if (unnamedControls.length < 10) {
            unnamedControls.push({ tag: el.tagName.toLowerCase(), id: el.id || undefined });
          }
        }
        if (isNarrow && (rect.width < 36 || rect.height < 36) && smallTouchTargets.length < 10) {
          smallTouchTargets.push({
            tag: el.tagName.toLowerCase(),
            label: (text || aria).slice(0, 32),
            width: Math.round(rect.width),
            height: Math.round(rect.height),
          });
        }
      }
    }

    const dialogs = [...document.querySelectorAll('[role="dialog"], dialog[open]')].map((dlg) => {
      const ds = getComputedStyle(dlg);
      return { tag: dlg.tagName.toLowerCase(), bg: ds.backgroundColor, color: ds.color };
    });

    return {
      viewportW,
      scrollW,
      hasHorizontalOverflow: scrollW > viewportW + 1,
      overflowing,
      unnamedControls,
      smallTouchTargets,
      openDialogs: dialogs,
    };
  }, width <= 480);

  // Keyboard Tab traversal audit
  await page.evaluate(() => {
    if (document.activeElement && document.activeElement !== document.body) {
      document.activeElement.blur();
    }
  });
  const hiddenFocusViolations = [];
  const visited = [];
  for (let step = 0; step < maxTabs; step++) {
    await page.keyboard.press('Tab');
    const info = await page.evaluate(() => {
      const el = document.activeElement;
      if (!el || el === document.body || el === document.documentElement) return null;
      const style = getComputedStyle(el);
      const rect = el.getBoundingClientRect();
      const hiddenAncestor = Boolean(el.closest('[aria-hidden="true"], [hidden], [inert]'));
      const invisible = style.visibility === 'hidden' || style.display === 'none' || (rect.width === 0 && rect.height === 0);
      return {
        tag: el.tagName.toLowerCase(),
        id: el.id || undefined,
        text: (el.textContent || el.getAttribute('aria-label') || '').trim().slice(0, 32),
        hiddenAncestor,
        invisible,
      };
    });
    if (!info) continue;
    visited.push(info);
    if (info.hiddenAncestor || info.invisible) {
      hiddenFocusViolations.push(info);
    }
  }

  const errors = [];
  if (staticAudit.hasHorizontalOverflow) {
    errors.push(`Horizontal overflow detected (${staticAudit.scrollW}px > ${staticAudit.viewportW}px).`);
  }
  if (staticAudit.unnamedControls.length > 0) {
    errors.push(`${staticAudit.unnamedControls.length} interactive control(s) missing accessible name.`);
  }
  if (hiddenFocusViolations.length > 0) {
    errors.push(`${hiddenFocusViolations.length} focus step(s) landed on hidden or aria-hidden elements.`);
  }

  return {
    viewport: label,
    width,
    height,
    ok: errors.length === 0,
    errors,
    warnings: staticAudit.smallTouchTargets.length > 0
      ? [`${staticAudit.smallTouchTargets.length} narrow-screen control(s) below 36px touch target.`]
      : [],
    details: {
      ...staticAudit,
      tabSamples: visited.length,
      hiddenFocusViolations,
    },
  };
}

async function main() {
  const opts = parseArgs(process.argv.slice(2));
  if (opts.help) {
    console.log('Usage: node scripts/audit_ui.mjs <url-or-html-file> [--viewports 1440x900,768x900,375x812] [--max-tabs 25] [--json]');
    return;
  }
  const { chromium } = loadPlaywright();
  const url = toTargetUrl(opts.target);
  const executablePath = findBrowserExecutable();
  const browser = await chromium.launch({ headless: true, ...(executablePath ? { executablePath } : {}) });
  try {
    const context = await browser.newContext();
    const page = await context.newPage();
    await page.goto(url, { waitUntil: 'networkidle' });
    const results = [];
    for (const spec of opts.viewports) {
      const [w, h] = spec.split('x').map(Number);
      if (!w || !h) throw new Error(`Invalid viewport: ${spec}`);
      results.push(await auditViewport(page, spec, w, h, opts.maxTabs));
    }
    const ok = results.every((r) => r.ok);
    const report = { target: url, browser: executablePath ? path.basename(executablePath) : 'playwright-chromium', ok, results };
    if (opts.asJson) {
      console.log(JSON.stringify(report, null, 2));
    } else {
      console.log(`[${ok ? 'PASS' : 'FAIL'}] UI Audit (${report.browser}) -> ${opts.target}`);
      for (const r of results) {
        console.log(`  ${r.viewport}: ${r.ok ? 'OK' : 'FAIL'} (tabs sampled: ${r.details.tabSamples}, scrollW: ${r.details.scrollW}/${r.details.viewportW})`);
        for (const e of r.errors) console.log(`    error: ${e}`);
        for (const w of r.warnings) console.log(`    warn : ${w}`);
      }
    }
    process.exitCode = ok ? 0 : 1;
  } finally {
    await browser.close();
  }
}

main().catch((err) => {
  console.error(`Audit failed: ${err.message}`);
  process.exitCode = 2;
});
