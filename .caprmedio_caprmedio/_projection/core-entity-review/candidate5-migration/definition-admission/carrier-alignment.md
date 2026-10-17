# Carrier definition admission — minimal source alignment

Status: proposal only. No source Atom, identity, Status or runtime was changed by this packet.

Basis: Candidate #6 decisions 1–31 and the 14 prepared Carrier definition drafts. The two placeholders for Carrier.Ownership Class and Carrier.Storage Boundary are superseded, not missing definitions. This packet does not activate any of the wider set of 45 definition drafts.

## Boundary

R defines what an Entity or dependent property is. D specifies its representation, serialization, placement and storage constraints. Do not convert a D Atom into an R Atom while retaining its D ID. The already-prepared R drafts receive new IDs only through the later admitted creation operation.

Keep Carrier.ID distinct from its filename, path and canonical address. Do not create a Carrier or binding entry for every YAML field or Markdown section. General D policies can carry dependent properties inside an existing File Carrier.

Preserve useful storage protections when retiring the rejected classifications. Do not treat this packet as permission to delete runtime files, history or other Carriers.

## Source paths and observed revisions

All paths in this table are relative to this exact source root:

`/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/`

| Source | Observed Version | Source path | Proposed disposition |
| --- | --- | --- | --- |
| CA-R-1342 | 13 | `04_requirement/CA-R-1342-CORE_META_MODEL-CORE-REQUIREMENT--define-delivery-content-role.md` | Same ID/Summary; narrow Delivery to representation |
| CA-M-313 | 7 | `05_method/CA-M-313-CORE_META_MODEL-METHOD--write-delivery-claims-with-the-delivery-cce-profile.md` | Same ID/Summary; align its authoring instructions |
| CA-D-316 | 13 | `07_delivery/CA-D-316-CORE_META_MODEL-GENERAL--classify-carriers-by-ownership.md` | Archive obsolete claim; no replacement |
| CA-D-341 | 13 | `07_delivery/CA-D-341-CORE_META_MODEL-CORE--separate-persistent-authority-from-runtime-state.md` | Same ID/Summary; preserve storage protection without rejected properties |
| CA-D-258 | 12 | `07_delivery/CA-D-258-CORE_META_MODEL-CORE-DELIVERY--classify-file-carrier.md` | Archive only with admitted File Carrier R replacement |
| CA-D-259 | 12 | `07_delivery/CA-D-259-CORE_META_MODEL-CORE-DELIVERY--classify-directory-carrier.md` | Archive only with admitted Directory Carrier R replacement |
| CA-D-414 | 15 | `07_delivery/CA-D-414-CORE_META_MODEL-CORE--classify-carrier-as-a-primary-entity.md` | Archive only with admitted Carrier R replacement |

These revisions identify the reviewed inputs, not a new fixed-pin requirement. Read the actual source before applying; do not apply this text over a changed claim without checking that change.

## 1. CA-R-1342 — define the Delivery role

Current conflict: its Claim says Delivery defines the Carrier model, and its Details expressly assign Carrier definitions/classification to D even without a representation decision. This contradicts the approved defining-R requirement.

Keep Summary exactly: **Define Delivery Content Role**.
Keep ID CA-R-1342 and Content Role Requirement. This is a revision of the same role-definition Claim, not a different topic. Proposed next Version: 14 if the reviewed source remains Version 13.

Exact proposed Subjects:

```yaml
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Delivery"
  depends_on:
    - "Entity/Continuant/Object/Atom/Content Role"
    - "Entity/Continuant/Object/Atom.Substance"
    - "Entity/Carrier"
    - "Entity"
```

Exact proposed Scope:

> the Delivery Content Role.

Exact proposed Claim:

> Delivery **means** the Content Role of an Atom Substance that specifies how an Entity is represented, serialized, stored or placed in a Carrier.

Exact proposed Details:

> Delivery governs representation formats, contents, addresses, placement, Entity/Carrier bindings and constraints on changes to those representations. Requirement defines the Entities, their dependent properties and their classification, including Carrier kinds. A statement defining what a Carrier or property is remains a Requirement; a statement specifying how its representation is encoded or placed is Delivery. A property stored in YAML or a Markdown section does not require its own Carrier entity or separately registered binding.

No unrelated RMED role definition is rewritten.

## 2. CA-M-313 — align Delivery authoring

Current conflict: authoring conventions 1 and 4, plus Details, explicitly encourage Carrier definitions/classifications as Delivery Claims. Changing R1342 alone would leave this direct instruction contradictory.

