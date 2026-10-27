---
atom_id: CA-R-868
content_role: Requirement
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.Version Number
  - Subject/Graph Node/Carrier
  - Subject/Graph Node/Domain/Continuant/Atom.Status
  - Subject/Graph Node/Domain/Continuant/Atom.Updated At
version: 28
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
tier: 3
type: Rule
---
# Summary

Archive active Atoms

## Scope

The ATOM_ARCHIVE shortcut withdrawing exact selected active Markdown Atom authority under the Atom's applicable qualified status model and transition rules.

## Claim

the ATOM_ARCHIVE Tool **must** provide withdrawal of active Markdown Atom authority while preserving its historical evidence:

- preserve governed meaning, complete body, Summary, stable Atom ID, Type, prior history, resolvable historical dependents **and** all other properties except the representation's admitted lifecycle Status, version-qualified identity and Carrier location. resolve the archive transition from the actual Atom Content Role/Type's applicable status model under CA-R-1521; write the archived representation with Status `Archived`, identity `Atom ID@N`, the predecessor's numeric Version `N` and its prior Updated At. Standalone archival does not create a new Version or refresh Updated At. When a real Atom update also archives a predecessor, the predecessor keeps its Version and Updated At and the published successor receives the next Version and actual edit time. exclude the archived version from current authority; archival is **not** promotion, upgrade **or** a semantic content update.
- use the applicable archive Carrier encoding **and** placement under CA-D-289 **and** CA-D-303. The archive filename and location use the version-qualified identity `Atom ID@N` and the admitted archive placement. unchanged meaning **and** identity do **not** require retaining the active filename; the whole Carrier transition remains atomic.
- reject Drafts, already archived Atoms, non-Atom Markdown, missing **or** unsupported status/transition models, invalid destinations, **and** collisions **before** applying a complete validated selection. do **not** invent a universal lifecycle for other Entity **or** Artifact kinds.
- archive **`=1`** explicit Atom target per Action with its expected Version or digest. Preserve that Action's admitted whole-Carrier transition and verified source/destination restoration safeguards. A several-Atom Workflow stops at its first failed Action, retains completed archives and leaves the remainder untouched; do not restore earlier completed Atom Actions.
- default **to** a mutation-free dry run. accept `--apply` **only** through authorized Project-local MCP delegation with a sealed Initiative action envelope.

Atom deletion is not admitted. Retirement or archival **must** follow the applicable lifecycle model and preserve required history. General file cleanup is a separate operation. Resume and retry policy for a several-Atom sequence is deferred.

the operational Action is CA-O-029. CA-E-306 supplies the automated conformance cases for this capability; the Tool Requirement does **not** duplicate their procedure.

## Details
