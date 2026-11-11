---
atom_id: CA-C-563
content_role: Concern
type: Question
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: medium
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-P-2526, CA-P-2527, CA-O-169, CA-D-564]
version: 1
updated_at: "2026-10-21T10:13:48Z"
---
# Summary

Choose Local release image-retention scope

## Concern

Should automatic Local release retention cover all unused positively identified CAPRMEDIO runtime images on this Docker host, including test Projects, or only images owned/linked to the selected Project?

## Evidences

The Operator explicitly requested image maintenance after a green full suite and confirmed retaining only the last rebuild of the current version, not one image per historical version. The retained image is the exact candidate admitted and launched by that release, not a moving tag or arbitrary host-clock ordering. Current O169/M332/D564 and cleanup code restrict retirement to selected-Project ownership or proven links. Host-wide deletion would additionally affect other test Projects and unowned runtime-schema-labelled images. Prior manual deletion approvals named exact targets and do not establish that recurring wider scope. The scope question was asked in-session and remains unanswered.

Current canonical ImageManager already names the candidate after the green suite. P2528 independently verifies that order, failed-suite/tag-preparation stops and exact immutable launch. A narrow existing-safety correction now skips all image cleanup if the launched candidate was not verified, even on first installation; root focused59/59 checks passed and independent review approved. No actual release or Docker effect occurred.

## Blast radius

Hold scope-sensitive retention implementation and active contract changes until the Operator chooses. Preserve current ownership rules, container references, no-force/no-prune safeguards and pending reporting. P2526/P2527 remain incomplete; P2529 final acceptance waits. Independent ordering/proof-guard work is accepted separately and grants no broader deletion authority. Do not stop foreign/running containers or infer permission from tags, dates or missing version metadata alone.
