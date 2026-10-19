---
atom_id: CA-O-100
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Method Lesson Drafting"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Object/Atom/Content Role: Method", "Entity/Continuant/Object/Atom/Content Role: Evaluation", "Implementation", "Atom/Content Role: Plan/Type: Plan", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/Actor/Type: AI Agent"]
version: 6
updated_at: "2026-10-18 07:47:46 +0400"
relations:
  relates_to:
    - CA-O-090
    - CA-R-1559
    - CA-R-1591
    - CA-M-002
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-100-PROJECT_CONFIGURATION-ACTION--draft-methods-from-verified-implementation-issues.md
  source_atom_id: CA-O-100
  source_atom_revision: 6
  source_sha256: fce0b6a3f865fefa7d304094535ef7a11fa3c141e424408a3f94c431f09f6aec
  original_relations_sha256: b2489f323a77e636b921e72f37bc2992e015b00afb6db114252392e02cf825d6
---
# Summary

Draft Methods from verified implementation issues

## Operation

Method Lesson Drafting **means** the Agentic Action that derives a bounded Standard Method Draft from a verified implementation issue **in** a separately admitted learning Run.

- inputs: an explicit learning request, bounded P/Plan work, retained admitted Evaluation-portfolio results, relevant focused-regression results, reproducible failure, diagnosis, actual fix, passing regression evidence, current governing Method/RED authority, existing related Drafts, **and** confidence/permission gates.
- require sufficient evidence that the proposed correction explains the defect **and** that relevant checks pass on the fixed candidate. an initial test failing because behavior is not implemented yet is **not** a Method lesson; uncertain **or** stale evidence returns `blocked`.
- check existing Methods **and** pending Drafts before writing. return `already_covered` with their references **when** no distinct Method is needed; repeated failures **must not** create duplicate lessons.
- **when** a missing Method is justified **and** authoring is admitted, create **or** refine the applicable Standard Draft with **=1** Claim, its precise governed Entity, correct Scope Unit, actual Author, structured content, **and** linked evidence. preserve Summary identity rules **and** keep Drafts without assigned Atom IDs.
- return `drafted` with the Draft references **and** evidence for separate acceptance by CA-O-090, **or** `blocked` with the unmet gate. this Action does **not** promote Methods **or** generalize them into broader policies.

## Details
