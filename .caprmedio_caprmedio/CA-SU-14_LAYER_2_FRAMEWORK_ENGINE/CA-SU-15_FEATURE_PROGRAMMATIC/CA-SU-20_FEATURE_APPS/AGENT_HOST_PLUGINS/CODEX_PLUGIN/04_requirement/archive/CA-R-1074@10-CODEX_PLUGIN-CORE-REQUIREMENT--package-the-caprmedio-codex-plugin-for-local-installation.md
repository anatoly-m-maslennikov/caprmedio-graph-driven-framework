---
subjects:
  governs: plugin-packaging
  depends_on: []
version: 10
updated_at: 2026-10-23 03:17:34 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1074@10
status: Archived
---
# Package the CAPRMEDIO Codex plugin for local installation

`CODEX_PLUGIN` **must** be one versioned installable package with a stable kebab-case identity, a required `.codex-plugin/plugin.json` manifest, contained relative references **to** **every** bundled skill **and** optional MCP, UI, asset, **or** hook resource, **and** one repository-local marketplace entry through which Codex can discover **and** install the package. Credentials **and** mutable runtime state **must** remain outside the package, **every** declared resource **must** resolve **after** installation, **and** the advertised identity, version, description, **and** capabilities **must** match the packaged content.
