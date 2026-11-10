---
atom_id: CA-C-465
ref_id: CA-C-465@2
container:
  scope_unit: CA-SU-16
role: Concern
form: Question
topics:
  main_subject: Subject/Engineering/Release Publication/Selector and Skill Synchronization
  dependencies:
  - Subject/Engineering/Release Publication/Recovery
relations:
  concern_about:
  - CA-P-1693
  - CA-D-562
  - CA-D-563
status: Archived
version: 2
updated_at: 2026-10-23 01:47:30 +0400
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: CA-C-465@2-TOOLS-QUESTION--how-to-publish-framework-selection-and-skill-safely.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/01_concern/archive
---
# Summary

How to publish Framework selection and Skill safely

## Concern

The full-Framework selector and public Skill are separate carriers. Choose a private exact pending-promotion receipt, complete package/Skill staging and gate verification before exposure, atomic selector replacement followed by publication of the bound complete Skill. This preserves D563's rule that candidate Skill publication follows N+1 selection; failures retain exact previous and candidate bytes and report pending rather than claim a fictitious cross-carrier atomic transaction. At88% design confidence, this is preferable to exposing N+1 Skill while N is selected or inventing another selector authority. Retry must match the exact same candidate, prior selector and planned Skill; unknown ownership and stale inputs refuse. P1693 implements this choice and proves recovery before the parent can close.

## Evidences

D562 requires atomic current.toml promotion; D563 binds public .agents/skills/ca to the same accepted candidate. Their separate locations do not provide a single filesystem transaction. Actual full-suite/image gates still precede exposure.

## Blast radius

Release promotion and its recovery only. No actual repository selection, Skill publication, image removal or Operator permission bypass is authorized by this record.
