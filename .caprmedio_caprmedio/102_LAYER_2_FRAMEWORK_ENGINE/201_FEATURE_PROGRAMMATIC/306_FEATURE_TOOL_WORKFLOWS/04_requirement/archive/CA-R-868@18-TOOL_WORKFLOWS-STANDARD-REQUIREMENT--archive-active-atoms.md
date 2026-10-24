---
atom_id: CA-R-868@18
content_role: Requirement
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Tool//ATOM_ARCHIVE
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Version Number
  - Subject/Engineering/Carrier
  - Atom/Revision/Status
  - Atom/Revision/Updated At
version: 18
updated_at: 2026-10-24 00:51:05 +0400
relations:
  relates_to:
  - CA-O-029
  - CA-E-306
  - CA-R-1521
  - CA-R-1788
  - CA-D-289
  - CA-D-303
tier: 3
---
# Summary

Archive active Atoms

## Scope

The ATOM_ARCHIVE shortcut withdrawing exact selected active Markdown Atom authority under the Atom's applicable qualified status model and transition rules.

## Claim

the ATOM_ARCHIVE Tool **must** provide withdrawal of active Markdown Atom authority while preserving its historical evidence:

- preserve governed meaning, complete body, Summary, stable Atom ID, Type, prior Revision history, resolvable historical dependents **and** all other properties except the admitted lifecycle Status, Version **and** actual Updated At changes. resolve the archive transition from the actual Atom Content Role/Type's applicable status model under CA-R-1521; set its admitted archival Status, advance Version by **`=1`** for the actual changed Atom and refresh actual Updated At under CA-R-1788. Preserve the exact before-Revision bytes and Version in required history; a no-op does not change Version or Updated At. exclude the withdrawn Revision from current authority; archival is **not** promotion, upgrade **or** a semantic Revision.
- use the applicable archive Carrier encoding **and** placement under CA-D-289 **and** CA-D-303. unchanged meaning **and** identity do **not** require retaining the active filename; the whole Carrier transition remains atomic.
- reject Drafts, already archived Atoms, non-Atom Markdown, missing **or** unsupported status/transition models, invalid destinations, **and** collisions **before** applying a complete validated selection. do **not** invent a universal lifecycle for other Entity **or** Artifact kinds.
- archive **`=1`** explicit Atom target per Action with its expected Revision or digest. Preserve that Action's admitted whole-Carrier transition and verified source/destination restoration safeguards. A several-Atom Workflow stops at its first failed Action, retains completed archives and leaves the remainder untouched; do not restore earlier completed Atom Actions.
- default **to** a mutation-free dry run. accept `--apply` **only** through authorized Project-local MCP delegation with a sealed Initiative action envelope.

Atom deletion is not admitted. Retirement or archival **must** follow the applicable lifecycle model and preserve required history. General file cleanup is a separate operation. Resume and retry policy for a several-Atom sequence is deferred.

the operational Action is CA-O-029. CA-E-306 supplies the automated conformance cases for this capability; the Tool Requirement does **not** duplicate their procedure.

## Details
