---
identity:
  id: CA-P-2851
  ref_id: CA-P-2851
context:
  container:
    scope_unit: CA-SU-15
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  tier: 4
state:
  status: Done
  version: 1
  updated_at: 2026-11-10 00:31:33 +0400
destination:
  file:
    name: CA-P-2851-WORK_REPORT--2850.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan
author: Anatoly Maslennikov
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2850
---

## Summary

Archive retired Tool Scope Units

## Details

Work started after the Operator authorized archival to parent Scope Units and removal of the retired units and declarations. The identified set is CA-SU-2 through CA-SU-8. Four lanes cover six Tool scopes, orchestrator authority, retained MCP runtime relocation, and inbound references.

The installed mutation context returned internal_failure. The previously authorized manual fallback is in use. No archival, deletion, test or runtime activation result is claimed by this initial checkpoint.

### Verified retirement checkpoint

The Operator’s final decision retires Workflow Orchestrator; no engine was restored. CA-SU-2 through CA-SU-8 and their seven Current declarations are removed. The direct declaration reader and Project binding resolve 41 Scope Units instead of 48.

The Tool-scope ledger accounts for 224 unique original carriers: 19 Current carriers archived with unchanged bodies, Versions and Updated At; 205 historical/noncurrent carriers relocated byte-for-byte. The Orchestrator ledger accounts for 759 carriers: 30 Current archived under APPS, four shared MCP contracts rehomed Current (R1901, M504, E600, E796), and 725 historical/noncurrent carriers preserved byte-for-byte. Six native Actions O112–O117 and their six delivered mirrors were archived separately. Existing archived/Draft history was preserved as recorded, without broad legacy normalization.

The parent closure archived nine obsolete selected-route/catalog contracts (R1847, R1848, D547, D548, E567, E568, C576, C584, R2785). R2659, R1100, M196 and E314 now omit the removed Orchestrator topology; R1626 cites the retained Core Step authority R1789.

FRAMEWORK_DELIVERY no longer depends on the retired host worker/recovery protocols. Twelve obsolete recovery/private-worker contracts were archived; R1891, M347, E590 and D583 retain direct-host release authority. O181 and O183 use the current MCP runtime-test locations. Local/public release functionality remains in FEATURE_PROJECT_TOOLS.

Twenty-four live Docker/runtime files and 202 test/fixture/helper files moved from the old Orchestrator delivery directory to FEATURE_MCP/docker and FEATURE_MCP/tests. Ignored old-directory residue was moved into the retirement scratch directory rather than deleted. The old delivery path is absent. Its first focused relocation checks passed 24 modules / 180 tests.

### Verified shared registration

The Operator chose the existing generated-registry RMED approach, an editable provider inventory, and an explicit global MCP blacklist. R3013, M506, D704, E798 and E810 were reconciled narrowly with that choice while preserving their Headers and Summaries. The inventory/generator/runtime and release/image generation gates are implemented. Initial tests prove a provider can be added through inventory and generation without a gateway edit, with blacklist listing/direct-call denial.

Independent review found duplicate-JSON-key, provider-lifecycle, schema-validation, generic-result presentation and runtime-error classification defects. All five were fixed and the independent re-review passed. The registry rejects duplicate JSON keys and invalid schema versions, validates metadata before creating Providers, validates generic request/result schemas, keeps Workbench-specific presentation inside its Provider, and reports blocking registry faults at ERROR level.

The editable inventory is `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/tool_providers.json`; `tool_registry.json` is generated from it. The inventory currently registers the 28-Tool Workbench Provider and explicitly blacklists 30 retired or host-only names. Global denial filters discovery and direct invocation; Project exclusions can only narrow access. Provider additions require inventory and implementation changes plus generation, without a central gateway Tool-name allowlist edit.

### Final focused verification

- Registry regression checks: 13 passed; focused MCP/shared/HTTP checks: 42 passed.
- Native Workspace end-to-end checks: eight passed; shared multi-Project isolation: two passed. These host-native checks passed outside the filesystem-event sandbox.
- Final release-package checks: 29 passed; release registry boundary: eight passed; Dockerfile generation contract: three passed. These check packaging and image admission logic without building an image.
- Additional focused image safety/launcher/metadata checks passed (nine, 12 and nine respectively), as did two full-suite-image-build contract checks.
- Standalone registry generation passed with inherited PYTHONPATH removed. The lockfile check, declared two-file typing scope, Ruff and final diff whitespace check passed; this is not a whole-project type-check or full-suite claim.
- Live Workbench readback reports 41 Scope Units and zero retired Scope Units. A separate readback of 80 obsolete/declaration identities found no Current carriers; the four retained MCP contracts remain Active under CA-SU-21.

The broader Code Synopsis review remains C714/P2847; I9’s moved entrypoint locator alone was rebased.

Proof ledgers and verification output are under `.caprmedio_tmp/scope-retirement-20261110/`. No build, release, deployment or post-checkpoint Git publication has occurred.
