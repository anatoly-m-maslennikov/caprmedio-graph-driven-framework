---
atom_id: CA-P-2315
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Configuration, Scope Unit, Atom, Plan]
version: 1
updated_at: "2026-10-13 18:52:21 +0400"
relations:
  is_decomposition_of: [CA-P-2270]
---
# Summary

Resolve graph authority from declared sources

## Objective

Graph-authority refresh resolves its finite source closure through the selected Project's declared authority roots instead of obsolete hardcoded folders.

## Details

Estimated own work: up to 15 minutes. Inherit CA-P-2270's independently accepted contract and authority gates. Implement only the refresh consumer and focused tests; split further work before exceeding this bound. Root owns Plans and Git.

Reuse the existing Project Structure reader and declared source ownership. Preserve the finite source-ID selection, exact version/hash checks, duplicate and missing-source refusal, and selected Project boundary. Do not infer identity from filenames, restore archived sources, choose a new Settings policy, add legacy fallback, or weaken stale-source checks. Report any remaining closure mismatch rather than automatically repinning it.

No source metadata/content/Subject migration, runtime activation or live publication is included. Independently verify the changed code, complete current closure result and stale/missing/ambiguous source refusal. Broader admission remains blocked independently by legacy source defects and missing current release authority.

### Definition of Done

The Plan is **not** Done if refresh still uses obsolete authority roots; current declared sources cannot be resolved; focused closure and refusal checks fail; a source mismatch is hidden by fallback or blanket repinning; independent verification is missing; or runtime/source-migration readiness is claimed from this bounded consumer correction.
