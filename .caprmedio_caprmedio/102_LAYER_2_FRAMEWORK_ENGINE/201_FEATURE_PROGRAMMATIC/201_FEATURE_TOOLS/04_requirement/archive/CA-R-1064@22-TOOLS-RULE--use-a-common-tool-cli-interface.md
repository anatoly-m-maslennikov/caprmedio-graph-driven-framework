---
subjects:
  governs: Subject/Graph Node/Engineering/Architecture/Communication
  depends_on: []
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 22
updated_at: 2026-10-27 06:04:45 +0400
atom_id: CA-R-1064@22
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
tier: 1
---
# Use a common Tool CLI interface

**every** Tool **must** expose the same machine-readable CLI contract for Tool kind, capability identity, help, input schema, result envelope, diagnostics, **and** exit status. **every** Finder, including **every** Checker, **must** be strictly read-only with respect **to** governed Atoms **and** Journals; **every** Doer **must** support a dry-run mode that returns its resolved targets, complete planned effects, **and** validation results **without** mutation.
