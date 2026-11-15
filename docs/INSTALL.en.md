# Install and use PivotUI

[中文](INSTALL.zh-CN.md) · [Project overview](../README.en.md) · [Skill guide](SKILLS.en.md)

Install one complete language edition and a native **pivotui** Skill entry. Choose [one-command npx installation](#command-install) or [download-and-copy ZIP installation](#zip-install). Both start with `design-orchestrator` and read only the modules needed for your task.

[Global installation: npx](#global-install) / [ZIP](#global-zip-install) · [Optional raw files/MCP](#manual-setup) · [Legacy Python installer](#legacy-python) · MCP: [Codex](#codex) / [Claude Code](#claude-code) / [DSH](#deepseek-harness) / [other Agents](#other-agents).

<a id="command-install"></a>

## Option 1: One npx command

Requires **Node.js 22+ and npm/npx**. Run the command in the **target project's root**, in the environment where the Agent runs:

```sh
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent codex --language en
```

npx downloads a prepared release package and runs its installer. This command does not require Git, Python or MCP setup. Use the same command in Windows, macOS and Linux terminals with Node.js and npm/npx installed.

The first run downloads the complete installation package and may take a while. Wait for **`Installed PivotUI ...`** to confirm installation. A spinner stopping or the terminal returning to its prompt does not by itself confirm success. If it fails, keep the displayed error and see [troubleshooting](#npx-troubleshooting).

Choose the Agent you use:

```sh
# Claude Code
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent claude-code --language en
# DSH / DeepSeek Harness
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent dsh --language en
# Cursor
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent cursor --language en
# Another host that supports local SKILL.md packages
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent generic --language en --skills-dir "<your-agent-skills-directory>"
```

Use `--language zh` for Chinese. This selects the authored instructions; upstream packages retain their original language. For `generic`, supply the actual host skills directory. The installer creates its `pivotui/` subdirectory.

### Project scope and user scope

By default, installation is scoped to the current project:

| Agent | Native entry in the project |
| --- | --- |
| Codex / DSH / Cursor | `.agents/skills/pivotui/SKILL.md` |
| Claude Code | `.claude/skills/pivotui/SKILL.md` |
| Generic | `<your-agent-skills-directory>/pivotui/SKILL.md` |

The complete library is kept under `.pivotui/libraries/`. Run from the project root or select it explicitly:

```sh
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent codex --language en --project "<target-project-directory>"
```

<a id="global-install"></a>

For a **global installation shared by your local projects**, add `--global` instead. You can run it from any folder:

```sh
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent codex --language en --global
```

Here, **global means the current user account on this computer**. It does not install for other accounts, remote machines or cloud sessions. For another Agent, replace `codex` with `claude-code`, `dsh` or `cursor`; keep `--global`. Do not combine it with `--project`.

User-wide library storage is `~/.pivotui/libraries/`. Codex and Cursor use `~/.agents/skills/pivotui/`; DSH uses the same shared directory, respecting `DSH_AGENTS_HOME`. Claude Code uses `~/.claude/skills/pivotui/`, respecting `CLAUDE_CONFIG_DIR`. Some hosts read other tools' compatibility directories too; keep one chosen language entry visible to a host.

Official discovery references: [Codex Skills](https://developers.openai.com/codex/skills), [Claude Code Skills](https://code.claude.com/docs/en/skills) and [configuration directory](https://code.claude.com/docs/en/claude-directory.md), [DSH Skills](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md), and [Cursor Skills](https://cursor.com/docs/skills). The [npm package specification](https://docs.npmjs.com/cli/v11/using-npm/package-spec) and [npx reference](https://docs.npmjs.com/cli/v11/commands/npx) describe package URLs and command execution.

### Preview and custom directories

Preview destinations and validate the source without installing files into the project:

```sh
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent codex --language en --dry-run
```

npx may still download its package into the npm cache. Override the library store and/or entry directory when needed:

```sh
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent codex --language en --install-dir "<library-storage-directory>" --skills-dir "<your-agent-skills-directory>"
```

Replace placeholders with real paths and retain quotes around paths with spaces. Keep the complete library available to the Agent. A local install is not automatically available in a remote machine or cloud session.

The installer preserves other skills, project instructions and MCP settings. It checks the full copied edition and refuses to overwrite an unrelated or manually edited entry. Repeating the same installation is supported; switching `--language` updates the selected entry while keeping previous library copies.

<a id="zip-install"></a>

## Option 2: Download a ZIP and copy two folders

For **Codex, DSH or Cursor**, installation means copying **`.agents` and `.pivotui` together into your project folder**. You do not need to run a command.

The **same ZIP also supports global installation**: copy the two folders into your user home folder instead. See [global ZIP installation](#global-zip-install) below.

### Copy the folders

Download one ZIP:

- [PivotUI English project ZIP](https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/PivotUI-English-project-v0.4.0-r2.zip)
- [PivotUI Chinese project ZIP](https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/PivotUI-Chinese-project-v0.4.0-r2.zip)

1. Extract the ZIP. Open the extracted `PivotUI-English` or `PivotUI-Chinese` folder. You will see `.agents`, `.pivotui`, and `INSTALL.md`.
2. Select **both `.agents` and `.pivotui`**, copy them, and paste them into the folder for your project. Copy the whole folders, without opening them or picking out files inside.
3. Open that project in your Agent, start a new chat, and select **pivotui**.

Here is what you should see in your project after copying:

```text
your-project/
├── .agents/
└── .pivotui/
```

**Which folder is my project folder?** It is the outermost folder you open in your Agent. If it already contains `src` or `package.json`, paste the two folders beside them. A new, empty project folder is fine too. Copy the two folders themselves, not the outer `PivotUI-English` or `PivotUI-Chinese` folder.

That completes the file installation. PivotUI is installed for **the project you copied it into**. Keep both folders together when moving the project. You do not need to copy `INSTALL.md` or run anything inside the downloaded ZIP.

If `.agents` and `.pivotui` are not visible in the extracted folder, turn on your file manager's hidden-file display. If your project already has folders with these names, merge their contents and keep its other files. If asked to overwrite a file with the same name, check whether you have changed the existing PivotUI file before replacing it; do not replace the project's entire settings folder.

### If you use Claude Code

1. In the **extracted download**, rename `.agents` to `.claude`.
2. Copy **`.claude` and `.pivotui` together** into your project folder.
3. Open that project in Claude Code, start a new chat, and select **pivotui**.

Rename only the folder in the extracted download, not an existing `.agents` folder in your project. If your project already has `.claude`, merge the downloaded files into it: the PivotUI files go under `.claude/skills/pivotui/`, alongside your other skills and settings. Keep those other files. You do not need to copy another PivotUI entry into `.agents` for Claude Code.

<a id="global-zip-install"></a>

### Install the ZIP globally: copy once for your projects

Use the same ZIP linked above. For **Codex, DSH or Cursor**:

1. Extract the ZIP and open the extracted `PivotUI-English` or `PivotUI-Chinese` folder.
2. Open **your user home folder**. On Windows, open File Explorer, enter `%USERPROFILE%` in its address bar, and press Enter. On macOS or Linux, open your Home folder, written as `~` in paths.
3. Copy **both `.agents` and `.pivotui`** from the extracted download into that home folder. Copy the complete folders, including their contents.
4. Start a new chat in your Agent and select **pivotui**. You can use this copy across your local projects without copying it into each project.

Your home folder should contain:

```text
your-home-folder/
├── .agents/
└── .pivotui/
```

**For Claude Code:** rename `.agents` to `.claude` **in the extracted download**, then copy both `.claude` and `.pivotui` into the same user home folder. Do not rename an existing `.agents` folder in your home folder.

If these destination folders already exist, merge the contents and keep your other skills and settings. Review any same-file overwrite prompt before replacing a PivotUI file you have edited. Put the two folders directly in your home folder, without the outer `PivotUI-English` or `PivotUI-Chinese` wrapper.

**This is global for your current account on this computer.** Other accounts, remote machines and cloud sessions need their own installation. If you customized `CLAUDE_CONFIG_DIR` or `DSH_AGENTS_HOME`, use the [npx `--global` command](#global-install) with the matching Agent instead; it will find that configured skills directory and set the library link correctly.

For other Agents that require a different folder location, use the [custom directory option](#command-install) so the installer can set up the correct file paths.

### Start using PivotUI

Both installation routes expose **one native pivotui entry**, which reads the complete library's **27 module entrypoints** as needed. Select it and describe the interface you want; you do not need to paste setup prompts into project rules. Installation/file checks are distinct from executing a complete host workflow; see [actual verification](VALIDATION.md).

<a id="manual-setup"></a>

## Optional: manual files and MCP

Either installation route above is enough for native Skill use. The following sections are alternatives for hosts that need MCP or raw file access; they are not additional installation requirements.

### Get one edition

The original complete-edition archives remain available: [English ZIP](https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/PivotUI-English-v0.4.0.zip) and [Chinese ZIP](https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/PivotUI-Chinese-v0.4.0.zip). They contain the raw language edition, local MCP server and required package resources. They differ from the project-ready ZIPs above: they do not include a project-level native entry. You can also use `English/` or `Chinese/` in a repository checkout.

- Choose `Chinese/` for Chinese authored instructions, or `English/` for English authored instructions.
- External packages retain their upstream language in both editions.
- Keep the directory structure, `SKILL.md` files, references, scripts, datasets, and license notices together.
- Register only the chosen edition. Both editions use identical skill names; registering both creates duplicate-name ambiguity.

In this guide, **`<edition-root>` means the absolute path to the directory that contains `orchestration/`, `page-design/`, `design-system/`, and `mcp/`**. It is not the repository root, the ZIP file, or the `mcp/` directory. Replace every angle-bracket placeholder with a real path before running a command. The extracted outer folder may be renamed.

### Choose a manual connection method

| Method | Requirements | Best use |
| --- | --- | --- |
| Local MCP | An assistant with local stdio MCP support; Python 3.11+ | Metadata discovery followed by selected instruction/resource reads through three tools |
| Direct file access | An assistant that can read the chosen edition and the target project | Hosts without MCP; instructions are read directly from their actual files |

Both methods use the same skills and routing rules. MCP provides a controlled reader; the connected assistant applies the instructions and performs the work. It does not execute Markdown, start other agents, or call a model API by itself.

## Set up local MCP (optional)

### Install the server dependencies

Open a terminal in `<edition-root>/mcp/skill-cluster`. The server pins `mcp==2.3.0` and `PyYAML==6.0.3` in its `requirements.txt`.

Windows PowerShell:

```powershell
Set-Location "<edition-root>/mcp/skill-cluster"
python -m venv .venv
& ./.venv/Scripts/python.exe -m pip install -r requirements.txt
& ./.venv/Scripts/python.exe -X utf8 server.py --help
```

macOS/Linux:

```sh
cd "<edition-root>/mcp/skill-cluster"
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -X utf8 server.py --help
```

Use the virtual environment's Python executable in the assistant's connection settings. Running another Python executable can produce a missing-module error even after a successful installation.

### Register the connection

Add a **local stdio MCP server** in the host application's settings. Enter these values:

| Setting | Value |
| --- | --- |
| Connection label | `pivotui` |
| Command, Windows | `<edition-root>/mcp/skill-cluster/.venv/Scripts/python.exe` |
| Command, macOS/Linux | `<edition-root>/mcp/skill-cluster/.venv/bin/python` |
| Arguments, in order | `-X`, `utf8`, `<edition-root>/mcp/skill-cluster/server.py` |
| Transport | `stdio` |

For hosts that accept the common `mcpServers` JSON format, a Windows example is:

```json
{
  "mcpServers": {
    "pivotui": {
      "command": "<edition-root>/mcp/skill-cluster/.venv/Scripts/python.exe",
      "args": [
        "-X",
        "utf8",
        "<edition-root>/mcp/skill-cluster/server.py"
      ]
    }
  }
}
```

Replace the `command` with `<edition-root>/mcp/skill-cluster/.venv/bin/python` on macOS/Linux. Forward slashes simplify Windows JSON paths; if you use backslashes, escape them as `\\`. Some hosts use another settings format, so enter the same command and separate arguments in their supported format. Merge the entry into existing settings rather than replacing other server connections.

The server inside an edition discovers that edition by its own location; its working directory does not decide the language. It exposes the protocol server name `design-skill-cluster`; the connection label `pivotui` may be different.

Usually no root argument is needed. To select roots explicitly, append `--skill-root` and an absolute root path to `args`. Repeat the pair only for additional compatible libraries you intend to expose. Once you specify a root, defaults are replaced, not appended. Do not add another copy of a bundled package under the same name.

### Choose your Agent

Use **one** of the following registration methods after installing the dependencies above. All examples use the same edition server. Shell commands quote paths containing spaces; replace every `<edition-root>` before running them.

<a id="codex"></a>

#### Codex

With the Codex CLI installed, register the server:

```sh
# Windows: PowerShell or another shell with codex on PATH
codex mcp add pivotui -- "<edition-root>/mcp/skill-cluster/.venv/Scripts/python.exe" -X utf8 "<edition-root>/mcp/skill-cluster/server.py"

# macOS / Linux
codex mcp add pivotui -- "<edition-root>/mcp/skill-cluster/.venv/bin/python" -X utf8 "<edition-root>/mcp/skill-cluster/server.py"
```

Alternatively, merge this table into `~/.codex/config.toml` (or a trusted project's `.codex/config.toml`). This is useful when configuring the desktop app without the CLI:

```toml
[mcp_servers.pivotui]
command = "<edition-root>/mcp/skill-cluster/.venv/Scripts/python.exe"
args = ["-X", "utf8", "<edition-root>/mcp/skill-cluster/server.py"]
```

Use `<edition-root>/mcp/skill-cluster/.venv/bin/python` for macOS/Linux. Run `codex mcp list` to inspect registration, then reload the client and perform the tool checks below. Append the [entry rule](#entry-rule) to the target project's `AGENTS.md`, preserving its existing instructions. See the official [MCP guide](https://developers.openai.com/codex/mcp) and [AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md).

<a id="claude-code"></a>

#### Claude Code

Register the local server in user scope so it is available across your projects:

```sh
# Windows
claude mcp add --transport stdio --scope user pivotui -- "<edition-root>/mcp/skill-cluster/.venv/Scripts/python.exe" -X utf8 "<edition-root>/mcp/skill-cluster/server.py"

# macOS / Linux
claude mcp add --transport stdio --scope user pivotui -- "<edition-root>/mcp/skill-cluster/.venv/bin/python" -X utf8 "<edition-root>/mcp/skill-cluster/server.py"
```

Run `claude mcp list`, then use `/mcp` inside Claude Code to inspect the connection and perform the tool checks below. Append the [entry rule](#entry-rule) to the target project's `CLAUDE.md`. See the official [MCP guide](https://code.claude.com/docs/en/mcp) and [project memory guide](https://code.claude.com/docs/en/memory).

<a id="deepseek-harness"></a>

#### DSH / DeepSeek Harness

For [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness), use its official `@deepseek-ai/dsh-mcp-client` plugin. It uses a Cordis YAML patch rather than the `mcpServers` JSON format. Save the following as `pivotui.cordis.yml`, replacing the paths:

```yaml
- insert:
    - id: mcp-pivotui
      name: '@deepseek-ai/dsh-mcp-client'
      config:
        serverName: pivotui
        transport: stdio
        command: '<edition-root>/mcp/skill-cluster/.venv/Scripts/python.exe'
        args:
          - '-X'
          - 'utf8'
          - '<edition-root>/mcp/skill-cluster/server.py'
```

On macOS/Linux, use `<edition-root>/mcp/skill-cluster/.venv/bin/python` for `command`. Start the web profile with the patch:

```sh
dsh web --patch "<absolute-path-to-pivotui.cordis.yml>"
```

For persistent setup, merge the insert operation into the web profile's `$DSH_HOME/profiles/web/cordis.patch.yml`; preserve existing operations. Use either persistent configuration or `--patch` for this server, not both. The default home is `~/.dsh`. Append the [entry rule](#entry-rule) to the target project's `AGENTS.md` and use that project as the DSH workspace. The plugin exposes tools such as `mcp__pivotui__catalog_skills`.

DSH is in developer preview; these steps follow its documented plugin interface. See the official [MCP setup](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/guide/mcp-memory.md), [plugin reference](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/mcp/mcp-client/README.md), and [CLI reference](https://github.com/deepseek-ai/deepseek-harness/blob/master/apps/cli/reference/README.md).

<a id="other-agents"></a>

#### Cursor and other Agent tools

For **Cursor**, merge the `mcpServers` JSON example above into the target project's `.cursor/mcp.json` or your user-level `~/.cursor/mcp.json`. Reload the MCP connection and perform the checks below. See the [official Cursor MCP guide](https://cursor.com/docs/mcp).

For another host with **local stdio MCP** support, use the same Python executable and argument list in its supported format. A host that accepts only remote HTTP servers cannot launch this local stdio server directly. If the Agent can read local files, use [direct file access](#direct-files) instead. Save the entry rule in that host's project instructions, or paste it at the beginning of a task.

These are documented configuration routes. The [verification record](VALIDATION.md) reports the checks actually performed; it does not claim that every host has been tested end to end.

### Verify the connection

Reconnect or reload the host's MCP connections. Confirm that these tools are available:

| Tool | Example arguments | Expected result |
| --- | --- | --- |
| `catalog_skills` | `{}` | Metadata for **27 entrypoints** in the complete 0.4.0 edition; no instruction bodies |
| `load_skill` | `{"skill_id":"design-orchestrator"}` | The selected management entry and its linked resource names |
| `read_skill_file` | `{"skill_id":"design-orchestrator","path":"references/scenarios.md","offset":0,"limit":1200}` | The requested slice of that scenario resource |

The 27 entrypoints belong to 23 top-level packages and four nested interaction skills. Tool names may be prefixed by the host's connection name. A saved configuration alone does not prove the connection is active; a successful catalog and selected-file read does.

If you launch `server.py` directly without `--help`, it waits for MCP requests over standard input. It does not open a website or print a graphical menu. Normally the host launches and stops this process.

<a id="direct-files"></a>

## Manual direct file access (optional)

Keep the selected edition in a stable location the assistant can access. Register its package paths using the host's skill mechanism, if supported. Hosts differ in how many directory levels they scan: do not assume that pointing a native skill scanner at `English/` or `Chinese/` will discover all functional categories and nested skills.

When category scanning is unavailable, give the assistant the exact management entry:

```text
<edition-root>/orchestration/design-orchestrator/SKILL.md
```

It can use the edition's `README.md` to locate the selected packages and read only their needed entries and resources. If manual registration is required, register the actual package directories; keep nested interaction entries with their parent package. Copying only `SKILL.md` loses resources and can break relative links. Preserve the complete edition whenever possible.

<a id="entry-rule"></a>

## Entry rule for manual setup

For manual file or MCP setup, put the following instruction in the target project's assistant instructions, or send it at the start of the task. Skip this step when using the installed native **pivotui** Skill. Replace the path for direct-file use:

```text
Use PivotUI for this project's interface work. Start with design-orchestrator.
With MCP, discover catalog metadata, load the management entry, then load only
the selected skills and necessary resources. Without MCP, read
<edition-root>/orchestration/design-orchestrator/SKILL.md and the selected files.
Use only this language edition. Assign one lead per region, preserve the
existing product theme and components, and keep one authoritative token source.
Honor external skills' invocation restrictions. Complete the requested output,
including the relevant interaction, responsive behavior, and verification.
```

For manual setup, this standing instruction directs tasks to the management layer. The native **pivotui** entry created by the installer already contains that routing. Selecting the installed Skill is sufficient; you do not need to add this instruction separately.

## Give tasks in ordinary language

You can now describe the result you want, for example:

```text
Build an operations dashboard using the existing brand and components.
Include a performance overview, a trend chart, and actionable exceptions.
Make the important actions work on narrow screens as well.
```

The management layer can assign the dashboard region to `dashboard-design`, reuse an adequate existing shell and theme, and involve interaction, component, or responsive specialists only for concrete gaps.

Other useful requests:

- “Build an order list with search, filters, selection, and bulk actions; keep the selected filters when returning from an order detail.”
- “Fix this table's mobile overflow while keeping the existing visual design.”
- “Compare three suitable visual directions for this product; give recommendations only.”
- “Use this supplied screenshot as the visual target and implement the page.”
- “Compare the navigation and information grouping of these named product references.”

You can still name a skill directly for a deliberately scoped task. External classics and legacy workflows that require explicit selection retain that rule; automatic routing does not remove their invocation restrictions.

## Optional capabilities

| Capability | What else is needed |
| --- | --- |
| General UI implementation | Access to the target project and its framework/runtime; rendering or browser tools for visual and interaction checks |
| UI/UX Pro Max research | Python 3; its included scripts and datasets use the standard library for local searches |
| Image-design skills | The actual image-generation/image-inspection tools required by the selected upstream entry |
| Stitch workflow | A working Stitch tool connection and an explicitly requested compatible task |
| External frontend workflow | The runtime, assets, framework and verification tools specified by that pinned package |

The MCP reader exposes UTF-8 text resources. It does not execute scripts or serve binary images; those operations use the host's normal file, runtime and media tools. Resolve a selected package's actual location before running its scripts. Keep image output, a design document and implemented code distinct when requesting a deliverable.

<a id="legacy-python"></a>

## Legacy Python installer

The earlier Python installer remains available for an existing repository checkout. It requires Python 3.11+ and the complete checkout; it is not required for npx or ZIP installation:

```sh
python scripts/install.py --agent codex --language en
```

Use `python3` on macOS/Linux. This older installer defaults to user-wide directories, unlike the project-scoped npx default. Keep its previous `--skills-dir` and `--install-dir` values when maintaining an existing installation. For new installations, use either main route above.

<a id="npx-troubleshooting"></a>

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| npx only shows a spinner | It may still be downloading. Wait for `Installed PivotUI ...`; use the verbose command below if you need to retry and capture details |
| npx exits with code `128` | Keep the full error and log; the number alone does not identify the cause. If you used the older GitHub-source command, retry with the release-package command above |
| Native `pivotui` entry is missing | Start a new session; check the printed entry path and the host's actual skills directory; use `--skills-dir` for a custom location |
| Installer reports an edited entry | Preserve your edits before reinstalling; it will not overwrite a customized `SKILL.md` |
| `ModuleNotFoundError` with MCP | The configured executable must be the virtual environment where `requirements.txt` was installed |
| Server cannot start | Use absolute paths; quote spaces in shell commands; keep each MCP argument separate |
| Empty catalog | The selected root must contain packages or functional category folders; check any explicit `--skill-root` |
| Duplicate or ambiguous skill name | Remove the second edition/duplicate library, or choose an exact catalog `id` intentionally |
| Missing reference file | Restore the full package and its layout; do not move a nested entry away from its parent |
| Instructions are truncated | Continue `read_skill_file` using returned `next_offset`; restart if `revision` changes |
| Host tries to load everything | Add the standing instruction above; discover metadata first and read only selected entries/resources |
| Instructions load but images/code do not appear | Check the requested deliverable and the host's actual image, file-editing, runtime or browser capabilities |

When retrying a failed download, this command prints more detail. Keep any Agent, language or destination options you need. npm's `--loglevel=verbose` and `--timing` options must come **before `--package`**:

```sh
npx --yes --loglevel=verbose --timing --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent codex --language en
```

Verbose output shows requests and stages, not necessarily a live download percentage. There is no need to interrupt a download that is still progressing just to add logging.

The older GitHub-source command remains available as an alternative. It **requires Git** and may fetch the repository more than once, so prefer the release-package command above:

```sh
npx --yes github:Getaway-Wuji/PivotUI --agent codex --language en
```

## Updating

For npx installations, use the latest release-package command from this guide, keeping the same Agent, language and scope. Preserve any `--project`, `--global`, `--install-dir` or `--skills-dir` choices. The current package is:

```sh
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent codex --language en
```

The URL selects a specific published package; repeating an older URL does not fetch a newer release. The installer verifies the selected package and updates its managed entry while retaining previous library copies. An edited entry or a conflicting existing target library is reported rather than silently overwritten.

For project-ready ZIP installations, download the newer project ZIP and merge its complete library and chosen native entry into the same locations. Review any local PivotUI edits first, and retain other skills and project settings. For legacy Python installs, update the checkout and rerun the older command with the same destinations.

For raw-file/MCP installations, download a complete newer edition and review its release notes and notices. Replace the selected edition as a unit, recreate its virtual environment if the path or dependencies change, update the host's absolute launch paths, and repeat the catalog/selected-file checks. Keep product-specific tokens and design decisions in the target project. The [architecture guide](ARCHITECTURE.en.md) explains how responsibility and shared decisions are coordinated.
