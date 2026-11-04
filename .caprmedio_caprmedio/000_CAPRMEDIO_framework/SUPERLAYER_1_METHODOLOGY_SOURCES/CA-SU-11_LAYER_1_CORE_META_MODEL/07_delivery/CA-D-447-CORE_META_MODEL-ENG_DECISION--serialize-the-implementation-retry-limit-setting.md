---
version: 30
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Implementation Retry Limit
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Governing Configuration
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Implementation Retry Limit'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)/(.Header.Form := Plan)'
  - CAPRMEDIO_MODEL <+ Carrier
atom_id: CA-D-447
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize the implementation retry-limit setting

## Claim

### Prose Claim


explicitly selected Implementation Retry Limits.


an explicitly selected Implementation Retry Limit **must** use the integer field assigned **to** its owning source Carrier:

- Framework Instance Settings TOML: `implementation.retry_limit`.
- Default Settings TOML: the same field under CA-D-408-CORE_META_MODEL-DELIVERY--reuse-framework-parameter-fields-in-default-settings.
- a Plan Atom's own File Carrier frontmatter: `implementation_retry_limit`, including a Hub's mandatory Markdown File Carrier.

## Details

### inheritance and ownership

- allowed values follow CA-R-1488@21-CORE_META_MODEL-DEFINITION--define-implementation-retry-limit; the default value is owned **only** by Default Settings.
- omitted instance values resolve under CA-M-279-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-missing-framework-parameters-from-default-settings; omitted Plan fields inherit under CA-M-295-CORE_META_MODEL-METHOD--resolve-implementation-retry-limits-by-source-precedence@7 **without** copied values. preserve explicit **=0**.
- a Hub override belongs **to** that same Plan identity, **not** a separate Objective **or** settings file; do **not** use `epic_overrides`.
- **every** Plan has its own Markdown file **and** DoD under CA-D-460-CORE_META_MODEL-CORE-DELIVERY--serialize-plan-atom-carrier-bundles **and** CA-D-470-CORE_META_MODEL-DELIVERY--serialize-plan-file-sections; its existence does **not** require a selected retry override.
