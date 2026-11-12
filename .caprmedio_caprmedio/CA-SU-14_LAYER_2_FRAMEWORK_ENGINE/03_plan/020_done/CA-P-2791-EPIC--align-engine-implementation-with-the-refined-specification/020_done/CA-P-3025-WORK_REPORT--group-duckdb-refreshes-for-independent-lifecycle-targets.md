---
identity:
  atom_id: CA-P-3025
  ref_id: CA-P-3025
context:
  role: plan
  form: work_report
  container:
    atom: CA-P-2791
  label: Work Report
  tier: 4
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-3014
state:
  version: 1
  status: done
  updated_at: '2026-11-12T02:41:17.711374+00:00'
destination:
  file:
    name: CA-P-3025-WORK_REPORT--group-duckdb-refreshes-for-independent-lifecycle-targets.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
---
## Summary

Group DuckDB refreshes for independent lifecycle targets

## Details

Compared two batches of 50 on matching disposable Docker fixtures. Archive used one refresh instead of 50. Promote used two instead of 51, including the load of exact predecessors. The two batches took 13.7 s grouped and 29.0 s ungrouped. The final query showed 50 Current and 50 Archived rows. Focused checks cover dependent targets and publication after a partial failure.

Verified image `sha256:7607f7793de81d53b1d68b31c49ebe97c5dde9d2214b2318b44142dec92599f1`.
