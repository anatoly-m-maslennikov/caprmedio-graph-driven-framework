---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/File.Main Content
  passive:
  - CAPRMEDIO <+ MODEL <+ Carrier
  - CAPRMEDIO <+ MODEL <+ Journal
  - CAPRMEDIO <+ MODEL <+ Event Record
  - CAPRMEDIO <+ MODEL <+ Atom.ID
version: 26
updated_at: 2026-11-02 19:44:26 +0400
relations:
  evaluation_for:
  - CA-D-435
  - CA-D-339
atom_id: CA-E-465
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 4
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/06_evaluation/CA-E-465-PROJECT_CONFIGURATION-EVAL_CASE--validate-replacement-event-schema-encoding.md
  source_atom_id: CA-E-465
  source_atom_revision: 26
  source_sha256: ec1bbb5eb5770b3176e9e04fef2848da6ec14e69b3eb4bdf89548629a0a4a43f
  original_relations_sha256: ab954123eb0e5c59cf4240bd5fc1eff515c3df6541497c0bfdef1e8385c68df3
---
## Summary

Validate replacement Event schema encoding

## Claim scope

the Main Content of the selected schema-version `3` replacement Journal Event Carrier.

## Claim

the Main Content of the selected schema-version `3` replacement Journal Event Carrier **must** support evaluation of CA-D-435-PROJECT_CONFIGURATION-DELIVERY--serialize-atom-replacement-event-references without treating Project conformance as storage integrity.

## Cases

- case 1: encode a completed File Carrier `MOVE` Event Record with paired string predecessor **and** array-of-string successor fields; preserve the supplied successor order.
- case 2: keep that envelope valid **and** vary the observed IDs: canonical, legacy, nonconforming, duplicate, self-referencing, **or** an empty successor array. also vary the result filename **or** archive placement independently of the safe Event path encoding.
- case 3: omit **only** one paired field, supply null **or** the wrong storage type, use a schema **or** Event kind that does **not** define the pair, **or** change the payload **without** updating its digest.
- case 4: replay an identical sealed Event Record; **then** submit a different payload under the same Event identity.
- case 5: validate an ordinary historical Event Record without replacement fields.

## Acceptance

the Main Content evaluation **must** report that:

- cases 1 **and** 2 remain recordable with the supplied values unchanged. case 2 **may** fail CA-E-462-CORE_META_MODEL-POLICY--validate-atom-replacement-event-evidence independently; its conformance verdict **must not** prevent recording under CA-R-1491-CORE_META_MODEL-RULE--keep-project-validation-out-of-journal-admission.
- case 3 fails the selected encoding **or** integrity check without changing accepted history.
- the identical replay reuses the existing receipt without a duplicate record; an identity collision with a different payload fails without overwriting history.
- case 5 retains its selected historical schema. passing this Evaluation does **not** prove active successors, exact archive preservation, valid Project identifiers, valid placement, **or** a correctly performed replacement.
