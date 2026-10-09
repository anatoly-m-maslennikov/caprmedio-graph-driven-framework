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
version: 1
updated_at: "2026-10-09 15:41:25 +0400"
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
- Methodology local flow: selected active source Atoms **and** declared support artifacts **from** `.caprmedio_caprmedio` → root `methodology/` → compiled/traceable installation under `.caprmedio_caprmedio/000_CAPRMEDIO_framework`. compilation applies this Project's selected extensions/configuration; installed projections retain their relation to original source Atoms.
- Engine/package local flow: root `102_FRAMEWORK_ENGINE` **plus** delivered Methodology, ca Skill/defaults **and** locked dependencies → reusable beta package under `.caprmedio_install` → runtime execution/state/environments for this Project under `.caprmedio_runtime`. an installed runtime executes its selected package, **not** an implicit development checkout.
- the package can install into another Project, including a non-Git Project **or** another root **in** the same repository. Project settings, configuration, runtime records **and** endpoints remain isolated. reuse the same package schema instead of independent Tool-only/full-Engine layouts.
- current `.caprmedio_install` contains operational state; preserve **and** migrate that state **before** package promotion. repair the installer that deletes the whole folder as legacy. protected/private contents **and** unrelated Project resources are outside blanket cleanup.
- root `101_LAYER_1_FRAMEWORK_METHODOLOGY` is currently a derived delivery copy. migrate its delivery role/consumers into `methodology/`, account for its distinct data **and** retire its redundant role; do **not** delete authoring source **or** referenced rollback evidence.
- other known copies include `.release-sources-*`, `_release_materialized`, nested repeated control roots, older installed package trees **and** empty legacy roots. compare identity, consumers **and** retention **before** consolidation; immutable selected/rollback snapshots are intentional artifacts, **not** extra editable authorities.

### Release cycles and gates

1. local cycle: **before** real publication/cutover, freeze the inputs/Version **and** pass the full current test suite, including required host/Docker/MCP e2e checks. then explicitly invoke the local Workflow to export, compile, package, migrate/install, install ca, build/admit the image, start/reuse the selected Project's container **and** verify its returned MCP endpoint.
2. public cycle: check/update README, synchronize the canonical Version **and** prepare a good full PR description; place **only** its concise bullet-point summary **in** `VERSION_HISTORY.md`. **before** publishing, run a fresh full suite for that final snapshot. commit/push **all** safe validated changes to `amm/dev`, then create/update the PR to `main` **with** the full description. merging is **not** requested.
3. **every** required gate has complete coverage/identity evidence. failed, blocked, skipped **or** incomplete required checks stop the corresponding cycle; no focused/mock/old receipt substitutes for a full pass. `.DS_Store` is ignored, **not** a gate failure.
4. preserve N while preparing/admitting N+1. new source/package/configuration changes that affect a validated closure require renewed acceptance. local runtime mutation **and** cleanup occur **only** **after** the local gate, **not** as a side effect of planning.
5. Workflow **and** Action Runs are recorded **in** the shared Journal **with** honest outcomes; uncertain effects are **not** automatically replayed. inherit confidence/retry/permission controls **from** Framework Instance Settings **and** applicable Operator input rather than invent another policy.

### Work organization

- this file **and** its matching folder are Carriers of **=1** Epic Plan. children explicitly store `is_decomposition_of`; prerequisite Plans store `blocks`. navigation numbers/listing order are **not** a separate execution schedule.
- own work for **=1** AI Agent **must** fit **<=15** minutes. larger Plans **must** be decomposed **before** execution. independent ready work may run **in** parallel; source/Git/shared-state integration remains under **=1** owner.
- reuse the existing release/compiler/installer/startup Tools where their contracts remain valid. update RMED **and** O definitions first, then tests **and** implementation; independent review checks code against those definitions.
- creating this Epic **only** creates planned work. no implementation, migration, deletion, dependency installation, release, push, PR, image/container start **or** merge is executed now.

### Decomposing Plans

preparation: Plans 01–10; local cycle: 11–13; public cycle: 14–17; integrated closure: 18. explicit blocking Relations are authoritative.

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
- [18-CA-P-1866-TASK--review-both-release-cycles-against-their-authority](17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles/18-CA-P-1866-TASK--review-both-release-cycles-against-their-authority.md)

### Definition of Done

the Plan is **not** Done **if** ((**any** direct decomposing Plan is **not** Done) **or** (a required full-suite gate lacks a complete current pass) **or** (the beta package cannot install/run **without** the development checkout) **or** (Methodology source/projection/package/runtime boundaries conflict) **or** (state/history/another Project is lost **or** leaked) **or** (the local installation/MCP handoff is unverified) **or** (`amm/dev` **and** its PR to `main` are unconfirmed) **or** (an essential RMED/Operations/principle finding remains)).
