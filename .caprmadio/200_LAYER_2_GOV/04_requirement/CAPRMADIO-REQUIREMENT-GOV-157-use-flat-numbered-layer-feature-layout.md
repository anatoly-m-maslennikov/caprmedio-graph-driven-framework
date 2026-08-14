---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-157
scope_path: layer:gov
subject_scopes:
  - layout
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-131-nine-content-roles-with-plan
    - CAPRMADIO-REQUIREMENT-META-139-use-canonical-carrier-address-as-authority
    - CAPRMADIO-REQUIREMENT-META-143-use-flat-layer-owned-feature-scopes
    - CAPRMADIO-REQUIREMENT-META-172-share-canonical-features-across-spec-and-implementation
---

# Use a flat numbered Layer–Feature layout

The `.caprmadio/` root contains the installed-framework boundary, project settings, generated control carriers, and numbered Layer scopes. It must not contain project-level Content-role directories. Every governed semantic carrier has exactly one Layer owner.

Explicit Layer and Feature scope directories are flat siblings and use these uppercase fixed-width grammars:

```text
<L>00_LAYER_<L>_<LAYER_NAME>/
<L><FF>_FEATURE_<FEATURE_NAME>/
```

`L` is the one-digit Layer order and is repeated in the Layer label because Layer order is a mandatory visible identity. `FF` is the two-digit Feature order within that Layer from `01` through `99`. A Feature's first digit identifies its sole parent Layer. Layer and Feature names use `UPPER_SNAKE_CASE`.

Every Layer and Feature scope materializes only the lowercase Content-role directories it uses:

```text
01_concern/
02_analysis/
03_plan/
04_requirement/
05_method/
06_assurance/
07_delivery/
08_implementation/
09_ops/
```

Active Atoms live directly in their role directory, pre-admission candidates live under `drafts/`, and inactive Atoms live unchanged under `archive/`. Their placement is authoritative and is not repeated as embedded lifecycle metadata.

The canonical Layer and Feature structure is:

```text
100_LAYER_1_META/
200_LAYER_2_GOV/
300_LAYER_3_SPEC/
301_FEATURE_METHODOLOGY/
302_FEATURE_TOOLS/
303_FEATURE_SKILLS/
304_FEATURE_PROFILES/
305_FEATURE_ADAPTERS/
306_FEATURE_ASSURANCE/
307_FEATURE_DOCUMENTATION/
400_LAYER_4_IMPLEMENTATION/
401_FEATURE_METHODOLOGY/
402_FEATURE_TOOLS/
403_FEATURE_SKILLS/
404_FEATURE_PROFILES/
405_FEATURE_ADAPTERS/
406_FEATURE_ASSURANCE/
407_FEATURE_DOCUMENTATION/
500_LAYER_5_DELIVERY/
600_LAYER_6_OPS/
```

The installed framework boundary `000_caprmadio_framework/` is outside the Layer and Feature number space and is governed separately. Native source code, executable tests, skill packages, configuration, CI, and other Implementation remain in their prescribed repository locations outside `.caprmadio/`.
