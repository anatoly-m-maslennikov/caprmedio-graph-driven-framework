---
atom_id: CA-P-2421
ref_id: CA-P-2421
container:
  atom: CA-P-2401
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Domain/Continuant/Atom
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2401
status: Done
version: 5
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 10-CA-P-2421-TASK--repair-current-graph-authority-source-resolution.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done
work_sequence_number: 10
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Repair current graph-authority source resolution

## Objective

Advance the bounded Epic repair or evidence-reconciliation responsibility for CA-C-525 without broadening deployment or historical effects.

## Details

Own graph_authority_refresh.py, graph_authority.json only if a supported binding update is required, and dedicated graph authority tests. Reuse current declared authoritative source resolution; preserve finite approved IDs, unique active source/provenance checks, and fail-closed behavior for missing, ambiguous, projected or unsafe carriers. Do not move governed sources or silently expand authority. Golden fixture must model D305 at its declared owner without live source coupling.

Use the current mrt_programmatic_methods_compact.projection.md and applicable current source RMEDO; the projection is not authority. Use Luna workers, preserve other edits, keep one owner per file and leave Git/index/commit integration to root. Before changing behavior, inspect callers and current source authority. At confidence below95percent, stop the affected behavior and ask the Operator rather than inventing policy.

Estimated own work: at most15minutes. Split further before exceeding that bound. After each completion, review and update dependent Tasks before execution. Prefer frozen public-interface/functional evidence over implementation-shaped tests. Run Project Python only in the selected uv-managed environment. No production MCP test, restart, reload, deployment, or uncertain effect replay. User-authorized manual fallback applies if MCP cannot do the job; retain exact predecessors and actual Journal provenance.

### Definition of Done

A concrete bounded deliverable has inspected sources/callers, reproducible checks and truthful outcomes/limitations. Code repairs retain all applicable safeguards; evidence-only work makes no effect or deployment claim. Any blocker or unresolved choice is recorded as a Concern.

### Completion checkpoint

Repaired the D305 binding to current Project Configuration v16 and admitted only explicitly declared optional Project Configuration source roots, including lazy delivery-only materialization. Core Meta Model remains required. Worker verification:33 focused/related tests, Ruff and diff checks passed; current D305 lookup verified. Full finite graph verification still stops at stale D268; dependent CA-P-2426 investigates without automatic pin refresh. No production or deployed repair claim.
