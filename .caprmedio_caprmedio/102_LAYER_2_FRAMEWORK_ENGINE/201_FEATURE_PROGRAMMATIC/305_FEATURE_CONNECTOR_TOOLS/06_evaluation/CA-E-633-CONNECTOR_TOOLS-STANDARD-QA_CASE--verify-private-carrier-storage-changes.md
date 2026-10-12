---
atom_id: CA-E-633
content_role: Evaluation
type: QA Case
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool"
  depends_on: ["Artifact/Carrier","Action","Workflow","Atom","Operator"]
version: 2
updated_at: "2026-10-13 02:07:21 +0400"
relations:
  evaluation_for: [CA-R-1941, CA-D-630, CA-O-215, CA-O-216, CA-O-217]
  relates_to: [CA-E-628, CA-M-381]
---
# Summary

Verify private carrier storage changes

## Scope

Required falsifiable cases for CA-R-1941, CA-D-630 and O215/O216/O217, using independently authored expected requests and before/after ledgers. No tests are claimed to have run.

## Claim

the private variant passes **only** **if** its explicitly admitted storage result **and** preservation frontier are independently verified. missing **or** contradictory evidence is unresolved/failure, never a pass **or** an invented effect.

## Details

### Fixtures and accepted cases

Prepare a bounded temporary root with a file, empty folder, nested folder with a complete explicit inventory, unrelated sibling, occupied destination, symlinked source/ancestor/destination, escaping locator and deliberately substituted entry. Supply independent identity/type/content/mode/parent/permission evidence and the expected exact map; do not derive expected output from the helper.

- Rename a file and an explicitly inventoried folder within their same parent. Require the exact requested new binding, source absence, preserved contents/modes/inventory and unchanged unrelated entries.
- Move a file and explicitly inventoried folder to the exact bound destination. Require source absence, exact destination and preservation evidence. Any basename change must have been explicit in the approved binding; no inferred rename or merge passes.
- Remove one explicitly approved non-Atom file and one independently confirmed empty non-Atom folder. Require observed absence and unchanged unrelated/protected/history carriers. No child-removal effect is admitted.

### Refusal and uncertainty cases

1. Reject an unknown private variant, public physical path target, malformed binding, missing permission, unresolved roots, root/ancestor target, escape, missing or ambiguous source, wrong kind and stale source/parent/destination state without effects.
2. Reject every symlink/substitution case, destination collision, occupied distinct destination, source-subtree/invalid-overlap destination, overwrite or merge proposal. Include changes after preview; refusal must not be reported as success.
3. Add, remove or substitute a folder entry after its approved inventory. Reject the changed frontier rather than expanding it. Reject nonempty-folder removal even if a caller supplies a recursive flag or wildcard; unknown fields fail.
4. Present current/archived Atom carriers, required history, protected sources and malformed/uncertain classification for removal. Reject all of them. Absence of a recognizable Atom ID alone does not establish non-Atom eligibility.
5. Supply an internal carrier move from an admitted Atom lifecycle context and verify only the private storage contribution; the helper neither chooses lifecycle metadata nor claims the Atom transition completed. Reject missing or stale lifecycle/history context. Compare every referrer byte before/after: neither rename nor move may invoke O040 or rewrite references.
6. Verify an already satisfied unchanged rename/move request as a no-op only with current evidence. Missing expected-present source is a failure, not proof of a previous effect. For removal, a bound already-absent cleanup state is a no-op only when that exact absence was expected and permission/eligibility remains valid.
7. Inject effect, readback and verification failures. Preserve attributable known partial effects; unknown effects require `effect_uncertain`. Nonempty errors cannot indicate success; an exception-free unverified result cannot return empty errors. No-op must prove requested state unchanged.

### Acceptance and disposition

Compare exact independent before/proposed/after ledgers, resolved bindings and actual effect/error evidence. Any widened set, hidden reference/lifecycle decision, lost preservation evidence or false completion rejects the realization. Retain unresolved evidence and known effects; no automatic rollback, retry, resume or concurrent-publication guarantee is inferred. This source specifies future functional checks, not packet acceptance.
