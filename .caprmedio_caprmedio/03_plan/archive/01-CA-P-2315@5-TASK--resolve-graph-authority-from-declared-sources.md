---
atom_id: CA-P-2315@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Structure
  depends_on:
  - Configuration
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 5
updated_at: 2026-10-24 10:27:10 +0400
relations:
  is_decomposition_of:
  - CA-P-2270
tier: 3
---
# Summary

Resolve graph authority from declared sources

## Objective

Graph-authority refresh resolves its finite source closure through the selected Project's declared authority roots instead of obsolete hardcoded folders.

## Details

Estimated own work: up to 15 minutes. Inherit CA-P-2270's independently accepted contract and authority gates. Implement only the refresh consumer and focused tests; split further work before exceeding this bound. Root owns Plans and Git.

Reuse the existing Project Structure reader and declared source ownership. Preserve the finite source-ID selection, exact version/hash checks, duplicate and missing-source refusal, and selected Project boundary. Do not infer identity from filenames, restore archived sources, choose a new Settings policy, add legacy fallback, or weaken stale-source checks. Report any remaining closure mismatch rather than automatically repinning it.

No source metadata/content/Subject migration, runtime activation or live publication is included. Independently verify the changed code, complete current closure result and stale/missing/ambiguous source refusal. Broader admission remains blocked independently by legacy source defects and missing current release authority.

### Acceptance

Implementation committed as 92261be4e. The finite 26-source graph authority closure resolves through declared Core ownership; path-only manifest changes retain IDs, versions and hashes. Focused graph tests 8/8 passed in both worker and root runs; validator checkpoint 309/309 and relation tests 7/7 passed. Independent review accepted the narrow resolver; missing, duplicate, unsafe and escaped source roots still refuse. No Release/runtime acceptance is implied; CA-D-572 remains unresolved under the parent.

### Definition of Done

The Plan is **not** Done if refresh still uses obsolete authority roots; current declared sources cannot be resolved; focused closure and refusal checks fail; a source mismatch is hidden by fallback or blanket repinning; independent verification is missing; or runtime/source-migration readiness is claimed from this bounded consumer correction.
