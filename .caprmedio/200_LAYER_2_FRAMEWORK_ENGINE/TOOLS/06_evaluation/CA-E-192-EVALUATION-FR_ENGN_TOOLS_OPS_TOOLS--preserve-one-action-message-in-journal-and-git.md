---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-20 20:22:00
relations:
  evaluation_for:
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--append-governed-file-change-event
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
---
# Preserve one action message in the Journal and Git

## Claim checked

The Journal file-change event and Git commit carry the same canonical action message.

## Test case

Apply one valid context whose canonical message contains two typed upstream relation groups and an `UPDATE` action, then compare the sealed message, NDJSON `action_message`, and Git commit subject byte for byte.

## Acceptance criteria

All three byte sequences are identical, preserve the canonical relation and action ordering, and contain no added prefix, suffix, quoting, normalization, or line wrapping.

## Failure disposition

Reject the flow at the first mismatch and report which carrier diverged from the sealed canonical message.
