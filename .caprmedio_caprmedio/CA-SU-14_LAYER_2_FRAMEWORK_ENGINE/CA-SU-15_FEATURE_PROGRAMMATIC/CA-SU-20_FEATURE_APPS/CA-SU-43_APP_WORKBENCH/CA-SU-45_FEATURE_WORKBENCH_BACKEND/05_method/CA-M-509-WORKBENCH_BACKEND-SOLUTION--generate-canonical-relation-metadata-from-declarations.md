---
identity:
  ref_id: CA-M-509
  id: CA-M-509
context:
  container:
    scope_unit: CA-SU-45
  role: Method
  form: Solution
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data
      Handling <+ Schema
    dependencies:
    - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  tier: 3
state:
  status: Active
  version: 3
  updated_at: 2026-11-09 19:30:15 +0400
destination:
  file:
    name: CA-M-509-WORKBENCH_BACKEND-SOLUTION--generate-canonical-relation-metadata-from-declarations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method
author: Anatoly Maslennikov
relations:
  method_for:
  - CA-R-2724
  IS_REPLACEMENT_FOR:
  - CA-D-705
---

## Summary

Generate canonical relation metadata from declarations

## Claim

### Prose Claim

Generate one rebuildable relation registry from Current Requirement relation Declarations. Use that registry for Workbench relation-name resolution and direct/derived materialization.

- Include canonical Relation names, explicit inverse aliases, literal unqualified inverse bindings, and their source Atom IDs and versions.
- Accept the applicable Declaration Forms, including Relation Declaration. An inverse alias introduced by a canonical Declaration needs no separate Relation Declaration.
- Normalize an explicit inverse alias by swapping its endpoints once. For an unambiguous legacy named inverse, preserve the same fact through its declared counterpart. Do not edit the source carrier or invent a binding.
- Derive container facts from the effective Header.Container value, including its Header.Context.Container carrier layout. Resolve the Project root as a Scope Unit using uppercase(Project prefix) followed by -SU-00. Build inverse views from each canonical direct fact once. A changed source refreshes only the affected direct and inverse rows and hashes.
- Preserve exact model names. Existing ambiguity warnings and omission rules still apply; do not choose a winner or repair source declarations silently.
- Keep arbitrary prose and general CFEL evaluation out of this compiler. Do not evaluate qualified Model derivation rules or turn them into runtime facts. Unsupported or ambiguous literal metadata is diagnosed and omitted, not guessed.

Regenerate the registry on every supported image rebuild, including local release. Use the same compiler for the existing refresh of relevant Current Declaration changes, so the runtime does not keep stale relation metadata. The asset is derived data, not another source of truth or a separately maintained list.

## Semantics

Canonicalization changes the query representation of an unambiguous fact, not its meaning or its authored source. The runtime graph still uses its admitted Atom and Scope Unit sources; relation metadata does not add new graph vertex domains.

## Details

### Generated asset delivery

Deliver the relation registry as a deterministic JSON asset. It retains declared names, unqualified inverse bindings, inverse aliases, and source Atom IDs, versions, paths and fingerprints. A changing generation timestamp is excluded from its fingerprint, so identical selected inputs produce identical bytes.

The generator receives an explicit selected Project root and output path. On every supported image-build path, including local release, generate the asset before computing the image fingerprint and assembling the build context. Local release includes and verifies the asset in its staged package alongside the existing code-owned tool registry. The post-start discovery catalog is not a generator input.

Only the generated metadata asset and its digest enter the build context and image identity; Project authority carriers stay outside the image context. A missing asset or failed required generation prevents acceptance of that image or package; it is never silently replaced with a handwritten or stale list.

At runtime, use the selected Project's admitted declaration capture and the same compiler when relevant Declarations change, reusing existing owner synchronization and derived-asset storage. Keep MCP tool discovery's code/config registry separate; do not restore startup scans of the full Atom inventory merely to register MCP tools.

The existing image/package identity verification covers the generated asset. Registry metadata does not add a source table, a second source of truth, a scheduler or a service.
