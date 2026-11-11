---
atom_id: CA-D-604
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 10
updated_at: "2026-10-14 20:53:35 +0400"
subjects:
  governs: "Framework Installation contribution/Generation and release proof"
  depends_on: [Tool, Runtime, Framework Package, Command, Docker Image, Journal]
relations:
  delivery_for: [CA-R-1913, CA-R-1918, CA-M-362]
---
# Summary

Retain generation, command and release proof

## Scope

The evidence that one runtime execution belongs to one activated package and target context.

## Claim

the INSTALL_TOOLS facade **must** bind every runtime process observation to state generation, command and package release proof, and **must not** accept a PID-only assertion as execution identity.

## Details

`.caprmedio_runtime/installation/generations/<state_generation>/release-proof.toml` contains package manifest SHA-256, `framework_version`, version carrier SHA-256, source catalog SHA-256, Full Gate receipt SHA-256, immutable image digest, target context SHA-256 and selector SHA-256. `command.toml`, `environment.toml`, and `wrapper` use the single canonical native schema in CA-D-601-TOOLS-DELIVERY--bind-package-owned-runtime-environment-and-wrappers; their fields are not redefined here. `process.toml`, if present, contains a transient PID only beside those immutable bindings and observed start token.

The generation directory uses the positive integer generation defined by CA-D-601-TOOLS-DELIVERY--bind-package-owned-runtime-environment-and-wrappers and is written under CA-D-603-TOOLS-DELIVERY--serialize-per-project-installation-lock and retained across a later generation. A process observation with a changed selector, command, package, context or generation is stale even when its PID remains live. No process record grants selector publication, migration cleanup or retry authority.

### Native proof staging

The closed native `release-proof.toml` keys are `schema_version = 2`, `package_manifest_sha256`, `framework_version`, `version_toml_sha256`, `source_catalog_sha256`, `full_gate_receipt_sha256`, `image_digest`, `target_project_context_sha256`, `state_generation`, `installation_lock_generation`, `installation_command_sha256`, `command_sha256`, `command_stage_manifest_sha256`, `methodology_delivery_manifest_ref`, `methodology_delivery_manifest_sha256`, and `selector_sha256`.

`methodology_delivery_manifest_ref` is the normalized Project-relative path of the actual compiler-owned delivery manifest at this target's declared Applicable Methodology output. `methodology_delivery_manifest_sha256` hashes that file's complete bytes, not its self-excluding semantic digest. Reopen the manifest's canonical schema, context/package/catalog/compiler/source bindings and every declared output byte and mode before deriving these proof fields. A caller-provided digest, another Project's manifest or a matching Boolean does not substitute for that reopening. The prepared target compilation is completed before destructive replacement; selected promotion retains the exact candidate compilation accepted by its Full Gate. Final admission reopens the same delivery manifest and output tree. Prior schema-1 proof remains historical evidence; do not supply missing Methodology evidence by assumption.

A staged proof lives with the exact prospective `selector.toml` bytes under `.caprmedio_tmp/installation/proofs/<installation_lock_generation>`, both mode 0600. The concrete installation lock remains held while creating and reopening these regular carriers. For an already selected package, the writer physically reopens the D598 package/selector, persisted D600 context and D601 command-stage carriers. Before selection, it instead reopens the sealed candidate package and its actual retained Full Gate plus exact prospective D598 bytes, under the same concrete installation lock. A prospective selector is not current authority. Persisting a candidate context is non-active preparation, not runtime activation. It derives package/version/catalog/Full Gate/image facts from those reopened carriers, not caller strings. The command-stage manifest byte hash binds all staged command files. `installation_command_sha256` equals the lock's command binding; `command_sha256` is the separate prospective runtime command digest.

The raw prospective selector must use the closed D599 native schema and match that same package, context, positive integer generation, lock generation and immutable image. `selector_sha256` hashes those exact bytes without changing their formatting. This avoids a cycle: render selector bytes, hash them, render proof, then publish the already-rendered selector only after the complete installation is independently admitted.

The reader reopens and validates all of the same byte and typed bindings. Staging and successful reading confer no Operator authority or Full Gate pass, publish no selector, write no configuration or process state, and do not reuse legacy string-generation proof writers. The later admitted publisher copies the verified proof to the final native generation, then publishes those same selector bytes last.

### Installation command

CA-O-200 has its own direct installation command; the CA-O-199 source-admission receipt does not authorize it. The canonical JSON command input has exactly `schema_version = 1`, `operation = install_framework_runtime`, `command_id`, `operator`, `journal_author`, `operators_registry_sha256`, `action_source`, `target_project_context_sha256`, `package_manifest_sha256`, `full_gate_receipt_sha256` and `prior_runtime_selector_sha256`. The final field is null for a physically empty bootstrap or the exact observed native/legacy selector digest for replacement. `action_source` has exactly `atom_id = CA-O-200`, `version`, `path` and `sha256`, reopened from admitted Action bytes. The registered account is explicit; no display-name inference or permission Boolean is used.

