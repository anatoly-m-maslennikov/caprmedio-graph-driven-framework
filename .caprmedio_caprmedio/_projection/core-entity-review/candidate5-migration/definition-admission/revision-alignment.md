# Candidate #6 — narrow History / Revision source alignment

Status: proposed source-content alignment only. No source Atom, identity, lifecycle or runtime change has been made by this document.

Basis: Candidate #6 decisions 1, 3, 12, 19 and 29; its retained History/Revision branch; the prepared History and Revision/Type: Atom drafts; and the Operator's existing every-real-update Version decision. Sources below were read on 2026-10-16. Re-read them before applying these proposals; listed Versions identify the inspected state, not permanent tool pins.

## Boundary

- A current Atom is an Atom. Its Version Number does not turn it into a historical Revision entity.
- An archived Atom itself represents the preserved historical Atom state. Do not add a dependent `Atom.Revision`, a second current Atom, or another snapshot wrapper.
- Every actual same-ID Atom update increments Version by exactly 1 under CA-R-1432. A no-op does not. This update rule is distinct from the definition of a historical Revision.
- Preserve existing historical bytes. Neither this definition nor the proposals below require another snapshot, Journal baseline, earlier Journal entry, receipt, event-order check or publication gate. Git preservation is not replaced by a new mechanism.
- Do not rewrite all uses of the word Revision. References to earlier state, or old wording that does not introduce a conflicting rule, remain separate content-migration work.

## 1. CA-R-1371 — remove mutable historical-state exception

Source: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1371-CORE_META_MODEL-CORE--define-artifact-revision.md`

Current Version: **10**. Current Summary: **Define Artifact Revision**.

Blocker: its Claim first calls the state immutable, then permits Status and Updated At to change without another semantic Revision. Its `Artifact/Revision` Subject also preserves the old current-Artifact taxonomy. This contradicts the historical-state definition and the already-active CA-R-1432 / CA-R-1788 update rules.

Identity proposal: preserve CA-R-1371 and its exact Summary. It still defines the recorded historical state of an Artifact; this is a correction of that same definition. Do not rename the Summary to `Define Revision` silently: that would require a new ID under CA-R-1464.

Replace Subjects with:

```yaml
subjects:
  governs: "Entity/Continuant/History/Revision"
  depends_on:
    - "Entity/Continuant/History"
```

Replace Scope with:

> Preserved historical states of Artifacts.

Replace Claim with:

> a Revision **means** a preserved historical state of an Artifact. it belongs to History; it is **not** a dependent property of the current Artifact. the preserved state **must not** be edited as though it were the current state.

Replace Details with:

> A current Atom remains an Atom with its own Version Number and Updated At. Its accepted updates follow CA-R-1432 and CA-R-1788. An archived Atom itself represents the earlier Atom state; no additional Revision wrapper is required. This definition does not require a separate snapshot operation, Journal record, historical baseline or permission check. Journal records describe events, not Journal snapshots.

The separate prepared `Revision/Type: Atom` draft supplies the narrower Atom case. The generic definition does not prescribe Version fields for every other kind of historical state.

## 2. CA-R-1372 — retire Journal snapshot/revision rule

Source: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1372-CORE_META_MODEL--derive-journal-revision-updated-at.md`

Current Version: **11**. Current Summary: **Derive Journal Revision updated at**.

Blocker: its whole Claim requires `Journal/Revision` and a derived Updated At. Candidate #6 decision 19 explicitly retires this concept. CA-R-1745 already defines Journal as event records and distinguishes a record from its event.

Exact disposition: retire/archive CA-R-1372 using the admitted lifecycle route, preserving its history. Do not repurpose it as a Journal record timestamp rule.

- Replacement Subjects: none.
- Replacement Scope / Claim / Details: none.
- Replacement ID: none.
- Do not introduce `Journal.Updated At`, a Journal snapshot, or a new Journal-revision admission check.

This is an already-approved retirement proposal, not an executed retirement.

## 3. CA-R-1306 — replace old revision-owned Status definition

Source: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1306-CORE_META_MODEL-CORE-REQUIREMENT--define-status-as-an-artifact-revision-property.md`

Current Version: **13**. Current Summary: **Define Status as an Artifact Revision Property**.

Blocker: it defines Status generally as an Artifact Revision Property. Candidate #6 decision 29 explicitly makes Atom.Status a property of the Atom. The shared meaning across owners belongs to the derived Terms graph, not another authoritative universal definition layer. This is not fixed by changing its Subject alone.

Identity proposal: preserve the old Atom as history and prepare a new-ID, owner-qualified replacement. Its Summary must change; do not reuse CA-R-1306 for a differently named definition. No new ID is assigned here. Do not blindly redirect all old consumers to Atom.Status: uses concerning other owners or shared meanings need their existing occurrence-specific dispositions.

Proposed new Summary:

> Define Atom Status

Proposed Subjects:

```yaml
subjects:
  governs: "Entity/Continuant/Object/Atom.Status"
  depends_on:
    - "Entity/Continuant/Object/Atom"
    - "Entity/Continuant/Object/Atom/Content Role"
