---
identity:
  atom_id: CA-A-1337
  ref_id: CA-A-1337
context:
  role: analysis_and_advisory
  form: Analysis Report
  container:
    scope_unit: CA-SU-14
  tier: 3
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
state:
  version: 1
  status: done
  updated_at: '2026-11-12T01:56:16.322021+00:00'
destination:
  file:
    name: CA-A-1337-FRAMEWORK_ENGINE-ANALYSIS_REPORT--compare-atom-lifecycle-workflows-with-their-implementation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory/020_done
---
## Summary

Compare Atom Lifecycle Workflows with their implementation

## Question

Which parts of the six Current Atom Lifecycle Workflows match the working implementation, and what should the Python pilot preserve or resolve?

## Scope

CA-P-3019 under CA-P-3018. Current Workflow, Step, and Action Atoms in PROJECT_CONFIGURATION, the six Lifecycle routes, their Workbench source and effect bindings, and their MCP response adapter. CA-P-2934 and CA-P-3003 record prior implementation and image verification.

## Approach

Three read-only reviews traced authored operations, implementation, and Engine authority. The test run used Python 3.14.7 and the working tree based on `f8aab16bf1`, including concurrent edits. Live observations refer to the earlier CA-P-3018 MCP calls on image 0.4.4.43. Code module names below are in `FEATURE_TOOLS/ATOM_LIFECYCLE` unless noted.

## Results

| Current O Workflow | Authored sequence and code mapping |
|---|---|
| CA-O-10016@2 Create Draft | Steps O-10014, O-10012, O-10015, O-10013 call Actions O-10006, O-10002, O-10004, O-10003. Read and check input, request a correction when needed, then prepare and save. The provider handles input correction. `draft.create_draft` owns preparation and save. |
| CA-O-10018@2 Promote Draft | Step O-10017 calls Action O-10005. `publish.promote_draft` validates the pinned Draft and destination, handles predecessors, writes the Current carrier, and removes the Draft. |
| CA-O-10009@2 Archive Atom | Step O-10008 calls Action O-10001. The authored Workflow tells callers to archive descendants first. `state_actions.archive_workflow` instead plans and applies the descendant-first cascade in one call. |
| CA-O-10011@3 Change Current Status | Step O-10010 calls Action O-10007. `status_cascade.change_status_workflow` selects, preflights and applies the tree. It reopens terminal parents before their descendants and closes descendants before parents. Backlog to Active also applies Active throughout the Current tree. |
| CA-O-10023@2 Update Atom Directly | Step O-10022 calls Action O-10000. `state_actions.direct_update` applies an edit in place for an exact non-container Atom. |
| CA-O-10024@3 Update Atom | Steps O-10020, O-10019, O-10021 call Create Draft, Archive Atom, and Promote Draft in order. `publish.update_atom` stages the update and reuses these code paths with the original Current Status. |

All listed Steps are Version 1 except O-10015@2. Actions O-10002 and O-10004 are Versions 2 and 4 respectively. The other listed Actions are Version 1.

### Findings

1. **Transient Update regression.** The content-only branch reads `plan['same']`, which `draft.prepare_draft` does not return. The composed-update regression test raised `KeyError: 'same'`. The reviewed failing code is `publish.py` SHA-256 `4d558827397b44ebc8bebf79db7f951b3f36eebed4baeeaa22782fa03b8b07a4`; `draft.py` is `b8e893f2d7ae1e3f77e17dbabeb08964413be8e2bf7e361503ab8613310f7eb6`.
2. **Draft descendants blocked the live Epic.** The Workbench descendant query admits Draft references. The original cascade attempted to select them as Current sources. The checkout now filters qualified Draft and Archived references before source selection and passes the Draft-child regression test. The Operator requires Epic Backlog to Active to activate contained Tasks recursively. Keep a two-level fixture in the Python pilot.
3. **Container content edit.** The live direct update of the Epic was refused. The direct Action is scoped to non-containers. The checkout now adds a body-only path through composed Update that keeps the container's identity and destination. Verify that path in the installed image before relying on it.
4. **MCP loses actionable results.** A successful single operation returns only `status: completed` in `FEATURE_MCP/registry_lifecycle_provider.py`. The Workflow result specifies saved or removed references. During Epic creation we needed a separate query to locate the saved Draft.
5. **Version rules differ.** O-10003 says Current Version plus one for a same-ID Draft. Code allocates above the highest known Version. O-10005 retains the Draft Version, and code rejects a same-ID Draft unless the predecessor is exactly one Version lower. Reconcile this with the Operator's promotion rule before treating Version behavior as parity.
6. **Filename input error is opaque.** A comma in the Epic Summary caused a generic backend failure in destination derivation. The same operation succeeded after removing the punctuation. Report the failing field or use an admitted serialization rule.
7. **Authored Workflow ordering is incomplete in the diagrams.** Archive and Change Status show one Step each. Their prose carries descendant ordering. Use that prose and the latest Operator decision when preparing the parity fixtures.

### Verification

The first run passed 183 tests and 52 subtests, with one composed-update failure. After concurrent changes, the same focused lifecycle and MCP registry suite passed 187 tests and 52 subtests. The corrected `publish.py` SHA-256 was `301b2ace3183f2773deaa419c34fb70dbb2542a0d5a6f102d1d538a8986b40ca`. The earlier live Epic operations verified Draft creation, promotion, and activation of one Current child. The rerun tested the checkout. Live verification of the newer changes remains pending.

## TLDR

The six routes already separate a useful portion of preflight and effect application. Pilot Change Current Status with explicit inputs, recursive activation and partial-effect evidence. Resolve the identified Version discrepancy and keep successful result details visible across the Engine and MCP boundary.
