---
atom_id: CA-D-544
ref_id: CA-D-544
container:
  scope_unit: CA-SU-24
role: Delivery
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Prompt Authoring
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
tier: 3
status: Active
version: 18
updated_at: 2026-11-02 19:46:47 +0400
carrier_destination:
  file:
    name: CA-D-544-PROMPTS-ENG_DECISION--deliver-current-implementation-workflow-prompt-carriers.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/07_delivery
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
---
# Summary

Deliver current Implementation Workflow prompt carriers

## Scope

the definition-only shared-context package at `LAYER_2_FRAMEWORK_ENGINE/FEATURE_AGENTIC/FEATURE_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW/SHARED_CONTEXT/`.

## Claim

the package **must** contain only `CA-O-231`, `CA-O-232`, `CA-O-233`, `CA-O-094`, `CA-O-234`, `CA-O-096`, `CA-O-099`, and `CA-O-239` `.prompt.md` carriers, plus `README.md`, `definition_frontier.projection.json`, and `tests/`.

## Details

Each prompt header carries exact Step, Action, and context. This Delivery specifies definition-only carriers, not executable admission. Keep the existing native package, executable source_bindings, and frozen corpus unchanged until separately admitted runtime realization; do not dispatch these definitions through the old adapter.

Every invocation packet additionally carries exactly one `selected_project`
binding before a prompt can verify its governed sources or call an Agent:

| Field | Required value | Boundary |
| --- | --- | --- |
| `selected_project.kind` | `selected_project` | identifies the Project frozen by the selected Workflow; it is not an absolute host path, current directory, code-root copy, or mount grant |
| `selected_project.source_root` | `.caprmedio_caprmedio` | the only authority root for prompt-source resolution |
| `selected_project.source_references` | the exact current `source_bindings` rows, each with Atom ID, Version, project-relative `path`, and SHA-256 | every path is nonempty, relative, has no `..` segment, begins under `source_root`, and resolves only beneath the frozen selected Project |
| `requirements`, `methods`, `evaluations`, `delivery` | complete applicable direct source rows: `atom_id`, `version`, Project-relative `path`, `sha256`, and full `content` | independently verify the authorized initial selection, its declared universe and applicable governing parents against current Project authority; preserve R/D implementation targets separately from governing context |
| `method_projection` (optional) | a legacy source-bound derived view | it neither replaces direct source rows nor blocks a Run when absent; no compiled paragraph or projection file is required |
| `workspace` | the existing absolute, non-symlink disposable workspace supplied to the Agent | no source binding infers or substitutes this path |
| `permissions.implementation_workspace` | the existing exact `{kind: disposable_workspace, path: workspace, allow_write: true}` capability | it must match `workspace`; this Delivery adds no write grant |

The selected Workflow runtime resolves `selected_project` only from its frozen
Project context. Absent, stale, duplicate, mismatched, escaping, or
partially-readable source references, incomplete direct RMED inputs, or a
missing/mismatched workspace capability blocks before Agent launch or effects.
This binding exposes neither credentials nor an Agent endpoint and does not
authorize a hidden mount, arbitrary writer, or live-model execution. An
explicit executable mock remains `mock-not-live-llm` evidence only.

An Integrated prompt response carries the current Step's prompt, bound inputs,
output contract, and opaque continuation identity. Publishing it leaves the Step
pending. The controlling session may perform or delegate the admitted work and
submit its actual result through the same Workflow interface. Only the executor
validates that bound submission and chooses the next Step; a prompt alone is not
completion. Retain the persistent Plan, partial effects, candidate-specific
review/check evidence and finite retry state across requests. The implementation
instructions use CA-R-2117, CA-M-431, and CA-E-653 for narrowest-branch RMED
ownership comments; citations alone do not prove conformance.