Keep Summary exactly: **Write Delivery Claims with the Delivery CCE Profile**.
Keep ID CA-M-313 and Content Role Method. Proposed next Version: 8 if the reviewed source remains Version 7.

Exact proposed Subjects:

```yaml
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Delivery.Substance"
  depends_on:
    - "Entity/Continuant/Object/Atom/Content Role: Delivery"
    - "Entity/Carrier"
    - "Entity/Continuant/Object/Atom.Subjects"
    - "Entity/Continuant/Term"
    - "Entity/Continuant/Object/Relation"
```

The Term dependency concerns the applicable CCE Operators; it does not introduce a new Term definition layer.

Exact proposed Scope:

> authoring Delivery Substance with the applicable Delivery CCE Role Profile.

Exact proposed Claim:

> a Delivery Substance **must** use the applicable Delivery CCE Role Profile with these authoring conventions:
>
> 1. name the governed Entity or Carrier and state its representation, storage or placement constraint directly.
> 2. include format, content, address, placement or lifecycle conditions **when** they are relevant to that contribution.
> 3. choose CCE Operators to express the applicable modality, conditions, quantities and comparisons.
> 4. use admitted typed Relations when the contribution expresses a representation binding.
> 5. keep the Substance about its governed Subject; reference separately governed contributions instead of redefining them.

Exact proposed Details:

> Entity, property and Carrier-kind definitions belong to Requirement. Delivery uses those definitions to specify representation. Do not invent a filename, format or lifecycle condition merely to fill a template. YAML fields and Markdown sections can represent properties inside one File Carrier without a separate binding record for each property.

Keep its existing typed parent relation. Its existing contextual reference to R1342 is not reclassified into an invented dependency by this packet.

## 3. CA-D-316 — retire the rejected classification

Current governs: `Entity/Carrier.Ownership Class`.
Current Scope: internal CAPRMEDIO Carriers.
Current Claim: every internal CAPRMEDIO Carrier must have exactly one Ownership Class from Framework-Owned, Project-Owned, Runtime State.
Current Details: empty.

Candidate #6 decision 30 rejects this entire generic property and value set. There is no representation rule left after removing that requirement.

Proposed action: archive CA-D-316 through the existing lifecycle operation. Do not change its Summary, Scope, Claim or Details into a different storage rule. No new ID or replacement Claim is needed. Do not add its field or values to any R draft.

Archiving this Atom does not archive other storage rules merely because they once mentioned its classes. D341 is explicitly retained below.

## 4. CA-D-341 — retain the storage protection

Current conflict: its Subject is the rejected Carrier.Storage Boundary property, and its wording uses the rejected ownership classification. The useful Claim is protection of canonical content and history from cleanup, which the Operator explicitly retained.

Keep Summary exactly: **Separate Persistent Authority from Runtime State**.
Keep ID CA-D-341 and Content Role Delivery. Proposed next Version: 14 if the reviewed source remains Version 13.

Exact proposed Subjects:

```yaml
subjects:
  governs: "Entity/Carrier"
  depends_on:
    - "Entity/Continuant/History"
```

Exact proposed Scope:

> persistent Carriers holding canonical authority or retained history, in relation to runtime cleanup.

Exact proposed Claim:

> runtime cleanup **must not** remove persistent Carriers holding canonical authority or retained history.

Exact proposed Details:

> Delivery placement and retention rules must keep that content outside the cleanup target set. This protection does not require a Carrier.Ownership Class or Carrier.Storage Boundary property, and it does not classify a Carrier as disposable merely because a runtime uses it.

This preserves the existing protection without forcing all historical content into one directory or asserting that every runtime location is disposable. Existing concrete project storage paths remain unchanged. No cleanup is executed here.

## 5. Pure Carrier classification D Atoms

These are definitions rather than independent representation policies. Retire them only after the corresponding new R definition is actually admitted; empty or pending drafts are not coverage.

| Existing Atom | Current Subject / exact defining Claim | Prepared replacement draft |
| --- | --- | --- |
| CA-D-258 | `Entity/Carrier/File Carrier`; “the Term File Carrier NARROWER_THAN Carrier.” | `../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-carrier-file-carrier.md` |
| CA-D-259 | `Entity/Carrier/Directory Carrier`; “the Term Directory Carrier NARROWER_THAN Carrier.” | `../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-carrier-directory-carrier.md` |
| CA-D-414 | `Entity/Carrier`; “the Term Carrier must be NARROWER_THAN Primary Entity.” | `../empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-carrier.md` |

