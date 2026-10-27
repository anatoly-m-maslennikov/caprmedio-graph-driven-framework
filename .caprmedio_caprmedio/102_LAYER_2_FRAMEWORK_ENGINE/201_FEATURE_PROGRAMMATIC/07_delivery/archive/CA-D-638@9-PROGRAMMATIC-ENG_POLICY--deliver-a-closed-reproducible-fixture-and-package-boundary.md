---
atom_id: CA-D-638@9
content_role: Delivery
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-24 10:48:25 +0400
subjects:
  governs: Subject/Engineering/Carrier
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
relations:
  delivery_for:
  - CA-M-395
type: Eng Policy
tier: 5
---
# Summary

Deliver a closed reproducible fixture and package boundary

## Scope

Reproducible fixture/replay bundles and implementation packages delivered for a bounded PROGRAMMATIC change, including descendant Scope Units. Existing component-specific delivery places and package formats remain authoritative.

## Claim

A delivered fixture/replay bundle or implementation package must expose one inspectable manifest binding its entrypoint and declared execution environment to the complete selected input and dependency boundary. Required bytes are carried in the bundle or identified as explicit external dependencies; successful use must not depend on undeclared ambient files, imports, mutable Project Atoms or authoring-workspace state.

## Details

- Place the manifest with the delivered bundle/package metadata in its declared Delivery place. Use its existing manifest/metadata format when it can preserve these distinctions; do not maintain a second independent inventory for the same boundary. Resolve carried paths relative to the bundle/package boundary; distinguish external references explicitly.
- The manifest identifies the bundle/schema revision, entrypoint and invocation context, selected interpreter/dependency environment, and required member/support/configuration/schema inputs. Bind carried inputs to their paths and content digests; when an input is an identified Atom, preserve its actual Atom ID and Version as well. A dependency on an external service or environment is declared, not falsely represented as bundled bytes.
- For fixture/replay delivery, also bind the selected governing definitions and their consistent manifests, fixture inputs, expected outputs or expected failures, and any separate live-current compatibility purpose. Include the bounded lazy-read support closure needed by the exercised scenario, not the entire live Project graph.
- Preserve intentionally invalid target bytes and their expected result without treating them as invalid harness/support state. New current authority does not silently rewrite a frozen oracle; an intentional fixture-contract change delivers a correspondingly consistent bundle revision.
- Keep canonical fixture/package inputs separate from the live Project corpus and non-authoritative runtime copies. Disposable materializations and remnants use the configured Project Temporary State boundary; reusable canonical fixture sources and retained evidence are not automatically disposable.
- The manifest describes delivery and reproducibility, not authoring authority, mutation permission, successful execution, complete Journal coverage or another release-admission registry. Preserve existing file/path safety and source-preservation rules.
