# Install and use PivotUI

[中文](INSTALL.zh-CN.md) · [Project overview](../README.en.md) · [Skill guide](SKILLS.en.md)

Choose **one complete edition** and connect it to an AI assistant that can read local files or use local MCP tools. After the initial setup, give the assistant the design task. PivotUI's `design-orchestrator` chooses the relevant skills; you do not need to select a list of skills for every request.

Jump to your tool: [Codex](#codex) · [Claude Code](#claude-code) · [DSH / DeepSeek Harness](#deepseek-harness) · [Cursor and other Agents](#other-agents).

For a first task without MCP, extract an edition and paste the [starter prompt](../prompts/pivotui-starter.en.txt), replacing its directory and task placeholders. The Agent must be able to read that directory. For ongoing use, follow the setup below and save the [entry rule](#entry-rule).

## 1. Get one edition

Download the Chinese or English archive from [Releases](https://github.com/Getaway-Wuji/PivotUI/releases/latest), or clone this repository and use its `Chinese/` or `English/` directory. The archives contain complete editions, including their local MCP server and required package resources.

- Choose `Chinese/` for Chinese authored instructions, or `English/` for English authored instructions.
- External packages retain their upstream language in both editions.
- Keep the directory structure, `SKILL.md` files, references, scripts, datasets, and license notices together.
- Register only the chosen edition. Both editions use identical skill names; registering both creates duplicate-name ambiguity.

In this guide, **`<edition-root>` means the absolute path to the directory that contains `orchestration/`, `page-design/`, `design-system/`, and `mcp/`**. It is not the repository root, the ZIP file, or the `mcp/` directory. Replace every angle-bracket placeholder with a real path before running a command. The extracted outer folder may be renamed.

## 2. Choose a connection method

| Method | Requirements | Best use |
| --- | --- | --- |
| Local MCP | An assistant with local stdio MCP support; Python 3.11+ | Metadata discovery followed by selected instruction/resource reads through three tools |
| Direct file access | An assistant that can read the chosen edition and the target project | Hosts without MCP; instructions are read directly from their actual files |

Both methods use the same skills and routing rules. MCP provides a controlled reader; the connected assistant applies the instructions and performs the work. It does not execute Markdown, start other agents, or call a model API by itself.

## 3A. Set up local MCP

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

## 3B. Set up direct file access

Keep the selected edition in a stable location the assistant can access. Register its package paths using the host's skill mechanism, if supported. Hosts differ in how many directory levels they scan: do not assume that pointing a native skill scanner at `English/` or `Chinese/` will discover all functional categories and nested skills.

When category scanning is unavailable, give the assistant the exact management entry:

```text
<edition-root>/orchestration/design-orchestrator/SKILL.md
```

It can use the edition's `README.md` to locate the selected packages and read only their needed entries and resources. If manual registration is required, register the actual package directories; keep nested interaction entries with their parent package. Copying only `SKILL.md` loses resources and can break relative links. Preserve the complete edition whenever possible.

<a id="entry-rule"></a>

## 4. Make the management layer the default entry

Put the following instruction in the target project's assistant instructions, or send it at the start of the task. Replace the path for direct-file use:

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

This small standing instruction is what makes ordinary task requests enter the management layer. Installing files or connecting a catalog does not, by itself, guarantee that every host will select the orchestrator for every UI request.

## 5. Give tasks in ordinary language

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

## 6. Optional capabilities

| Capability | What else is needed |
| --- | --- |
| General UI implementation | Access to the target project and its framework/runtime; rendering or browser tools for visual and interaction checks |
| UI/UX Pro Max research | Python 3; its included scripts and datasets use the standard library for local searches |
| Image-design skills | The actual image-generation/image-inspection tools required by the selected upstream entry |
| Stitch workflow | A working Stitch tool connection and an explicitly requested compatible task |
| External frontend workflow | The runtime, assets, framework and verification tools specified by that pinned package |

The MCP reader exposes UTF-8 text resources. It does not execute scripts or serve binary images; those operations use the host's normal file, runtime and media tools. Resolve a selected package's actual location before running its scripts. Keep image output, a design document and implemented code distinct when requesting a deliverable.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| `ModuleNotFoundError` | The configured executable must be the virtual environment where `requirements.txt` was installed |
| Server cannot start | Use absolute paths; quote spaces in shell commands; keep each MCP argument separate |
| Empty catalog | The selected root must contain packages or functional category folders; check any explicit `--skill-root` |
| Duplicate or ambiguous skill name | Remove the second edition/duplicate library, or choose an exact catalog `id` intentionally |
| Missing reference file | Restore the full package and its layout; do not move a nested entry away from its parent |
| Instructions are truncated | Continue `read_skill_file` using returned `next_offset`; restart if `revision` changes |
| Host tries to load everything | Add the standing instruction above; discover metadata first and read only selected entries/resources |
| Instructions load but images/code do not appear | Check the requested deliverable and the host's actual image, file-editing, runtime or browser capabilities |

## Updating

Download a complete newer edition and review its release notes and notices. Replace the selected edition as a unit, recreate its virtual environment if the path or dependencies change, update the host's absolute launch paths, and repeat the catalog/selected-file checks. Keep product-specific tokens and design decisions in the target project so a library update does not replace them. The [architecture guide](ARCHITECTURE.en.md) explains how responsibility and shared decisions are coordinated.
