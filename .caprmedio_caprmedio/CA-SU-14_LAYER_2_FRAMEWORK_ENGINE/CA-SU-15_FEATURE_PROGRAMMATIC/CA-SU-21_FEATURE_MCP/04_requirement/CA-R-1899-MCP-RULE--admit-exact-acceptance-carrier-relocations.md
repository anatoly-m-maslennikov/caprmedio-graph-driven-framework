---
atom_id: CA-R-1899
ref_id: CA-R-1899
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data Validation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Serialization
  - Subject/CAPRMEDIO/Carrier/File
tier: 3
status: Active
version: 14
updated_at: 2026-11-09 21:15:45 +0400
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

### Scope

the one registered relocation of three acceptance carriers under the current Epic.

- the registration is authority for exactly CA-P-1618@1, CA-P-1535@2 and CA-P-1622@4; every prior and current path, digest and canonical input digest is exact.
- preserve the existing fixed-path selected-source refresh. this admission creates no alias, raw-manifest edit, general relocation capability or changed source pin.
- derive the candidate, seal it under the existing typed Operator publisher, retain its lock and pending intent, revalidate currentness before publication, then require strict readback and a real Work Journal receipt.
- unknown, duplicate, stale, mismatched or extra relocation evidence refuses before effects. a pending publication or recording remains recoverable through the existing lifecycle.

### Relocation admission procedure

**to** admit the exact acceptance-carrier relocations, derive one candidate from the current binding and the closed registration in Details before applying the existing authorized publication lifecycle.


#### Scope

the one registered relocation of three acceptance carriers under the current Epic.

1. reopen the closed registration in Details, its exact canonical input bytes and the three retained current source carriers; require each current carrier's bytes, identity, version and digest to match its registration.
2. replace only the three registered source-path occurrences from the listed prior path to the listed current path. retain every other manifest field, route, graph, registry pin and source digest unchanged except the resulting canonical serialization and its derived `canonical_manifest_sha256`; the route-identical `selected_binding_digest` remains unchanged.
3. validate the whole candidate against current source pins and the existing selected-route schema. reject any changed topology, alias, unregistered path or mismatched occurrence before intent.
4. seal and publish only through the existing typed Operator context, lock, pending intent, rederivation and atomic readback lifecycle; record the actual result through the existing Work Journal.
5. retain pending publication or recording evidence for recovery. when the exact registered original input, sealed intent and current sources still match, an interrupted pre-effect attempt may retry the same candidate once under the existing lock. once that exact candidate exists, recovery is recording-only and performs no rewrite; ambiguous bytes refuse. historical evidence and installed runtime remain unchanged.

### Closed relocation registration

the acceptance-carrier relocation admission **must** use the closed serialization below for its exact three-carrier authority revision.


#### Scope

the one registered relocation of three acceptance carriers under the current Epic.

the **only** registration is the JSON object under `### Accepted carrier relocations`. its keys and nested relocation shapes are exact; duplicate or unknown fields are invalid. version and schema version are strict integers. paths are safe regular Project-relative carriers with no symlink ancestry.

the exact canonical input bytes and all three retained current source-carrier bytes **must** match. each relocation replaces only its registered prior source path with its registered current source path; carrier identity, version and digest remain unchanged. no route, graph, registry, source digest or normal fixed-path refresh behavior is otherwise admitted for change. the resulting canonical serialization and its derived `canonical_manifest_sha256` are recomputed; the route-identical `selected_binding_digest` remains unchanged.

the private reader feeds the existing typed host publisher, trusted Operator context, lock, pending intent, atomic write, strict readback and Work Journal receipt. an interrupted pre-effect attempt may retry the same candidate once only when the exact registered original input, sealed intent and current sources still match. once the exact candidate exists, recovery is recording-only without rewrite; ambiguous bytes refuse. no public MCP route, generic relocation capability, alias or caller-supplied registration is introduced.

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
