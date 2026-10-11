---
atom_id: CA-P-1848
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 17
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 8
updated_at: "2026-10-10 19:48:43 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on:
    - "Project"
    - "Plan"
    - "AI Agent"
    - "Operator"
    - "Framework Instance Settings"
    - "Framework Package"
    - "Methodology Source"
    - "Applicable Methodology"
    - "Project Structure"
    - "Requirement"
    - "Method"
    - "Delivery"
    - "Workflow"
    - "Action"
    - "Journal"
    - "Workflow Run"
    - "Carrier"
    - "Scope Unit"
    - "Atom"
    - "Projection"
    - "Status"
    - "Content Role"
    - "Project Settings"
    - "Evaluation"
    - "Tool"
    - "Version"
relations: {}
---
# Summary

Unify installation **and** local/public release cycles

## Objective

the caprmedio Project delivers a reusable beta Framework Package **and** an isolated per-Project runtime **through** complete, tested local **and** public release cycles.

## Details

### Approved boundaries

- **=1** source authority: editable Methodology Atoms belong to declared Project Methodology Scope Units; editable Engine implementation belongs to root `102_FRAMEWORK_ENGINE`.
- Methodology local flow: verify the corrected registrations map authoring Methodology Sources to the Project Methodology unit and that `project_structure.toml` agrees before any installed-target wipe. The installed target is not authoring authority and remains read-only until Local release. From the Project authority, only selected active Methodology-source Atoms (Core Meta-Model, selected extensions and Project Configuration) form non-live preflight inputs. After the full preflight passes, they replace root `101_FRAMEWORK_METHODOLOGY` product contents (no drafts or archive); applicable Methodology compiles there; then only `.caprmedio_caprmedio/000_CAPRMEDIO_framework` is wiped and replaced from the product directory as-is. Preserve `caprmedio_framework_settings.toml`, authoritative configuration, `project_structure.toml`, Operator registry and support settings; generated manifests and selectors refresh. A missing selected revision fails before effects.
- Engine/package local flow: root `102_FRAMEWORK_ENGINE` **plus** delivered Methodology, ca Skill/defaults **and** locked dependencies → reusable beta package under `.caprmedio_install` → runtime execution/state/environments for this Project under `.caprmedio_runtime`. an installed runtime executes its selected package, **not** an implicit development checkout.
- concrete CAPRMEDIO Local/Public Release Operations belong only in the Project root `.caprmedio_caprmedio/09_operations`. Their release helper Tool RMED is authored in `205_FEATURE_PROJECT_TOOLS`, a `PROGRAMMATIC` sibling of `TOOLS`, and delivered at root `PROJECT_TOOLS` outside the reusable Engine. Reusable compiler/installer, shared package/gate models/codecs, detached readers and generic O200 install/bootstrap/restore capability remain in `TOOLS`; no release Operation or helper is delivered as general Methodology or Framework Package content.
- **all** mutable runtime settings belong **in** this Project's `.caprmedio_runtime/config.toml`, outside versioned package bytes. first installation creates admitted defaults **only if** the file is absent; reinstall, replacement **and** failure recovery preserve an existing file byte-for-byte. an incompatible configuration requires an explicit migration **or** an identified blocked result, **not** silent replacement. this runtime configuration does **not** duplicate Project Settings, Framework Instance Settings, generated selectors **or** Journal records.
- the package can install into another Project, including a non-Git Project **or** another root **in** the same repository. Project settings, configuration, runtime records **and** endpoints remain isolated. reuse the same package schema instead of independent Tool-only/full-Engine layouts.
- current `.caprmedio_install` contains operational state; preserve **and** migrate that state **before** package replacement. the destructive phase deletes only the selected installed package tree, never the whole folder: protected/private contents, exact owned migration roots, configuration, Project authority, Journal and transaction evidence are outside that boundary.
- root `101_FRAMEWORK_METHODOLOGY` is the product boundary, not a draft, archive or authoring authority. Its contents are replaced only from the Project's migrated active Methodology authority; account for distinct data and preserve referenced rollback evidence before any affected product replacement.
- other known copies include `.release-sources-*`, `_release_materialized`, nested repeated control roots, older installed package trees **and** empty legacy roots. compare identity, consumers **and** retention **before** consolidation; immutable selected/rollback snapshots are intentional artifacts, **not** extra editable authorities.

### Current implementation scope

