---
identity:
  id: CA-P-2922
  ref_id: CA-P-2922
context:
  container:
    atom: CA-P-2791
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Atom
  tier: 4
state:
  status: Done
  version: 1
  updated_at: 2026-11-11 02:23:40 +0400
destination:
  file:
    name: CA-P-2922-WORK_REPORT--verify-the-retained-mcp-and-workbench-image.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2818
  - CA-P-2815
  - CA-P-2812
author: Anatoly Maslennikov
---

## Summary

Verify the retained MCP and Workbench image

## Details

Workflow-engine work is deferred in P2791/P2912/P2860 and C727. It does not block the retained image; no executor, scheduler, routing, Run history or recovery was added.

Built and admitted image `sha256:c6e5cfb3e431582a495673dd00cb1cc5113c46a47592761d853b79cedd0abcf1` (0.4.4.40). The first build was rejected after concurrent source changes; the stable-window build passed. Verified ownership of one stopped obsolete Project container and removed it. The normal Project launcher then reported READY_STARTED on port 56317. Health and Workbench return HTTP 200.

Actual MCP query_schema/query_run/query_check passed over 3,976 indexed Atoms: JSON-matrix result file by default, explicit inline rows, preview zero, metadata-only Check and rejected SQL UPDATE. Browser row requests now explicitly use inline delivery. The real browser result-grid, Compact layout and completion checks each passed after correcting their fixture/selector/readiness issues. Focused checks: 8 Backend delivery cases, 4 MCP adapter cases, 9 Workbench HTTP cases and 20 frontend helper/config cases passed. One post-start Docker sample reported 302 MiB and 0.45% CPU; this is not a soak or peak measurement.

Evidence: `.caprmedio_tmp/CA-P-2791/CA-P-2818/` contains image-build/start logs, image-smoke.json, browser logs and test logs. Full-suite, final performance/resource/soak acceptance and the complete local-release workflow were not run in this batch. P2791/P2817/P2818 remain open. No push was performed.
