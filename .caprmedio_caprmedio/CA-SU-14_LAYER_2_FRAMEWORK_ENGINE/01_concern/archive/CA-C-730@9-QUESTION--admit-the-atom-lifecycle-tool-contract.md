---
identity:
  id: CA-C-730
  ref_id: CA-C-730@9
context:
  container:
    scope_unit: CA-SU-14
  role: Concern
  form: Question
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 3
state:
  status: Archived
  version: 9
  updated_at: 2026-11-11 13:41:54 +0400
destination:
  file:
    name: CA-C-730@9-QUESTION--admit-the-atom-lifecycle-tool-contract.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern/archive
author: Anatoly Maslennikov
relations:
  concern_about:
  - CA-O-127
  - CA-P-2934
  - CA-O-128
  - CA-R-1093
  - CA-M-374
  - CA-D-623
  - CA-R-1432
  - CA-R-1788
  - CA-E-521
---

## Summary

Admit the Atom Lifecycle Tool contract

## Concern

What remains to admit and publish the six Atom Lifecycle Tools selected for CA-P-2934?

## Details

The Operator selected the six separate Workflow Drafts. Update handles a Scope Unit change as an ordinary property change with derived placement. The new Tools have no separate Move operation. Review the supporting Step and Action Drafts and retire the combined Workflow after its Current references are accounted for. The selected Drafts wait for an additional input dictionary on a format or allowed-value error and allow cancellation while waiting.

The retirement removed the old lifecycle effect adapters. Retained metadata, Header, scope and Journal primitives can support new effects. Direct Update of an exactly selected carrier has Current requirements for persisted readback, unchanged ID, Version and Updated At, and preservation of omitted properties. Current R1093, M374 and D623 require every changed same-ID edit to advance Version and Updated At and retain history. O128, R1432, R1788 and E521 require Direct Update to preserve those values. Before implementing a persisted Direct Update, decide which rule governs and reconcile the affected sources. The exact old/new scalar patch shape is already available in R1934 and D623. Prepare disposable fixtures while this decision is open.

The installed Codex App Server relays standard MCP forms in the same Tool call. The no-effect probe delivered corrected input on Accept and kept the Action counter at zero on Cancel. See CA-P-2967. Decide the response for clients without form support and verify the real Tool's cancellation boundary before publishing it.

Three Drafts propose an explicit boundary for the lifecycle effects: CA-R-1093@25-draft, CA-M-374@12-draft and CA-D-623@13-draft. Their carve-outs name the combined Workflow and Action. Update them to name the selected separate definitions before adoption.

CA-P-2968 verifies the SDK's post-start cancellation behavior in isolation. An unshielded Action was interrupted. A shield let one synthetic Action finish while the session stayed open. The real Tool boundary still needs its own verification.

CA-R-1521 requires the qualified Status model. The Operator confirmed that allowed Status values come from Declarations, using `:=` in Subjects and `::` in Formal Claims. Current CA-R-2696 and CA-R-3010 use older Status notation in their Formal Claims. Current CA-R-1539, CA-R-1608 and CA-R-1875 state additional qualified values in prose. Sent the notation discrepancy to the Model owner. Use the adopted Formal Claims as the build-time source for validation and preserve inherited values per CA-R-1308. The installed Workbench schema exposes Status as text. The retained reader pins raw bytes at an exact path. The Tool still needs to resolve one authored carrier from the requested logical identity. See CA-P-2970, CA-P-2972 and CA-P-2973.
