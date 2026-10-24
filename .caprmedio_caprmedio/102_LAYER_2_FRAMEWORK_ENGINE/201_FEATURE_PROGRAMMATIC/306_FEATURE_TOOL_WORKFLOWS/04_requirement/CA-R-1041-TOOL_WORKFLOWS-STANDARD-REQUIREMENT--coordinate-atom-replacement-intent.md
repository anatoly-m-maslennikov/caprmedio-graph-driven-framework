---
atom_id: CA-R-1041
content_role: Requirement
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/Engineering/Tool//REPLACE_ATOM
version: 13
updated_at: 2026-10-24 01:37:42 +0400
relations: {}
tier: 3
type: Rule
---
# Summary

Coordinate Atom replacement intent

## Scope

REPLACE_ATOM's explicit singular or frozen bulk replacement intent, delegated application boundary and truthful result evidence.

## Claim

REPLACE_ATOM **must** coordinate explicit Atom replacement intent **without** owning generic Carrier creation, relation editing, **or** archival semantics.

- an atomic replacement accepts **`=1`** exact active predecessor Atom ID, **`>=1`** distinct exact sealed prepared-new successor Carrier sets, **and** action context. each prepared-new successor set contains complete sealed content, assigned identity, and destination; no preexisting-successor mode is admitted.
- reject a missing, duplicate, inactive, or self-referential predecessor; missing, duplicate, partial, or unsealed prepared-new successor content; or a used successor identity or destination. return a sealed replacement action containing the supplied predecessor, complete prepared-new successor set, and predecessor archive intent.
- a several-predecessor Workflow supplies explicit mappings but invokes one independently admitted replacement Action per predecessor. Stop at its first failed Action, retain completed replacements and leave the remainder untouched; do not promise a cross-predecessor all-or-nothing effect.
- use the canonical Atom lifecycle capability to materialize only the complete sealed prepared-new successor set, establish every successor as Active, and then archive the predecessor; pass the explicit IDs **to** the provenance pipeline. do **not** infer successor content, perform generic Carrier creation, or write replacement relations **in** Atom Carriers.
- default **to** a mutation-free dry run. permit apply **only** through authorized project-local MCP delegation with a sealed Initiative action envelope.
- a successful delegated effect requires durable COMMIT_TRIGGER intake acknowledgment **before** MCP reports success. an intake acknowledgment is necessary for that handoff **but** is **not** proof that replacement was applied **or** that its authoritative Journal event **and** Run evidence were durably recorded. REPLACE_ATOM does **not** append the Journal, stage files, **or** create a Git Commit.
- distinguish a prepared sealed description, a deferred delegated request, **and** an actually applied replacement. prepared **or** deferred results **must** state that the archive effect is **not** applied; acceptance, sealing, **or** intake alone **must not** be reported as completed replacement.
- at the actual effect boundary, revalidate the exact predecessor and every prepared-new successor's complete sealed content, identity, unused destination, current source/destination conditions, complete sealed mapping, and current delegated authority. materialize every successor and verify each is durably Active **before** predecessor archival. use CA-O-051's whole-Carrier transition: preserve the predecessor's body, Summary, Type, identity **and** frontmatter values except actual archive Status, Version **and** Updated At. Its actual changed archive Revision advances Version by **`=1`** and uses the applicable canonical archive encoding; retain exact before-Revision bytes and Version as required history.
- report actual replacement completion **only** with observed canonical lifecycle effects **and** durable authoritative archive-event evidence naming the explicit predecessor **and** complete **`>=1`** materialized Active successor set under CA-R-807. preserve each explicit mapping and its actual result; partial or uncertain effects must not be described as completed replacement.
- retain exact actual Workflow/Action Run identities, definition Revisions, input/result/effect references, start **and** truthful terminal/pending evidence **and** actual durable receipts under the reviewed CA-P-1443/CA-P-1451 shared contract. recording failure leaves completion evidence blocked **and** pending evidence intact; preserve the missing-recording disposition **without** replaying performed replacement **or** resetting authority. an unpersisted acknowledgment is **not** Journal completion.

## Details

CA-O-031 owns the replacement Action; CA-O-051 and CA-R-807 govern canonical lifecycle effects and immutable replacement history. CA-E-299 covers the prepared description; CA-E-247 covers admission, delegated-effect and receipt distinctions. The Tool admits no preexisting-successor mode, does not infer missing successor content, and gains no lifecycle or Journal authority from intake acceptance.

Every Summary value change requires a new Atom ID and predecessor archival through this replacement Workflow, even when the Claim remains unchanged. Return the explicit target, created and archived IDs separately: for target `100` replaced by new Atom `200`, the result identifies target `100`, created `200` and archived `100`. Replacement does not automatically retarget incoming references; independent Find and Modify Workflows select and update those referencing Atoms. Resume and retry policy for independent replacements remains deferred. Current source, destination, permission, preview and each replacement's internal storage-effect safeguards remain required.