- Keep both release Workflows callable through the existing Project MCP. Local release remains programmatic; Public release has exactly one content prompt.
- Keep configuration preservation, existing pre-release test gates, scoped Git checkpoints, canonical Journal records and MCP startup/smoke verification.
- Defer automatic rollback, retry/resume and uncertain-effect recovery. A failed step stops and reports the actual state for manual Operator handling.
- Defer automatic migration of legacy layouts and compatibility paths. Implement the agreed current Project/source/product/installed layout only; retain old files without treating compatibility work as a release prerequisite.
- Defer additional release CLI launchers and command/configuration wrappers. Reuse existing MCP entrypoints and runtime settings instead of introducing a parallel release command surface.
- Deferred portions of existing Tasks remain recorded for later work and do not block this current vertical cut. This deferral does not turn incomplete work into a pass or weaken the required tests before destructive replacement.

### Release cycles and gates

There are exactly two Operator commands. Each performs its internal preparation automatically; source admission, candidate construction, validation, handover and conformance checks are stages, not separately commanded Workflows. CA-R-1799 authorizes one complete public Workflow. Completion of a prior command, a receipt or this Plan never authorizes the other command.

1. **Local release.** First verify the corrected Project source registrations and `project_structure.toml`; treat `.caprmedio_caprmedio/000_CAPRMEDIO_framework` as read-only installed content until the command's later replacement step. Prepare the selected active Methodology-source inputs (Core Meta-Model, selected extensions and Project Configuration), Engine/package candidate, image and required non-live test inputs without changing product or installed contents. Run the complete current suite for this sealed preflight, including required host, image, Docker and MCP end-to-end checks, **before the first destructive product wipe**. On a pass, in this order, wipe product contents in root `101_FRAMEWORK_METHODOLOGY`; replace them from the selected active source; compile applicable Methodology; wipe installed contents under `.caprmedio_caprmedio/000_CAPRMEDIO_framework`; and copy the product directory there as-is. Commit each completed source/product/installed transition to Git, staging only that step's owned changes and never unrelated graph edits. Do not repeat the full suite solely for that deterministic generated product/install copy. Preserve `caprmedio_framework_settings.toml`, authoritative configuration, Project structure, Operator registry and support settings; generated manifests and selectors refresh. Then preserve/migrate Project configuration and state, replace only the selected installed package, install the `ca` skill, install the same sealed package into that Project's `.caprmedio_runtime`, start or reuse its selected image and smoke its returned MCP endpoint. A runtime uses the installed package, never an implicit checkout; another Project remains isolated. No rebuild is permitted between the gate and replacement.
2. **Public release.** Reuse the canonical Version and produce README/documentation updates automatically. Ask one content prompt only: it returns the complete PR description with full “What's new” and “What's fixed” lists and the concise Version History bullet summary. Run the complete current suite for the final publishable closure before effects. On a complete pass, commit and push the safe validated closure to `amm/dev`, then create or update its PR to `main` with that full description; do not merge. Reuse a matching PR URL when known. If a newly created PR returns its URL after push, append the actual URL in a mechanical metadata-only follow-up commit/push; this link-only update needs no second full suite. A product, package, source, configuration or documentation change still requires a fresh complete suite before publication.
3. Every required gate has complete identity and coverage evidence. Failed, blocked, skipped or incomplete checks stop the corresponding command; focused, mock or old receipts do not substitute. Failed effects retain configuration and Project-owned Journal/transaction evidence and report the actual state without an automatic replay or a stale-success claim. `.DS_Store` is ignored, not a gate failure.
4. The two Project Operations Workflows retain their bound Steps, Actions, Project helper Tools and shared-Journal evidence, with parentage and exact input/output identities. Their concrete Operations are in `.caprmedio_caprmedio/09_operations`; release helpers are in `PROJECT_TOOLS`, while reusable compiler/installer and generic package/install capabilities remain in `TOOLS`. The exporter registers ProjectTools D declarations as excluded delivery-boundary content rather than shipping them or rejecting them as outside-Engine. Their internal stages use inherited Framework Instance Settings and the authorized Operator input; they do not add approval, review or retry rituals.

### Work organization

- The five Methodology transitions have separate scoped Git checkpoints: product clear, active-source copy, compilation, installed clear, and installed product copy. Grouping transitions within one Workflow Step does not combine their commits; unchanged or read-only work does not create an empty commit.
- this file **and** its matching folder are Carriers of **=1** Epic Plan. children explicitly store `is_decomposition_of`; prerequisite Plans store `blocks`. navigation numbers/listing order are **not** a separate execution schedule.
- own work for **=1** AI Agent **must** fit **<=15** minutes. larger Plans **must** be decomposed **before** execution. independent ready work may run **in** parallel; source/Git/shared-state integration remains under **=1** owner.
- reuse the existing release/compiler/installer/startup Tools where their contracts remain valid. update RMED **and** O definitions, tests and implementation in the two command contracts; complete-suite validation provides the required release gate without a separately commanded review or handover.
- relocate CAPRMEDIO-specific release Operations/helper code out of general Methodology and Framework Package delivery, preserving reusable compiler/installer, shared package/gate model/codec, detached-reader and generic O200 install/bootstrap/restore capability in `TOOLS`. Register ProjectTools D declarations outside the exporter frontier. This is planned work only, not a code, structure, runtime or Git mutation by this Epic.
- creating this Epic **only** creates planned work. no implementation, migration, deletion, dependency installation, release, push, PR, image/container start **or** merge is executed now.