Proposed successor Subjects are respectively `Entity/Carrier/File Carrier`, `Entity/Carrier/Directory Carrier` and `Entity/Carrier`. The new R Claims are the prepared definitions, not new D claims.

Do not rewrite the old D IDs into the R definitions or give the old “Primary Entity” partition new life. Preserve their original Summary and content as history. The replacement R IDs are intentionally unassigned in this proposal.

Before archiving D258/D259, handle their live contextual references in CA-D-463, CA-D-464 and CA-D-465 against the admitted successors. Do not fabricate typed dependencies to preserve existing `relates_to` fields. Preserve real Carrier-bundle, one-object and materialization constraints. Exact reference edits belong to the admission operation after real successor IDs exist; this packet does not guess them.

## Checked companions that need no change here

- **CA-E-482, Version 13**, `06_evaluation/CA-E-482-CORE_META_MODEL-GENERAL-EVALUATION_APPROACH--validate-principle-content-role-semantics.md`: Delivery already “covers what a Carrier stores and how it represents or places that content.” It delegates role authority to current definitions, so no additional Carrier-specific rewrite is needed.
- **CA-D-262, Version 14**, `07_delivery/CA-D-262-CORE_META_MODEL-DELIVERY--register-current-file-carrier-formats.md`: concrete File Carrier format admission remains a Delivery representation policy. Do not remove Markdown/TOML/YAML/JSON support to fix classification.
- **CA-D-507, Version 3**, `07_delivery/CA-D-507-CORE_META_MODEL-CORE--separate-entity-identity-from-carrier-format.md`: changing representation format or extension alone must not change carried Entity identity. Preserve this constraint. It is not a definition that makes Carrier ID equal path.
- **CA-E-523, Version 4**, `06_evaluation/CA-E-523-CORE_META_MODEL-QA_CASE--journal-view-integrity.md`: its D341 reference remains valid because D341 retains the same protection and ID.

## Separate later content work

These findings do not justify widening this admission packet:

- **CA-D-416, Version 13**, `07_delivery/CA-D-416-CORE_META_MODEL-CORE--classify-markdown-atom-carrier.md`, defines Markdown Atom Carrier as narrower than File Carrier. That more specific kind is not one of the 45 prepared definition targets. Decide its representation-versus-kind treatment in the remaining content mapping; do not invent another R ID or delete a still-used specialization merely to finish this packet.
- **CA-D-505, Version 3**, `07_delivery/CA-D-505-CORE_META_MODEL-CORE--define-the-entity-carrier-binding.md`, prescribes obsolete `(Entity)/Carrier` property notation. **CA-D-506, Version 3**, `07_delivery/CA-D-506-CORE_META_MODEL-CORE--give-every-non-ephemeral-entity-a-carrier.md`, depends on that binding model. The prepared Carrier definitions do not adopt those prescriptions. Align the binding model separately without introducing per-field Carrier entries.
- **CA-D-451, Version 6**, `07_delivery/CA-D-451-CORE_META_MODEL-STANDARD--classify-folders-by-their-carrier-responsibility.md`, and **CA-D-464, Version 6**, `07_delivery/CA-D-464-CORE_META_MODEL-CORE--represent-one-governed-object-with-each-directory-carrier.md`, retain old Structural Entity/Revision language. Keep the useful distinction between carrying directories and administrative placement; do not silently rewrite those mixed claims during pure taxonomy retirement.
- **CA-E-522, Version 3**, `06_evaluation/CA-E-522-CORE_META_MODEL-QA_CASE--storage-boundary-classification-interpretability.md`, has broader storage/Journal assumptions, including rejection of runtime as canonical truth and one shared Work Journal. They require separate reconciliation with current Journal/storage policies. Do not use that broad check to reinterpret the narrow D341 cleanup protection or revive the rejected Storage Boundary property.
- **CA-R-1690**, `04_requirement/CA-R-1690-CORE_META_MODEL-CORE-REQUIREMENT--preserve-external-boundary-obligations.md`, discusses Delivery authority for Carrier names, identities and Catalog representations. Read those as representation/encoding, not permission for D-only entity definitions. Any ambiguous wording repair belongs to its own content review, not a blanket external-authority rewrite.

## Admission check

The minimal coordinated change consists of the three proposed revisions (R1342, M313, D341), retirement of D316, and conditional replacement retirement of D258/D259/D414 when their real R successors exist. Keep all prepared definition drafts inactive until the admitted operation actually creates their R sources and preserves predecessors.

Read back the changed sources and successor coverage; rebuild the source-derived graph without adding Carrier.Ownership Class or Carrier.Storage Boundary. No runtime test suite or live migration was run for this proposal.

