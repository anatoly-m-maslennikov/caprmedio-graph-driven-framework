---
subjects:
  governs: Governed Change/File Identity
  depends_on:
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
version: 20
updated_at: 2026-10-25 17:32:27 +0400
relations:
  evaluation_for:
  - CA-R-802
  - CA-M-087
  - CA-R-805
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-182@20
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 3
---
# Reject multiple file identities

## Claim checked

a request for one atomic file action **must not** implicitly choose **or** combine multiple independently governed file identities. this restriction does **not** prohibit an explicitly sealed folder **or** bulk action admitted by CA-M-087 **and** CA-R-805.

## Test cases

- supply an atomic-file trigger whose candidates resolve **to** two independently governed file identities **without** an explicitly sealed folder **or** bulk target set.
- include a separately admitted folder **or** bulk action with a frozen ordered target set as a control, satisfying the same authorization **and** frontier gates required by its governing authority.

## Acceptance criteria

- the ambiguous atomic-file request returns the deterministic multiple-identities diagnostic **before** staging **or** committing **any** change; no target is selected implicitly.
- the admitted frozen-set control does **not** fail solely because its set **contains** multiple files. no member **may** be added, omitted **or** regrouped by inference.
- this membership check does **not** itself authorize either action **or** bypass effect-boundary revalidation.

## Failure disposition

reject implicit selection **or** aggregation, rejection of an **otherwise** admitted frozen-set action solely for file count, an altered sealed target set **or** an unauthorized Git effect.
