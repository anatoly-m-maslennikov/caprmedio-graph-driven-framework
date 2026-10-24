---
atom_id: CA-C-576
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: high
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-R-1527, CA-R-1843, CA-R-1845, CA-O-016, CA-P-2581]
  relates_to: [CA-C-583, CA-C-584, CA-P-2613]
version: 7
updated_at: "2026-10-23T12:49:37+0400"
---
# Summary

Current native Workflow dispatch lacks Integrated continuation

## Concern

Current source R1527@7 defines Integrated execution as the current participating session receiving the bound Action inputs and instructions, performing the Action and returning its result to the executor. O016@17 binds all eight current Steps as Integrated. The current native implementation path instead invokes a separate ephemeral Codex CLI callback synchronously. Retaining prior-result data does not make that separate Agent the current participating session.

Read-only inspection found no public pending-prompt/result-submission path in the current enqueue, enqueue_selected and status operations. The native graph immediately transitions after a callback result and its execution session is in memory. A frozen current-graph check also observes O231 dispatching legacy O091. This is current source and isolated-fixture evidence, not an observation of a deployed current Workflow or a production incident.

## Required disposition

After the Operator-directed three-file legacy refactor is independently accepted, implement the existing Integrated context contract through a durable bound pending frontier, prompt/input return to the current session, admitted later result submission and continuation without replaying completed Actions or effects. Reuse the existing Project, request, Run, frozen source, candidate, packet, visit and retry fields. Validate stale, conflicting, repeated and cross-Project submissions and preserve partial evidence. Keep separate-Agent callbacks available only for explicitly Isolated invocations; do not silently substitute them for Integrated Steps.

CA-P-2581 and CA-P-2596 through CA-P-2602 own the bounded implementation and isolated functional acceptance. Existing source authority owns the Workflow graph, permissions, result labels, retry accounting and release handoff; this Problem does not introduce another Workflow, new business gate or release authorization. Do not activate refreshed bindings or claim current native admission from definition-only, callback-only or fixture-integrity checks.

## Evidence boundary

The refreshed full Method projection has 39 verified current source pins. The new frozen fixture carries 17 current Workflow/Step/Action sources plus all 39 exact raw Method carriers and explicit R/D/E support; fixture integrity is distinct from native execution. Initial adapter-boundary tests are genuinely red at O231 versus O091. No production MCP, Docker replacement, full suite or deployment was used in this investigation.

## Verified local implementation and binding-drift checkpoint — 23 October 2026

The bounded local implementation evidence is now distinct from the unresolved binding/runtime gate: 64 focused checks, strict SDK journey 4/4, final Docker-free stdio smoke with 23 tools, and the related observation/recovery checks were recorded as local verification only. They do not admit the visible Project binding or production runtime.

The mechanical binding audit records an in-memory O016@18 candidate as valid with SHA256 ad385a288efa2bb1857c3d9f11c019d40485569090ccda17854182b56b93d861. All 15 non-target route pins and both query admissions differ from the candidate by version, path and digest only; no shape, order or flag drift was observed. The raw Project manifest still fails the retired O091 unique-current check. Query observations are CA-O-158@5 -> CA-O-158@7 (ProjectConfiguration), CA-O-161@4 -> CA-O-161@6, CA-O-163@6 -> CA-O-163@8 and CA-O-162@4 -> CA-O-162@6.

The preserved Project projection baseline is SHA256 f6577216b7ee914d9abf3939677df9208d9658a3e91fe74ad13b34c09539329c; the Engine legacy baseline is SHA256 d6dca70bbaa3530958d5950278104ed5628b7a282539675fecd9f9a58845b684. A1142 remains v2 with historical W09; no A1142 edit, candidate emission or admission was performed. The pre-existing 15-versus-16 optional move_atom difference is non-target drift.

The operation inventory is mechanical evidence only: create_atom, move_atom, build_entities_graph, build_terms_graph and find_and_fetch_journal_events each have 12 leaf entries; change_atom_status has 14; replace_atom 15; update_atom 23; create_scope_unit, rename_scope_unit, move_scope_unit, remove_scope_unit and build_applicable_methodology each have 57; find_and_fetch_artifacts has 3; revert_changes has 12. Query admission has 15 pin leaves. The source graph has 29 edges; 13 terminal edges map to the complete sentinel, while the source retains distinct completed/blocked terminal targets. These counts are not coverage or semantic-pass claims.

CA-P-2612 source wording review is accepted with 99% independent-review confidence; no Plan status is changed here. Publication, live binding mutation, runtime admission and deployment remain blocked by the unresolved raw-manifest/current-binding drift.


## Source-contract acceptance checkpoint — 23 October 2026

The five-source wording review is accepted: CA-R-1847@16, CA-R-1848@9, CA-D-547@12, CA-E-567@7 and CA-E-568@8 passed parser/body checks and independent review. This closes the source-contract preparation portion only. The mechanical drift remains: the in-memory O016@18 candidate is valid, while the raw Project manifest fails the retired O091 unique-current check; all 15 non-target route pins and both query admissions differ only by version/path/digest. CA-P-2613 remains Backlog pending the Operator's review-scope choice. No candidate emission, A1142 edit, live binding mutation or runtime admission occurred.

## Readback clarification — 23 October 2026

The accepted source-contract review is CA-R-1847@16, CA-R-1848@9, CA-D-547@12, CA-E-567@7 and CA-E-568@8; worker body/archive checks and independent review passed. The report's query identifiers use full Atom IDs and the source-graph statement distinguishes the 29 total edges from its 13 complete-sentinel terminal edges and distinct completed/blocked terminal targets.

## Full binding-review authorization checkpoint — 23 October 2026

The Operator authorized the previously held review of all 15 non-target route pins and both query admissions. CA-P-2613 is Active with six read-only review leaves; the source-contract review remains accepted at 99% confidence. The raw Project manifest still fails the retired O091 unique-current check, so this Concern remains Active. No candidate emission, A1142 edit, live binding mutation or runtime admission was performed.

## Semantic binding-review checkpoint — 23 October 2026

The all-route review is complete as a planning/provenance result. CA-C-583
captures the six-route Journal receipt/completion semantic reconciliation and
CA-C-584 captures the exact 15-operation MCP frontier versus optional
move_atom. CA-P-2614 through CA-P-2619 are Done as review records; CA-P-2613
remains Active with CA-P-2620 and CA-P-2621 Backlog. The raw Project manifest
still does not resolve the retired CA-O-091 locator to exactly one current
Carrier; this wording is not a claim that two active O091 carriers exist.
The 50-pin source revalidation and Project/Engine/A1142/Core baselines are
unchanged. No candidate emission, live binding mutation or runtime admission
occurred.

## Current O016@20 admission checkpoint — 23 October 2026

Fresh inventory now reports current O016@20 with body bytes unchanged from the
exact O016@18 archive. This does not clear the Concern: the implementation
frontier still has exact legacy-17 and direct-18 support, so compatibility for
O016@20 requires a bounded candidate-only admission assessment and focused
isolated checks. Do not broaden support to every version greater than 18.
CA-P-2627 owns the compatibility proposal and CA-P-2628 owns the focused
isolated tests. The public 15-operation route, live 16-operation Project
manifest, visible binding and runtime remain unchanged; no admission,
publication or deployment is claimed.
