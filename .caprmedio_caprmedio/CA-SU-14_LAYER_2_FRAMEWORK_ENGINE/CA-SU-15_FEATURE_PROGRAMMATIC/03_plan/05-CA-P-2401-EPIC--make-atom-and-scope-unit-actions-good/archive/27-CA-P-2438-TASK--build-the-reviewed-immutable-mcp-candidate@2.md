---
atom_id: CA-P-2438
content_role: Plan
type: Plan
label: Task
work_sequence_number: 27
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 2
updated_at: "2026-10-20T12:50:48.772Z"
---
# Summary

Build the reviewed immutable MCP candidate

## Objective

Complete one bounded Epic CA-P-2401 responsibility with truthful source, fixture and runtime evidence.

## Details

After adapter review and source reconciliation, build one immutable candidate via existing ImageManager. Capture exact source fingerprint, parser source hash, image labels and immutable digest; prove production container and settings/state unchanged during build. No production replacement in this Task.

Use the PROGRAMMATIC M projection. At most15minutes own work; split dependent Tasks before extending. Preserve concurrent edits, exact predecessors and selected uv-managed environment. Review/update dependent Task before execution.

### Definition of Done

Bounded deliverable and reproducible checks are recorded, with runtime effects and limitations explicit.

### Dependency review before execution

Final rootvalidator531passed/no skips/errors, parser12passed, focusedConcern/schema/reference112passed. Independentread-onlyreview acceptedConcernsemantics; expectedmanifesthashcomparison is not an inventedruntimegate. D378currentv15Scope/Claim/Details match the frozenencodingcontract byte-for-byte; Subjects/version/time differ only. R1022v17Currenttarget/source-boundType behavior and D461defaultinheritedstatuscapture are implemented; actualread-onlyC528/C532create-shapedpreflights passed with unchangedbytes, includingDone targetP2433.

Use the existing guarded audit image-admission helper (its historical P2410 path/labels are tooling provenance, not a new P2410 completion) to perform P2438 build: immutableImageManager identity, freshnonproductionfixture/root/namespace, and protectedproductionpre/post comparison. No serverlaunch in this Task. Methodologysource-only10-Atom batch may finish concurrently because Frameworkengineclosure is separate; normalrelease still waits final sourcefreeze and intersectingcontractreview.
