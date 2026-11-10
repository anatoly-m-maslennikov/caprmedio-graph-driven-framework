---
atom_id: CA-R-1899
ref_id: CA-R-1899
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Storage
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling
    <+ Data Validation
  - MODEL//CAPRMEDIO <+ Projection
  - MODEL//CAPRMEDIO <+ Actor/Operator
  - MODEL//CAPRMEDIO <+ Execution
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling
    <+ Serialization
  - MODEL//CAPRMEDIO <+ Carrier/File
tier: 3
status: Active
version: 15
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-R-1899-MCP-RULE--admit-exact-acceptance-carrier-relocations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
current_scope_unit: MCP
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-354
  - CA-D-592
---

## Summary

Admit exact acceptance-carrier relocations

## Claim

### Prose Claim

the selected binding Projection **must** admit only the three exact registered acceptance-carrier path relocations specified in Details while preserving their bytes, identities, versions, pins, route structure, graph and registry.

## Details

### Registered relocation admission

- The sole authority is the closed registration for exactly CA-P-1618@1, CA-P-1535@2, and CA-P-1622@4; every prior/current path, identity, version, digest, and canonical input digest must match.
- Preserve fixed-path selected-source refresh. Replace only the three registered prior paths; create no alias, raw-manifest edit, general relocation capability, changed source pin, or caller-supplied registration. All other manifest fields, routes, graph edges, registry pins, source digests, and selected_binding_digest remain unchanged; only canonical serialization and derived canonical_manifest_sha256 may change.
- Derive and seal one candidate under the typed Operator context, lock, pending intent, revalidation, atomic publication, strict readback, and real Work Journal receipt. Unknown, duplicate, stale, mismatched, extra, unsafe, or unregistered evidence refuses before effects.
- A pending publication/recording remains recoverable. An interrupted pre-effect attempt may retry the same candidate once only when exact registered input, sealed intent, and current sources still match; once the candidate exists, recovery is recording-only without rewrite. Ambiguous bytes refuse; historical evidence and installed runtime remain unchanged.

### Closed registration

The exact JSON under Accepted carrier relocations is the only registration. Its keys/nested shapes and integer schema/version are strict; paths are safe regular Project-relative carriers without symlink ancestry. The private reader feeds the existing trusted Operator publisher, lock, pending intent, atomic write, strict readback, and Work Journal receipt. No public MCP route, generic relocation capability, or alias is introduced.
#### Accepted carrier relocations

```json
{
  "schema_version": 1,
  "registration_id": "acceptance-carrier-relocations-p1117-20261008",
  "authorization_ref": ".caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations.md",
  "input_manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
  "input_manifest_sha256": "1381b8c41d59e7f3636ac69e37e365e41b8429469e748e9824e982a7ccdd71a9",
  "input_canonical_manifest_sha256": "2235d03cdb904942c9b26118a867769696fbe3dfc650eebb6c2e8d49b19bbc4e",
  "relocations": [
    {
      "atom_id": "CA-P-1618",
      "version": 1,
      "prior_source_path": ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/29-CA-P-1618-TASK--accept-current-artifact-query-source-frontier.md",
      "current_source_path": ".caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/29-CA-P-1618-TASK--accept-current-artifact-query-source-frontier.md",
      "digest": "bdf10c928c10c102dc489c8e3e526ffe73e8a33d492f4dabc8b5d0129c453b1f"
    },
    {
      "atom_id": "CA-P-1535",
      "version": 2,
      "prior_source_path": ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/15-CA-P-1535-TASK--accept-final-journal-query-source.md",
      "current_source_path": ".caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/15-CA-P-1535-TASK--accept-final-journal-query-source.md",
      "digest": "6246b46d2961d795e29eeb224f01b14979434d4ad24cf3f4913c490268cf52dc"
    },
    {
      "atom_id": "CA-P-1622",
      "version": 4,
      "prior_source_path": ".caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/10-CA-P-1620-TASK--deliver-release-version-workflow/done/02-CA-P-1622-TASK--review-release-version-source-and-admission.md",
      "current_source_path": ".caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/10-CA-P-1620-TASK--deliver-release-version-workflow/done/02-CA-P-1622-TASK--review-release-version-source-and-admission.md",
      "digest": "7cd6a839a190add10108bdd5e58700aeae7a89316aa721b2b5340bda865a2739"
    }
  ]
}
```
