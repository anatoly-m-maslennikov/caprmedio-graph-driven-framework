# Applied project-wide DSET artifacts

## Purpose

This directory owns current project-wide atomic artifacts, evergreen
specifications and plans, analysis, promoted evidence, and verification for
the repository that develops DSET.

## Boundaries

Layer-specific truth belongs to the corresponding applied layer. Installed
methodology is referenced by unique identity and never duplicated here.
Historical aggregates and completed migration records are inert repository
history outside `.carmadio` and are not project-control inputs.

```mermaid
flowchart LR
    PROJECT["100 Project"]
    META["101 META"]
    GOV["102 GOV"]
    TOOL["103 TOOL"]
    SKILL["104 SKILL"]
    IMPL["105 IMPL"]
    OPS["106 OPS"]
    VERSION["150 Versions"]

    PROJECT --> META --> GOV --> TOOL --> SKILL --> IMPL --> OPS
    PROJECT --> VERSION
```

## Start here

- `CARMADIO-META-HUB.md`
- `CARMADIO-GOV-HUB.md`
- `CARMADIO-TOOL-HUB.md`
- `CARMADIO-SKILL-HUB.md`
- `CARMADIO-IMPL-HUB.md`
- `CARMADIO-OPS-HUB.md`
- `CARMADIO-VERSIONS-HUB.md`
- `000_dset-methodology-hub.md`