### Decomposing Plans

Plans 01–19 retain their useful boundary, package, migration, test and public-documentation responsibilities as internal stages of the two commands; they do not create additional Operator commands or approval/review workflows. Explicit blocking Relations remain authoritative.

- [01-CA-P-1849-TASK--specify-installation-and-release-boundaries](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/01-CA-P-1849-TASK--specify-installation-and-release-boundaries.md)
- [02-CA-P-1850-TASK--protect-existing-state-during-installation-migration](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/02-CA-P-1850-TASK--protect-existing-state-during-installation-migration.md)
- [03-CA-P-1851-TASK--consolidate-methodology-source-and-delivery-paths](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/03-CA-P-1851-TASK--consolidate-methodology-source-and-delivery-paths.md)
- [04-CA-P-1852-TASK--export-only-active-methodology](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/04-CA-P-1852-TASK--export-only-active-methodology.md)
- [05-CA-P-1853-TASK--compile-and-install-project-methodology](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/05-CA-P-1853-TASK--compile-and-install-project-methodology.md)
- [06-CA-P-1854-TASK--build-the-reusable-beta-framework-package](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/06-CA-P-1854-TASK--build-the-reusable-beta-framework-package.md)
- [07-CA-P-1855-TASK--install-an-isolated-runtime-for-a-selected-project](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/07-CA-P-1855-TASK--install-an-isolated-runtime-for-a-selected-project.md)
- [08-CA-P-1856-TASK--run-tools-and-docker-mcp-from-the-installed-package](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/08-CA-P-1856-TASK--run-tools-and-docker-mcp-from-the-installed-package.md)
- [09-CA-P-1857-TASK--consolidate-duplicate-delivery-copies-safely](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/09-CA-P-1857-TASK--consolidate-duplicate-delivery-copies-safely.md)
- [10-CA-P-1858-TASK--test-installation-across-fresh-projects](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/10-CA-P-1858-TASK--test-installation-across-fresh-projects.md)
- [11-CA-P-1859-TASK--pass-the-full-test-suite-before-local-release](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/11-CA-P-1859-TASK--pass-the-full-test-suite-before-local-release.md)
- [12-CA-P-1860-TASK--execute-the-gated-local-release-cycle](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/12-CA-P-1860-TASK--execute-the-gated-local-release-cycle.md)
- [13-CA-P-1861-TASK--verify-the-local-installation-and-finalize-its-cleanup](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/13-CA-P-1861-TASK--verify-the-local-installation-and-finalize-its-cleanup.md)
- [14-CA-P-1862-TASK--prepare-public-release-documentation-and-notes](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/14-CA-P-1862-TASK--prepare-public-release-documentation-and-notes.md)
- [15-CA-P-1863-TASK--pass-the-full-test-suite-before-public-release](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/15-CA-P-1863-TASK--pass-the-full-test-suite-before-public-release.md)
- [16-CA-P-1864-TASK--commit-and-push-the-validated-release-to-amm-dev](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/16-CA-P-1864-TASK--commit-and-push-the-validated-release-to-amm-dev.md)
- [17-CA-P-1865-TASK--open-the-release-pr-from-amm-dev-to-main](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/17-CA-P-1865-TASK--open-the-release-pr-from-amm-dev-to-main.md)
- [19-CA-P-1871-TASK--finalize-version-history-with-the-verified-release-pr-link](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/19-CA-P-1871-TASK--finalize-version-history-with-the-verified-release-pr-link.md)
- [18-CA-P-1866-TASK--review-both-release-cycles-against-their-authority](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/18-CA-P-1866-TASK--review-both-release-cycles-against-their-authority.md)

### Definition of Done

the Plan is **not** Done **if** ((**any** in-scope direct decomposing Plan is **not** Done) **or** (a required full-suite gate lacks a complete current pass for sealed bytes) **or** (the beta package cannot install/run **without** the development checkout) **or** (Methodology source/projection/package/runtime boundaries conflict) **or** (installation replaces existing runtime configuration) **or** (state/history/another Project is lost **or** leaked) **or** (the local installation/MCP handoff is unverified) **or** (`amm/dev` **and** its PR to `main` are unconfirmed) **or** (an essential RMED/Operations/principle finding remains)).
