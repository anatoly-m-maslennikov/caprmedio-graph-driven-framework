---
identity:
  atom_id: CA-D-638
  ref_id: CA-D-638
context:
  container:
    scope_unit: CA-SU-15
  role: Delivery
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery
      <+ Reproducibility
    dependencies:
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Requirement)
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Method)
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Evaluation)
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Delivery)
  tier: 6
relations:
  delivery_for:
  - CA-M-395
state:
  status: Active
  version: 16
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-D-638-PROGRAMMATIC-DIRECT_POLICY--deliver-a-closed-reproducible-fixture-and-package-boundary.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/07_delivery
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Deliver a closed reproducible fixture and package boundary

## Claim

### Prose Claim

A delivered fixture/replay bundle or implementation package must expose one inspectable manifest binding its entrypoint and declared execution environment to the complete selected input and dependency boundary. Required bytes are carried in the bundle or identified as explicit external dependencies; successful use must not depend on undeclared ambient files, imports, mutable Project Atoms or authoring-workspace state.

## Details

### Scope

Reproducible fixture/replay bundles and implementation packages delivered for a bounded PROGRAMMATIC change, including descendant Scope Units. Existing component-specific delivery places and package formats remain authoritative.

- Place the manifest with the delivered bundle/package metadata in its declared Delivery place. Use its existing manifest/metadata format when it can preserve these distinctions; do not maintain a second independent inventory for the same boundary. Resolve carried paths relative to the bundle/package boundary; distinguish external references explicitly.
- The manifest identifies the bundle/schema revision, entrypoint and invocation context, selected interpreter/dependency environment, and required member/support/configuration/schema inputs. Bind carried inputs to their paths and content digests; when an input is an identified Atom, preserve its actual Atom ID and Version as well. A dependency on an external service or environment is declared, not falsely represented as bundled bytes.
- For fixture/replay delivery, also bind the selected governing definitions and their consistent manifests, fixture inputs, expected outputs or expected failures, and any separate live-current compatibility purpose. Include the bounded lazy-read support closure needed by the exercised scenario, not the entire live Project graph.
- Preserve intentionally invalid target bytes and their expected result without treating them as invalid harness/support state. New current authority does not silently rewrite a frozen oracle; an intentional fixture-contract change delivers a correspondingly consistent bundle revision.
- Keep canonical fixture/package inputs separate from the live Project corpus and non-authoritative runtime copies. Disposable materializations and remnants use the configured Project Temporary State boundary; reusable canonical fixture sources and retained evidence are not automatically disposable.
- The manifest describes delivery and reproducibility, not authoring authority, mutation permission, successful execution, complete Journal coverage or another release-admission registry. Preserve existing file/path safety and source-preservation rules.
