---
atom_id: CA-P-2636
content_role: Plan
type: Plan
label: Task
work_sequence_number: 97
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Backlog
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom.Tier
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 7
updated_at: "2026-10-29 22:47:14 +0400"
tier: 3
---

# Summary

Prepare numeric-tier and parentage consumer migration

## Objective

Prepare the source-bound Engine consumer migration plan for numeric Atom Tier,
Scope Contract representation and Scope Unit parentage. Record the P2701
publication handoff without implementing it. This Task remains Backlog:
source publication is complete for the bounded handoff, but implementation,
runtime admission, tests, rebuild and release are not performed or authorized
by this planning update.

### Published P2701 handoff — 29 October 2026

Current Methodology Atoms are the authority. The publication receipt is
evidence of a bounded source frontier, not a replacement authority or runtime
permission:

- Receipt: `.caprmedio_tmp/p2701-scope-contract/publication-result.json`,
  state `complete`, 86 applied Current carriers and one retirement.
  SHA-256:
  `fd02a26710fd20121aa41425a2cf0e8d64186d2edd9c74d0be96c126c9dbed6e`.
- Prepared package: `.caprmedio_tmp/p2701-scope-contract/publication-package.json`.
  SHA-256:
  `37085a11af54d849782174c0829438d576c552edda2c2b20edaad7afbc71adc9`.
  Its `prepared` state is distinct from the completed publication receipt.
- Read-only inspection verified all 86 Current file hashes, 86 unique paths,
  the package/receipt identity set and the eight successor mappings. This is
  source evidence only, not a full graph/schema or runtime assessment.
- CA-R-1434 is retired without replacement. Its retained archive is historical;
  do not invent a successor, reuse the retired Claim as Current authority, or
  infer that a remaining runtime capability must be removed solely from this
  retirement.

Summary-changing successors have distinct identities:

| Historical predecessor | Published successor |
|---|---|
| CA-E-210 | CA-E-660 |
| CA-E-482 | CA-E-661 |
| CA-E-655 | CA-E-662 |
| CA-R-1443 | CA-R-2424 |
| CA-R-1551 | CA-R-2425 |
| CA-R-1773 | CA-R-2426 |
| CA-R-1774 | CA-R-2427 |
| CA-R-2130 | CA-R-2428 |

Resolve Current definitions by their actual Atom IDs and validate freshly
selected versions, paths and hashes before later admission. The table records
identity succession; it does not authorize blind replacement inside historical
archives, quoted evidence or deliberately frozen fixtures.

The package excludes Goal rows CA-R-1186, CA-R-1469, CA-R-1474, CA-R-1482,
CA-R-1601, CA-R-1602 and CA-R-1606, and retains held promotions CA-E-002,
CA-R-007 and CA-R-686. This handoff does not admit those items or establish
full Candidate #7 closure.

### Current model to consume

1. Numeric `tier` is graph-ordering data, not a fixed mapping to named classes,
   Content Roles, Types, Policies, Decisions or structural depth. Do not
   restore `local_tier`, `global_tier` or a persisted replacement global rank
   to satisfy old code.
2. A Scope Contract uses numeric Tier `0` and the filename TIER token
   `SCOPE_CONTRACT`. It is not a new Atom Type, Atom.Label or Scope Unit Type.
   Preserve the actual Workflow, Action and Step Types. Policies and Decisions
   are independent of Tier.
3. For the same owning Scope Unit, admit the equal-Tier-0 exception only for
   the source-admitted typed M/E/D/O-to-R serving relations. Preserve each
   Relation Type's independent source/target constraints and ordering domain.
   Do not turn this into arbitrary equal-Tier admission, R-to-R,
   R-to-M/E/D/O, M/E/D/O-to-M/E/D/O, reversed serving directions, or automatic
   conflict selection. Cross-Scope rules remain a separate source-defined
   check, not a comparison of a derived global rank.
4. Parentage comes from governing declarations, not filesystem nesting or an
   authored `structural_level` restored for old readers. Do not invent a
   stored `contains` field or conflate Scope Contract representation with the
   declaration fields `scope_unit_type` and `scope_unit_label`.
5. Resolve Goal-specific negative-Tier, ownership and ordering-context rules
   from their applicable Current definitions. Do not conflate those
   exceptions with Scope Contract Tier 0 or infer an Operator Scope Unit.

