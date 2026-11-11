---
identity:
  id: CA-P-2766
  ref_id: CA-P-2766
context:
  container:
    atom: CA-P-2715
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2731
state:
  status: Done
  version: 2
  updated_at: 2026-11-09 02:11:53 +0400
destination:
  file:
    name: CA-P-2766-WORK_REPORT--verify-and-locally-release-the-refined-engine.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done
author: Anatoly Maslennikov
---

## Summary

Verify and locally release the refined Engine

## Details

Deployed and verified local release 0.4.4.40. All 251 selected tests and eight isolated Docker E2E cases passed; the separate profiler-off short CPU/RAM and View-result lifecycle gate passed without changed limits. All 105 checked installed production Python modules and both generated schema/relation assets match the release package. Live query_schema exposes dotted paths with snake_case segments, including header.identity.atom_id and content.claim.formal_claim; Mode 2 is enabled. The 171 expected Current source versions match; R2731 is retired. Declared direct/derived bindings have no missing inverse facts. The real-project canary passed all Atom and Scope Unit operations and removed its temporary sources: 48 Scope Units remain, no canary rows or files remain, and all 500 benchmark Atoms are preserved. Ordinary live edit/rename/move visibility was 0.338–0.439 seconds; first/last schema and structural rebuilds took 31.645–40.163 seconds. Release cleanup retained an image without proven Project ownership; deployment itself is healthy. The 78 legacy Atoms, older non-Workbench Tools, standalone chat and native Codex rendering remain explicitly deferred. Code Synopses I4/I5/I6 remain historical Draft reports, not Current implementation authority. Detailed acceptance evidence is in inventory/implementation-evidence.json.
