# Applied project-wide CAPRMADIO artifacts

## Purpose

Project-level carriers live directly in the ordered Content-role folders under
`.caprmadio`. Structural scopes repeat the same role layout beneath their own
directories.

## Boundaries

Layer-specific truth belongs to the corresponding applied layer. The external
installed methodology remains isolated under `000_caprmadio_framework`.
Native implementation remains outside `.caprmadio`; only governed
Implementation carriers and journals belong under `07_IMPLEMENTATION`.

```mermaid
flowchart TB
    ROOT[".caprmadio"]
    METHODOLOGY["000_caprmadio_framework<br/>external installed methodology"]
    PROJECT["Project roles<br/>01_CONCERN … 08_OPS"]
    META["101 META scope"]
    GOV["102 GOV scope"]
    SPEC["103 SPEC scope"]
    TOOL["103 TOOL scope"]
    SKILL["104 SKILL scope"]
    IMPL["105 IMPL scope"]
    OPS["106 OPS scope"]

    ROOT --> METHODOLOGY
    ROOT --> PROJECT
    ROOT --> META
    ROOT --> GOV
    ROOT --> SPEC
    ROOT --> TOOL
    ROOT --> SKILL
    ROOT --> IMPL
    ROOT --> OPS
```

## Start here

- Project roles: `01_CONCERN` through `08_OPS`, materialized when used.
- Structural scopes: `101_layer_meta` through `106_layer_ops`.
- Installed methodology: `000_caprmadio_framework`.
- Settings: `caprmadio_settings.toml`.
