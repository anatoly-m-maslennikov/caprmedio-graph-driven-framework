---
atom_id: CA-O-135
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Entities Graph Construction Step"
  depends_on: ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Occurrent/Execution/Workflow Run", "Entity/Node/Occurrent/Execution/Step Run", "Agentic Step Execution Context", "Entity/Node/Continuant/Projection/Type: Entities Graph"]
version: 5
updated_at: "2026-10-19 15:57:03 +0400"
relations:
  relates_to: [CA-O-133, CA-O-134, CA-R-1509, CA-R-1525, CA-R-1526, CA-R-1527]
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-135-PROJECT_CONFIGURATION-STEP--construct-the-requested-entities-graph.md
  source_atom_id: CA-O-135
  source_atom_revision: 5
  source_sha256: ed2bc60d8e2030bc0ac8f14323e4d3f33b3d579c989c4543f2eb9580273adad5
  original_relations_sha256: ba5b0565492adc01712e4665d0a19d0c5305e0eba4cd6d2277b6b196e73a92be
---
# Summary

Construct the requested Entities Graph

## Operation

Entities Graph Construction Step **means** the node of CA-O-133 invoking **=1** Action, CA-O-134, with graph kind fixed **to** Entities Graph.

- bind the Action's admitted request, exact source selection, narrower display selection **if** any, current authoritative source set, governing source/Relation Kind authority, representation configuration, target Projection/output destination **and** existing Projection/evidence from the corresponding Workflow invocation inputs.
- bind permissions, admitted realization/execution kind **and** recording context from that invocation's current admitted execution context. retain actual Workflow/Step/Action definition Revisions **and** actual Run/parent references; no previously completed Run **or** projected state supplies missing inputs.
- resolve execution kind under CA-R-1526. for an Agentic invocation, bind **=1** Integrated **or** Isolated context from the explicitly supplied Workflow runtime parameter under CA-R-1527; for Programmatic execution, no Agent context is selected. missing input, capability, permission **or** Agentic context blocks dispatch rather than silently substituting a realization.
- return the Action's exact result/effects/evidence **to** CA-O-133 **without** copying construction behavior, changing scope, repairing sources **or** turning internal Tool calls into Steps.

## Details

this reusable binding is distinct from its Step Run. the separately placed Workflow/Step Carriers retain unambiguous references under CA-D-467.
