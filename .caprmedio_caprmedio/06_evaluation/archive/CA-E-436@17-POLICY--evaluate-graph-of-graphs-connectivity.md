---
cce_version: cce_1
cce_form: evaluation
version: 17
updated_at: 2026-10-24 21:35:46 +0400
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-R-1407
  - CA-R-007
subjects:
  governs: Project/Graph of Graphs/connectivity
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - Graph of Graphs
  - Subject/Domain/Node/Continuant/Term//Artifact
  - Subject/Engineering/Implementation Binding
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Engineering/Framework Instance
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-436@17
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Policy
tier: 2
---
# Evaluate graph-of-graphs connectivity

the Graph of Graphs connectivity Evaluation **must** return `fail` **if** a governed Artifact **or** delivered Implementation element has no recoverable location **or** no valid connection **to** the shared connected whole; a connection **may** cross graph boundaries, **and** specialized Methodology, Engine, **or** other Scope Unit checks **may** supply evidence **to** this Evaluation. apply cycle restrictions **only** **to** graph families whose authority requires them; connectivity **must not** impose universal acyclicity.