Canonical UTF-8 JSON uses sorted keys, compact separators, no trailing newline and no self-digest. Retain exact input at a safe digest-named Project-relative path before the actual direct Action start, then reopen the retained input and actual Action/source binding before staging, independently of Journal append or receipts. The lock's `command_sha256` is this input's actual byte hash. These records do not grant permission for a different target, package, replacement or retry.

Account resolution follows CA-D-494-CORE_META_MODEL-DELIVERY--store-operator-registry-in-project-root: use the explicit `journal_author` mapping, or the exact registered `name` when that name already is a valid Journal account. Converting a human display name to an account alias is not permitted.

Candidate-aware command, native-proof and MCP readers validate the same complete physical package, context, inventory, fields and modes as installed readers, but accept the exact prospective package/runtime selector bytes instead of requiring live selectors to be published first. The publisher must physically reopen the retained Full Gate; neither a typed handoff nor a prospective proof asserts a pass. After installation, the unchanged installed readers reopen the actual final carriers. This breaks the staging/activation cycle without relaxing post-installation validation.

### Selected promotion command

The existing selected CA-O-169 promotion uses its own actual Action Run, not a manufactured CA-O-200 Run. Its immutable command uses the same canonical JSON and digest-addressed `.caprmedio_runtime/installation/commands/<sha256>.json` carrier. This separate closed variant has the direct-command keys above, with `operation = promote_selected_runtime`, an `action_source` pin for the actually selected CA-O-169 revision, and exactly one additional key: `parent_lineage`. The former `selected_start_receipt` Journal-proof field is not required or supplied.

`parent_lineage` is the ordered list of actual parent Run IDs supplied by the existing selected Session. Before retaining the command or acquiring its publication lock, the selected provider revalidates its actual Action Run, source, frozen selected inputs and existing authorization independently of the Journal. The command's Operator and Journal account resolve through the exact registered mapping. A command, context or lineage assertion alone grants no authority. Historical command readers reopen the retained exact command bytes and their Action, Operator/account, lineage, package and context bindings; they do not reconstruct a live Session, require a Journal start or receipt, or assert current execution authority.

For subsequent-command discovery of a selected installed generation, reopen the retained actual CA-O-169 result, immutable command, observed publication and original gate closure; a promoted flag or checkpoint alone is insufficient. Their exact physical bindings and actual completed source outcome must agree, without a prior Journal entry, terminal recording or receipt prerequisite. Completion of later retirement or of the enclosing Workflow is not required for this association. The installation's own prepublication and final validation retains its already-bound concrete gate and actual readback. Discovery grants no replay or fresh execution permission and creates no Run, start-facts ledger or Journal proof.

### Direct installed-generation association

1. A completed direct installation result retains observed effect rows for the exact original gate closure, using these kinds: `full_gate_receipt`, `retained_candidate_descriptor`, `retained_package_sidecar`, `unit_gate_receipt`, `build_receipt`, `verification_receipt` and `e2e_gate_receipt`. Every reference is an actual Project-contained regular carrier with its original raw byte digest. Retain and reopen the unchanged original closure before destructive effects; do not manufacture a replacement receipt, infer a locator from an aggregate digest or select the latest available receipt.
2. For subsequent-command discovery, reopen the actual retained direct Action result and its immutable installation command. Its completed source outcome, command/context/package/generation bindings and every required physical effect must agree, independently of Journal history, terminal recording or receipts. The existing typed gate evidence and descriptor/sidecar relations determine the artifact and package roots; references never grant permission for another root or execution. Missing, ambiguous, changed or incomplete retained physical association blocks that discovery. The installation's own prepublication and final validation instead uses its already-bound concrete gate; it does not require its future terminal event.
3. Direct installed-generation discovery decodes that original typed gate closure and independently revalidates its package, proof, selectors and all gate receipt bindings. It creates no selected Workflow, parent lineage, new Action start or replay permission. Historical results without the required original references remain historical evidence, not a guessed current association.

### Direct installation result

An actual CA-O-200 execution retains its immutable canonical JSON result at `.caprmedio_tmp/installation/results/<actual-action-run-id>/result.json`, mode 0600, before recording its actual observations in the plain Project Journal. Its closed keys are `schema_version = 1`, `action_id = CA-O-200`, `action_run_id`, `installation_command_sha256`, `package_manifest_sha256`, `target_project_context_sha256`, `state_generation`, `effect_outcome`, `reason` and `effects`. The outcome is one of `completed`, `blocked_before_delete`, `unavailable_after_delete` or `effect_uncertain`; `reason` is a string or null. Every effect has exactly `kind`, safe Project-relative `reference` and the observed byte `sha256`. Effects describe actual retained carriers, not intended effects. The retained source-effect result is independent of Journal append/read: report actual logging I/O failure with the original result reference without changing the observed effect outcome, requiring receipts, introducing retry/recovery machinery or replaying installation. Selected CA-O-169 keeps its existing shared Session result/checkpoint transport rather than creating this direct-Action result or another Run.
