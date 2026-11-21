# Component System 1.0.1

This is a complete standalone English edition of the component-system skill. The matching Chinese edition uses the same identifiers, structure and behavior. Choose one language edition per installation or MCP connection.

| Package | Origin | Author/source | Version | Distribution contents |
| --- | --- | --- | --- | --- |
| `component-system` | internal | This design skill cluster; reference attribution is in the skill's source map | 1.0.1 | Original guidance; no third-party component source or assets included |

## Use

Open the skill's `SKILL.md` for a component task, or let an existing `design-orchestrator` select `component-system` from metadata. The skill works without the rest of the cluster. Its relative references contain the necessary shared conventions and conditional guidance. No authoring archive, fixed component framework or external account is required.

Install the whole `component-system` directory in the host's declared skill root. Retain its references and `agents/openai.yaml`. In a full edition, this package sits under `components/`. For a local MCP connection, the standalone archive also includes the existing skill-cluster server and its usage guide under the edition's `mcp/skill-cluster/` directory. Its default discovery root is that language root. Follow that guide to create an environment and install its declared requirements; no local launch configuration or environment is bundled. Reading MCP output supplies rules, not executed implementation.

## Contents and evidence

- A concise entry, UI metadata, and six references covering contracts, families, directions, sources, shared conventions, and integration/validation.
- Three illustrative contract examples in the contracts reference. They are specifications, not executable component templates.
- Original guidance synthesized from supplied references and Foundations/Orchestration 0.2. Third-party component code, screenshots, full research, caches and personal paths are excluded.

This module package does not republish or change the full skill cluster. The existing orchestrator already names this capability; discover the actual entry before using it. Full-cluster release/version/baseline updates are a separate integration step. External pages may change; check the actual installed version and applicable license when adopting implementation code. The skill's `references/source-map.md` states research limits. Runtime and product accessibility must be checked in the target implementation.
