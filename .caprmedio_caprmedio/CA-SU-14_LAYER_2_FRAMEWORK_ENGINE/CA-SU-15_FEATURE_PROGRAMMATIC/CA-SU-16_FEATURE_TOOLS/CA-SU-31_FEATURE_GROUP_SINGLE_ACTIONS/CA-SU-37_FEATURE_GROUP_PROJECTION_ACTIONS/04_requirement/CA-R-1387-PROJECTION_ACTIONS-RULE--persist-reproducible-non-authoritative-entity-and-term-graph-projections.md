---
atom_id: CA-R-1387
ref_id: CA-R-1387
container:
  scope_unit: CA-SU-37
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
tier: 1
status: Active
version: 21
updated_at: 2026-11-03 23:17:14 +0400
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROJECTION_ACTIONS
claim_target_scope_unit: PROJECTION_ACTIONS
---
# Persist reproducible non-authoritative Entity and Term graph Projections

`GENERATE_ENTITY_GRAPH` **must** accept one explicitly selected folder **or** equivalent source frontier **and** derive one reproducible, non-authoritative Projection. The result **must** contain **every** declared Term found **in** the parseable frontier; each Term's direct parent **when** declared; the direct dependency graph; the complete dependency-Term closure; cycles **and** relation-cardinality violations; source Carrier path **and** digest lineage; unknown **or** unparseable regions; the selected frontier identity; **and** an explicit non-authoritative status.

Identical readable source bytes **and** settings **must** produce byte-identical semantic output **in** stable order. Unknown **or** unparseable regions remain visible **and** **must not** be silently omitted, repaired, **or** interpreted as absence. A cycle **or** cardinality violation is reported as projection data **and** a failed validation disposition, never repaired by changing authority.

Description **and** ordinary generation are mutation-free. Persistence occurs **only** **when** the caller supplies an explicit output path **or** a registered Project setting resolves one unambiguous Projection destination. One output Carrier represents exactly one source frontier **and** is replaced atomically. The Tool **must** reject destinations inside governed Atom **or** Journal authority, path traversal, symlink escape, ambiguous configured destinations, **and** **any** request that would make the Projection authoritative.

the persisted Projection is suitable for strictly read-only consumption by `WORKBENCH` and optional presentation by `GRAPH_UI`, but it has no authority of its own: current Atoms, Journals, authoritative Settings Artifacts, **and** **any** other authority admitted by the applicable methodology remain authoritative independently of the Projection.
