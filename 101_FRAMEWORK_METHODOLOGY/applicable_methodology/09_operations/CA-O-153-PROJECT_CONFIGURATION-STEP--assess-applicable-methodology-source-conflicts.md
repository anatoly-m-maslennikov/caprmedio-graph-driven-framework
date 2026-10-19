---
atom_id: CA-O-153
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 6
updated_at: "2026-10-19 03:06:29 +0400"
subjects:
  governs: "Applicable Methodology Compilation Assess Step"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Occurrent/Execution/Workflow Run", "Entity/Continuant/Projection/Type: Applicable Methodology", "Assess Source Conflicts", "Methodology Source.Expansion Boundary", "Core Meta-Model", "Entity/Continuant/Object/Atom", "Applicable Methodology Conflict", "Applicable Methodology Source Frontier Digest"]
relations:
  relates_to: [CA-O-011, CA-O-005]
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-011-PROJECT_CONFIGURATION-WORKFLOW--bind-source-reconciliation-to-applicable-methodology/CA-O-153-PROJECT_CONFIGURATION-STEP--assess-applicable-methodology-source-conflicts.md
  source_atom_id: CA-O-153
  source_atom_revision: 6
  source_sha256: 12e1ee8fd7b6fc6719e239694593be064feaf373993f40a6c31049129c43b3e2
  original_relations_sha256: 9e53cce5969842350ce25539597bb1bfbc787ff9378d7f40487b722802818257
---
# Summary

Assess Applicable Methodology source conflicts

## Operation

this Step is the assess node **of** CA-O-011, Applicable Methodology Compilation, invoking **`=1`** Action, CA-O-005, Assess Source Conflicts.

### Inputs and parameters

bind the exact selected source frontier returned by CA-O-152 and the Workflow Run's applicable Core expansion-boundary and conflict authority.

check Core expansion-boundary conformance under CA-R-1375 **and** the applicable conflict authority, including CA-R-1373; detect **every** boundary violation, duplicate selected Atom identity, unresolved replacement, incompatible retained Candidate, **and** unresolved priority. retain conflicting source Atoms rather than silently discarding them. calculate one deterministic digest of the exact selected frontier **and** report the complete deterministic conflict set **before** changing Applicable Methodology membership.

### Agentic invocation binding

for an invocation whose actual bound Action is Agentic, bind **`=1`** Integrated **or** Isolated context under CA-R-1527 from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, block that Agentic invocation; do **not** default **or** silently substitute. retain the selected context with the Step Run. a Programmatic invocation does **not** acquire an Agent context **or** require this parameter. this binding grants no additional authority **and** does **not** change the Action's identity **or** behavior.

## Details
