---
atom_id: CA-A-1247
ref_id: CA-A-1247
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Formal Model
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 15:49:28 +0400
carrier_destination:
  file:
    name: CA-A-1247-CAPRMEDIO-SPECIFICATION_PROPOSAL--scope-assets-to-non-executable-implementation-content.md
    path: .caprmedio_caprmedio/02_analysis
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Scope Assets to non-executable Implementation content

## Decision

Asset means any non-executable content within Implementation. It does not mean every non-executable file in the repository. Logical Asset content remains distinct from the File/Directory/Database Carrier representing it. An Atom, governing configuration or Journal is not reclassified merely because its Carrier is a non-executable file.

The proposed construction remains Implementation > Code > Module, Unit, Asset. No existing Function, Class, Package or Tool is automatically mapped to Asset by this decision. Unit meaning and those old-kind mappings remain open; the Asset population question is resolved.
