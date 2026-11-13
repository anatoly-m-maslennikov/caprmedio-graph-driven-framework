---
identity:
  atom_id: CA-E-653
  ref_id: CA-E-653
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
      <+ Traceability
    dependencies: []
  tier: 5
relations:
  evaluation_for:
  - CA-M-526
state:
  status: active
  version: 15
  updated_at: '2026-11-12T12:29:26.735990+00:00'
destination:
  file:
    name: CA-E-653-PROGRAMMATIC-EVAL_CASE--verify-rmed-implementation-traceability.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
cce_version: cce_1
cce_form: evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
## Summary

Verify RMED implementation traceability

## Claim

### Prose Claim

Each assessed module that directly implements a Requirement, Evaluation, Delivery or Method whose Form is Solution, Decision or Direct Policy has one header comment per implemented Atom. Each comment contains only its Atom ID and Version. Optional comments on narrower owning units follow the same syntax. Comments do not prove conformance or completion.

## Details

### Scope

New or materially changed admitted PROGRAMMATIC implementation and requested
refreshes of its source trace. Vendor code, generated output, frozen fixtures,
and legacy history are excluded unless explicitly admitted into the assessed
source boundary.

#### Applicable conditions

Do not infer applicability from a projection alone. Apply this case only to the admitted source boundary.

#### Test case

Use an isolated fixture with a module that directly implements several Requirement, Evaluation, Delivery and Method claims. Include a Direct Policy that the module implements. Include an Atom that is only called by the module and a generic coding Policy that guides it without being implemented.

Verify one bare versioned Atom comment per line before the first code, using the file language's comment syntax. `# CA-R-123@1` is a syntax example only; the fixture uses actual Current IDs and Versions. Resolve each cited ID and Version against the applicable Current authority and check that the module materially implements that claim. Accept optional narrower function or class comments; their absence alone is not failure. Do not require role-labelled blocks, a marker, narrowest-leaf selection or automatic ancestor removal.

Include a shared provider that materially implements a Method and a consumer that only imports or calls that provider. The provider cites its implemented Method with a bare current ID and Version; the consumer does not cite that Method merely for calling it. Check actual delegation or decorator behavior rather than treating an import as proof that the shared behavior ran. A generic Policy that guides either module still receives no implementation citation.

Include valid many-to-many ownership and false positives: malformed or unversioned IDs, stale or unresolved versions, paths or titles used as IDs, a Method Policy cited only as guidance, and an Atom that is only called. Check excluded files separately rather than changing them automatically.

#### Acceptance criteria

Pass when each assessed module carries the required bare ID-and-Version comments, each cited relationship is substantive, and optional narrower comments are valid when present. Reject role labels, prose or an `implementation of` marker in those comments. Generic coding Policies and called-only Atoms do not become implementation owners. A stale or unresolved citation is a reported traceability gap, not a reason to invent an ID or silently bump its Version.

#### Failure disposition

Reject traceability readiness for the affected source and report each missing,
invalid, stale, overbroad, or unidentifiable citation. Preserve implementation
behavior and do not create a release gate, mutate authority, or mass-edit files
outside the admitted boundary.

Use CA-M-403's locality preference and CA-M-405's observed-evidence boundary
when interpreting results. CA-E-642's many-to-many coverage rule means that
relations route the review but do not replace substantive evidence.