```

Proposed Scope:

> Status borne by an Atom, including the recorded value preserved in an archived Atom.

Proposed Claim:

> Atom.Status **means** the Atom's lifecycle classification under its applicable Status model. Status is a dependent property of the Atom; its allowed values resolve under the applicable Atom, Content Role and Type rules.

Proposed Details:

> IS_BORNE_BY expresses the property-to-Atom relation. A current Atom is not a historical Revision merely because it has a Version Number. An archived Atom preserves its recorded Status; preserving history does not rewrite that value. CA-R-1412 supplies the one-Status requirement. The separate allowed-value rules define inherited and additional values; this definition adds no values, transition procedure or mandatory history record. Shared Status meanings are derived in the Terms graph from source usage, not independently authored here for every owner.

The already-prepared `Define Atom.Status allowed values` draft remains separate: it governs the base set and inheritance, not this property's meaning. Cross-owner Status / Activity and allowed-value conflicts are owned by their respective alignment proposals, not silently resolved by this replacement.

## 4. CA-D-256 — move the definition to R and preserve a D binding policy

Source: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/CA-D-256-CORE_META_MODEL-CORE-DELIVERY--define-carries.md`

Current Version: **14**. Current Summary: **Define CARRIES**.

Blockers: the second Details bullet says that whenever a carried Entity has Revisions, its binding identifies the exact carried Revision. Applied literally to a current Atom, this substitutes a Revision for the actual Atom. Separately, this D Atom is the sole inspected defining authority for CARRIES: no current Core R contains a CARRIES definition. Merely correcting D256's Details would leave the defining-R requirement unmet.

Identity proposal: replace the mixed D256 contribution with a new R definition and a separate new D representation/binding policy. The D successor's Summary and primary contribution change, so do not reuse CA-D-256. Do not change D256's Content Role to Requirement while keeping its D ID. Preserve D256 as history only after the approved successors are admitted. No successor ID is allocated here.

This supersedes the earlier same-ID D256 proposal. Coordinate with [carrier-alignment.md](carrier-alignment.md), especially R1342 and M313: R defines Entities and Relation kinds; D specifies representation. These are proposals, not completed R coverage.

### 4a. New supporting R — same CARRIES meaning

Proposed Summary:

> Define CARRIES

Proposed Subjects:

```yaml
subjects:
  governs: "Entity/Continuant/Object/Relation/Type: CARRIES"
  depends_on:
    - "Entity/Carrier"
    - "Entity"
    - "Entity/Continuant/Object/Relation"
```

Proposed Scope:

> Carrier bindings of non-ephemeral Entities.

Proposed Claim, preserving D256's existing definition exactly:

> CARRIES **means** the directed Relation from a Carrier **to** the non-ephemeral Entity that it stores **or** represents.

Proposed Details:

> IS_CARRIED_BY **means** the inverse of CARRIES, directed from a non-ephemeral Entity to its Carrier. The Entity/Carrier binding exposes this inverse direction; it is not a separately authored primitive Relation fact. This preserves the existing meaning defined by CA-D-257. Neither direction requires a separately registered binding for each YAML field or Markdown section, a new Carrier, a snapshot or a historical record. The applicable D policy specifies how the represented Entity is bound and represented. No additional endpoint class, graph ownership, cardinality or inference permission is introduced by moving this definition to R.

The new R must be admitted before it is cited as defining authority. It defines CARRIES and its existing inverse direction together, not two independent primitive facts. This text preserves existing semantics; it does not claim a complete new Relation registry admission.

### 4b. New D successor — representation binding only

Proposed Summary:

> Bind Carriers to their represented current or historical Entities

Proposed Subjects:

```yaml
subjects:
  governs: "Entity/Carrier"
  depends_on:
    - "Entity"
    - "Entity/Continuant/Object/Relation/Type: CARRIES"
    - "Entity/Continuant/History/Revision"
```

Proposed Scope:

> Carrier bindings of non-ephemeral Entities.

Proposed Claim:

> a Carrier binding **must** identify the Entity actually represented by that Carrier. a current Entity's Carrier binds that current Entity; a preserved historical state's Carrier binds that Revision. citing a current Entity's Version **must not** reclassify the current Entity as a historical Revision.

Proposed Details:

> Use the separately defined CARRIES meaning. Its IS_CARRIED_BY inverse exposes the same binding with the endpoints reversed; neither direction substitutes a historical Revision for the current Entity actually represented. The applicable Carrier policy determines the representation. General representation rules may carry dependent properties inside one File Carrier; this policy does not require a separately registered binding for each field or section. It creates no additional Carrier, snapshot, Journal record or history gate.

No new Carrier is demanded. Existing files, folders and database representations remain governed by their existing D rules.

### 4c. CA-D-257 — preserve the existing inverse in R, then retire the D definition

