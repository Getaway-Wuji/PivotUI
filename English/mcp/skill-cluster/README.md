# PivotUI MCP

A local, read-only MCP server using the official Python SDK 2.3.0. It exposes skill metadata and selected instruction files. The connected AI chooses the relevant skills, applies their rules, and performs the user's design or implementation task. The server does not call a model API, execute skill scripts, preload every skill body, or install external skills.

## Choose one language distribution

Use either the complete `English` distribution or the complete `Chinese` distribution. Both use the same skill names and standard `SKILL.md` entrypoints. Register one language root per cluster connection; adding both makes identical names ambiguous and does not provide automatic translation.

A server inside a distribution reads functional categories, for example `English/page-design/dashboard-design/SKILL.md`. Authored and upstream skills share categories; the edition README records their origins and availability. A release can be extracted under a different folder name. These defaults are relative to the server file, not the current working directory.

Bundled external packages need no additional root. Do not register a second copy of a bundled skill with the same name.

Language selection changes which instructions are available. Skill bodies and references are still loaded only when the task needs them. External skills retain their upstream language.

## Install and start

Requires Python 3.11 or later. In this directory, create a virtual environment, install the pinned requirements, and start the server with that environment's Python.

Windows PowerShell:

```powershell
python -m venv .venv
& ./.venv/Scripts/python.exe -m pip install -r requirements.txt
& ./.venv/Scripts/python.exe -X utf8 server.py
```

macOS/Linux:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -X utf8 server.py
```

In later examples, `python` means the virtual environment's executable. To select explicit roots or add an installed external library, repeat `--skill-root`. Once any root is specified, only the specified roots are used; defaults are not appended.

```text
python server.py --skill-root <selected-language-directory> --skill-root <installed-external-library>
```

The server discovers packages directly under a root or one functional category level below it, plus nested `sub-skills` within those packages. Shared documents and nested support examples are not registered as skills. An upstream package added beside an authored package uses the same discovery mechanism; the README source label does not change routing. Each operation refreshes metadata, so adding or editing a skill does not require restarting the server. A folder may differ from the YAML `name`. If several entries have the same name, select an exact catalog `id`.

Overlapping roots register the same resolved entrypoint once, retaining its first catalog id and the outermost skill-package boundary discovered within the configured roots. Registering only a nested entry's directory does not grant access to its unconfigured parent package. Separate filesystem copies remain distinct entries even when their contents match.

## Three fixed tools

| Tool | Input | Result |
| --- | --- | --- |
| `catalog_skills` | Optional metadata filter `query` | Names, descriptions, ids, aliases, categories, and upstream implicit-invocation flags; no skill bodies |
| `load_skill` | `skill_id`: name, alias, or exact id | One selected entrypoint and the filenames it directly links |
| `read_skill_file` | `skill_id`, relative `path`, optional `offset` and `limit` | A character slice of one UTF-8 text file within the selected package |

A response contains at most 12,000 content characters; a file may be at most 2 MiB. Long files return `truncated`, `next_offset`, and `revision`. Continue from the returned offset. If the revision changes between pages, restart the read to avoid combining versions.

These tools are stateless reads, not a session cache. Repeated calls read fresh content. The host AI should reuse entries and resources already available in the task context, rereading when needed to obtain missing content or verify changes.

A nested skill can read shared references in its top-level package, such as `../../references/rules.md`. Absolute paths, paths or symbolic links escaping that package, and binary resources are rejected. Resource contents are returned as text and never executed.

Aliases: `taste-skill` → `design-taste-frontend`; `dashboard-skill` → `dashboard-design`; `interaction-skill` → `interaction-design`; `floating-component-skill` → `floating-components`. `global-style-skill` uses its own name. The taste folder alias selects the same entry, not another skill. An alias does not imply that its target is installed. Historical `redesign-existing-projects` is not silently aliased to the current taste workflow.

## Connect an MCP host

Add a local stdio MCP connection named `pivotui` in your assistant's settings. Use the virtual environment's **absolute Python executable path**, with three separate arguments: `-X`, `utf8`, and the **absolute path to this `server.py`**. The placeholder paths below must be replaced before use. The server inside the chosen edition uses that edition's default roots.

For hosts supporting the common `mcpServers` JSON format:

```json
{
  "mcpServers": {
    "pivotui": {
      "command": "<virtual-environment Python executable>",
      "args": ["-X", "utf8", "<edition-root>/mcp/skill-cluster/server.py"]
    }
  }
}
```

On Windows, the executable normally ends in `.venv/Scripts/python.exe`; on macOS/Linux, `.venv/bin/python`. Use forward slashes or escaped backslashes in JSON paths. Other hosts may use a different settings format: enter the same command and separate arguments there. Merge the entry into existing settings without replacing other connections.

For explicit roots, append `"--skill-root", "<selected skill root>"` pairs to `args`. The AI first discovers metadata, then loads only the entries and resources needed for the current task. A saved configuration does not establish that the connection is active; verify it through the host. The protocol server name remains `design-skill-cluster` and can differ from the connection label.

When run directly, the server waits for MCP requests over standard input. It does not open a website. Normally the host launches and stops it. To check command-line availability without waiting for a connection, run `python -X utf8 server.py --help` using the virtual environment.

## Make routing the default

Add this standing instruction to the target project's assistant rules:

```text
Use PivotUI for interface work. Start with design-orchestrator, discover metadata,
then load only selected skills and needed resources. Use one language edition.
Assign one lead per region and reuse the product's authoritative tokens and
components. Honor external invocation restrictions and complete the requested
output, including applicable behavior, responsive layout and verification.
```

Connecting the catalog alone does not guarantee every host will choose the management entry automatically. This instruction gives the host a default entry. Its AI performs the work; the server only reads selected instructions.

## Verify the installed connection

After connecting, call these tools in order:

1. `catalog_skills` with `{}`: the complete 0.4.0 edition returns **27 entrypoints** across 23 top-level packages and four nested interaction skills. Catalog output contains metadata, not skill bodies.
2. `load_skill` with `{"skill_id":"design-orchestrator"}`: inspect the selected management entry.
3. `read_skill_file` with `{"skill_id":"design-orchestrator","path":"references/scenarios.md","offset":0,"limit":1200}`: inspect a selected resource slice.

Host interfaces may prefix tool names with their connection name. If names are ambiguous, remove duplicated language roots or use an exact catalog id deliberately. If text is truncated, follow `next_offset` and check `revision` as described above. Local authoring tests are not required for installation and are excluded from the public distribution. Virtual environments and caches also stay local.

The reader returns text resources; scripts and binary images require the host's own runtime or media capabilities. A working catalog does not prove every external image, browser or design workflow is available.

Implementation references: [official Python SDK](https://py.sdk.modelcontextprotocol.io/), [client API](https://py.sdk.modelcontextprotocol.io/client/), and [stdio operation](https://py.sdk.modelcontextprotocol.io/run/).
