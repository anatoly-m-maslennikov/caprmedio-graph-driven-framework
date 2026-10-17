---
atom_id: CA-O-139
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Project Structure Maintenance Selection Step"
  depends_on: ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow", "Entity/Occurrent/Execution/Workflow Run", "Entity/Occurrent/Execution/Step Run", "Agentic Step Execution Context"]
version: 4
updated_at: "2026-10-15 18:53:30 +0000"
relations:
  relates_to: [CA-O-015, CA-O-004, CA-R-1509, CA-R-1510, CA-R-1511, CA-R-1527]
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/09_operations/CA-O-139-CORE_META_MODEL-STEP--select-project-structure-maintenance-sources.md
  source_atom_id: CA-O-139
  source_atom_revision: 4
  source_sha256: 095c487878d7929484196dc72f06922e5cac9960d41094d28b2981c8ad891ff3
  original_relations_sha256: a7cbaf0db4bd5a8ab86dd769c379969ce27ce98e1d1de55c69ce1763b7d11cce
---
# Summary

Select project structure maintenance sources

## Operation

Project Structure Maintenance Selection Step **means** the node **in** the owning Workflow CA-O-015 that invokes **=1** existing Action, CA-O-004, with the following bindings.

| Required input or parameter | Bound source |
| --- | --- |
| Current Project Structure, relevant Settings, Goal/Atom references, and separate Carrier observations | The exact admitted CA-O-015 Workflow Run inputs, kept separately by source kind. |
| Applicable source-selection constraints and eligible source universe | The Workflow Run's current governing authority and bounded structural request; unresolved input selection remains an Action result, not a guessed binding. |

For an invocation whose actual bound Action is Agentic, bind **=1** Integrated **or** Isolated context under CA-R-1527 from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. Missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, block that Agentic invocation; do **not** default **or** silently substitute. A Programmatic invocation does **not** acquire an Agent context. Applicable authority, permissions and remaining retry allowance come from the same Workflow Run; the binding grants no additional authority.

Return the referenced Action's exact result **to** CA-O-015 **without** copying **or** redefining the Action's behavior, changing its outcome, **or** choosing the next Step here. CA-O-015 owns every transition and terminal guard. Retain the exact Action/Step Revisions, input/result source identities, actual effects and resolved context with the Step Run under CA-R-1510/CA-R-1511; a source definition is **not** evidence of an executed Run.

## Details
