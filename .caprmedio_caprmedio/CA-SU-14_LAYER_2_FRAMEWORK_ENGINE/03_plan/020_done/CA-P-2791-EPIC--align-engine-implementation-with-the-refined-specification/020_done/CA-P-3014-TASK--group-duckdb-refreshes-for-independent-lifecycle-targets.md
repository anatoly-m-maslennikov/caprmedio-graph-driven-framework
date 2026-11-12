---
identity:
  atom_id: CA-P-3014
  ref_id: CA-P-3014
context:
  role: plan
  form: Plan
  label: Task
  tier: 4
  container:
    atom: CA-P-2791
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
relations:
  IS_BLOCKED_BY:
  - CA-P-3010
state:
  version: 1
  status: done
  updated_at: '2026-11-12T01:26:29.632971+00:00'
destination:
  file:
    name: CA-P-3014-TASK--group-duckdb-refreshes-for-independent-lifecycle-targets.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
---
## Summary

Group DuckDB refreshes for independent lifecycle targets

## Objective

Reduce the time spent refreshing Workbench during batch Archive and Promote.

## Details

- Review and update the relevant RMEDO before implementation.
- Profile targeted reads, file effects and DuckDB refreshes for a batch of 50.
- Group refreshes for independent targets. Keep the existing order for targets that depend on each other.
- Verify immediate query visibility, per-target outcomes and completed effects when a batch stops on a failure.
- Compare warm timings on the same disposable fixture. The 29.5-second reduced-history baseline was 9.5 seconds for individual Draft creation, 9.4 seconds for batch Archive and 10.5 seconds for batch Promote.