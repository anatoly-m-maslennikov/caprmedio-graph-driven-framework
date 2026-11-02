---
atom_id: CA-D-613@13
content_role: Delivery
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Public Release/Workflow Binding
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Engineering/Public Release/Workflow Binding
version: 13
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
type: Eng Decision
tier: 3
---
# Summary

Serialize public-release Workflow bindings

## Scope

The Operation identities and execution boundary of one public release.

## Claim

Public release **must** implement CA-O-188 through its four declared Step/Action pairs in order: CA-O-189/CA-O-190, CA-O-191/CA-O-192, CA-O-195/CA-O-196 and CA-O-197/CA-O-198. These source identities describe the work; they do not require a closed manifest, fixed RMED pin set or whole-registry validation before the direct command runs.

## Details

| Step | Action | Result boundary |
| --- | --- | --- |
| CA-O-189 | CA-O-190 | discover zero or one actual matching open `amm/dev` to `main` PR |
| CA-O-191 | CA-O-192 | obtain the one content result: full PR body and concise Version History summary |
| CA-O-195 | CA-O-196 | apply the prepared documentation/history, commit and push, then create or update the matching Draft PR |
| CA-O-197 | CA-O-198 | add its actual URL to Version History when missing, commit and push the follow-up |

The Operator's explicit command covers this public release for the selected Project and personal remote. Source bindings describe which Operations the implementation performs; they are not authorization, execution success or a caller-selected executor.

Before the first public push or PR write, run the full test suite with required integration tests built from current code. Failed tests or unavailable required test infrastructure stop release. Do not add separate Atom validation, closed-registry admission or a sealed-package Full Gate. Existing ordinary selected Workflows retain their own permission and admission boundary.

Actual-URL-only finalization is mechanical: use the returned matching PR URL, preserve non-metadata inputs and do not repeat the suite or content prompt. Do not guess a URL, merge, retarget the PR or replay an uncertain remote effect. Report actual failures and partial effects for manual handling. Version History records the released Version and actual PR; Journal records, when appended, describe real events without requiring earlier history or proof receipts.
