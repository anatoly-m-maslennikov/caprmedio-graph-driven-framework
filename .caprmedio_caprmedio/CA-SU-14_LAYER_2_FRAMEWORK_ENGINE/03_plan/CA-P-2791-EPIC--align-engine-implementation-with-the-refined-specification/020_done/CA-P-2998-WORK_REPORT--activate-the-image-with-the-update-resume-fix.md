---
identity:
  id: CA-P-2998
  ref_id: CA-P-2998
context:
  container:
    atom: CA-P-2791
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Done
  version: 1
  updated_at: 2026-11-11 20:08:17 +0400
destination:
  file:
    name: CA-P-2998-WORK_REPORT--activate-the-image-with-the-update-resume-fix.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2934
author: Anatoly Maslennikov
---

## Summary

Activate the image with the Update resume fix

## Details

The current-code image includes the Update resume fix and 16 verified native placement inputs. The exact-image canary passed public Archive and Change Status on a disposable Project. Live health, Workbench frontend and HTTP query, and MCP query_run passed after activation.

Both Workbench guards passed. Cold indexing took 25.2 seconds. The 500-Atom batches took 2.5–6.5 seconds. The resource guard peaked at 524 MiB with zero OOM kills. CA-C-730 tracks admission for the four authoring tools.
