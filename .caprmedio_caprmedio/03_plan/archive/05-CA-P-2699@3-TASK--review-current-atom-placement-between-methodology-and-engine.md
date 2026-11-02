---
atom_id: CA-P-2699@3
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
tier: 4
version: 3
updated_at: 2026-10-29 19:19:04 +0400
subjects:
  governs: Entity
relations:
  IS_CONTAINED_BY:
  - CA-P-2694
---
## Summary

Review Current Atom placement between Methodology and Engine

## Objective

Review every Current authoritative RMEDO source Atom cheaply with Luna. Decide whether its content belongs to Methodology or Engine, and identify the appropriate existing Scope Unit for Engine content. Report mixed or genuinely project-local/control cases instead of forcing a false binary choice.

## Details

Latest Operator clarification narrows the active placement review to Current RMEDO sources across Methodology, Engine and project-local folders. C/A/P placement and the cross-cutting parent-Plan question are deferred. The already collected broader cheap review is retained as parked preparation, not an adopted migration queue. Current includes Done, Canceled and other non-Draft/non-Archived statuses. Do not migrate C/A/P/O or change their content as a side effect. Exclude historical archives, Drafts, installed source copies, generated Projections and Journal records. Report malformed/ambiguous candidates and duplicate identities; do not silently drop them.

Use Summary, Claim or role-specific primary content, Claim Scope, relevant Details and declared ownership as evidence. Do not classify only by current folder, Content Role, Subject, filename, language keyword or technology name. R is an outcome/model definition and M is how it is achieved; either can belong to different topics. Project-specific Workflow definitions can remain Project Configuration; their runtime implementation belongs to Engine.

Examples from the latest Operator decisions: readable model names are a Methodology Method; technical key-name conversion in the Markdown/TOML adapter is an Engine Method under ADAPTERS. Both can govern Entity/Aspect/Text Writing Style. Abstract model structure and carrier mappings are distinct from the code and algorithms that implement them.

Use only Scope Units actually declared in Project Structure. Prefer the new Engine structure over obsolete per-tool units. No invented Scope Units or domain entities. Keep policy inheritance and actual-child ownership conditions visible. For a mixed Atom propose a split candidate, without changing its ID or Summary. Existing container membership and native relations must be checked before any eventual move; this task does not execute moves.

Run disjoint Luna lanes over one source-pinned inventory. Keep output thin: Atom ID, current Scope Unit, classification, proposed Scope Unit, confidence, action/status and short reason. Every selected source path must appear exactly once, even where identity metadata is unresolved. Escalate concrete low-confidence questions after grouping; no semantic deep review or large copied-Claim mapping report.

## Definition of Done

Every selected Current source is accounted for once in a thin review table. Every Engine placement either names a valid existing Engine Scope Unit or is explicitly unresolved. Mixed, project-local, stale-source and malformed cases are visible. Scope selection, counts and verification limits are recorded. No Current placement/content change is claimed without a later reviewed migration.

## Progress

Done — completed the cheap Luna placement review for all 2,443 selected Current RMEDO sources. Findings: 1,351 Methodology, 1,012 Engine, 79 project-local and 1 mixed. The thin table records 418 MoveCandidate, 1 SplitCandidate, 48 NeedsDecision and 1,976 Keep dispositions. All Engine destinations are registered Engine descendants; actual source hashes and registry content were rechecked. The 49 uncertain/split cases remain explicit, not approved moves.

[Review result](rmedo-placement-review.md) · [Thin placement table](current-rmedo-placement.tsv) · [Uncertain cases](rmedo-placement-uncertainties.tsv).

C/A/P placement and the mixed-parent-Plan question are deferred by the Operator. Broader acquired rows remain parked scratch evidence; 41 non-Atom execution documents and 3 legacy Implementation carriers are outside the focused result. No Current RMEDO placement or content was changed. Existing nine prepared Drafts remain unpromoted.