Source: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/CA-D-257-CORE_META_MODEL-CORE-DELIVERY--define-is-carried-by.md`

Current Version: **15**. Current Summary: **Define IS_CARRIED_BY**.

Its Claim defines IS_CARRIED_BY as the inverse of CARRIES, directed from a non-ephemeral Entity to its Carrier. Its Details repeat the exact-carried-Revision conflation. Leaving this active unchanged would restore both the D-only definition problem and the binding ambiguity.

Exact disposition: after the proposed supporting CARRIES R and the new D binding-policy successor are admitted, archive CA-D-257 with its original Summary and content preserved as history. The R Details above retain its entire inverse meaning. The new D successor governs the shared binding in both directions and removes the current/historical conflation. No independent D257 policy remains after those two contributions are preserved.

- Replacement Subjects / Scope / Claim / Details on CA-D-257 itself: none; it is retired, not rewritten into another Content Role.
- Separate inverse primitive or separately authored inverse fact: none.
- Extra inverse-specific successor ID: none. The same supporting R and D successors replace the relevant contributions of both D256 and D257.

Coordinate this conditional retirement with the Carrier lane's R1342/M313 alignment. References to the old defining D Atoms must resolve to the admitted successors according to the meaning they use; exact successor IDs remain unassigned. Do not retire either D definition while only proposal text exists. This does not authorize creating typed dependencies where a consumer only has a contextual reference.

## Existing support — leave unchanged for this narrow alignment

| Source | Inspected Version | Why no additional edit is required here |
| --- | --- | --- |
| CA-R-1432 | 13 | Already increments Version exactly once for every actual same-ID update, keeps no-ops unchanged, and preserves exact predecessor bytes. Its semantic change-class label does not require inventing another Revision wrapper. |
| CA-R-1788 | 6 | Already separates a current Status update from copying exact historical bytes and excludes ancestor-only locator changes. |
| CA-R-1745 | 20 | Defines Journal as records about events, not the events themselves. No Journal snapshot is needed. |
| CA-R-1192 | 12 | Defines dependency through a bearer but does not classify Revision as a Dependent Entity. |
| CA-R-1260 | 14 | Defines IS_BORNE_BY for actual dependent entities; no inspected clause forces Revision to use it. |
| CA-D-565 | 4 | Applies only when an Atom newly attains Archived Status and no more-specific mapping exists. It explicitly does not settle placement for every historical predecessor; do not generalize it into a rewrite of exact old bytes. |

No explicit current rule asserting `Revision IS_BORNE_BY Atom` was found. Do not invent such a rule to remove it; the observed contradictions are the old definition/Subjects and the exact binding clause above.

## Deferred, not definition-admission blockers

- CA-R-1268 v12 defines the old Artifact partition. Its broader disposition belongs to the already-planned Artifact / Structural Entity content pass, not a blanket replacement with History or Object.
- CA-R-1419 v9 restricts when Archived Status is admissible. It does not require every preserved predecessor to have its stored Status rewritten to Archived. Its old Activity dependency and Subjects need the separate Status/partition cleanup.
- CA-R-1412 v11, CA-R-1415 v12, CA-R-1416 v12, CA-R-1417 v11, CA-R-1078 v17 and CA-R-1080 v16 use older Atom Revision wording while their current Subjects already govern Atom properties. Clarifying those titles/Scopes is later content work; do not assign new IDs merely to complete this historical-state definition. Their claims about preserved values do not require an Atom.Revision property.
- CA-R-1311 v15, CA-R-1501 v6 and CA-R-1502 v6 use old Artifact/Revision/currentness terminology. They do not authorize editing preserved historical bytes; wider owner/Term mapping remains deferred.
- CA-D-270 v15, CA-D-274, CA-D-446, CA-D-463, CA-D-483 v8 and the edit-draft rules use older revision wording or concrete carrier conventions. Preserve actual Version, Status, Author and exact-state references. No bulk carrier migration or serialization change is included here.
- CA-R-366 v23 and CA-R-1314 v16 retain exact-state/provenance references. Referencing an Atom's exact Version does not by itself create another Entity. Applicable Methodology relocation/content alignment remains separate.

## Acceptance for this proposal packet

- R1371, the owner-qualified Status replacement, the supporting CARRIES R definition and the D binding-policy successor have exact proposed text. The Journal snapshot rule has an explicit no-replacement retirement. D257 has an exact conditional retirement, with its existing inverse meaning preserved in the supporting R and its representation implications preserved in the shared D successor.
- R1371 preserves its existing ID and Summary. R1306 requires a new ID for its corrected owner-qualified Summary/definition. D256 is replaced by separately identified R and D contributions; its D successor's changed Summary requires a new D ID. No successor ID is allocated here.
- Admission must not be reported from this proposal. Active source edits, lifecycle effects, current-source graph regeneration and evaluation remain separate work.
- No statement here establishes that all Entities or Relations have defining R coverage. The supporting CARRIES R is still a proposal, not an active source.
- No new snapshot, history-completeness, Journal, ordering, permission or runtime gate is introduced.
