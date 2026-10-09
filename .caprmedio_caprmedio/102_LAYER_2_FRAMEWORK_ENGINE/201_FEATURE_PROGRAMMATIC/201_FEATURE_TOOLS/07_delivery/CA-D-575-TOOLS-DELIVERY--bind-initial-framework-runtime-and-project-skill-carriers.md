---
atom_id: CA-D-575
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 6
updated_at: "2026-10-09 16:57:27 +0400"
subjects:
  governs: "Tool/INSTALL_TOOLS/First-initialization runtime and Skill carriers"
  depends_on: [Tool, Framework Package, Runtime, Skill, Manifest, Docker Image, Journal]
relations:
  delivery_for: [CA-R-1881, CA-M-338]
---
# Summary

Bind initial Framework runtime and project Skill carriers

## Scope

The reusable content-addressed Framework package, package selector, isolated target-Project selector and project-local Skill carriers.

## Claim

the INSTALL_TOOLS first-initialization variant **must** use a reusable Framework package at `.caprmedio_install/releases/<package_manifest_sha256>/` with `manifest.toml`, the complete `102_FRAMEWORK_ENGINE/`, sealed `pyproject.toml`, `uv.lock` and `version.toml`, admitted defaults, `METHODOLOGY/`, `SKILLS/ca/`, active source catalog and declared support; `.caprmedio_install/current.toml` **must** select only a reopened verified package. A target Project's `.caprmedio_runtime/installation/current.toml` **must** bind that package, target-Project context and state generation only after the complete hook-free `.agents/skills/ca/` payload is published. Retained image proof **must** prove a fixed isolated context contains those exact package bytes and that its immutable image and canary bind the exact manifest and source-context digests.

## Details

### Package, selector and runtime carriers

The package manifest schema is declared only by `102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-596-TOOLS-DELIVERY--encode-the-reusable-framework-package.md`; the sole package-selector schema is declared only by `102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-598-TOOLS-DELIVERY--encode-current-reusable-package-selector.md`; and the sole target-runtime-selector schema is declared only by `102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-599-TOOLS-DELIVERY--encode-target-runtime-installation-selector.md`. This Delivery **must not** add, omit or restate any field from those closed schemas. Package-owned wrapper and environment carriers execute only the package command boundary from CA-D-601; they never contain a checkout root.

### Compiler-currentness proof

The compiler-currentness carrier contains the exact compiler input source-context digest, compiled-tree digest, compiler entrypoint identity, canonical compiled root, `source_snapshot_is_current` results before and after verification, complete zero-conflict selected frontier from canonical `compile_report`, and exact `projection_bytes` reconstruction from canonical `output_plan` for every compiled output at its planned `role_directory`/`basename` and source-relative path. The complete compiled-tree path set, payload hashes, generated-tree digest, source hashes, and metadata each equal that read-only reconstruction before package planning. An unresolved, conflict-dependent, colliding, or changed-snapshot selection rejects. This proves a current mechanical projection, not that a compiler Run occurred.

### Bootstrap-image proof and locations

The bootstrap-image evidence contains exactly the package manifest SHA-256, source-context SHA-256, immutable image digest, fixed-context digest, `bootstrap_proof_key`, canonical private proof location, canonical private fixed-context location, three immutable canonical command records, and canary result; `bootstrap_proof_key` is SHA-256 of canonical UTF-8 rows `(package_manifest_sha256, immutable_image_digest)`, ordered in that stated field order. The proof is at `.caprmedio_runtime/framework/bootstrap-image-evidence/<bootstrap_proof_key>/evidence.toml` and its fixed context at `.caprmedio_runtime/framework/bootstrap-image-evidence/<bootstrap_proof_key>/context/`; these private locations are derived, never caller inputs. It is private retained Tool evidence, never a D566 member, selector field, public request field, Workflow, Run, Journal schema, or mutable success flag.

### Fixed inputs and command-output carriers

Its context contains only the sealed package, the existing fixed `IMAGE_DOCKERFILE`, the exact sealed `pyproject.toml` and `uv.lock` rows required by that producer, and fixed canary carriers; every member is an enumerated sealed row. The records respectively cover build, immutable-ID inspection, and canary and each contains exact argv, exit status, start and finish times, plus exact relative paths and SHA-256 values for immutable byte carriers `commands/<build|inspect|canary>/stdout` and `commands/<build|inspect|canary>/stderr` beneath the proof root. The fixed build reuses the existing Release fixed canary and bounded pure build, command-record, and image-inspection primitives only where compatible with bootstrap labels; package-driven adapters may not invoke selected-N, candidate-suite, promotion, or retirement preconditions. The fixed build produces only a local immutable image ID: it applies exactly the two labels named in the Claim and neither tags, pushes, selects, nor deletes an image. The immutable-ID inspection and canary must independently match those labels and the package bytes.

### Selector and Journal intent

The initializer internally reopens the derived retained proof and re-inspects the image before an installation effect; it does not rerun producer effects. Finder metadata is excluded under CA-R-1898. An existing empty public Skill directory retains the ordinary atomic replacement path. For a verified metadata-only directory, retain its exact directory and metadata bytes at the internally derived private sibling `.agents/skills/.ca-retained-metadata-<private suffix>/ca` before the same whole-Skill atomic publication; a changed target containing real Skill state refuses displacement. No member-by-member public Skill publication is admitted. A failed replacement retains the sealed staging and any retained-metadata sibling as actual effect references, exposes no partial Skill as completed, and does not select the package. These private recovery carriers are not another authority or Journal.

The initializer reopens the manifest and selectors only through the CA-D-596, CA-D-598 and CA-D-599 schemas. A canonical started-Run input remains `requested_run_id`, package-manifest SHA-256, sealed source-context SHA-256 and immutable image digest. A `requested_run_id` cannot start a changed intent: a changed binding permits only existing-Run inspection or recovery and creates neither another started evidence entry nor a second source ledger. The target selector defined by CA-D-599 is the sole activation carrier and is written only after a complete Skill publication; separate-directory writes are not treated as one atomic transaction. For first initialization, the target runtime boundary remains empty until that publication; adopting Project metadata does not create an upgrade or idempotency path. Package and Skill contents are regular, project-contained carriers with their manifest digests; no secret-shaped carrier, hook, global configuration, permanent bootstrap setting, source mutation, second registry, caller-selected build input, image tag or checkout reference is delivered. The Action writes its actual installation started and terminal evidence only through the canonical Work Journal; runtime carriers and private image evidence do not become a second Journal.

### Bootstrap-to-N+1 compatibility

The subsequent Release Version reader retains its own N proof and schemas. This first-install Delivery supplies no alternate `candidate_snapshot_manifest_sha256`, `manifest_sha256`, `release`, `selected_release_root`, `framework_engine_root` or `methodology_root` field and does not define an N-to-N+1 compatibility exception. It proves first initialization only through the actual retained package, package selector, target selector, Skill and canonical Journal evidence reopened through CA-D-596, CA-D-598 and CA-D-599.
