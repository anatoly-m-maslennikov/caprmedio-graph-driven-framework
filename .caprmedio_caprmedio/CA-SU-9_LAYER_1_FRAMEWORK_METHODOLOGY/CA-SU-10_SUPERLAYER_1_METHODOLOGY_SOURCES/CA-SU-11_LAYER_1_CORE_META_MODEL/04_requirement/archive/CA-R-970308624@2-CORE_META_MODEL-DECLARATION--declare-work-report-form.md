---
identity:
  id: CA-R-970308624
  ref_id: CA-R-970308624@2
context:
  container:
    scope_unit: CA-SU-11
  role: Requirement
  form: Declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Work Report)
  tier: 3
state:
  status: Archived
  version: 2
  updated_at: 2026-11-08 19:06:46 +0400
destination:
  file:
    name: CA-R-970308624@2-CORE_META_MODEL-DECLARATION--declare-work-report-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archive
---

## Summary

Declare Work Report Form

## Claim

### Prose Claim

A Work Report records the execution of one Plan with Form Plan in a separate Atom. This is the reported Task. It has its own ID and the same Summary and Container as that Task. IS_WORK_REPORT_FOR identifies the Task by its base Atom ID.

Details records:

- actual changes;
- checks performed;
- results;
- remaining gaps.

The report is updated throughout execution. Its Status describes the reporting work: Active while maintained, Done when the final known changes, checks, results and remaining gaps are recorded, or Canceled when reporting is abandoned. Completed reporting includes explicit remaining gaps. The Task retains its own Status.

### Formal Claim

```CFEL
# model
Atom/(.Header.Form := Work Report);

Atom/(.Header.Form := Work Report).Content.Details:: {::1};

Atom/(.Header.Form := Work Report).Content.Details.*[]{::0};

Atom/(.Header.Form := Work Report).Content.Summary ;> Atom/(.Header.Form := Work Report).Content.Details;

# instances
$report[<Atom>, (.Header.Form = Work Report)];

$report.Header.Role == Plan;

$report {::1}((IS_WORK_REPORT_FOR)) $task[<Atom>, (.Header.Role = Plan) AND (.Header.Form = Plan)];

$report.Header.ID != $task.Header.ID;

$report.Content.Summary == $task.Content.Summary;

$report.Header.Container == $task.Header.Container
```

## Semantics

A Work Report is the evolving record of a Task’s execution.
