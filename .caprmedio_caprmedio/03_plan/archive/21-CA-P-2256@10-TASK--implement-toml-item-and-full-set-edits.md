---
atom_id: CA-P-2256@10
content_role: Plan
type: Plan
label: Task
work_sequence_number: 21
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Action
  - Workflow
  - Configuration
  - Revision
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 10
updated_at: 2026-10-24 07:52:46 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
  blocks:
  - CA-P-2266
  - CA-P-2267
  - CA-P-2269
  - CA-P-2275
tier: 3
---
# Summary

Implement TOML item and full-set edits

## Objective

Maintain the bounded private TOML connector for item/value and full-set add/replace/remove edits, with receiving-schema and publication boundaries explicit.

## Details

The private preserving materializer and writer integration are complete in the bounded [CA-P-2307 selection packet](21-CA-P-2256@10-TASK--implement-toml-item-and-full-set-edits/done/02-CA-P-2307-TASK--select-tomlkit-for-preserving-configuration-text.md), [CA-P-2308](21-CA-P-2256@10-TASK--implement-toml-item-and-full-set-edits/done/03-CA-P-2308-TASK--preserve-toml-text-during-pure-edits.md), [CA-P-2309](21-CA-P-2256@10-TASK--implement-toml-item-and-full-set-edits/done/04-CA-P-2309-TASK--verify-toml-text-preservation-independently.md) and [CA-P-2310](21-CA-P-2256@10-TASK--implement-toml-item-and-full-set-edits/done/05-CA-P-2310-TASK--integrate-preserving-toml-materialization.md). TOMLKit 0.15.1 is the selected dependency for that private path. These results do not establish receiving-schema, live-write, runtime or publication acceptance.

[CA-P-2297 — Bind TOML modifications to receiving schemas](21-CA-P-2256@10-TASK--implement-toml-item-and-full-set-edits/01-CA-P-2297-TASK--bind-toml-modifications-to-receiving-schemas.md) remains Active and owns the distinct receiving/currentness/permission/effect work. Candidate #7 methodology edits are independent of this Tool backlog. Existing Done children remain Done; no status cascade is inferred.

### Decomposition

- [CA-P-2297 — Bind TOML modifications to receiving schemas](21-CA-P-2256@10-TASK--implement-toml-item-and-full-set-edits/01-CA-P-2297-TASK--bind-toml-modifications-to-receiving-schemas.md)
- [CA-P-2307 — Select TOMLKit for preserving configuration text](21-CA-P-2256@10-TASK--implement-toml-item-and-full-set-edits/done/02-CA-P-2307-TASK--select-tomlkit-for-preserving-configuration-text.md)
- [CA-P-2308 — Preserve TOML text during pure edits](21-CA-P-2256@10-TASK--implement-toml-item-and-full-set-edits/done/03-CA-P-2308-TASK--preserve-toml-text-during-pure-edits.md)
- [CA-P-2309 — Verify TOML text preservation independently](21-CA-P-2256@10-TASK--implement-toml-item-and-full-set-edits/done/04-CA-P-2309-TASK--verify-toml-text-preservation-independently.md)
- [CA-P-2310 — Integrate preserving TOML materialization](21-CA-P-2256@10-TASK--implement-toml-item-and-full-set-edits/done/05-CA-P-2310-TASK--integrate-preserving-toml-materialization.md)

### Definition of Done

Keep this Plan Active until the private connector and CA-P-2297 receiving outcome have current source/implementation pins, focused valid/refusal/no-op/error/effect checks and independent review. No dependency selection or private integration result alone authorizes live configuration writes, runtime activation, migration or publication.
