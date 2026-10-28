---
atom_id: CA-O-111@19
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
version: 19
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action//Repair RMED Review Batch'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.Version Number
  - Subject/Graph Node/Domain/Continuant/Atom.Summary
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Engineering/Execution Control/Decision Confidence
  - Subject/Graph Node/Domain/Continuant/History/Journal
relations: {}
tier: 3
---
# Summary

Fix confirmed local RMED Atom issues

## Operation

Repair RMED Review Batch **means** the Action that applies the smallest authorized correction for confirmed local findings.

1. read the current Atom, applicable checking criteria, **and** its check report. **if** the checked source **or** applicable criteria changed, stop that item's repair with the mismatch recorded; retain the earlier report as historical evidence rather than inventing a current pass **or** adding an automatic recheck.
2. resolve confirmed findings under the applicable local rules, permissions, **and** confidence threshold. preserve necessary information, Subject targets, **and** relation targets.
   - correct forced execution as a capability Requirement **only** **when** its intended capability **and** target are established **and** the semantic change is authorized.
   - preserve required outcomes, validation gates, safeguards, **and** behavior during authorized execution. do **not** replace `must` with `may` mechanically **or** invent a target.
   - retirement requires explicit authority; unresolved intent **or** absent authority blocks the correction rather than weakening the Claim.
3. classify the change under CA-O-067. increment Version by exactly **`1`** **and** refresh `updated_at` on **every** actual same-ID edit, including formatting **or** equivalent wording; an exact no-op retains both. a Summary-value **or** genuine Type change requires replacement authority. for a Summary change, `allow_replacements=true` **with** fix permission delegates replacement **within** the selected Atom; the executor reserves a new ID **and** Version **`=1`**, archives the predecessor, **and** records the transition. retain exact prior Revision bytes as required history **without** another metadata edit to them.
4. apply the correction **and** record the actual changes **in** the same Atom report. uncertain, unauthorized, **or** outside-scope work remains blocked rather than expanding this Run.
5. return `fixed_not_rechecked` **or** `replaced_not_rechecked` **only** **when** **all** **`=6`** initial checks concluded **and** **all** findings were corrected **or** rejected with recorded reasons. otherwise return `blocked`, preserving safe partial edits **and** the remaining findings **or** unfinished coverage. this Action performs no proposal review, post-fix Evaluation, **or** automatic recheck loop.

## Details

at the configured context threshold, save the current Atom, unfinished correction, **and** completed edits **in** a short handoff. continue **in** a fresh subagent **without** repeating an already applied edit. context handoff does **not** consume a repair retry; genuine failed execution attempts remain subject **to** the admitted retry policy.

a correction record is evidence of an edit, **not** a passing check **or** completion of an unperformed check. preserve original check outcomes **and** blockers separately from corrections. a later check is a separately requested Run.
