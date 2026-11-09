---
atom_id: CA-R-1120
ref_id: CA-R-1120
container:
  scope_unit: CA-SU-16
role: Requirement
form: Rule
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data Validation"
tier: 1
status: Active
version: 21
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Reconcile Git and Journal provenance in both directions

the Toolset **must** provide deterministic, idempotent reconciliation **in** both directions between real-change Git commits **and** canonical Journal events. it **must** identify a Git commit **without** its expected Journal event, a Journal event whose bound real-change commit is absent **or** unreachable, duplicate action **or** event bindings, mismatched subject revisions **or** digests, **and** Journal-only commit watermark lag.

reconciliation **may** append missing evidence **only** **when** it can derive that evidence from sealed durable action state **and** reachable repository history **without** invention. **otherwise** it **must** preserve the discrepancy as explicit blocked state for operator resolution. a reconciled action **must** expose its action identity, Initiative, real-change commit SHA, Journal event identity, affected subject identity **and** revision **or** digest, **and** Journal-batch commit SHA.
