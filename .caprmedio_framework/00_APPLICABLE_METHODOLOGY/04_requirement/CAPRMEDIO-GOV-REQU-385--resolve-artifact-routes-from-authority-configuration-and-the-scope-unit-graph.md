---
cce_version: cce_1
cce_form: resolution
subjects:
  governs:
    occurrent:
      - Artifact Classification Resolution
  depends_on:
    continuant:
      - Applicable Methodology
      - Local Configuration
      - Scope Unit Graph
version: 14
updated_at: 2026-08-29 02:40:41 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-GOV-REQU-385--resolve-artifact-routes-from-authority-configuration-and-the-scope-unit-graph.md
---
# Resolve Artifact Classification from Authority and Configuration

CAPRMEDIO **must** resolve **every** Artifact Content Role, Type, **and** semantic route from Applicable Methodology, Local Configuration, **and** current Scope Unit Graph context **and** **must** fail on an unknown, disabled, stale, multiply mapped, **or** ambiguous classification.