Key published source anchors include CA-R-2424@1, CA-D-651@12, CA-D-283@31
and CA-E-661@1 for Scope Contract representation; CA-R-2124@14,
CA-R-2267@2, CA-R-2268@1 and CA-R-1665@33 for Tier/Type independence;
CA-R-655@42, CA-R-2149@13, CA-E-654@11 and CA-R-808@31 for ordering and
the bounded serving exception. These are observed source revisions; later
source changes require fresh resolution rather than accepting stale pins.

### Observed consumer surface and migration order

The bounded code/config scan found no direct production literals for the
eight predecessor IDs or CA-R-1434 in the checked Engine/PROJECT_TOOLS scope.
CA-R-1551 remains in the deliberately frozen workflow golden corpus; that
historical fixture is not a Current-source dependency to replace blindly.
This is not proof of absence in dynamic lookups, installed images or every
artifact.

The concrete migration is primarily semantic:

1. Align Atom field/schema/domain admission and authority manifests:
   `check_fields.py`, `check_schema_extended.py`, `registry.json`,
   `structure_authority.json` and `graph_authority.json` still encode the
   old carrier/rank assumptions. Bind the complete applicable Current source
   frontier, not merely the eight identity replacements.
2. Align `request_models.py` and `selection.py`: old
   `global_tiers`/`local_tiers` selectors are not numeric `tier` support.
   Specify any compatibility surface explicitly; do not persist old fields.
3. Align filename, upgrade, replacement and lifecycle owners:
   `atom_operations.py`, orchestrator `replacement.py`/`engine.py` and
   `lifecycle_intents.py`. Preserve stable identities, exact retained
   predecessors, statuses, unrelated Properties and safety boundaries while
   applying the admitted numeric/Scope Contract filename rules.
4. Align `check_structure_extended.py`, `check_graph_extended.py` and
   `caprmedio_relation_types.toml`. Remove named-tier, role-to-Standard,
   structural-depth/global-rank and blanket equal-tier assumptions; implement
   only the exact admitted ordering domains and typed Tier-0 exception.
5. Review `project_structure.py` and `connector_scope_parsing.py` separately
   for retired declaration-field assumptions. They are Scope Unit declaration
   consumers, not a reason to add Scope Contract as a Type or Label.
   Preserve parent traversal, Rename descendant-parent updates, empty-only
   Remove, path safety and the local-order/navigation distinction.
6. Do not run old `backfill_global_tier.py` or
   `backfill_required_atom_properties.py` unchanged against the new model.
   Coordinate any explicitly authorized data migration rather than restoring
   obsolete fields through repair.
7. Validate refreshed source-based projection generations before consuming
   them. Previously inspected CA-PROJ-004/CA-PROJ-010 snapshots contained old
   IDs or retired R1434; Methodology is rebuilding its views. Do not overwrite
   its work, treat projections as authority, or text-rewrite frozen evidence.

This is an observed bounded inventory, not an implementation or exhaustive
runtime audit. Future checks should use isolated source-bound cases for
numeric Tier, preserved Workflow/Action/Step Types, Tier-0 filename encoding,
the admitted serving exception and forbidden equal-tier directions. Keep
legacy fixture worlds distinct from new-model cases. No such tests are run
by this Task update.

### Execution boundary

The former notice-only named-class/Goal-owner assumptions are superseded in
this planning record by Current source resolution. Existing code is not a
source-authoring gate, and broken consumers do not authorize rolling back
Methodology. Scope Unit physical operations remain Stage 2 under CA-P-2480;
this Task does not rename or move units, code, projections or configurations.

Keep implementation unstarted. Prepare bounded dependent work only within an
authorized Engine pass, rechecking current source bytes and applicable
Relation Type definitions before effects. No Methodology source edits,
parser/schema implementation, tests, rebuild, deployment, release or Git work
are authorized by this handoff record.

## Details

### Definition of Done

A reviewed migration plan identifies the complete applicable Current source
and governing-configuration frontier, the verified P2701 handoff and identity
map, concrete consumer ownership/callers, ordered migration boundaries and
isolated acceptance cases. It separates unresolved Goal/held-promotion work
and legacy fixtures from admitted inputs, and splits any execution work above
15 minutes into separate Tasks before execution.

The condition is falsified by missing applicable source/rule bindings,
unclassified unsafe consumers, invented replacement authority, broader
equal-Tier admission, a Scope Contract Type/Label mutation, historical
rewrites, or an implementation/readiness claim based only on this Plan,
receipt or projection. Recording this handoff alone does not complete the
whole migration-planning Task or admit a runtime.
