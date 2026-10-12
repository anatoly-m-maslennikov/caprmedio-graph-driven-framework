---
atom_id: CA-P-1849
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-10 18:58:38 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on: [Project, Plan, AI Agent, Operator, Framework Instance Settings, Framework Package, Methodology Source, Applicable Methodology, Project Structure, Requirement, Method, Delivery, Workflow, Action, Journal]
relations:
  is_decomposition_of: [CA-P-1848]
  blocks: [CA-P-1850, CA-P-1851, CA-P-1852, CA-P-1853, CA-P-1854]
---
# Summary

Specify installation **and** release boundaries

## Objective

the AI Agent establishes the RMED **and** Operations contract that separates a reusable beta Framework Package **from** a selected Project runtime **and** defines the local **and** public release cycles.

## Details

1. Define exactly two Operator commands: Local release and Public release. Internal source admission, preparation, validation, commit and conformance stages execute inside their command; no stage is separately commanded, approved or handed over.
2. Before any installed-methodology wipe, verify the corrected registrations point authoring Methodology Sources to the Project Methodology unit and that `project_structure.toml` agrees. The installed target is read-only until Local release. Only active Methodology-source atoms (Core Meta-Model, selected extensions and Project Configuration) form non-live preflight inputs; Project Engine, Plans and other atoms are excluded.
3. Define Local release's ordering: prepare the candidate and run its complete preflight suite **before the first destructive product wipe**; then clear root `101_FRAMEWORK_METHODOLOGY`, replace it from the selected source, compile applicable Methodology, clear the installed target and copy the product directory as-is to `.caprmedio_caprmedio/000_CAPRMEDIO_framework`. Do not repeat the full suite solely for this deterministic generated copy. Preserve `caprmedio_framework_settings.toml`, authoritative configuration, Project Structure, Operator registry and support settings; generated manifests/selectors refresh. Commit only each step's owned changes.
4. Define full-suite, state-isolation, Journal and honest-failure contracts for both commands. The Local command prepares the reusable package and per-Project runtime, installs `ca`, and proves image/restart/MCP smoke only after the complete preflight suite passes.
5. Define Public release under CA-R-1799: one content prompt produces the full PR description and concise Version History bullets; the command runs its complete suite before commit/push to `amm/dev` and PR create/update to `main`, without merge. A known matching PR URL is reused; a new URL receives a metadata-only follow-up commit/push without a second suite.
6. Place concrete Local/Public Release Operations only in `.caprmedio_caprmedio/09_operations`. Place release helper Tool RMED in `205_FEATURE_PROJECT_TOOLS` under `PROGRAMMATIC`, delivered at root `PROJECT_TOOLS` outside the reusable Engine; retain reusable compiler/installer, shared package/gate models/codecs, detached readers and generic O200 install/bootstrap/restore capability in `TOOLS`. Plan relocation/exclusion of project release code and ProjectTools D declaration exporter boundary from general Methodology/framework-package delivery.

### Decomposing Plans

- [01-CA-P-1867-TASK--update-local-installation-and-release-contracts](01-CA-P-1849-TASK--specify-installation-and-release-boundaries/01-CA-P-1867-TASK--update-local-installation-and-release-contracts.md)
- [02-CA-P-1868-TASK--specify-the-portable-package-and-installation-tools](01-CA-P-1849-TASK--specify-installation-and-release-boundaries/02-CA-P-1868-TASK--specify-the-portable-package-and-installation-tools.md)
- [03-CA-P-1869-TASK--define-the-public-release-workflow-and-tool-contract](01-CA-P-1849-TASK--specify-installation-and-release-boundaries/03-CA-P-1869-TASK--define-the-public-release-workflow-and-tool-contract.md)
- [04-CA-P-1870-TASK--reconcile-and-validate-installation-release-contracts](01-CA-P-1849-TASK--specify-installation-and-release-boundaries/04-CA-P-1870-TASK--reconcile-and-validate-installation-release-contracts.md)

### Definition of Done

the Plan is **not** Done **if** either command or an internal stage remains unspecified, authoring sources can be wiped as installed content, a source/product/installed boundary conflicts, a release Operation/helper is delivered as general Methodology/framework package, reusable generic capability leaves `TOOLS`, ProjectTools D declarations ship in or fault the exporter frontier, the complete-suite gate or failure/isolation contract is missing, or the Public command needs more than its one content prompt.
