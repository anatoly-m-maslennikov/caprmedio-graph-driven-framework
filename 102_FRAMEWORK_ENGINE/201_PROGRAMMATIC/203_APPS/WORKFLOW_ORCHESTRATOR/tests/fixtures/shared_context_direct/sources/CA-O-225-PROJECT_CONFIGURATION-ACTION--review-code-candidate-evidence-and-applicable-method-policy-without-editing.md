---
atom_id: "CA-O-225"
content_role: "Operations"
type: "Action"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
author: "Anatoly Maslennikov"
status: "Active"
version: 4
updated_at: "2026-10-21T23:46:56+00:00"
global_tier: 11
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action"
  depends_on:
    - "Entity/Node/Continuant/Atom/Content Role: Requirement"
    - "Entity/Node/Continuant/Atom/Content Role: Method"
    - "Entity/Node/Continuant/Atom/Content Role: Evaluation"
    - "Entity/Node/Continuant/Atom/Content Role: Delivery"
    - "Entity/Node/Continuant/Implementation"
    - "Entity/Carrier"
    - "Entity/Node/Continuant/Actor/Type: Operator"
relations:
  relates_to:
    - "CA-E-642"
    - "CA-M-402"
    - "CA-M-403"
    - "CA-M-405"
    - "CA-M-411"
    - "CA-M-396"
    - "CA-M-397"
    - "CA-M-398"
    - "CA-M-399"
    - "CA-M-400"
    - "CA-E-389"
    - "CA-E-539"
    - "CA-E-540"
    - "CA-E-253"
    - "CA-E-264"
    - "CA-E-265"
    - "CA-E-266"
    - "CA-E-267"
    - "CA-E-363"
    - "CA-E-364"
    - "CA-E-365"
    - "CA-E-366"
    - "CA-E-385"
    - "CA-E-453"
    - "CA-D-638"
---
# Summary

Review code-candidate evidence and applicable Method policy without editing

## Operation

Code Candidate Semantic Review means the read-only Action that checks the candidate, actual Evaluation/diagnosis evidence, and selected current R/M/E/D and Project-Principle bindings. It assesses the complete bound applicable Method-policy set and reuses its meaning; it does not create or duplicate policy. Map each applicable obligation to its Evaluation predicate and current evidence, or retain an explicit gap. Record inapplicability with a reason rather than silently omitting an obligation. Missing required coverage is unresolved; a selected subset of green linters is not complete review evidence.

An optional review_phase is final by default, preserving standalone review behavior. In preliminary phase, assess the available candidate and complete bound code/policy assessment without pretending pending final checks have run. Return preliminary_clear only with no confirmed findings from that assessment; list every pending check and current source/candidate binding. Preliminary clearance is neither passed nor acceptance. Return findings for confirmed defects, partial for unfinished selected assessment, and unresolved for required authority, context, coverage, or permissions missing. Final assessment requires actual complete current evidence bound to the same candidate, test definitions, applicable authority, portfolio, and inputs; changed relevant bytes invalidate affected evidence.

Return `passed` only when every selected assessment is current and complete with no findings. Return `findings` when selected assessment is complete and confirms implementation defects, test issues, or an admitted expected-phase observation. Return `partial` when actual selected assessment work remains unfinished. Return `unresolved` only when required evidence, authority, context, or permission is missing or blocked; retain completed findings and actual results. For CA-O-089 labels, implementation/test defect maps to findings; authority/environment/unresolved maps to unresolved; expected_initial_failure remains an expected-phase observation and cannot produce an accepted-candidate claim unless admitted expected-phase criteria genuinely hold.

## Details

No automatic fix, source/Atom edit, expected-result edit, retry, promotion, release, or Journal-completeness gate. Read-only commands are allowed; temporary fixture writes require explicit permission. Distinguish test issue, implementation defect, authority/environment blocker, expected-phase observation, and non-proven concern.
