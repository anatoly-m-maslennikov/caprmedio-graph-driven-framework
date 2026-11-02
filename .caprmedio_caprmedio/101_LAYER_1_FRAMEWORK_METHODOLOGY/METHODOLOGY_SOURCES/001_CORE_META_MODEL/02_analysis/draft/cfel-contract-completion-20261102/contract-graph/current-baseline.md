# Formal Contract Graph

Bounded extraction only. CFEL blocks remain authoritative source text; this view does not execute CFEL.

## Coverage

- candidate sources: 1101
- bound sources: 557
- declared entity targets: 129
- declared component targets: 2
- declared relation targets: 12
- shared sources: 413
- fenced claim blocks: 176
- cfel blocks: 105
- recognized clauses: 178
- unsupported clauses: 104
- coverage gaps: 544
- duplicate declarations: 1
- missing relation semantics: 12
- inheritance diagnostics: 1

## Declared Narrowing Tree

Each identity has its source-bound contract below.

```text
CFEL
Carrier
	/ Database
	/ Directory
	/ Docker Image
	/ File
		/ Markdown
			/ Markdown Atom Carrier
	/ Git Branch
	/ Git Commit
	/ Git Index
	/ Git Repository
	/ Pull Request
Event Record
Node
	/ Aspect
	/ Continuant
		/ Actor
		/ Atom
			/ (.Role:=Analysis)
			/ (.Role:=Concern)
			/ (.Role:=Delivery)
			/ (.Role:=Evaluation)
			/ (.Role:=Method)
			/ (.Role:=Operations)
				/ Action
				/ Step
				/ Substep
				/ Workflow
			/ (.Role:=Plan)
			/ (.Role:=Requirement)
				/ (.Form:=Declaration)
				/ (.Form:=Relation Definition)
		/ Journal
		/ Named Selection
		/ Package
			/ Implementation
		/ Projection
		/ Scope Unit
			/ Project
	/ MODEL
	/ Occurrent
	/ PROJECT STRUCTURE
Term
```

## Entity and Property Contracts

### `Actor` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Declaration source: `CA-R-2542@2`
  - Semantics:
    An Actor participates in Project work.
  - Fenced Claim block:
```CFEL
Actor;
Actor ((NARROWER_THAN)) @Continuant
```
  - Allowed Relations and other formal clauses:
    - `Actor` — NARROWER_THAN → `@Continuant`; Host=undefined; Target=undefined
  - Unresolved CFEL: `Actor`
- Shared RMED source: `CA-R-2156@10`
  - Remaining Claim prose:
    **every** Actor that performs **or** authorizes a governed action **must** have **`=1`** Type **in** (Operator, AI Agent).
- Shared RMED source: `CA-R-1250@26`
  - Remaining Claim prose:
    the Term Actor **must** be NARROWER_THAN Primary Entity.
- Shared RMED source: `CA-R-2425@2`
  - Remaining Claim prose:
    - **only** an Operator **may** resolve a conflict between active Project-wide foundational invariants, **and** an Operator's decision to resolve that conflict is non-delegable.
    - an AI Agent **may** detect, analyze, **and** propose resolutions for a conflict between active Project-wide foundational invariants but **must not** choose a resolution for a conflict between active Project-wide foundational invariants.
    - an AI Agent **may** resolve a conflict that does **not** involve two active Project-wide foundational invariants **only** **when** the AI Agent's active Operator delegation permits **every** required action **and** the configured confidence requirements are satisfied.

### `Aspect` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Node` — CA-R-2462@2
- Declaration source: `CA-R-2543@2`
  - Semantics:
    An Aspect is a topic through which an Atom addresses its Subject.
  - Fenced Claim block:
```CFEL
Aspect;
Aspect ((NARROWER_THAN)) @Node
```
  - Allowed Relations and other formal clauses:
    - `Aspect` — NARROWER_THAN → `@Node`; Host=undefined; Target=undefined
  - Unresolved CFEL: `Aspect`

### `Atom` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Declaration source: `CA-R-2508@2`
  - Semantics:
    An Atom is the smallest independently governed Artifact.
  - Fenced Claim block:
```CFEL
Atom;
UNIQUE(Atom//, (.ID, .Version));
Atom ((NARROWER_THAN)) @Continuant
```
  - Allowed Relations and other formal clauses:
    - `Atom` — NARROWER_THAN → `@Continuant`; Host=undefined; Target=undefined
  - Unresolved CFEL: `Atom`
  - Unresolved CFEL: `UNIQUE(Atom//, (.ID, .Version))`
- Shared RMED source: `CA-R-636@13`
  - Remaining Claim prose:
    **before** closing a material Concern, CAPRMEDIO **must** inspect its upstream RMED lineage **and** update the earliest inadequate active owner.
- Shared RMED source: `CA-R-1033@28`
  - Remaining Claim prose:
    When a Lineage Impact analysis addresses an Atom, `compatible` must mean the child remains valid against the parent Revision required by the gate and traversal stops without a child update; a pinned earlier Revision does not establish compatibility where the new Revision is required.
- Shared RMED source: `CA-R-1034@26`
  - Remaining Claim prose:
    When a Lineage Impact analysis addresses an Atom, `update_required` must mean the child requires a new Revision against the new parent Revision before traversal continues.
- Shared RMED source: `CA-R-1035@26`
  - Remaining Claim prose:
    When a Lineage Impact analysis addresses an Atom, `replacement_required` must mean the child requires a successor and archival before traversal continues through every affected descendant.
- Shared RMED source: `CA-R-1036@26`
  - Remaining Claim prose:
    When a Lineage Impact analysis addresses an Atom, `uncertain` must mean a blocking Question or Problem is required and traversal stops until resolution.
- Shared RMED source: `CA-R-1037@26`
  - Remaining Claim prose:
    a Lineage Impact Analysis Atom **must** identify the changed Atom **and** exact previous **and** new Revisions, change class **and** basis, responsible Operator **and** session provenance, expected impact radius, **every** examined child Revision **and** disposition with its basis, **every** resulting Revision, successor, **or** blocking Concern Atom, **every** recursive branch result, **and** the overall fixed-point conclusion.
- Shared RMED source: `CA-R-1256@25`
  - Remaining Claim prose:
    the Term Relational Atom **must** be NARROWER_THAN Atom.
- Shared RMED source: `CA-R-1432@27`
  - Remaining Claim prose:
    **before** changing an admitted Atom, CAPRMEDIO **must** assign **`=1`** change class using these boundaries, identity results, **and** required reviews:
    
    | Change class | Boundary | Identity result | Required review |
    |---|---|---|---|
    | `carrier_only` | Representation, the Atom's own filename **or** local placement, encoding, **or** lossless Entity-name/reference renaming **without** changing governed meaning **or** the Atom's Summary value **or** Content Role | Keep the Atom ID; increment Version by exactly **`1`** | Verify lossless recoding |
    | `refinement` | Wording **or** criteria become clearer **or** stricter while content, applicability, **and** acceptance meaning remain equivalent **and** Summary **and** Content Role remain unchanged | Keep the Atom ID; increment Version by exactly **`1`** | Demonstrate equivalence |
    | `semantic_revision` | Meaning **or** applicability changes while Summary **and** Content Role remain unchanged | Keep the Atom ID; increment Version by exactly **`1`** | Declare the delta **and** complete lineage-impact review |
    | `replacement` | the Summary value changes under CA-R-1464 **or** Content Role changes | Create a new Atom ID; preserve the predecessor **and** successor identity binding under CA-R-807 | Review the replacement boundary **and** affected lineage |
    
    For an existing Atom, only a Summary **or** Content Role change creates a new base Atom ID. Content Role changes always create a new Atom, even with unchanged Summary. Claim, other Content, Type, Status, applicability **or** other property changes alone retain the base ID when Summary **and** Content Role stay unchanged. Scope narrowing **or** expansion is a `semantic_revision`, **not** carrier-only. Adding a separately authored Atom gives that new Atom its own ID; it does not itself replace an existing Atom whose Summary **and** Content Role remain unchanged. Lossless serialization of the same Summary value is **not** a Summary change. the semantic change class is independent of storage transactions **or** version-control change sets; persistence preserves the admitted Atom, Carrier, **and** Journal authority.
    
    **every** actual same-ID update **must** increment Version by exactly **`1`**, regardless of change class, **and** refresh Updated At under CA-R-1788. an exact no-op **must** retain Version **and** Updated At. When a predecessor is archived, its Archive Carrier **must** carry `status: Archived`, identify that predecessor as `<canonical-ID>@<old-version>`, and preserve its numeric Version, prior Updated At, and unrelated content. The Current successor retains the canonical ID, advances Version by exactly **`1`**, and receives the actual Project-time edit instant. Git history preserves the exact pre-archive Carrier bytes; the archive conversion does not require an exact-byte copy.
    
    this classification concerns changes **to** the Atom's own bytes, metadata, direct ownership **or** local placement. moving an ancestor **only** changes a descendant's repository locator **when** that descendant's own bytes, metadata, direct owner **and** placement relative **to** that owner remain unchanged; this is **not** an Atom update **and** **must** retain that descendant's Version **and** Updated At. this boundary applies **to** **all** Atoms, including Plans nested under a moved Plan **and** Atoms whose owning Scope Unit moves. an actual change **to** the Atom itself, including its Status, filename, direct owner **or** local placement, still follows the classification **and** revision rules above. Exact pre-change bytes remain available through Git history.
    
    Tools **may** propose a class but **must** fail closed **when** the distinction between refinement, semantic revision, **and** replacement is uncertain.
- Shared RMED source: `CA-R-1448@25`
  - Remaining Claim prose:
    Targeting Atoms **means** the set of **all** Atoms whose resolved Claim Target Scope Unit **`=`** the selected Scope Unit, independently of **where** those Atoms are owned **or** stored.
- Shared RMED source: `CA-R-1449@21`
  - Remaining Claim prose:
    Subtree-targeting Atoms **means** the union of Targeting Atoms for the selected Scope Unit **and** **every** descendant Scope Unit.
- Shared RMED source: `CA-R-1497@23`
  - Remaining Claim prose:
    a Lineage Impact Analysis Atom **must not** serve as execution evidence of its own correctness. Analysis **and** the factual Journal Records carrying execution evidence remain distinct contributions under CA-R-1683 **and** CA-R-1684.
- Shared RMED source: `CA-R-1499@21`
  - Remaining Claim prose:
    For an Atom as a governed Artifact, Authority must mean its governed capacity to establish meaning of a declared kind.
- Shared RMED source: `CA-R-1500@21`
  - Remaining Claim prose:
    The following interpretation is required when this governed concept is used:
    
    Applicability **means** whether an Artifact's governed meaning applies **in** a particular declared context, including structural scope, selected capability, environment, version, **or** time boundary.
- Shared RMED source: `CA-R-1501@21`
  - Remaining Claim prose:
    For an Atom as a governed Artifact, Currentness must mean which exact applicable Artifact Revision is presently effective in the declared context.
- Shared RMED source: `CA-R-154@34`
  - Remaining Claim prose:
    **every** Atom **must** contain **only** content necessary for its one independently replaceable Claim.
- Shared RMED source: `CA-R-1578@25`
  - Remaining Claim prose:
    Hub Atom **means** a derived description of a Plan Atom with **`>0`** outgoing derived `CONTAINS` links to Plan Atoms; it does **not** introduce another Type, Subtype, stored classification, identity, **or** authority tier. contained Atoms retain their own Claims rather than becoming parts of the Hub Claim.
- Shared RMED source: `CA-R-1598@25`
  - Remaining Claim prose:
    **every** Atom Revision **must** carry its applicable Properties within its own Markdown Carrier so that its own declared content can be read **without** reconstructing it from a filename **or** directory placement.
    
    - the applicable model determines which Properties are required, optional, **or** inapplicable; self-sufficiency does **not** invent missing Properties **or** permit an invalid value.
    - a Relation **to** another Atom remains declared **only** on its registered owning endpoint; the other endpoint **and** inverse views are resolved from that declaration, **not** independently copied.
    - self-sufficiency does **not** require copying the referenced Atom, governing model, **or** inherited Settings authority into this Atom.
- Shared RMED source: `CA-R-1630@41`
  - Remaining Claim prose:
    the effective atomic admission strictness setting **must** be **in** (`medium`, `high`).
    
    **at** medium strictness, CAPRMEDIO requires accepted authority, **`=1`** primary Claim, **`=1`** enabled Artifact Type, owning Scope, creation provenance, material relations, priority for Concern Atoms **only**, **and** sufficient precision **to** establish a stable Artifact identity **and** initial accepted Revision. optional non-authoritative context **may** remain explicitly unknown.
    
    **at** high strictness, CAPRMEDIO stops **before** emission while **any** material authority, definition, boundary, classification, Scope, lineage, Conflict, **or** Evaluation question remains ambiguous. it asks focused questions **until** the Atom meets the same one-primary-Claim identity standard.
    
    the two levels assess one-step promotion eligibility. promotion is proposed **only** **when** the Claim applies unchanged at the broader enabled Scope **and** always requires explicit Operator acceptance.
    
    admission does **not** prohibit later same-ID Revisions. **every** later change passes the atomic change-class gate; changing the primary Claim identity requires a replacement.
- Shared RMED source: `CA-R-1633@40`
  - Remaining Claim prose:
    **every** `semantic_revision` **or** `replacement` of an admitted Atom **must** retain **`=1`** identifiable Lineage Impact Analysis whose primary conclusion is the impact state of that exact changed parent Revision. The assessment **may** be part of an existing completed shared review package; a separate Analysis Atom for each changed Atom is not required. A `carrier_only` **or** equivalent `refinement` change **must** require lossless-recoding **or** equivalence Verification instead.
- Shared RMED source: `CA-R-1671@27`
  - Remaining Claim prose:
    `eng_decision` **must** be registered as orphan-permitted, so an active Eng Decision **may** have no parent Eng Policy even **in** strict authority mode.
- Shared RMED source: `CA-R-1672@27`
  - Remaining Claim prose:
    `eng_policy` **must** be registered as terminal-permitted, so an active Eng Policy Atom **may** remain childless in Atom topology **after** its local Eng Decision Atoms have been losslessly absorbed **and** archived.
- Shared RMED source: `CA-R-1685@28`
  - Remaining Claim prose:
    User Stories **and** intended Outcomes remain optional framing, while measured **or** reported outcomes remain factual observations rather than reusable Operations definitions.
- Shared RMED source: `CA-R-1689@33`
  - Remaining Claim prose:
    **every** semantic change **to** CORE_META_MODEL follows one closed amendment sequence:
    
    1. explore **without** changing governed truth;
    2. obtain explicit operator acceptance for one primary claim;
    3. map affected authority, layers, handoffs, Projections, Methods, Evaluation, Delivery, Implementations, **and** Operations;
    4. verify CORE_META_MODEL eligibility **and** acyclic layer placement;
    5. persist the accepted Atom **or** Atom Revision;
    6. archive **only** predecessors that are fully replaced;
    7. complete revision-bound lineage-impact review through **every** affected descendant;
    8. refresh **every** affected declared Projection required by the applicable gate; **and**
    9. verify the resulting authority **and** downstream fixed point.
- Shared RMED source: `CA-R-1716@28`
  - Remaining Claim prose:
    Concern, Analysis, Task, **and** native Implementation **may** propose a PRMEDO authority change, but **only** Operator-approved PRMEDO authority **may** establish that change.
- Shared RMED source: `CA-R-2102@14`
  - Remaining Claim prose:
    For every complete Current Atom, require one Role, Form, ID, Status, Updated At, Version, Tier, effective Label and Summary, subject to their applicable individual Declarations. Version is a positive integer; Updated At is a datetime with timezone. The effective Label is the explicit Label when present and otherwise the Form name. Author is not an Atom Property.
    
    Subjects is a grouping Property with no direct value. Its active Subject has one reference and its passive Subjects have zero or more references. Resolve the target Scope from the active Subject under the applicable model rules. Carrier compatibility fields do not override that resolution. Encode direct Node-instance Relation facts under Relations.
    
    For RMED, require one Claim as its direct Markdown value. CFEL may provide that value without prose. Do not create a Formal Claim child. Apply the respective content rules for Concern, Analysis, Plan and Operations, and preserve their established primary content headings.
    
    A Draft may be incomplete but carries exactly one Atom ID; report missing required Properties and check the complete applicable Current contract before promotion. Each Property's own values and dependent Properties are counted independently.
    
    Legacy carrier spellings remain readable during migration. This transition does not assert additional Atom Properties.
- Shared RMED source: `CA-R-366@35`
  - Remaining Claim prose:
    **every** exact Atom Revision reference **must** identify Atom identity, Version, **and** Updated At.
- Shared RMED source: `CA-R-771@32`
  - Remaining Claim prose:
    an Atom **must** be split **when** part of its content can be accepted, replaced, **or** retired independently from the Atom's remaining Claim.
- Shared RMED source: `CA-R-829@33`
  - Remaining Claim prose:
    **every** active Current-scope Requirement Atom is an authority peer of **every** other active Current-scope Requirement Atom **in** the same numeric Tier.
- Shared RMED source: `CA-R-922@38`
  - Remaining Claim prose:
    a Current-scope Atom **means** an Atom whose resolved Claim Target Scope Unit **`=`** its current Scope Unit.
- Shared RMED source: `CA-R-923@39`
  - Remaining Claim prose:
    a Relational Atom **means** an Atom that has no containing Scope Unit **or** whose resolved Claim Target Scope Unit differs from its current Scope Unit.
- Shared RMED source: `CA-M-288@22`
  - Remaining Claim prose:
    **to** refer **to** Subtree-targeting Atoms filtered **to** Active Revisions **and** Content Role **in** (Requirement, Method, Evaluation, Delivery), an Author **may** use `spec` as a non-authoritative alias for that same filtered set.
- Shared RMED source: `CA-E-240@46`
  - Remaining Claim prose:
    **Claim checked.**
    
    **every** Atom resolves its ownership, **`=1`** GOVERNS Subject, **and** zero **or** one Claim Target Scope Unit independently of **any** applicability restrictions **in** its Main Content. Applicable Goal and Demand rules, including the Operator-owned Project Goal, retain their required target conditions.
- Shared RMED source: `CA-E-425@30`
  - Remaining Claim prose:
    the Relational Atom classification Evaluation **must** enforce the qualified Types admitted by CA-R-924 **without** treating Plan Labels as Types.
    
    - accept permitted relational Requirement/Goal, Requirement/Demand, **and** Plan/Plan cases with explicit non-default Claim targets.
    - accept a current-scope Plan with decomposition **or** blocking **without** classifying it as relational merely because those Relations exist.
    - change the Plan Label from Task **to** Objective **or** Epic; retain the same target-based classification.
    - reject an unregistered qualified Type, an invalid relational target, **or** a Label interpreted as Type authority.
    
    report the exact Atom, qualified Type, **and** target condition.
- Shared RMED source: `CA-E-444@34`
  - Remaining Claim prose:
    the Evaluation **must** check selected authoritative Method Atoms of Type Term Definition for well-formedness **and** exactly-one defining authority, **then** check the authored sources **in** this order: entity names, Claim, Claim Scope, Semantics, Details, **and** other authored fields. It **must** compare Term occurrences with the meaning established by their explicit authoritative Term Definition **and** compare complete entity names with their source-backed canonical entities. Agreement between several Semantics sections **must not** substitute for a Term Definition. The results **must** distinguish well-formedness, source consistency **and** checked coverage, preserve source Atom, Revision **and** exact field occurrence for **every** finding, **and** leave insufficient identity, authority **or** coverage evidence unresolved rather than passed.
- Shared RMED source: `CA-E-520@30`
  - Remaining Claim prose:
    an RMED Atom passes this local Evaluation **only** **when** **all** of these checks pass with source evidence:
    
    Apply CA-R-2500 and CA-D-479 to every RMED Claim. Check its readable prose and any R-only nested Formal claim as one scoped contribution; Semantics and Details are optional supporting sections.
    
    | Check | Passing condition |
    |---|---|
    | properties | frontmatter is valid; required local Properties are present, admitted, correctly typed, **and** consistent with the body; body Properties occupy their required sections; values are **not** inferred from filenames **or** folders |
    | scope | **`=1`** coherent applicability description applies throughout the contribution **and** supporting text; a composite boundary **may** describe **`=1`** Scope |
    | claim | Claim expresses **`=1`** independently replaceable contribution **and** distinguishes capability requirements from authorization **to** execute; multiple clauses, conditions, **or** allowed values alone do **not** imply multiple Claims |
    | details | Details explain the scoped Claim **without** adding an independent obligation, permission, exception, **or** applicability change |
    | summary | Summary faithfully shortens the scoped Claim **without** changing its contribution **or** decisive boundary |
    | cce | the complete Markdown follows the supplied current CCE rules, including syntax, capitalization, structure, **and** understandability |
    
    a failed check **must** identify its local source evidence, rule, **and** proposed correction. unresolved required local evidence **must** remain a coverage gap. a pass **must** include a concrete source observation **and** the rule it satisfies. mechanical evidence does **not** prove Claim meaning.
- Shared RMED source: `CA-E-668@2`
  - Remaining Claim prose:
    For **every** selected Scope, the complete set of active Atoms **must** align with **every** active Project-wide foundational invariant.
- Shared RMED source: `CA-D-270@27`
  - Remaining Claim prose:
    **every** Markdown Atom Revision Carrier **must** serialize its positive integer Version as `version` **and** its Project-time Updated At value as `updated_at` **in** YAML frontmatter.
- Shared RMED source: `CA-D-303@28`
  - Remaining Claim prose:
    **every** Atom replacement **or** archival operation **must** replace **or** archive one whole Atom Carrier as one atomic Carrier transition.
- Shared RMED source: `CA-D-336@30`
  - Remaining Claim prose:
    Active Atom Carrier discovery **must** resolve requested Atom IDs from the identities carried inside the selected Project-owned Markdown source frontier **and** select carried Status Active.
    
    - validate the associated canonical addresses against those internal values under CA-D-480.
    - report zero **or** multiple Active matches **and** missing **or** conflicting identity **or** Status; do **not** repair discovery by silently preferring a filename **or** directory.
    - a non-Active containing Hub does **not** change the Status of a nested Atom.
- Shared RMED source: `CA-D-398@26`
  - Remaining Claim prose:
    An owning Atom may carry its explicitly defined machine-readable Properties in YAML frontmatter. Its RMED Claim remains in Markdown, with an optional R-only nested Formal claim; frontmatter is not a second Claim or independent source. legacy `project_scope_unit_graph` **or** `project_graph_state` YAML maps **may** be read as migration evidence; they **must not** own current Scope Unit declarations, paths, Scope Unit Name/order values, Project identity, Project Prefix, **or** selected Authority Modes. Project initialization inputs belong **to** Project Settings; instance defaults belong **to** Framework Instance Settings; unit declarations **and** explicit unit overrides belong **to** Project Structure. this format does **not** require creation **or** consumption of a structural Projection.
    
    ### Current source pin
    
    Proposed N+1 successor of `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/CA-D-398-CORE_META_MODEL-ENG_DECISION--encode-configuration-surfaces-in-owning-atoms.md`, CA-D-398@24, SHA-256 `256cbe9a58a3d46138774de8baef3061b7a0520d292867474cc2a13f56c80bc9`. Current bytes remain unchanged; this Draft does not restore legacy frontmatter metadata as authority.
- Shared RMED source: `CA-D-463@26`
  - Remaining Claim prose:
    **every** Atom Revision **must** have **`=1`** authoritative Carrier Bundle on the Project filesystem containing **`=1`** Markdown File Carrier **and** **`>=0`** additional Carriers admitted by its applicable Delivery authority.
    
    the Markdown file carries the Atom's own Properties under CA-D-478 **and** CA-D-479. additional Carriers represent that same Revision **without** replacing the mandatory file **or** independently redefining its Properties.
- Shared RMED source: `CA-D-478@31`
  - Semantics:
    YAML and Markdown are carrier locations for different Atom properties, not
    alternative authorities for the same value. A section's name identifies its
    `content.*` property; a metadata property remains a YAML value.
  - Remaining Claim prose:
    Use YAML Frontmatter for an Atom's metadata properties. Use named Markdown
    Main Content sections for `content.*` properties. Each applicable Atom Property
    has one canonical internal location; its value is not duplicated between YAML
    and Markdown.
    
    This reusable Policy governs Atom representation. It does not create a Carrier
    or a CARRIES fact for each property or section, and it does not change the
    owning direction of an Atom-to-Atom Relation.
    
    Qualified classifications are carried as ordinary metadata properties. For example, `Atom/(.Role := Concern)` selects the Atom's `role` value, and a qualified Form selects its `form` value; neither creates a nested Role object. Use the property names and canonical value encodings registered by the applicable D policy, including CA-D-657, rather than inventing a new field from the display path.
- Shared RMED source: `CA-D-480@23`
  - Remaining Claim prose:
    **every** Atom Property represented by a filename, matching directory name, **or** placement **must** agree with its canonical internal value under the applicable Delivery encoding.
    
    - compare resolved values using the registered encoding; a Summary Slug is checked against its Summary serialization, **not** against identical raw text.
    - a mismatch is invalid **and** **must** be reported; the address **must not** silently override the value carried inside the Atom.
    - agreement checking does **not** authorize rewriting the Atom **or** address. corrections require the applicable authorized change.
- Shared RMED source: `CA-D-485@24`
  - Remaining Claim prose:
    a writer **must** preserve the distinction between a defaulted Atom Property **and** an inherited external setting:
    
    - a required Atom value selected by applying a default is still carried at its canonical internal location; equality **to** that default does **not** permit omitting the value.
    - an unselected optional override remains absent; do **not** copy an inherited effective setting into a locally selected override.
    - retain an explicit override even **when** it currently equals the inherited value, because later upstream changes **must not** change that selection.
- Shared RMED source: `CA-R-2123@9`
  - Remaining Claim prose:
    Each Current Method Atom in this Scope must use Eng Policy or Eng Decision. Each Current Delivery Atom uses Policy or Decision under the general Delivery Type definitions.
- Shared RMED source: `CA-D-664@2`
  - Remaining Claim prose:
    The Carrier below is the Markdown file delivering this Atom.
    
    Frontmatter starts at the beginning of the file:
    
    1. An opening line containing `---`.
    2. YAML data.
    3. A closing line containing `---`.
    
    Location is the directory path relative to the repository root.
  - Fenced Claim block:
```CFEL
Atom >> @Carrier//Markdown file;
Atom.**!(.Content, .Content.**) >> @Carrier//Markdown file.frontmatter;
Atom.Content.** >> @Carrier//Markdown file.markdown;
@Carrier//Markdown file.filename{:1}: [string]{:1};
@Carrier//Markdown file.location{:1}: [string]{:1};
@Carrier//Markdown file.frontmatter.author{:0}
```
  - Unresolved CFEL: `Atom >> @Carrier//Markdown file`
  - Unresolved CFEL: `Atom.**!(.Content, .Content.**) >> @Carrier//Markdown file.frontmatter`
  - Unresolved CFEL: `Atom.Content.** >> @Carrier//Markdown file.markdown`
  - Unresolved CFEL: `@Carrier//Markdown file.filename{:1}: [string]{:1}`
  - Unresolved CFEL: `@Carrier//Markdown file.location{:1}: [string]{:1}`
  - Unresolved CFEL: `@Carrier//Markdown file.frontmatter.author{:0}`
- Shared RMED source: `CA-R-2556@2`
  - Remaining Claim prose:
    - For an Atom with an active Subject, all assertions and prescriptions concern that active Subject.
    - References to other Subjects describe the active Subject's endpoints, inputs, outputs, conditions or dependencies.
    - Independent assertions about another Subject belong in an Atom with that active Subject.
    - For an Atom whose active Subject is a Node, each Relation count constrains that active Subject's own outgoing Relations.

### `Atom/(.Role:=Analysis)` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Atom` — CA-R-2508@2
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Inherited Property Declaration refs; no child Property Node is created:
  - `Atom.Status` — CA-R-2488@2
  - `Atom.Updated At` — CA-R-2489@2
  - `Atom.Relations.contained_by` — CA-R-2490@2
  - `Atom.Relations.contained_by.atom` — CA-R-2491@2
  - `Atom.Relations.contained_by.scope_unit` — CA-R-2492@2
  - `Atom.ID` — CA-R-2493@2
  - `Atom.Role` — CA-R-2494@2
  - `Atom.Form` — CA-R-2495@2
  - `Atom.Version` — CA-R-2496@2
  - `Atom.Label` — CA-R-2497@2
  - `Atom.Content` — CA-R-2498@2
  - `Atom.Content.Summary` — CA-R-2499@2
  - `Atom.Content.Claim` — CA-R-2500@2
  - `Atom.Content.Claim Scope` — CA-R-2501@2
  - `Atom.Content.Semantics` — CA-R-2502@2
  - `Atom.Content.Details` — CA-R-2503@2
  - `Atom.Tier` — CA-R-2504@2
  - `Atom.Tier.Label` — CA-R-2505@2
  - `Atom.Subjects.Passive` — CA-R-2506@2
  - `Atom.Relations` — CA-R-2507@2
  - `Atom.Subjects` — CA-R-2545@2
  - `Atom.Subjects.Active` — CA-R-2546@2
- Declaration source: `CA-R-2510@2`
  - Semantics:
    An Analysis establishes a finding, explanation, comparison, or rationale.
  - Fenced Claim block:
```CFEL
Atom/(.Role: Analysis)
```
  - Unresolved CFEL: `Atom/(.Role: Analysis)`
- Shared RMED source: `CA-R-1648@31`
  - Remaining Claim prose:
    an external review **must** be imported as an External Analysis Report Atom whose governed envelope identifies its source, provenance, reviewed scope, original body, **and** native attachments **without** requiring a provider-specific finding schema. one internal Analysis derives from that Atom, records the project's finding-level interpretation **and** dispositions, **and** becomes the **only** Analysis source from which project-owned Concern, Plan, Requirement, Method, Evaluation, **or** Delivery Atoms are derived. **every** accepted disposition that changes project meaning **or** work is materialized **in** its owning CAPRMEDIO Content Role; rejected **or** non-actionable findings remain **only** **in** the internal Analysis.
- Shared RMED source: `CA-R-1725@26`
  - Remaining Claim prose:
    **every** admitted external Analysis is reviewed by one internal Analysis **before** it can produce project-owned Concern, Plan, Requirement, Method, Evaluation, **or** Delivery Atoms. the external Analysis remains authoritative **only** for what its external source reported; the internal Analysis owns the project's interpretation **and** dispositions, **and** **every** resulting Atom owns its independently accepted meaning.

### `Atom/(.Role:=Concern)` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Atom` — CA-R-2508@2
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Inherited Property Declaration refs; no child Property Node is created:
  - `Atom.Status` — CA-R-2488@2
  - `Atom.Updated At` — CA-R-2489@2
  - `Atom.Relations.contained_by` — CA-R-2490@2
  - `Atom.Relations.contained_by.atom` — CA-R-2491@2
  - `Atom.Relations.contained_by.scope_unit` — CA-R-2492@2
  - `Atom.ID` — CA-R-2493@2
  - `Atom.Role` — CA-R-2494@2
  - `Atom.Form` — CA-R-2495@2
  - `Atom.Version` — CA-R-2496@2
  - `Atom.Label` — CA-R-2497@2
  - `Atom.Content` — CA-R-2498@2
  - `Atom.Content.Summary` — CA-R-2499@2
  - `Atom.Content.Claim` — CA-R-2500@2
  - `Atom.Content.Claim Scope` — CA-R-2501@2
  - `Atom.Content.Semantics` — CA-R-2502@2
  - `Atom.Content.Details` — CA-R-2503@2
  - `Atom.Tier` — CA-R-2504@2
  - `Atom.Tier.Label` — CA-R-2505@2
  - `Atom.Subjects.Passive` — CA-R-2506@2
  - `Atom.Relations` — CA-R-2507@2
  - `Atom.Subjects` — CA-R-2545@2
  - `Atom.Subjects.Active` — CA-R-2546@2
- Declaration source: `CA-R-2509@2`
  - Semantics:
    A Concern identifies a question, conflict, or problem.
  - Fenced Claim block:
```CFEL
Atom/(.Role: Concern)
```
  - Unresolved CFEL: `Atom/(.Role: Concern)`
- Shared RMED source: `CA-R-635@24`
  - Remaining Claim prose:
    a material Concern **may** be considered solved **only** **when** its analyzed cause is corrected **and** its recurrence risk is governed.

### `Atom/(.Role:=Delivery)` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Atom` — CA-R-2508@2
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Inherited Property Declaration refs; no child Property Node is created:
  - `Atom.Status` — CA-R-2488@2
  - `Atom.Updated At` — CA-R-2489@2
  - `Atom.Relations.contained_by` — CA-R-2490@2
  - `Atom.Relations.contained_by.atom` — CA-R-2491@2
  - `Atom.Relations.contained_by.scope_unit` — CA-R-2492@2
  - `Atom.ID` — CA-R-2493@2
  - `Atom.Role` — CA-R-2494@2
  - `Atom.Form` — CA-R-2495@2
  - `Atom.Version` — CA-R-2496@2
  - `Atom.Label` — CA-R-2497@2
  - `Atom.Content` — CA-R-2498@2
  - `Atom.Content.Summary` — CA-R-2499@2
  - `Atom.Content.Claim` — CA-R-2500@2
  - `Atom.Content.Claim Scope` — CA-R-2501@2
  - `Atom.Content.Semantics` — CA-R-2502@2
  - `Atom.Content.Details` — CA-R-2503@2
  - `Atom.Tier` — CA-R-2504@2
  - `Atom.Tier.Label` — CA-R-2505@2
  - `Atom.Subjects.Passive` — CA-R-2506@2
  - `Atom.Relations` — CA-R-2507@2
  - `Atom.Subjects` — CA-R-2545@2
  - `Atom.Subjects.Active` — CA-R-2546@2
- Declaration source: `CA-R-2515@2`
  - Semantics:
    A Delivery specifies how something is represented, stored, or placed in a Carrier.
  - Fenced Claim block:
```CFEL
Atom/(.Role: Delivery)
```
  - Unresolved CFEL: `Atom/(.Role: Delivery)`

### `Atom/(.Role:=Evaluation)` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Atom` — CA-R-2508@2
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Inherited Property Declaration refs; no child Property Node is created:
  - `Atom.Status` — CA-R-2488@2
  - `Atom.Updated At` — CA-R-2489@2
  - `Atom.Relations.contained_by` — CA-R-2490@2
  - `Atom.Relations.contained_by.atom` — CA-R-2491@2
  - `Atom.Relations.contained_by.scope_unit` — CA-R-2492@2
  - `Atom.ID` — CA-R-2493@2
  - `Atom.Role` — CA-R-2494@2
  - `Atom.Form` — CA-R-2495@2
  - `Atom.Version` — CA-R-2496@2
  - `Atom.Label` — CA-R-2497@2
  - `Atom.Content` — CA-R-2498@2
  - `Atom.Content.Summary` — CA-R-2499@2
  - `Atom.Content.Claim` — CA-R-2500@2
  - `Atom.Content.Claim Scope` — CA-R-2501@2
  - `Atom.Content.Semantics` — CA-R-2502@2
  - `Atom.Content.Details` — CA-R-2503@2
  - `Atom.Tier` — CA-R-2504@2
  - `Atom.Tier.Label` — CA-R-2505@2
  - `Atom.Subjects.Passive` — CA-R-2506@2
  - `Atom.Relations` — CA-R-2507@2
  - `Atom.Subjects` — CA-R-2545@2
  - `Atom.Subjects.Active` — CA-R-2546@2
- Declaration source: `CA-R-2514@2`
  - Semantics:
    An Evaluation establishes a falsifiable check, acceptance criterion, or disposition rule.
  - Fenced Claim block:
```CFEL
Atom/(.Role: Evaluation)
```
  - Unresolved CFEL: `Atom/(.Role: Evaluation)`
- Shared RMED source: `CA-R-1503@21`
  - Remaining Claim prose:
    an Evaluation Atom **must** define the checked Claim, applicable conditions, acceptance criteria, **and** disposition rule **without** prescribing the mechanism that realizes its check.
- Shared RMED source: `CA-R-1505@25`
  - Remaining Claim prose:
    an Evaluation Atom's realization chains **must** remain distinct between deterministic test implementations **and** qualitative, probabilistic, statistical, rubric-based, **or** model-judged evaluation implementations.
    
    **every** chain **must** keep these contributions distinguishable:
    
    - its executable Implementation;
    - its configuration **or** rubric;
    - its factual execution result;
    - its Evidence;
    - its Verification judgment.
- Shared RMED source: `CA-R-1741@29`
  - Remaining Claim prose:
    **every** concrete recurrence protection **must** be represented by an Evaluation Atom that defines one mechanism-neutral bounded check for the corrected failure class.
- Shared RMED source: `CA-M-264@27`
  - Remaining Claim prose:
    **to** write **or** maintain an Evaluation, identify its checked authority **and** Scope, select a suitable test technique, specify recoverable inputs, procedure, **and** observable falsifying conditions, **and** preserve the distinction between foundational evaluation authority, independent shared evaluation criteria **where** they are independently governed, **and** concrete evaluation criteria; keep writing techniques, test frameworks, **and** authoring conventions **in** Method authority rather than treating them as test results.
- Shared RMED source: `CA-M-265@26`
  - Remaining Claim prose:
    **to** derive Er, Em, **and** Ed groups, resolve the Content Role of **every** `evaluation_for` target **and** include the Evaluation **in** the corresponding Requirement, Method, **or** Delivery group; **if** targets span multiple roles, **then** include it **in** **every** applicable group **without** assigning a new Content Role **or** persisting a duplicate target-role field. absence of individual targets on a Core **or** General Evaluation policy admitted by CA-R-1018-CORE_META_MODEL-CORE-REQUIREMENT--register-evaluation-targets **must not** require an invented classification.
- Shared RMED source: `CA-R-1518@23`
  - Remaining Claim prose:
    **in** the CAPRMEDIO Project, Evaluation responsibility for operational definitions **and** their Tool implementations **must** follow this allocation:

### `Atom/(.Role:=Method)` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Atom` — CA-R-2508@2
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Inherited Property Declaration refs; no child Property Node is created:
  - `Atom.Status` — CA-R-2488@2
  - `Atom.Updated At` — CA-R-2489@2
  - `Atom.Relations.contained_by` — CA-R-2490@2
  - `Atom.Relations.contained_by.atom` — CA-R-2491@2
  - `Atom.Relations.contained_by.scope_unit` — CA-R-2492@2
  - `Atom.ID` — CA-R-2493@2
  - `Atom.Role` — CA-R-2494@2
  - `Atom.Form` — CA-R-2495@2
  - `Atom.Version` — CA-R-2496@2
  - `Atom.Label` — CA-R-2497@2
  - `Atom.Content` — CA-R-2498@2
  - `Atom.Content.Summary` — CA-R-2499@2
  - `Atom.Content.Claim` — CA-R-2500@2
  - `Atom.Content.Claim Scope` — CA-R-2501@2
  - `Atom.Content.Semantics` — CA-R-2502@2
  - `Atom.Content.Details` — CA-R-2503@2
  - `Atom.Tier` — CA-R-2504@2
  - `Atom.Tier.Label` — CA-R-2505@2
  - `Atom.Subjects.Passive` — CA-R-2506@2
  - `Atom.Relations` — CA-R-2507@2
  - `Atom.Subjects` — CA-R-2545@2
  - `Atom.Subjects.Active` — CA-R-2546@2
- Declaration source: `CA-R-2513@2`
  - Semantics:
    A Method states how to achieve an outcome.
  - Fenced Claim block:
```CFEL
Atom/(.Role: Method)
```
  - Unresolved CFEL: `Atom/(.Role: Method)`
- Shared RMED source: `CA-R-1767@34`
  - Remaining Claim prose:
    A Method Eng Policy governs reusable engineering policy and an Eng Decision selects a bounded engineering approach. A Delivery Policy governs a reusable representation or delivery family, while a Delivery Decision selects a bounded representation or delivery choice. **neither** Eng Policy **nor** Eng Decision is an execution Plan **or** native Implementation.
- Shared RMED source: `CA-R-1768@29`
  - Remaining Claim prose:
    an Eng Decision **may** be archived as absorbed **only** **after** **`>=1`** active Eng Policies preserve **every** part of its still-necessary governed meaning for the affected realization scope.

### `Atom/(.Role:=Operations)` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Atom` — CA-R-2508@2
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Inherited Property Declaration refs; no child Property Node is created:
  - `Atom.Status` — CA-R-2488@2
  - `Atom.Updated At` — CA-R-2489@2
  - `Atom.Relations.contained_by` — CA-R-2490@2
  - `Atom.Relations.contained_by.atom` — CA-R-2491@2
  - `Atom.Relations.contained_by.scope_unit` — CA-R-2492@2
  - `Atom.ID` — CA-R-2493@2
  - `Atom.Role` — CA-R-2494@2
  - `Atom.Form` — CA-R-2495@2
  - `Atom.Version` — CA-R-2496@2
  - `Atom.Label` — CA-R-2497@2
  - `Atom.Content` — CA-R-2498@2
  - `Atom.Content.Summary` — CA-R-2499@2
  - `Atom.Content.Claim` — CA-R-2500@2
  - `Atom.Content.Claim Scope` — CA-R-2501@2
  - `Atom.Content.Semantics` — CA-R-2502@2
  - `Atom.Content.Details` — CA-R-2503@2
  - `Atom.Tier` — CA-R-2504@2
  - `Atom.Tier.Label` — CA-R-2505@2
  - `Atom.Subjects.Passive` — CA-R-2506@2
  - `Atom.Relations` — CA-R-2507@2
  - `Atom.Subjects` — CA-R-2545@2
  - `Atom.Subjects.Active` — CA-R-2546@2
- Declaration source: `CA-R-2463@2`
  - Semantics:
    An Operations Atom defines reusable work. It can define an Action, a Workflow, a Step, or a Substep.
  - Fenced Claim block:
```CFEL
Atom/(.Role: Operations)
```
  - Unresolved CFEL: `Atom/(.Role: Operations)`
- Shared RMED source: `CA-R-1729@26`
  - Remaining Claim prose:
    an Operations Atom lifecycle **must** govern admission **and** currency of its reusable operational behavior **or** Actor participation/authorization policy. historical execution facts **and** Journal Records remain preserved history regardless of whether that Operations Atom is Draft, Active, **or** Archived, **or** whether an operational response is complete.
- Shared RMED source: `CA-R-1515@23`
  - Remaining Claim prose:
    **in** the caprmedio Project, the canonical O definitions of Actions **and** Workflows used by TOOLS **must** belong **to** methodology source Scope Units.

### `Atom/(.Role:=Operations)/Action` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Atom/(.Role:=Operations)` — CA-R-2463@2
  - `Atom` — CA-R-2508@2
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Inherited Property Declaration refs; no child Property Node is created:
  - `Atom.Status` — CA-R-2488@2
  - `Atom.Updated At` — CA-R-2489@2
  - `Atom.Relations.contained_by` — CA-R-2490@2
  - `Atom.Relations.contained_by.atom` — CA-R-2491@2
  - `Atom.Relations.contained_by.scope_unit` — CA-R-2492@2
  - `Atom.ID` — CA-R-2493@2
  - `Atom.Role` — CA-R-2494@2
  - `Atom.Form` — CA-R-2495@2
  - `Atom.Version` — CA-R-2496@2
  - `Atom.Label` — CA-R-2497@2
  - `Atom.Content` — CA-R-2498@2
  - `Atom.Content.Summary` — CA-R-2499@2
  - `Atom.Content.Claim` — CA-R-2500@2
  - `Atom.Content.Claim Scope` — CA-R-2501@2
  - `Atom.Content.Semantics` — CA-R-2502@2
  - `Atom.Content.Details` — CA-R-2503@2
  - `Atom.Tier` — CA-R-2504@2
  - `Atom.Tier.Label` — CA-R-2505@2
  - `Atom.Subjects.Passive` — CA-R-2506@2
  - `Atom.Relations` — CA-R-2507@2
  - `Atom.Subjects` — CA-R-2545@2
  - `Atom.Subjects.Active` — CA-R-2546@2
- Declaration source: `CA-R-2467@2`
  - Semantics:
    An Action is a reusable operational building block. Its boundary reflects one modeled responsibility.
  - Fenced Claim block:
```CFEL
Atom/(.Role: Operations)/Action;
Action//{:0+}((IS_RUN_BY)) (in (Step, Substep))//
```
  - Allowed Relations and other formal clauses:
    - `Action//` — IS_RUN_BY → `(in (Step, Substep))//`; Host=0+; Target=undefined
  - Unresolved CFEL: `Atom/(.Role: Operations)/Action`

### `Atom/(.Role:=Operations)/Step` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Atom/(.Role:=Operations)` — CA-R-2463@2
  - `Atom` — CA-R-2508@2
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Inherited Property Declaration refs; no child Property Node is created:
  - `Atom.Status` — CA-R-2488@2
  - `Atom.Updated At` — CA-R-2489@2
  - `Atom.Relations.contained_by` — CA-R-2490@2
  - `Atom.Relations.contained_by.atom` — CA-R-2491@2
  - `Atom.Relations.contained_by.scope_unit` — CA-R-2492@2
  - `Atom.ID` — CA-R-2493@2
  - `Atom.Role` — CA-R-2494@2
  - `Atom.Form` — CA-R-2495@2
  - `Atom.Version` — CA-R-2496@2
  - `Atom.Label` — CA-R-2497@2
  - `Atom.Content` — CA-R-2498@2
  - `Atom.Content.Summary` — CA-R-2499@2
  - `Atom.Content.Claim` — CA-R-2500@2
  - `Atom.Content.Claim Scope` — CA-R-2501@2
  - `Atom.Content.Semantics` — CA-R-2502@2
  - `Atom.Content.Details` — CA-R-2503@2
  - `Atom.Tier` — CA-R-2504@2
  - `Atom.Tier.Label` — CA-R-2505@2
  - `Atom.Subjects.Passive` — CA-R-2506@2
  - `Atom.Relations` — CA-R-2507@2
  - `Atom.Subjects` — CA-R-2545@2
  - `Atom.Subjects.Active` — CA-R-2546@2
- Declaration source: `CA-R-2465@2`
  - Semantics:
    A Step is a unit of work within a Workflow. It runs an Action or contains Substeps.
  - Fenced Claim block:
```CFEL
Atom/(.Role: Operations)/Step;
Step//{:1}((IS_CONTAINED_BY)) Workflow//;
((Step//{:1+}((CONTAINS)) Substep//)
AND (Step//{:0}((RUN)) Action//))
OR
((Step//{:0}((CONTAINS)) Substep//)
AND (Step//{:1}((RUN)) Action//))
```
  - Allowed Relations and other formal clauses:
    - `Step//` — IS_CONTAINED_BY → `Workflow//`; Host=1; Target=undefined
  - Unresolved CFEL: `Atom/(.Role: Operations)/Step`
  - Unresolved CFEL: `((Step//{:1+}((CONTAINS)) Substep//)
AND (Step//{:0}((RUN)) Action//))
OR
((Step//{:0}((CONTAINS)) Substep//)
AND (Step//{:1}((RUN)) Action//))`

### `Atom/(.Role:=Operations)/Substep` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Atom/(.Role:=Operations)` — CA-R-2463@2
  - `Atom` — CA-R-2508@2
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Inherited Property Declaration refs; no child Property Node is created:
  - `Atom.Status` — CA-R-2488@2
  - `Atom.Updated At` — CA-R-2489@2
  - `Atom.Relations.contained_by` — CA-R-2490@2
  - `Atom.Relations.contained_by.atom` — CA-R-2491@2
  - `Atom.Relations.contained_by.scope_unit` — CA-R-2492@2
  - `Atom.ID` — CA-R-2493@2
  - `Atom.Role` — CA-R-2494@2
  - `Atom.Form` — CA-R-2495@2
  - `Atom.Version` — CA-R-2496@2
  - `Atom.Label` — CA-R-2497@2
  - `Atom.Content` — CA-R-2498@2
  - `Atom.Content.Summary` — CA-R-2499@2
  - `Atom.Content.Claim` — CA-R-2500@2
  - `Atom.Content.Claim Scope` — CA-R-2501@2
  - `Atom.Content.Semantics` — CA-R-2502@2
  - `Atom.Content.Details` — CA-R-2503@2
  - `Atom.Tier` — CA-R-2504@2
  - `Atom.Tier.Label` — CA-R-2505@2
  - `Atom.Subjects.Passive` — CA-R-2506@2
  - `Atom.Relations` — CA-R-2507@2
  - `Atom.Subjects` — CA-R-2545@2
  - `Atom.Subjects.Active` — CA-R-2546@2
- Declaration source: `CA-R-2466@2`
  - Semantics:
    A Substep is a leaf unit within a Step. It runs a reusable Action.
  - Fenced Claim block:
```CFEL
Atom/(.Role: Operations)/Substep;
Substep//{:1}((IS_CONTAINED_BY)) Step//;
Substep//{:1}((RUN)) Action//
```
  - Allowed Relations and other formal clauses:
    - `Substep//` — IS_CONTAINED_BY → `Step//`; Host=1; Target=undefined
    - `Substep//` — RUN → `Action//`; Host=1; Target=undefined
  - Unresolved CFEL: `Atom/(.Role: Operations)/Substep`

### `Atom/(.Role:=Operations)/Workflow` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Atom/(.Role:=Operations)` — CA-R-2463@2
  - `Atom` — CA-R-2508@2
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Inherited Property Declaration refs; no child Property Node is created:
  - `Atom.Status` — CA-R-2488@2
  - `Atom.Updated At` — CA-R-2489@2
  - `Atom.Relations.contained_by` — CA-R-2490@2
  - `Atom.Relations.contained_by.atom` — CA-R-2491@2
  - `Atom.Relations.contained_by.scope_unit` — CA-R-2492@2
  - `Atom.ID` — CA-R-2493@2
  - `Atom.Role` — CA-R-2494@2
  - `Atom.Form` — CA-R-2495@2
  - `Atom.Version` — CA-R-2496@2
  - `Atom.Label` — CA-R-2497@2
  - `Atom.Content` — CA-R-2498@2
  - `Atom.Content.Summary` — CA-R-2499@2
  - `Atom.Content.Claim` — CA-R-2500@2
  - `Atom.Content.Claim Scope` — CA-R-2501@2
  - `Atom.Content.Semantics` — CA-R-2502@2
  - `Atom.Content.Details` — CA-R-2503@2
  - `Atom.Tier` — CA-R-2504@2
  - `Atom.Tier.Label` — CA-R-2505@2
  - `Atom.Subjects.Passive` — CA-R-2506@2
  - `Atom.Relations` — CA-R-2507@2
  - `Atom.Subjects` — CA-R-2545@2
  - `Atom.Subjects.Active` — CA-R-2546@2
- Declaration source: `CA-R-2464@2`
  - Semantics:
    A Workflow defines a graph of Steps for governed work.
  - Fenced Claim block:
```CFEL
Atom/(.Role: Operations)/Workflow;
Workflow//{:1+}((CONTAINS)) Step//
```
  - Allowed Relations and other formal clauses:
    - `Workflow//` — CONTAINS → `Step//`; Host=1+; Target=undefined
  - Unresolved CFEL: `Atom/(.Role: Operations)/Workflow`
- Shared RMED source: `CA-R-2565@2`
  - Remaining Claim prose:
    When a Workflow archives an Atom:
    
    1. Keep Atom.Version unchanged.
    2. Keep Atom.Updated At unchanged.
    3. Do not create a new Atom Version solely for archiving.

### `Atom/(.Role:=Plan)` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Atom` — CA-R-2508@2
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Inherited Property Declaration refs; no child Property Node is created:
  - `Atom.Status` — CA-R-2488@2
  - `Atom.Updated At` — CA-R-2489@2
  - `Atom.Relations.contained_by` — CA-R-2490@2
  - `Atom.Relations.contained_by.atom` — CA-R-2491@2
  - `Atom.Relations.contained_by.scope_unit` — CA-R-2492@2
  - `Atom.ID` — CA-R-2493@2
  - `Atom.Role` — CA-R-2494@2
  - `Atom.Form` — CA-R-2495@2
  - `Atom.Version` — CA-R-2496@2
  - `Atom.Label` — CA-R-2497@2
  - `Atom.Content` — CA-R-2498@2
  - `Atom.Content.Summary` — CA-R-2499@2
  - `Atom.Content.Claim` — CA-R-2500@2
  - `Atom.Content.Claim Scope` — CA-R-2501@2
  - `Atom.Content.Semantics` — CA-R-2502@2
  - `Atom.Content.Details` — CA-R-2503@2
  - `Atom.Tier` — CA-R-2504@2
  - `Atom.Tier.Label` — CA-R-2505@2
  - `Atom.Subjects.Passive` — CA-R-2506@2
  - `Atom.Relations` — CA-R-2507@2
  - `Atom.Subjects` — CA-R-2545@2
  - `Atom.Subjects.Active` — CA-R-2546@2
- Declaration source: `CA-R-2511@2`
  - Semantics:
    A Plan describes bounded intended work or an intended outcome.
  - Fenced Claim block:
```CFEL
Atom/(.Role: Plan);
IF ((Atom/(.Role: Plan).Status = Active) AND (Atom/(.Role: Plan).Work Sequence Number{=1}))
THEN (Atom/(.Role: Plan).Relations.contained_by{==1})
```
  - Unresolved CFEL: `Atom/(.Role: Plan)`
  - Unresolved CFEL: `IF ((Atom/(.Role: Plan).Status = Active) AND (Atom/(.Role: Plan).Work Sequence Number{=1}))
THEN (Atom/(.Role: Plan).Relations.contained_by{==1})`
- Shared RMED source: `CA-R-1534@22`
  - Remaining Claim prose:
    adding, removing, reordering, **or** changing a decomposed Plan Atom **must not** establish **or** replace the Hub Atom's identity; **every** related Atom retains its independent Claim **and** lifecycle.
- Shared RMED source: `CA-R-1542@23`
  - Remaining Claim prose:
    the Plan Backlog **means** Plan Atoms retained for future work outside the current Plan Scope, including standalone Plans **and** Plans with decomposition; a Version Label does **not** establish another Status.
- Shared RMED source: `CA-R-1575@25`
  - Remaining Claim prose:
    **every** Plan Atom **must** have **`>=1`** of:
    
    - its own work content;
    - **`>0`** outgoing derived `CONTAINS` links **to** directly contained Plan Atoms.
    
    both contributions **may** be present within the same Claim; a Summary alone **without** either contribution is insufficient.
- Shared RMED source: `CA-R-1589@24`
  - Remaining Claim prose:
    **every** executable Plan with **none** directly contained Plan Atoms **must** bound its own work **to** an estimate of **<=15** minutes for **=1** assigned AI Agent, with sufficient inputs, required output, verification, **and** no unresolved Operator decision; a Plan with contained children **may** have a larger roll-up estimate. the rule applies independently of Label.
- Shared RMED source: `CA-R-1590@22`
  - Remaining Claim prose:
    a Plan Atom **may** exist **without** an `IS_CONTAINED_BY` connection to a containing Plan; its Label **must not** require a containing Plan.
- Shared RMED source: `CA-R-1592@23`
  - Remaining Claim prose:
    Plan execution **must not** contain a cycle of completion prerequisites, including one formed jointly by `BLOCKS` **and** the requirement **to** complete directly contained Plan work **before** its containing Plan can be Done **or** Canceled.
- Shared RMED source: `CA-R-1691@30`
  - Remaining Claim prose:
    assigning a Development Backlog candidate **to** a current **or** future version does **not** establish governed truth. the candidate becomes active work **only** **when** the operator selects it **and** CAPRMEDIO creates **`=1`** bounded Task Atom for its action. execution **then** materializes the minimum Requirement, Method, Evaluation, Delivery, **or** future Operations Atoms needed **to** govern that work.
    
    **`=1`** backlog line **may** produce multiple Atoms. multiple closely related backlog lines **may** produce **`=1`** Concern **or** RMED Atom **only** **when** they resolve **to** **`=1`** independently replaceable claim. Analysis, Task, Implementation, **and** Operations use their separately governed atomicity models.
    
    the backlog entry **may** link the resulting Atoms for navigation but remains a non-authoritative planning candidate **until** release finalization removes **or** reschedules it.
- Shared RMED source: `CA-R-1714@27`
  - Remaining Claim prose:
    an operative plan is ephemeral session control; a Plan is a persisted CAPRMEDIO artifact created **only** by governed entry criteria.
- Shared RMED source: `CA-R-1715@27`
  - Remaining Claim prose:
    still-valid operative actions left unfinished by deferral, blocking, topic change, compaction, session end, **or** partial completion **must** be reconciled into the applicable governed Plan.
- Shared RMED source: `CA-M-123@29`
  - Remaining Claim prose:
    **to** write one Definition of Done, the Author **must** perform **all** of:
    
    1. begin the falsification condition expression with: the Plan is **not** Done **if**.
    2. make **every** atomic condition observable **and** decidable.
    3. enclose **every** composite condition **and** **every** function argument **in** explicit parentheses.
    4. evaluate the condition expression according **to** CA-M-122-CORE_META_MODEL-IMPLEMENTATION_METHOD--evaluate-condition-expressions.
- Shared RMED source: `CA-E-504@22`
  - Remaining Claim prose:
    the blocking Evaluation **must** reject a start **unless** **all** explicit blockers are Done **and** the applicable execution permissions hold.
- Shared RMED source: `CA-D-460@25`
  - Remaining Claim prose:
    a Plan Atom Carrier Bundle **must** consist of **`=1`** Markdown File Carrier **and** **`<=1`** optional matching Directory Carrier using the same canonical stem under CA-D-469-CORE_META_MODEL-DELIVERY--serialize-plan-carrier-stems.
    
    - the Markdown file carries the Plan's own Properties **and** follows CA-D-470-CORE_META_MODEL-DELIVERY--serialize-plan-file-sections, including its mandatory Definition of Done.
    - a matching directory organizes related Plan Carriers; it neither creates another Atom **nor** replaces the mandatory Markdown file.
    - the file **and** optional directory represent the same identity, Summary, Label, **and** Status, checked under CA-D-480-CORE_META_MODEL-DELIVERY--keep-atom-addresses-consistent-with-carried-properties.
    - related Plan files carry independent Atoms; they are **not** additional Carriers of the Hub's Claim.
- Shared RMED source: `CA-D-470@29`
  - Remaining Claim prose:
    **every** Plan Markdown File Carrier **must** contain YAML Frontmatter followed by the Plan layout registered **in** CA-D-479-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties:
    
    1. `# Summary` carries the Summary value.
    2. `## Objective` carries the intended work **or** outcome Claim, including its applicability restrictions.
    3. `## Details` carries supporting information **and** **`=1`** nested `### Definition of Done` section with the Plan's falsifying Condition Expression.
    
    the Definition of Done is the Plan's existing Property, **not** a second completion Claim **or** an optional detail. carry its value **only** **in** that nested section. **any** other supporting Details **must** stay within the Objective. use CA-D-479-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties for section boundaries; do **not** duplicate these Properties **in** frontmatter **or** add a separate Scope section duplicating restrictions **in** the Objective. a Hub uses this same mandatory file, **not** an additional Objective Atom.
- Shared RMED source: `CA-R-1711@31`
  - Remaining Claim prose:
    the caprmedio Project **must** classify the Development Backlog as an Epic whose direct Task members are accepted intended actions that have no narrower Epic.

### `Atom/(.Role:=Requirement)` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Atom` — CA-R-2508@2
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Inherited Property Declaration refs; no child Property Node is created:
  - `Atom.Status` — CA-R-2488@2
  - `Atom.Updated At` — CA-R-2489@2
  - `Atom.Relations.contained_by` — CA-R-2490@2
  - `Atom.Relations.contained_by.atom` — CA-R-2491@2
  - `Atom.Relations.contained_by.scope_unit` — CA-R-2492@2
  - `Atom.ID` — CA-R-2493@2
  - `Atom.Role` — CA-R-2494@2
  - `Atom.Form` — CA-R-2495@2
  - `Atom.Version` — CA-R-2496@2
  - `Atom.Label` — CA-R-2497@2
  - `Atom.Content` — CA-R-2498@2
  - `Atom.Content.Summary` — CA-R-2499@2
  - `Atom.Content.Claim` — CA-R-2500@2
  - `Atom.Content.Claim Scope` — CA-R-2501@2
  - `Atom.Content.Semantics` — CA-R-2502@2
  - `Atom.Content.Details` — CA-R-2503@2
  - `Atom.Tier` — CA-R-2504@2
  - `Atom.Tier.Label` — CA-R-2505@2
  - `Atom.Subjects.Passive` — CA-R-2506@2
  - `Atom.Relations` — CA-R-2507@2
  - `Atom.Subjects` — CA-R-2545@2
  - `Atom.Subjects.Active` — CA-R-2546@2
- Declaration source: `CA-R-2512@2`
  - Semantics:
    A Requirement states a required outcome or behavior, or defines a governed model and its constraints.
  - Fenced Claim block:
```CFEL
Atom/(.Role: Requirement)
```
  - Unresolved CFEL: `Atom/(.Role: Requirement)`
- Shared RMED source: `CA-R-024@27`
  - Remaining Claim prose:
    CAPRMEDIO **must** resolve conflicts among active Requirements other than Requirements expressing Project-wide foundational invariants through explicit rules determined by their applicability tiers rather than presentation order, Concern priority, **or** implicit interpretation.
- Shared RMED source: `CA-E-434@24`
  - Remaining Claim prose:
    **when** an accepted Requirement is used **to** govern work **or** evaluate a result, its checkability Evaluation **must** return `pass` **if** the available evidence identifies **all** of the following:
    
    - recoverable inputs for checking the Requirement;
    - a recoverable check procedure;
    - a recoverable interpretation that yields **=1** result **in** (`pass`, `fail`).
    
    **if** **any** of these conditions is missing, the checkability Evaluation **must** return `fail`. satisfying them does **not** require a separate Evaluation Atom **unless** applicable authority requires that Atom for the particular case under CAPRMEDIO-META-REQU-124; an independently governed Evaluation Claim still follows the Atom boundary rules.
- Shared RMED source: `CA-R-1694@41`
  - Remaining Claim prose:
    **every** Requirement **must** state its required outcome, obligation, permission, prohibition, **or** accepted external boundary **without** prescribing internal code **or** code organization merely as a construction choice.
    
    - an accepted external interface, protocol, data shape, **or** host obligation **may** be required **when** conformance **to** that boundary is itself the required outcome. this does **not** prescribe an **otherwise** interchangeable internal realization.
    - a programming language, library, algorithm, function, class, module, source-file organization, **or** another construction technique does **not** become a Requirement solely because it is normative; classify its primary contribution under CA-R-1531@20 **and** CA-R-2513.
    - packaging, release, deployment, distribution, installation, migration, upgrade, **and** rollback are topics, **not** Content Role selectors. classify a Carrier representation **or** placement under CA-R-2515, reusable Action **or** Workflow behavior under CA-R-2463, **and** treat an actual realization as native Implementation rather than an Atom Content Role. mentioning one of those topics does **not** turn a procedure into Delivery authority.
    - a candidate that combines this independently replaceable outcome with an independently replaceable construction, Carrier, **or** operational Claim requires separate Atoms under the one-Claim authority; a composite Claim is **not** split merely because it has multiple clauses.
- Shared RMED source: `CA-R-1707@31`
  - Remaining Claim prose:
    **every** governed development change that proceeds toward realization has **`>=1`** Requirement Atom, **and**, among Requirement, Method, Evaluation, **and** Delivery, Requirement is the **only** mandatory Content Role; Method, Evaluation, **and** Delivery Atoms are optional **unless** applicable authority requires them for the particular case.

### `Atom/(.Role:=Requirement)/(.Form:=Declaration)` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Atom/(.Role:=Requirement)` — CA-R-2512@2
  - `Atom` — CA-R-2508@2
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Inherited Property Declaration refs; no child Property Node is created:
  - `Atom.Status` — CA-R-2488@2
  - `Atom.Updated At` — CA-R-2489@2
  - `Atom.Relations.contained_by` — CA-R-2490@2
  - `Atom.Relations.contained_by.atom` — CA-R-2491@2
  - `Atom.Relations.contained_by.scope_unit` — CA-R-2492@2
  - `Atom.ID` — CA-R-2493@2
  - `Atom.Role` — CA-R-2494@2
  - `Atom.Form` — CA-R-2495@2
  - `Atom.Version` — CA-R-2496@2
  - `Atom.Label` — CA-R-2497@2
  - `Atom.Content` — CA-R-2498@2
  - `Atom.Content.Summary` — CA-R-2499@2
  - `Atom.Content.Claim` — CA-R-2500@2
  - `Atom.Content.Claim Scope` — CA-R-2501@2
  - `Atom.Content.Semantics` — CA-R-2502@2
  - `Atom.Content.Details` — CA-R-2503@2
  - `Atom.Tier` — CA-R-2504@2
  - `Atom.Tier.Label` — CA-R-2505@2
  - `Atom.Subjects.Passive` — CA-R-2506@2
  - `Atom.Relations` — CA-R-2507@2
  - `Atom.Subjects` — CA-R-2545@2
  - `Atom.Subjects.Active` — CA-R-2546@2
- Declaration source: `CA-R-2516@2`
  - Semantics:
    A Declaration states a Node’s structure and applicable constraints.
  - Fenced Claim block:
```CFEL
Atom/(.Role: Requirement)/(.Form: Declaration)
```
  - Unresolved CFEL: `Atom/(.Role: Requirement)/(.Form: Declaration)`
- Shared RMED source: `CA-R-2481@2`
  - Remaining Claim prose:
    The proposed Atom schema **must** distinguish Role from Form. The current Atom `content_role` field maps to the proposed `role` value, and the current `type` field maps to the proposed `form` value. A Declaration Atom has `role: Requirement` and `form: Declaration`; Declaration is a Form under the Requirement Role, not a new Role value. In Subject addresses, express that pair as `Atom/(.Role := Requirement)/(.Form := Declaration)`. Use `Form` for the form qualifier in place of a legacy nested `Role: X` or `Type: X` qualifier.
    
    Role identifies the contribution. Form identifies its authoring form and does not override or duplicate Role.
- Shared RMED source: `CA-R-2482@2`
  - Remaining Claim prose:
    - A formal Scope Declaration is contained outside the Scope Unit it constrains.
    - It states permitted active and passive Subjects, Relations, endpoints and cardinalities.
    - Its Subjects resolve in the applicable MODEL and PROJECT STRUCTURE instances.
    - A Target Scope does not widen its granted permissions.
    - The Declaration does not establish runtime behavior.
- Shared RMED source: `CA-D-662@2`
  - Remaining Claim prose:
    Node Declaration carriers require role, form and subjects.active. Encode passive Subjects as subjects.passive when present. Omit the author field.
    - Active and Passive Subjects are authored sets.
    - Derive HAS_ACTIVE_SUBJECT from subjects.active. Do not store it twice.
    - Store authored instance references under relations.
    - The containment reference key is its target kind: atom or scope_unit. The referenced target must match that kind.
    - contained_by encodes IS_CONTAINED_BY; CONTAINS is derived.
    - Relation links do not duplicate Subject membership.
  - Fenced Claim block:
```CFEL
Atom.Role >> @Carrier//Markdown file.frontmatter.role;
Atom.Form >> @Carrier//Markdown file.frontmatter.form;
Atom.Subjects.Active >> @Carrier//Markdown file.frontmatter.subjects.active;
Atom.Subjects.Passive >> @Carrier//Markdown file.frontmatter.subjects.passive;
Atom.Relations >> @Carrier//Markdown file.frontmatter.relations
```
  - Unresolved CFEL: `Atom.Role >> @Carrier//Markdown file.frontmatter.role`
  - Unresolved CFEL: `Atom.Form >> @Carrier//Markdown file.frontmatter.form`
  - Unresolved CFEL: `Atom.Subjects.Active >> @Carrier//Markdown file.frontmatter.subjects.active`
  - Unresolved CFEL: `Atom.Subjects.Passive >> @Carrier//Markdown file.frontmatter.subjects.passive`
  - Unresolved CFEL: `Atom.Relations >> @Carrier//Markdown file.frontmatter.relations`

### `Atom/(.Role:=Requirement)/(.Form:=Relation Definition)` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Atom/(.Role:=Requirement)` — CA-R-2512@2
  - `Atom` — CA-R-2508@2
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Inherited Property Declaration refs; no child Property Node is created:
  - `Atom.Status` — CA-R-2488@2
  - `Atom.Updated At` — CA-R-2489@2
  - `Atom.Relations.contained_by` — CA-R-2490@2
  - `Atom.Relations.contained_by.atom` — CA-R-2491@2
  - `Atom.Relations.contained_by.scope_unit` — CA-R-2492@2
  - `Atom.ID` — CA-R-2493@2
  - `Atom.Role` — CA-R-2494@2
  - `Atom.Form` — CA-R-2495@2
  - `Atom.Version` — CA-R-2496@2
  - `Atom.Label` — CA-R-2497@2
  - `Atom.Content` — CA-R-2498@2
  - `Atom.Content.Summary` — CA-R-2499@2
  - `Atom.Content.Claim` — CA-R-2500@2
  - `Atom.Content.Claim Scope` — CA-R-2501@2
  - `Atom.Content.Semantics` — CA-R-2502@2
  - `Atom.Content.Details` — CA-R-2503@2
  - `Atom.Tier` — CA-R-2504@2
  - `Atom.Tier.Label` — CA-R-2505@2
  - `Atom.Subjects.Passive` — CA-R-2506@2
  - `Atom.Relations` — CA-R-2507@2
  - `Atom.Subjects` — CA-R-2545@2
  - `Atom.Subjects.Active` — CA-R-2546@2
- Declaration source: `CA-R-2517@2`
  - Semantics:
    A Relation Definition states a Relation’s meaning and endpoints.
  - Fenced Claim block:
```CFEL
Atom/(.Role: Requirement)/(.Form: Relation Definition)
```
  - Unresolved CFEL: `Atom/(.Role: Requirement)/(.Form: Relation Definition)`
- Shared RMED source: `CA-R-2486@2`
  - Remaining Claim prose:
    A Relation Definition states its allowed Host and Target in its Formal claim where existing notation expresses the selectors; otherwise use precise prose. An endpoint signature constrains admissible links; it does not assert links between every matching pair. Cardinality annotations constrain counts independently.
    
    Use HAS_INVERSE for a derived reverse view. Its endpoint sets are the direct Relation's sets swapped. State any displayed reverse signature consistently with that derivation; do not create a separate Definition for the inverse.

### `CFEL` — primary_node

- Declaration source: `CA-R-2244@3`
  - Semantics:
    `/` supplies specialization and inheritance. `//` expresses a named instance
    of a kind. `.` addresses a dependent Property; `:` declares an allowed value
    without requiring its left operand to be a Property.
    
    `Part +> Whole` and `Whole <+ Part` express one containment fact. The pointer
    faces the Whole. IS_CONTAINED_BY is stored from Part to Whole; CONTAINS is
    its derived inverse. Containment supplies no inheritance.
    
    `X >| Y` and `Y |< X` express the same HAS_CLASSIFICATION fact. Entity Y is
    used as an applicable Classification axis; the pointer faces that endpoint.
    This introduces no separate Classification Entity kind or canonical inverse
    Relation Type. Axis applicability does not itself state group membership,
    structural containment, or inheritance.
    
    `X/(.Y: Z)` identifies X qualified by its own Property Y and admitted value Z.
    The leading dot addresses X.Y relative to X. The qualified X inherits X's
    applicable features and constraints; Y does not become a narrower kind of X.
    The Property and value still require their independent governing admission.
    
    `@` calls an already declared Entity, not only a kind, and declares no target.
    `()` provides logical grouping, including relative Property qualification.
    The compound `((RELATION_TYPE))` form remains distinct: a named Relation
    reads from its declared source to target, and its opposite view uses a
    declared derived inverse. Only direct facts are independently stored.
    
    `[format]` specifies the addressed Property's direct-value Format; a
    post-Property `{count}` counts its direct values. A Relation has two
    independent directional slots: the count before its token applies per
    written Source toward Target, while the count after it applies in reverse
    per Target toward Source. Reversing the writing swaps the slots. These
    slots count Relation instances, not distinct targets or Relation arity.
    An omitted slot remains unspecified. CA-R-2243 owns the count forms and
    their bounds; Relation counts do not change direct-value counts.
    
    The Status Group complement expression remains bounded by its governing
    mapping and CA-R-1931; it introduces no general formula language.
    
    Formal constraints belong in the Definition Claim. Semantics explains their
    meaning without adding a second Claim.
  - Remaining Claim prose:
    Graph Syntax defines how Entity Definitions express specialization,
    named-instance, dependent-property, allowed-value, containment, Classification
    axis, already-declared Entity reference, logical grouping, named-Relation,
    value-Format, and cardinality constructs. Its structural parts are Relation,
    Format, and Cardinality. Syntax neither executes a Workflow nor creates an
    Entity instance.
    
    `X: Y` declares Y as an allowed value of X, irrespective of X's kind or
    preceding path; it is not assignment. YAML null and an empty string are
    values for counting, while Format and prose decide admissibility. General
    formulas and bracketed conditions remain separate.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL <+ Relation
CFEL <+ Format
CFEL <+ Cardinality

specialization: /
named_instance: //
dependent_property: .
allowed_value: :
containment: +>, <+
classification_axis: >|, |<
declared_entity_reference: @
logical_grouping: ()
relative_property_qualification: X/(.Y: Z)
named_relation: Source ((RELATION_TYPE)) Target
direct_values: X.Y[format]{count}
relation_counts: Source {forward-count}RELATION{reverse-count} Target
cardinality: {n}, {n+}, {n..m}
inverse: declared and derived, never independently stored
```
- Declaration source: `CA-R-2487@2`
  - Remaining Claim prose:
    CFEL (CAPRMEDIO Formal Expression Language) defines the syntax and meaning of graph expressions used in Subject addresses and Formal Claims.
    
    CFEL is a model component alongside Graph and Carrier. The Graph contains Nodes and Relations; CFEL expresses them.
- Shared RMED source: `CA-R-1194@32`
  - Semantics:
    A path may address classification without declaring an Entity kind. `Atom.Content Role` addresses the relative Property, while `Atom/(.Content Role: Plan)` identifies a qualified Atom inheriting applicable Atom features and constraints. Neither form invents an intermediate Entity kind. The root and operators follow the adopted Entity syntax under CA-R-1931; no Project-name namespace layer is introduced.
  - Remaining Claim prose:
    The following interpretation is required when this governed concept is used:
    
    A Subject Path is a full canonical expression identifying one thing or topic addressed by GOVERNS or DEPENDS_ON. Entity is the canonical expression root under CA-R-2462; this Definition does not enumerate a closed root-branch set. A source path retains the declared operators and full qualification; a short display label is not another identity or alias.
    
    The target is selected by the meaning addressed, not by the Atom's Local Scope Unit, Content Role, folder or Carrier. The path names a target; it is not itself the Subject Relation. A defining Atom may introduce that target, so format checks do not require prior target existence.
- Shared RMED source: `CA-R-1321@34`
  - Remaining Claim prose:
    The following interpretation is required when this governed concept is used:
    
    a Subject Expression **means** a reference **to** **`=1`** canonical Subject Target formed from entity names, registered relation syntax, **and** an optional registered Atom-owner selector. The case-significant lexical component `Atom` occurs **in** the full canonical Entity expression `Entity/Object/Continuant/Governing Objects/Atom`; lowercase `atom(...)` is a distinct case-significant selector keyword, **not** an alias **or** spelling of `Atom` **and not** another Entity kind. Only an approved-profile expression **may** begin with `atom(content_role="<exact Content Role>")` **or** `atom(content_role="<exact Content Role>",type="<exact Atom Type>")`; `type` has no standalone form. Selector literals are non-empty, double-quoted exact literals with no escaping, evaluation, wildcard, alias, or case folding. The reserved selector form is initial `atom(...)`; this does not reserve an ordinary noninitial Name `atom`.
    
    Outside the Term branch, an Entity reference **must** use its exact complete canonical expression with every source-established qualifier; a bare Term is not that expression. The sole one-Term exception is the Subject root `Entity`. Ordinary lexical components **may** reuse Terms with consistent approved meanings; an instance's name is **not** automatically a lexical Term. Inside `((...))`, a registered direct Relation token resolves to **`=1`** admitted Relation Type under the named-Relation notation. Its bare spelling is not that Relation Type entity's complete canonical expression; naming comparison uses the full qualified expression separately. The selector keyword, keys, punctuation, **and** literals remain syntax, **not** entities **or** additional canonical names merely because they occur **in** an expression. A qualified Atom expression such as `Atom/(.Content Role: <exact Content Role>)/(.Type: <exact Atom Type>)` is available only when both exact values have independent source admission; its segments do not become admitted merely by appearing in selector syntax.
    
    `/`, `//`, `.`, `:`, `+>`, `<+`, `>|`, `|<`, `@`, parentheses, the named-relation form `Source ((RELATION_TYPE)) Target`, **and** cardinality follow CA-R-1931 **and** CA-R-2244. `//` is one separator token between a kind **and** a named instance; its right operand is the instance's name, **not** an Atom ID. `@` calls an already declared Entity; it is **not** an Atom-version selector or kind-only reference. Parentheses provide logical grouping. `Part +> Whole` and `Whole <+ Part` are containment, not inheritance or sequence. `X >| Y` and `Y |< X` express the same HAS_CLASSIFICATION fact with Entity Y used as an applicable Classification axis, not membership or a new Entity kind. Relation counts use `Source {forward-count}RELATION{reverse-count} Target`; direct values use `Property[format]{count}`. Operators, calls, grouping, relation delimiters, Formats, **and** cardinality are **not** Terms.
    
    The complete expression **must** resolve **to** **`=1`** canonical Subject Target that already exists **or** is explicitly introduced by applicable defining authority under CA-R-1194 **and** CA-R-1931. Syntax alone neither creates **nor** admits a target **or** native EntityGraph fact. Selector syntax neither enumerates Atom rows **nor** admits an Entity endpoint. The expression identifies the target, **not** the Atom's Subject Relation **to** it. An arbitrary composite expression is **not** one Term **or** automatically one entity name; an admitted qualified property name **may** identify **`=1`** entity.
- Shared RMED source: `CA-R-1931@18`
  - Semantics:
    `/` is specialization and supplies inheritance. `+>` and `<+` are containment
    and do not supply inheritance, sequence, or a property relation. `//` names
    an instance of a kind; `.` addresses a dependent Property; and `:` declares
    an allowed value rather than assigning one. A reference marker calls an
    already declared Entity and creates neither an alias nor a duplicate.
    
    `X.Y` addresses Property Y, and `X.Y: Z` expresses its allowed value.
    `X/(.Y: Z)` instead identifies qualified X entities. For example,
    `Atom/(.Type: Method)` means an Atom with the stated Type qualification, not
    the Type Property inheriting Atom's features. This syntax example alone does
    not admit Method as a Type value; the existing Content Role use is written
    `Atom/(.Content Role: Method)`. Every qualification still requires its own
    admitted Property and allowed value. Existing Carrier keys and encodings
    remain governed separately by Delivery; the notation adds no nested object.
    
    Status Group classifies Atom Statuses through
    `Atom.Status >| Status Group`. The following `<+` expressions describe each
    group's Status parts. In this
    mapping, `* not in (Draft, Archived)` selects admitted Atom Status values
    other than Draft and Archived. It does not admit new Status values, missing
    values or a general expression language. Containment does not imply
    inheritance; the Property-qualified Atom kind inherits through `/`.
  - Remaining Claim prose:
    In an Entity Path, `/` separates a broader kind from its narrower kind; `//`
    separates an Entity kind from a named instance; `.` separates a bearer from a
    dependent Property; and `:` separates any `X` from its allowed literal value
    `Y`, irrespective of X's kind or path. `@` calls an already declared Entity;
    it is not limited to kinds and declares no target. Parentheses provide logical
    grouping.
    
    `Part +> Whole` and `Whole <+ Part` are opposite writings of the same
    containment fact. Its direct fact is Part IS_CONTAINED_BY Whole, and CONTAINS
    is derived. `X >| Y` and `Y |< X` are opposite writings of the same
    HAS_CLASSIFICATION fact, with Entity Y used as an applicable Classification
    axis rather than belonging to a separate Classification Entity kind. This Rule does not
    invent an inverse canonical Relation Type for HAS_CLASSIFICATION.
    
    `X/(.Y: Z)` denotes a narrower kind of X qualified by its own Property Y
    and value Z. The leading dot inside parentheses is relative to X: `.Y`
    addresses `X.Y`. The qualified X inherits X's applicable features and
    constraints. The Property is the qualification condition; it does not become
    a narrower kind of its bearer. This form replaces the proposed classification
    Property category and the earlier bare `X/Y: Z` qualification spelling.
    
    `Source ((RELATION_TYPE)) Target` expresses a defined named Relation. Persist
    the direct fact once and show its declared derived inverse only as a derived
    view. Entity syntax neither creates target identities nor admits native facts
    without defining authority. A defining Atom may introduce its governed Entity.
    
    Cardinality uses `{n}`, `{n+}`, and `{n..m}`. Direct Property values retain
    their post-Property notation, for example `X.Y[format]{n}`. A Relation has two
    independent directional slots: `Source {forward-count}RELATION{reverse-count}
    Target`. The pre-operator slot constrains Relation instances in the written
    Source-to-Target direction per Source; the post-operator slot independently
    constrains the reverse count per Target. These are not distinct-target counts. For example, `Step {1}+>{1+} Workflow` requires one Workflow per
    Step and one or more Steps per Workflow; its reverse writing is
    `Workflow {1+}<+{1} Step`. `Property {1}((IS_PROPERTY_OF)) Bearer` requires
    exactly one outgoing IS_PROPERTY_OF Relation for each Property occurrence;
    postfix-only `{1}` would instead constrain the reverse count per Bearer.
    Each Relation is binary and connects two endpoint nodes or node instances.
    The slots count Relation instances, not Relation arity; omitted slots remain
    unspecified. This Relation counting is independent of the Property's
    direct-value Format and cardinality.
    Advanced functions, formulas, interpolation, and bracketed conditions are out
    of scope.
    
    ### Formal claim
  - Fenced Claim block:
```text
Entity/Object/Continuant/Package <+ Module <+ Code Unit
Atom/(.Content Role: Operations)/(.Type: Step) {1}+>{1+} Atom/(.Content Role: Operations)/(.Type: Workflow)
Atom/(.Content Role: Operations)/(.Type: Sub-step) {1}+>{0+} Atom/(.Content Role: Operations)/(.Type: Step)
Atom/(.Content Role: Method)
Entity/Object/Continuant/Governing Objects/Atom.Status >| Status Group: Draft <+ Draft
Entity/Object/Continuant/Governing Objects/Atom.Status >| Status Group: Archived <+ Archived
Entity/Object/Continuant/Governing Objects/Atom.Status >| Status Group: Current <+ * not in (Draft, Archived)
Source ((RELATION_TYPE)) Target
```
- Shared RMED source: `CA-R-2471@2`
  - Remaining Claim prose:
    In Subject addresses and Formal Claims, `X/Y` selects a narrower Primary Node and `X//Name` an instance of a Primary Node. A Property cannot narrow or instantiate. `X.p` addresses a Property borne by X; an unchanged inherited Property is resolved to its existing declaration rather than redeclared or given another bearer. In Subject addresses, `X/(.p := V)` admits V as a Property value and selects the whole Primary Node X where p equals V. The case does not exclude other allowed values from X.p. `(Node, Node.**)` selects Node and its recursive dependent Properties; it is not a narrowing assertion. Shared Node rules are declared once and inherited by applicable narrower Nodes.
    
    `Part +> Whole` and `Whole <+ Part` are opposite written views of one composition fact, not narrowing. `X >| Axis` and `Axis |< X` are opposite views of one classification fact. `:` marks an allowed value. `=` tests a condition; `==` establishes a required or derived conclusion. Parentheses group expressions; `in (a, b)` expresses membership. `@X` refers to the existing target without copying or reparenting it.
    
    For `Source {:f}((RELATION)){:r} Target`, the pre-operator cardinality constrains the allowed number of outgoing Relation instances per selected source, and the post-operator cardinality constrains the allowed number of reverse links per selected target; reversal swaps their positions. The same notation constrains Properties, instances, and Relations. `{:n}` declares an allowed cardinality, not an actual value; `{=n}` tests a cardinality, and `{==n}` states a required conclusion. Repeated references in a rule, including its conditions and conclusions and both Step alternatives, bind the same selected member. An omitted cardinality annotation leaves that cardinality undefined, as in Current CA-R-2243; it is not an implicit zero or permission. Omitted-domain behavior requires a separate decision before parser adoption.
    
    `(Node, Node.**)` is the model-entity selector. `(Node//, (Node//).**)` is the instance-layer selector. `Node//` selects Node instances including instances of narrower kinds. `(Node//).**` selects recursive Property occurrences of a Node instance; it does not independently instantiate a Property kind. The two layers have separate permissions. Repeated instance matches count once by identity.
    
    Subjects remain addresses and do not contain complete Formal Claims. In Subjects, `:=` combines allowed value and condition, including `Atom.Status := Draft` and `Atom/(.Role := Method)`; it does not write an instance value. Formal Claims retain separate `:` and `=` meanings. The withdrawn `..` form is not adopted; `::` has no assigned meaning here.
- Shared RMED source: `CA-R-2472@2`
  - Remaining Claim prose:
    - `p{:n}` constrains occurrences of the named Property.
    - `p: [format]{:n}` constrains its allowed values.
    - `p.*[format]{:n}` constrains immediate dependent names.
    - `p.**[format]{:n}` constrains dependent names recursively.
    - `p.*[name format]{:n}: [value format]{:m}` also constrains each selected Property's values.
    - The left count is the number of selected Property names.
    - The right count is the number of values per existing Property.
    - Separate expressions use `;`.
    
    Names are unique within one bearer. `x.y.z` differs from `x.z`.
    
    Resolve local declarations first. Resolve inherited declarations next. If neither declares dependents, state `p.*[]{:0}`. Missing annotations remain undefined.
  - Unresolved CFEL: `CFEL fence is outside Claim; its contents were not interpreted.`
  - Unresolved CFEL: `CFEL fence is outside Claim; its contents were not interpreted.`
- Shared RMED source: `CA-M-457@2`
  - Remaining Claim prose:
    - Use admitted CFEL when it expresses the constraint.
    - Use short Claim prose only when CFEL cannot express the constraint without a single-use extension.
    - Do not invent syntax for one constraint.
    - State IS_PROPERTY_OF acyclicity in prose, including no self-loop.
    - Repetitive prose or Semantics is not required.
- Shared RMED source: `CA-R-2548@2`
  - Remaining Claim prose:
    - `>>` delivers an Object to the referenced Carrier or Carrier part.
    - A selection delivers its selected Objects.
    - `@` refers to an already declared target.
    - `!(selectors)` excludes those branches from a selection.
    - Relative exclusions use the selection's base.
    - `=` states an equality condition.
- Shared RMED source: `CA-R-2549@2`
  - Remaining Claim prose:
    - `x > y`: x is greater than y.
    - `x >= y`: x is greater than or equal to y.
    - `x < y`: x is less than y.
    - `x <= y`: x is less than or equal to y.
    - `x + y` returns the numeric sum of two numeric operands. If both operands are integers, the result is an exact integer.
    - Each operand resolves to one numeric value. No string coercion is allowed.
    - Evaluate `+` before `=`, `!=`, `>`, `>=`, `<` and `<=`. Parentheses override this order.
    - `=` tests equality, including in a Claim invariant; it does not assign a value.
    - A missing or multi-valued operand makes an evaluated comparison invalid.
    - Guard optional Properties by their occurrence before comparing their values.
    - A comparison in Claim must hold. In an IF condition, it tests the values.
    - An IF conclusion is evaluated only when its condition holds.
    - A Declaration applies the comparison to each matching instance.
    - Comparisons do not assign values or change occurrence counts.
    - `+>`, `<+`, `>|` and `|<` remain distinct Relation operators.
  - Unresolved CFEL: `CFEL fence is outside Claim; its contents were not interpreted.`
- Shared RMED source: `CA-R-2550@2`
  - Remaining Claim prose:
    - `p ?= e1 ?= e2` is one ordered fallback chain. Use p when authored; otherwise use the first available valid expression from left to right. An authored invalid value is an error, not absence. Omission is Property absence, not null, an empty string, zero or false.
    
    - Expressions may be literals, same-bearer Property paths, explicit bound Property reads, or `LOOKUP(R, q)`. An explicit foreign-bearer read must resolve one target in the declared evaluation context; zero or multiple targets are errors.
    
    - `LOOKUP(R, q)` starts from p’s bearer, follows one existing outgoing R link at each step, and returns the nearest compatible authored q value. The starting bearer is excluded. A known end with no applicable authored value returns absence, allowing the next fallback.
    
    - Resolve q by full Property declaration identity and applicability in the effective MODEL. Skip a bearer only when q is inapplicable or its authored occurrence is absent. Do not match unrelated Properties by bare name or invent a slot on an inapplicable kind.
    
    - An invalid present value, unresolved applicability or graph facts, multiple outgoing targets, or a revisited bearer is an error. Follow only the relation direction named by R.
    
    - Lookup is lazy: stop at the first valid available value. Later branches are not evaluated. Missing final values and evaluated fallback-expression cycles are errors. More than one applicable fallback chain is an error. Independent Declaration constraints still apply.
    
    - Resolve the effective value without writing a Carrier or adding an authored occurrence. It must satisfy p’s declared value Format and cardinality. A fallback cannot satisfy a required authored occurrence. Property-declaration inheritance is unchanged; recursive instance-value lookup occurs only through explicit LOOKUP.
  - Fenced Claim block:
```CFEL
p ?= expression
```
  - Unresolved CFEL: `CFEL fence is outside Claim; its contents were not interpreted.`
  - Unresolved CFEL: `p ?= expression`
- Shared RMED source: `CA-R-2551@2`
  - Remaining Claim prose:
    `UNIQUE(selector, (.p, .q))` requires unique tuples of the selected Properties across the selected logical instances in the explicit Project evaluation context. An optional third argument, `condition`, restricts the population: `UNIQUE(selector, (.p, .q), condition)`.
    
    - Use each selected instance's state in one explicit Project snapshot. Do not expand earlier lifecycle states as DETERMINES does. Without a condition, evaluate the complete selected population regardless of Status Group or containment, including selected Drafts and Archived instances. An incomplete or unresolved population is an error. A known empty population satisfies uniqueness.
    - Evaluate a condition on each candidate instance before resolving tuple Properties. Relative Properties bind to that same instance. False excludes it; unresolved, invalid or ambiguous conditions are errors. Use the existing Boolean grouping and AND/OR syntax.
    - For each selected instance, bind every tuple Property to that same instance. Each must have exactly one valid scalar value; missing, invalid or multiple values fail the constraint.
    - Two distinct selected logical instances must not have equal value tuples. Repeated references or Carrier representations of the same logical instance do not create additional instances. Do not infer that two instances are one merely because their key tuples match.
    - Compare scalar values in their declared Format without implicit normalization or coercion. A declared reference compares by its resolved target identity; an absent or ambiguous binding is an error, with no raw Carrier-locator fallback. Tuple components need not be individually unique.
    - Optional Properties require an explicitly resolved subset whose members carry the required values; do not silently skip missing rows.
    
    `UNIQUE` is a declarative condition. It does not allocate, renumber or write values.
- Shared RMED source: `CA-R-2552@2`
  - Remaining Claim prose:
    - `Kind//` selects existing instances of Kind and its narrower kinds.
    - `Kind//{:n}` applies the existing cardinality to the selected logical instances within the Project context. Resolve the complete selection and count each instance once across repeated references or Carrier representations. An unresolved population is an error.
    - `Kind//$x` ranges over the selected instances. Each constraint must hold for every matching binding. Repeated `$x` references in one Claim block identify the same instance within each binding.
    - `in` and `not in` test an instance's identity against a selected instance set. `=` and `!=` compare bound instance references by identity; they do not test kind membership or broadcast a scalar comparison over a set.
    - `Kind//$x.p` selects and binds an instance and reads its Property `p`. `$x.p` reads that same bound instance's Property.
    - In an IF condition, `Kind//$c ((R)) Kind//$p` tests a link that already exists, including a legitimately derived inverse. It is not an endpoint signature and does not create a link.
    - Evaluate the condition for candidate bindings. Its THEN conclusion applies only to bindings for which that link exists; it does not require links between every candidate pair.
    - Endpoint counts aggregate matching links per endpoint; they do not require a link between every pair of bindings.
    - Binding selects existing instances. It does not create an instance named `$x` or assign a value imperatively. `@` continues to reference an existing target.
  - Unresolved CFEL: `CFEL fence is outside Claim; its contents were not interpreted.`
- Shared RMED source: `CA-R-2561@2`
  - Remaining Claim prose:
    `IMMUTABLE(p)` requires the same valid scalar Property value for one logical bearer from the first point when the surrounding scope selects that Property onward.
    
    - At first applicability, bind the one existing valid scalar value. Existing occurrence, Format and value-cardinality constraints still apply. Guard an optional Property before applying `IMMUTABLE`.
    - Bind later versions to the same logical bearer using supplied lineage, not by matching the mutable Property value. A new Version or Carrier representation does not create a new bearer for this check.
    - If an IF guard activates `IMMUTABLE`, the constraint remains active for that bearer after the first true condition, including when later versions no longer satisfy the guard.
    - Use the first applicable value, not the latest observed value. Missing or invalid required values, unresolved bearer lineage, or incomplete history needed to establish the first applicable value are errors; none proves immutability.
    - After activation, every later version of that bearer must still provide exactly one valid scalar value matching the bound value. A later false guard or removal of an optional Property does not suspend the constraint. Compare using the declared scalar Format, without implicit normalization or coercion.
    
    `IMMUTABLE` is a declarative invariant. It does not write, allocate or lock a value, or perform a Workflow step.
- Shared RMED source: `CA-R-2562@2`
  - Remaining Claim prose:
    `DETERMINES(selector, (.key, ...), (.dependent, ...))` requires equal ordered key tuples to have equal ordered dependent tuples. An optional fourth argument, `condition`, restricts the state population: `DETERMINES(selector, (.key, ...), (.dependent, ...), condition)`.
    
    - Use one explicit Project evaluation context. Resolve the complete relevant state history selected by Kind, including versions and rebuild states, rather than only the latest Current snapshot.
    - The context supplies the historical population, Property-value resolution and declared reference-identity bindings. These are evaluation inputs, not new Artifact fields.
    - Evaluate an optional condition separately on each candidate historical state before resolving tuple Properties. Relative or selected-Kind Property references in that condition bind to that same state. A false condition excludes the state. An unresolved, invalid or ambiguous condition is an error. Without a condition, use all selected states. Do not select by only the latest state and then include its excluded historical states.
    - Bind every tuple Property to the same selected state. Each must resolve to exactly one valid scalar value. Missing, invalid or multiple values are errors; do not skip rows.
    - Compare tuple positions in order. Compare scalar values using their declared Format without implicit normalization or coercion. A declared reference compares by its resolved target identity. Missing or ambiguous reference bindings are errors; raw text or Carrier locators are not fallback identities.
    - For every pair of selected states, equal keys require equal dependents. Repeated keys with equal dependents are allowed. Different keys may have equal dependents.
    - An unresolved or incomplete required history is an error. A known complete empty selection satisfies the constraint.
    
    `DETERMINES` does not assert key uniqueness, merge instances, allocate IDs, freeze inputs, assign values or execute a Workflow.
- Shared RMED source: `CA-R-2563@2`
  - Remaining Claim prose:
    `FENCED_LABELS(p)` selects one label per fenced code-block occurrence in one scalar Markdown value.
    
    - Evaluate p separately for each matching bearer. Do not pool values across Atoms.
    - Use the complete recursive Markdown block parse. Exclude indented code blocks.
    - Preserve duplicate labels as separate occurrences. An unlabelled fence contributes an empty label.
    - `FENCED_LABELS(p): [format]{:n}` requires every selected label to match the Format. The count constrains selected occurrences, including duplicates.
    - The finite literal Format `[in (CFEL)]` matches only CFEL. An empty selection satisfies the Format condition but must still satisfy the count.
    - Bind parsed labels through the governing Markdown Format and the existing CFEL-labelled-fence rule. No whole-info-string, token or case-normalization policy is added here.
    - Missing or multiple Markdown values, incomplete parsing and unresolved or ambiguous label bindings are evaluation errors. Never replace them with an empty selection.
    
    Selection reads Markdown value structure, not Graph Nodes or dependent Properties. CFEL body syntax is validated separately.
- Shared RMED source: `CA-R-2566@2`
  - Remaining Claim prose:
    `Kind//(c1, ...).p` selects p from matching instances of Kind and its narrower kinds in one explicit current-Project instance snapshot.
    
    - Relative filter paths bind the same candidate instance. Outer variables retain their enclosing bindings; an unbound or ambiguous variable is an error.
    - Every filter condition must hold. Commas inside filter parentheses mean AND. Outside them, selector commas retain their existing union meaning. Existing AND, OR and grouping remain available. Filter conditions and AND groups evaluate left-to-right with short-circuiting: a later field read is evaluated only after its earlier guard holds.
    - A missing, invalid or unresolved evaluated filter is an error, not false. Short-circuiting excludes only an unevaluated later condition; it never turns an evaluated invalid value into a skipped record. Reference comparisons use resolved target identity, not raw identifiers or Carrier data.
    - Each matching instance contributes exactly one valid scalar p. Selection does not implicitly expand lifecycle history.
    - `MAX(selection)` returns the greatest selected scalar under its Format-defined ordering. Numeric and datetime values are orderable. Compare datetimes as instants, not lexical strings.
    - Empty, incomplete, incompatible or non-orderable selections are errors.
    - Equal greatest values return that scalar value. MAX does not select a record row.
    
    Both operations are read-only. They create no record, Property, Relation, value or lifecycle transition.
- Shared RMED source: `CA-R-2585@2`
  - Remaining Claim prose:
    - Within `COUNT(...)`, `p: $` selects the direct value occurrences of Property p on the current bearer. `$` is anonymous and binds no new named variable. It does not select dependent Property names.
    - Repeated equal values remain separate occurrences. A known absent optional p selects an empty selection of value occurrences. An unresolved or malformed bearer, Property population, or value is an error, not an empty set.
    - `COUNT(p: $)` returns the nonnegative number of selected direct value occurrences. `COUNT(DISTINCT p: $)` returns the number of their unique values.
    - DISTINCT equality is the declared Format equality: no implicit string trimming, case folding, coercion, or canonicalization. A reference Format compares resolved reference identity.
    - Counts apply per current bearer, not across Atoms. Existing Property occurrence, value-format, value-count, and source constraints remain in force.
    - Outside this COUNT selection, existing `p: literal` and `p: [format]{:n}` meanings are unchanged.
  - Unresolved CFEL: `CFEL fence is outside Claim; its contents were not interpreted.`
- Shared RMED source: `CA-R-2588@2`
  - Remaining Claim prose:
    - `Host {:0}((*))` sets the default outgoing Relation cardinality for Host to zero.
    - `((*))` selects Relation names. Allowed-value notation such as `{:x}` and literal value bindings keep their existing meanings.
    - Resolve the selected MODEL, inheritance and applicable named Relation constraints before applying the default. Match the Host, Relation, Target and model or instance layer. A matching named entry supplies its own outgoing count.
    - Apply the default to links outside the matched Host, Relation, Target and layer of a named exception. A local named exception also works with an inherited default.
    - Narrowing inheritance preserves each selector's scope. Property dependence is distinct from narrowing.
    - Named constraints retain their bounds, including an explicit named zero. An explicit MODEL override replaces the matching effective rule. Check all other applicable named constraints together and report conflicting bounds.
    - Conditional constraints retain their conditions. Normalize `>|` and `|<` to their HAS_CLASSIFICATION directions: an assertion or true conditional conclusion supplies the matching entry only for its stated Host, axis, value and condition. A Relation reference used only as a condition or example grants nothing. Do not infer unspecified axes or counts.
    - Model-entity and instance selectors have separate effective whitelists. An entry applies only to its stated layer. A direct Relation permission does not automatically permit its inverse view; each direction needs its own named entry. Derived inverse links are not authored a second time.
    - Every count concerns the active Subject's outgoing Relations. The counterpart Declaration owns its own outgoing counts.
  - Unresolved CFEL: `CFEL fence is outside Claim; its contents were not interpreted.`
  - Unresolved CFEL: `CFEL fence is outside Claim; its contents were not interpreted.`
  - Unresolved CFEL: `CFEL fence is outside Claim; its contents were not interpreted.`

### `Carrier` — primary_node

- Declaration source: `CA-R-1958@15`
  - Remaining Claim prose:
    A Carrier **means** a storage representation of a Continuant, distinct from what it represents. A Carrier can represent a record of an Occurrent, **not** the Occurrent itself.
    
    ### Formal claim
    For implementation_of, the direct owner is the governed Implementation Carrier and each tuple targets the specification Atom it implements. For evidence_for, the direct owner is the evidence Carrier and each tuple targets the Evaluation or Implementation Carrier it supports. These are endpoint permissions, not extra fields on reusable Relation Types or additional storage facts for their derived inverses.
  - Fenced Claim block:
```text
Carrier.ID[string]{1}
Carrier.Canonical Address[string]{1}
Carrier.Format[string]{1}
```
- Shared RMED source: `CA-R-644@25`
  - Remaining Claim prose:
    CAPRMEDIO **may** admit a materialized representation **only** **when** an explicit Requirement establishes that the representation is necessary **to** preserve a required outcome **or** a material governed distinction under CA-M-005.
    
    possible justifications include:
    
    - an external contract;
    - portability;
    - performance;
    - availability;
    - an audit snapshot; **or**
    - independently usable publication.
    
    these examples do **not** close the set of justifications; another justification still requires the explicit Requirement **and** demonstrated necessity.
- Shared RMED source: `CA-E-502@29`
  - Remaining Claim prose:
    the Plan Carrier Evaluation **must** reject Carrier facts that create duplicate identity **or** contradict the shared Plan model.
    
    - accept a mandatory Markdown file **with** **or** **without** a matching optional Hub directory under `CA-D-460-CORE_META_MODEL-CORE-DELIVERY--serialize-plan-atom-carrier-bundles`; reject a directory **without** that file.
    - count a matching pair once; reject two IDs, divergent stems, conflicting Status, a separate Epic identity, **or** an Objective file that claims **to** be another Atom for the same Hub.
    - require DoD **in** **every** supplied Plan file, even **when** it carries contained child Plans **or** explicit overrides.
    - validate leading navigation numbers **before** Atom IDs, their local uniqueness, mutable Label tokens, **and** canonical Summary slugs. changing a number **or** Label **must not** change identity **or** scheduling.
    - read Plan Status from its own file **and** check its local placement; reject read-time inference from a containing Hub **or** path.
    - change a parent Plan's Status to Active, Backlog, Done, Canceled **or** Archived as admitted by its model: require independent single-Atom Actions for the selected latest descendants under CA-R-1521, without an optional descendant mode. For a containing Plan Atom requested Done **or** Canceled, preserve selected latest contained Plans already Done **or** Canceled and request Canceled for every other selected latest contained Plan. After the cascade, every selected latest contained Plan must be Done **or** Canceled; mixed terminal statuses are allowed, and no child is forced to match the parent's requested Status merely because the parent is Done **or** Canceled. For target Archived, every contained latest Atom is requested as Archived, including Done Plans. Other admitted targets retain the same-Status cascade. Check each Atom's own model; reject an invented target value **or** a multi-target Action.
    - retain each Current descendant inside its parent Carrier tree with the local Status mapping under CA-D-461; for a contained Current Plan, validate its Status placement relative to its immediate containing Plan's Directory Carrier. For example, a Done child is in `<parent-directory>/done/<child>.md`, using its canonical matching stem. Validate Draft carriers in the owning Scope Unit's shared `03_plan/draft` area. Validate each Archived Plan Markdown Carrier directly in the shared `03_plan/archived` area, without parent/child Plan directory nesting, and with CA-D-289's Version suffixes.
    - leave referenced Plans outside the tree **and** older archived Revision bytes, Version **and** Status unchanged; reject older Revisions as cascade targets. Allow retained-history subtrees and non-Atom assets to accompany the matching Directory Carrier byte-for-byte unchanged, without inferring Status effects. No independent migration of noncanonical legacy `archive/` trees is implied.
    - accept root Backlog Plans **in** `03_plan/001_backlog`; reject `031_backlog` as the canonical new encoding **and** reject a `version-<VERSION>` directory substituted for a Version-labeled Plan identity.
    - retain one identity **when** contained work is added, removed, **or** reordered; a changed Summary follows Atom replacement authority rather than independent filename editing.
    
    report the invalid Carrier Bundle, source fact, **and** violated Delivery rule.
- Shared RMED source: `CA-E-522@19`
  - Remaining Claim prose:
    the Evaluation **must** assess storage-boundary interpretability using the following evidence **and** result conditions.
    
    ### Inputs
    
    use the Operator's classifications, retention explanations, **and** the governing evidence that establishes the expected classification for **every** submitted case.
    
    ### Expected answers
    
    | Case | Expected classification |
    | --- | --- |
    | Workflow **and** Implementation events | the shared Project Work Journal through its D-defined Project-wide Carrier |
    | multiple segments **in** the selected Journal Carrier | Carriers of the same Journal, **not** additional Journals |
    | Artifact Change Log **and** Process Log | non-authoritative Projections of that Journal, **not** separate historical sources |
    
    ### Result
    
    - return `fail` **if** the evidence establishes **any** of these conditions:
      - **`<90`**% of classifications are correct.
      - a classification treats Runtime State **or** scratch as canonical truth.
      - a placement creates a separate authoritative Journal for a Workflow, Scope Unit, **or** Content Role.
      - a segment **or** log classification contradicts its expected answer above.
    - **otherwise**, return `unresolved` **if** missing evidence **or** an ambiguous boundary prevents the expected answers **or** classification score from being established. record a Concern for **every** ambiguous boundary **and** stop storage-boundary readiness **until** the governing rule **or** its presentation is corrected.
    - **otherwise**, return `pass`: the evidence establishes **`>=90`**% correct classifications **and** satisfies **all** absolute boundary checks above.
- Shared RMED source: `CA-E-523@18`
  - Remaining Claim prose:
    the Evaluation **must** assess Journal-view integrity using the following fixtures **and** result conditions.
    
    ### Inputs
    
    use **`=1`** admitted Artifact-change event associated with an execution **and** **`=1`** admitted read-only execution event, their source records, the declared Journal selection, **and** the derived views.
    
    ### Expected behavior
    
    - the Artifact-change event **may** appear **in** the two views with the same canonical Event identity.
    - the read-only execution **must not** require a fabricated Artifact-change event.
    - rebuilding a view from the same declared Journal selection **must** preserve its source event references **and** represented historical facts.
    
    ### Result
    
    - return `fail` **if** a fixture contradicts the expected behavior **or** does **any** of the following:
      - independently writes history into a view.
      - creates a second authoritative record merely **to** serve the other view.
      - changes a represented fact **without** its source record.
      - invents an execution association **or** successful outcome.
      - treats a record as proof that its claimed outcome occurred.
      - reports known incomplete **or** stale coverage as complete current history.
    - **otherwise**, return `unresolved` **if** missing evidence **or** an ambiguous boundary prevents the expected behavior **or** integrity checks from being evaluated. record a Concern for **every** ambiguous boundary **and** stop storage-boundary readiness **until** the governing rule **or** its presentation is corrected.
    - **otherwise**, return `pass`: the evidence satisfies **all** expected behavior **and** integrity checks above.
- Shared RMED source: `CA-D-304@30`
  - Remaining Claim prose:
    **every** Carrier-only recoding **must** preserve Atom identity, Claim, its textual Claim Scope, Claim Target Scope Unit, Atom Scope, **and** authored direct semantic relations **without** semantic change.
- Shared RMED source: `CA-D-309@27`
  - Remaining Claim prose:
    **every** admitted materialized representation Carrier **must** have a recoverable binding **to** its exact canonical source Revision **and** **`=1`** deterministic regeneration **or** reconciliation rule.
    
    the binding **may** be recovered through the selected authoritative source frontier **and** governing derivation authority; it does **not** require source metadata **to** be embedded **in** **every** resulting Carrier. an applicable Carrier specification determines whether **and** how **any** explicit binding is serialized.
    
    for Applicable Methodology projected Atom Carriers, CA-D-305 requires an explicit one-way binding **to** the original source Atom Carrier while preserving its authored content, identity, **and** Revision. that specific binding **must not** create duplicate source authority **or** impose a blanket persisted source frontier on other Projections contrary **to** CA-R-1494.
- Shared RMED source: `CA-D-311@26`
  - Remaining Claim prose:
    **every** governed Carrier **must** represent its carried Artifact Revision deterministically **and** human-readably **without** adding, removing, duplicating, **or** changing authoritative content.
- Shared RMED source: `CA-D-312@28`
  - Remaining Claim prose:
    **every** Scope Unit **must** have one authority Carrier place **and** one Delivery Carrier place **without** treating its Delivery place as another Scope Unit.
- Shared RMED source: `CA-D-341@29`
  - Remaining Claim prose:
    runtime cleanup **must not** remove persistent Carriers holding canonical authority or retained history.
- Shared RMED source: `CA-D-377@26`
  - Remaining Claim prose:
    the Framework Instance Settings TOML Carrier **must not** contain Atom Frontmatter, Atom ID, Atom Revision metadata, Atom relations, rationale, **or** provenance; its Revision binding follows CA-D-360.
- Shared RMED source: `CA-D-394@23`
  - Remaining Claim prose:
    a convenience symlink Carrier **must** expose the one native reusable framework source governed by project-local authority **without** creating copied authority, an additional governance owner, **or** a live authority cycle.
- Shared RMED source: `CA-D-395@24`
  - Remaining Claim prose:
    a Carrier encoding of `scope_path` **must** omit the ambient current Project **and** use an empty path for Project Scope.
- Shared RMED source: `CA-D-434@25`
  - Remaining Claim prose:
    a current authoritative Operations Atom File Carrier **must** reside **in** the `09_operations/` Content Role Directory directly under its owning Scope Unit. first-artifact directory materialization remains governed by CA-D-296-CORE_META_MODEL--materialize-content-role-directories-on-first-artifact; this placement does **not** replace the separately governed placement of projected copies **or** archived Revisions.
- Shared RMED source: `CA-D-466@22`
  - Remaining Claim prose:
    **when** an applicable qualified Artifact Status model exists **and** an Artifact has **`=1`** valid current Status, its Carrier placement **must** follow the most specific applicable Delivery rule for that Artifact Type; **only when** no more-specific mapping exists, Active uses the canonical current directory **and** another Status uses its lowercase Status subdirectory. **when** no applicable qualified Status model exists, Carrier placement **must not** derive a Status directory from absent Status.
- Shared RMED source: `CA-D-636@16`
  - Remaining Claim prose:
    a Carrier binding **must** identify the Entity actually represented by that Carrier. a current Entity's Carrier binds that current Entity; a preserved historical version's Carrier binds that archived Atom version or the historical record actually represented, not a separate Revision entity. citing a current Entity's Version **must not** reclassify the current Entity as an archived version.
- Shared RMED source: `CA-R-1642@32`
  - Remaining Claim prose:
    the following ordered generated-data pipeline stages **must** be registered, referenced by their Carrier prefixes governed by CA-D-388-PROJECT_CONFIGURATION-ENG_DECISION--serialize-generated-data-stage-prefixes-and-formats:
    
    | Stage reference | Stage meaning |
    | --- | --- |
    | `src` | canonical Journal input; authority comes from the Journal, **not** the prefix. |
    | `stg` | deterministic, lossless Projection of a bounded `src` frontier. |
    | `mrt` | consumer-ready semantic Projection, including Requirement groupings by scope **and** tier **or** Mermaid relation maps. |
    | `biz` | aggregated CAPRMEDIO artifact **and** implementation metrics, including point-in-time snapshots **and** historical trends. |
    
    dependencies **must** move forward through `src → stg → mrt → biz`; a stage **may** depend on **any** earlier registered stage but **must not** depend on a later stage.
- Shared RMED source: `CA-E-513@23`
  - Remaining Claim prose:
    the Atom Carrier Validation definition check **must** reject a graph **or** binding that cannot preserve its declared read-only assessment boundary.
    
    - require **=1** entry **and** **=1** Step node, a resolvable Step reference, **=1** Action per Step, explicit compatible input bindings, **and** admitted Workflow-scoped transitions.
    - require reachable terminal outcomes for incomplete, invalid, valid, **and** execution-error cases as defined by the referenced Action; **none** of the outcomes **may** be silently mapped **to** valid.
    - verify that this graph is acyclic, contains no implicit retry **or** repair, **and** does **not** duplicate Action behavior inside its Step bindings **or** graph.
    - verify that findings do **not** prevent assessment of independent targets, while missing authority **or** changed inputs cannot become proof of conformance.
    - reference current self-sufficiency **and** source-binding Evaluations for the checked conditions; definition conformance **must not** be reported as a successful Tool execution.
- Shared RMED source: `CA-D-320@23`
  - Remaining Claim prose:
    the CAPRMEDIO Project **must** place its selected running Framework Engine releases, stable launchers, Tools, Apps, Skills, sessions, service state, **and** resumable execution state under `.caprmedio_runtime/`. runtime technical **and** business Journal Carriers use their explicitly configured governed sinks **and** are **not** required **to** use this Directory Carrier.
- Shared RMED source: `CA-D-324@28`
  - Remaining Claim prose:
    **every** Scope Unit **in** the CAPRMEDIO Project **must** use the same administrative Content Role directory mapping directly under its own authority directory for current-scope placement:
    
    - Concern: `01_concern/`;
    - Analysis: `02_analysis/`;
    - Plan: `03_plan/`;
    - Requirement: `04_requirement/`;
    - Method: `05_method/`;
    - Evaluation: `06_evaluation/`;
    - Delivery: `07_delivery/`;
    - Implementation: `08_implementation/`;
    - Operations: `09_operations/`.
    
    materialize these directories under `CA-D-296-CORE_META_MODEL-DELIVERY--materialize-content-role-directories-on-first-artifact`. preserve specific Carrier placement rules **and** apply Status placement under `CA-D-466-CORE_META_MODEL-DELIVERY--place-carriers-by-applicable-status-delivery`.
- Shared RMED source: `CA-D-388@21`
  - Remaining Claim prose:
    Journal input **and** generated Projection Carriers **must** use these ordered stage prefixes: canonical Journal input `src`, deterministic lossless staging Projection `stg`, consumer-ready semantic Projection `mrt`, **and** aggregated metrics Projection `biz`. `src` **must** use canonical NDJSON Journal input; `stg` **must** use TOON. these prefixes classify Journal inputs **and** generated Projections **only**. unregistered stage prefixes remain available for later governed Extension.
- Shared RMED source: `CA-D-396@21`
  - Remaining Claim prose:
    **every** structured production log record **must** include, **where** applicable:
    
    - UTC timestamp, severity, **and** a stable event name;
    - component, environment, **and** deployed version;
    - run, request, job, workflow, session, correlation, **or** trace identity;
    - relevant domain entity identity **and** lifecycle state;
    - outcome, duration, attempt number, **and** retry disposition;
    - stable error code **and** exception class for failures; **and**
    - a concise human-readable message with sanitized diagnostic context.
- Shared RMED source: `CA-D-405@21`
  - Remaining Claim prose:
    the Development Backlog Carrier **must not** retain a completed-work section.
- Shared RMED source: `CA-D-499@12`
  - Remaining Claim prose:
    an `ERROR` **or** `WARNING` record **must** be actionable: it identifies the failed **or** degraded condition, affected scope, expected operator **or** automated response, **and** whether retry is safe.
- Shared RMED source: `CA-D-500@13`
  - Remaining Claim prose:
    production logs record material state transitions **and** boundary outcomes; ordinary internal ticks do **not** define routine production log events.
- Shared RMED source: `CA-D-501@13`
  - Remaining Claim prose:
    an exception is emitted once at the boundary responsible for handling **or** escalating it; lower layers preserve structured context **without** duplicating the same stack trace at **every** call boundary.
- Shared RMED source: `CA-D-502@12`
  - Remaining Claim prose:
    production logs **must not** contain passwords, API keys, access tokens, session secrets, cookies, private keys, complete credentials, **or** unredacted secret-bearing payloads.
- Shared RMED source: `CA-D-503@12`
  - Remaining Claim prose:
    personal, customer, **and** commercially sensitive data in production logs **must** be omitted, masked, hashed, tokenized, **or** **otherwise** minimized according to the applicable boundary.
- Shared RMED source: `CA-D-504@14`
  - Remaining Claim prose:
    production technical **and** business runtime log Journals **must** use the deployment environment's governed logging sink. governed CAPRMEDIO workflow **and** local project-control Journals **are not** substitutes for the production system's log platform.

### `Carrier/Database` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Carrier` — CA-R-1958@15
- Inherited Property Declaration refs; no child Property Node is created:
  - `Carrier.Canonical Address.Segment` — CA-R-1948@12
  - `Carrier.Canonical Address` — CA-R-1949@11
  - `Carrier.Format` — CA-R-1950@12
  - `Carrier.ID` — CA-R-1951@12
- Declaration source: `CA-R-1955@11`
  - Remaining Claim prose:
    A Database Carrier **means** a Carrier that represents content in a database.

### `Carrier/Directory` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Carrier` — CA-R-1958@15
- Inherited Property Declaration refs; no child Property Node is created:
  - `Carrier.Canonical Address.Segment` — CA-R-1948@12
  - `Carrier.Canonical Address` — CA-R-1949@11
  - `Carrier.Format` — CA-R-1950@12
  - `Carrier.ID` — CA-R-1951@12
- Declaration source: `CA-R-1956@11`
  - Remaining Claim prose:
    A Directory Carrier **means** a Carrier that uses a directory to represent its carried Continuant. Merely containing files does **not** make a directory a Directory Carrier.
- Shared RMED source: `CA-D-264@29`
  - Remaining Claim prose:
    an Artifact Revision whose canonical Carrier is nested below a Directory Carrier **must** derive **`=1`** direct `IS_CONTAINED_BY` connection to the Structural Entity Revision carried by its nearest ancestor Directory Carrier **and** the reverse `CONTAINS` view from that connection.
- Shared RMED source: `CA-D-318@24`
  - Remaining Claim prose:
    **every** governed Project **must** place its governing Artifacts **and** project-control evidence under `.caprmedio_<project_name>/`, **where** `<project_name>` is that Project's exact lowercase name.
- Shared RMED source: `CA-D-331@23`
  - Remaining Claim prose:
    a durable Hub Carrier **may** list stable child folders **and** their Hubs but **must not** enumerate individual Atom Carriers **or** Runtime State descendants.
- Shared RMED source: `CA-D-451@21`
  - Remaining Claim prose:
    a filesystem folder **must** be classified as a Directory Carrier **only** **when** it carries a Structural Entity under CA-D-263.
    
    - a folder's visibility **in** a graph **or** its containment of files does **not** itself establish that binding.
    - administrative Content Role directories **and** Status subdirectories provide Carrier placement, **not** separate Structural Entities **or** Directory Carriers. Status placement remains governed by CA-D-295 **and** CA-D-352.
- Shared RMED source: `CA-D-464@25`
  - Remaining Claim prose:
    **every** represented Directory Carrier **must** carry **`=1`** governed object Revision: either one Structural Entity Revision **or**, **where** an applicable Delivery rule permits it, one Atom Revision; it **must not** establish a second object merely because it contains subordinate Carriers.
- Shared RMED source: `CA-D-550@19`
  - Remaining Claim prose:
    **all** persistent view Projection Carriers of a Project **must** reside under **`=1`** Directory Carrier: `.caprmedio_<project_name>/_projection/`, **except** Applicable Methodology, whose Carrier Root **must** remain `.caprmedio_<project_name>/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/`.
- Shared RMED source: `CA-D-321@21`
  - Remaining Claim prose:
    the CAPRMEDIO Project **must** place disposable scratch, staging, test cache, atomic-write intermediate, build intermediate, **and** interrupted-cleanup Carriers under `.caprmedio_tmp/`.
- Shared RMED source: `CA-D-322@19`
  - Remaining Claim prose:
    the CAPRMEDIO Project root **must** use (101_FRAMEWORK_METHODOLOGY, 102_FRAMEWORK_ENGINE, 103_OPERATOR_DOCUMENTATION, 104_CORE_EXTENSIONS, 105_RELEASES, 110_COMMUNITY_EXTENSIONS, 110_FIELD) as its current Scope Unit Delivery Directory Carriers.
- Shared RMED source: `CA-D-323@19`
  - Remaining Claim prose:
    `.caprmedio_caprmedio/` **must** use (101_LAYER_1_FRAMEWORK_METHODOLOGY, 102_LAYER_2_FRAMEWORK_ENGINE, 103_LAYER_3_OPERATOR_DOCUMENTATION, 104_LAYER_4_CORE_EXTENSIONS, 105_LAYER_5_RELEASES, 110_FEATURE_COMMUNITY_EXTENSIONS, 110_FEATURE_FIELD) as its current top-level Scope Unit authority Directory Carriers.
- Shared RMED source: `CA-D-325@24`
  - Remaining Claim prose:
    the CORE_META_MODEL **and** PROJECT_CONFIGURATION Scope Units of the CAPRMEDIO Project **must** use authority Directory Carriers under `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/` **and** `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/` respectively.
- Shared RMED source: `CA-D-327@23`
  - Remaining Claim prose:
    the CAPRMEDIO Project root **must** carry **only** Delivery Directory Carriers produced for Project Scope Units whose authority Carriers live under `.caprmedio_caprmedio/` **or** another registered Project-owned Carrier root.

### `Carrier/Docker Image` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Carrier` — CA-R-1958@15
- Inherited Property Declaration refs; no child Property Node is created:
  - `Carrier.Canonical Address.Segment` — CA-R-1948@12
  - `Carrier.Canonical Address` — CA-R-1949@11
  - `Carrier.Format` — CA-R-1950@12
  - `Carrier.ID` — CA-R-1951@12
- Declaration source: `CA-R-2198@5`
  - Remaining Claim prose:
    A Docker Image **means** an immutable, addressable Carrier of packaged Implementation.

### `Carrier/File` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Carrier` — CA-R-1958@15
- Inherited Property Declaration refs; no child Property Node is created:
  - `Carrier.Canonical Address.Segment` — CA-R-1948@12
  - `Carrier.Canonical Address` — CA-R-1949@11
  - `Carrier.Format` — CA-R-1950@12
  - `Carrier.ID` — CA-R-1951@12
- Declaration source: `CA-R-1957@11`
  - Remaining Claim prose:
    A File Carrier **means** a Carrier that represents content in a file.
- Shared RMED source: `CA-R-2269@3`
  - Remaining Claim prose:
    For a Markdown File Carrier, Main Content is its Markdown body and YAML Frontmatter is its optional structured metadata region. Main Content can contain Paragraphs and CCE Operator occurrences; these are content parts, not additional Files. A Frontmatter Scalar is one direct primitive value within a declared metadata field. These logical regions are not separate Carriers.
    
    The Filename may contain zero or more Scope Unit Tokens. Each serialized Scope Unit reference uses one token under CA-D-302; this does not require all File names to carry such a token.
    
    ### Formal claim
  - Fenced Claim block:
```text
Carrier/File.Main Content[string]{0..1}
Carrier/File.Main Content.Paragraph[string]{0+}
Carrier/File.Main Content.CCE Operator[string]{0+}
Carrier/File.YAML Frontmatter{0}
Carrier/File.YAML Frontmatter.Scalar[scalar]{0+}
Carrier/File.Filename.Scope Unit Token[string]{0+}
```
- Shared RMED source: `CA-E-457@34`
  - Remaining Claim prose:
    the Evaluation **must** reject an Atom Revision **if** it has other than **`=1`** authoritative Markdown Atom Carrier on the Project filesystem, its authoritative Carrier does **not** contain YAML Frontmatter followed by the Content-Role-specific structured Main Content under CA-D-479-CORE_META_MODEL-DELIVERY--use-stable-headings-for-atom-body-properties, **or** a TOML, YAML, JSON, database, **or** projected copy is treated as authoritative for that Atom Revision.
- Shared RMED source: `CA-E-506@28`
  - Remaining Claim prose:
    the Evaluation **must** accept **only** Atom Carriers that preserve self-sufficiency, **`=1`** internal value source, **and** consistent outward representations.
- Shared RMED source: `CA-D-330@27`
  - Remaining Claim prose:
    **every** CAPRMEDIO-owned Markdown, TOML, **or** YAML File Carrier **must** remain valid, legible, **and** navigable **in** GitHub repository file preview **without** relying on editor-specific syntax for required content.
- Shared RMED source: `CA-D-356@22`
  - Remaining Claim prose:
    **every** authoritative Markdown Atom Carrier **must** contain YAML Frontmatter followed by Main Content.
- Shared RMED source: `CA-D-416@29`
  - Remaining Claim prose:
    the Term Markdown Atom Carrier **must** be **NARROWER_THAN** File Carrier.
- Shared RMED source: `CA-D-452@19`
  - Remaining Claim prose:
    secret values **must** be stored **only** **in**:
    
    - gitignored `.env` File Carriers; **or**
    - a dedicated secret vault.
- Shared RMED source: `CA-R-621@16`
  - Remaining Claim prose:
    the caprmedio Implementation **must** resolve both Settings Artifacts through the Core Meta-Model Carrier rules CA-D-359 **and** CA-D-364 **without** defining a Project-specific competing location.
- Shared RMED source: `CA-D-326@26`
  - Remaining Claim prose:
    the current CAPRMEDIO configuration **must** place projected Atom File Carriers under `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/<04_requirement|05_method|06_evaluation|07_delivery|09_operations>/` with **every** source basename preserved.
- Shared RMED source: `CA-D-328@23`
  - Remaining Claim prose:
    the CAPRMEDIO Project **must** place its shared Work Journal **in** `.caprmedio_caprmedio/_journal/`.
- Shared RMED source: `CA-D-337@20`
  - Remaining Claim prose:
    the CAPRMEDIO Project **must** place its own license at root `LICENSE` **and** retained third-party legal File Carriers under root `LICENSES/` outside CAPRMEDIO authority, installation, **and** Runtime State roots.
- Shared RMED source: `CA-D-339@27`
  - Remaining Claim prose:
    the shared Project Work Journal **must** materialize its logical event table by serializing its ordered event Records as append-only NDJSON File Carrier segments **in** `.caprmedio_<project_name>/_journal/` **or** its registered subdirectories. these segments **must** remain Carriers of the same Journal, **not** separate Journals for Scope Units, Content Roles, workflows, **or** derived log views. describing the Journal as a table does **not** replace this registered serialization **or** require a database Carrier.

### `Carrier/File/Markdown` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Carrier/File` — CA-R-1957@11
  - `Carrier` — CA-R-1958@15
- Inherited Property Declaration refs; no child Property Node is created:
  - `Carrier/File.Extension` — CA-R-1974@12
  - `Carrier/File.Filename` — CA-R-1975@12
  - `Carrier/File.Path` — CA-R-1976@12
  - `Carrier/File.Filename.Scope Unit Token` — CA-R-2345@2
  - `Carrier/File.Format` — CA-R-2346@2
  - `Carrier/File.Main Content` — CA-R-2347@2
  - `Carrier/File.Main Content.CCE Operator` — CA-R-2348@2
  - `Carrier/File.Main Content.Paragraph` — CA-R-2349@2
  - `Carrier/File.YAML Frontmatter` — CA-R-2350@4
  - `Carrier/File.YAML Frontmatter.Scalar` — CA-R-2351@2
  - `Carrier.Canonical Address.Segment` — CA-R-1948@12
  - `Carrier.Canonical Address` — CA-R-1949@11
  - `Carrier.Format` — CA-R-1950@12
  - `Carrier.ID` — CA-R-1951@12
- Declaration source: `CA-R-2456@3`
  - Semantics:
    `Carrier/File/Markdown` is an Entity kind. Its `/` path expresses
    specialization and inheritance from `Carrier/File`; it is not a lexical
    Term hierarchy. Names in the path may reuse lexical Terms. The existing File Carrier definition
    supplies inherited File-Carrier structure, while the registered Markdown
    Format supplies Markdown encoding and interpretation rules.
    
    YAML Frontmatter is optional for a Markdown File Carrier under the existing
    File-region Rule. This definition therefore does not require YAML Frontmatter
    for every Markdown file. It does not define a filename, extension, identifier,
    section, field, lifecycle, or a separate Carrier for a Markdown region.
  - Remaining Claim prose:
    A Markdown File Carrier **means** a File Carrier whose Format is Markdown.
    
    ### Formal claim
  - Fenced Claim block:
```text
Carrier/File/Markdown
```
- Shared RMED source: `CA-D-663@2`
  - Remaining Claim prose:
    - Map heading ancestry to nested Content Properties.
    - The first heading may have any level.
    - Skipped levels create no empty Properties.
    - Fenced heading-like text creates no section.
    - Preserve the actual heading tree.

### `Carrier/File/Markdown/Markdown Atom Carrier` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Carrier/File/Markdown` — CA-R-2456@3
  - `Carrier/File` — CA-R-1957@11
  - `Carrier` — CA-R-1958@15
- Inherited Property Declaration refs; no child Property Node is created:
  - `Carrier/File.Extension` — CA-R-1974@12
  - `Carrier/File.Filename` — CA-R-1975@12
  - `Carrier/File.Path` — CA-R-1976@12
  - `Carrier/File.Filename.Scope Unit Token` — CA-R-2345@2
  - `Carrier/File.Format` — CA-R-2346@2
  - `Carrier/File.Main Content` — CA-R-2347@2
  - `Carrier/File.Main Content.CCE Operator` — CA-R-2348@2
  - `Carrier/File.Main Content.Paragraph` — CA-R-2349@2
  - `Carrier/File.YAML Frontmatter` — CA-R-2350@4
  - `Carrier/File.YAML Frontmatter.Scalar` — CA-R-2351@2
  - `Carrier.Canonical Address.Segment` — CA-R-1948@12
  - `Carrier.Canonical Address` — CA-R-1949@11
  - `Carrier.Format` — CA-R-1950@12
  - `Carrier.ID` — CA-R-1951@12
- Declaration source: `CA-R-2457@3`
  - Semantics:
    `Carrier/File/Markdown/Markdown Atom Carrier` is an Entity kind. Its
    `/` path expresses specialization and inheritance from Markdown File Carrier;
    it is not a lexical Term path. For an authoritative Markdown Atom Carrier,
    the existing Delivery policy requires YAML Frontmatter followed by Main
    Content. Existing Delivery policies govern the representation of an Atom's
    Role, Type, Status, and other applicable properties.
    
    The YAML Frontmatter and Main Content are existing logical regions of the File
    Carrier, not new per-section Carriers. This definition does not restate their
    field definitions, create identifiers or extensions, or define lifecycle
    behavior. It does not make YAML Frontmatter mandatory for Markdown File
    Carriers that do not represent Atoms.
  - Remaining Claim prose:
    A Markdown Atom Carrier **means** a Markdown File Carrier that represents an
    Atom.
    
    ### Formal claim
  - Fenced Claim block:
```text
Carrier/File/Markdown/Markdown Atom Carrier
```

### `Carrier/Git Branch` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Carrier` — CA-R-1958@15
- Inherited Property Declaration refs; no child Property Node is created:
  - `Carrier.Canonical Address.Segment` — CA-R-1948@12
  - `Carrier.Canonical Address` — CA-R-1949@11
  - `Carrier.Format` — CA-R-1950@12
  - `Carrier.ID` — CA-R-1951@12
- Declaration source: `CA-R-2200@5`
  - Semantics:
    A Git Repository contains its Git Branches. This is containment, not a narrower-kind relation.
  - Remaining Claim prose:
    A Git Branch **means** a repository-owned Carrier identifying a branch head.

### `Carrier/Git Commit` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Carrier` — CA-R-1958@15
- Inherited Property Declaration refs; no child Property Node is created:
  - `Carrier.Canonical Address.Segment` — CA-R-1948@12
  - `Carrier.Canonical Address` — CA-R-1949@11
  - `Carrier.Format` — CA-R-1950@12
  - `Carrier.ID` — CA-R-1951@12
- Declaration source: `CA-R-2199@5`
  - Semantics:
    Its native commit identity is interpreted within its repository context. Author, signer and source facts remain provenance.
  - Remaining Claim prose:
    A Git Commit **means** an immutable Carrier representing a committed repository snapshot and its commit metadata.

### `Carrier/Git Index` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Carrier` — CA-R-1958@15
- Inherited Property Declaration refs; no child Property Node is created:
  - `Carrier.Canonical Address.Segment` — CA-R-1948@12
  - `Carrier.Canonical Address` — CA-R-1949@11
  - `Carrier.Format` — CA-R-1950@12
  - `Carrier.ID` — CA-R-1951@12
- Declaration source: `CA-R-2202@5`
  - Remaining Claim prose:
    A Git Index **means** a Carrier representing a repository's staged-file snapshot.

### `Carrier/Git Repository` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Carrier` — CA-R-1958@15
- Inherited Property Declaration refs; no child Property Node is created:
  - `Carrier.Canonical Address.Segment` — CA-R-1948@12
  - `Carrier.Canonical Address` — CA-R-1949@11
  - `Carrier.Format` — CA-R-1950@12
  - `Carrier.ID` — CA-R-1951@12
- Declaration source: `CA-R-2203@6`
  - Semantics:
    A remote repository or branch on GitHub is another Carrier. Git Repository > Git Branch denotes whole/part containment. Local connection names and URLs describe how the repository is selected.
  - Remaining Claim prose:
    A Git Repository **means** a Carrier of versioned content and Git references.
    
    ### Formal claim
  - Fenced Claim block:
```text
Git Repository > @(Git Branch)
```

### `Carrier/Pull Request` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Carrier` — CA-R-1958@15
- Inherited Property Declaration refs; no child Property Node is created:
  - `Carrier.Canonical Address.Segment` — CA-R-1948@12
  - `Carrier.Canonical Address` — CA-R-1949@11
  - `Carrier.Format` — CA-R-1950@12
  - `Carrier.ID` — CA-R-1951@12
- Declaration source: `CA-R-2201@5`
  - Remaining Claim prose:
    A Pull Request **means** a repository-hosted Carrier of a proposed change and its review state.

### `Event Record` — primary_node

- Declaration source: `CA-R-2557@2`
  - Semantics:
    An Event Record is a persistent description of an event and its recorded evidence.
  - Remaining Claim prose:
    An Event Record is immutable.
  - Fenced Claim block:
```CFEL
Event Record {:0}((IS_PROPERTY_OF));
Event Record// {:1}((IS_CONTAINED_BY)) Journal//
```
  - Allowed Relations and other formal clauses:
    - `Event Record` — IS_PROPERTY_OF → `None`; Host=0; Target=undefined
    - `Event Record//` — IS_CONTAINED_BY → `Journal//`; Host=1; Target=undefined
- Shared RMED source: `CA-R-2567@2`
  - Remaining Claim prose:
    Event Records with action create or update describe accepted, completed business creations or updates. No-op, failed, unaccepted, archive and Carrier-only events do not use these actions.
    
    One accepted business update has one update Event Record.
    
    - Its change delta contains only changed logical Properties.
    - Atom.Content and all its descendants are excluded from Event Records for now.
    - Each recorded change identifies the Property by its complete path and records its old and new value or absence.
    - Promotion is an update; Version and Status are included when they change.
    - Updated At may be included when changed. Its new value follows the maximum of happened_at over accepted create and update Event Records for that object through this record’s happened_at.
    - This recorded copy is audit evidence. It does not supply that maximum or constitute another business update.
    - Carrier filename and directory changes are excluded from the delta.
    - A Carrier-only rename or move creates no update Event Record.
- Shared RMED source: `CA-R-2570@2`
  - Remaining Claim prose:
    - Event Record.happened_at is the time the recorded event happened.
    - Event Record.inserted_at is the time the record was added to its Journal.
    - Delayed insertion does not replace happened_at with inserted_at.
- Shared RMED source: `CA-R-2571@2`
  - Remaining Claim prose:
    An Event Record for Atom creation or update has object_output. An update record also has object_input; creation input is optional.
    
    For each present Atom input or output, the Event Record captures:
    
    - Atom.ID.
    - Atom.Version.
    - Atom.Updated At.
    
    object_input contains the values before the change. object_output contains the values after it. Their IDs may differ. The captured values remain as recorded.
- Shared RMED source: `CA-R-2584@2`
  - Remaining Claim prose:
    An Event Record for Projection creation or update has object_output. An update record also has object_input; creation input is optional.
    
    For each present Projection input or output, the Event Record captures:
    
    - Projection.ID.
    - Projection.Updated At.
    
    object_input contains the values before the change. object_output contains the values after it. Neither side contains a Version. The captured values remain as recorded.

### `Journal` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Declaration source: `CA-R-2536@2`
  - Semantics:
    A Journal preserves accepted event history.
  - Fenced Claim block:
```CFEL
Journal {:0}((IS_PROPERTY_OF));
Journal//{:1};
Journal >| (Container == yes);
Journal// {:0+}((CONTAINS)) Event Record//;
Journal ((NARROWER_THAN)) @Continuant
```
  - Nested Property contracts:
    - `Journal//` property; names=None; names count=1; values=None; values count=undefined
  - Allowed Relations and other formal clauses:
    - `Journal` — IS_PROPERTY_OF → `None`; Host=0; Target=undefined
    - `Journal >| Container == yes`
    - `Journal//` — CONTAINS → `Event Record//`; Host=0+; Target=undefined
    - `Journal` — NARROWER_THAN → `@Continuant`; Host=undefined; Target=undefined
- Shared RMED source: `CA-R-1491@29`
  - Remaining Claim prose:
    the Journal **must** preserve observable Project events independently of whether the recorded Project state conforms **to** Applicable Methodology.
    
    - append **and** read supplied observations **without** a Journal validation layer, required historical chain, canonical receipt, digest check, deduplication, retry **or** recovery gate. prior records are **not** prerequisites for a new entry.
    - Atom-ID grammar, filenames, placement, Properties, Relations **and** lifecycle conformance belong **to** separate Evaluations **and** their Tools; none is a Journal append/read gate.
    - preserve supplied observed values **without** silently repairing them **or** inventing an earlier event, baseline, Actor, session, time **or** result. log entries do **not** prove Project conformance **or** correct execution.
    - later Project changes **must not** prevent recording historical observations **or** rebind them **to** current state.
    - each explicit append records its supplied data, including repeated data; do **not** suppress it as a duplicate **or** overwrite existing entries.
    - retain ordinary authorized Project/filesystem access **and** truthful I/O failure. the Journal grants no permission **to** mutate a source, perform a Git effect **or** bypass access controls. existing records remain readable as recorded **without** migration.
- Shared RMED source: `CA-R-1684@28`
  - Remaining Claim prose:
    factual Journal Records carry what occurred, was measured, **or** was reported during execution **or** operation, with available provenance **and** context. their evidence **may** include logs, complaints, tickets, errors, execution outputs, measurements, delivery outcomes, **and** externally received operational reports.
    
    a factual Record does **not** explain causes, justify a choice, synthesize implications, **or** prescribe Spec **or** Operations authority.
    
    Analysis interprets Concerns, factual Records, Requirements, Methods, Evaluation, Delivery, Implementations, **or** Operations. it **may** compare alternatives, investigate causes, synthesize findings, explain implications, **and** provide rationale for a governed Claim.
    
    **when** one Carrier mixes factual input with interpretation, the factual Record **and** interpretive Analysis remain separate governed contributions with explicit references.
    
    factual execution Records **and** interpretive Analysis are **not** reusable Operations definitions.
- Shared RMED source: `CA-R-1712@27`
  - Remaining Claim prose:
    successful **and** failed release **or** deployment events, deployed environment state, runtime health, **and** incidents **must** be treated as operational facts whose execution evidence **and** state changes are carried by Journal Records. these facts **and** Records are distinct from reusable Operations definitions **and** **must not** themselves establish **or** silently change Plan, Requirement, Method, Evaluation, Delivery, **or** Operations authority.
- Shared RMED source: `CA-R-1720@38`
  - Remaining Claim prose:
    **every** Project **must** use **`=1`** authoritative Work Journal for **all** CAPRMEDIO-governed provenance events, including Artifact changes, Workflow Runs, Step Runs, Action executions, **and** Implementation lifecycle events. append supplied actual observations to that Project Journal and read them as recorded. each explicit append is an append, including repeated data; no canonical-once, deduplication, prior-history, chain, validation, receipt, retry or recovery prerequisite applies.
    
    Existing Journal entries remain unchanged and readable without migration or synthetic baselines. The Journal is a log of supplied observations, not permission or proof of source, lifecycle, Run or Git correctness; it does not promise historical replay or recovery. its logical event table does **not** require **`=1`** physical file **or** a database table; Carrier representation remains governed by Delivery authority.
- Shared RMED source: `CA-R-1743@26`
  - Remaining Claim prose:
    **every** execution outcome of a recurrence-protection mechanism **must** be carried by a Journal Record as execution evidence, distinct from the reusable Operations definition.
- Shared RMED source: `CA-E-464@24`
  - Remaining Claim prose:
    the Evaluation **must** reject a Core Meta-Model rule that makes Journal recording, replacement evidence, **or** either canonical log Projection depend on Git installation, commit topology, hooks, **or** commit messages.
    
    with no Git Extension selected, admitted Journal records **and** their Artifact Change Log **and** Process Log Projections **must** remain valid under their applicable authority. with the Git Extension selected, its commit references **may** add provenance but **must not** create a second authoritative event history. changing **or** removing secondary Git history **must not** destroy the recorded identity **and** evidence needed **to** rebuild the two logs. a missing **or** invalid authoritative Journal remains a failure **in** either case.
- Shared RMED source: `CA-E-476@23`
  - Remaining Claim prose:
    report a failed Evaluation **if** the Journal loses recordable evidence because of Project defects, accepts corrupted **or** unauthorized writes, silently changes observations, **or** rewrites accepted history.
- Shared RMED source: `CA-D-308@26`
  - Remaining Claim prose:
    **every** Journal Carrier **must** serialize its ordered Records append-only **in** its registered format **and** **must not** rewrite an admitted Record.
- Shared RMED source: `CA-D-549@19`
  - Remaining Claim prose:
    **all** persistent project-control Journal File Carriers of a Project **must** reside under **`=1`** Directory Carrier: `.caprmedio_<project_name>/_journal/`.
- Shared RMED source: `CA-D-559@17`
  - Remaining Claim prose:
    runtime technical **and** business Journals **may** be delivered **to** an explicitly configured local database, remote database, **or** governed logging sink. these Carriers **need not** reside under `.caprmedio_<project_name>/_journal/` **or** `.caprmedio_runtime/`.

### `MODEL` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Node` — CA-R-2462@2
- Declaration source: `CA-R-2559@2`
  - Semantics:
    MODEL declares Node kinds, Relations, Properties, and rules.
  - Remaining Claim prose:
    - A local MODEL inherits CAPRMEDIO's MODEL.
    - MODEL inheritance is distinct from Node narrowing.
    - Local overrides replace matching inherited rules in the local MODEL.
    - Local overrides preserve the base MODEL's rules.
    - Unmodified inherited Declarations are reused.
  - Fenced Claim block:
```CFEL
MODEL {:0}((IS_PROPERTY_OF));
MODEL >| (Container == yes);
MODEL ((NARROWER_THAN)) @Node
```
  - Allowed Relations and other formal clauses:
    - `MODEL` — IS_PROPERTY_OF → `None`; Host=0; Target=undefined
    - `MODEL >| Container == yes`
    - `MODEL` — NARROWER_THAN → `@Node`; Host=undefined; Target=undefined

### `Named Selection` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Declaration source: `CA-R-2587@2`
  - Semantics:
    A Named Selection names criteria for choosing members. Selected members retain their identity.
  - Fenced Claim block:
```CFEL
Named Selection {:0}((IS_PROPERTY_OF));
Named Selection ((NARROWER_THAN)) @Continuant
```
  - Allowed Relations and other formal clauses:
    - `Named Selection` — IS_PROPERTY_OF → `None`; Host=0; Target=undefined
    - `Named Selection` — NARROWER_THAN → `@Continuant`; Host=undefined; Target=undefined

### `Node` — primary_node

- Declaration source: `CA-R-2462@2`
  - Semantics:
    A Node can be the Host or Target of a Relation.
  - Fenced Claim block:
```CFEL
(Node, Node.**) {:0}((*));
(Node//, (Node//).**) {:0}((*));
Node {:0}((IS_PROPERTY_OF));
(Node, Node.**) {:0..1}((IS_PROPERTY_OF));
Node {:0+}((NARROWER_THAN)) Node;
Node {:0+}((HAS_NARROWER)) Node;
(Node, Node.**) {:0+}((HAS_PROPERTY)) Node.**;
Node// {:0+}((INSTANCE_OF)) Node;
Node {:0+}((HAS_INSTANCE)) Node//;
(Node//).** {:1}((IS_PROPERTY_OF)) (Node//, (Node//).**);
(Node//, (Node//).**) {:0+}((HAS_PROPERTY)) (Node//).**;
IF ((Node, Node.**) {=0}((IS_PROPERTY_OF)))
THEN ((Node, Node.**) >| (Independence == Primary Node));
IF ((Node, Node.**) {=1}((IS_PROPERTY_OF)))
THEN ((Node, Node.**) >| (Independence == Property))
AND ((Node, Node.**) {==0}((HAS_NARROWER)))
AND ((Node, Node.**) {==0}((HAS_INSTANCE)))
```
  - Allowed Relations and other formal clauses:
    - `(Node, Node.**)` — * → `None`; Host=0; Target=undefined
    - `(Node//, (Node//).**)` — * → `None`; Host=0; Target=undefined
    - `Node` — IS_PROPERTY_OF → `None`; Host=0; Target=undefined
    - `(Node, Node.**)` — IS_PROPERTY_OF → `None`; Host=0..1; Target=undefined
    - `Node` — NARROWER_THAN → `Node`; Host=0+; Target=undefined
    - `Node` — HAS_NARROWER → `Node`; Host=0+; Target=undefined
    - `(Node, Node.**)` — HAS_PROPERTY → `Node.**`; Host=0+; Target=undefined
    - `Node//` — INSTANCE_OF → `Node`; Host=0+; Target=undefined
    - `Node` — HAS_INSTANCE → `Node//`; Host=0+; Target=undefined
    - `(Node//).**` — IS_PROPERTY_OF → `(Node//, (Node//).**)`; Host=1; Target=undefined
    - `(Node//, (Node//).**)` — HAS_PROPERTY → `(Node//).**`; Host=0+; Target=undefined
  - Unresolved CFEL: `IF ((Node, Node.**) {=0}((IS_PROPERTY_OF)))
THEN ((Node, Node.**) >| (Independence == Primary Node))`
  - Unresolved CFEL: `IF ((Node, Node.**) {=1}((IS_PROPERTY_OF)))
THEN ((Node, Node.**) >| (Independence == Property))
AND ((Node, Node.**) {==0}((HAS_NARROWER)))
AND ((Node, Node.**) {==0}((HAS_INSTANCE)))`
- Shared RMED source: `CA-R-2474@2`
  - Remaining Claim prose:
    HAS_VALUE binds a Property on an instance to its admitted literal value. For example, the version Property of Atom instance CA-P-123 has value 1. The Property declaration supplies its value format, admitted domain and cardinality; the literal 1 is not a separately declared graph Node and requires no Declaration Atom.
    
    HAS_VALUE is a value binding rather than an ordinary Node-to-Node graph Relation. It must not create graph endpoints or independently authored inverse facts for literals. A Primary Node has no direct value. A Property on a Primary Node instance may hold direct values where its effective declaration permits them, including inherited Property declarations. Applying a declared Property to an instance does not instantiate that Property through HAS_INSTANCE or give its declaration another bearer.
- Shared RMED source: `CA-M-456@2`
  - Remaining Claim prose:
    - Choose names that distinguish their referents.
    - Avoid Entity, Type, Content or Value when they add no information.
    - Keep useful qualified and compound expressions.
    - Use one canonical Term per concept across prose, formal paths and YAML.
    - Do not introduce unnecessary synonyms or replace words globally.
- Shared RMED source: `CA-E-669@2`
  - Remaining Claim prose:
    A migration packet passes only when its selected Node inventory, predecessor dispositions, governing sources and consumer changes are explicit and independently reviewed. Reject incomplete or contradictory coverage; a prepared Draft is not an adopted Declaration.
- Shared RMED source: `CA-M-458@2`
  - Remaining Claim prose:
    Object means a Node instance.

### `Node/Continuant` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Node` — CA-R-2462@2
- Declaration source: `CA-R-2589@2`
  - Semantics:
    A Continuant persists as an identifiable thing.
  - Fenced Claim block:
```CFEL
Node/Continuant
```
  - Unresolved CFEL: `Node/Continuant`
- Shared RMED source: `CA-R-1502@25`
  - Remaining Claim prose:
    an Artifact's Authority, Applicability, **and** Currentness **must** remain distinct Properties under CA-R-1499, CA-R-1500, **and** CA-R-1501.
    
    - an authoritative Artifact **may** be inapplicable **to** a given context.
    - an applicable historical Revision **may** no longer be current.
    - a current Projection **may** accurately report state **without** possessing semantic authority.

### `Node/Occurrent` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Node` — CA-R-2462@2
- Declaration source: `CA-R-2590@2`
  - Semantics:
    An Occurrent is an actual occurrence unfolding in time. A record describes an occurrence; it is distinct from the occurrence itself.
  - Fenced Claim block:
```CFEL
Node/Occurrent
```
  - Unresolved CFEL: `Node/Occurrent`
- Shared RMED source: `CA-D-654@3`
  - Semantics:
    The Event remains the actual occurrence. Its Event Record is a distinct
    Continuant that may have a Carrier. CARRIES and its derived IS_CARRIED_BY view
    therefore apply to the represented non-ephemeral record rather than directly
    to the Occurrent.
  - Remaining Claim prose:
    An Occurrent is not carried or stored as the occurrence itself. When
    information about an Occurrent is retained, a Continuant record represents
    that information; the Carrier binds the Continuant record, not the Occurrent.
    An Event Record in a Journal is one such record.
    
    This reusable Policy governs Occurrent representation. It creates no new
    Carrier, per-occurrence binding, Journal record, or relation type.

### `PROJECT STRUCTURE` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Node` — CA-R-2462@2
- Declaration source: `CA-R-2560@2`
  - Semantics:
    PROJECT STRUCTURE describes the actual structure of a Project, including its Scope Units, Aspects, and other declared components.
  - Fenced Claim block:
```CFEL
PROJECT STRUCTURE {:0}((IS_PROPERTY_OF));
PROJECT STRUCTURE >| (Container == yes);
PROJECT STRUCTURE ((NARROWER_THAN)) @Node
```
  - Allowed Relations and other formal clauses:
    - `PROJECT STRUCTURE` — IS_PROPERTY_OF → `None`; Host=0; Target=undefined
    - `PROJECT STRUCTURE >| Container == yes`
    - `PROJECT STRUCTURE` — NARROWER_THAN → `@Node`; Host=undefined; Target=undefined

### `Package` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Declaration source: `CA-R-2525@2`
  - Semantics:
    A logical collection of implementation and documentation parts.
  - Fenced Claim block:
```CFEL
Package >| (Container == yes);
Package//{:0..1}((IS_CONTAINED_BY)) Package//;
Package//{:0+}((CONTAINS)) Package//;
IF (Package//$package not in (Package/Implementation//))
THEN ($package {==1}((IS_CONTAINED_BY)) Package//);
Package ((NARROWER_THAN)) @Continuant
```
  - Allowed Relations and other formal clauses:
    - `Package >| Container == yes`
    - `Package//` — IS_CONTAINED_BY → `Package//`; Host=0..1; Target=undefined
    - `Package//` — CONTAINS → `Package//`; Host=0+; Target=undefined
    - `Package` — NARROWER_THAN → `@Continuant`; Host=undefined; Target=undefined
  - Unresolved CFEL: `IF (Package//$package not in (Package/Implementation//))
THEN ($package {==1}((IS_CONTAINED_BY)) Package//)`
- Shared RMED source: `CA-R-2174@6`
  - Remaining Claim prose:
    Code **means** program instructions and definitions that realize behavior.
- Shared RMED source: `CA-R-1517@18`
  - Remaining Claim prose:
    **in** the caprmedio Project, a Tool's implementation reference **to** a methodology Action **or** Workflow definition **must not** target an O Atom owned by the Tool's Scope Unit **or** **any** descendant of that Scope Unit.
- Shared RMED source: `CA-R-1800@17`
  - Remaining Claim prose:
    **in** the caprmedio Project, **every** Tool **must** implement **`=1`** Action defined by an existing applicable methodology O Atom.
- Shared RMED source: `CA-E-488@23`
  - Remaining Claim prose:
    the Evaluation of a CAPRMEDIO Tool's methodology binding **must** check the canonical Action owner, binding cardinality, **and** division of Evaluation responsibility under CA-R-1515-PROJECT_CONFIGURATION-RULE--keep-canonical-actions-and-workflows-in-methodology, CA-R-1800-PROJECT_CONFIGURATION-RULE--bind-every-tool-to-one-methodology-action, CA-R-1517-PROJECT_CONFIGURATION-RULE--keep-tool-operational-authority-outside-its-own-subtree, **and** CA-R-1518-PROJECT_CONFIGURATION-RULE--separate-methodology-and-tool-evaluation-responsibilities.

### `Package/Implementation` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Package` — CA-R-2525@2
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Inherited Property Declaration refs; no child Property Node is created:
  - `Package.structural_level` — CA-R-2555@2
- Declaration source: `CA-R-2553@2`
  - Semantics:
    The root Package of a Project's implementation.
  - Fenced Claim block:
```CFEL
Package/Implementation;
Package/Implementation//{:1};
Package/Implementation// {:0}((IS_CONTAINED_BY)) Package//
```
  - Nested Property contracts:
    - `Package/Implementation//` property; names=None; names count=1; values=None; values count=undefined
  - Allowed Relations and other formal clauses:
    - `Package/Implementation//` — IS_CONTAINED_BY → `Package//`; Host=0; Target=undefined
  - Unresolved CFEL: `Package/Implementation`

### `Project` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Scope Unit` — CA-R-2523@2
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Inherited Property Declaration refs; no child Property Node is created:
  - `Scope Unit.ID` — CA-R-2526@2
  - `Scope Unit.Name` — CA-R-2527@2
  - `Scope Unit.Label` — CA-R-2528@2
  - `Scope Unit.Local Order` — CA-R-2529@2
  - `Scope Unit.Path` — CA-R-2530@2
  - `Scope Unit.Project Boundary Position` — CA-R-2531@2
  - `Scope Unit.structural_level` — CA-R-2554@2
- Declaration source: `CA-R-2524@2`
  - Semantics:
    A Project is the root Scope Unit.
  - Remaining Claim prose:
    A Project uses CAPRMEDIO's MODEL.
  - Fenced Claim block:
```CFEL
Scope Unit/Project;
Scope Unit/Project//{:1};
Project >| (Container == yes);
Project// {:0}((IS_CONTAINED_BY)) Scope Unit//;
Project ((NARROWER_THAN)) @Scope Unit
```
  - Nested Property contracts:
    - `Scope Unit/Project//` property; names=None; names count=1; values=None; values count=undefined
  - Allowed Relations and other formal clauses:
    - `Project >| Container == yes`
    - `Project//` — IS_CONTAINED_BY → `Scope Unit//`; Host=0; Target=undefined
    - `Project` — NARROWER_THAN → `@Scope Unit`; Host=undefined; Target=undefined
  - Unresolved CFEL: `Scope Unit/Project`
- Shared RMED source: `CA-R-047@34`
  - Remaining Claim prose:
    a CAPRMEDIO self-improvement cycle **must** keep the following participating contributions distinct **and** traceably related:
    
    - observations recorded **in** the Journal;
    - Analysis;
    - Tasks;
    - changes **to** Plan, Requirement, Method, Evaluation, Delivery, **and** Operations authority;
    - Implementation;
    - Delivery;
    - follow-up Evaluation.
    
    reusable Operations definitions remain distinct from the Journal Records of their executions **and** observations under CAPRMEDIO-META-REQU-092.
- Shared RMED source: `CA-R-053@26`
  - Remaining Claim prose:
    **before** CAPRMEDIO claims improvement, the governed improvement cycle **must** identify the exact target **and** baseline revision, evaluation frame, protected trade-offs, **and** continuation **or** stop condition.
- Shared RMED source: `CA-R-1486@20`
  - Remaining Claim prose:
    FRAMEWORK_METHODOLOGY **must** define how Projects are represented **and** operated.
- Shared RMED source: `CA-R-2448@3`
  - Remaining Claim prose:
    the CAPRMEDIO Framework Instance **must** keep **all** valuable Project information recoverable across sessions, handoffs, context loss, **and** Implementation changes.
- Shared RMED source: `CA-R-632@27`
  - Remaining Claim prose:
    **every** governed improvement cycle **in** caprmedio **must** declare **`=1`** primary target:
    
    - the CAPRMEDIO Framework Instance operating within caprmedio; **or**
    - the CAPRMEDIO Framework being developed as the caprmedio Project's output.
- Shared RMED source: `CA-R-819@36`
  - Remaining Claim prose:
    the CAPRMEDIO Framework Instance **must not** require **any** of the Operator's human participants **to** acquire specialist craft proficiency **or** personally perform specialist craft work **to** create, deliver, run, **or** maintain **any** feasible Project.
- Shared RMED source: `CA-M-005@28`
  - Remaining Claim prose:
    **to** govern the Project's mechanisms, admit **or** retain a mechanism **only** **when** the other admitted mechanisms cannot preserve a required outcome **or** a material governed distinction.
- Shared RMED source: `CA-M-006@31`
  - Remaining Claim prose:
    **to** govern the Project, keep its Terms, Claims, rules, structure, **and** Implementation mutually coherent **where** they share authority **or** interact.
- Shared RMED source: `CA-M-091@27`
  - Remaining Claim prose:
    **to** maintain reusable Project information, keep **only** the smallest information set sufficient **to** understand, govern, operate, **and** change the Project.
- Shared RMED source: `CA-M-093@23`
  - Remaining Claim prose:
    choose among acceptable alternatives by minimizing elapsed time from an Operator-accepted change intent **to** an Operator-accepted result according **to** the current Operator-declared velocity priority.
- Shared RMED source: `CA-M-096@24`
  - Remaining Claim prose:
    select which optional rules **and** rule groups are active for the affected scope **and** Project stage according **to** the current Operator-declared active-rule-set priority **without** disabling mandatory authority.
- Shared RMED source: `CA-M-296@21`
  - Remaining Claim prose:
    **to** preserve valuable information while developing caprmedio, keep that information recoverable from its proper Project Artifacts **without** depending on Agent memory **or** session continuity.
    
    - do **not** use `MEMORY.md`, similar memory files, conversation summaries, **or** handoff notes as governing authority **or** as the sole preserved copy of valuable information.
    - preserve accepted decisions, findings, rationale, **and** necessary evidence **in** their appropriate Artifacts under Applicable Methodology. keep governing Atoms, analysis, **and** factual Journal records distinct; preserving a finding does **not** make it accepted authority.
    - secondary summaries **may** help locate sources, but **must not** substitute for reading the relevant current sources **before** relying on their contents **or** claiming that work is complete.
    - **before** reducing context **or** handing work over, ensure that valuable information remains recoverable from those Artifacts. a later session **must not** need an earlier Agent's private memory **to** recover it.
    - missing, unavailable, **or** conflicting source information remains an explicit gap; do **not** fill it with remembered assertions. request Operator clarification **when** the unresolved gap prevents a sufficiently supported decision.
- Shared RMED source: `CA-M-446@3`
  - Remaining Claim prose:
    **to** govern the Project, reuse existing authority **and** canonical representations **without** independently maintaining duplicates for the same purpose **in** the same context.
- Shared RMED source: `CA-M-448@4`
  - Remaining Claim prose:
    **to** expose information for a task, preserve **all** information necessary for governed use, expose the complete currently justified sufficient information set for that task from the preserved information **and** nothing outside that set, **and** keep **all** unexposed preserved information recoverable.
- Shared RMED source: `CA-E-208@26`
- Shared RMED source: `CA-E-229@26`
  - Remaining Claim prose:
    the Operator controls **every** governed Project part outside the CAPRMEDIO Framework Instance, **and** **every** material change **to** those parts is observable, steerable, interruptible, **and** recoverable under the Operator's current authority.
- Shared RMED source: `CA-E-667@3`
  - Remaining Claim prose:
    the Principle **and** Core set Evaluation **must** return `fail` **if** a known Project-wide invariant has no canonical owner, a Principle is **only** a narrow application rather than a broad commitment, a required supporting Core Claim is absent, Claims conflict **or** independently duplicate authority **in** the same context, **or** an Atom has an incompatible Local Tier **or** Content Role; **otherwise**, it **may** return `pass` for the reviewed frontier **without** claiming that undiscovered gaps are impossible. evaluate Principle Content Roles under CA-E-482; the former Actor-policy interpretation of Plan does **not** create an exception **to** current Content Role authority. faithful Core specialization **must not** count as duplicate authority; fixed child counts, a universal RMED checklist per Principle, expansion from Intent, **and** formula/text equivalence **must not** be acceptance conditions. report missing support **and** conflicting owners **to** the Operator **without** silently selecting a winner.
- Shared RMED source: `CA-R-1759@37`
  - Remaining Claim prose:
    the Project Scope Unit **must** have **`=0`** parent Scope Units **and** Type: Unordered.
- Shared RMED source: `CA-R-1772@35`
  - Remaining Claim prose:
    CAPRMEDIO **must** use Project-scope Requirement authority plus its real Implementation as the minimum Project model, **must not** require an Implementation Atom, **and** **may** enable other Atom roles, applicability tiers, descendant scopes, **or** automation **only** **when** necessary. Scope Unit ancestry remains parent-declaration data; no Structural Level property is required.
- Shared RMED source: `CA-R-1776@38`
  - Remaining Claim prose:
    CAPRMEDIO **must** keep Structural ownership, scope inclusion, local order, normative authority, applicability tier, Subject classification, semantic control, dependency, realization, information **or** result flow, **and** lifecycle succession as distinct graph dimensions. a position **or** edge on one dimension **must not** create **or** substitute for a position **or** edge on another.
- Shared RMED source: `CA-R-2426@3`
  - Remaining Claim prose:
    CAPRMEDIO must preserve all irreducible governed invariants that apply across the entire current Project independently of Scope Unit ancestry, scope label, Content Role, Artifact form, Extension, Project Configuration or substrate. Those Project-wide foundational invariants retain their applicability throughout the Project; Project-owned Tier `0` Atoms express their foundational authority. This does not make every local or Project-owned Tier `0` Atom Project-wide, add a conflict winner based on Tier, or impose a fixed Role checklist.
- Shared RMED source: `CA-R-2427@2`
  - Remaining Claim prose:
    Every Project-wide foundational invariant must have exactly one active Project-owned Tier `0` Atom as its canonical authority owner. One such Atom may own several related invariants; this does not require one Atom per invariant or one Tier `0` Atom for the Project. Faithful specialization does not create independent duplicate authority.
- Shared RMED source: `CA-R-850@30`
  - Remaining Claim prose:
    the CAPRMEDIO Framework Instance **must not** be classified as an Actor.
- Shared RMED source: `CA-R-927@41`
  - Remaining Claim prose:
    **every** Project **must** be the Target Scope Unit of **`>=1`** accepted Requirement Atom of Type Project Goal. The Project Goal's current/local owner **must** be its Operator Actor, not the Project Scope Unit. This is the exception to ordinary Scope Unit ownership; the Operator **must not** be registered as a Scope Unit. Other Goal Atoms target non-Project Scope Units and use ordinary ownership.
- Shared RMED source: `CA-M-112@27`
  - Remaining Claim prose:
    **to** express CAPRMEDIO Project meaning, the Author **must** use English as the base language.
- Shared RMED source: `CA-D-317@27`
  - Remaining Claim prose:
    the Methodology **and** Tool governance of the CAPRMEDIO Framework Instance serving a Project **must** reside under that Project's `.caprmedio_<project_name>/000_CAPRMEDIO_framework/` Directory Carrier. this Carrier **must** contain that Project's Methodology Sources **and** Framework Instance Settings. another Project's Framework Instance **or** a repository-shared framework directory **must not** substitute for this Project's instance.
- Shared RMED source: `CA-R-1680@30`
  - Remaining Claim prose:
    CAPRMEDIO applies the same structural constitution **and** governance semantics **to** its own repository while keeping native reusable framework source, project authority, **and** non-authoritative convenience locators under distinct owners.

### `Projection` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Declaration source: `CA-R-2535@2`
  - Semantics:
    A Projection is a derived view of source Atoms. It does not establish or override their Claims.
  - Fenced Claim block:
```CFEL
Projection {:0}((IS_PROPERTY_OF));
Projection ((NARROWER_THAN)) @Continuant
```
  - Allowed Relations and other formal clauses:
    - `Projection` — IS_PROPERTY_OF → `None`; Host=0; Target=undefined
    - `Projection` — NARROWER_THAN → `@Continuant`; Host=undefined; Target=undefined
- Shared RMED source: `CA-R-1406@26`
  - Remaining Claim prose:
    materializing, refreshing, **or** deleting a Graph Projection **must not** establish, change, **or** remove Entity identity.
- Shared RMED source: `CA-R-1408@25`
  - Remaining Claim prose:
    The following interpretation is required when this governed concept is used:
    
    a Graph of Graphs **means** a composition of CAPRMEDIO Graphs connected through graph-qualified typed references **or** shared source identities. secondary graphs **in** this composition remain Projections under CA-R-1471-CORE_META_MODEL-CORE-REQUIREMENT--keep-secondary-graphs-derived-from-source-authority, **and** their internal, cross-graph, **and** authoritative-source connections remain governed by CA-R-1472-CORE_META_MODEL-GENERAL-REQUIREMENT--admit-typed-secondary-graph-connections.
    
    the composition does **not**, by itself, require another separately generated overview Artifact. **if** an overview is generated, its represented connections remain derived from the participating graphs **and** their sources **without** becoming another authority.
- Shared RMED source: `CA-R-1409@30`
  - Remaining Claim prose:
    When a General Artifact Graph Projection is produced, it represents Scope Units, Atoms (including Container Atoms), Journals and Projections from authoritative sources. Carrier locations and containment come from their governing declarations. A Directory Carrier is not made a Scope Unit or abstract model Object merely by existing on disk. The view is derived and creates no separate authority or obsolete Artifact/Structural Entity partition.
- Shared RMED source: `CA-R-1460@22`
  - Remaining Claim prose:
    the governing derivation logic of a Projection **must** remain distinct from its Carrier materialization strategy. whether **and** how its result is represented **or** persisted **in** Carriers does **not**, by itself, define the transformation **or** content-preservation behavior of that derivation, its semantic Type, **or** its refresh behavior; those remain determined by their applicable governing Claims. describing a derivation as direct **or** content-preserving does **not** select a persistence strategy.
- Shared RMED source: `CA-R-1463@26`
  - Remaining Claim prose:
    the Core Meta-Model **must** provide Artifact Change Log **and** Process Log as **`=2`** log Projection Types derived from the same Project Journal, under CA-R-1467@19-CORE_META_MODEL-DEFINITION--define-artifact-change-log-projection **and** CA-R-1468@20-CORE_META_MODEL-REQUIREMENT--define-process-log-projection. these Types organize recorded history **without** introducing independent Journals; additional Projection Types remain governed by the open Projection model.
    
    **every** represented historical fact **must** remain traceable **to** its canonical source event record **and** Event identity. the same source event **may** appear **in** both views **without** becoming two authoritative records. a read-only execution requires no fictitious Artifact change; membership **and** execution associations **must** come from recorded source evidence rather than invented events **or** inferred success. a view **must** remain rebuildable from its declared Journal selection, disclose known incomplete **or** stale source coverage **without** claiming complete current history, **and** obtain corrections through the owning source authority rather than independent log edits.
- Shared RMED source: `CA-R-1493@20`
  - Remaining Claim prose:
    a Projection's governed generator **or** generation procedure **and** declared configuration **must** identify how **to** rebuild that Projection.
- Shared RMED source: `CA-R-1494@20`
  - Remaining Claim prose:
    a Projection **must** record dependency provenance **only** **when** its registered job requires that information; no Projection is required **to** persist a blanket source frontier.
    
    this conditional recording obligation does **not** remove source traceability required by `CA-R-2535-CORE_META_MODEL-CORE-REQUIREMENT--define-projection-artifact-form` **or** a more specific admitted Projection specification.
- Shared RMED source: `CA-R-1507@19`
  - Remaining Claim prose:
    a Projection **may** refresh **only** **after** **every** declared source Atom exists.
- Shared RMED source: `CA-R-1567@25`
  - Remaining Claim prose:
    an Atom Collection **or** decomposition view grouping CAPO **or** I content **must** remain a derived grouping and **must not** acquire an Atom Tier or imply a Tier from its grouped Content Roles or Types. When a view displays a source Atom, it preserves that source Atom's numeric Tier; the grouping itself has no independent Tier.
    
    nesting expresses composition, **not** Core **or** General authority; a Plan Directory Carrier remains a Carrier of its existing Atom under CA-D-460-CORE_META_MODEL-ENG_DECISION--serialize-plan-atom-carrier-bundles, **not** an independently tiered collection **or** second Atom.
- Shared RMED source: `CA-R-1568@26`
  - Remaining Claim prose:
    a view Projection **may** be delivered as an Implementation output of its governing RMED **without** becoming an Atom **or** another source of truth for the facts it represents.
    
    - its output contribution is I; its Artifact kind remains Projection **and** its content remains derived from its declared sources.
- Shared RMED source: `CA-R-1593@25`
  - Remaining Claim prose:
    the Plan Graph **means** a Projection whose nodes reference authoritative Plan Atoms **and** whose graph-owned Relations represent Plan containment **and** blocking. explicit once-owned Plan Relation declarations are the sources of those facts; optional directory placement represents them **without** becoming another declaration.
- Shared RMED source: `CA-R-1609@22`
  - Remaining Claim prose:
    a representation inside a Projection **must** remain distinct from the Entity it represents.
    
    - depicting an existing Artifact **or** Scope Unit does **not** create another authoritative Artifact **or** Scope Unit.
    - a representation **may** identify a source Entity **or** a derived element admitted by the Projection specification; source identities **and** traceability remain governed by CA-R-2535.
    - this boundary introduces no separate Projection Element Term, lifecycle, **or** independently maintained authority.
- Shared RMED source: `CA-R-1649@33`
  - Remaining Claim prose:
    **every** Projection Rebuild **must** have **`=1`** Work Journal Action whose terminal Event records the rebuild outcome.
- Shared RMED source: `CA-R-1706@30`
  - Remaining Claim prose:
    CAPRMEDIO provides a non-authoritative lineage-impact Projection whenever an upstream Atom revision is changed, replaced, **or** archived. the Projection derives the reachable descendant set **without** modifying **or** retargeting **any** persisted relation.
    
    for **every** affected descendant, the Projection identifies the exact earlier revision **in** its lineage, the upstream event that triggered review, **and** the current disposition: review required, update the existing Atom, create a new Atom, archive the Atom, **or** confirmed compatible **without** change. unresolved descendants remain visible **until** disposition is recorded through governed history.
    
    the Projection **may** group **and** prioritize work, but it **must not** change an Atom, break a historical link, **or** establish compatibility merely by listing it.
- Shared RMED source: `CA-R-1728@27`
  - Remaining Claim prose:
    **every** Projection rebuild attempt **must** produce append-only Journal provenance from its start through **`=1`** terminal outcome, binding the target Projection, exact source Atom revisions **and** Journal records, generator, configuration, **and** produced revision **when** successful. Programmatic generation **and** LLM generation are provenance facts **only**; the two generation forms grant the Projection no authority.
- Shared RMED source: `CA-R-1749@26`
  - Remaining Claim prose:
    a derived view preserves **every** source's declared scope **and** **must not** inflate truth, completeness, evaluation, **or** priority by aggregating sources.
- Shared RMED source: `CA-R-2225@4`
  - Remaining Claim prose:
    Each focused Subject Graph Projection **must** state and use one declared selection. Scope Unit criteria select Current RMEDO source Atoms by their Local Scope Unit, with an explicit option to include descendants declared in Project Structure. Folder nesting does not determine the selected Scope Units. Subject-branch criteria select canonical target branches while retaining ancestor context and the source-backed properties needed for inheritance within the selected source set.
    
    Multiple selected Scope Units form a union; multiple selected branches form a union. When both criteria are supplied, both restrictions apply. With neither restriction, use all Current RMEDO sources. The Projection Type determines its view, not which sources are selected.
    
    For dependency-only results, compare exact Depends On and Governs paths inside the same selected source set. Do not silently consult sources outside that set to suppress entries. Namespace and Subject operator boundaries remain significant; a lexical prefix such as Atom must not also match AtomExtra.
- Shared RMED source: `CA-M-114@43`
  - Remaining Claim prose:
    **to** build a terminology list using the Catalog Type, the Generator **must** derive **every** Governed Term's name **and** Project-specific meaning from its active Method Atom of Type Term Definition. read the Term named by the defining Claim **and** verify that the Term Definition Atom's GOVERNS Subject Relation identifies its defined target under CA-R-1279-CORE_META_MODEL-RULE--govern-every-defined-term. inspect **every** named entity **and** named component of a Subject Path, **not** **only** its terminal component; extract **only** evidenced occurrences of reusable Project Terms. keep exact full entity names **and** source-admitted instance labels distinct from reusable Term occurrences; their spelling **or** position **in** a Subject Path alone does **not** classify them as Terms **or** require a Term Definition. obtain **every** evidenced reusable Term's meaning from that Term's own defining Claim, **not** by treating **all** path components as definitions supplied by the referencing Atom **or** inferring its meaning from Entity Definitions **or** their Semantics. include an entry **only** **when** its explicit Term Definition Claim establishes a Project-specific meaning; consistent use **or** capitalization alone does **not** supply defining authority. report uncertain Term classification **or** segmentation as unresolved; **do not** invent a definition, infer lexical authority from spelling, **or** silently resolve that uncertainty as ordinary vocabulary. exclude words **and** phrases used **only** with their ordinary English meanings. retain the source reference **without** classifying the direct Subject reference **or** a complete composite Subject Path as a Term **or** creating independent vocabulary authority.
- Shared RMED source: `CA-M-116@31`
  - Remaining Claim prose:
    **to** derive navigation values from an Atom Claim, the Generator **must** derive the concise human-readable Summary **when** creating the Atom **and** derive requested Translations directly from the Claim, **without** adding authoritative meaning. choose wording under CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning. for an existing Atom identity, retain **and** check the Summary under CA-R-1273-CORE_META_MODEL-CORE-REQUIREMENT--keep-summary-source-faithful **and** CA-R-1464-CORE_META_MODEL-REQUIREMENT--keep-summary-fixed-for-atom-identity rather than regenerating it as an independent Projection.
- Shared RMED source: `CA-M-231@34`
  - Remaining Claim prose:
    **to** derive an Atom's navigation values, derive them from authoritative content rather than another navigation value:
    
    - derive a new Atom's Summary from its finalized primary contribution within its applicability under CA-R-2499 **and** CA-M-442. for RMED, use Claim read within Scope, **not** Scope alone.
    - derive **every** requested Projection from its applicable complete source content, including relevant textual applicability restrictions, **not** from the Summary.
    - for an existing Atom identity, retain its Summary **and** check source faithfulness. a needed Summary change follows CA-R-1464 **and** **must not** be applied as a same-identity refresh.
- Shared RMED source: `CA-E-241@45`
  - Remaining Claim prose:
    **every** active **or** draft Atom **contains** **`=1`** human-readable precise CCE Claim **and** a source-faithful Summary. requested Translation **and** terminology Projections preserve their source meaning; their absence **when** **not** requested is **not** an Atom defect.
    
    ### Test case
    
    create valid active **and** draft Atom Claims for **every** admitted Content Role. include fixtures with no requested Translation **or** terminology Projection **and** fixtures with requested Projections. derive a candidate Summary during Atom creation, **then** retain it for checks of subsequent Revisions under CA-E-463-CORE_META_MODEL-EVAL_CASE--validate-summary-identity-preservation. derive requested Translation **and** terminology Projections twice **without** regenerating the existing Atom's Summary. **then** introduce ambiguity, an unstated participant, two independent Claims, an added Projection meaning, an independent vocabulary entry, **and** a confidence result below the effective Confidence Threshold resolved according **to** CA-M-271-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-confidence-thresholds-by-source-precedence.
    
    ### Acceptance criteria
    
    **every** valid fixture has **`=1`** precise interpretation, a source-faithful Summary, **and** reproducible Projections **when** requested. no fixture fails merely because an optional Projection was **not** requested. **every** invalid fixture fails. a confidence result below the effective Confidence Threshold leaves the Atom unchanged **and** requests Operator disposition. changing the applicable Operator input, Plan override, enclosing Hub override, **or** Framework Instance Settings default changes the checked threshold according **to** CA-M-271-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-confidence-thresholds-by-source-precedence **without** retaining a fixed percentage gate.
    
    ### Failure disposition
    
    record a Concern naming the affected Claim **or** Projection.
- Shared RMED source: `CA-D-635@16`
  - Remaining Claim prose:
    Use this filename:
    
    `<PROJECT_PREFIX>-PROJ-<ID>-<CURRENT_SCOPE_NAME>--<PROJECTION_TYPE>--<NAMED_SELECTION>.md`
    
    Store the full Projection ID as `projection_id` in YAML frontmatter. The filename and frontmatter must identify the same Projection.
- Shared RMED source: `CA-D-653@16`
  - Remaining Claim prose:
    Deliver each selected Subject Graph as a UTF-8 Markdown Projection Carrier under the Project's declared Projection root. The Carrier reuses the existing Projection identity, filename, timestamp, and source-list format while rendering the content defined by its exact registered Projection Type. This Delivery is Tier 3 in CORE_META_MODEL and delivers the Tier 1 definition CA-R-2150@15 in that same Scope Unit.
- Shared RMED source: `CA-D-665@2`
  - Fenced Claim block:
```CFEL
Projection// >> Carrier/Markdown_file//
```
  - Unresolved CFEL: `Projection// >> Carrier/Markdown_file//`

### `Scope Unit` — primary_node

- Transitive ancestor Declarations; their contracts are not copied:
  - `Node/Continuant` — CA-R-2589@2
  - `Node` — CA-R-2462@2
- Declaration source: `CA-R-2523@2`
  - Semantics:
    A Scope Unit defines a boundary of responsibility for Atoms.
  - Fenced Claim block:
```CFEL
Scope Unit >| (Container == yes);
Scope Unit//{:0..1}((IS_CONTAINED_BY)) Scope Unit//;
Scope Unit//{:0+}((CONTAINS)) Scope Unit//;
IF (Scope Unit//$unit not in (Scope Unit/Project//))
THEN ($unit {==1}((IS_CONTAINED_BY)) Scope Unit//);
Scope Unit ((NARROWER_THAN)) @Continuant
```
  - Allowed Relations and other formal clauses:
    - `Scope Unit >| Container == yes`
    - `Scope Unit//` — IS_CONTAINED_BY → `Scope Unit//`; Host=0..1; Target=undefined
    - `Scope Unit//` — CONTAINS → `Scope Unit//`; Host=0+; Target=undefined
    - `Scope Unit` — NARROWER_THAN → `@Continuant`; Host=undefined; Target=undefined
  - Unresolved CFEL: `IF (Scope Unit//$unit not in (Scope Unit/Project//))
THEN ($unit {==1}((IS_CONTAINED_BY)) Scope Unit//)`
- Shared RMED source: `CA-R-014@18`
  - Remaining Claim prose:
    CAPRMEDIO **must** support repository-level work **and** repository-relative Scope Units, including Scope Units using the `WORK_AREA` Label, containing code, services, libraries, documentation, methodology, data, **or** mixed content **without** requiring a particular architecture **or** deployability model.
- Shared RMED source: `CA-R-033@17`
  - Remaining Claim prose:
    a conflict between active Core Requirements on one ancestor–descendant path **must** preserve the ancestor-scope Core **and** reconcile the descendant-scope Core **without** changing the ancestor meaning.
- Shared RMED source: `CA-R-040@16`
  - Remaining Claim prose:
    **every** dependency between Project Layers **must** point from the Project root **or** an earlier Layer **to** a later Layer **in** the cumulative order.
- Shared RMED source: `CA-R-2444@3`
  - Remaining Claim prose:
    FIELD **must** collect inputs from other CAPRMEDIO users, including feedback, questions, suggestions, **and** problem reports.
- Shared RMED source: `CA-R-2450@3`
  - Remaining Claim prose:
    the ordered Project Layers are FRAMEWORK_METHODOLOGY at Local Order `1`, FRAMEWORK_ENGINE at `2`, OPERATOR_DOCUMENTATION at `3`, CORE_EXTENSIONS at `4`, **and** RELEASES at `5`.
- Shared RMED source: `CA-R-686@30`
  - Remaining Claim prose:
    CAPRMEDIO **must** govern core methodology authority, reusable Extension authority, **and** Project-specific Project Configuration authority as distinct strata **without** copying **or** silently transferring meaning among them.
- Shared RMED source: `CA-R-705@27`
  - Remaining Claim prose:
    the CAPRMEDIO Framework **must** comprise **all** outputs of the caprmedio Project delivered **to** the repository's root Implementation Folders. OPERATOR_DOCUMENTATION, CORE_EXTENSIONS, **and** RELEASES are downstream Project Layers; COMMUNITY_EXTENSIONS **and** FIELD are direct Project Features.
- Shared RMED source: `CA-R-709@27`
  - Remaining Claim prose:
    **every** CAPRMEDIO Feature is an `unordered_unit`, is owned by **=1** immediate Structural unit, **and** has no `local_order`.
- Shared RMED source: `CA-R-712@22`
  - Remaining Claim prose:
    **every** Project Layer is an immediate child of CAPRMEDIO **and** does **not** own another Project Layer's scope.
- Shared RMED source: `CA-R-775@21`
  - Remaining Claim prose:
    FIELD is an unordered direct child of caprmedio; it has no `local_order` **and** is **not** a Project Layer.
- Shared RMED source: `CA-R-1217@25`
  - Remaining Claim prose:
    an Extension **means** an immutable Methodology Source that adds authority within the Core Meta-Model's permitted expansion boundary under CA-R-1375-CORE_META_MODEL-CORE-REQUIREMENT--restrict-methodology-source-expansion-to-core-permission. specialization is admitted **only** **where** that boundary permits it **and** preserves applicable Core Meta-Model authority; unchanged Core Carrier bytes alone do **not** establish preservation.
- Shared RMED source: `CA-R-1219@32`
  - Remaining Claim prose:
    a Methodology Source **means** a Scope Unit selected as input **to** Applicable Methodology compilation.
- Shared RMED source: `CA-R-1220@26`
  - Remaining Claim prose:
    **every** Installed Extensions Catalog Entry **must** identify **`=1`** immutable Extension Candidate by stable Identity, Version, Author, Source, Source Version, Origin, **and** Content Digest.
- Shared RMED source: `CA-R-1264@26`
  - Remaining Claim prose:
    the Term Scope Unit **must not** be NARROWER_THAN Atom.
- Shared RMED source: `CA-R-1292@31`
  - Remaining Claim prose:
    **every** Scope Unit **must** remain the Claim Target Scope Unit of **`>=1`** accepted Goal Atom.
- Shared RMED source: `CA-R-1375@33`
  - Remaining Claim prose:
    an Extension **or** Project Configuration **must** add Claims, Terms, allowed values, Types, Methods, Evaluations, Deliveries, Operations, activation rules, compatibility rules, **or** priority rules **only** **where** one active CORE_META_MODEL Atom permits the addition **and** **must not** redefine, replace, shadow, weaken, delete, contradict, reinterpret, **or** mutate Core Meta-Model authority at **any** numeric Tier; an Atom's numeric Tier alone grants no exception **to** this source authority boundary.
- Shared RMED source: `CA-R-1484@22`
  - Remaining Claim prose:
    **every** non-Project Scope Unit **must** have **`=1`** declaration **in** its owning Project Structure that supplies its unique Name, direct parent, Type, Label, applicable Local Order, navigation number, **and** authority/Implementation Folder bindings. the declaration establishes the unit independently of Goal coverage **and** Carrier materialization; these remain separately evaluated conditions. Project Settings establishes the root identity, **and** Project Structure **must not** redeclare it as a child. Name/Order Atoms **and** concrete binding Atoms **must not** coexist as independent authorities for the same declared values.
- Shared RMED source: `CA-R-1656@28`
  - Remaining Claim prose:
    **every** Scope Unit except a Scope Unit root **must** have **`=1`** direct parent Scope Unit.
- Shared RMED source: `CA-R-1677@33`
  - Remaining Claim prose:
    the validator **must** validate **every** derived Ordered Scope Unit location **and** **every** of its components against the active authority defining the Scope Unit Path and Local Order. It **must not** treat a Structural Coordinate or persisted Structural Level field as an independent authority.
- Shared RMED source: `CA-R-1721@32`
  - Remaining Claim prose:
    the governing owner declares the structural scope set applicable **to** **every** structural scope. Scope sets **may** be identical, overlapping, **or** different across structural owners; reuse **or** correspondence **must** be explicit **and** cannot be inferred from matching labels alone.
- Shared RMED source: `CA-R-1722@31`
  - Remaining Claim prose:
    an Extension **must** provide a reusable, independently governed, optional package of capability contributions. its authority **and** evolution remain distinct from Core Meta-Model **and** Project Configuration authority.
- Shared RMED source: `CA-R-1723@26`
  - Remaining Claim prose:
    **every** Extension declares stable identity, version boundary, explicit extension points, compatibility obligations, **and** the canonical capabilities it adds **or** specializes **without** copying **or** redefining canonical authority.
- Shared RMED source: `CA-R-1730@39`
  - Remaining Claim prose:
    Scope Unit ancestry **must** follow declared Scope Unit parentage. CAPRMEDIO **must not** author or persist a Structural Level property; an optional derived depth or path rendering **must not** independently override that parentage under CA-R-1485.
    
    the Operator **may** choose **any** suitable Scope Unit Label, including `Layer`, `Feature`, `group`, `supergroup`, **or** `sub-feature`, **without** changing the unit's ancestry, authority, precedence, **or** Relation semantics. Labels **and** readability fields do **not** replace the active authority for those distinctions.
- Shared RMED source: `CA-R-1748@37`
  - Remaining Claim prose:
    applicable inherited authority **must** remain effective **in** a descendant Scope Unit **unless** that authority explicitly permits a specialization **and** the specialization stays within the permitted boundary.
    
    - the specialization **must not** change the parent meaning outside its declared descendant scope.
    - ancestor Core authority remains protected under CA-R-033; a child declaration **or** an override label does **not** grant permission **to** weaken it.
    - Extension **and** Project Configuration additions **must** also preserve Core Meta-Model authority at **every** numeric Tier under CA-R-1375-CORE_META_MODEL--restrict-methodology-source-expansion-to-core-permission. changing the descendant's numeric Tier **or** retaining unchanged Core Carrier bytes does **not** bypass that boundary. No Content-Role or Type-to-Tier restriction is introduced.
- Shared RMED source: `CA-R-1754@31`
  - Remaining Claim prose:
    an operator **may** promote a coherent reusable subset of Project Adaptation authority into a separately identified Extension while preserving exact source provenance **and** leaving the source Project Adaptation unchanged **until** explicit reconciliation.
- Shared RMED source: `CA-R-1762@35`
  - Remaining Claim prose:
    **every** Scope Unit **must** characterize its Project Boundary Position, Type value, **and** Child Composition independently. the Type value is required under CA-R-1758, including the Project's Unordered value under CA-R-1759.
- Shared RMED source: `CA-R-837@35`
  - Remaining Claim prose:
    the resolver **must** resolve **`=1`** direct Scope Unit from the Atom's internally carried ownership, checked against its canonical Carrier address, **or** from the registered canonical Carrier authority for a non-Atom Artifact **and** include that Artifact **in** **every** Scope Unit on the direct Unit's complete ancestor path; missing, multiple, unknown, **or** cyclic scope ownership is invalid.
- Shared RMED source: `CA-R-862@33`
  - Remaining Claim prose:
    **every** non-Project Scope Unit **must** have its authority place **and** Implementation Folder bound by its authoritative Project Structure declaration. concrete bindings **must not** be independently maintained **in** Delivery Atoms; applicable Delivery authority governs the representation, placement, **and** general Carrier conventions rather than repeating a unit's selected paths.
- Shared RMED source: `CA-R-917@34`
  - Remaining Claim prose:
    the CAPRMEDIO Metamodel **must** be fractal by applying the same Scope Unit governance pattern recursively at **every** Structural level.
- Shared RMED source: `CA-R-960@28`
  - Remaining Claim prose:
    Child Composition **means** the classification of one Scope Unit's direct children as **none**, LAYERS, FEATURES, **or** MIXED.
- Shared RMED source: `CA-R-964@29`
  - Remaining Claim prose:
    Unit **means** Scope Unit **when** CAPRMEDIO uses Unit as a governed shorthand.
- Shared RMED source: `CA-E-249@36`
  - Remaining Claim prose:
    a methodology expansion mapping Evaluation **must** return `fail` **if** a source element, exact canonical target, mapping rule, intended Scope, **or** applicable Core Meta-Model distinction at **any** numeric Tier is missing, canonical ownership is ambiguous, preservation is unproven, **or** the mapping redefines, replaces, shadows, weakens, deletes, contradicts, **or** reinterprets applicable Core Meta-Model authority at **any** numeric Tier; it **must** return `pass` **only** **when** the declared mapping preserves that authority **and** stays within its permitted expansion boundary. an Operator-approved loss **must not** count as conformance; report the failed boundary **and** leave the affected application stopped.
- Shared RMED source: `CA-D-445@22`
  - Remaining Claim prose:
    an explicit Scope Unit authority **or** Implementation Folder binding **in** Project Structure **may** select a native directory layout instead of the default Scope Unit directory convention. the binding **must** remain unambiguous, inside authorized path boundaries, distinct from another unit's exact authority binding, **and** explicit about its owning unit. a selected native layout **must not** change declared parentage, derived ancestry/path, Type, Local Order, **or** Name merely because its path has different nesting **or** numeric tokens. ordinary physical containment remains observable **without** becoming a second declaration of structural parentage.

### `Term` — primary_node

- Declaration source: `CA-R-1318@31`
  - Remaining Claim prose:
    A Term is a direct specialization of Entity at `Term`. A Term has one Name, the word or phrase used for its meaning. Its named instances initially form a flat set, using `Term//<Name>` without additional Term groups. This declares the vocabulary kind and its existing Name property; it does not implement the deferred Terms Graph.
    
    **every** instance of `Term` **must** represent a reusable word **or** phrase component of complete **or** qualified entity expressions **and** authored content whose approved Project-specific meaning remains consistent across **all** its uses.
    
    ### Formal claim
  - Fenced Claim block:
```text
Term
Term.Name[string]{1}
```
- Shared RMED source: `CA-R-1319@27`
  - Remaining Claim prose:
    a Governed Term **means** a reusable Term whose approved Project-specific meaning is owned by **`=1`** active Method Atom of Type Term Definition.
- Shared RMED source: `CA-R-1320@26`
  - Remaining Claim prose:
    a General Term **means** a word **or** phrase used with its ordinary English meaning rather than a Project-specific meaning.
- Shared RMED source: `CA-R-1347@29`
  - Remaining Claim prose:
    a Root Term **means** a Term with **`=0`** direct NARROWER_THAN parents **in** the Terms Graph.
- Shared RMED source: `CA-M-229@31`
  - Remaining Claim prose:
    **to** render CAPRMEDIO content, the Author **must** apply the following lexical-case rules:
    
    - start **every** Governed Term with a capital letter.
    - start **every** General Term with a lowercase letter.
    - preserve the lowercase spelling of **every** ordinary English word at the start of a sentence **or** list item **unless** an active rule requires an exact-case token.
    - preserve the required case of canonical Terms, Scope Unit Names, **and** exact registered references, including at sentence **and** list-item starts.
    - preserve the canonical spelling of **every** registered CCE Operator. use CA-D-280 for its representation **in** Markdown Atom Carrier Main Content.
- Shared RMED source: `CA-E-512@25`
  - Remaining Claim prose:
    **Claim checked.**
    
    **every** CCE Claim satisfies the lexical-case Method CA-M-229-CORE_META_MODEL-IMPLEMENTATION_METHOD--render-governed-terms-and-cce-operators-distinctly **and** the Markdown operator representation specified by CA-D-280-CORE_META_MODEL-ENG_DECISION--serialize-cce-operators-in-bold.

### `Actor.Name` — property

- Declaration source: `CA-R-2544@2`
  - Fenced Claim block:
```CFEL
Actor.Name{:0..1}: [string]{:1};
Actor.Name.*[]{:0}
```
  - Nested Property contracts:
    - `Actor.Name` property; names=None; names count=0..1; values=string; values count=1
    - `Actor.Name` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Atom.Content` — property

- Declaration source: `CA-R-2498@2`
  - Fenced Claim block:
```CFEL
Atom.Content{:1}: []{:0};
Atom.Content.*[string]{:0+};
Atom.Content.**[string]{:0+}: [markdown]{:1}
```
  - Nested Property contracts:
    - `Atom.Content` property; names=None; names count=1; values=; values count=0
    - `Atom.Content` immediate_dependents; names=string; names count=0+; values=None; values count=undefined
    - `Atom.Content` recursive_dependents; names=string; names count=0+; values=markdown; values count=1
- Shared RMED source: `CA-R-1203@32`
  - Remaining Claim prose:
    an Atom **must** be split **if** its Claim governs **`>1`** canonical Entities through GOVERNS Subject Relations.
- Shared RMED source: `CA-R-1270@24`
  - Remaining Claim prose:
    **if** **every** component of a logically composite Claim **must** be accepted, replaced, **and** retired together, **then** the composite Claim **must** remain one Claim.
- Shared RMED source: `CA-R-1271@29`
  - Remaining Claim prose:
    one Claim **may** express composite applicability restrictions as its Claim Scope through an explicitly grouped deterministic Scope Expression. the restrictions qualify the same Claim, **not** additional Claims **or** additional Claim Target Scope Units.
- Shared RMED source: `CA-R-1358@33`
  - Remaining Claim prose:
    multiple Claims with the same Atom Scope, Claim Target Scope Unit, textual Claim Scope, **and** Property X **must** be consolidated as **`=1`** Claim Value Set **if** they differ **only** by one allowed value of X.
- Shared RMED source: `CA-R-1359@28`
  - Remaining Claim prose:
    a Claim Value Set **means** one Claim expression **in** the form `X: (A, B, C)`, **where** X identifies **`=1`** Property **and** `(A, B, C)` identifies one finite unordered set of **`>=1`** unique canonical values allowed by X; the value order carries no authority, **and** the complete set **must** have one authority unit **and** lifecycle by accepting, replacing, **and** retiring **all** values together as one Claim.
- Shared RMED source: `CA-R-1417@31`
  - Semantics:
    Content is the Markdown portion whose natural-language meaning generally needs interpretation. Metadata properties use YAML. A complete RMED Content portion has its Claim as a direct Markdown value. A fenced CFEL expression may provide that value without prose. Do not create a separate Formal Claim child. Tools can extract sections or parse the supported formal syntax without proving all prose meaning.
    
    One Content portion is a structured group with zero direct scalar values and independently counted child properties. This introduces no generic Substance field. The retained Summary's word Revision means an Atom version, not a separate Revision entity.
  - Remaining Claim prose:
    Each Atom version **must** have exactly one Content portion.
- Shared RMED source: `CA-R-643@33`
  - Remaining Claim prose:
    **every** governed Claim **must** have **`=1`** authoritative Atom owner.
- Shared RMED source: `CA-R-940@33`
  - Remaining Claim prose:
    **every** Atom Claim **must** be readable by its intended human reader.
- Shared RMED source: `CA-R-941@29`
  - Remaining Claim prose:
    **every** Atom Claim **must** have **`=1`** precise interpretation.
- Shared RMED source: `CA-M-237@31`
  - Remaining Claim prose:
    **to** author one Claim Value Set, the Author **must**:
    
    1. identify **`=1`** Property X within **`=1`** Claim;
    2. write its finite allowed-value set as `X: (A, B, C)`;
    3. include **`>=1`** unique canonical values **and** treat their order as non-authoritative;
    4. retain the complete set as **`=1`** Claim **only** **if** **all** values **must** be accepted, replaced, **and** retired together;
    5. interpret `:` as Claim Value-Set syntax inside that Claim **and** as **`=1`** IS_ALLOWED_VALUE_OF relation **only** inside a Subject Expression.
- Shared RMED source: `CA-M-294@25`
  - Remaining Claim prose:
    **when** choosing wording for CAPRMEDIO content, the Author **must** choose words **and** phrases that are simpler **and** more familiar **to** the intended reader **when** they preserve the intended meaning **without** adding ambiguity.
- Shared RMED source: `CA-M-308@22`
  - Remaining Claim prose:
    **to** resolve one effective CCE Role Profile for one Atom Claim, the Author **must** perform **all** of:
    
    1. resolve the Atom's Content Role **before** selecting a profile.
    2. **if** the Content Role is Plan, Requirement, Method, Evaluation, Delivery, **or** Operations, select the corresponding profile under CA-M-309 through CA-M-314.
    3. apply an admitted Type profile **and** content-slot profile **after** the role profile; treat each narrower profile as a restriction **or** declared subordinate use, **not** as permission **to** change the role's primary contribution.
    4. distinguish operators that express the primary Claim contribution from operators inside a condition, Definition of Done, input, result, failure, transition, representation, **or** another governed subordinate slot.
    5. **if** the Content Role is Concern **or** Analysis, apply shared CCE **without** a role-specific profile.
    6. **if** the Content Role is Implementation, return no registered CCE Role Profile **without** selecting a fallback profile **or** reporting role-profile conformance.
    7. **if** the Content Role, Type, content slot, **or** applicable profile is unresolved, report the exact unresolved selection **and** do **not** report role-profile conformance.
- Shared RMED source: `CA-M-315@23`
  - Remaining Claim prose:
    **to** validate one Atom Claim against its effective CCE Role Profile, the Validator **must** perform **all** of:
    
    1. resolve the effective profile under CA-M-308 **without** inferring a different Content Role from the wording under review.
    2. identify the Claim's primary contribution, every subordinate content slot, **and** every registered CCE Operator occurrence.
    3. verify that the primary contribution matches the resolved role profile **and** that every narrower Type **or** content-slot contribution remains within its admitted boundary.
    4. verify that every CCE Operator use is permitted for its exact primary **or** subordinate context **and** has explicit logical scope.
    5. reject a primary contribution owned by another Content Role even **when** every individual CCE Operator is present **in** the global registry.
    6. for Concern **or** Analysis, validate shared CCE **and** their governed Content Role meaning **without** requiring a role-specific profile.
    7. for Implementation content, report that no CCE Role Profile is registered; do **not** apply another role's profile **or** report role-profile conformance.
    8. report every mismatch by Content Role, Type, content slot, primary contribution, **and** Operator occurrence. do **not** rewrite the source Claim **or** report conformance while one required classification remains unresolved.
- Shared RMED source: `CA-M-439@3`
  - Remaining Claim prose:
    **to** write a Term Definition, the Author **must** identify **`=1`** reusable word **or** phrase as its Term **and** write an explicit Claim that establishes that Term's meaning. state the Term's applicable meaning directly; do **not** substitute an inventory of entity uses, agreement among Entity Definitions **or** Semantics, a generated dictionary, **or** an inferred common substring for the defining Claim.
    
    write Claim Scope **to** state the definition's applicability **without** introducing an alternative meaning for the same Term **or** an exception **to** canonical full-name uniqueness. write Semantics **to** explain the declared meaning, necessary distinctions, **and** its consistent composition **when** clarification is needed; do **not** make Semantics the sole carrier of a missing defining Claim. write Details **to** record source support **and** explanatory examples **without** inventing a second authoritative meaning **or** an entity for a lexical component.
    
    express permitted reuse with the same Term meaning across different full canonical entity names. distinguish the reusable Term from the complete name that identifies **`=1`** canonical entity. outside the Term branch, a Term **must not** alone constitute the complete entity name; the Subject root `Entity` is the sole exception. use the complete admitted expression for every other such entity. preserve exact complete canonical names **in** **all** authored references **to** their entities; repeated references do **not** create entities **or** naming collisions.
    
    use the existing body headings **and** Method authoring conventions. write only the definition content **and** its source-backed explanations; this Method **must not** allocate an entity identity, admit a Relation Type by parsing, invent a part-of-speech schema, require a lookup table **or** Projection, **or** redefine identifier lifecycle semantics from example spelling.
- Shared RMED source: `CA-M-444@3`
  - Remaining Claim prose:
    **to** make an Atom Claim easy **to** understand, the Author **must** express **and** organize its content so the intended reader can identify what is claimed, what it concerns, **and** how its conditions **and** consequences fit together **without** guessing unstated connections.
- Shared RMED source: `CA-E-384@40`
  - Remaining Claim prose:
    the Evaluation **must** reject an Atom **if** **any** applicable content-boundary condition fails:
    
    - the Atom has **`!=1`** Claims, **`!=1`** resolved Claim Target Scope Units, an independently replaceable component inside **`=1`** Claim, ambiguous composite grouping, **or** a non-deterministic Scope Expression.
    - RMED Scope is missing its applicability description, merely repeats the carried current **or** target Scope Unit, introduces a second independently replaceable Claim, **or** conflicts with the Claim. applicability **must** be explicit **in** Scope rather than maintained independently **in** Claim **or** Details.
    - Details change, contradict, broaden, narrow, **or** add an independent contribution **to** the primary contribution within its applicability instead of expanding it under CA-R-2503-CORE_META_MODEL-DEFINITION--keep-details-within-the-primary-contribution.
    - Summary is **not** source-faithful **to** the finalized primary contribution under CA-R-2499-CORE_META_MODEL-CORE-REQUIREMENT--define-summary-as-an-atom-property **and** CA-R-1273-CORE_META_MODEL-CORE-REQUIREMENT--keep-summary-source-faithful, including its applicability restrictions. for RMED, use the Claim read within Scope; a Summary of Scope alone fails. a Summary sourced from Analysis Results **or** TLDR instead of Question fails this check.
    
    evaluate restrictions **to** selected sibling Scope Units under CA-E-461-CORE_META_MODEL-POLICY--warn-about-selected-sibling-claim-boundaries separately from these rejection criteria.
- Shared RMED source: `CA-E-402@31`
  - Remaining Claim prose:
    the Evaluation **must** reject a Claim Value Set **if** it identifies **`!=1`** Property, has **`=0`** values, repeats a value, uses one noncanonical value, has nonfinite **or** ordered semantics, **contains** one value **not** allowed by its Property, permits one value **to** be accepted, replaced, **or** retired independently, **or** parses `:` as Subject Expression syntax.
- Shared RMED source: `CA-E-403@34`
  - Remaining Claim prose:
    the Evaluation **must** report **`=1`** Claim Value Set consolidation candidate **only** **if** **every** contributing active Atom has the same Atom Scope, Atom Governed Subject, Claim Target Scope Unit, textual Claim Scope, Property, **and** exact qualifiers, has **`=1`** mechanically parseable single-value Claim, **and** differs **only** by **`=1`** unique value proven through IS_ALLOWED_VALUE_OF for that Property; it **must not** mutate, merge, archive, replace, compile, **or** change a Source Atom by another operation, use semantic **or** LLM inference, **or** cause Applicable Methodology compilation **to** fail.
- Shared RMED source: `CA-E-461@28`
  - Remaining Claim prose:
    **when** **`=1`** Atom Claim concerns **only** **`>=2`** selected sibling Scope Units **and** does **not** apply **to** their containing Scope Unit as a whole, the Evaluation **must** report a non-blocking boundary warning for review; that restriction alone **must not** make the Atom invalid **or** trigger automatic rejection, splitting, **or** retargeting **to** their parent.
- Shared RMED source: `CA-E-472@28`
  - Remaining Claim prose:
    wording evaluated under CA-M-294 fails **if** **any** of the following holds:
    
    - a demonstrated simpler, more familiar alternative preserves the intended meaning, but unnecessary jargon **or** specialized wording is retained.
    - a simplification removes **or** changes a necessary participant, obligation, permission, quantity, condition, boundary, **or** logical distinction.
    - a simplification adds ambiguity, substitutes a synonymous full name for an entity's complete canonical entity name, changes a component Term's declared meaning, **or** substitutes a synonym for a canonical CCE Operator **or** reference.
    - a simplified Summary adds **to**, broadens, narrows, **or** contradicts its source Claim **or** Claim Scope.
- Shared RMED source: `CA-D-495@25`
  - Remaining Claim prose:
    a Markdown Atom Carrier **must** carry the Claim's applicability **in** the registered body sections, **not** as a duplicate frontmatter value:
    
    - for ordinary RMED layouts, carry applicability **in** Scope, followed by the qualified contribution **in** Claim **and** supporting information **in** Details, using the exact headings registered by CA-D-479.
    - carry formal content in a CFEL fence within the Claim under CA-D-479. The Claim may contain CFEL without prose. Do not create a Formal Claim child or an operative frontmatter Claim.
    - for other Content Roles, retain applicability **in** their registered primary content. this rule does **not** change their body-section layouts.
    - an ordinary RMED Claim scope section **must** contain an applicability description, **not** just a copy of `current_scope_unit` **or** `claim_target_scope_unit`. those fields remain the carried structural references under CA-D-482.
    - carry the applicability restrictions **=1** time. in the ordinary RMED layout, Claim **and** Details are read within Claim scope; do **not** maintain a second scope declaration **in** either section **or** frontmatter.
- Shared RMED source: `CA-D-655@3`
  - Remaining Claim prose:
    an M/Term Definition **must** carry its Term spelling **and** authoritative meaning **in** its registered Claim section, **and** its applicable meaning boundary **in** Claim scope **when** required by the existing applicability authority. carry supporting distinctions **and** examples **in** Semantics **or** Details **when** applicable under the registered body layout. a review result **must** identify the selected Term Definition Atom **and** revision, checked source boundary **and** coverage, checked stage, affected Atom **and** revision, exact field occurrence **and** relevant context, assessed condition **and** result, **and** any conflict **or** uncertainty. distinct results for definition well-formedness, meaning ownership, occurrence consistency **and** coverage **must not** be collapsed **into** an unqualified pass. this evidence **must not** require a dictionary Projection, lookup index, new storage format **or** synthetic graph entity.

### `Atom.Content.Claim` — property

- Declaration source: `CA-R-2500@2`
  - Fenced Claim block:
```CFEL
Atom/(.Role in RMED).Content.Claim{:1}: [markdown]{:1};
Atom/(.Role in RMED).Content.Claim.*[]{:0};
FENCED_LABELS(Atom/(.Role in RMED).Content.Claim): [in (CFEL)]{:0..1}
```
  - Unresolved CFEL: `Atom/(.Role in RMED).Content.Claim{:1}: [markdown]{:1}`
  - Unresolved CFEL: `Atom/(.Role in RMED).Content.Claim.*[]{:0}`
  - Unresolved CFEL: `FENCED_LABELS(Atom/(.Role in RMED).Content.Claim): [in (CFEL)]{:0..1}`
- Shared RMED source: `CA-R-1682@41`
  - Remaining Claim prose:
    applicable Active Requirement, Method, Evaluation, **and** Delivery Atoms across **all** Governance loci collectively form the Project's normative Spec for governed Entities, including Change content **and** Implementation; particular Change content, actual realizations, **and** execution evidence remain distinct from the specification governing them.
- Shared RMED source: `CA-M-460@2`
  - Remaining Claim prose:
    - Keep the Claim on its active Subject.
    - Prefer positive statements that preserve the constraint.
    - Use ancestor rules for inherited constraints.
    - Reuse applicable shared rules.
    - State a permission when it changes an applicable restriction.

### `Atom.Content.Claim Scope` — property

- Declaration source: `CA-R-2501@2`
  - Fenced Claim block:
```CFEL
Atom/(.Role in RMED).Content.Claim Scope{:0..1}: [markdown]{:1};
Atom/(.Role in RMED).Content.Claim Scope.*[]{:0}
```
  - Unresolved CFEL: `Atom/(.Role in RMED).Content.Claim Scope{:0..1}: [markdown]{:1}`
  - Unresolved CFEL: `Atom/(.Role in RMED).Content.Claim Scope.*[]{:0}`

### `Atom.Content.Details` — property

- Declaration source: `CA-R-2503@2`
  - Fenced Claim block:
```CFEL
Atom/(.Role in RMED).Content.Details{:0..1}: [markdown]{:1};
Atom/(.Role in RMED).Content.Details.*[string]{:0+}
```
  - Unresolved CFEL: `Atom/(.Role in RMED).Content.Details{:0..1}: [markdown]{:1}`
  - Unresolved CFEL: `Atom/(.Role in RMED).Content.Details.*[string]{:0+}`

### `Atom.Content.Semantics` — property

- Declaration source: `CA-R-2502@2`
  - Fenced Claim block:
```CFEL
Atom/(.Role in RMED).Content.Semantics{:0..1}: [markdown]{:1};
Atom/(.Role in RMED).Content.Semantics.*[]{:0}
```
  - Unresolved CFEL: `Atom/(.Role in RMED).Content.Semantics{:0..1}: [markdown]{:1}`
  - Unresolved CFEL: `Atom/(.Role in RMED).Content.Semantics.*[]{:0}`

### `Atom.Content.Summary` — property

- Declaration source: `CA-R-2499@2`
  - Fenced Claim block:
```CFEL
Atom.Content.Summary{:1}: [markdown]{:1};
Atom.Content.Summary.*[]{:0};
DETERMINES(
  Atom//,
  (.ID),
  (.Content.Summary),
  (Atom.Status >| Status Group = Current) OR (Atom.Status >| Status Group = Archived)
)
```
  - Nested Property contracts:
    - `Atom.Content.Summary` property; names=None; names count=1; values=markdown; values count=1
    - `Atom.Content.Summary` immediate_dependents; names=; names count=0; values=None; values count=undefined
  - Unresolved CFEL: `DETERMINES(
  Atom//,
  (.ID),
  (.Content.Summary),
  (Atom.Status >| Status Group = Current) OR (Atom.Status >| Status Group = Archived)
)`
- Shared RMED source: `CA-R-1273@32`
  - Remaining Claim prose:
    a Summary **must** preserve the intent **and** applicability of its finalized primary contribution under CA-R-2499, **without** adding, broadening, narrowing, **or** contradicting its contribution. brevity **may** omit supporting detail, but **must not** change what the Atom is about **or** add a conclusion absent from that contribution. for ordinary RMED, source faithfulness is evaluated against the Claim read within its Scope, **not** against either section alone.
- Shared RMED source: `CA-R-1274@29`
  - Remaining Claim prose:
    an Atom's primary content block, remaining Main Content, Claim restrictions, **or** Translation **must not** be reconstructed **or** validated from its Summary. Summary is derived navigation, **not** authority for the content it abbreviates.
- Shared RMED source: `CA-R-1418@28`
  - Remaining Claim prose:
    **every** Atom **must** have **`=1`** Summary for navigation, derived from its finalized primary contribution within its applicability under CA-R-2499 **without** independent authority.
- Shared RMED source: `CA-R-1464@22`
  - Remaining Claim prose:
    an Atom **must** keep the Summary created with it across **all** of its Revisions. **if** its Summary needs a change, **then** it **must** be replaced by a new Atom with a new Atom ID, even **if** its Claim is unchanged.
- Shared RMED source: `CA-E-463@23`
  - Remaining Claim prose:
    the Evaluation **must** reject a candidate Atom Revision **if** its Summary differs from the Summary established for that Atom identity, even **when** its Claim is unchanged. it **must** reject treating Summary as an independently identified, versioned, **or** timestamped Artifact; Summary belongs **to** its Atom under CA-R-2499.
- Shared RMED source: `CA-D-282@26`
  - Remaining Claim prose:
    **every** Atom Filename Summary Slug **must** be the lowercase ASCII kebab-case serialization of the complete Atom Summary.
- Shared RMED source: `CA-M-459@2`
  - Remaining Claim prose:
    Write Atom.Content.Summary to cover the Atom's complete contribution.

### `Atom.Form` — property

- Declaration source: `CA-R-2495@2`
  - Fenced Claim block:
```CFEL
Atom.Form{:1}: [string]{:1};
Atom.Form.*[]{:0}
```
  - Nested Property contracts:
    - `Atom.Form` property; names=None; names count=1; values=string; values count=1
    - `Atom.Form` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Atom.ID` — property

- Declaration source: `CA-R-2493@2`
  - Fenced Claim block:
```CFEL
Atom.ID{:1}: [string]{:1};
Atom.ID.*[]{:0};
IF ((Atom.Status >| Status Group = Current) OR (Atom.Status >| Status Group = Archived))
THEN (IMMUTABLE(Atom.ID))
```
  - Nested Property contracts:
    - `Atom.ID` property; names=None; names count=1; values=string; values count=1
    - `Atom.ID` immediate_dependents; names=; names count=0; values=None; values count=undefined
  - Unresolved CFEL: `IF ((Atom.Status >| Status Group = Current) OR (Atom.Status >| Status Group = Archived))
THEN (IMMUTABLE(Atom.ID))`
- Shared RMED source: `CA-M-276@29`
  - Remaining Claim prose:
    **to** repair accidental reuse of an assigned Project Atom ID, an AI Agent **must** perform **all** of:
    
    1. identify the distinct source Atoms by exact Carrier address, Revision, **and** recorded history. distinguish accidental reuse from legitimate Revisions of the same Atom **and** derived copies of its Carrier.
    2. establish the original valid owner from recorded assignment history. **if** the original owner cannot be established at the effective Confidence Threshold, request an Operator decision for that collision **before** changing its identities **or** references. filename order, discovery order, current filesystem timestamps, **or** the highest Version **must not** select the owner.
    3. preserve the original owner's Atom ID. give **every** later accidental reuse the next unreused Project-wide number for its own Content Role under CA-D-450-CORE_META_MODEL-DELIVERY--number-project-owned-atoms-within-each-content-role, using the encoding under CA-D-378-CORE_META_MODEL-DELIVERY--serialize-assigned-atom-identities. this corrects invalid reuse **and** does **not** authorize changing a valid owner's immutable identity.
    4. preserve **every** affected Atom's Claim, Content Role, Atom Scope, Claim Target Scope Unit, **and** textual Claim Scope. preserve its immutable prior Revisions **and** recorded history; record the exact predecessor-to-corrected-identity mapping **in** the existing Work Journal **without** rewriting historical Carriers **or** Records.
    5. resolve **every** affected current reference against its intended Atom using the reference's context **and** recorded history. update references **only** **when** their intended targets are established; request an Operator decision for unresolved references. do **not** replace the ambiguous ID indiscriminately.
    6. verify that the repaired active identities resolve uniquely **and** **every** affected current reference still identifies its intended Claim **before** declaring the collision repaired. keep unrelated Claims **and** identities unchanged.
    7. perform repair as an explicitly authorized source change, **not** as an automatic side effect of lookup **or** compilation. preserve CA-D-336-CORE_META_MODEL-DELIVERY--resolve-active-atoms-from-canonical-carrier-identities's failure on ambiguous lookup **until** source repair is complete, **and** regenerate affected Projections from their corrected sources through their existing governed workflows.
- Shared RMED source: `CA-E-448@30`
  - Remaining Claim prose:
    the Evaluation **must** reject completion of an Atom ID collision repair under CA-M-276-CORE_META_MODEL-IMPLEMENTATION_METHOD--repair-accidental-atom-id-reuse **if** **any** of:
    
    - the original owner was selected **without** sufficient recorded assignment evidence **or** the required Operator decision, **or** its valid Atom ID changed.
    - a later accidental reuse retains the colliding ID, receives a previously used number, **or** receives an ID outside its Project prefix **and** Content Role sequence.
    - an affected Claim, Content Role, Atom Scope, Claim Target Scope Unit, **or** textual Claim Scope changes beyond the approved identity-reference correction, a distinct Claim is lost **or** merged, **or** an unrelated identity changes.
    - a prior Revision **or** historical Record is rewritten, history becomes unreachable, **or** the Work Journal lacks the exact mapping between the historical Carrier **and** its corrected identity.
    - an affected current reference resolves ambiguously, remains unresolved, **or** resolves **to** a different intended Claim; an uncertain reference is rebound **without** the required Operator decision.
    - legitimate same-Atom Revisions **or** derived copies are renumbered as accidental reuse, **or** lookup **or** compilation silently selects an identity winner.
    
    the Evaluation **must** distinguish a paused collision awaiting an Operator decision from a completed repair. its checks **must** cover the verified-original-owner case, reversed Carrier discovery order, an unknown original owner, an ambiguous incoming reference, **and** legitimate same-Atom Revisions **or** derived copies.
- Shared RMED source: `CA-D-378@27`
  - Remaining Claim prose:
    **every** assigned Current or Archived Atom ID **must** begin with the registered uppercase Project identity prefix. the canonical Project-owned Atom ID encoding **must** match `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-<GLOBAL_NUMBER_WITHIN_CONTENT_ROLE>`. Every Draft Atom **must** carry a Draft-only `atom_id` marker: `<canonical-ID>@<proposed-version>-draft` for a proposed revision of an existing Atom, or `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-draft` for a new Atom; `@<proposed-version>-draft` occurs once in the ID and matching Draft filename identity segment. A Draft marker is permitted on a Draft source, not a Current source. The role-only new-Atom marker allocates no canonical number. For Archived predecessors, qualify the Atom-ID filename segment and `atom_id` as `<canonical-ID>@<old-version>` exactly once, preserving its numeric Version and Updated At; do not require an exact-byte archive carrier. the Atom Content Role Identity Letter **must** be **in** (Concern: C, Analysis: A, Plan: P, Requirement: R, Method: M, Evaluation: E, Delivery: D, Operations: O). a `<PROJECT_PREFIX>-P` Identifier **must** identify a Plan Atom, including one labeled Epic, **and** **must not** identify a separate non-Atom collection.
- Shared RMED source: `CA-D-446@28`
  - Remaining Claim prose:
    For each canonical Atom ID, at most one Current Atom source **may** exist across all admitted Status values. Every Current or Archived Atom version **must** be identified by exactly one canonical Atom ID and Version Number; Archived versions **may** retain that ID at distinct Version Numbers. Every Draft Atom **must** carry one `atom_id` marker form specified by CA-D-378; a Current source uses the canonical ID. An Archived predecessor is identified by its canonical ID qualified once with its unchanged numeric Version, with `status: Archived` and its prior Updated At retained; Git history preserves exact pre-archive bytes.
    
    - for a Current or Archived Atom version, carry the canonical Atom ID as the top-level String `atom_id` **and** Version Number as `version`; their pair identifies one Atom version **without** another `identifier` field. A Draft carries only the explicit marker allowed by the Claim and CA-D-378.
    - a Draft Carrier **must** carry `atom_id` using only the Draft marker forms admitted by CA-D-378. These forms do not change the Current Atom ID uniqueness rule.
    - when an identified Atom is changed to Draft, its Draft Carrier carries the corresponding Draft marker admitted by CA-D-378; the marker and filename remain governed by CA-D-378 and CA-D-650. Do **not** create a second concurrent Draft Carrier for that Status edit.
    - when a Current Atom changes, create an Archive Carrier for the predecessor with its qualified ID, `status: Archived`, unchanged numeric Version and old Updated At; the Current successor retains the canonical ID, advances Version from N to N+1, and receives actual edit time under CA-R-1432/CA-R-1788. An exact no-op retains Version/time. There is no demotion Version exception.
    - a Draft carrying `<canonical-ID>@<proposed-version>-draft` for an existing Atom proposes an update to that same canonical Atom at the marker's proposed Version. For an actual update, that Version must be the current canonical Version plus one under the existing version-advance rule; archive the current canonical predecessor with its old numeric Version, Updated At and unrelated content, and update that Atom, subject to exact-current, identity/collision, Summary/replacement, Type/Status, schema and permission rules. An exact no-op retains the existing Version/time and creates no predecessor archive. This same-canonical rule does not determine promotion behavior for the role-only new-Atom marker.
- Shared RMED source: `CA-D-508@19`
  - Remaining Claim prose:
    **every** identified Project-owned Atom **must** receive the next unreused number from the Project-wide sequence for its Content Role.
- Shared RMED source: `CA-D-568@19`
  - Remaining Claim prose:
    Draft identity continuity **must** follow the exact admitted target and the applicable identity rules; retained Draft history **must not** be a prerequisite for Create, Update, promotion, another admitted Status change or their success.
    
    - do **not** require, reconstruct, register, resolve or validate a `revision_lineage.history_entry_ref`, unique Draft head, origin chain, direct retained-history parent, pending head reservation or consuming successor before an otherwise admitted effect. A manually authored Draft is not refused merely because those records are absent, incomplete, malformed or unavailable.
    - Draft `atom_id` presence and marker form follow CA-D-378 and CA-D-446; Draft filename identity-segment serialization follows CA-D-650. Do **not** restore a former assigned Identity from an archive, lineage/origin metadata, Journal, prior tool demotion or another historical record. Preserve real historical identities without releasing them for reuse. Ordinary Content Role, Summary/replacement, identity/collision, expected-target/currentness, permission and Carrier/schema checks remain applicable; absence of retained Draft history is not itself an identity conflict.
    - When a Current Atom revision is updated, preserve the predecessor's old numeric Version, Updated At and unrelated content while archiving it with `status: Archived` and the version-qualified identity; exact pre-archive bytes remain in Git history. Do **not** fabricate a Create event, origin, earlier Draft admission, head, parent or successor to make the current operation admissible. A Summary change still follows the admitted replacement rule.
    - Journal existence, completeness, continuity, baseline, prior entry or receipt **must not** gate these effects or their success. Attempt to append supplied actual observations independently; report an actual append failure as a diagnostic without invalidating a completed mutation or replaying its effects.

### `Atom.Label` — property

- Declaration source: `CA-R-2497@2`
  - Fenced Claim block:
```CFEL
Atom.Label{:0..1}: [string]{:1};
Atom.Label.*[]{:0};
Atom.Label ?= Atom.Form
```
  - Nested Property contracts:
    - `Atom.Label` property; names=None; names count=0..1; values=string; values count=1
    - `Atom.Label` immediate_dependents; names=; names count=0; values=None; values count=undefined
  - Unresolved CFEL: `Atom.Label ?= Atom.Form`

### `Atom.Relations` — property

- Declaration source: `CA-R-2507@2`
  - Fenced Claim block:
```CFEL
Atom.Relations{:1}: []{:0};
Atom.Relations.*[Relation//]{:0+}
```
  - Nested Property contracts:
    - `Atom.Relations` property; names=None; names count=1; values=; values count=0
    - `Atom.Relations` immediate_dependents; names=Relation//; names count=0+; values=None; values count=undefined
- Shared RMED source: `CA-R-030@26`
  - Remaining Claim prose:
    a scope **in** strict authority mode **must** maintain a complete, conflict-free active PRMEDO authority topology with these constraints:
    
    - **every** local Tier 0 Atom **and** Core has **`>=1`** permitted active child **unless** the applicable Type authority registers its Type as terminal;
    - the normative-authority subgraph is acyclic under CA-R-833;
    - **every** edge follows the tier **and** structural-direction rules applicable **to** its graph kind **and** Relation Kind; **and**
    - an Active RMED Atom's direct relation **to** an RMED Atom requires an Active target under CAPRMEDIO-GOV-REQU-767. other endpoint classes retain the Status constraints of their own governing Relation authority.
    
    the authority-subgraph acyclicity constraint does **not** impose acyclicity on **every** other graph, including Workflow control flow.
- Shared RMED source: `CA-R-037@27`
  - Remaining Claim prose:
    **in** strict authority mode, **every** active tier-classified PRMEDO Atom **must** have **`>=1`** permitted active parent **unless** the applicable Type authority registers its Type as orphan-permitted.
    
    a permitted parent is:
    
    - the active Project Goal Atom for a Project-owned Tier 0 Atom;
    - an applicable lower-global-tier Atom **in** the same structural scope, or a Tier 0 Requirement for a same-Scope Tier 0 Method, Evaluation, Delivery, or Operations Atom when the applicable typed relation admits it; **or**
    - an Atom permitted by the global tier topology **in** an ancestor structural scope.
    
    this parent-coverage condition is necessary but insufficient for authority-topology completeness **and** cannot establish Project Scope Contract completeness.
- Shared RMED source: `CA-R-038@16`
  - Remaining Claim prose:
    a scope **in** casual authority mode **may** contain active PRMEDO Core **and** Standard Atoms **without** permitted active parents **and** **may** omit permitted active children.
- Shared RMED source: `CA-R-1686@33`
  - Remaining Claim prose:
    the change propagates **only** forward through the ordered layer graph. it:
    
    1. identifies affected downstream Projections, Methods, Evaluation criteria, Delivery rules, Implementations, **and** Operations consumers;
    2. marks **every** affected downstream artifact potentially stale **without** mutating historical atoms;
    3. routes required reconciliation **to** the artifact's owning layer; **and**
    4. closes **only** **when** **every** affected currentness **or** evaluation gate reaches its required disposition.
- Shared RMED source: `CA-R-2149@14`
  - Semantics:
    A verified Project Goal uses its Target Project, while its owner remains the Operator Actor; ordinary endpoints use their Local Scope Unit. Apart from the explicitly stated equal-Tier-0 exception, the numeric comparison and strict-ancestor rule are unchanged. The exact Project Configuration → Core Meta-Model prerequisite alternative is the logical-role declaration in CA-R-1218@31; it does not authorize the reverse, another source-role pair, a transitive edge, or a relation from a containing Project or Methodology Sources Scope Unit.
  - Remaining Claim prose:
    Each stored governing RMED relation must target an Atom in the same ordering Scope Unit at a strictly lower numeric Tier or satisfy the narrow Tier 0 exception below, an Atom in a strict ancestor ordering Scope Unit, or the Core Meta-model prerequisite of Project Configuration explicitly declared by CA-R-1218@31. The prerequisite exception is one-way and non-transitive. Other descendant and sibling targets are forbidden. Unresolved membership, endpoint, Tier or Scope evidence does not pass. A verified Project Goal uses its Target Project for this ordering check; its owner remains the Operator.
    
    As a narrow exception, within the same Local Scope Unit, a Tier `0` Method, Evaluation, Delivery or Operations source may target a Tier `0` Requirement only through a stored typed governing relation already admitted for those endpoints by its defining declaration. Equal Tier `0` does not otherwise pass: it does not admit Requirement-to-Requirement, Requirement-to-M/E/D/O, or M/E/D/O-to-M/E/D/O links. This exception creates no Relation Kind or Operations relation admission and does not establish an automatic conflict winner.
    
    These constraints apply to the source-declared Selection “Stored Governing RMED Relation Occurrences”, not to arbitrary context or history links. There is no automatic conflict winner based on Tier, timestamp or these ordering rules.

### `Atom.Relations.contained_by` — property

- Declaration source: `CA-R-2490@2`
  - Fenced Claim block:
```CFEL
Atom.Relations.contained_by{:0..1}: []{:0};
Atom.Relations.contained_by.*[in(atom,scope_unit)]{:1}
```
  - Nested Property contracts:
    - `Atom.Relations.contained_by` property; names=None; names count=0..1; values=; values count=0
    - `Atom.Relations.contained_by` immediate_dependents; names=in(atom,scope_unit); names count=1; values=None; values count=undefined

### `Atom.Relations.contained_by.atom` — property

- Declaration source: `CA-R-2491@2`
  - Fenced Claim block:
```CFEL
Atom.Relations.contained_by.atom{:0..1}: [atom id]{:1};
Atom.Relations.contained_by.atom.*[]{:0}
```
  - Nested Property contracts:
    - `Atom.Relations.contained_by.atom` property; names=None; names count=0..1; values=atom id; values count=1
    - `Atom.Relations.contained_by.atom` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Atom.Relations.contained_by.scope_unit` — property

- Declaration source: `CA-R-2492@2`
  - Fenced Claim block:
```CFEL
Atom.Relations.contained_by.scope_unit{:0..1}: [scope unit]{:1};
Atom.Relations.contained_by.scope_unit.*[]{:0}
```
  - Nested Property contracts:
    - `Atom.Relations.contained_by.scope_unit` property; names=None; names count=0..1; values=scope unit; values count=1
    - `Atom.Relations.contained_by.scope_unit` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Atom.Role` — property

- Declaration source: `CA-R-2494@2`
  - Fenced Claim block:
```CFEL
Atom.Role{:1}: [string]{:1};
Atom.Role.*[]{:0}
```
  - Nested Property contracts:
    - `Atom.Role` property; names=None; names count=1; values=string; values count=1
    - `Atom.Role` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Atom.Status` — property

- Declaration source: `CA-R-2488@2`
  - Fenced Claim block:
```CFEL
Atom.Status{:1}: [string]{:1};
Atom.Status.*[]{:0};
Atom.Status: Draft;
Atom.Status: Active;
Atom.Status: Archived
```
  - Nested Property contracts:
    - `Atom.Status` property; names=None; names count=1; values=string; values count=1
    - `Atom.Status` immediate_dependents; names=; names count=0; values=None; values count=undefined
  - Allowed values:
    - `Atom.Status: Draft`
    - `Atom.Status: Active`
    - `Atom.Status: Archived`
- Shared RMED source: `CA-R-1308@27`
  - Remaining Claim prose:
    a global Status value domain **must not** override the Status domain resolved from the complete qualified path of an Artifact Type **or** Atom Content Role **and** Type.
- Shared RMED source: `CA-R-1312@28`
  - Remaining Claim prose:
    an Artifact Revision Status value **must** remain distinct from the Action **or** Workflow whose execution **may** establish that value.
- Shared RMED source: `CA-R-1313@27`
  - Remaining Claim prose:
    an Extension **or** Project Configuration **may** add Status values **and** transition rules **only** under one exact complete qualified Artifact Type **or** Atom Content Role **and** Type path.
- Shared RMED source: `CA-R-1412@24`
  - Remaining Claim prose:
    **every** Atom **must** have **`=1`** Status.
- Shared RMED source: `CA-R-1610@25`
  - Remaining Claim prose:
    RMED Claims reconstructed from existing Implementation **or** its Projections **must** remain proposed Draft Claims **until** accepted through the applicable Atom acceptance authority.
    
    - extraction **or** inference alone does **not** establish Active authority.
    - the accepted RMED, **not** the legacy Implementation **or** its Projection, governs subsequent refactoring **and** Evaluation of the result.
- Shared RMED source: `CA-R-1947@13`
  - Remaining Claim prose:
    Atom.Status **must** admit (Draft, Active, Archived). Narrower Atom kinds inherit these values and **may** add allowed values under their applicable Content Role or Type. An inherited value does **not** require a separate declaration for every narrower kind.
- Shared RMED source: `CA-D-483@23`
  - Remaining Claim prose:
    **every** Atom Revision **must** carry **`=1`** explicit `status` value **in** its own Markdown frontmatter.
    
    - the value **must** belong **to** the applicable Content Role **and** Type Status model.
    - placement **must** agree under CA-D-466 **and** its specific Delivery rules; it is **not** a second Status source.
    - another Revision **or** a containing Hub **must not** override this Revision's carried Status.
    
    - encode `status` as **=1** nonempty YAML string using the exact value admitted by the selected Status model. do **not** accept a list, null, **or** another Revision's value as this Revision's Status.

### `Atom.Subjects` — property

- Declaration source: `CA-R-2545@2`
  - Fenced Claim block:
```CFEL
Atom.Subjects{:1}: []{:0};
Atom.Subjects.*[in(Active,Passive)]{:0..2}
```
  - Nested Property contracts:
    - `Atom.Subjects` property; names=None; names count=1; values=; values count=0
    - `Atom.Subjects` immediate_dependents; names=in(Active,Passive); names count=0..2; values=None; values count=undefined
- Shared RMED source: `CA-R-1202@30`
  - Remaining Claim prose:
    **every** direct GOVERNS value **and** **every** direct DEPENDS_ON value **in** an Atom's Subjects Property **must** resolve **to** **`=1`** canonical Subject Target. resolution **must not** require an intermediate Subject/Entity **or** Subject/Reference Property **or** a repeated target-kind field.
- Shared RMED source: `CA-R-1275@32`
  - Remaining Claim prose:
    An Atom.Subjects target must name the thing or topic the Atom governs or depends on; it is not a copied target, intermediate Subject object, or a requirement for a separate entity kind.
- Shared RMED source: `CA-R-1276@25`
  - Remaining Claim prose:
    **every** direct reference **in** an Atom's Subjects Property **must** use **`=1`** Relation Kind **in** (GOVERNS, DEPENDS_ON). the relation entry supplies this kind **without** an additional kind Property on a Subject object.
- Shared RMED source: `CA-R-1278@23`
  - Remaining Claim prose:
    **every** Atom **may** declare **`>=0`** distinct direct DEPENDS_ON targets **in** its Subjects Property.
- Shared RMED source: `CA-R-1597@20`
  - Remaining Claim prose:
    an Atom's Subject Paths **must** identify the Subject Targets of its Subject Relations **without** substituting those paths for its owning Scope Unit **or** its Claim Target Scope Unit.
- Shared RMED source: `CA-R-2004@14`
  - Remaining Claim prose:
    A direct GOVERNS or DEPENDS_ON target in Atom.Subjects must be the topic addressed by a canonical Entity-rooted Subject expression and may identify a kind, axis, property, allowed value, or named instance.
- Shared RMED source: `CA-R-2100@8`
  - Remaining Claim prose:
    An Atom **may** have zero or one direct GOVERNS Subject Relation. No Atom's Subjects **may** contain more than one direct GOVERNS Subject Relation.
- Shared RMED source: `CA-M-125@47`
  - Remaining Claim prose:
    **to** assign an Atom's Subjects, the Author **must** perform **all** of:
    
    1. read the entire Markdown Main Content, including Summary, Scope, Claim, Details, other registered sections, nested headings, tables, examples, **and** reference labels. build an inventory of canonical Subject Target mentions with exact locations **and** full resolved paths. treat an Atom citation label rendered under `CA-M-444-CORE_META_MODEL-IMPLEMENTATION_METHOD--atom-claims-expose-their-meaning-conditions-and-consequences-clearly` as the referenced Atom's complete filename **without** its `.md` extension **or** directory path. under `CA-R-1280-CORE_META_MODEL-RULE--reference-every-prerequisite-subject-through-depends-on`, the label is readable reference evidence, **not** a Subject Target mention **or** Subject target, including **when** it occurs **in** the same sentence as Subject Target language; inventory a Subject Target **only** **when** surrounding prose independently uses it.
    
       recognize an evidenced reusable Term through its authoritative Method Atom of Type Term Definition, including the lexical Term `Term` at `Term//Term`. `Evaluation` remains a Term **when** used inside an Evaluation Atom. use structural definitions, such as `CA-R-1318-CORE_META_MODEL-DEFINITION--define-term` for the Term kind and `CA-R-2514-CORE_META_MODEL-DEFINITION--define-evaluation-content-role` for the Evaluation Content Role, together with the usage context to resolve the referenced Entity target; those structural definitions do **not** replace the lexical meaning owner. self-reference alone does **not** remove a mentioned Subject Target from the inventory **or** establish a new Subject Target; a Term's spelling alone does **not** establish its Subject target. a source-admitted instance name after `//`, a selector literal, **or** syntax is **not** automatically a reusable Term. retain unresolved meaning as an explicit gap rather than treating it as ordinary wording.
    2. select the **`=1`** canonical Subject Target that the Claim governs **and** reference its narrowest exact Subject Path directly through GOVERNS.
    
       - for a Claim about entry **or** exit criteria of a Property, apply this same narrowest-target rule rather than substituting its wider bearer.
       - **when** the Atom has Content Role Evaluation **and** its Claim defines a conformance check, select the canonical target whose conformance is checked; do **not** select a generic Evaluation label **or** the execution of the check merely from its Content Role. bind the checked authority separately with `evaluation_for` under `CA-R-1018-CORE_META_MODEL--register-evaluation-targets`.
    3. connect **every** other Subject Target **in** the mention inventory through DEPENDS_ON using its narrowest exact full Subject Path. include mentions outside Claim; do **not** repeat GOVERNS **or** add unmentioned Subject Targets. unresolved mentions block completion rather than disappearing from the inventory.
    4. for a definition Claim, use its defined Term **in** the Subject Path that identifies the target being defined, under `CA-R-1279-CORE_META_MODEL-RULE--govern-every-defined-term`. resolve evidenced reusable lexical components through their Method Term Definitions, while resolving a name after `//` through its instance-naming and source authority rather than automatically requiring a Term Definition; the path identifies the target **and** the GOVERNS link is the Subject Relation. the path does **not** define its component Terms.
    5. split the Atom **before** assignment **when** the Claim governs **`>1`** canonical Subject Targets.
    6. verify that the distinct GOVERNS **and** DEPENDS_ON targets equal the mention inventory. record **every** reference once **without** creating an intermediate Subject object, repeating definitions, **or** treating path components **and** implicit bearer prefixes as separate Subject Target mentions.
    7. serialize the direct references under `CA-D-269-CORE_META_MODEL-DELIVERY--serialize-atom-subjects-in-frontmatter`. its migration-limited legacy compatibility preserves existing temporal carrier evidence; it does **not** add temporal nesting **to** a migrated flat Carrier.
- Shared RMED source: `CA-E-246@47`
  - Remaining Claim prose:
    **every** valid Atom has zero **or** one GOVERNS Subject Target matching its Claim **and** DEPENDS_ON for **every** other Subject Target independently mentioned **in** its complete Markdown Main Content; an Atom citation label is **not** a Subject Target mention **or** Subject target, and the distinct target set **`=`** that mention inventory **without** an intermediate Subject object.
- Shared RMED source: `CA-D-269@28`
  - Remaining Claim prose:
    For Markdown Atom carriers, encode `subjects` as a mapping with one scalar nonempty Entity path under `active` and zero or more unique nonempty Entity paths as a YAML sequence under `passive`. An omitted `passive` means zero. The grouping mapping has no direct value; its child values are counted separately. A Draft may be incomplete before promotion.
    
    Preserve the decoded Entity paths exactly under the applicable notation and resolve targets under the applicable Subject rules. A defining Atom may introduce its target and path together. Do not add an intermediate reference object or a repeated target-type field. YAML quotes are not part of the decoded expression; preserve escapes and reference boundaries. Each YAML key occurs once within its own mapping. Preserve formal cardinality annotations and decoded Entity escapes exactly; do not serialize notation as extra YAML fields.
    
    The canonical keys are `active` and `passive`. Existing `governs` and `depends_on` remain readable during carrier migration. Mixed old and new aliases with unequal values are invalid. Equal aliases can be read during transition, without asserting additional Subjects.

### `Atom.Subjects.Active` — property

- Declaration source: `CA-R-2546@2`
  - Fenced Claim block:
```CFEL
Atom.Subjects.Active{:0..1}: [string]{:1};
Atom.Subjects.Active.*[]{:0};
IF (Atom.Status >| Status Group = Current)
THEN (Atom.Subjects.Active{==1})
```
  - Nested Property contracts:
    - `Atom.Subjects.Active` property; names=None; names count=0..1; values=string; values count=1
    - `Atom.Subjects.Active` immediate_dependents; names=; names count=0; values=None; values count=undefined
  - Unresolved CFEL: `IF (Atom.Status >| Status Group = Current)
THEN (Atom.Subjects.Active{==1})`

### `Atom.Subjects.Passive` — property

- Declaration source: `CA-R-2506@2`
  - Remaining Claim prose:
    Passive Subjects identify direct contextual dependencies.
  - Fenced Claim block:
```CFEL
Atom.Subjects.Passive{:0..1}: [string]{:0+};
Atom.Subjects.Passive.*[]{:0};
COUNT(Atom.Subjects.Passive: $) = COUNT(DISTINCT Atom.Subjects.Passive: $)
```
  - Nested Property contracts:
    - `Atom.Subjects.Passive` property; names=None; names count=0..1; values=string; values count=0+
    - `Atom.Subjects.Passive` immediate_dependents; names=; names count=0; values=None; values count=undefined
  - Unresolved CFEL: `COUNT(Atom.Subjects.Passive: $) = COUNT(DISTINCT Atom.Subjects.Passive: $)`

### `Atom.Tier` — property

- Declaration source: `CA-R-2504@2`
  - Remaining Claim prose:
    Goals whose active Subject resolves to the Project use Tier -1. Ordinary Scope Unit-owned non-Goal Atoms use Tier 0 or higher.
  - Fenced Claim block:
```CFEL
Atom.Tier{:1}: [int]{:1};
Atom.Tier.*[in(Label)]{:0..1};
Atom.Tier >= -1
```
  - Nested Property contracts:
    - `Atom.Tier` property; names=None; names count=1; values=int; values count=1
    - `Atom.Tier` immediate_dependents; names=in(Label); names count=0..1; values=None; values count=undefined
  - Unresolved CFEL: `Atom.Tier >= -1`
- Shared RMED source: `CA-R-025@16`
  - Remaining Claim prose:
    a conflict between active Requirements at different global tiers **must** preserve the lower-numbered claim **and** reconcile the higher-numbered claim **without** changing the lower-numbered meaning.
- Shared RMED source: `CA-R-1669@28`
  - Remaining Claim prose:
    an Implementation Method qualified under CA-R-1767 **must** receive its numeric Tier from its complete Claim and current Scope Unit under CA-M-438; reusability alone **must not** force a particular Tier. Tier admission **must not** impose a Content-Role or Type-to-Tier restriction.
- Shared RMED source: `CA-R-1710@29`
  - Remaining Claim prose:
    Concern priority, Plan blocking, **and** Atom numeric Tier **must** remain distinct coordinates; **every** non-Project-Goal Atom's numeric Tier cardinality follows CA-R-2125 regardless of its Content Role, **without** turning a Concern priority **or** a Plan Work Sequence Number into a numeric Tier. No Content-Role or Type-to-Tier restriction is introduced.
- Shared RMED source: `CA-R-2125@10`
  - Remaining Claim prose:
    **every** non-Project-Goal Atom **must** carry exactly one integer Tier. An ordinary Atom owned by a Scope Unit uses an integer Tier **>=0**. Project Goal is the separate explicit Tier `-1` case under CA-R-2132.
    
    This rule defines owner-relative ranges, not a finite set of values. Higher integers remain admissible and may be assigned or raised when required by the approved governing-relation ordering. No Content-Role or Type-to-Tier restriction is imposed.
- Shared RMED source: `CA-R-2131@10`
  - Remaining Claim prose:
    a non-Project Scope Unit **must** admit an integer Tier **>=0** for every ordinary Atom it owns. Higher integer Tiers remain admissible without an upper bound and may be assigned or raised when required by the approved governing-relation ordering.
    
    This range rule imposes no Content-Role or Type-to-Tier restriction.
- Shared RMED source: `CA-R-2132@12`
  - Remaining Claim prose:
    Every Requirement Atom of Type Project Goal **must** target the Project, be owned by its Operator Actor instead of a Local Scope Unit, and carry exactly one numeric Tier `-1`. Tier `-1` is explicit, is not omitted, and is outside the ordinary nonnegative Tier range. This Rule does not impose an arbitrary Type-to-Tier restriction beyond verified Project Goal identity and ownership.
- Shared RMED source: `CA-R-2424@2`
  - Remaining Claim prose:
    A Scope Unit’s local foundational commitments are expressed by its Atoms at numeric Tier `0`, whose readable Tier Label is Scope Contract. Tier `0` applies to Project and non-Project Scope Units. Each Atom retains its Content Role and Type, including existing Operations Types such as Workflow, Action and Step. Tier `1` and above specializes or realizes the local foundational commitments. This rule does not require an Atom for every Content Role or exactly one Tier `0` Atom for a Scope Unit. The external Project Goal retains its Operator Actor owner and its separately governed Tier `-1`.
- Shared RMED source: `CA-R-2428@2`
  - Remaining Claim prose:
    a Scope Unit in the Project **must** admit an integer Tier **>=0** for every ordinary Atom it owns. The explicit Project Goal case carries Tier `-1` under CA-R-2132. Higher integer Tiers remain admissible without an upper bound and may be assigned or raised when required by the approved governing-relation ordering.
    
    This range rule imposes no Content-Role or Type-to-Tier restriction.
- Shared RMED source: `CA-M-438@17`
  - Remaining Claim prose:
    to derive one Current R/M/E/D Atom's integer Tier, the Author **must**:
    
    1. resolve the complete Atom Claim and actual owner. For an ordinary endpoint resolve its Local Scope Unit; for a verified Operator-owned Project Goal resolve its Target Project as the ordering context under CA-R-2149, without changing its Actor owner. Resolve declared ancestry for these contexts;
    2. select only stored governing RMED relation occurrences under CA-R-2148@10. The source endpoint **must** be a Current R/M/E/D Atom, and the target endpoint **may** be any Current Atom permitted by that relation's endpoint definition;
    3. preserve a valid existing integer Tier. Ordinary Scope Unit-owned Atoms use Tier **>=0**, and a verified Project Goal uses exactly Tier **-1**;
    4. for each selected same-Scope occurrence, require the target Tier to be strictly lower than the source Tier, except that an admitted typed governing relation from a same-Scope Tier 0 Method, Evaluation, Delivery, or Operations Atom to a Tier 0 Requirement is allowed; for a target in a strict ancestor Scope Unit, accept the occurrence without comparing Tiers; for a source and target that resolve within the same Project to the Project Configuration source role and its Core Meta-Model prerequisite role declared by CA-R-1218@31, accept the occurrence without comparing Tiers;
    5. treat every other descendant or sibling target, unknown relation membership or endpoints, missing Tier/scope/parentage, unresolved logical-role identity, unresolved Project correspondence, an unresolved CA-R-1218@31 prerequisite declaration, derived inverse views, and cycles as unresolved failures rather than silently passing them. Where the approved ordering requires it and the owner range permits it, raise the source integer Tier until the same-Scope constraint holds.
    
    Tier is a graph-ordering level only. It does not classify semantic abstraction, importance, Claim Scope breadth, Content Role, Type, Source ownership, filename, structural depth, or any named tier category.
- Shared RMED source: `CA-E-654@12`
  - Remaining Claim prose:
    this Evaluation **must** cover one coherent numeric graph-ordering case:
    
    - ordinary Project-owned and non-Project Scope Unit-owned Atoms carry integer Tier **>=0**; a verified Project Goal carries exactly Tier **-1**;
    - a verified Operator-owned Project Goal retains its Actor owner and uses its Target Project only as ordering context; a same-Project root Atom at Tier 0 may target that Tier -1 Goal, and a descendant-Scope Atom may target it through strict ancestry; unverified Goals or Goals of another Project do not pass;
    - the integer Tier is independent of Content Role, Type, semantic abstraction, Claim Scope breadth, filename, structural depth, and any named category;
    - for every stored governing Current R/M/E/D relation occurrence selected under CA-R-2148@10, a same-Scope target has a strictly lower Tier than its source, except an admitted typed governing relation from a local Tier 0 Method, Evaluation or Delivery source to a local Tier 0 Requirement target; where an Operations source has an independently admitted typed governing relation to a Requirement, the same narrow exception applies; no new Operations relation is admitted;
    - a strict-ancestor target is permitted without Tier comparison; the exact one-way source-Project-Configuration-to-target-Core-Meta-Model logical-role prerequisite declared by CA-R-1218@31 is permitted without Tier comparison when both roles resolve within the same Project; reverse Core-to-Project-Configuration, Project-root-to-Core, Methodology-Sources-root-to-Core, Extension-to-Core, Project-Configuration-to-Extension, cross-Project, and unresolved-role cases do not pass; every other descendant and sibling target is forbidden;
    - the CA-R-2148@10 Selection source endpoint is Current R/M/E/D, while the target may be any Current Atom permitted by the registered relation endpoint definition; an independently admitted Operations-source exception is checked separately;
    - equal Tier 0 is rejected for R-to-R, R-to-M/E/D/O and M/E/D/O-to-M/E/D/O, and for any relation or endpoints not admitted by its defining declaration; ancestor and declared prerequisite alternatives remain unchanged;
    - valid existing integers are preserved, and a source integer may be raised when required by the same-Scope ordering and admitted owner range;
    - unknown relation membership or endpoints, missing Tier/scope/parentage, unresolved logical-role identity, unresolved Project correspondence, an unresolved CA-R-1218@31 prerequisite declaration, derived inverse views, and cycles are unresolved failures, not silent passes.
    
    No Content-Role or Type-to-Tier restriction is introduced by this case.
- Shared RMED source: `CA-D-651@13`
  - Remaining Claim prose:
    an Atom filename **must** serialize the Atom's internally carried numeric Tier only through the currently registered filename grammar. For numeric Tier `0`, the Tier segment **must** be the literal `SCOPE_CONTRACT`, exactly once. This token represents `tier: 0`; it does not set the Atom's Type or separate Label property and does not require a second frontmatter flag. Other numeric Tiers keep their registered filename encodings. Numeric Tier tokens are representations only; a higher integer Tier requires an explicitly registered token rule and **must not** be guessed from a retired Local Tier or Global Tier label. Filename interpretation **must** preserve the Atom identity, owner, target, Scope, and sequence grammar, and a filename alone **must not** become the source of the numeric Tier.
    
    The external Project Goal grammar **must** be recognized before applying any ordinary filename default. No Content Role or Type-to-Tier restriction is introduced by this delivery rule.
- Shared RMED source: `CA-D-652@13`
  - Remaining Claim prose:
    an Atom filename **may** omit the default Tier `3` token only where the registered filename grammar explicitly defines that omission. The Atom **must** still carry its numeric Tier internally under CA-R-2504; omission **must not** add, remove, or alter an Atom Property, infer a Content Role or Type restriction, or change the represented source Properties in a Projection or other non-Atom Artifact. A Project Goal's explicit Tier `-1` grammar is evaluated before any ordinary default omission.

### `Atom.Tier.Label` — property

- Declaration source: `CA-R-2505@2`
  - Fenced Claim block:
```CFEL
Atom.Tier.Label{:0..1}: [string]{:1};
Atom.Tier.Label.*[]{:0};
IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 0)) THEN (Atom.Tier.Label == Scope Contract);
IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 1)) THEN (Atom.Tier.Label == Core);
IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 2)) THEN (Atom.Tier.Label == General);
IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 3)) THEN (Atom.Tier.Label == Standard);
IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 4)) THEN (Atom.Tier.Label == Detail)
```
  - Nested Property contracts:
    - `Atom.Tier.Label` property; names=None; names count=0..1; values=string; values count=1
    - `Atom.Tier.Label` immediate_dependents; names=; names count=0; values=None; values count=undefined
  - Unresolved CFEL: `IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 0)) THEN (Atom.Tier.Label == Scope Contract)`
  - Unresolved CFEL: `IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 1)) THEN (Atom.Tier.Label == Core)`
  - Unresolved CFEL: `IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 2)) THEN (Atom.Tier.Label == General)`
  - Unresolved CFEL: `IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 3)) THEN (Atom.Tier.Label == Standard)`
  - Unresolved CFEL: `IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 4)) THEN (Atom.Tier.Label == Detail)`

### `Atom.Updated At` — property

- Declaration source: `CA-R-2489@2`
  - Fenced Claim block:
```CFEL
Atom.Updated At{:1}: [datetime]{:1};
Atom.Updated At.*[]{:0};
Atom//$atom.Updated At == MAX(Event Record//(.object_output{=1}, .object_output.version{=1}, .object_output.id = $atom.ID, .object_output.version = $atom.Version, (.action = create OR .action = update)).happened_at)
```
  - Nested Property contracts:
    - `Atom.Updated At` property; names=None; names count=1; values=datetime; values count=1
    - `Atom.Updated At` immediate_dependents; names=; names count=0; values=None; values count=undefined
  - Unresolved CFEL: `Atom//$atom.Updated At == MAX(Event Record//(.object_output{=1}, .object_output.version{=1}, .object_output.id = $atom.ID, .object_output.version = $atom.Version, (.action = create OR .action = update)).happened_at)`
- Shared RMED source: `CA-R-1416@26`
  - Remaining Claim prose:
    **every** Atom **must** have **`=1`** unambiguous Updated At date-time.
- Shared RMED source: `CA-R-1788@18`
  - Remaining Claim prose:
    **every** actual accepted edit **to** an Atom Carrier **must** refresh that Current Atom's `updated_at` **to** the actual Project-time edit instant, including a formatting, lossless serialization, Entity-name, admitted Current Status, direct-owner, **or** current-Atom local-placement edit. an exact no-op **must** retain Updated At. When a real update publishes a successor and archives its predecessor, the Archive Carrier **must** retain the predecessor's prior Updated At, numeric Version, and unrelated content while carrying the Archived status and version-qualified identity; Git history preserves the exact pre-archive bytes. Standalone archival is not an edit to the Current Atom's content: it only materializes the Archived representation with its version-qualified identity, filename and location, so it does not create a successor or refresh Updated At.
- Shared RMED source: `CA-E-521@22`
  - Remaining Claim prose:
    the Evaluation **must** accept **only** an actual same-ID edit that refreshes `updated_at` **and** increments Version by exactly **`1`**, regardless of semantic change class. an exact no-op retains Version **and** Updated At; required predecessor history retains its exact prior bytes.

### `Atom.Version` — property

- Declaration source: `CA-R-2496@2`
  - Fenced Claim block:
```CFEL
Atom.Version{:1}: [int]{:1};
Atom.Version.*[]{:0};
Atom.Version >= 1
```
  - Nested Property contracts:
    - `Atom.Version` property; names=None; names count=1; values=int; values count=1
    - `Atom.Version` immediate_dependents; names=; names count=0; values=None; values count=undefined
  - Unresolved CFEL: `Atom.Version >= 1`

### `Atom/(.Role:=Concern).Priority` — property

- Declaration source: `CA-R-2518@2`
  - Fenced Claim block:
```CFEL
Atom/(.Role: Concern).Priority{:1}: [string]{:1};
Atom/(.Role: Concern).Priority.*[]{:0};
Atom/(.Role: Concern).Priority: High;
Atom/(.Role: Concern).Priority: Medium;
Atom/(.Role: Concern).Priority: Low
```
  - Unresolved CFEL: `Atom/(.Role: Concern).Priority{:1}: [string]{:1}`
  - Unresolved CFEL: `Atom/(.Role: Concern).Priority.*[]{:0}`
  - Unresolved CFEL: `Atom/(.Role: Concern).Priority: High`
  - Unresolved CFEL: `Atom/(.Role: Concern).Priority: Medium`
  - Unresolved CFEL: `Atom/(.Role: Concern).Priority: Low`
- Shared RMED source: `CA-R-1629@39`
  - Remaining Claim prose:
    a Concern Atom has **`=1`** Priority value: High, Medium, **or** Low.
    
    direct comparison of Concern Atoms **must** follow the admissible Operator-selected priority model governed by CA-R-1487:
    
    - use the selected model, its effective parameters, **and** its active criteria.
    - Scope Unit ancestry **must not** add an implicit Priority increment.
    - **if** the model **or** its application does **not** justify a selection, leave the conflict unresolved **and** ask the Operator.
    
    the Framework Instance Settings Artifact exposes **`=2`** selection modes:
    
    - `ask_always`, the default, explains the conflict **and** asks the operator; **and**
    - `auto_by_effective_priority`, which **may** select **only** one uniquely eligible winner.
    
    the selection mode **must** ask the Operator **if** ties, incomparable structure, uncertainty, **or** multiple winners occur. mutually unsatisfiable external obligations stop for Operator **or** external resolution. PRMEDO Tier precedence, deterministic replacement, explicit scoped override, stale-view routing, **and** Implementation drift follow their own semantics rather than this selection mode.
- Shared RMED source: `CA-E-623@30`
  - Remaining Claim prose:
    conflict selection follows the admissible Operator-selected priority model **without** an implicit ancestry bonus **and** never chooses through a tie, incomparable scope, uncertainty, **or** ineligible external obligation.
- Shared RMED source: `CA-D-386@23`
  - Remaining Claim prose:
    a Concern Atom Carrier **must** serialize **`=1`** selected Priority as `priority` with the lowercase value `high`, `medium`, **or** `low`. **every** non-Concern Content Role Atom Carrier **must** omit `priority`; virtual `highest` **must not** be stored.

### `Atom/(.Role:=Operations)/Action.Execution Kind` — property

- Declaration source: `CA-R-2521@2`
  - Fenced Claim block:
```CFEL
Atom/(.Role: Operations)/Action.Execution Kind{:1}: [string]{:1};
Atom/(.Role: Operations)/Action.Execution Kind.*[]{:0};
Atom/(.Role: Operations)/Action.Execution Kind: Programmatic;
Atom/(.Role: Operations)/Action.Execution Kind: Agentic
```
  - Unresolved CFEL: `Atom/(.Role: Operations)/Action.Execution Kind{:1}: [string]{:1}`
  - Unresolved CFEL: `Atom/(.Role: Operations)/Action.Execution Kind.*[]{:0}`
  - Unresolved CFEL: `Atom/(.Role: Operations)/Action.Execution Kind: Programmatic`
  - Unresolved CFEL: `Atom/(.Role: Operations)/Action.Execution Kind: Agentic`

### `Atom/(.Role:=Plan).AI Agent Confidence Threshold` — property

- Declaration source: `CA-R-2519@2`
  - Fenced Claim block:
```CFEL
Atom/(.Role: Plan).AI Agent Confidence Threshold{:0..1}: [int]{:1};
Atom/(.Role: Plan).AI Agent Confidence Threshold.*[]{:0};
Atom/(.Role: Plan).AI Agent Confidence Threshold
  ?= LOOKUP(IS_CONTAINED_BY, Atom/(.Role: Plan).AI Agent Confidence Threshold)
  ?= Scope Unit/Project//$project.Settings.AI Agent Confidence Threshold
```
  - Unresolved CFEL: `Atom/(.Role: Plan).AI Agent Confidence Threshold{:0..1}: [int]{:1}`
  - Unresolved CFEL: `Atom/(.Role: Plan).AI Agent Confidence Threshold.*[]{:0}`
  - Unresolved CFEL: `Atom/(.Role: Plan).AI Agent Confidence Threshold
  ?= LOOKUP(IS_CONTAINED_BY, Atom/(.Role: Plan).AI Agent Confidence Threshold)
  ?= Scope Unit/Project//$project.Settings.AI Agent Confidence Threshold`

### `Atom/(.Role:=Plan).Work Sequence Number` — property

- Declaration source: `CA-R-2520@2`
  - Fenced Claim block:
```CFEL
Atom/(.Role: Plan).Work Sequence Number{:0..1}: [int]{:1};
Atom/(.Role: Plan).Work Sequence Number.*[]{:0};
IF (Atom/(.Role: Plan).Work Sequence Number{=1})
THEN (Atom/(.Role: Plan).Work Sequence Number > 0);
UNIQUE(
  Atom/(.Role: Plan)//,
  (.Relations.contained_by.atom, .Work Sequence Number),
  (.Status = Active) AND (.Work Sequence Number{=1}) AND (.Relations.contained_by.atom{=1})
);
UNIQUE(
  Atom/(.Role: Plan)//,
  (.Relations.contained_by.scope_unit, .Work Sequence Number),
  (.Status = Active) AND (.Work Sequence Number{=1}) AND (.Relations.contained_by.scope_unit{=1})
)
```
  - Unresolved CFEL: `Atom/(.Role: Plan).Work Sequence Number{:0..1}: [int]{:1}`
  - Unresolved CFEL: `Atom/(.Role: Plan).Work Sequence Number.*[]{:0}`
  - Unresolved CFEL: `IF (Atom/(.Role: Plan).Work Sequence Number{=1})
THEN (Atom/(.Role: Plan).Work Sequence Number > 0)`
  - Unresolved CFEL: `UNIQUE(
  Atom/(.Role: Plan)//,
  (.Relations.contained_by.atom, .Work Sequence Number),
  (.Status = Active) AND (.Work Sequence Number{=1}) AND (.Relations.contained_by.atom{=1})
)`
  - Unresolved CFEL: `UNIQUE(
  Atom/(.Role: Plan)//,
  (.Relations.contained_by.scope_unit, .Work Sequence Number),
  (.Status = Active) AND (.Work Sequence Number{=1}) AND (.Relations.contained_by.scope_unit{=1})
)`
- Shared RMED source: `CA-R-992@36`
  - Remaining Claim prose:
    a Work Sequence Number **must not** establish **or** change Atom identity, Atom Scope, Claim Target Scope Unit, Type, authoring Subtype, decomposition, **or** blocking.
- Shared RMED source: `CA-R-997@34`
  - Remaining Claim prose:
    **every** supplied Work Sequence Number **must** be a unique positive ordinal among Plans directly contained by the same Plan **or** sharing the same top-level Plan container.
- Shared RMED source: `CA-D-381@23`
  - Remaining Claim prose:
    **every** Carrier rendering of a Work Sequence Number **must** use decimal digits.

### `Atom/(.Role:=Requirement)/(.Form:=Relation Definition).Content.notation_for_subject` — property

- Declaration source: `CA-R-2522@2`
  - Remaining Claim prose:
    When a short subject notation is admitted for the Relation, this Property is required.
  - Fenced Claim block:
```CFEL
Atom/(.Role: Requirement)/(.Form: Relation Definition).Content.notation_for_subject{:0..1}: [string]{:1};
Atom/(.Role: Requirement)/(.Form: Relation Definition).Content.notation_for_subject.*[]{:0}
```
  - Unresolved CFEL: `Atom/(.Role: Requirement)/(.Form: Relation Definition).Content.notation_for_subject{:0..1}: [string]{:1}`
  - Unresolved CFEL: `Atom/(.Role: Requirement)/(.Form: Relation Definition).Content.notation_for_subject.*[]{:0}`

### `Carrier.Canonical Address` — property

- Declaration source: `CA-R-1949@11`
  - Remaining Claim prose:
    A Carrier's Canonical Address **means** its designated locator under the applicable addressing rules. It is **not** the Carrier's ID.
- Shared RMED source: `CA-D-267@27`
  - Remaining Claim prose:
    that address **must** be its sole Carrier encoding **and** embedded metadata **must not** duplicate it. Atom Properties instead follow CA-D-478 **and** CA-D-480.
- Shared RMED source: `CA-D-296@29`
  - Remaining Claim prose:
    a Scope Unit's administrative Content Role directory **must** be materialized for canonical Artifact placement **only** **when** the first current Artifact requires that placement.

### `Carrier.Canonical Address.Segment` — property

- Declaration source: `CA-R-1948@12`
  - Remaining Claim prose:
    A Canonical Address Segment **means** one component of a Carrier's Canonical Address under its applicable address format.
    
    ### Formal claim
  - Fenced Claim block:
```text
Carrier.Canonical Address.Segment[string]{1}
```
- Shared RMED source: `CA-D-289@24`
  - Remaining Claim prose:
    **every** Archived Atom Carrier basename **must** serialize the archived Atom's canonical ID with exactly one `@<version>` marker, where `<version>` is the unchanged numeric Version Number of that Archived Atom version. The marker **must** occur in the filename's Atom-ID segment under CA-D-283; do **not** append a second `@<version>` to a basename that already carries the marker. Existing legacy archive basenames are not normalized automatically.
- Shared RMED source: `CA-D-290@25`
  - Remaining Claim prose:
    a Current Atom source Carrier basename **must not** contain an `@<version>` suffix, regardless of the Atom's admitted Status value.
- Shared RMED source: `CA-D-301@28`
  - Remaining Claim prose:
    **every** Project-owned Carrier address segment
    
    - **must** use **only** portable automation-safe ASCII letters, digits, underscores, hyphens, **and** dots, with `@` admitted **only** **in** the `@<version>` Archive suffix immediately **before** the file extension, as specified by CA-D-289,
    - **must not** contain whitespace, control characters, path separators, shell metacharacters, empty **or** reserved segments, **or** unsafe leading **or** trailing characters,
    - **and** **must** remain sibling-unique under ASCII case folding.
- Shared RMED source: `CA-D-352@25`
  - Remaining Claim prose:
    a Status subdirectory used for Artifact Carrier placement **must not** be a Directory Carrier.

### `Carrier.Format` — property

- Declaration source: `CA-R-1950@12`
  - Remaining Claim prose:
    A Carrier's Format **means** the rules for encoding and interpreting its represented content. The registered File Carrier values include Markdown, TOML, YAML and JSON under CA-D-262; representation details remain governed by Delivery.
    
    ### Formal claim
  - Fenced Claim block:
```text
Carrier/File.Format: Markdown
Carrier/File.Format: TOML
Carrier/File.Format: YAML
Carrier/File.Format: JSON
```

### `Carrier.ID` — property

- Declaration source: `CA-R-1951@12`
  - Remaining Claim prose:
    A Carrier ID identifies one Carrier. Its filename and path are **not** its ID.
    
    ### Formal claim
  - Fenced Claim block:
```text
Carrier.ID[string]{1}
```

### `Carrier/Directory.Name` — property

- Declaration source: `CA-R-1952@12`
  - Remaining Claim prose:
    A Directory Carrier's Name **means** the name of its directory within its parent directory, excluding the parent path.
    
    ### Formal claim
  - Fenced Claim block:
```text
Directory.Name[string]{1}
```
- Shared RMED source: `CA-D-297@31`
  - Remaining Claim prose:
    **when** the default Scope Unit directory convention is used, **every** Project-internal Scope Unit authority Directory Carrier Name **must** serialize the registered derived Scope Unit Path representation, Navigational Order Number, Label, applicable Local Order, **and** Scope Unit Name **in** that order. no Structural Level field or token is required or authoritative. a declared native Carrier binding under CA-D-445-CORE_META_MODEL-GENERAL-DELIVERY--admit-explicit-scope-unit-carrier-bindings **must not** be reinterpreted through this default convention.
- Shared RMED source: `CA-D-298@30`
  - Remaining Claim prose:
    **when** the default Scope Unit directory convention is used, a Scope Unit authority Directory Carrier Name **must** serialize Local Order immediately **after** Label **only** for an Ordered Scope Unit **and** **must not** serialize Local Order for an Unordered Scope Unit. a declared native Carrier binding under CA-D-445-CORE_META_MODEL-GENERAL-DELIVERY--admit-explicit-scope-unit-carrier-bindings **must not** be reinterpreted through this default convention.
- Shared RMED source: `CA-D-299@30`
  - Remaining Claim prose:
    **every** root Delivery Directory Carrier **must** serialize the registered derived Scope Unit Path representation, Navigational Order Number, **and** Scope Unit Name **and** **must not** serialize Label **or** Local Order. no Structural Level field or token is required or authoritative. a declared native Carrier binding under CA-D-445 **must not** be reinterpreted through this default convention.

### `Carrier/Directory.Numeric Prefix` — property

- Declaration source: `CA-R-1953@13`
  - Remaining Claim prose:
    A Directory Carrier's Numeric Prefix **means** the leading numeric part of its Name when the applicable naming convention uses one.
    
    ### Formal claim
  - Fenced Claim block:
```text
Directory.Numeric Prefix[int]{0..1}
```

### `Carrier/Directory.Path` — property

- Declaration source: `CA-R-1954@12`
  - Remaining Claim prose:
    A Directory Carrier's Path **means** the locator of its directory within a filesystem, absolute or relative to a stated base. It does **not** define Scope Unit parentage or Carrier identity.
    
    ### Formal claim
  - Fenced Claim block:
```text
Directory.Path[string]{1}
```

### `Carrier/File.Extension` — property

- Declaration source: `CA-R-1974@12`
  - Remaining Claim prose:
    A File Carrier's Extension **means** the filename suffix used to indicate its format. The extension does **not** establish the carried Entity's identity.
    
    ### Formal claim
  - Fenced Claim block:
```text
File.Extension[string]{0..1}
```

### `Carrier/File.Filename` — property

- Declaration source: `CA-R-1975@12`
  - Remaining Claim prose:
    A File Carrier's Filename **means** the name of its file within its containing directory, including any extension. It does **not** include the directory path.
    
    ### Formal claim
  - Fenced Claim block:
```text
File.Filename[string]{1}
```
- Shared RMED source: `CA-D-283@32`
  - Remaining Claim prose:
    **every** identified Project-owned Markdown Atom filename other than a Plan filename governed by CA-D-469 **must** match `<ATOM_ID>[-<CURRENT_SCOPE>][-<TIER>][-<LABEL>][-<TARGET_SCOPE>]--<SUMMARY_SLUG>.<EXT>`. When present, the `LABEL` segment uses the Atom's effective Label: its explicit Label when present, otherwise its Type name under CA-R-2497. Normalize that token under CA-D-284; an explicit Label replaces the Type name there and does not change the Atom's Type. **every** same-identity Atom Version **must** preserve its exact assigned Atom-ID segment **in** its Carrier filename **and** serialize its retained Summary under CA-D-282. A Draft filename uses the Draft marker as its Atom-ID segment as specified by CA-D-650. An Archived predecessor uses `<canonical-ID>@<old-version>` exactly once in that segment under CA-D-289; do not append a duplicate version suffix. Existing legacy archive filenames are not normalized automatically. a replacement filename **must** contain the successor Atom ID **and** the successor's Summary Slug; a Summary Slug **must not** be edited independently of its source Summary.
- Shared RMED source: `CA-D-284@24`
  - Remaining Claim prose:
    **every** structured Atom filename token **must** use uppercase ASCII with underscores inside tokens, while Summary Slug **and** extension **must** use lowercase ASCII.
- Shared RMED source: `CA-D-287@28`
  - Remaining Claim prose:
    **every** Demand Atom filename **must** serialize its Type **and** Producer Scope as `DEMANDS_FROM-<PRODUCER_SCOPE>`.
- Shared RMED source: `CA-D-363@28`
  - Remaining Claim prose:
    the authoritative Project Settings TOML File Carrier filename **must** be exactly `caprmedio_project_settings.toml`.
- Shared RMED source: `CA-D-469@24`
  - Remaining Claim prose:
    **every** identified Plan Carrier stem **must** use `[<WORK_SEQUENCE_NUMBER>-]<ATOM_ID>[-<LABEL>]--<SUMMARY_SLUG>`, with `.md` **only** on its File Carrier.
    
    - the optional Label is a navigation token, **not** an Atom Type token; normalize it under CA-D-284.
    - render the Summary under CA-D-282.
    - **by default**, direct Plans decomposing the same Hub use unique leading Work Sequence Numbers **before** their Atom IDs, under CA-D-381 **and** CA-R-997.
    - a same-bundle Directory Carrier **and** File Carrier use the same stem; number **or** Label changes preserve Atom identity **and** do **not** declare `BLOCKS`.
- Shared RMED source: `CA-D-650@12`
  - Remaining Claim prose:
    A Draft Atom proposing a revision of an existing Atom **must** carry `atom_id: <canonical-ID>@<proposed-version>-draft`, where `<proposed-version>` is the proposed numeric Atom Version. Its filename **must** carry that exact marker once as the Atom-ID segment before the filename's mutable components under CA-D-283. Do **not** append another `@<version>` suffix to the basename. The Draft marker identifies the proposed revision; it does not replace or advance the Current Atom source before an admitted update.
    
    New-Atom Draft markers continue to use the role-only form governed by CA-D-378; this rule does not add a version number to a new Atom's marker or change other filename components.
- Shared RMED source: `CA-D-498@13`
  - Remaining Claim prose:
    **every** filename token representing a Scope Unit **must** use its complete Scope Unit Name, rendered **in** uppercase with underscores under `CA-D-284-CORE_META_MODEL-DELIVERY--serialize-filename-token-case`, **without** abbreviation **or** a separately maintained alias.

### `Carrier/File.Filename.Scope Unit Token` — property

- Declaration source: `CA-R-2345@2`
  - Remaining Claim prose:
    A File Carrier Filename Scope Unit Token is one stable uppercase token for a referenced Scope Unit. A filename may contain zero or more tokens; each serialized Scope Unit reference uses one token selected by Project Configuration.
    
    ### Formal claim
  - Fenced Claim block:
```text
Carrier/File.Filename.Scope Unit Token[string]{0+}
```
- Shared RMED source: `CA-D-302@28`
  - Remaining Claim prose:
    **every** Scope Unit reference serialized **in** an Atom filename **must** use **`=1`** stable uppercase token selected from its Scope Unit Name by Project Configuration.

### `Carrier/File.Format` — property

- Declaration source: `CA-R-2346@2`
  - Remaining Claim prose:
    A File Carrier's Format is the rules for encoding and interpreting its represented content. Core Meta-Model permits registered Markdown, TOML, YAML and JSON formats; Extensions and Project Configuration may register additional Carrier Formats.
    
    ### Formal claim
  - Fenced Claim block:
```text
Carrier/File.Format[string]{1}
```
- Shared RMED source: `CA-D-262@27`
  - Remaining Claim prose:
    the Core Meta-Model **must** permit registered File Carrier Formats including Markdown, TOML, YAML, **and** JSON while Extensions **and** Project Configuration **may** register additional Carrier Formats.

### `Carrier/File.Main Content` — property

- Declaration source: `CA-R-2347@2`
  - Remaining Claim prose:
    A Markdown File Carrier Main Content means the content after its YAML Frontmatter and is its Markdown body. It is optional, may contain Paragraph and CCE Operator occurrences as content parts, and is not a separate File.
    
    ### Formal claim
  - Fenced Claim block:
```text
Carrier/File.Main Content[string]{0..1}
```
- Shared RMED source: `CA-D-357@21`
  - Remaining Claim prose:
    the Main Content of a Markdown Atom Carrier **means** the content **after** its YAML Frontmatter.
- Shared RMED source: `CA-D-479@27`
  - Remaining Claim prose:
    For RMED, carry one `## Summary` and one `## Claim` as sibling Properties, optionally preceded by `## Claim scope` before Claim and followed by `## Semantics` and `## Details` in that order. The Claim's direct Markdown value may consist of a fenced CFEL expression without prose. Do not create a `Formal claim` child, a separate Prose claim section, or a duplicate frontmatter Claim. Omit absent optional sections.
    
    Map headings to Property paths with a code-fence-aware outline. A section ends at the next real heading of the same or higher level, or at the end of Main Content. Lower-level real headings nest under their parent; equal-level headings are siblings, and skipped levels create no empty Properties. Heading-like text in a fence is content. Direct value counts and dependent Property counts are independent. Retrieving a section subtree includes its selected heading and its descendants.
    
    Normalize real heading names to lowercase, replace spaces with underscores, and strip characters other than letters, numbers, underscore and hyphen. Reject an empty normalized key or duplicate normalized key under one parent. A flattened lookup is admissible only when unambiguous; canonical paths retain their parent chain.
    
    Legacy layouts remain readable during migration. The existing C/A/P/O primary-content headings and their own Type-specific content rules remain applicable. A Draft may be incomplete but must satisfy the applicable complete contract before promotion.

### `Carrier/File.Main Content.CCE Operator` — property

- Declaration source: `CA-R-2348@2`
  - Remaining Claim prose:
    A Main Content CCE Operator is a textual occurrence of a CCE Operator in a Markdown File Carrier Main Content; its serialized spelling and rendering follow the canonical Delivery rule.
    
    ### Formal claim
  - Fenced Claim block:
```text
Carrier/File.Main Content.CCE Operator[string]{0+}
```
- Shared RMED source: `CA-D-280@25`
  - Remaining Claim prose:
    **every** CCE Operator occurrence within Markdown Atom Carrier Main Content **must** use its exact canonical spelling with bold rendering; a word-form CCE Operator **must** use lowercase bold text, while a symbolic CCE Operator **must** use bold inline-code rendering.

### `Carrier/File.Main Content.Paragraph` — property

- Declaration source: `CA-R-2349@2`
  - Remaining Claim prose:
    A Main Content Paragraph is one prose paragraph in a Markdown File Carrier Main Content; zero or more may occur. Delivery serializes each paragraph on one unwrapped source line with one blank line between adjacent paragraphs.
    
    ### Formal claim
  - Fenced Claim block:
```text
Carrier/File.Main Content.Paragraph[string]{0+}
```
- Shared RMED source: `CA-D-279@24`
  - Remaining Claim prose:
    **every** Markdown Atom Carrier Main Content prose paragraph **must** use one unwrapped source line **and** one blank line between adjacent paragraphs.

### `Carrier/File.Path` — property

- Declaration source: `CA-R-1976@12`
  - Remaining Claim prose:
    A File Carrier's Path **means** the locator of its file within a filesystem, absolute or relative to a stated base. It is a locator, **not** the Carrier's ID.
    
    ### Formal claim
  - Fenced Claim block:
```text
File.Path[string]{1}
```

### `Carrier/File.YAML Frontmatter` — property

- Declaration source: `CA-R-2350@4`
  - Remaining Claim prose:
    A Markdown File Carrier YAML Frontmatter is its optional structured metadata region. It has no direct scalar value and is a logical region, not a separate Carrier; its encoding uses economical YAML syntax and keeps uncontrolled prose in Main Content.
    
    ### Formal claim
  - Fenced Claim block:
```text
Carrier/File.YAML Frontmatter{0}
```
- Shared RMED source: `CA-D-657@2`
  - Remaining Claim prose:
    Encode each key once and use a YAML sequence for multiple values. Use a nonempty string for each required string; null and collections do not satisfy a scalar requirement. Integers exclude booleans.
    
    For Markdown Atom carriers:
    
    - Encode Role and Form as `role` and `form`, each exactly one nonempty string from the applicable domain.
    - Encode identity, Version, Status, Updated At and Tier as `atom_id`, `version`, `status`, `updated_at` and `tier`. Apply their respective Property rules. An optional Label uses `label`; do not duplicate Summary or Claim in frontmatter.
    - Encode Subjects under `subjects` using the Subjects serialization rule. Encode direct Node-instance Relation facts under `relations`; use each Relation's own representation and do not author inverse facts separately.
    - Do not encode an Atom Author. Event authorship is governed by the Event Record model.
    - Derive Target Scope Unit from the active Subject using the applicable model authority. During carrier migration, `current_scope_unit` and `claim_target_scope_unit`, if present, are legacy compatibility data; they do not establish Atom Properties or override the resolved Scope. Their retention, removal and consistency validation require the selected migration's explicit disposition. Do not infer a target from the carrier directory or use either field as an unverified fallback.
    - Place a complete RMED Claim in its `## Claim` section. Its direct Markdown value may contain CFEL and need not contain prose; do not create a `Formal claim` child.
    
    Legacy `content_role`, `type`, `subjects.governs` and `subjects.depends_on` remain readable during migration. Conflicting old and new names for the same Property are invalid in any carrier; equal pairs are readable during transition and do not create duplicate logical values. Compatibility does not make the old names canonical in the migrated model.

### `Carrier/File.YAML Frontmatter.Scalar` — property

- Declaration source: `CA-R-2351@2`
  - Remaining Claim prose:
    A YAML Frontmatter Scalar is one direct primitive value within a declared metadata field of a File Carrier YAML Frontmatter; zero or more may occur. Registered YAML-safe controlled strings are serialized as plain scalars.
    
    ### Formal claim
  - Fenced Claim block:
```text
Carrier/File.YAML Frontmatter.Scalar[scalar]{0+}
```
- Shared RMED source: `CA-D-277@24`
  - Remaining Claim prose:
    the YAML Frontmatter of a Markdown Atom Carrier **must** serialize registered YAML-safe controlled string values as plain scalars **and** **must** place uncontrolled human prose **in** Main Content.

### `Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Artifact Timestamp Timezone` — property

- Declaration source: `CA-R-1977@13`
  - Remaining Claim prose:
    Artifact Timestamp Timezone **means** the Framework Settings value that supplies the timezone interpretation used when emitting Artifact timestamps.
    
    ### Formal claim
  - Fenced Claim block:
```text
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Artifact Timestamp Timezone[string]{0..1}
```
- Shared RMED source: `CA-D-390@27`
  - Remaining Claim prose:
    the Framework Instance Settings Artifact **may** set `[artifact_timestamps].timezone` **to** `local`, `UTC`, **or** an IANA timezone name, with `local` as the default; **every** emitted `updated_at` value uses `YYYY-MM-DD HH:MM:SS +ZZZZ` with its explicit numeric UTC offset, **and** the setting supplies its timezone interpretation.

### `Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Code-Root Locators` — property

- Declaration source: `CA-R-1978@13`
  - Remaining Claim prose:
    Code-Root Locators **means** the Framework Settings references to the framework code roots used by the Project.
    
    ### Formal claim
  - Fenced Claim block:
```text
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Code-Root Locators[string]{1+}
```
- Shared RMED source: `CA-D-371@24`
  - Remaining Claim prose:
    the Framework Instance Settings TOML Carrier **must** encode **`>=1`** code-root locator for the instance.

### `Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Confidence` — property

- Declaration source: `CA-R-1979@13`
  - Remaining Claim prose:
    Confidence **means** the group of Framework Settings defaults for the declared Confidence Thresholds.
    
    ### Formal claim
  - Fenced Claim block:
```text
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Confidence{0}
```

### `Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Framework Control-Root Locator` — property

- Declaration source: `CA-R-1980@13`
  - Remaining Claim prose:
    Framework Control-Root Locator **means** the Framework Settings reference to the Project's governed framework control directory.
    
    ### Formal claim
  - Fenced Claim block:
```text
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Framework Control-Root Locator[string]{1}
```
- Shared RMED source: `CA-D-370@26`
  - Remaining Claim prose:
    the Framework Instance Settings TOML Carrier **must** encode the framework control-root locator for its Project, resolving **to** the Directory Carrier prescribed by CA-D-317 **without** selecting a different authority root.

### `Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Identifier` — property

- Declaration source: `CA-R-1981@14`
  - Remaining Claim prose:
    Framework Settings Identifier identifies the Project's authoritative Framework Settings configuration, **not** an Atom.
    
    ### Formal claim
  - Fenced Claim block:
```text
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Identifier[string]{1}
```
- Shared RMED source: `CA-D-358@26`
  - Remaining Claim prose:
    the Identifier of the authoritative Framework Instance Settings Artifact **must** be `caprmedio_framework_settings`.

### `Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Interaction` — property

- Declaration source: `CA-R-1982@13`
  - Remaining Claim prose:
    Interaction **means** the group of Framework Settings choices that govern presentation of information to the Operator.
    
    ### Formal claim
  - Fenced Claim block:
```text
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Interaction{0}
```
- Shared RMED source: `CA-R-1439@23`
  - Remaining Claim prose:
    the interaction reporting mode **must** affect presentation **only**, **without** changing authorization, Artifact creation, workflow routing, validation, **or** safety behavior.
- Shared RMED source: `CA-R-1440@24`
  - Remaining Claim prose:
    **every** interaction reporting mode **must** report the following mandatory information:
    
    - blockers **and** failed operations;
    - ambiguity that requires Operator input;
    - permission **or** approval requests;
    - safety-critical information;
    - material deviations from the requested outcome.

### `Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Parameter Resolution` — property

- Declaration source: `CA-R-1983@13`
  - Remaining Claim prose:
    Parameter Resolution **means** selecting the effective framework parameter value from explicit Framework Settings **or** Default Settings under the parameter's governing rules.
    
    ### Formal claim
  - Fenced Claim block:
```text
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Parameter Resolution{0}
```
- Shared RMED source: `CA-M-279@24`
  - Remaining Claim prose:
    **to** resolve a Framework Instance Settings parameter, use its explicit value **if** that parameter is present **in** the current Project's Framework Instance Settings; **otherwise**, use the corresponding value from Default Settings. determine presence for the individual parameter, **not** its containing section **or** the truthiness of its value, so valid `false`, `0`, **and** empty values remain explicit selections. validate the selected value against its governing parameter authority **and** reject an invalid explicit value **without** falling back. **if** neither source supplies a required parameter, report that parameter as unresolved **and** stop the operation that requires it; an optional parameter **may** remain absent. do **not** copy inherited values into Framework Instance Settings as explicit selections.
- Shared RMED source: `CA-E-450@27`
  - Remaining Claim prose:
    the Evaluation **must** reject framework parameter resolution **if** **any** of the following falsifying conditions holds:
    
    - a valid explicit parameter loses **to** a Default Settings value;
    - a missing parameter fails **to** inherit its available valid default, including **when** another parameter **in** the same section is explicit;
    - a valid explicit `false`, `0`, **or** empty value is mistaken for an absent parameter;
    - an invalid explicit value is accepted **or** replaced by a fallback value;
    - an invalid selected default is accepted, **or** a required parameter missing from Framework Instance Settings **and** Default Settings receives an invented value;
    - an optional parameter absent from Framework Instance Settings **and** Default Settings is rejected solely for its absence;
    - resolution reads another Project's instance selections **or** writes inherited values back as explicit selections;
    - unchanged input values resolve differently on a repeated read;
    - Default Settings uses an unregistered Carrier location **or** a parameter representation that differs from its registered Framework Instance Settings representation.
    
    use the registered parameter constraints for the cases; **when** the current parameter catalog lacks a Boolean, zero-valued, **or** empty-valued example, use isolated test-fixture parameters **without** adding them **to** authoritative Settings.

### `Event Record.ID` — property

- Declaration source: `CA-R-2558@2`
  - Fenced Claim block:
```CFEL
Event Record.ID{:1}: [string]{:1};
Event Record.ID.*[]{:0};
UNIQUE(Event Record//, (.ID))
```
  - Nested Property contracts:
    - `Event Record.ID` property; names=None; names count=1; values=string; values count=1
    - `Event Record.ID` immediate_dependents; names=; names count=0; values=None; values count=undefined
  - Unresolved CFEL: `UNIQUE(Event Record//, (.ID))`

### `Event Record.Relations` — property

- Declaration source: `CA-R-2581@2`
  - Fenced Claim block:
```CFEL
Event Record.Relations{:1}: []{:0};
Event Record.Relations.*[Relation//]{:0+}
```
  - Nested Property contracts:
    - `Event Record.Relations` property; names=None; names count=1; values=; values count=0
    - `Event Record.Relations` immediate_dependents; names=Relation//; names count=0+; values=None; values count=undefined

### `Event Record.Relations.HAS_EVENT_AUTHOR` — property

- Declaration source: `CA-R-2582@2`
  - Fenced Claim block:
```CFEL
Event Record.Relations.HAS_EVENT_AUTHOR{:1}: [Actor//]{:1};
Event Record.Relations.HAS_EVENT_AUTHOR.*[]{:0}
```
  - Nested Property contracts:
    - `Event Record.Relations.HAS_EVENT_AUTHOR` property; names=None; names count=1; values=Actor//; values count=1
    - `Event Record.Relations.HAS_EVENT_AUTHOR` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Event Record.action` — property

- Declaration source: `CA-R-2580@2`
  - Fenced Claim block:
```CFEL
Event Record.action{:1}: [string]{:1};
Event Record.action.*[]{:0};
Event Record.action: create;
Event Record.action: update;
Event Record.action: archive
```
  - Nested Property contracts:
    - `Event Record.action` property; names=None; names count=1; values=string; values count=1
    - `Event Record.action` immediate_dependents; names=; names count=0; values=None; values count=undefined
  - Allowed values:
    - `Event Record.action: create`
    - `Event Record.action: update`
    - `Event Record.action: archive`

### `Event Record.happened_at` — property

- Declaration source: `CA-R-2568@2`
  - Fenced Claim block:
```CFEL
Event Record.happened_at{:1}: [datetime]{:1};
Event Record.happened_at.*[]{:0}
```
  - Nested Property contracts:
    - `Event Record.happened_at` property; names=None; names count=1; values=datetime; values count=1
    - `Event Record.happened_at` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Event Record.inserted_at` — property

- Declaration source: `CA-R-2569@2`
  - Fenced Claim block:
```CFEL
Event Record.inserted_at{:1}: [datetime]{:1};
Event Record.inserted_at.*[]{:0}
```
  - Nested Property contracts:
    - `Event Record.inserted_at` property; names=None; names count=1; values=datetime; values count=1
    - `Event Record.inserted_at` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Event Record.object_input` — property

- Declaration source: `CA-R-2572@2`
  - Fenced Claim block:
```CFEL
Event Record.object_input{:0..1}: []{:0};
Event Record.object_input.*[in(id,version,updated_at)]{:2..3}
```
  - Nested Property contracts:
    - `Event Record.object_input` property; names=None; names count=0..1; values=; values count=0
    - `Event Record.object_input` immediate_dependents; names=in(id,version,updated_at); names count=2..3; values=None; values count=undefined

### `Event Record.object_input.id` — property

- Declaration source: `CA-R-2573@2`
  - Fenced Claim block:
```CFEL
Event Record.object_input.id{:1}: [string]{:1};
Event Record.object_input.id.*[]{:0}
```
  - Nested Property contracts:
    - `Event Record.object_input.id` property; names=None; names count=1; values=string; values count=1
    - `Event Record.object_input.id` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Event Record.object_input.updated_at` — property

- Declaration source: `CA-R-2575@2`
  - Fenced Claim block:
```CFEL
Event Record.object_input.updated_at{:1}: [datetime]{:1};
Event Record.object_input.updated_at.*[]{:0}
```
  - Nested Property contracts:
    - `Event Record.object_input.updated_at` property; names=None; names count=1; values=datetime; values count=1
    - `Event Record.object_input.updated_at` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Event Record.object_input.version` — property

- Declaration source: `CA-R-2574@2`
  - Fenced Claim block:
```CFEL
Event Record.object_input.version{:0..1}: [int]{:1};
Event Record.object_input.version.*[]{:0}
```
  - Nested Property contracts:
    - `Event Record.object_input.version` property; names=None; names count=0..1; values=int; values count=1
    - `Event Record.object_input.version` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Event Record.object_output` — property

- Declaration source: `CA-R-2576@2`
  - Fenced Claim block:
```CFEL
Event Record.object_output{:0..1}: []{:0};
Event Record.object_output.*[in(id,version,updated_at)]{:2..3}
```
  - Nested Property contracts:
    - `Event Record.object_output` property; names=None; names count=0..1; values=; values count=0
    - `Event Record.object_output` immediate_dependents; names=in(id,version,updated_at); names count=2..3; values=None; values count=undefined

### `Event Record.object_output.id` — property

- Declaration source: `CA-R-2577@2`
  - Fenced Claim block:
```CFEL
Event Record.object_output.id{:1}: [string]{:1};
Event Record.object_output.id.*[]{:0}
```
  - Nested Property contracts:
    - `Event Record.object_output.id` property; names=None; names count=1; values=string; values count=1
    - `Event Record.object_output.id` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Event Record.object_output.updated_at` — property

- Declaration source: `CA-R-2579@2`
  - Fenced Claim block:
```CFEL
Event Record.object_output.updated_at{:1}: [datetime]{:1};
Event Record.object_output.updated_at.*[]{:0}
```
  - Nested Property contracts:
    - `Event Record.object_output.updated_at` property; names=None; names count=1; values=datetime; values count=1
    - `Event Record.object_output.updated_at` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Event Record.object_output.version` — property

- Declaration source: `CA-R-2578@2`
  - Fenced Claim block:
```CFEL
Event Record.object_output.version{:0..1}: [int]{:1};
Event Record.object_output.version.*[]{:0}
```
  - Nested Property contracts:
    - `Event Record.object_output.version` property; names=None; names count=0..1; values=int; values count=1
    - `Event Record.object_output.version` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Package.structural_level` — property

- Declaration source: `CA-R-2555@2`
  - Fenced Claim block:
```CFEL
Package.structural_level{:1}: [int]{:1};
Package.structural_level.*[]{:0};
Package.structural_level >= 0;
Package/Implementation//$implementation.structural_level = 0;
IF (Package//$contained ((IS_CONTAINED_BY)) Package//$container)
THEN ($contained.structural_level = $container.structural_level + 1)
```
  - Nested Property contracts:
    - `Package.structural_level` property; names=None; names count=1; values=int; values count=1
    - `Package.structural_level` immediate_dependents; names=; names count=0; values=None; values count=undefined
  - Unresolved CFEL: `Package.structural_level >= 0`
  - Unresolved CFEL: `Package/Implementation//$implementation.structural_level = 0`
  - Unresolved CFEL: `IF (Package//$contained ((IS_CONTAINED_BY)) Package//$container)
THEN ($contained.structural_level = $container.structural_level + 1)`

### `Project.Settings` — property

- Declaration source: `CA-R-2532@2`
  - Fenced Claim block:
```CFEL
Project.Settings{:1}: []{:0};
Project.Settings.*[in (Name, Prefix, AI Agent Confidence Threshold)]{:3}
```
  - Nested Property contracts:
    - `Project.Settings` property; names=None; names count=1; values=; values count=0
    - `Project.Settings` immediate_dependents; names=in (Name, Prefix, AI Agent Confidence Threshold); names count=3; values=None; values count=undefined
- Shared RMED source: `CA-R-1052@40`
  - Remaining Claim prose:
    the CAPRMEDIO Framework **must** distinguish authoritative Project initialization Settings, Framework Instance behavior Settings, **and** Project Structure declarations from read-only Project Scope Unit Graph Projections. structural observations **and** generated effective values **must not** become independent Settings **or** Project Structure authority.
- Shared RMED source: `CA-R-1401@27`
  - Remaining Claim prose:
    the Project Settings Artifact **must not** be an Atom.
- Shared RMED source: `CA-E-459@38`
  - Remaining Claim prose:
    the Evaluation **must** reject Project Settings **if**
    
    - it is treated as an Atom **or** Projection,
    - has an Atom ID **or** Atom Content Role,
    - is **not** available independently of Project Atoms **and** Implementation,
    - violates its registered Project-root placement **or** filename,
    - has other than **`=1`** authoritative TOML Carrier,
    - **contains** Framework Instance choices **or** independently editable Project Structure,
    - violates its foundational content boundary, applicable shared settings specifications, applicable concrete field specifications, **or** the complete closed current field signature under CA-D-366,
    - lacks a required CORE_META_MODEL definition **or** storage rule for Project Settings Name **or** Project Settings Prefix,
    - lacks an Operator-selected Project Settings Name,
    - lacks an Operator-selected Project Settings Prefix,
    - treats a Methodology Atom, Framework Instance Settings, **or** a Projection as an independent authoritative source of either selected value,
    - **or**, for history-binding evaluation under CA-D-365, lacks an exact current Revision, SHA-256 Digest, **and** admitted Work Journal receipt.
- Shared RMED source: `CA-D-364@29`
  - Remaining Claim prose:
    the Project Settings Artifact for a Project named `<project_name>` **must** use `caprmedio_project_settings.toml` directly inside that selected Project's `.caprmedio_<project_name>/` control root as its **`=1`** authoritative TOML File Carrier.
- Shared RMED source: `CA-D-365@26`
  - Remaining Claim prose:
    the current Project Settings Revision **and** SHA-256 Digest **must** bind **to** its authoritative TOML Carrier through a canonical completed governed-change Work Journal receipt **or** an explicitly authorized canonical recovered-state Work Journal receipt registering its observed baseline; the receipt **must** match the selected Project, exact Carrier path, logical Artifact Revision, **and** Digest. absence, ambiguity, **or** mismatch **must** leave its currentness unknown.
- Shared RMED source: `CA-D-366@29`
  - Remaining Claim prose:
    the Project Settings TOML Carrier **must** encode Operator-editable Project initialization inputs through sections **and** fields specified by concrete settings-specification Atoms under its foundational content **and** authority boundaries **and** applicable shared settings specifications; it **must not** store Framework Instance choices **or** authoritative Project Structure declarations **or** derived structural values as independently editable settings.
- Shared RMED source: `CA-R-622@32`
  - Remaining Claim prose:
    the CAPRMEDIO Framework Instance serving caprmedio **must** consume Project Settings **and** Framework Instance Settings according **to** Core Meta-Model authority under CA-R-1750, **without** redefining their purpose, locations, **or** selected values **in** Project Atoms.

### `Project.Settings.AI Agent Confidence Threshold` — property

- Declaration source: `CA-R-2564@2`
  - Fenced Claim block:
```CFEL
Project.Settings.AI Agent Confidence Threshold{:1}: [int]{:1};
Project.Settings.AI Agent Confidence Threshold.*[]{:0}
```
  - Nested Property contracts:
    - `Project.Settings.AI Agent Confidence Threshold` property; names=None; names count=1; values=int; values count=1
    - `Project.Settings.AI Agent Confidence Threshold` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Project.Settings.Name` — property

- Declaration source: `CA-R-2533@2`
  - Fenced Claim block:
```CFEL
Project.Settings.Name{:1}: [string]{:1};
Project.Settings.Name.*[]{:0}
```
  - Nested Property contracts:
    - `Project.Settings.Name` property; names=None; names count=1; values=string; values count=1
    - `Project.Settings.Name` immediate_dependents; names=; names count=0; values=None; values count=undefined
- Shared RMED source: `CA-D-375@29`
  - Remaining Claim prose:
    the Project Settings TOML Carrier **must** encode the Operator-selected Project Name as its exact nonempty lowercase TOML string value **in** `project.name`, **before** the first Project Atom **or** Implementation is created.

### `Project.Settings.Prefix` — property

- Declaration source: `CA-R-2534@2`
  - Fenced Claim block:
```CFEL
Project.Settings.Prefix{:1}: [string]{:1};
Project.Settings.Prefix.*[]{:0}
```
  - Nested Property contracts:
    - `Project.Settings.Prefix` property; names=None; names count=1; values=string; values count=1
    - `Project.Settings.Prefix` immediate_dependents; names=; names count=0; values=None; values count=undefined
- Shared RMED source: `CA-D-658@3`
  - Remaining Claim prose:
    the Project Settings TOML Carrier **must** encode the Operator-selected Project Prefix as its exact nonempty uppercase TOML string value under CA-D-378 **in** `artifacts.identity.project_prefix` **before** the first Project Atom is created.

### `Projection.Form` — property

- Declaration source: `CA-R-2538@2`
  - Fenced Claim block:
```CFEL
Projection.Form{:1}: [string]{:1};
Projection.Form.*[]{:0};
Projection.Form: Catalog;
Projection.Form: Map;
Projection.Form: Hub
```
  - Nested Property contracts:
    - `Projection.Form` property; names=None; names count=1; values=string; values count=1
    - `Projection.Form` immediate_dependents; names=; names count=0; values=None; values count=undefined
  - Allowed values:
    - `Projection.Form: Catalog`
    - `Projection.Form: Map`
    - `Projection.Form: Hub`

### `Projection.ID` — property

- Declaration source: `CA-R-2537@2`
  - Fenced Claim block:
```CFEL
Projection.ID{:1}: [string]{:1};
Projection.ID.*[]{:0};
DETERMINES(Projection//, (.Form, .Source.Named Selection), (.ID));
DETERMINES(Projection//, (.ID), (.Form, .Source.Named Selection))
```
  - Nested Property contracts:
    - `Projection.ID` property; names=None; names count=1; values=string; values count=1
    - `Projection.ID` immediate_dependents; names=; names count=0; values=None; values count=undefined
  - Unresolved CFEL: `DETERMINES(Projection//, (.Form, .Source.Named Selection), (.ID))`
  - Unresolved CFEL: `DETERMINES(Projection//, (.ID), (.Form, .Source.Named Selection))`
- Shared RMED source: `CA-R-1943@15`
  - Remaining Claim prose:
    Every Projection has one Projection ID. The same Projection Type, named source selection and source of truth identify the same Projection and keep the same ID across rebuilds.

### `Projection.Source` — property

- Declaration source: `CA-R-2586@2`
  - Fenced Claim block:
```CFEL
Projection.Source{:1}: []{:0};
Projection.Source.*[in (Named Selection, Atoms)]{:1..2}
```
  - Nested Property contracts:
    - `Projection.Source` property; names=None; names count=1; values=; values count=0
    - `Projection.Source` immediate_dependents; names=in (Named Selection, Atoms); names count=1..2; values=None; values count=undefined

### `Projection.Source.Atoms` — property

- Declaration source: `CA-R-2540@2`
  - Remaining Claim prose:
    Each value is an Atom ID with an explicit Version.
  - Fenced Claim block:
```CFEL
Projection.Source.Atoms{:0..1}: [string]{:0+};
Projection.Source.Atoms.*[]{:0}
```
  - Nested Property contracts:
    - `Projection.Source.Atoms` property; names=None; names count=0..1; values=string; values count=0+
    - `Projection.Source.Atoms` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Projection.Source.Named Selection` — property

- Declaration source: `CA-R-2541@2`
  - Fenced Claim block:
```CFEL
Projection.Source.Named Selection{:1}: [Named Selection//]{:1};
Projection.Source.Named Selection.*[]{:0}
```
  - Nested Property contracts:
    - `Projection.Source.Named Selection` property; names=None; names count=1; values=Named Selection//; values count=1
    - `Projection.Source.Named Selection` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Projection.Updated At` — property

- Declaration source: `CA-R-2539@2`
  - Fenced Claim block:
```CFEL
Projection.Updated At{:1}: [datetime]{:1};
Projection.Updated At.*[]{:0};
Projection//$projection.Updated At == MAX(Event Record//(.object_output{=1}, .object_output.version{=0}, .object_output.id = $projection.ID, (.action = create OR .action = update)).happened_at)
```
  - Nested Property contracts:
    - `Projection.Updated At` property; names=None; names count=1; values=datetime; values count=1
    - `Projection.Updated At` immediate_dependents; names=; names count=0; values=None; values count=undefined
  - Unresolved CFEL: `Projection//$projection.Updated At == MAX(Event Record//(.object_output{=1}, .object_output.version{=0}, .object_output.id = $projection.ID, (.action = create OR .action = update)).happened_at)`
- Shared RMED source: `CA-R-1495@21`
  - Remaining Claim prose:
    **every** Projection has **`=1`** unambiguous Updated At date-time identifying its latest completed rebuild.
- Shared RMED source: `CA-D-310@25`
  - Remaining Claim prose:
    **every** Projection Carrier **must** serialize the time of its latest completed rebuild as `updated_at` **in** Project time **without** treating that value alone as proof of currentness.

### `Scope Unit.ID` — property

- Declaration source: `CA-R-2526@2`
  - Fenced Claim block:
```CFEL
Scope Unit.ID{:1}: [string]{:1};
Scope Unit.ID.*[]{:0}
```
  - Nested Property contracts:
    - `Scope Unit.ID` property; names=None; names count=1; values=string; values count=1
    - `Scope Unit.ID` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Scope Unit.Label` — property

- Declaration source: `CA-R-2528@2`
  - Fenced Claim block:
```CFEL
Scope Unit.Label{:0..1}: [string]{:1};
Scope Unit.Label.*[]{:0}
```
  - Nested Property contracts:
    - `Scope Unit.Label` property; names=None; names count=0..1; values=string; values count=1
    - `Scope Unit.Label` immediate_dependents; names=; names count=0; values=None; values count=undefined
- Shared RMED source: `CA-R-1382@24`
  - Remaining Claim prose:
    **every** Ordered Scope Unit **must** use Layer as its default Label.
- Shared RMED source: `CA-R-980@30`
  - Remaining Claim prose:
    **every** Unordered Scope Unit **must** use Feature as its default Label.
- Shared RMED source: `CA-R-982@32`
  - Remaining Claim prose:
    the Operator **may** replace the default Label independently for **every** Scope Unit **without** changing its Type.

### `Scope Unit.Local Order` — property

- Declaration source: `CA-R-2529@2`
  - Fenced Claim block:
```CFEL
Scope Unit.Local Order{:0..1}: [int]{:1};
Scope Unit.Local Order.*[]{:0}
```
  - Nested Property contracts:
    - `Scope Unit.Local Order` property; names=None; names count=0..1; values=int; values count=1
    - `Scope Unit.Local Order` immediate_dependents; names=; names count=0; values=None; values count=undefined

### `Scope Unit.Name` — property

- Declaration source: `CA-R-2527@2`
  - Fenced Claim block:
```CFEL
Scope Unit.Name{:1}: [string]{:1};
Scope Unit.Name.*[]{:0}
```
  - Nested Property contracts:
    - `Scope Unit.Name` property; names=None; names count=1; values=string; values count=1
    - `Scope Unit.Name` immediate_dependents; names=; names count=0; values=None; values count=undefined
- Shared RMED source: `CA-R-1297@26`
  - Remaining Claim prose:
    a Scope Unit Name **must not** equal the uppercase underscore-joined rendering of **any** word-form CCE Operator.
- Shared RMED source: `CA-R-962@29`
  - Remaining Claim prose:
    **every** Scope Unit **must** have **`=1`** authoritative Name.
- Shared RMED source: `CA-R-970@32`
  - Remaining Claim prose:
    **every** Scope Unit Name **must** be unique within its Project.
- Shared RMED source: `CA-R-971@31`
  - Remaining Claim prose:
    a readable rendering derived from a Scope Unit Name **must not** become an independent Scope Unit property **or** authority.
- Shared RMED source: `CA-M-275@21`
  - Remaining Claim prose:
    **to** write a Scope Unit Name, join nonempty uppercase letter-or-digit word tokens with single underscores.
- Shared RMED source: `CA-M-299@18`
  - Remaining Claim prose:
    **to** distinguish a Scope Unit reference from ordinary English, use its exact uppercase Scope Unit Name **to** denote the Scope Unit. an **otherwise** identical lowercase word retains its ordinary English meaning.

### `Scope Unit.Path` — property

- Declaration source: `CA-R-2530@2`
  - Remaining Claim prose:
    The Path lists Scope Unit identities along the complete declared containment chain from the root to the addressed Scope Unit.
  - Fenced Claim block:
```CFEL
Scope Unit.Path{:1}: [string]{:1+};
Scope Unit.Path.*[]{:0}
```
  - Nested Property contracts:
    - `Scope Unit.Path` property; names=None; names count=1; values=string; values count=1+
    - `Scope Unit.Path` immediate_dependents; names=; names count=0; values=None; values count=undefined
- Shared RMED source: `CA-R-1661@31`
  - Remaining Claim prose:
    **every** Structural Path **must** be derived from active Scope Unit identities **and** their declared Structural Parent Relations.
    
    a retained representation for readability **must** remain derived **and** consistent with those authoritative inputs under CA-R-1485. it **must not** independently establish **or** change structural ancestry. permitted storage follows the applicable Delivery authority; this rule does **not** admit another authored Project Structure field.
- Shared RMED source: `CA-R-1688@38`
  - Remaining Claim prose:
    Scope path is a project-relative address containing **`>=0`** operator-labeled structural scopes ordered from broader parent **to** narrower child.
    
    the current project is ambient. Scope **may** govern ownership, applicability, **and** inheritance, but it never changes stable Artifact identity, Artifact form, Content Role, **or** Governance locus.
- Shared RMED source: `CA-R-2133@10`
  - Remaining Claim prose:
    Scope Unit ancestry **must** be derived from the authoritative Project Structure parent declarations and their corresponding stored structural-parent relations. CAPRMEDIO **must not** author or persist a Structural Level property for a Scope Unit. A displayed ancestry depth or path segment, **when** materialized for readability, is derived from that parent chain only; it **must not** establish, replace, or override parentage, ownership, or authority, and unresolved or conflicting inputs remain unresolved.
- Shared RMED source: `CA-R-2134@10`
  - Remaining Claim prose:
    An Ordered Scope Unit's readable location **must** be derived from its authoritative Structural Path and applicable Local Order. CAPRMEDIO **must not** author or persist a Structural Coordinate property, and no displayed location or navigation token may establish parentage, sibling order, ownership, or Atom authority. Local Order remains the position among ordered siblings with one direct parent; ancestry remains the parent-chain fact.

### `Scope Unit.Project Boundary Position` — property

- Declaration source: `CA-R-2531@2`
  - Fenced Claim block:
```CFEL
Scope Unit.Project Boundary Position{:1}: [string]{:1};
Scope Unit.Project Boundary Position.*[]{:0}
```
  - Nested Property contracts:
    - `Scope Unit.Project Boundary Position` property; names=None; names count=1; values=string; values count=1
    - `Scope Unit.Project Boundary Position` immediate_dependents; names=; names count=0; values=None; values count=undefined
- Shared RMED source: `CA-R-844@28`
  - Remaining Claim prose:
    RELEASES **must** be the CAPRMEDIO Project Layer with Local Order `5`.
- Shared RMED source: `CA-R-975@26`
  - Remaining Claim prose:
    CORE_EXTENSIONS **must** be the CAPRMEDIO Project Layer with Local Order `4`.

### `Scope Unit.structural_level` — property

- Declaration source: `CA-R-2554@2`
  - Fenced Claim block:
```CFEL
Scope Unit.structural_level{:1}: [int]{:1};
Scope Unit.structural_level.*[]{:0};
Scope Unit.structural_level >= 0;
Scope Unit/Project//$project.structural_level = 0;
IF (Scope Unit//$contained ((IS_CONTAINED_BY)) Scope Unit//$container)
THEN ($contained.structural_level = $container.structural_level + 1)
```
  - Nested Property contracts:
    - `Scope Unit.structural_level` property; names=None; names count=1; values=int; values count=1
    - `Scope Unit.structural_level` immediate_dependents; names=; names count=0; values=None; values count=undefined
  - Unresolved CFEL: `Scope Unit.structural_level >= 0`
  - Unresolved CFEL: `Scope Unit/Project//$project.structural_level = 0`
  - Unresolved CFEL: `IF (Scope Unit//$contained ((IS_CONTAINED_BY)) Scope Unit//$container)
THEN ($contained.structural_level = $container.structural_level + 1)`

### `Term.Name` — property

- Declaration source: `CA-R-2415@3`
  - Remaining Claim prose:
    Term.Name means the required word or phrase used as the Term's meaning.
    
    ### Formal claim
  - Fenced Claim block:
```text
Term.Name[string]{1}
```
- Shared RMED source: `CA-R-1324@27`
  - Remaining Claim prose:
    a Term name **must not** contain unescaped `/`, `//`, `.`, `:`, `+>`, `<+`, `>|`, `|<`, `((`, `))`, `@`, `(`, `)`, `[`, `]`, `{`, or `}`. These are reserved Subject Expression syntax for specialization or instances, Property and allowed-value qualification, containment, classification, named Relations, calls to already declared Entities, logical grouping, direct-value Format, or cardinality. A backslash escapes a literal operator character in a name; this Rule does not ban such escaped literal name characters or invent a quote DSL. This Term-name rule does not make the RHS name after `//` a Term; that operand identifies an instance that already exists or is explicitly introduced by applicable defining authority under its separate naming/source authority. Syntax alone neither creates nor admits the instance. The lowercase `atom` keyword and its selector punctuation remain registered initial-selector syntax under CA-R-1321, not a broadened Term-name policy.

## CFEL, Carrier, and Term Component Contracts

### `CFEL <+ Cardinality` — declared component

- Declaration source: `CA-R-2243@5`
  - Semantics:
    The lowercase `atom.version_number` example illustrates logical Carrier access under CA-D-478; it is not a canonical Subject-path declaration.
    
    The same cardinality notation applies to different explicitly identified counts. `[format]` specifies a Property's direct-value Format, while a post-Property `{cardinality}` counts those direct values. A Relation's pre-operator and post-operator slots count its independent forward and reverse directions. These dimensions remain independent.
    
    Counts apply independently to direct values and never to nested keys. A YAML
    sequence carries multiple values under one unique property key; it is not a
    list value Format. A CFEL expression in the Claim is part of its direct value; a separate Formal Claim child is not required.
  - Remaining Claim prose:
    Cardinality annotations count an addressed property's direct values. Nested
    keys and their values do not contribute to the parent's count. `{n}` requires
    exactly n, `{n+}` at least n with no upper bound, and `{n..m}` the inclusive
    range n through m. Bounds are non-negative integers and n is not greater than
    m.
    
    `{0}` forbids direct values without forbidding declared child properties;
    `Atom.Subjects{0}` therefore permits its independently counted governs and
    dependency children. A Relation uses two independent directional slots:
    `Source {forward-count}RELATION{reverse-count} Target`. In
    `Step {1}+>{1+} Workflow`, the pre-operator count requires one Workflow per
    Step and the post-operator count requires one or more Steps per Workflow. The
    equivalent reverse writing is `Workflow {1+}<+{1} Step`. Neither spelling
    changes the separate exactly-one-immediate-whole rule.
    In `Source {forward-count}((RELATION_TOKEN)){reverse-count} Target`, the
    pre-operator slot counts outgoing Relation instances of that Type per source
    occurrence and the post-operator slot counts reverse links per target
    occurrence. Each actual Relation connects two nodes or node instances, its
    source and target; neither slot counts Relation arity or the two endpoints
    inside a Relation. `Property {1}((IS_PROPERTY_OF)) Bearer` constrains exactly
    one outgoing IS_PROPERTY_OF Relation per Property occurrence; it does not set
    the Property's value count. A postfix-only count would constrain the reverse
    count per Bearer instead.
    The endpoints in these schematics stand for actual full admitted Entity
    expressions, not a new Relation between kind nodes. An omitted annotation
    leaves cardinality undefined.
    
    ### Formal claim
  - Fenced Claim block:
```text
Atom/(.Content Role: Operations)/(.Type: Step) {1}+>{1+} Atom/(.Content Role: Operations)/(.Type: Workflow)
Atom/(.Content Role: Operations)/(.Type: Sub-step) {1}+>{0+} Atom/(.Content Role: Operations)/(.Type: Step)
atom.version_number[int]{1}
Atom/(.Content Role: Requirement).Content.Claim[string]{1}
Atom.Subjects{0}
Atom.Subjects.Governs[string]{1}
Atom.Subjects.Depends On[string]{0+}
```

### `CFEL <+ Format//markdown` — declared component

- Declaration source: `CA-R-2547@2`
  - Remaining Claim prose:
    The markdown Format admits Markdown source. A section value preserves its markup. Its retrieved value includes its heading and descendant sections.

## Relation Contracts

### `((DERIVED_FROM))` — declared Relation

- Declaration source: `CA-R-1639@35`
  - Remaining Claim prose:
    DERIVED_FROM means the directed Relation from a derived represented content version to an exact source content version used to derive it. Version references identify the relevant states; this does not introduce a Revision entity.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL <+ Relation//DERIVED_FROM
```

### `((HAS_ACTIVE_SUBJECT))` — declared Relation

- Declaration source: `CA-R-2479@2`
  - Remaining Claim prose:
    HAS_ACTIVE_SUBJECT links an Atom to the thing or topic named by its active Subject. Derive it from subjects.active. A Declaration addresses a Node; other Atoms are not restricted to the Node branch.
  - Fenced Claim block:
```CFEL
Atom/(.Role: Requirement)/(.Form: Declaration)// ((HAS_ACTIVE_SUBJECT)) (Node, Node/**, .**)
```
  - Allowed Relations and other formal clauses:
    - `Atom/(.Role: Requirement)/(.Form: Declaration)//` — HAS_ACTIVE_SUBJECT → `(Node, Node/**, .**)`; Host=undefined; Target=undefined
- Host / Target contracts:
  - `Atom/(.Role: Requirement)/(.Form: Declaration)//` — HAS_ACTIVE_SUBJECT → `(Node, Node/**, .**)`; Host=undefined; Target=undefined

### `((HAS_CLASSIFICATION))` — declared Relation

- Declaration source: `CA-R-2477@2`
  - Remaining Claim prose:
    HAS_CLASSIFICATION relates a Node to an applicable classification axis. `Node >| Axis` and `Axis |< Node` are opposite written views of the same fact. An axis is distinct from its value case.
  - Fenced Claim block:
```CFEL
(Node, Node/**, .**) >| Axis
```
  - Unresolved CFEL: `(Node, Node/**, .**) >| Axis`

### `((HAS_EVENT_AUTHOR))` — declared Relation

- Declaration source: `CA-R-2583@2`
  - Remaining Claim prose:
    HAS_EVENT_AUTHOR identifies the Actor who performed the recorded event.
  - Fenced Claim block:
```CFEL
Event Record// ((HAS_EVENT_AUTHOR)) Actor//;
HAS_EVENT_AUTHOR ((HAS_INVERSE)) IS_EVENT_AUTHOR_OF
```
  - Allowed Relations and other formal clauses:
    - `Event Record//` — HAS_EVENT_AUTHOR → `Actor//`; Host=undefined; Target=undefined
    - `HAS_EVENT_AUTHOR` — HAS_INVERSE → `IS_EVENT_AUTHOR_OF`; Host=undefined; Target=undefined
- Host / Target contracts:
  - `Event Record//` — HAS_EVENT_AUTHOR → `Actor//`; Host=undefined; Target=undefined
- HAS_INVERSE bindings; this does not certify an undeclared inverse Relation:
  - `((IS_EVENT_AUTHOR_OF))` — CA-R-2583@2

### `((HAS_INVERSE))` — declared Relation

- Declaration source: `CA-R-2485@2`
  - Remaining Claim prose:
    HAS_INVERSE links a direct Relation to its derived inverse. The inverse swaps the direct Relation's Host and Target. Its links are derived from the direct links and are not authored separately.
  - Fenced Claim block:
```CFEL
Relation// ((HAS_INVERSE)) Relation//
```
  - Allowed Relations and other formal clauses:
    - `Relation//` — HAS_INVERSE → `Relation//`; Host=undefined; Target=undefined
- Host / Target contracts:
  - `Relation//` — HAS_INVERSE → `Relation//`; Host=undefined; Target=undefined

### `((INSTANCE_OF))` — declared Relation

- Declaration source: `CA-R-2476@2`
  - Fenced Claim block:
```CFEL
Node// ((INSTANCE_OF)) ((Node, Node/**, .**) >| Independence = Primary Node);
INSTANCE_OF ((HAS_INVERSE)) HAS_INSTANCE
```
  - Allowed Relations and other formal clauses:
    - `Node//` — INSTANCE_OF → `((Node, Node/**, .**) >| Independence = Primary Node)`; Host=undefined; Target=undefined
    - `INSTANCE_OF` — HAS_INVERSE → `HAS_INSTANCE`; Host=undefined; Target=undefined
- Host / Target contracts:
  - `Node//` — INSTANCE_OF → `((Node, Node/**, .**) >| Independence = Primary Node)`; Host=undefined; Target=undefined
- HAS_INVERSE bindings; this does not certify an undeclared inverse Relation:
  - `((HAS_INSTANCE))` — CA-R-2476@2

### `((IS_ALLOWED_VALUE_OF))` — declared Relation

- Declaration source: `CA-R-1436@25`
  - Remaining Claim prose:
    an IS_ALLOWED_VALUE_OF Relation from value V **to** target Entity X **in** the Entities Graph **means** that governing authority admits V as a possible value of X **in** its qualified context, irrespective of X's kind or path. This Relation does **not** assign V **to** a particular occurrence **or** determine direct-value cardinality.
- Shared RMED source: `CA-R-1346@26`
  - Remaining Claim prose:
    a Term **may** occur **in** allowed-value entity names **in** multiple qualified Property contexts **when** it retains the same approved meaning **and** governing authority admits the value separately **in** **every** such context; distinct modeled entities **must** have distinct complete canonical names, **and** admission **in** one context does **not** admit the value **in** another. Within these allowed-value contexts, this permits component reuse and does not make that one Term the complete canonical entity name of another Entity.

### `((IS_CONTAINED_BY))` — declared Relation

- Declaration source: `CA-R-2478@2`
  - Remaining Claim prose:
    IS_CONTAINED_BY relates a contained Node to its immediate Container. Containment does not imply narrowing or inheritance.
  - Fenced Claim block:
```CFEL
(Node, Node/**, .**) ((IS_CONTAINED_BY)) ((Node, Node/**, .**) >| Container = yes);
IS_CONTAINED_BY ((HAS_INVERSE)) CONTAINS
```
  - Allowed Relations and other formal clauses:
    - `(Node, Node/**, .**)` — IS_CONTAINED_BY → `((Node, Node/**, .**) >| Container = yes)`; Host=undefined; Target=undefined
    - `IS_CONTAINED_BY` — HAS_INVERSE → `CONTAINS`; Host=undefined; Target=undefined
- Host / Target contracts:
  - `(Node, Node/**, .**)` — IS_CONTAINED_BY → `((Node, Node/**, .**) >| Container = yes)`; Host=undefined; Target=undefined
- HAS_INVERSE bindings; this does not certify an undeclared inverse Relation:
  - `((CONTAINS))` — CA-R-2478@2

### `((IS_PROPERTY_OF))` — declared Relation

- Declaration source: `CA-R-2473@2`
  - Remaining Claim prose:
    IS_PROPERTY_OF directs a Property to exactly one immediate bearer. HAS_PROPERTY is its derived inverse. The bearer relation is acyclic. `Bearer.Property` addresses the Property.
  - Fenced Claim block:
```CFEL
((Node, Node/**, .**) >| Independence = Property) {:1}((IS_PROPERTY_OF)) (Node, Node/**, .**);
IS_PROPERTY_OF ((HAS_INVERSE)) HAS_PROPERTY
```
  - Allowed Relations and other formal clauses:
    - `((Node, Node/**, .**) >| Independence = Property)` — IS_PROPERTY_OF → `(Node, Node/**, .**)`; Host=1; Target=undefined
    - `IS_PROPERTY_OF` — HAS_INVERSE → `HAS_PROPERTY`; Host=undefined; Target=undefined
- Shared RMED source: `CA-R-1351@22`
  - Remaining Claim prose:
    a Primary Entity referenced by a Subject **must** have **`=0`** outgoing IS_PROPERTY_OF Relations.
- Host / Target contracts:
  - `((Node, Node/**, .**) >| Independence = Property)` — IS_PROPERTY_OF → `(Node, Node/**, .**)`; Host=1; Target=undefined
- HAS_INVERSE bindings; this does not certify an undeclared inverse Relation:
  - `((HAS_PROPERTY))` — CA-R-2473@2

### `((NARROWER_THAN))` — declared Relation

- Declaration source: `CA-R-2475@2`
  - Remaining Claim prose:
    The narrower Node inherits applicable Relation and Property constraints without cloning declarations or instance facts.
  - Fenced Claim block:
```CFEL
((Node, Node/**, .**) >| Independence = Primary Node) ((NARROWER_THAN)) ((Node, Node/**, .**) >| Independence = Primary Node);
NARROWER_THAN ((HAS_INVERSE)) HAS_NARROWER
```
  - Allowed Relations and other formal clauses:
    - `((Node, Node/**, .**) >| Independence = Primary Node)` — NARROWER_THAN → `((Node, Node/**, .**) >| Independence = Primary Node)`; Host=undefined; Target=undefined
    - `NARROWER_THAN` — HAS_INVERSE → `HAS_NARROWER`; Host=undefined; Target=undefined
- Shared RMED source: `CA-R-1244@33`
  - Remaining Claim prose:
    a Term **may** have **`>=0`** direct NARROWER_THAN parents.
- Host / Target contracts:
  - `((Node, Node/**, .**) >| Independence = Primary Node)` — NARROWER_THAN → `((Node, Node/**, .**) >| Independence = Primary Node)`; Host=undefined; Target=undefined
- HAS_INVERSE bindings; this does not certify an undeclared inverse Relation:
  - `((HAS_NARROWER))` — CA-R-2475@2

### `((RUN))` — declared Relation

- Declaration source: `CA-R-2480@2`
  - Remaining Claim prose:
    RUN binds a Step or Substep to an Action for execution.
  - Fenced Claim block:
```CFEL
(in (Step, Substep))// ((RUN)) Action//;
Action// ((IS_RUN_BY)) (in (Step, Substep))//;
RUN ((HAS_INVERSE)) IS_RUN_BY
```
  - Allowed Relations and other formal clauses:
    - `(in (Step, Substep))//` — RUN → `Action//`; Host=undefined; Target=undefined
    - `Action//` — IS_RUN_BY → `(in (Step, Substep))//`; Host=undefined; Target=undefined
    - `RUN` — HAS_INVERSE → `IS_RUN_BY`; Host=undefined; Target=undefined
- Host / Target contracts:
  - `(in (Step, Substep))//` — RUN → `Action//`; Host=undefined; Target=undefined
- HAS_INVERSE bindings; this does not certify an undeclared inverse Relation:
  - `((IS_RUN_BY))` — CA-R-2480@2

### `((depends_on))` — declared Relation

- Declaration source: `CA-R-1026@30`
  - Remaining Claim prose:
    `depends_on` **means** a direct dependency-ordering relation from a dependent Artifact **to** its prerequisite Artifact, with `required_by` as its inverse-derived view. Plan start dependencies use the Plan Graph's `BLOCKS` under CA-R-1580 instead; this Relation Kind **must not** duplicate that scheduling fact.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL <+ Relation//depends_on
CFEL <+ Relation//required_by
```
- Shared RMED source: `CA-M-239@25`
  - Remaining Claim prose:
    **to** derive one non-Plan Artifact dependency order, the resolver **must**:
    
    1. construct one directed graph from direct `relations.depends_on` edges from **every** dependent Artifact **to** **every** prerequisite Artifact;
    2. derive its `required_by` inverse view **without** authoring inverse edges;
    3. calculate one deterministic prerequisite-first topological order with canonical identity **only** as a tie-breaker; **and**
    4. reject a cycle.
    
    the resolver **must not** use target-list position, Local Order, **or** `relations.derived_from` as a dependency edge.
- Shared RMED source: `CA-E-404@27`
  - Remaining Claim prose:
    the Evaluation **must** reject one derived non-Plan Artifact dependency order **if** a relation endpoint is **not** an admitted non-Plan Artifact, one `relations.depends_on` target reference repeats, a permutation of target-list positions changes its direct-edge set **or** derived order, an edge is absent from `relations.depends_on`, `relations.derived_from` contributes an edge, **or** the direct dependency graph **contains** a cycle.

## Coverage Gaps and Conflicts

- `CA-R-2256@2`: Declaration active Subject is not a declared Node, Property, Relation, or component.
- Unbound source evidence: `CA-R-2256@2`
  - Remaining Claim prose:
    CAPRMEDIO Framework is the product produced by the caprmedio Project. This Subject identifies that product and its required capabilities. Project Settings identify the Project; this project-local definition identifies its product.
    
    ### Formal claim
  - Fenced Claim block:
```text
Entity/Aspect/Product: CAPRMEDIO Framework
```
- `CA-R-881@31`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-881@31`
  - Remaining Claim prose:
    cross-unit relation ownership **must** follow the applicable relation-family authority rather than a universal common-ancestor rule; a Demand **must** be owned by its Consumer Scope Unit under CA-R-932@37 **and** **must** constrain **only** the Producer result that Consumer is permitted **to** depend on, with the applicable ancestry **and** ordered-sibling restrictions preserved.
- `CA-E-436@26`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-E-436@26`
  - Remaining Claim prose:
    the Graph of Graphs connectivity Evaluation **must** return `fail` **if** a governed Artifact **or** delivered Implementation element has no recoverable location **or** no valid connection **to** the shared connected whole; a connection **may** cross graph boundaries, **and** specialized Methodology, Engine, **or** other Scope Unit checks **may** supply evidence **to** this Evaluation. apply cycle restrictions **only** **to** graph families whose authority requires them; connectivity **must not** impose universal acyclicity.
- `CA-R-1016@28`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1016@28`
  - Remaining Claim prose:
    `rationale_for` **means** the direct relation from a Rationale Analysis Atom
    to the Atom that it explains.
- `CA-R-1017@28`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1017@28`
  - Remaining Claim prose:
    `method_for` **means** the direct relation from a Method Atom to the
    Requirement Atom that the Method serves.
- `CA-R-1018@35`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1018@35`
  - Remaining Claim prose:
    `evaluation_for` **means** the direct relation from an Evaluation Atom to an
    Atom whose authority the Evaluation checks.
- `CA-R-1019@27`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1019@27`
  - Remaining Claim prose:
    `delivery_for` **means** the direct relation from a Delivery Atom to the Atom
    that the Delivery realizes.
- `CA-R-1020@27`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1020@27`
  - Remaining Claim prose:
    `implementation_of` **means** the direct relation from an Implementation
    carrier to the specification Atom that it implements.
- `CA-R-1021@27`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1021@27`
  - Remaining Claim prose:
    `evidence_for` **means** the direct relation from an Evidence carrier to the
    carrier that the Evidence supports.
- `CA-R-1022@29`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1022@29`
  - Remaining Claim prose:
    `concern_about` **means** the direct relation from a Concern Atom to the
    governed entity that it concerns.
- `CA-R-1023@24`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1023@24`
  - Remaining Claim prose:
    an Atom **may** declare `derived_from` **and** another registered direct relation **when** the two relations express different direct facts.
- `CA-R-1024@25`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1024@25`
  - Remaining Claim prose:
    a registered direct relation **must not** imply a transitive relation.
- `CA-R-1025@25`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1025@25`
  - Remaining Claim prose:
    **every** additional direct relation meaning **must** have separate owning Requirement authority instead of reusing a registered relation with a different meaning.
- `CA-R-1027@26`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1027@26`
  - Remaining Claim prose:
    `implementation_of` **must** be registered as the declared upstream relation **and** `implemented_by` as its inverse-derived downstream relation **in** the realization ordering domain.
- `CA-R-1029@24`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1029@24`
  - Remaining Claim prose:
    **every** Lineage Impact disposition **must** preserve the examined parent Revision, the examined child Revision, the selected disposition, **and** **any** resulting child Revision **or** blocking Concern Atom.
- `CA-R-1030@24`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1030@24`
  - Remaining Claim prose:
    TOOLING **must not** select `update_required`, `replacement_required`, **or** `uncertain` **without** an explicit governed disposition.
- `CA-R-1032@25`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1032@25`
  - Remaining Claim prose:
    **every** release **or** downstream gate that requires a revised Atom **must** remain blocked **until** its Lineage Impact Analysis concludes that **every** affected branch has reached a fixed point.
- `CA-R-1038@25`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1038@25`
  - Remaining Claim prose:
    **`=1`** Lineage Impact Analysis Atom **may** contain multiple child rows **when** **every** row supports its one primary conclusion that the changed parent Revision's Impact Review is complete **or** blocked.
- `CA-R-1039@25`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1039@25`
  - Remaining Claim prose:
    a Lineage Impact Analysis Atom **must not** replace an examined child, supporting Evidence, **or** another Atom's Claim.
- `CA-R-1040@28`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1040@28`
  - Remaining Claim prose:
    validators **must** reject **every** inverse typed relation authored **in** an Atom Carrier.
- `CA-R-117@29`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-117@29`
  - Remaining Claim prose:
    **every** semantic relation **must** have **`=1`** authoritative declaration.
- `CA-R-118@33`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-118@33`
  - Remaining Claim prose:
    the dependent Atom **must** own the **`=1`** authoritative declaration of its direct semantic relation.
- `CA-R-1199@34`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1199@34`
  - Remaining Claim prose:
    GOVERNS **means** the direct Subject Relation Kind from an Atom **to** the canonical Subject graph node about which the Atom governs through its applicable role-specific content.
- `CA-R-1200@37`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1200@37`
  - Remaining Claim prose:
    DEPENDS_ON **means** the direct Subject Relation Kind from an Atom **to** a canonical Subject graph node mentioned **in** its applicable role-specific content or other registered content, other than its GOVERNS target. this reference does **not** make the Atom's content—or every Governing Configuration fact—authoritative about that Subject graph node; formal authority depends on the applicable registered content form and role. a formal Claim may be carried in Markdown, structured YAML, or Governing Configuration, but Governing Configuration facts are not automatically Atom Claims.
- `CA-R-121@29`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-121@29`
  - Remaining Claim prose:
    **every** declared semantic relation **must** connect its two named participants through one registered immediate meaning.
- `CA-R-1243@27`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1243@27`
  - Remaining Claim prose:
    BEARS **must** be the derived inverse view of IS_BORNE_BY **in** the Entities Graph **and** **must not** be another primitive Relation Kind of that graph.
- `CA-R-1246@32`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1246@32`
  - Remaining Claim prose:
    Relation Type names are shared across CAPRMEDIO Graphs and unique within the Project. A Relation Type is not owned by a graph kind. Existing Entity Definition constraints, where applicable, supply graph-specific endpoint classes, endpoint graph contexts, cardinality, permissions, and prohibitions for that shared Type. They do not create graph-owned Type copies or impose a new per-Type/per-graph admission registry; this contract chooses neither default allow nor default deny.
    
    instances of the same graph kind governed by the same Applicable Methodology **must** reuse the same defining Relation Type authority and any applicable Entity Definition constraints. Matching names identify the shared Type; they do not create interchangeable copies or erase graph-specific constraints.
    
    where an Entity Definition constraint applies, it determines graph-specific endpoint constraints, **not** a requirement that all endpoints occupy the same graph. admitted cross-graph endpoints and source references under CA-R-1472 retain their endpoint identity and source traceability. another graph **may** represent a source-traceable reference **or** view of the Relation **without** creating a graph-specific Type copy.
- `CA-R-1260@34`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1260@34`
  - Semantics:
    Primary means that identity does not require another Entity occurrence as bearer. Dependent means that identity requires an immediate bearer, as expressed by IS_BORNE_BY. These describe bearer dependence, not additional taxonomy branches. An absent edge in an incomplete view does not establish independence.
  - Remaining Claim prose:
    an IS_BORNE_BY Relation from Entity A **to** Entity B **in** the Entities Graph **means** that A is a Dependent Entity whose identity requires B as its immediate bearer.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Relation//IS_BORNE_BY
CFEL > Relation//BEARS
```
- `CA-R-1280@32`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1280@32`
  - Remaining Claim prose:
    an Atom's Subjects, **when** present, **must** be exactly the distinct canonical Subject Targets independently mentioned **in** its Markdown Main Content, **not** an Atom citation label rendered under `CA-M-444-CORE_META_MODEL-METHOD--make-atom-claims-easy-to-understand` as the referenced Atom's complete filename **without** its `.md` extension **or** directory path: zero **or** one GOVERNS target for its Claim, **and** DEPENDS_ON targets for **every** other mentioned Subject Target.
- `CA-R-1345@27`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1345@27`
  - Remaining Claim prose:
    the NARROWER_THAN graph **must** remain acyclic.
- `CA-R-1437@28`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1437@28`
  - Remaining Claim prose:
    **every** independently authored Relation fact **must** have **`=1`** authoritative source declaration under Single Source of Truth. its representation **in** multiple CAPRMEDIO Graph views remains a reference **or** derived Projection of that declaration **without** creating another independently maintained source.
    
    a Relation derived under admitted derivation authority **must** remain traceable **to** that authority **and** its authoritative input facts, including through upstream Projections. it does **not** require a fabricated direct source declaration for the derived result. this distinction **must not** weaken a Relation Kind's requirement for an explicit source fact **or** permit unsupported inference.
- `CA-R-1472@26`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1472@26`
  - Remaining Claim prose:
    a secondary CAPRMEDIO Graph **may** represent typed Relations between its own nodes, **to** another secondary graph **or** its nodes, **and** **to** source Atoms **or** other admitted authoritative sources.
    
    **every** connection **must** identify **`=1`** shared project-unique Relation Type under its defining authority, with its declared direction preserved, **and** must conform to any applicable governing Entity Definition endpoint-class, endpoint-graph-context, **and** cardinality constraints. a graph-qualified reference **or** context may qualify that connection without creating graph-owned Type identity. crossing a graph boundary **must not** create a graph-specific Type identity, import a foreign Relation Type as native, **or** make a referenced external endpoint a native node of the receiving graph. a cross-graph reference preserves the referenced endpoint identity **and** source traceability **without** copying its source fact into independent authority. these permissions do **not** create a Relation Type definition **or** authorize inference beyond the defining authority and applicable Rules.
- `CA-R-1569@23`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1569@23`
  - Remaining Claim prose:
    A leaf Step launches exactly one referenced Action or Workflow with its parameters and input bindings. A Sub-step launches an Action only. A Step containing ordered Sub-steps has no Action or Workflow call of its own; a Sub-step cannot contain further Sub-steps.
- `CA-R-1580@24`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1580@24`
  - Remaining Claim prose:
    **in** the Plan Graph, `A BLOCKS B` **means** that Plan `B` may start only
    after Plan `A` is Done. An inverse lookup is derived from the same explicit
    fact and is not separately authored; Subject DEPENDS_ON remains distinct.
- `CA-R-1632@32`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1632@32`
  - Remaining Claim prose:
    **when** an Atom receives a new accepted Revision, **every** directly dependent child reached by the Impact Review **must** receive **`=1`** disposition from (`compatible`, `update_required`, `replacement_required`, `uncertain`).
- `CA-R-1643@38`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1643@38`
  - Remaining Claim prose:
    the allowed values of `Work Journal/Event/Type` **must** be (Started, Progressed, Completed, Failed, Interrupted, Abandoned, Recovered).
- `CA-R-1644@35`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1644@35`
  - Remaining Claim prose:
    a `recovered` Journal event is admissible **only** for facts established by **any** of:
    
    - observed Carrier state;
    - preserved history;
    - Artifact movement;
    - native targets;
    - review records; **or**
    - bounded session state.
    
    unresolved Actor, time, intent, scope, **or** outcome **must** remain explicit uncertainty rather than fabricated history.
- `CA-R-1654@35`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1654@35`
  - Remaining Claim prose:
    `feature_realization` **must** be registered as a typed relation that maps a declared SPEC Feature Scope Unit **to** its applicable native Realization targets **without** making those targets Scope Units.
- `CA-R-1657@30`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1657@30`
  - Remaining Claim prose:
    the directed graph formed by active `structural_parent` relations **must** be acyclic.
- `CA-R-1659@28`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1659@28`
  - Remaining Claim prose:
    CAPRMEDIO **must** derive the inverse `structural_children` view from stored `structural_parent` relations **and** **must not** persist that inverse separately.
- `CA-R-1660@33`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1660@33`
  - Remaining Claim prose:
    the Structural Parent Relation **must** be the kind-independent Structural ownership relation directed from a child **to** its immediate parent. Project Structure owns Scope Unit parent declarations; structural graph views derive the corresponding `structural_parent` edge **without** maintaining a second source. a Carrier's physical containment **must not** silently replace a declared logical parent.
- `CA-R-1676@34`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1676@34`
  - Remaining Claim prose:
    **if** a direct relation is authored by a Current Atom with Content Role **in** (Requirement, Method, Evaluation, Delivery) **and** targets an Atom with Content Role **in** (Requirement, Method, Evaluation, Delivery), **then** the target Atom **must** be Current.
- `CA-R-1697@33`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1697@33`
  - Remaining Claim prose:
    **every** CAPRMEDIO traceability assertion **must** identify the exact governed claim revision on which a receiving artifact, implementation target, evaluation use, delivery action, operational observation, **or** other governed result relies.
- `CA-R-1699@34`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1699@34`
  - Remaining Claim prose:
    **every** governed change forms one directed provenance transaction from exact parent Artifact revisions **to** the governed Artifacts **or** native targets created **or** revised by that change.
- `CA-R-1735@25`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1735@25`
  - Remaining Claim prose:
    **every** persisted transition between self-improvement stages **must** be represented by a typed relation owned by the receiving artifact.
- `CA-R-1992@13`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1992@13`
  - Remaining Claim prose:
    `Atom/Content Role: Operations/Type: Step.Enabled Relations.Contains` **must** be True. a Step Atom **may** contain other Step Atoms. a containing Step with substeps has no own Action launch.
- `CA-R-1993@17`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-1993@17`
  - Remaining Claim prose:
    CARRIES **means** the directed Relation from a Carrier **to** the non-ephemeral Entity that it stores **or** represents.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Relation//CARRIES
CFEL > Relation//IS_CARRIED_BY
```
- `CA-R-2170@7`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2170@7`
  - Remaining Claim prose:
    `IS_DERIVED_RELATION_OF` **means** a direct relation from one derived Relation
    Type instance to one source Relation Type instance from which its relation
    meaning is derived.
- `CA-R-2245@5`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2245@5`
  - Semantics:
    Workflow Run ((IS_EXECUTION_OF)) Workflow
    
    The reusable definition is not the execution itself. Workflow Run's binding to
    one Workflow belongs in the Workflow Run Entity Definition, not in every use
    of this Relation Type.
  - Remaining Claim prose:
    IS_EXECUTION_OF connects an actual execution to the reusable definition being
    executed. The stored direction is Workflow Run to Workflow. HAS_EXECUTION is
    its declared derived inverse, not a second stored fact.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Relation//IS_EXECUTION_OF
CFEL > Relation//HAS_EXECUTION
```
- `CA-R-2246@5`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2246@5`
  - Semantics:
    Event Record ((RECORDS)) Workflow Run
    
    A Workflow Run is one recorded occurrence kind, not the only one. The Event
    Record persists independently of that Occurrent. This Definition imposes no
    record-count constraint.
  - Remaining Claim prose:
    RECORDS connects an Event Record to the actual occurrence described by that
    record. The stored direction is Event Record to the actual Event or execution it records. IS_RECORDED_BY
    is its declared derived inverse, not a second stored fact.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Relation//RECORDS
CFEL > Relation//IS_RECORDED_BY
```
- `CA-R-2247@3`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2247@3`
  - Semantics:
    RECORDS can be reused for different Event Record/occurrence pairs. Defining a
    named Type neither creates an actual run, record, or edge nor requires a
    separate Relation ID or primary branch.
  - Remaining Claim prose:
    Relation defines the structure of reusable Relation Types. A named instance
    such as `Relation//RECORDS` or `Relation//IS_EXECUTION_OF` is a reusable Type
    that can connect many endpoint pairs. A Type has a canonical Name and Meaning;
    its direction, derived inverse, and transitivity meaning describe the Type,
    not one actual edge.
    
    An actual directed connection is the tuple (source, Relation Type, target).
    The source reference identifies where the connection starts; the target reference identifies where it ends. These endpoint references belong to the actual connection, not to the reusable Type. Persist each direct fact once; a declared inverse is derived.
    Endpoint permissions, structural constraints, and counts belong in governing
    Entity Definitions rather than being inferred from a Type name.
    
    ### Formal claim
  - Fenced Claim block:
```text
Relation.Name[string]{1}
Relation.Meaning[string]{1}
```
- `CA-R-2248@2`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2248@2`
  - Semantics:
    In `atom.version_number[int]`, `int` identifies the integer value Format. A
    format annotation does not itself impose uniqueness. Markdown, YAML, TOML, and
    JSON are Carrier representation formats, not members of this value-type branch.
  - Remaining Claim prose:
    A Value Format defines the admissible type of each direct property value,
    separately from its cardinality. Neither list nor map is a value Format: YAML
    sequences carry multiple values and mappings carry declared child properties.
    `ref` is not a value Format; identifying values use string while their
    Definitions state what they identify. Nested properties have independent value
    formats and counts.
    
    Data Type names the value domain. Uniqueness Selection identifies the
    comparison population. YAML null and an empty string each count as one direct
    value when present; Format and prose conditions determine admissibility.
    
    ### Formal claim
  - Fenced Claim block:
```text
Format.Data Type[string]{1}
Format.Uniqueness Selection[string]{0..1}
```
- `CA-R-2249@3`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2249@3`
  - Semantics:
    bool is the value domain selected by a `[bool]` annotation on one direct
    property value.
  - Remaining Claim prose:
    The bool Value Format admits Boolean values: true and false. It does not set a
    property's cardinality, default, nullability, or carrier representation.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Format/bool
```
- `CA-R-2250@3`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2250@3`
  - Semantics:
    int is the value domain selected by an `[int]` annotation on one direct
    property value.
  - Remaining Claim prose:
    The int Value Format admits integer numeric values with no fractional part. It
    does not set a numeric range, cardinality, uniqueness rule, or carrier
    representation.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Format/int
```
- `CA-R-2251@3`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2251@3`
  - Semantics:
    float is the value domain selected by a `[float]` annotation on one direct
    property value.
  - Remaining Claim prose:
    The float Value Format admits floating-point numeric values. It does not set
    precision, a numeric range, cardinality, uniqueness, or carrier
    representation.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Format/float
```
- `CA-R-2252@3`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2252@3`
  - Semantics:
    decimal is the value domain selected by a `[decimal]` annotation on one direct
    property value.
  - Remaining Claim prose:
    The decimal Value Format admits decimal numeric values. It does not set scale,
    precision, a numeric range, cardinality, uniqueness, or carrier
    representation.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Format/decimal
```
- `CA-R-2253@3`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2253@3`
  - Semantics:
    string is the value domain selected by a `[string]` annotation on one direct
    property value.
  - Remaining Claim prose:
    The string Value Format admits textual string values. It does not turn null
    into a string or set a property’s cardinality, uniqueness, or carrier
    representation.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Format/string
```
- `CA-R-2254@3`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2254@3`
  - Semantics:
    datetime is the value domain selected by a `[datetime]` annotation on one
    direct property value.
  - Remaining Claim prose:
    The datetime Value Format admits date-and-time values. It does not set a
    timezone convention, precision, cardinality, uniqueness, or carrier
    representation.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Format/datetime
```
- `CA-R-2255@6`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2255@6`
  - Remaining Claim prose:
    EXECUTES connects an actual Runtime to a Workflow Run it executes. The stored direction is Runtime to Workflow Run. IS_EXECUTED_BY is its declared derived inverse and is not a second stored fact.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Relation//EXECUTES
CFEL > Relation//IS_EXECUTED_BY
```
- `CA-R-2257@2`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2257@2`
  - Remaining Claim prose:
    The scalar Value Format admits a direct primitive value, including string, numeric, Boolean, date/time and null values supported by the declared Carrier. Sequences and mappings remain carrier structures: sequence members are counted individually, while child mapping keys are not direct values of their parent. Specific value Formats can restrict this broad domain.
    
    ### Formal claim
  - Fenced Claim block:
```text
Format/scalar
```
- `CA-R-2279@2`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2279@2`
  - Remaining Claim prose:
    IS_DEFINED_BY is the derived counterpart of the defining GOVERNS links qualified by the Entity Definition ownership rule. It reuses that main link and its qualification; it adds no independently stored reverse fact.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Relation//IS_DEFINED_BY
```
- `CA-R-2327@3`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2327@3`
  - Remaining Claim prose:
    Cardinality is Graph Syntax for expressing the allowed number of direct values or contained parts.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Entity/Cardinality
```
- `CA-R-2328@3`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2328@3`
  - Remaining Claim prose:
    Format is Graph Syntax for expressing the value domain of a direct property value.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Entity/Format
```
- `CA-R-2329@3`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2329@3`
  - Remaining Claim prose:
    Relation is Graph Syntax for expressing a named directed connection and its derived counterpart.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Entity/Relation
```
- `CA-R-2352@2`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2352@2`
  - Remaining Claim prose:
    A Format Data Type names the admissible value domain of each direct property value, separately from cardinality. The initial vocabulary is provisional; list, map and reference semantics remain prose under the governing format definition.
    
    ### Formal claim
  - Fenced Claim block:
```text
Format.Data Type[string]{1}
```
- `CA-R-2353@2`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2353@2`
  - Remaining Claim prose:
    A Format Uniqueness Selection identifies the comparison population for a property uniqueness check; it is optional and does not itself impose uniqueness or define a notation.
    
    ### Formal claim
  - Fenced Claim block:
```text
Format.Uniqueness Selection[string]{0..1}
```
- `CA-R-2354@2`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2354@2`
  - Remaining Claim prose:
    A reusable Relation Type Meaning is its canonical meaning; direction, derived inverse and transitivity describe the Type rather than any one actual edge. Actual source and target endpoints remain tuple facts.
    
    ### Formal claim
  - Fenced Claim block:
```text
Relation.Meaning[string]{1}
```
- `CA-R-2355@2`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2355@2`
  - Remaining Claim prose:
    A reusable Relation Type Name is its canonical name. The named Type may connect many endpoint pairs; an actual edge remains the source/Type/target tuple and does not create a separate Relation ID.
    
    ### Formal claim
  - Fenced Claim block:
```text
Relation.Name[string]{1}
```
- `CA-R-2416@2`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2416@2`
  - Remaining Claim prose:
    BEARS is the declared derived inverse of IS_BORNE_BY; its full bearer-dependence meaning remains in CA-R-1260. No independently stored reverse fact is introduced.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Relation//BEARS
```
- `CA-R-2417@2`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2417@2`
  - Remaining Claim prose:
    HAS_EXECUTION is the declared derived inverse of IS_EXECUTION_OF; its full execution-binding meaning remains in CA-R-2245. No independently stored reverse fact is introduced.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Relation//HAS_EXECUTION
```
- `CA-R-2418@2`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2418@2`
  - Remaining Claim prose:
    IS_CARRIED_BY is the declared inverse of CARRIES; its full Carrier-binding meaning remains in CA-R-1993. No independently stored reverse fact is introduced.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Relation//IS_CARRIED_BY
```
- `CA-R-2420@2`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2420@2`
  - Remaining Claim prose:
    IS_EXECUTED_BY is the declared derived inverse of EXECUTES; its full Runtime-to-Workflow Run meaning remains in CA-R-2255. No independently stored reverse fact is introduced.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Relation//IS_EXECUTED_BY
```
- `CA-R-2421@2`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2421@2`
  - Remaining Claim prose:
    IS_RECORDED_BY is the declared derived inverse of RECORDS; its full Event Record meaning remains in CA-R-2246. No independently stored reverse fact is introduced.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Relation//IS_RECORDED_BY
```
- `CA-R-2422@2`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-2422@2`
  - Remaining Claim prose:
    required_by is the inverse-derived view of depends_on; its full dependency-ordering meaning remains in CA-R-1026. No independently stored reverse fact is introduced.
    
    ### Formal claim
  - Fenced Claim block:
```text
CFEL > Relation//required_by
```
- `CA-R-796@41`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-796@41`
  - Remaining Claim prose:
    child_of is the directed governing connection from a child Atom to the parent Atom whose Claim governs that child's contribution. It is distinct from containment, dependency, classification and source-layer membership. The Atom definition CA-R-2508 and ordering definition CA-R-2149 govern endpoint admission and ordering. This definition preserves the existing relation until its separate replacement Epic; it does not migrate its actual links.
- `CA-R-806@40`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-806@40`
  - Remaining Claim prose:
    The canonical name and meaning of each Relation Type **are** defined in its governing R Claim(s). A governing Claim **may** state a relevant inverse, derivation, or transitivity rule; no such optional property is required when it is not relevant.
- `CA-R-807@31`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-807@31`
  - Remaining Claim prose:
    replacement **or** absorption history **must** be recorded **only** **in** the authoritative Journal event that archives the predecessor. the authoritative Journal event that archives the predecessor **must** name the explicit predecessor Atom ID **and** **`>=1`** already active successor Atom IDs. active current-state Atom relations **must not** carry replacement history. formal `replaced_by` **and** `replacement_of` relation realization **must** remain deferred, **and** **any** later replacement navigation **must** be derived from immutable Journal **and** archive history under separately admitted authority.
- `CA-R-808@32`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-808@32`
  - Remaining Claim prose:
    **every** declared relation **must** satisfy the target position **and** ordering domain registered for its relation family. Stored governing RMED relation occurrences selected by CA-R-2148@10 **must** use the numeric Tier-and-Scope ordering in CA-R-2149: a same-Scope target **must** have a strictly lower numeric Tier, a target in a strict ancestor Scope Unit is accepted without Tier comparison, the exact one-way Project Configuration-to-Core Meta-Model logical-role prerequisite declared by CA-R-1218@31 is accepted without Tier comparison, and every other descendant **or** sibling target is forbidden. Temporal relations **must** use lifecycle succession, realization relations **must** use realization order, dependency relations **must** use dependency order, **and** **every** other admitted domain **must** use its own registered order. a universal upstream **or** downstream rule **must not** be inferred across different ordering domains, **and** an inverse-derived view **must not** create another declared edge.
- `CA-R-879@30`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-879@30`
  - Remaining Claim prose:
    `child_of` **must** be registered as the declared upstream relation **and** `parent_of` as its inverse-derived downstream relation **in** the normative-authority ordering domain.
- `CA-R-915@30`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-915@30`
  - Remaining Claim prose:
    the Local Order of two Scope Units **or** the position of one canonical target reference **in** `relations.<RELATION_KIND>` **must not** establish **or** alter a dependency between related Governed Entities.
- `CA-R-916@35`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-916@35`
  - Remaining Claim prose:
    **if** a Demand Atom's Consumer Atom Scope Unit **and** Producer Claim Target Scope Unit are ordered siblings, **then** its Producer Claim Target Scope Unit **must** precede its Consumer Atom Scope Unit.
- `CA-R-934@28`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-934@28`
  - Remaining Claim prose:
    a Demand Atom **must not** constrain Producer authority outside the exact Implementation result named by the Demand Atom.
- `CA-R-935@35`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-935@35`
  - Remaining Claim prose:
    a Demand Atom's Claim Target Scope Unit **must not** be an ancestor **or** descendant of its Consumer Scope Unit.
- `CA-R-945@36`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-945@36`
  - Remaining Claim prose:
    For a producer-to-consumer result flow expressed by an existing Relation, direction must run from the Producer Claim Target Scope Unit to the Consumer Atom Scope Unit.
- `CA-R-976@29`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-R-976@29`
  - Remaining Claim prose:
    a Navigational Order Number **must not** establish **or** change Scope Unit parentage, ancestry/path, Type, Local Order, Atom Tier, **or** dependency. It is a presentation value and cannot create a persisted Structural Coordinate or Structural Level.
- `CA-E-462@31`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-E-462@31`
  - Remaining Claim prose:
    the Evaluation **must** check whether an Atom replacement satisfies CA-R-807. Journal acceptance is **not** proof that the replacement is correct.
- `CA-E-496@20`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-E-496@20`
  - Remaining Claim prose:
    the Evaluation **must** check Tool-call evidence within a Step Run under CA-R-1528.
- `CA-E-620@31`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-E-620@31`
  - Remaining Claim prose:
    the registered relation vocabulary lets an independent assessor select the governed relation for representative artifact pairs **without** inventing another kind.
- `CA-E-622@49`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-E-622@49`
  - Remaining Claim prose:
    **every** known Relation Type accepts valid examples under its defining Claim; any applicable Entity Definition constraint supplies additional source/target, cardinality, lifecycle, or other constraints. reject unknown Types and violations of explicit applicable constraints, while retaining missing or conflicting constraint evidence as unresolved without choosing default allow or default deny.
- `CA-D-266@27`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-D-266@27`
  - Remaining Claim prose:
    `CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting **must not** be persisted as independent relation declarations.
- `CA-D-268@28`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-D-268@28`
  - Remaining Claim prose:
    **every** authored direct semantic relation **must** be serialized once under `relations.<RELATION_KIND>` on the Atom that owns its declared direction as a nonempty unordered collection of unique canonical target references; target position **must not** add, remove, **or** alter a direct relation **or** dependency. source-file target order is nonsemantic; validation **must not** require canonical sorting **or** order normalization. each Relation Kind's direction, endpoint validity **and** other declared semantics remain applicable.
- `CA-D-338@27`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-D-338@27`
  - Remaining Claim prose:
    **every** completed Projection Rebuild Event **must** serialize the published Projection Updated At value, output Carrier reference, **and** content digest.
- `CA-D-340@31`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-D-340@31`
  - Remaining Claim prose:
    Work Journal Event serialization **must** preserve the properties actually supplied as observations through safe encoding; reading **must** return stored properties as recorded.
    
    - preserve supplied identities, Types, action Kinds, Authors, times, session provenance, Scope, identifiers, filenames, paths **and** other values **when** present. do **not** invent missing values **or** rewrite them **to** satisfy current naming **or** classification rules.
    - an Atom ID **or** other observed property is payload data, **not** a Project-conformance judgment, permission **or** proof of correct execution.
    - do **not** impose required-field, event-identity, schema, digest, prior-history, chain, receipt, deduplication, retry **or** recovery admission **to** append/read.
    - retain existing historical representations **and** bytes **without** migration, repair **or** synthetic baselines. ordinary serialization/read failure is reported truthfully, **not** converted into fabricated data.
- `CA-D-471@22`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-D-471@22`
  - Remaining Claim prose:
    **every** explicit `A BLOCKS B` fact **must** be stored once on Plan `A` under `relations.blocks`, as a unique canonical Atom ID for Plan `B`; an omitted list encodes **`=0`** outgoing blocking Relations.
    
    - do **not** store a separate inverse list.
    - do **not** encode Plan scheduling with `relations.depends_on` **or** `subjects.depends_on`.
    - store Plan containment separately on the child under `IS_CONTAINED_BY`, with `CONTAINS` derived; do **not** derive blocking from containment **or** directory order.
- `CA-R-1213@38`: Declaration active Subject is not a declared Node, Property, Relation, or component.
- Unbound source evidence: `CA-R-1213@38`
  - Remaining Claim prose:
    Member identifies a projected Atom member by its source identity and Version; these references identify the members without changing their content or making the Projection authoritative. Each projected member retains the exact source relation required by CA-R-1314.
    
    the Applicable Methodology **must** be a non-authoritative Reconciled Projection compiled by direct, content-preserving derivation from current active Atom Revisions **in** selected Methodology Source Scope Units, preserving the selected source Atoms **and** their final selected Revisions unchanged. Applicable Methodology is **not** a Scope Unit **and** **must not** be the Claim Target Scope Unit of a Goal Atom.
    
    direct **and** content-preserving describe this derivation, **not** a Carrier persistence strategy; its Reconciled Projection classification does **not** select such a strategy. trace metadata **may** be added **to** projected Carriers **only** as governed by applicable Delivery authority, **without** changing the source Atom Revision **or** its Claim authority.
    
    ### Formal claim
  - Fenced Claim block:
```text
Entity/Object/Continuant/Projection/Type: Applicable Methodology.Member[string]{0+}
```
- `CA-R-1373@27`: Declaration active Subject is not a declared Node, Property, Relation, or component.
- Unbound source evidence: `CA-R-1373@27`
  - Remaining Claim prose:
    an Applicable Methodology/Conflict **means** one compiler-detected incompatible candidate selection within one exact Applicable Methodology source frontier.
    
    ### Formal claim
  - Fenced Claim block:
```text
Entity/Object/Continuant/Projection/Type: Applicable Methodology.Conflict{0}
```
- `CA-R-1616@21`: Declaration active Subject is not a declared Node, Property, Relation, or component.
- Unbound source evidence: `CA-R-1616@21`
  - Remaining Claim prose:
    Realization Graph **means** a non-authoritative Projection of Entities **and** typed Relations derived from a declared selection of existing Implementation sources **and** available evidence, used **to** understand that Implementation **and** support reverse engineering into proposed RMED.
    
    - the Projection **must** retain source traceability under CA-R-2535 **and** generation identity under CA-R-1493, using **only** the source kinds selected for the job; legacy Implementation need **not** have pre-existing RMED **or** Journal records.
    - missing evidence **and** uncertain interpretations **must** be reported. observed structure **or** behavior does **not** establish intended Requirements, a passed Evaluation, **or** completeness outside the checked selection.
    - the Artifact kind remains Projection, including **when** delivered as an Implementation output under CA-R-1568. views derive from its source-backed facts **without** creating another source of truth.
- `CA-R-1889@15`: Declaration active Subject is not a declared Node, Property, Relation, or component.
- Unbound source evidence: `CA-R-1889@15`
  - Remaining Claim prose:
    an FPF Analysis Report **means** a specialized Analysis Report whose bounded inquiry **or** interpretation product records an FPF analytical command, composition, **or** directly related analytical follow-up, retaining its findings **and** stated evidence limits as reporting content rather than adopting them as normative authority.
- `CA-R-2272@3`: Declaration active Subject is not a declared Node, Property, Relation, or component.
- Unbound source evidence: `CA-R-2272@3`
  - Remaining Claim prose:
    A Canonical Signature Projection reports the canonicalized CCE signatures of selected source expression occurrences, their exact source frontier and exclusions. It is a derived external report, not an Atom or proof that two Claims are equivalent. Its input evidence and delivery remain governed by CA-D-346 and the existing canonicalization rules.
    
    ### Formal claim
  - Fenced Claim block:
```text
Entity/Object/Continuant/Projection/Type: Canonical Signature
```
- `CA-R-2277@2`: Declaration active Subject is not a declared Node, Property, Relation, or component.
- Unbound source evidence: `CA-R-2277@2`
  - Remaining Claim prose:
    Extension Sources is the named Selection of immutable installed Extension source Atoms available as candidate inputs to methodology compilation. Membership establishes availability, not activation. Framework Settings separately selects activation and the installed source version for an Extension; Applicable Methodology separately includes only sources applicable under those settings.
    
    ### Formal claim
  - Fenced Claim block:
```text
Entity/Object/Continuant/Selection//Extension Sources
```
- `CA-E-465@23`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-E-465@23`
  - Remaining Claim prose:
    the selected schema-version `3` replacement Event Carrier satisfies CA-D-435-PROJECT_CONFIGURATION-DELIVERY--serialize-atom-replacement-event-references **without** treating Project conformance as storage integrity.
- `CA-D-435@23`: unexpected reserved character or trailing expression
- Unbound source evidence: `CA-D-435@23`
  - Remaining Claim prose:
    Journal serialization **must** preserve the actually supplied predecessor **and** successor Atom references of a replacement observation, including `predecessor_atom_id` **and** `successor_atom_ids` **when** supplied.
    
    - preserve reference values **and** array order as data through safe encoding. array order does **not** establish priority **or** execution order.
    - do **not** look up an earlier Journal record, require a predecessor chain, compute a digest, validate the replacement **or** fabricate a baseline **to** append these observations.
    - absence of replacement references does **not** establish whether the action was a replacement. do **not** infer missing identities, successors **or** historical facts.
    - existing records remain readable **without** rewriting their fields, selected representation **or** observed values. legacy **or** nonconforming values remain observations, **not** certified replacements.
    - actual source replacement, exact predecessor history **and** successor correctness remain independently governed by CA-R-807 **and** CA-E-462. Journal append **or** read grants no source-effect permission **and** proves none of those conditions.
- `CA-R-2469@2`: unterminated logical group
- Unbound source evidence: `CA-R-2469@2`
  - Remaining Claim prose:
    Evaluate ownership within the selected effective MODEL. Each member selected by (Node, Node/**, .**), including the root and each Property, has exactly one effective Current authoritative Requirement/Form: Declaration addressing that Node.
    
    Count inherited Current Declarations and explicit local replacements after MODEL override resolution. A replaced base Declaration remains available in its base MODEL and is not a second effective owner in the local MODEL. Drafts and archives are not Current owners. Other Atoms may address the same Node.
    The count uses only the effective Current Declaration-to-Node links in that MODEL. HAS_ACTIVE_SUBJECT is derived from the dedicated Subject field.
  - Fenced Claim block:
```CFEL
Atom/(.Role: Requirement)/(.Form: Declaration)// ((HAS_ACTIVE_SUBJECT)){:1} (Node, Node/**, .**)
```
  - Allowed Relations and other formal clauses:
    - `Atom/(.Role: Requirement)/(.Form: Declaration)//` — HAS_ACTIVE_SUBJECT → `(Node, Node/**, .**)`; Host=undefined; Target=1
- `CA-R-2470@2`: unterminated logical group
- Unbound source evidence: `CA-R-2470@2`
  - Remaining Claim prose:
    For Node1/Node2, Node2's instances receive Node1's applicable:
    
    - Relation cardinalities.
    - Declared Properties.
    - Property Formats and value domains.
    - Direct-value and nested-Property cardinalities.
    
    Applicable local Node constraints also apply. Inheritance does not copy actual values or Relation facts. Reuse an inherited Property's Declaration; an inherited lookup creates no new Property or bearer.
    
    Each Node's effective Declaration resolves its complete Relation whitelist, including permissions, directions, endpoints and cardinalities. A Relation absent from that effective whitelist is forbidden. An unresolved whitelist does not grant permission.
- `CA-R-001@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-001@25`
  - Remaining Claim prose:
    the Project Scope Unit topology **must** distinguish Structural Level as nesting depth, Local Order as the order of ordered siblings under the same parent, **and** Navigational Order Number as presentation; dependency permission **must** follow its relation-family authority **and** **must not** be created by a filename number, nesting position, **or** the assumption that **every** Scope Unit is a Layer.
- `CA-R-004@35`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-004@35`
  - Remaining Claim prose:
    the CAPRMEDIO Framework Instance **must** keep **every** governed part of itself under the Operator's control **and** keep the Operator able **to** change the Project through that instance.
- `CA-R-007@31`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-007@31`
  - Remaining Claim prose:
    CAPRMEDIO **must** record **all** **and** **only** the direct typed relations necessary **to** trace **every** governed authority **to** its real Implementation **and** material dependents; inverse, transitive, **and** aggregate relations **must** be derived.
- `CA-R-028@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-028@25`
  - Remaining Claim prose:
    CAPRMEDIO **must** provide the Operator with capabilities for resolving conflicts between Atoms.
- `CA-R-029@34`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-029@34`
  - Remaining Claim prose:
    the caprmedio Project **must** use the effective Authority Mode for the Project **and** **every** configured Scope Unit under CA-R-1430:
    
    - Framework Instance Settings selects the Project mode **and** the default Scope Unit mode.
    - a Scope Unit's explicit override comes **only** from its authoritative Project Structure declaration; an omitted override uses the effective Framework Instance setting.
    
    mode selection **must not** weaken active-authority consistency.
- `CA-R-035@34`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-035@34`
  - Remaining Claim prose:
    an AI Agent's assessment of necessary Project information **must** use progressive context acquisition: read **every** active Project-owned Tier 0 Atom **before** using indexes, Relations, **and** Subjects **to** identify applicable Atoms; read **and** check the full Claims of those Atoms; expand inspection **when** dependencies, conflicts, missing evidence, **or** uncertainty require it. indexes, Relations, **and** Subjects support discovery **and** **must not** substitute for checking the applicable Claims. shared ancestry, descendancy, **or** structural scope alone **must not** require loading **every** Atom's full content.
    
    the information is necessary **when** its omission would leave the AI Agent below the effective Confidence Threshold resolved under CA-M-271. the confidence **and** threshold remain operational heuristics, **not** comparable probabilities across configurations.
- `CA-R-1056@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1056@28`
  - Remaining Claim prose:
    CAPRMEDIO **must** supply an LLM **only** the guidance necessary **to** meet the Operator-defined adequacy threshold under the currently observed model, host, task, **and** risk conditions.
- `CA-R-1057@32`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1057@32`
  - Remaining Claim prose:
    CAPRMEDIO **must** expose **to** the Operator **only** the distinctions necessary **to** understand **and** control the current task.
- `CA-R-1058@37`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1058@37`
  - Remaining Claim prose:
    CAPRMEDIO **must** establish **or** change governed Project meaning **only** through explicit per-action acceptance by the Operator **or** active authority explicitly delegated by the Operator **to** the identified AI Agent performing the change.
- `CA-R-1178@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1178@26`
  - Remaining Claim prose:
    FRAMEWORK_ENGINE **must** minimize token consumption, AI Agent mistakes, **and** irrelevant **or** stale context **when** applying the Applicable Methodology, while preserving required Project outcomes.
- `CA-R-1179@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1179@28`
  - Remaining Claim prose:
    OPERATOR_DOCUMENTATION **must** provide the Operator with sufficient, readable information **to** use a CAPRMEDIO Framework Instance efficiently **to** achieve their Project Goals.
- `CA-R-1180@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1180@26`
  - Remaining Claim prose:
    CORE_EXTENSIONS **must** provide CAPRMEDIO-maintained Extensions that add **or** specialize optional CAPRMEDIO capabilities **without** modifying canonical Core Meta-Model authority.
- `CA-R-1181@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1181@28`
  - Remaining Claim prose:
    RELEASES **must** provide the Operator with usable, evaluated versions of CAPRMEDIO **and** their release notes describing changes, compatibility, **and** known limitations.
- `CA-R-1407@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1407@26`
  - Remaining Claim prose:
    the CAPRMEDIO Framework Instance **and** the Implementation **must** form one connected Graph of Graphs.
- `CA-R-1420@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1420@25`
  - Remaining Claim prose:
    the CAPRMEDIO Framework Instance **and** AI Agents **must** keep communication with the Operator necessary **and** sufficient for the Operator **to** make informed decisions.
- `CA-R-1421@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1421@23`
  - Remaining Claim prose:
    the CAPRMEDIO Framework Instance **must** support Configuration of available capabilities **and** addition of new capabilities through Extensions.
- `CA-R-1423@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1423@25`
  - Remaining Claim prose:
    CAPRMEDIO **must** support the Operator **in** producing **and** evaluating an improvement proposal for **every** material observed Project outcome, with the proposal limited **to** the narrowest scope affected by that outcome **and** kept within the Operator's current authority.
- `CA-R-1424@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1424@26`
  - Remaining Claim prose:
    the CAPRMEDIO Framework Instance **must** provide Tools sufficient **to** evaluate, repair, **and** maintain instance alignment with the current Applicable Methodology from the Project's registered Framework Instance directory, including accurate reporting of orphan Atoms **and** other nonconformance; repair **must** remain under Operator control, **and** the Operator **may** leave findings unresolved **or** retain nonconforming Artifacts.
- `CA-R-1426@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1426@23`
  - Remaining Claim prose:
    FRAMEWORK_ENGINE **must** provide observability **and** transparency sufficient for the Operator **to** understand execution, inspect changes **and** evidence, recognize failures **and** limitations, **and** make informed decisions.
- `CA-R-1799@18`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1799@18`
  - Remaining Claim prose:
    the CAPRMEDIO Framework Instance **must** provide capabilities for the Operator **without** initiating **or** forcing their execution independently of Operator authorization.
- `CA-R-2157@10`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-2157@10`
  - Remaining Claim prose:
    the Operator holds original authority over the Project **and** its CAPRMEDIO Framework Instance **and** **may** perform **or** authorize governed actions within that authority.
- `CA-R-2158@10`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-2158@10`
  - Remaining Claim prose:
    an AI Agent has no original authority, **must not** create **or** expand its own authority, **and** **may** perform **or** authorize a governed action **only** **when** a current Operator-established AI Agent Delegation **or** authorization rule identifies that AI Agent **and** permits the complete action, its target, **and** its decision boundary.
- `CA-R-2445@3`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-2445@3`
  - Remaining Claim prose:
    COMMUNITY_EXTENSIONS **must** catalog externally maintained Extension packages **without** making those packages CAPRMEDIO-owned Scope Units.
- `CA-R-633@19`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-633@19`
  - Remaining Claim prose:
    a framework-improvement cycle **in** caprmedio **must** improve the capabilities, configuration, **or** operation of the CAPRMEDIO Framework Instance used within the Project.
- `CA-R-634@20`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-634@20`
  - Remaining Claim prose:
    a Project-improvement cycle **in** caprmedio **must** improve the CAPRMEDIO Framework being developed through changes **to** its PRMEDO authority, its Implementation, **or** their combination.
- `CA-R-637@13`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-637@13`
  - Remaining Claim prose:
    **when** a resolved failure class can materially recur, Evaluation **must** detect it at the earliest practical boundary.
- `CA-R-642@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-642@23`
  - Remaining Claim prose:
    **every** canonical decomposition **must** declare its bounded universe **and** one discriminating question per axis **and** assign **every** admissible member **to** **`=1`** value on **every** applicable axis.
- `CA-R-706@31`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-706@31`
  - Remaining Claim prose:
    the caprmedio Project **must** include FRAMEWORK_METHODOLOGY, METHODOLOGY_SOURCES, **and** its Methodology Source Scope Units **in** its Project Scope Unit tree under the authority of its active Project-owned Tier 0 Atoms.
- `CA-R-815@33`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-815@33`
  - Remaining Claim prose:
    the CAPRMEDIO Framework Instance **must** support implementing **every** admissible priority model established by the Operator for possible Project trade-offs.
- `CA-R-818@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-818@26`
  - Remaining Claim prose:
    CAPRMEDIO **must** help the Operator keep the active rule set necessary **and** sufficient for the current scope, stage, **and** priorities.
- `CA-R-826@19`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-826@19`
  - Remaining Claim prose:
    CAPRMEDIO's current native LLM-application support set **contains** Codex **and** no other application. Native support **means** that CAPRMEDIO owns **and** maintains the application adapter required **to** install **and** invoke framework interfaces **and** resolve host-session identity **without** an Extension **or** operator-provided compatibility layer. **every** other LLM application remains outside native support **until** an applicable active Boundary Requirement expands **or** replaces this Boundary.
- `CA-R-827@30`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-827@30`
  - Remaining Claim prose:
    CAPRMEDIO **must** keep **every** governed Project part outside the CAPRMEDIO Framework Instance under the Operator's control throughout Project evolution.
- `CA-R-831@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-831@26`
  - Remaining Claim prose:
    CAPRMEDIO **must** govern independently evolvable reusable capabilities as explicit Extensions whose extension points, authority boundaries, **and** compatibility conditions are declared.
- `CA-R-832@33`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-832@33`
  - Remaining Claim prose:
    the CAPRMEDIO Framework Instance **must** provide configuration capabilities **to** select, combine, parameterize, **or** disable available optional canonical **and** Extension capabilities **only** within declared configuration boundaries **and** **without** redefining governed meanings.
    
    current Extension activation **and** selected Extension revisions use their authoritative Framework Instance Settings under CA-R-1207; this capability does **not** make Project Configuration Atoms a second owner of those selections.
- `CA-R-846@29`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-846@29`
  - Remaining Claim prose:
    CAPRMEDIO **must** let the Operator create AI Agent Delegations **and** mandatory authorization rules for **every** identified AI Agent **and** inspect, limit, modify, suspend, **and** revoke **every** such delegation **or** rule.
- `CA-M-094@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-094@23`
  - Remaining Claim prose:
    choose among acceptable alternatives by optimizing the delivered result against its applicable Project-defined performance measures according **to** the current Operator-declared performance priority.
- `CA-M-095@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-095@24`
  - Remaining Claim prose:
    choose among acceptable alternatives by optimizing verified agreement with applicable acceptance criteria according **to** the current Operator-declared correctness priority.
- `CA-M-097@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-097@25`
  - Remaining Claim prose:
    apply **every** active rule group's current Operator-declared conformance priority **to** its verification **and** enforcement **without** weakening the applicability of the rule.
- `CA-M-098@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-098@24`
  - Remaining Claim prose:
    choose among acceptable alternatives by minimizing Operator **and** other human time **and** effort according **to** the current Operator-declared human-effort priority.
- `CA-M-099@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-099@24`
  - Remaining Claim prose:
    choose among acceptable alternatives by minimizing LLM, compute, service, **and** monetary expense according **to** the current Operator-declared external-expense priority.
- `CA-M-100@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-100@25`
  - Remaining Claim prose:
    choose among acceptable alternatives by minimizing the expected effort of later changes **to** direction, scope, assumptions, Methods, **or** Implementation according **to** the current Operator-declared flexibility priority.
- `CA-M-105@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-105@27`
  - Remaining Claim prose:
    **to** represent a kind of information **in** the Project, use **`=1`** canonical Entity, including a Property, for that kind **in** the same context:
    
    1. reuse its existing canonical definition instead of introducing another Entity **or** Property for the same information.
    2. treat mappings, explanations, **and** realizations as representations of that definition rather than additional canonical definitions.
    3. **if** choosing between competing canonical definitions requires an unresolved decision, **then** stop the affected mapping **or** adaptation **and** return the alternatives **and** their evidence **to** the Operator.
- `CA-M-138@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-138@27`
  - Remaining Claim prose:
    **to** author CAPRMEDIO-internal Artifacts, use the exact canonical CAPRMEDIO vocabulary, coherent Term meanings, **and** the strictest syntax needed **to** preserve the governed distinctions; treat FPF as a derivation source rather than external authority.
- `CA-M-139@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-139@26`
  - Remaining Claim prose:
    **to** address the Operator, use ordinary language by default; introduce **only** the canonical CAPRMEDIO Terms needed **when** ordinary language would make a material distinction ambiguous **or** incorrect, **and** explain **every** introduced Term **in** ordinary language.
- `CA-M-261@14`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-261@14`
  - Remaining Claim prose:
    **to** create **or** evolve the Implementation, keep it rebuildable from the current governing RMED **without** relying on the existing Implementation **or** first preparing missing authority.
- `CA-M-262@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-262@23`
  - Remaining Claim prose:
    **to** rebuild the Implementation, use the current RMED as sufficient authority for reproducing its required behavior **and** passing its applicable Evaluations **without** the previous Implementation **or** additional specification preparation; **if** the implementation language changes, **then** update the affected Method **and** Delivery authority **before** rebuilding against the resulting current RMED. a ready-made alternative Implementation is **not** required.
    
    under unchanged governing RMED, reconstruct runtime behavior that produces the same output for the same complete runtime input, including relevant starting state, configuration, time, randomness, **and** external-service responses. preserve the applicable Method **and** Delivery constraints; identical source code **or** identical source-file bytes are **not** required. judge fresh reconstruction **and** repeated implementation by this runtime equivalence, **not** by a requirement **to** leave already-conforming code untouched. an authorized RMED change establishes a new comparison baseline **and** **must not** be reported as reconstruction against unchanged RMED.
- `CA-M-263@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-263@21`
  - Remaining Claim prose:
    **to** expose governed information **to** the Operator, provide an initial **or** adapted representation that the Operator accepts as sufficient for the current governed use **or**, **when** applicable adaptation attempts are exhausted **or** declined, explicitly report the remaining comprehension gap; adapt the representation **without** changing the governed information.
- `CA-M-266@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-266@23`
  - Remaining Claim prose:
    **to** implement within a Task, follow the Operator-selected mode: evaluate **and** fix, full rebuild, refactoring, **or** another authorized approach. keep the selected mode within the Task permissions **and** governing RMED; permission for a full rebuild **must not** be inferred from an evaluation-and-fix request. the reconstruction equivalence governed by CA-M-262 applies regardless of mode **and** does **not** require identical code **or** a no-change rerun.
- `CA-M-270@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-270@27`
  - Remaining Claim prose:
    **to** refactor existing Implementation, prepare the applicable verification **before** changing the target Implementation:
    
    1. derive regression checks, end-to-end checks, acceptance gates, **and** canary criteria from the applicable Evaluations; select techniques by applicability rather than requiring **every** technique for **every** change. apply the governing Methods within Delivery boundaries while implementing these checks.
    2. evaluate the existing Implementation using controlled complete inputs **and** record its outputs **and** existing failures as baseline evidence. expected correctness remains governed by RMED; an existing defect **must not** become a Requirement merely because it appears **in** the baseline.
    3. evaluate the refactored candidate against current RMED **and** the recorded baseline under CA-M-262, using the implementation loop **and** retry policy. preserve the applicable checks across the comparison **unless** an authorized RMED change establishes a new baseline under CA-R-1559.
    4. apply the required release gates **before** full rollout. **when** canary testing applies, prepare its criteria **before** refactoring **and** execute it on the candidate **after** that Implementation exists during the authorized controlled rollout.
    
    this existing-Implementation baseline is comparison evidence, **not** missing specification recovered from old code, **and** is **not** a prerequisite for a fresh reconstruction with no existing Implementation.
- `CA-M-447@4`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-447@4`
  - Remaining Claim prose:
    **to** construct a canonical decomposition that claims **to** cover a declared universe at one abstraction level, use parts drawn **only** from that universe that together cover the full declared universe **and** have no overlap between **any** two distinct parts at that level.
- `CA-E-001@33`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-001@33`
  - Remaining Claim prose:
    governed commitments **and** results **must** be checkable **when** used **to** govern work **or** evaluate a result.
- `CA-E-206@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-206@24`
  - Remaining Claim prose:
    a governed conclusion **may** be treated as reliable for an affected use **only** **when** **every** required input is present, known, consistent, **and** valid.
- `CA-E-209@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-209@25`
  - Remaining Claim prose:
    the intended Operator can identify the represented meaning, available controls, **and** material consequences.
- `CA-E-228@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-228@26`
  - Remaining Claim prose:
    the declared Operators collectively retain control over **every** governed part of the CAPRMEDIO instance **and** can use the instance **to** change the Project within their current authority.
- `CA-E-230@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-230@25`
  - Remaining Claim prose:
    the Operator can create, inspect, limit, modify, suspend, **and** revoke AI Agent Delegations **and** mandatory authorization rules for identified AI Agents.
- `CA-E-435@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-435@24`
  - Remaining Claim prose:
    the reconstruction readiness Evaluation **must** return `fail` **if** rebuilding required behavior **or** evaluating the rebuilt result needs authority recovered from the previous Implementation **or** specification work **before** reconstruction; **if** a language change is selected, **then** evaluate readiness against the current RMED **after** its affected Method **and** Delivery updates. absence of a prebuilt alternative **must not** by itself cause failure.
    
    the Evaluation **must not** report runtime equivalence **if** equal complete runtime inputs under unchanged RMED produce different outputs, relevant starting state **or** configuration **or** time **or** randomness **or** external-service responses are omitted from the comparison, applicable Method **or** Delivery constraints are violated, **or** an authorized RMED change is hidden inside the unchanged baseline. source-code differences alone **must not** cause failure. a fixed task order **or** readiness review **without** runtime evidence **must not** be reported as proof of equivalent reconstruction.
- `CA-E-437@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-437@25`
  - Remaining Claim prose:
    the methodology alignment support Evaluation **must** return `fail` **if** the available Tools cannot assess the governed instance against the current Applicable Methodology, omit known nonconformance, cannot support an authorized repair, **or** mutate authority **without** Operator permission; a targeted check **may** use a bounded affected Scope **and** its dependencies. an unresolved finding **or** Operator-created orphan **must not** by itself establish failure of the required support capability **or** be reported as conformance.
- `CA-E-438@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-438@25`
  - Remaining Claim prose:
    the implementation mode Evaluation **must** return `fail` **if**
    
    - execution replaces the Operator-selected mode **without** authorization,
    - treats an evaluation-and-fix request as permission for a full rebuild,
    - exceeds Task permissions,
    - **or** exempts the selected mode from the governing RMED.
    
    authorized rewriting **or** different source-code bytes **must not** by themselves cause failure **when** reconstruction equivalence under CA-M-262 is preserved.
- `CA-E-442@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-442@24`
  - Remaining Claim prose:
    the refactoring-verification Evaluation **must** return `fail` **if**
    
    - the target Implementation changes **before** applicable verification is prepared **and** the existing Implementation baseline is recorded,
    - baseline inputs are incomplete **or** uncontrolled,
    - an existing defect becomes expected correctness **without** governing authority,
    - the candidate is **not** checked against the governing RMED **and** baseline,
    - **or** required release gates are bypassed.
    
    **when** canary testing applies, it **must** return `fail` **if**
    
    - criteria were **not** prepared **before** refactoring
    - **or** the canary is reported as executed **without** running the candidate during an authorized controlled rollout.
    
    absence of an inapplicable testing technique **or** of an old-Implementation baseline for a fresh reconstruction **must not** by itself cause failure. baseline observations **must not** replace RMED as authority.
- `CA-E-656@20`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-656@20`
  - Remaining Claim prose:
    **every** canonical decomposition satisfies CA-M-447 **and** CA-R-642.
- `CA-R-1014@40`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1014@40`
  - Remaining Claim prose:
    an Atom Scope **must** include its current Scope Unit Scope **or** its Author's registered Operator fallback under CA-D-657-CORE_META_MODEL-DELIVERY--use-economical-yaml-frontmatter, its **`=1`** Atom Governed Subject, **and** **any** explicit Scope constraints **in** its Claim.
- `CA-R-1044@31`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1044@31`
  - Remaining Claim prose:
    An AI Agent may continue Plan work autonomously only when the applicable Decision Confidence reaches the Autonomous Confidence Threshold.
- `CA-R-1045@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1045@24`
  - Remaining Claim prose:
    **every** Autonomous Confidence Threshold **must** be an integer percentage **`>=0`** **and** **`<=100`**. resolve its effective value from the applicable source under CA-M-271; the methodology **must not** restrict that value **to** a closed list of preferred percentages.
- `CA-R-1051@34`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1051@34`
  - Remaining Claim prose:
    the active RMED authority graph represents **only** current governed state. historical states **and** transitions are excluded from that graph **and** preserved through canonical lifecycle placement **and** append-only Journals; generated Projections **may** render history **without** making it active RMED authority.
- `CA-R-1206@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1206@26`
  - Remaining Claim prose:
    installing an Extension **must** make its immutable authority available **to** Project Configuration **without** making the Extension authority applicable **to** the current Project.
- `CA-R-1207@31`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1207@31`
  - Remaining Claim prose:
    the Project Configuration **must** own Project-specific expansion rules, constraints, **and** defaults **only** **where** the Core Meta-Model permits expansion; current Extension activation **and** selected Extension revisions **must** remain owned by the Framework Instance Settings Artifact, **not** duplicated **in** Project Configuration Atoms.
- `CA-R-1245@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1245@26`
  - Remaining Claim prose:
    **in** a Subject Expression, `X:Y` **must** express only one IS_ALLOWED_VALUE_OF relation from value Y to target Entity X, irrespective of X's kind or path. This relation admits Y as a possible value in X's qualified context; it does not assign Y to an occurrence or determine direct-value cardinality.
- `CA-R-1247@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1247@24`
  - Remaining Claim prose:
    **every** `Entity/Property` occurrence **must** derive its
    source-admitted bearer-qualified identity from its complete Subject Path
    **without** imposing one global ordinal position on a reusable Term. Its
    outgoing direct IS_PROPERTY_OF Relation identifies its immediate bearer. Distinct
    modeled entities **must** use distinct complete canonical names, while repeated
    references **to** the same entity **must** retain its same complete canonical
    name.
- `CA-R-1251@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1251@24`
  - Remaining Claim prose:
    the Term Property **must** be NARROWER_THAN Dependent Entity.
- `CA-R-1259@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1259@24`
  - Remaining Claim prose:
    **every** Entity **may** bear **`>=0`** Property occurrences.
    
    ### Formal claim
  - Fenced Claim block:
```text
Entity {0+}((HAS_PROPERTY)){1} Property
```
- `CA-R-1261@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1261@24`
  - Remaining Claim prose:
    the Core Meta-Model **must not** declare its Entity subkind registry exhaustive **or** prevent compatible Extension **and** Project Configuration subkinds.
- `CA-R-1262@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1262@24`
  - Remaining Claim prose:
    Artifact **must not** be equivalent **to** Entity.
- `CA-R-1267@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1267@24`
  - Remaining Claim prose:
    the Term Dependent Entity **must** be NARROWER_THAN Entity.
- `CA-R-1279@32`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1279@32`
  - Remaining Claim prose:
    when an Atom's Claim explicitly defines a Term, it **must** use its **`=1`** direct GOVERNS Subject Relation **to** identify the canonical target defined by that Claim, with the defined Term as the terminal name **in** that target's Subject Path. the defining Claim, source use, **and** applicable Atom.Semantics establish that Term's meaning; the other Term components **in** the path are references **to** their own meanings, **not** additional meanings supplied by this Atom.
- `CA-R-1283@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1283@28`
  - Remaining Claim prose:
    the allowed Content Role values **must** be exactly (Concern, Analysis, Plan, Requirement, Method, Evaluation, Delivery, Operations).
- `CA-R-1284@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1284@26`
  - Semantics:
    `X.Y` addresses Property Y. `X.Y: Z` expresses that Z is an allowed value of
    that Property. `X/(.Y: Z)` qualifies a narrower kind of X by its own Property Y
    and admitted value Z. The leading dot addresses X.Y relative to X; the
    qualified X inherits X's applicable features and constraints. Y does not
    become a narrower kind of X, and no intermediate X/Y kind is declared. Neither form assigns a
    value to an existing instance merely by appearing in an expression.
    
    Atom Form is represented by the YAML `form` key; Atom Role is represented by `role`. Legacy `type` and `content_role` are readable only under the transition rules in CA-D-657. These encodings do not create separate Property kinds.
    For example, `Atom/(.Content Role: Method)` concerns Atoms classified by Content
    Role Method; Method is not used as a Type value in this example.
  - Remaining Claim prose:
    Type is a single-valued Property when an Entity admits that Property. It can
    be used for classification: `X/(.Type: Z)` identifies a kind narrower than X,
    qualified by the Type Property and its admitted value Z. The Type Property
    and a Property addressed directly by `X.Y` share the same Property meaning;
    classification use does not introduce another Property category.
    
    The applicable allowed-value set is finite at an Applicable Methodology
    Revision and expandable through governed Methodology Sources. Admission and
    requiredness remain scoped to the qualified Property context.
- `CA-R-1285@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1285@25`
  - Remaining Claim prose:
    an Entity occurrence that bears Type **must** have **`=1`** direct Type value.
- `CA-R-1286@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1286@25`
  - Remaining Claim prose:
    an Extension **or** Project Configuration **may** add Type values under **`=1`** exact qualified Type Subject **without** creating another Type Property.
- `CA-R-1293@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1293@28`
  - Remaining Claim prose:
    a Demand Atom owned by an Ordered Scope Unit **must not** target a later Ordered sibling under the same direct parent.
- `CA-R-1294@33`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1294@33`
  - Remaining Claim prose:
    a Demand Atom **must not** introduce a graph Relation Kind for its direction because its Consumer Atom Scope Unit **and** Producer Claim Target Scope Unit references determine that direction.
- `CA-R-1309@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1309@28`
  - Remaining Claim prose:
    the Core allowed values of Requirement Status **must** be exactly (Draft, Active, Archived).
- `CA-R-1325@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1325@24`
  - Remaining Claim prose:
    a Catalog used as a terminology list **or** vocabulary diagnostic index **must not** classify one complete composite Subject Expression as one Term.
- `CA-R-1348@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1348@25`
  - Remaining Claim prose:
    a qualified Type Subject **must** reuse the Term Type **and** **must not** create a role-specific Type Term.
- `CA-R-1349@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1349@21`
  - Remaining Claim prose:
    **all** qualified Type Subjects of **`=1`** Entity occurrence **must** identify the same Type Property.
- `CA-R-1350@20`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1350@20`
  - Remaining Claim prose:
    the most-specific applicable qualified Type Subject **must** determine the allowed-value set of the Entity occurrence's Type Property.
- `CA-R-1360@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1360@26`
  - Remaining Claim prose:
    Where a Canonical Signature is interpreted for a parenthesized restricted Boolean expression occurrence in one Atom Claim, the interpretation **must** produce **`=1`** derived non-authoritative comparison value, subject to the following constraints:
    
    - the grammar is:
      - `group ::= (operand **and** operand [**and** operand ...]) | (operand **or** operand [**or** operand ...])`;
      - `operand ::= atomic predicate | nested group with the same Boolean Operator`;
      - `atomic predicate ::= subject path: value`.
    - canonicalization:
      - flattens nested same-operator groups;
      - removes duplicate atomic predicates;
      - sorts the remaining atomic predicates;
      - preserves the root Boolean Operator.
    - canonicalization excludes:
      - mixed Boolean Operators;
      - **every** other CCE Operator;
      - unrecognized bold token;
      - unbalanced parentheses;
      - unparseable prose.
- `CA-R-1397@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1397@24`
  - Remaining Claim prose:
    the Core allowed values of Method Status **must** be exactly (Draft, Active, Archived).
- `CA-R-1398@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1398@24`
  - Remaining Claim prose:
    the Core allowed values of Evaluation Status **must** be exactly (Draft, Active, Archived).
- `CA-R-1399@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1399@24`
  - Remaining Claim prose:
    the Core allowed values of Delivery Status **must** be exactly (Draft, Active, Archived).
- `CA-R-1404@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1404@26`
  - Remaining Claim prose:
    the Framework Instance Settings Artifact **must not** be an Atom.
- `CA-R-1405@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1405@27`
  - Remaining Claim prose:
    the Core allowed values of Artifact Type **must** be (Atom, Journal, Projection, Project Settings, Framework Instance Settings, Default Settings).
- `CA-R-1410@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1410@22`
  - Remaining Claim prose:
    **every** CAPRMEDIO Graph **must** connect **to** the General Artifact Graph through **`>=1`** shared **or** referenced source Artifact **or** Structural Entity. the connection preserves the existing source identity **without** creating a duplicate source **or** requiring an artificial Artifact for a structural-only source.
- `CA-R-1415@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1415@26`
  - Remaining Claim prose:
    **every** Atom **must** have **`=1`** positive integer Version that increases monotonically across successive versions of the same Atom.
- `CA-R-1419@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1419@21`
  - Remaining Claim prose:
    an Atom version **may** have Status Archived **only** **if** it is a prior version **or** the final version of a replaced, absorbed, **or** retired Atom.
- `CA-R-1428@30`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1428@30`
  - Remaining Claim prose:
    a Confidence Threshold **must** take its value from applicable direct Operator input, an explicit Property on the current Plan, the nearest enclosing Hub Plan with an explicit Property, **or** the Framework Instance Settings default; the Plan-containment chain follows `IS_CONTAINED_BY` toward the nearest enclosing Plan, **not** Label spelling.
- `CA-R-1429@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1429@28`
  - Remaining Claim prose:
    - the settings foundations for Project Settings, Framework Instance Settings, **and** Default Settings **must** define their purpose, content, **and** authority boundaries;
    - an independently governable shared settings specification **must** preserve those foundations **without** selecting a concrete representation;
    - **every** concrete section, field, **or** Carrier syntax specification **must** be specified explicitly.
    
    a setting **must not** require a shared settings specification **unless** a distinct shared specification requires independent authority.
- `CA-R-1430@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1430@25`
  - Remaining Claim prose:
    Framework Instance Settings **must** select the Project Authority Mode **and** default Scope Unit Authority Mode. a Scope Unit's explicit Authority Mode override **must** be owned **only** by its Project Structure declaration; an omitted override uses the effective Framework Instance setting **without** becoming an authored per-unit value. permitted values are `strict` **and** `casual`; neither changes the authority of active Atoms.
- `CA-R-1441@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1441@26`
  - Remaining Claim prose:
    Default Settings **means** the authoritative Artifact containing reusable baseline values for registered CAPRMEDIO Framework Instance Settings parameters, **not** Project initialization inputs **or** a Project's explicit Operator selections.
- `CA-R-1447@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1447@25`
  - Remaining Claim prose:
    Owned Atoms **means** the set of **all** Atoms whose internally carried current Scope Unit **`=`** the selected Scope Unit.
    
    - a grouping Carrier, Plan decomposition, **or** physical placement does **not** replace that ownership value.
    - a missing, invalid, **or** ambiguous ownership value leaves membership unresolved; do **not** derive it from the filename **or** containing folders.
    - evaluate placement consistency separately **without** changing the selected Atom's declared ownership.
- `CA-R-1454@32`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1454@32`
  - Remaining Claim prose:
    for a requested source selection, a governed-only view of the Terms Graph **must** include **only** the Governed Terms admitted under CA-R-1319-CORE_META_MODEL--define-governed-term **and** CA-M-114-CORE_META_MODEL-IMPLEMENTATION_METHOD--derive-terminology-projection-from-definition-atoms from Term Definition Atoms **in** that selection **and** the Relations explicitly declared by source Atoms **in** that selection whose endpoints are included **and** whose Relation Type is identified by its defining source Claim **and** that, where applicable, conforms to the governing Entity Definition constraints; it **must** include **every** such Term **and** Relation. **every** displayed node **and** edge **must** retain traceability **to** its exact source Claim **and** Artifact Revision. this selection reuses the Terms Graph under CA-R-1335@31-CORE_META_MODEL-DEFINITION--define-terms-graph **and** the source Relation authority under CA-R-1437-CORE_META_MODEL--keep-one-source-for-each-relation-fact **without** introducing another graph kind **or** independent vocabulary authority.
    
    the view **may** be derived from an upstream Terms Graph Projection **when** the upstream selection **and** source evidence support the requested view. its upstream Projection identity **and** Revision **must** remain traceable **to** the exact Term Definition Atoms **and** source Relation declarations required by this Claim. the upstream Projection **must not** acquire defining authority **or** establish complete source coverage from an incomplete selection. distinct graph **and** separately identified filtered-view Projection instances retain their own identities while reusing the Terms Graph Type **and** the shared Relation Type definitions; a governed-only filter alone does **not** create another Type or alter its identity.
    
    these node **and** internal-Relation selection rules do **not** require importing the endpoints of separately admitted external references as native graph members. **if** the view includes cross-graph **or** source references under CA-R-1472-CORE_META_MODEL--admit-typed-secondary-graph-connections, it **must** keep them distinguishable from its native node **and** internal-Relation selection **and** preserve their endpoint identity and classes, shared Relation Type identity, any graph-qualified reference **or** context, **and** source traceability. such references **must not** silently enlarge the selected native graph **or** bypass an explicit source-declaration requirement for its internal Relations.
- `CA-R-1455@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1455@27`
  - Remaining Claim prose:
    a Catalog used as a vocabulary diagnostic index **must** distinguish ordinary English use under CA-R-1320 from evidence of unresolved Project-specific use, with **every** entry bound **to** its exact source occurrence, surrounding Claim **or** reference context, **and** Artifact Revision. the index **must** declare the source selection **and** checked definition coverage that bound its judgments. capitalization, consistent use, occurrence **in** GOVERNS **or** DEPENDS_ON, **or** the appearance of a Scope Unit name, Actor name, identifier, path, **or** syntax token alone **must not** establish Project-specific Term status **or** a missing definition.
    
    an unresolved Project-specific candidate **must** retain the source evidence that indicates Project-specific use **without** treating a suspected meaning as established authority. missing defining authority **must** be distinguished from conflicting defining authority **or** conflicting Project-specific uses. a missing-authority judgment requires complete checked definition coverage for its declared applicable source authority boundary; absence from an incomplete **or** filtered selection alone **must not** establish that judgment. **if** the evidence cannot settle ordinary versus Project-specific use, defining authority, **or** definition coverage, the affected case **must** remain explicitly uncertain with its source occurrence **and** the reason for uncertainty available for review. spelling alone **must not** transfer one occurrence's classification **to** another.
    
    these indexes **must** remain non-authoritative Projections of the cited source evidence; they **must not** supply missing definitions, require **every** word **to** acquire a Project-specific definition, promise mechanical certainty about meaning, **or** introduce another Terms Graph **or** invented Relation edges. **any** graph representation additionally requires independently admitted Relation Kind **and** source Relation authority; index membership alone establishes neither.
- `CA-R-1456@37`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1456@37`
  - Remaining Claim prose:
    a derived Entities Graph view **must** declare its requested source selection **and** **any** narrower display selection, including a hierarchy view. it **must** include **all** **and** **only** Entity identities admitted under CA-R-2462-CORE_META_MODEL-DEFINITION--define-entity by the selected source Claims that satisfy the declared display selection, **and** Relations explicitly declared by selected source Atoms whose endpoints are included, whose Relation Type has a defining source Claim, with any applicable Entity Definition constraints preserved, **and** that satisfy the declared display selection. a narrower view **must not** silently enlarge the source selection **or** be represented as the full combined graph. A declaration-only display selection excludes link instances. The presence of endpoints does not override that filter or require importing actual Relation tuples into the declaration view.
    
    **every** displayed node **and** edge **must** retain its existing canonical identity **and** traceability **to** its exact governing source Claim **and** Artifact Revision for Entity **or** Relation admission; **any** represented observed structural **or** recorded historical facts additionally retain their appropriate Scope Unit **or** Journal sources under CA-R-2535-CORE_META_MODEL-CORE-REQUIREMENT--define-projection-artifact-form. Property occurrences retain their complete bearer-qualified Subject Paths under CA-R-1247-CORE_META_MODEL-CORE-REQUIREMENT--identify-dependent-entity-occurrences-by-complete-subject-path; reuse of a Term, appearance **in** multiple views, **or** multiple governing Atoms for one Entity **must not** duplicate **or** merge source identities. source Relation facts retain their Type identity, direction, qualified endpoints, **and** source declaration; derived HAS_PROPERTY navigation retains traceability **to** its original IS_PROPERTY_OF fact under the pending [HAS_PROPERTY Relation Definition](CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-has-property.md) **without** becoming another primitive Relation fact.
    
    this selection reuses the Entities Graph under CA-R-1438@25-CORE_META_MODEL--define-entities-graph **without** another graph kind **or** independent model authority. a hierarchy display **must not** impose a tree constraint on the full graph, discard legitimate sharing, **or** introduce a global ordinal-position rule. display filtering **must not** change source bearer cardinalities, qualified identities, **or** allowed-value admission; IS_PROPERTY_OF **and** IS_ALLOWED_VALUE_OF retain their distinct governing authority.
    
    the view **may** be derived from an upstream Entities Graph Projection **when** the upstream selection **and** source evidence support the requested view. the view **must** retain the upstream Projection identity **and** Revision together with traceability **to** the ultimate authoritative sources; the upstream Projection **must not** replace source authority **or** establish source completeness beyond its evidenced coverage. an observed Carrier **or** Journal occurrence alone **must not** admit an Entity identity, define a Term, **or** admit a Relation Type **without** the required governing source Claims. distinct graph **and** separately identified filtered-view Projection instances retain their own identities while reusing the Entities Graph Type and project-shared Relation Type definitions; any graph-specific admission or constraints remain governed by selected Entity Definition constraints where present; a display filter alone does **not** admit another Type or create a graph-specific Type copy.
    
    these node **and** internal-Relation selection rules do **not** require importing the endpoints of separately admitted external references as native graph members. **if** the view includes cross-graph **or** source references under CA-R-1472-CORE_META_MODEL--admit-typed-secondary-graph-connections, it **must** keep them distinguishable from its native node **and** internal-Relation selection **and** preserve their endpoint identity, Relation Type identity, any applicable governing constraint context and its established endpoint classes, **and** source traceability. such references **must not** silently enlarge the selected native graph **or** bypass an explicit source-declaration requirement for its internal Relations.
- `CA-R-1466@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1466@21`
  - Remaining Claim prose:
    Git integration **must** be optional Extension authority, **not** a prerequisite of the Core Meta-Model. Git commit policies, commit-message encodings, hooks, **and** event-to-commit references belong **to** that Extension; selecting it **must not** replace the authoritative Journal **or** make Git history an independent source for the same recorded facts. the Core Meta-Model **must** remain applicable **without** Git integration.
- `CA-R-1470@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1470@26`
  - Remaining Claim prose:
    Single Source of Truth **means** **`=1`** canonical authoritative source for **every** independently maintained fact **in** the same applicable context. another representation of that fact references **or** derives from its source **without** becoming an independently maintained authority.
    
    source authority is assigned per fact under the governing model: Atoms carry governing Claims **and** their declared source Relations; Project Structure owns declared Scope Unit facts; Structural Entity Carriers supply materialization observations; Journals preserve recorded historical facts. native Implementation Carriers **may** be authoritative for their actual realized content, structure, dependencies, **and** behavior. other admitted sources retain their declared authority. this does **not** require **all** facts **to** reside **in** **`=1`** Atom, file, **or** Artifact. a derived result **may** use multiple authoritative input facts **without** creating another authoritative source for those input facts.
- `CA-R-1471@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1471@27`
  - Remaining Claim prose:
    secondary CAPRMEDIO Graphs **must** be Projections derived from their selected authoritative sources **or** source-traceable upstream Projections. their nodes **and** Relations **must** preserve source identities **and** traceability **to** the governing derivation authority **and** source facts.
    
    storing, composing, filtering, **or** rebuilding a secondary graph **must not** make its contents another source of authority. a represented source fact is corrected **at** its authoritative source; an incorrect derivation is corrected under its governing methodology. neither case is resolved by independently editing the projected fact **or** fabricating source history.
- `CA-R-1485@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1485@22`
  - Remaining Claim prose:
    Project Structure **may** retain derived ancestry/path representations for readability **only** **when** their authoritative parent declarations **and** consistency constraints are explicit. a retained authority path **must** satisfy applicable Carrier naming **and** placement rules, including admitted exceptions; no retained Structural Level or other depth field is an authored Project Structure property. inconsistent representations **must** produce a reported conflict **without** an automatic choice of a new Name, parent, order, **or** binding. readability does **not** establish another source of authority.
- `CA-R-1487@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1487@21`
  - Remaining Claim prose:
    the CAPRMEDIO Framework Instance **must** support the admissible priority model established by the Operator for the affected Scope **and** Project stage. **every** resulting alternative selection **must** satisfy **all** of the following:
    
    - respect applicable authority **and** non-negotiable constraints.
    - conform **to** that model, its effective parameters, **and** its active criteria **without** substituting another comparison algorithm.
    - remain unresolved **if** the selected model **or** its application does **not** justify a selection.
- `CA-R-1489@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1489@25`
  - Remaining Claim prose:
    an Implementation Retry Limit **must** take its effective value from applicable direct Operator input, an explicit Property on the current Plan, the nearest enclosing Hub Plan with an explicit Property, **or** Framework Instance Settings.
    
    - a Plan **may** have **<=1** explicit Implementation Retry Limit override, regardless of Label.
    - an omitted override **must** preserve inheritance **without** copying the inherited value into that Plan.
    - a retry decision **must** have **=1** valid effective limit; missing **or** ambiguous authority requires Operator disposition **before** another retry.
- `CA-R-1498@17`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1498@17`
  - Remaining Claim prose:
    recursive Structural Entity containment **must** **`=`** the transitive closure of direct Structural Entity containment.
- `CA-R-1504@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1504@23`
  - Remaining Claim prose:
    coverage between Evaluation Atoms **and** their realizations **may** be many-to-many **only** with explicit attribution:
    
    - **`=1`** Evaluation Atom **may** be realized by multiple distinct implementations.
    - **`=1`** implementation **may** realize multiple Evaluation Atoms **only** **when** its result remains attributable **to** **every** covered Claim.
- `CA-R-1506@19`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1506@19`
  - Remaining Claim prose:
    the mechanism labels `Test` **and** `Evaluation` **must** describe implementation mechanisms, **not** Type values under `Atom/Content Role: Evaluation/Type`. the governing Evaluation Atom **and** its realization **must not** acquire the same classification merely because their names overlap.
- `CA-R-151@32`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-151@32`
  - Remaining Claim prose:
    the CAPRMEDIO Metamodel **must** admit a durable construct **only** **when** the existing Metamodel cannot preserve the required operational distinction.
- `CA-R-1519@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1519@23`
  - Remaining Claim prose:
    an executor of a Workflow **must** conform **to** the applicable methodology execution rules rather than inventing behavior that is absent from its governing definitions.
- `CA-R-1520@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1520@22`
  - Remaining Claim prose:
    **when** a Workflow declares a handoff **to** another Workflow, its Run **must** end with a terminal result sufficient for the executor **to** evaluate **and** start the continuation separately.
- `CA-R-1521@29`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1521@29`
  - Remaining Claim prose:
    a Workflow for changing an Entity's Status **must** admit **any** requested Status allowed by that Entity's applicable status model, rather than a fixed list built into the Workflow. For Atom creation **and** explicit Atom Status updates, **any** value admitted by the qualified Content Role/Type model is selectable **without** a required intermediate Status **or** transition matrix.
- `CA-R-1525@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1525@24`
  - Remaining Claim prose:
    **every** Workflow Run **must** retain the exact Workflow graph Revision, referenced Step Atom Revisions, **and** referenced Action definition Revisions admitted for its execution.
- `CA-R-1528@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1528@22`
  - Remaining Claim prose:
    a Tool Call **means** an invocation of a Tool during execution; **when** it occurs within a Step Run, its execution evidence **must** remain associated with that parent Step Run **in** the canonical Project Journal.
- `CA-R-1539@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1539@22`
  - Remaining Claim prose:
    the Core Plan Status model **must** inherit the allowed values of Atom.Status and add (Backlog, Done, Canceled). Planned **must not** be a distinct Plan Status.
- `CA-R-1548@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1548@24`
  - Remaining Claim prose:
    Specification Content Roles (Spec, RMED) **means** the set (Requirement, Method, Evaluation, Delivery) that specifies governed content **and** Entities, including CAPO **and** I.
- `CA-R-1550@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1550@26`
  - Remaining Claim prose:
    a specification Claim about Change **or** Implementation content **must** remain **in** Spec Content Roles according **to** its own contribution rather than inherit the Content Role of the content it specifies.
- `CA-R-1552@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1552@22`
  - Remaining Claim prose:
    an AI Agent **may** perform **or** authorize a governed action **without** per-action Operator approval **only** **when** an active Operator-issued delegation authorizes that identified Agent, action, target scope, **and** applicable constraints.
- `CA-R-1554@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1554@21`
  - Remaining Claim prose:
    an AI Agent that performs a Scripted Migration **must** satisfy **all** of these participation conditions:
    
    - bind the migration **to** an exact governed Target Set;
    - fail **when** an expected target is absent;
    - produce a reviewable change set.
    
    these conditions constrain the AI Agent's participation; they do **not** define the migration's Steps **or** Workflow control flow **or** grant additional mutation authority.
- `CA-R-1555@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1555@21`
  - Remaining Claim prose:
    an identified AI Agent **may** omit clarification **only** **when** confidence **in** **every** following item meets its applicable configured requirement:
    
    - intent;
    - scope;
    - route;
    - entry criteria.
    
    confidence **must not** create delegated authority **or** bypass per-action Operator approval **when** active authority requires it.
- `CA-R-1556@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1556@23`
  - Remaining Claim prose:
    an identified AI Agent **may** create Spec Atoms directly from sufficiently clear Operator input **when** active Operator authority permits the required actions.
    
    an Analysis Report **may** precede **and** inform Spec **when** investigation **or** synthesis is useful. it is **not** a mandatory Carrier **or** gate for **every** Spec Claim.
- `CA-R-1557@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1557@21`
  - Remaining Claim prose:
    an AI Agent **must** keep a discovered conflict **in** Exploration Mode; it **may** create a Concern for that conflict **only** **when** the Operator requests persistence **or** defers its resolution.
- `CA-R-1558@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1558@23`
  - Remaining Claim prose:
    an AI Agent **must** handle exploratory Operator input **in** Exploration Mode under the following participation policy:
    
    - Exploration Mode permits brainstorming, discussion, research, analysis, comparison, terminology work, **and** structural modeling **without** creating **or** changing governed Artifacts.
    - input is exploratory **when** it primarily asks for information, explanation, comparison, critique, alternatives, **or** a recommendation, **or** introduces an idea, explores it, **or** asks for feedback on it.
    - an explicit Operator request **to** create **or** change governed state takes precedence over question-shaped wording.
    - **otherwise**, Exploration Mode ends **only** **when** the Operator explicitly accepts a conclusion **or** requests its promotion. the AI Agent **must** **then** create **only** the minimum Artifacts required **to** preserve the accepted meaning within the authorized change.
    - whether a mode transition is announced is an interaction-reporting choice; it does **not** change this participation policy.
- `CA-R-1559@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1559@24`
  - Remaining Claim prose:
    authorization **to** change a governing RMED Atom during implementation **must** satisfy the following Actor policy:
    
    - resolve the Atom's effective Author **before** the proposed change, its governing permissions, the effective Plan Autonomous Confidence Threshold under CA-R-1591, **and** **all** additional Operator rules.
    - obtain Operator approval **before** changing an Operator-authored Atom.
    - request Operator disposition **before** changing an AI-authored Atom **when** confidence is below the threshold **or** an additional rule requires approval.
    - an AI-authored Atom **may** change autonomously **only** **when** confidence is at **or** above the threshold **and** **all** applicable permissions **and** Operator rules allow it.
    - a prohibition remains a prohibition; authorship **or** confidence **must not** create permission.
    - a missing **or** unresolved Author **must not** be treated as proof of AI authorship; apply the Author default under CA-R-1080@29.
    - an authorized RMED change establishes a new baseline under CA-M-262, **and** the applicable work **and** Evaluations **must** be resolved again against it.
- `CA-R-1561@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1561@26`
  - Remaining Claim prose:
    an identified AI Agent **may** resolve a Concern from active Atoms **when** its active Operator delegation permits **every** required action **and** resolution confidence meets the configured semantic-resolution threshold; the resolution **may** create **or** change Atoms **in** other Content Roles **only** within that same delegated authority.
- `CA-R-1562@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1562@25`
  - Remaining Claim prose:
    the Operations Atom Type Action **means** the Type of an Operations Atom whose Claim specifies that same Atom's reusable Action behavior. the Action may be referenced by multiple Step Atoms in multiple Workflows without copying or redefining that behavior.
- `CA-R-1563@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1563@25`
  - Remaining Claim prose:
    the Operations Atom Type Workflow **means** the Type of an Operations Atom whose Claim specifies **`=1`** Workflow graph scheme for that same Atom using references **to** Step Atoms and the Workflow's declared Step structure.
- `CA-R-1565@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1565@21`
  - Remaining Claim prose:
    the admitted internal values of `Atom/Content Role: Operations/Type` **must** include (Action, Workflow, Step).
- `CA-R-1570@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1570@22`
  - Remaining Claim prose:
    a Workflow Atom **must** own **only** its graph scheme: Step references, declared order and structural Relations, entry points, **and** terminal outcomes. a Conditional Step definition owns its result-based routing; the Workflow graph does not use a separate result-transition Relation.
    
    - the referenced Step Atoms own Action references, parameters, **and** input bindings.
    - reusable Action Atoms own Action behavior.
    - the graph **must not** independently repeat those Step bindings **or** Action definitions; folder nesting **and** file order **must not** replace its declared control flow.
- `CA-R-1577@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1577@23`
  - Remaining Claim prose:
    a Plan Subtype **means** an explicitly governed specialization of Plan authoring rules; a Label **must not** imply that specialization **without** its own applicable authority.
- `CA-R-1584@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1584@23`
  - Remaining Claim prose:
    **every** Plan Atom with its own work content **must** have **`=1`** effective Assignee; a pure Hub **without** its own work does **not** require an additional Assignee merely because it organizes other Plans.
- `CA-R-1585@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1585@23`
  - Remaining Claim prose:
    **if** a Plan Atom has its own work **and** no explicit Assignee, **then** its effective Assignee **must** be **=1** AI Agent selected **to** execute that work.
- `CA-R-1587@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1587@22`
  - Remaining Claim prose:
    **every** autonomous Plan execution decision **must** resolve **=1** effective Autonomous Confidence Threshold from its applicable explicit **or** inherited source under CA-M-271.
- `CA-R-1588@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1588@26`
  - Remaining Claim prose:
    during authoring, a Plan with no separately selected Claim Target Scope Unit **must** select its owning Scope Unit as the target, independently of Plan containment **or** Label; a Hub does **not** become that default target. carry the resolved target under CA-D-482.
- `CA-R-1591@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1591@24`
  - Remaining Claim prose:
    autonomous continuation of Plan work **must** satisfy its effective Autonomous Confidence Threshold:
    
    - resolve the value under CA-M-271-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-confidence-thresholds-by-source-precedence.
    - **if** confidence **in** correct execution is below it, request Operator disposition **before** continuing.
    - **otherwise**, continue **only** within existing authority; meeting the threshold does **not** grant additional authority.
- `CA-R-1596@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1596@22`
  - Remaining Claim prose:
    **every** Atom Claim **must** resolve **to** **`=1`** Claim Target Scope Unit.
- `CA-R-1599@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1599@22`
  - Remaining Claim prose:
    **every** Plan Atom **must** have **`=1`** Definition of Done, including a Hub with no own work.
- `CA-R-1608@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1608@21`
  - Remaining Claim prose:
    the Core Concern Status model **must** inherit the allowed values of Atom.Status and add (Resolved, Canceled).
- `CA-R-1611@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1611@25`
  - Remaining Claim prose:
    reverse-engineering results **must** distinguish observed Implementation facts from proposed decisions about the intended refactored result.
    
    - behavior **or** constraints proposed for preservation **must** be identified as proposed decisions.
    - behavior **or** constraints proposed for change **must** be identified as proposed decisions.
    - unresolved behavior, missing evidence, **and** uncertain interpretations **must** remain explicit.
    
    an observed behavior **or** defect **must not** become a Requirement merely because it exists **in** the legacy Implementation. supporting evidence **must** remain recoverable **without** a proposed disposition **or** uncertainty being presented as an observed fact.
- `CA-R-1627@29`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1627@29`
  - Remaining Claim prose:
    secret values **must** remain **in** the permitted secret storage defined by CA-D-452. secrets include passwords, API keys, access **or** refresh tokens, session cookies, private keys, signing **or** encryption keys, authentication certificates, one-time **or** recovery codes, **and** connection strings **or** URLs containing credentials.
    
    ### authorized use
    
    - Tools **may** receive secrets from that storage, including through host injection, **and** use them for Operator-authorized authentication.
    - credential use **must** remain within the authorized transport **and** resource boundary. permission **to** authenticate does **not** authorize disclosure elsewhere.
    
    ### excluded surfaces
    
    - secret values **must not** appear **in** Atoms, Project Settings, Framework Instance Settings, generated Artifacts, runtime traces, logs, prompts, checkpoints, Evaluation inputs **and** results, Test fixtures **and** snapshots, evidence, support bundles, issues, pull requests, commits, **or** release records.
    - secret values **must** be redacted **before** data enters those surfaces. encoding **or** encrypting a secret does **not** permit its inclusion outside the permitted secret storage.
    
    ### personal identifiers
    
    email addresses, usernames, **and** account identifiers are identifiers rather than authenticators. they **may** appear **in** CAPRMEDIO **when** necessary **and** authorized, but **must** be minimized **and** treated as potentially personal data. CAPRMEDIO does **not** become the runtime owner merely because a human-readable Artifact names it.
    
    ### exposure response
    
    **if** a secret reaches an unauthorized durable **or** shared surface, stop propagation, revoke **or** rotate it immediately, **then** clean affected Carriers **and** record the incident **without** reproducing the value. deleting a current file is **not** sufficient remediation for a value already present **in** durable history **or** another replica.
- `CA-R-1628@41`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1628@41`
  - Remaining Claim prose:
    the framework-instance interaction reporting setting **must** have **`=1`** value **in** (`silent`, `verbose`).
- `CA-R-1631@34`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1631@34`
  - Remaining Claim prose:
    the Framework Instance Settings Artifact **must** resolve **every** registered optional Projection as active **or** inactive, with inactive as the default **and** an unknown Type value under Projection rejected.
- `CA-R-1634@43`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1634@43`
  - Remaining Claim prose:
    Catalog, Map, **and** Hub **must** be distinct Type values under Projection with no authority over linked Artifact Claims.
    
    a derived terminology list **or** vocabulary diagnostic index **must** use Catalog as its Projection Type; its purpose **and** selected population do **not** admit another Type.
- `CA-R-1646@39`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1646@39`
  - Remaining Claim prose:
    **every** governed proof record **must** bind its observation **to** the exact applicable inputs under which it was produced.
    
    - the binding includes the relevant Artifact **and** Implementation Revisions, configuration, evaluators, environments, **and** material inputs; CA-D-329 governs its representation.
    - reliance on that observation for a current candidate requires a matching input binding **and** satisfaction of its additional governing invalidation conditions.
    - a changed material input makes the affected proof stale for that candidate **until** the required checks run against the changed inputs. a missing **or** unresolved binding is unknown, **not** current.
    - an unrelated change does **not** invalidate proof **unless** it changes the evaluated dependencies **or** satisfies an additional governing invalidation condition.
    - retain the historical record unchanged. **not** (a recent timestamp **or** a refreshed Projection) alone proves currentness.
- `CA-R-1650@32`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1650@32`
  - Remaining Claim prose:
    the bounded session-state envelope **must** contain **only** routing invariants, current scope, applicable settings, compact session state, **and** references needed **to** load active authority on demand.
- `CA-R-1652@39`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1652@39`
  - Remaining Claim prose:
    the necessary-information Confidence Threshold **must** have an Operator-configurable integer-percentage instance default.
- `CA-R-1655@44`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1655@44`
  - Remaining Claim prose:
    CAPRMEDIO **must** resolve **every** Artifact's applicable classification from Applicable Methodology **and** Project Configuration, with structural context from authoritative Project Structure:
    
    - resolve Artifact Type under the applicable Type authority.
    - resolve Content Role **only** for an Atom; do **not** require a Journal **or** Projection **to** have an Atom Content Role.
    - resolve a semantic route **only** **where** the applicable authority defines that classification.
    - classify an unknown, disabled, stale, multiply mapped, **or** ambiguous value as an unresolved **or** failed classification, **not** as an accepted one.
    
    a derived Scope Unit Graph **must not** replace Project Structure as structural authority. reporting a classification failure does **not** itself impose a universal mutation **or** execution prohibition; the applicable Authority Mode **and** admission rules govern that consequence.
- `CA-R-1658@31`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1658@31`
  - Remaining Claim prose:
    a Scope Unit **must not** own a descendant Scope Unit through a stored structural-parent relation **when** another active Scope Unit lies between them.
- `CA-R-1664@36`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1664@36`
  - Remaining Claim prose:
    Rationale **must** be registered as an internal value of `Atom/Content Role: Analysis/Type` that owns **`=1`** explanatory conclusion **without** establishing **or** modifying normative specification.
- `CA-R-1678@29`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1678@29`
  - Remaining Claim prose:
    CAPRMEDIO **must** require operational mechanisms **to** be proportional **to** explicit failure risk **and** a declared authoritative-state boundary. CAPRMEDIO **must not** mandate one recovery **or** durability mechanism for **every** Project.
- `CA-R-1679@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1679@28`
  - Remaining Claim prose:
    CAPRMEDIO permits an effect guarantee **only** **when** its scope, assumptions, owner, temporal boundary, **and** enforcement conditions are explicit. a bounded local guarantee **must** never be presented as universal exactly-once execution.
- `CA-R-1681@33`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1681@33`
  - Remaining Claim prose:
    a reusable model rule belongs **in** CORE_META_MODEL **only** **when** it establishes reusable methodology authority **and** remains independent of implementation choices outside the Entity explicitly governed by its Claim. a Carrier format, mechanism, portability boundary, **or** external constraint **may** be named **when** that Entity itself is governed, but **must not** become a hidden prerequisite of unrelated Claims. project-specific implementation choices **must not** be imported as reusable methodology authority.
- `CA-R-1683@45`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1683@45`
  - Remaining Claim prose:
    CAPRMEDIO **must** distinguish RMED Spec authority for governed Entities; CAPO Change content under CA-R-1549@21, including specific reusable Operations definitions under CA-R-2463; concrete Implementation; actual executions **and** their Journal Records carrying facts, state changes, **and** Claim-bound evidence; **and** Verification judgments about sufficiency **and** currentness. Evaluation results, evidence, dashboards, **and** Verification judgments **may** support, challenge, **or** invalidate reliance on a Claim, but **must not** themselves establish, edit, replace, **or** override semantic authority.
- `CA-R-1687@31`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1687@31`
  - Remaining Claim prose:
    provenance establishes the origin, carrier identity, revision, sequence, **and** transformation history of a governed claim **or** Implementation. it does **not** by itself establish that the claim is correct, accepted, current, applicable, **or** sufficiently assured.
    
    complete governed provenance remains owned under CA-R-1720. a storage-history record, Author identity, session identifier, signature, hash, **or** intact Carrier proves **only** the bounded historical fact it records. **none** of those facts becomes evidence for the carrier's semantic claim **without** a separate, explicit claim-bound Evidence relation.
    
    Evidence used for reliance **must** identify the claim it supports, the relevant carrier **or** Journal Record, the producing **or** interpreting work **or** Method **when** material, **and** the applicable scope **and** time boundary. Verification remains a separate Evaluation conclusion. a claim, its carrier, **and** the work that created it **must not** silently evidence themselves.
- `CA-R-1690@33`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1690@33`
  - Remaining Claim prose:
    an Operator-accepted DDL, file schema, API, protocol, host format, supported-platform interface, CI interface, dependency boundary, **or** comparable external obligation is represented by its primary semantic contribution **and** external Governance Origin.
    
    - Content Role follows the Claim's primary contribution under CA-R-1531@20, independently of Governance Origin under CA-R-1701. an external origin does **not** by itself assign Requirement **or** **any** other Content Role.
    - an obligation imposed by an identified external source retains external Governance Origin **and** pins the applicable source version **or** digest. its graph connections use typed Relations whose Carrier encoding is governed by CA-D-268; these Relations do **not** create another Governance Origin.
    - Implementation **must** conform **to** the exact accepted obligation Revision it consumes **and** **must not** rewrite that obligation. a changed external source creates a new accepted Revision **when** the same obligation remains identifiable. a different obligation requires a new Atom **and** explicit predecessor **and** successor Atom IDs **in** the predecessor's archival Journal event, **not** a formal replacement Relation.
    - existing Implementations remain bound **to** their consumed Revisions **until** lineage-impact review determines their disposition.
    
    Requirement authority defines the external boundary **and** admitted Type values. Delivery authority governs Carrier names, identities, **and** Catalog representations. this separation does **not** reclassify those Carrier specifications as Requirements because their source is external.
- `CA-R-1695@36`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1695@36`
  - Remaining Claim prose:
    **every** structural Scope Unit that realizes RMED Atoms **must** record its Implementation Bindings **in** the shared Project Work Journal. its admitted Records establish, replace, correct, **or** remove Implementation Bindings **and** bind exact Requirement, Method, Evaluation, **and** Delivery Atom Revisions **to** the native implementation targets that declare their realization.
    
    the Journal is canonical for the declared implementation relationship. native source, configuration, executable evaluation mechanisms, packages, **and** delivery automation remain canonical for the operative realization itself. Operations evidence **and** Verification remain the authorities for what occurred **and** whether the realization is sufficiently assured. recording an implementation relationship never proves correctness **or** successful operation.
    
    an Implementation Binding **must** survive transformations **or** migration of secondary storage history. the binding therefore identifies **every** source Atom by stable artifact identity plus revision digest **and** **every** native implementation target by a stable locator plus content digest. secondary storage records, review records, Authors, sessions, **and** signatures remain useful provenance but are **not** the sole semantic identity of the binding.
    
    corrections, replacements, target removal, **and** changed implementation coverage append new records; accepted Journal records are never edited, reordered, **or** deleted. the effective implementation frontier is derived from the complete ordered record sequence.
    
    Implementation-role Projections are regenerated from the Journal **and** its declared current source **and** target frontier. they **may** present implementation coverage, mappings, missing realization, **and** potentially stale bindings, but they remain rebuildable **and** non-authoritative over the Journal, normative Atoms, native implementation, **or** evaluation conclusions.
- `CA-R-1696@36`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1696@36`
  - Remaining Claim prose:
    CORE_META_MODEL authority **must** define reusable model invariants **and** expansion boundaries **without** hidden dependence on a programming language, LLM provider **or** model, agent host, operating system, repository host, package manager, database, deployment platform, **or** other replaceable implementation mechanism.
    
    mechanism-specific obligations belong **to** the Scope that owns the mechanism. Extensions **and** PROJECT_CONFIGURATION **may** expand the model for their bounded use **without** rewriting its governing Claims.
    
    CORE_META_MODEL **may** name a mechanism **only** **when** the mechanism itself is the explicit Entity governed by the Claim, such as a Carrier format, portability boundary, **or** external constraint; this reference **must not** make that mechanism a hidden prerequisite of unrelated model Claims.
- `CA-R-1698@31`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1698@31`
  - Remaining Claim prose:
    CAPRMEDIO evolves governed authority through recoverable revisions that preserve the exact historical meaning on which accepted downstream work relied.
- `CA-R-1700@32`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1700@32`
  - Remaining Claim prose:
    a Role admits a Form value for an Atom **only** **when** that role has an independently governed atomic unit that benefits from stable identity, admission, **and** whole-unit lifecycle.
- `CA-R-1701@34`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1701@34`
  - Remaining Claim prose:
    Artifact Type, Atom Content Role, **and** Governance Origin **must** remain distinct classification axes **without** requiring an Artifact **or** a new Type for **every** possible combination; the Content Role axis applies **to** Atoms **only**.
- `CA-R-1702@46`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1702@46`
  - Remaining Claim prose:
    **every** transition through Concern, Analysis, Plan, Requirement, Method, Evaluation, Delivery, Implementation, **and** Operations produces **or** updates the meaning owned by the receiving Content Role **without** converting the source meaning into that role **or** implying completion of a later role.
    
    **in** particular:
    
    - Analysis owns findings, alternatives, explanation, **and** rationale;
    - Plan states intended work **without** realizing it; decomposition relates independent Plan Atoms **without** merging their Claims;
    - Requirement establishes model definitions, required properties, outcomes, **or** boundaries **without** selecting their Method;
    - Method provides authorship, construction, **and** Implementation conventions, Evaluation checks correctness, **and** Delivery specifies Carrier contents **and** boundaries;
    - Implementation materially realizes accepted Spec Claims **and** **may** contain procedural code, but does **not** prove Evaluation **or** operational success; **and**
    - Operations owns specific reusable Action behavior, Workflow graph, **and** Step invocation binding; Actor participation **and** authorization remain Requirement rules. actual executions **and** their Journal Records carrying execution evidence **and** state changes are distinct from those definitions **and** from RMED Spec.
    
    Relations carry meaning between roles while **every** related Artifact retains its own identity, authority, lifecycle, **and** owning role.
- `CA-R-1703@38`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1703@38`
  - Remaining Claim prose:
    an Implementation Overview is a non-authoritative Projection of what the current normative Atom frontier, native project targets, available provenance, **and** **any** registered implementation lineage sources show as implemented. its Implementation Bindings derive from the shared Project Journal under CA-R-1695; the current view does **not** replace the historical implementation event records retained **in** that Journal. the Atom Content Role axis does **not** apply **to** this Projection.
    
    it **may** report realization coverage, source-to-target bindings, relevant commits, **and** unresolved implementation gaps. it is regenerated mechanically **or** rebuilt through governed reasoning from its declared source frontier. it is never an Atom **and** cannot replace the Journal, normative Atoms, native implementation, Operations evidence, **or** Verification.
    
    the presence of this Projection does **not** require an internal Implementation Atom. storage, retention, **and** whether the Projection is committed **or** generated at runtime remain governed separately.
- `CA-R-1704@33`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1704@33`
  - Remaining Claim prose:
    **every** canonical Content Role name **must** be a noun that names its primary contribution **and** remains stable across workflow, Actor, Tool, **and** implementation changes.
- `CA-R-1705@29`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1705@29`
  - Remaining Claim prose:
    a Rationale is an Analysis Atom created **only** **after** **every** specification Atom it explains already exists. the Rationale stores the directed relation **to** its subjects; specification Atoms contain **none** of (embedded Rationale, persisted Rationale backlink).
    
    Rationale is explanatory rather than normative. Changing an obligation, boundary, Method, Evaluation condition, Delivery rule, **or** acceptance meaning requires a new applicable specification Atom rather than a Rationale.
- `CA-R-1708@39`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1708@39`
  - Remaining Claim prose:
    an Artifact **must** have **`=1`** Type admitted by applicable authority; the Core values are specified by CA-R-1405 **and** remain open **to** permitted expansion.
- `CA-R-1713@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1713@26`
  - Remaining Claim prose:
    Execution confidence **must** never create, extend, **or** replace operator authority.
- `CA-R-1717@29`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1717@29`
  - Remaining Claim prose:
    Generated-data stage names **must** classify transformation position **without** becoming Artifact forms, Content roles, Governance origins, scope coordinates, **or** sources of authority.
- `CA-R-1718@35`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1718@35`
  - Remaining Claim prose:
    independently governed meanings **must** remain distinct even **when** ordinary language, one Carrier, one workflow, **or** one Implementation change presents them together:
    
    - an Entity is **not** its description **or** Carrier;
    - a Requirement is **not** its Method;
    - a Method is **not** its Implementation;
    - an Evaluation criterion is **not** its execution result;
    - provenance is **not** evidence; **and**
    - an observed fact is **not** authority for the desired state.
    
    **if** wording could resolve **to** multiple governed meanings, **then** the intended meaning **and** its owning Type **must** be resolved **before** the Claim is admitted. this is an admission condition, **not** a definition of the recovery Action **or** Workflow.
    
    co-location, readable presentation, automation, **or** a Relation between meanings **must not** merge their identities **or** transfer their semantic force.
- `CA-R-1719@33`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1719@33`
  - Remaining Claim prose:
    a CAPRMEDIO invariant, claim, relation, **or** classification retains the same meaning **when** applied recursively at the Project root **or** **any** configured descendant structural scope. **every** use remains bounded **to** its declared scope **and** applicability; recursion does **not** widen authority, evidence, evaluation, **or** implementation coverage.
- `CA-R-1724@36`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1724@36`
  - Remaining Claim prose:
    the Framework Instance Settings Artifact **may** select, combine, parameterize, activate **in** foreground **or** background, **or** disable available Tools **and** Extensions **and** **must** resolve composition precedence explicitly **without** changing **any** selected capability's governed meaning. installation establishes availability, **not** activation: an installed Extension **may** remain disabled, **and** its retained settings do **not** enable it **unless** the Framework Instance Settings Artifact explicitly does so. the Framework Instance Settings Artifact **must** own the current activation selection **and** selected revision of **every** selected Extension.
- `CA-R-1726@29`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1726@29`
  - Remaining Claim prose:
    an admitted Concern is active while its independently resolvable matter still requires disposition **and** solved **after** that matter receives its terminal disposition. archival preserves a Concern that is obsolete, invalidated, duplicated, **or** absorbed **without** representing it as solved.
- `CA-R-1732@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1732@25`
  - Remaining Claim prose:
    an improvement proposal **must** target the narrowest governed owner capable of resolving its evidence-backed cause.
- `CA-R-1734@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1734@26`
  - Remaining Claim prose:
    **every** governed self-improvement stage **must** retain the canonical Content-role meaning of the artifact that represents it **without** absorbing the meaning of an earlier **or** later stage.
- `CA-R-1740@38`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1740@38`
  - Remaining Claim prose:
    **every** Project Scope Unit Graph Projection value **must** retain traceability **to** the exact Project Structure state, Settings state, Atom Revisions, Carrier observations, **or** Journal Records actually used **to** derive it. an unavailable **or** contradictory source **must** produce an explicit unresolved result for the affected value **without** erasing independent observations **or** claiming complete source coverage. declared values **and** observed materialization **must not** be conflated.
- `CA-R-1742@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1742@27`
  - Remaining Claim prose:
    Implementation **must** realize a recurrence Evaluation Atom through an executable test, evaluation, monitor, alert, **or** other conforming mechanism.
- `CA-R-1744@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1744@28`
  - Remaining Claim prose:
    an Operator-mandated Project-specific substrate **must** be governed by Project authority **or** PROJECT_CONFIGURATION **without** becoming an implicit prerequisite of the reusable CORE_META_MODEL.
- `CA-R-1747@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1747@28`
  - Remaining Claim prose:
    a native project target is Implementation rather than a governed Artifact **unless** CAPRMEDIO separately admits an Artifact identity that represents **or** binds it.
- `CA-R-1750@39`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1750@39`
  - Remaining Claim prose:
    an Operator-selected setting **must** have **`=1`** authoritative owner: Project Settings for Project initialization inputs, including Project Settings Name **and** Project Settings Prefix; Framework Instance Settings for CAPRMEDIO behavior, configuration choices, **and** Authority Mode defaults; **or** Project Structure for an explicit per-Scope-Unit Authority Mode override. Atoms define permitted parameters, constraints, **and** applicability **without** fixing **or** duplicating current selected values **or** Default Settings values. definitions **and** storage rules for Project Settings Name **and** Project Settings Prefix belong **to** CORE_META_MODEL.
    
    ### Current source pin
    
    Proposed N+1 successor of `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1750-CORE_META_MODEL--partition-operator-settings-between-settings-artifacts.md`, CA-R-1750@37, SHA-256 `a9222939e3847db6a2c5da16b55122c4108b4f467d8609452dc581088ea9d77c`. Current bytes remain unchanged; this Draft performs no promotion or runtime change.
- `CA-R-1755@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1755@27`
  - Remaining Claim prose:
    **every** Extension **must** affect **only** its declared applicability boundary.
- `CA-R-1756@35`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1756@35`
  - Remaining Claim prose:
    **every** Scope Unit **must** own **only** its direct child Scope Units through the same recursive structural-parent relation.
- `CA-R-1758@35`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1758@35`
  - Remaining Claim prose:
    **every** Scope Unit **must** have **`=1`** Type value **in** (Ordered, Unordered).
- `CA-R-1765@35`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1765@35`
  - Remaining Claim prose:
    an Artifact Type value **must not** use NARROWER_THAN **to** establish its admission as an Artifact.
- `CA-R-1770@31`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1770@31`
  - Remaining Claim prose:
    a Concern whose subject spans multiple Structural scopes belongs **to** their narrowest common ancestor.
- `CA-R-1771@29`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1771@29`
  - Remaining Claim prose:
    a Scope Unit **may** own (Ordered Scope Units **and** Unordered Scope Units) as direct children.
- `CA-R-1775@33`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1775@33`
  - Remaining Claim prose:
    **every** parent Scope Unit **must** own the Goal Atoms for its immediate child Scope Units under CA-R-926; those Goal Atoms belong **to** the parent's Owned Atoms **and** the child's Targeting Atoms **without** transferring their ownership.
- `CA-R-1789@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1789@21`
  - Remaining Claim prose:
    the executor **must** provide a self-contained Invocation sufficient for the receiving context **to** perform the admitted Action **without** remembering the Workflow procedure from earlier conversation.
    
    - identify the Workflow Run **and** Step Run, exact admitted definition bindings, bound inputs **or** accessible references, relevant prior results **and** actual effects, applicable permissions, **and** required output.
    - provide the instruction derived from the Action **and** its Step binding, including how **to** return the result **or** request missing input. the instruction is a derived presentation of governing authority, **not** another independently maintained procedure.
    - an Integrated Invocation returns this context **and** instruction through the session interface; an Isolated Invocation supplies it **to** the separate context. no particular transport is required by this core rule.
- `CA-R-1790@19`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1790@19`
  - Remaining Claim prose:
    the executor **must** retain execution state **and** select subsequent Steps from the Workflow's declared transitions. the participating session **or** separate Agent context performs the requested Action; it need **not** reconstruct **or** remember what the Workflow will do next.
- `CA-R-1791@18`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1791@18`
  - Remaining Claim prose:
    requesting participation **or** returning a prompt **must not** itself complete a Step Run.
- `CA-R-1792@18`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1792@18`
  - Remaining Claim prose:
    a terminal Workflow handoff **must** end the predecessor Run **and** let the executor admit a separate successor under `CA-R-1520-CORE_META_MODEL-GENERAL-REQUIREMENT--return-workflow-handoffs-through-terminal-results`. a session instruction **must not** silently resume an ended Run **or** bypass approval.
- `CA-R-1793@18`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1793@18`
  - Remaining Claim prose:
    the receiving context **must** report actual results against the identified Invocation. redelivery **or** reconnection **must not** imply permission **to** repeat already performed effects.
- `CA-R-1873@18`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1873@18`
  - Remaining Claim prose:
    Implementation production **must** derive I from current applicable RMED using governed Operations: **RMED → using O → I**. native I **may** subsequently act as source truth for its actual realized content, structure, dependencies, **and** behavior. a further view derived from I using O, including a dependency graph, **must** remain a non-authoritative Projection: **I → using O → Projection**.
- `CA-R-1874@19`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1874@19`
  - Remaining Claim prose:
    the Core allowed values of Operations Status **must** be exactly (Draft, Active, Archived); that one Content Role Status model applies to Operations Atoms with Type Workflow, Step, or Action unless an admitted Extension or Project Configuration establishes a more-specific Status domain under that exact Content Role and Type path.
- `CA-R-1875@19`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1875@19`
  - Remaining Claim prose:
    the Core Analysis Status model **must** inherit the allowed values of Atom.Status and add Done. That Content Role Status model applies to Analysis Atoms with Type Analysis Report or Rationale. An admitted Extension or Project Configuration **may** add values under the applicable complete Content Role and Type path; it **must not** remove inherited values.
- `CA-R-1990@12`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1990@12`
  - Remaining Claim prose:
    `Atom/Content Role: Plan.Enabled Relations.Contains` **must** be True. a Plan Atom **may** contain other Plan Atoms.
- `CA-R-1991@13`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1991@13`
  - Remaining Claim prose:
    `Atom/Content Role: Operations/Type: Workflow.Enabled Relations.Contains` **must** be True. a Workflow Atom **may** contain Step Atoms.
- `CA-R-1994@15`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1994@15`
  - Semantics:
    Subjects intentionally include actual things, descriptions and abstract topics. This mix does not make them one uniform kind of entity. A description can itself be a separate Subject; it is not the thing described.
    
    Artifact is a Term for a Node instance delivered into one or more Carrier instances. Carrying a record of an occurrence does not carry the actual occurrence. Artifact does not name another Node kind or branch. A Carrier remains distinct from what it represents.
  - Remaining Claim prose:
    An Entity used as a Subject-graph node must identify a thing or topic addressed by the graph; its description and Carrier remain separate.
- `CA-R-2003@15`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-2003@15`
  - Semantics:
    Property is the proposed kind `Entity/Property`, grounded in bearer dependence through IS_PROPERTY_OF. Its lexical Term is separately defined at `Term//Property`. Classifying an occurrence in that kind does not invent a bearer edge or treat a missing edge as proof of independence. The Property occurrence has identity qualified by its immediate bearer; the Property definition supplies its value Format and direct-value cardinality. The bearer-Relation count is distinct from the number of values a Property allows.
  - Remaining Claim prose:
    Every declared Property occurrence must have exactly one immediate bearer, identified by one outgoing direct IS_PROPERTY_OF connection to that bearer. A source establishes dependence independently of whether the edge is present, so a missing edge fails this requirement. The named Selection “Property Occurrences” selects those declared occurrences; it does not infer dependence from edges or create a bearer connection.
- `CA-R-2173@6`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-2173@6`
  - Semantics:
    Implementation is not a Projection merely because it realizes RMED. Its logical artifacts remain distinct from their Carriers and from the Runtime in which technical execution occurs.
    
    A Projection is a non-authoritative output produced from a declared source selection through a Workflow: source of truth → Workflow → Projection. Changes to a Projection belong in its authoritative sources, followed by a rebuild through its Workflow. A generated view of Implementation is a Projection; that does not make its directly edited sources Projections.
  - Remaining Claim prose:
    Implementation **means** the actual Code, Prompts, Documentation and Resources that realize RMED for a Project. Directly edited Implementation can be authoritative for what is actually implemented.
- `CA-R-2271@3`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-2271@3`
  - Remaining Claim prose:
    Framework Settings may explicitly override the necessary-information and semantic-resolution confidence defaults as integer percentages. Their effective defaults remain Operator-configurable under CA-R-1652 and CA-R-380; absence of an explicit value preserves the governed default resolution.
    
    Tool Selections groups the selected active/background capabilities and their per-capability settings. Extension Selections groups enabled or disabled installed Extensions, selected Versions where applicable, and retained per-Extension settings. These are structured groups with no direct scalar value; retaining settings does not enable a disabled Extension. Their internal declarations remain governed by applicable D authority, not a new generic schema.
    
    ### Formal claim
  - Fenced Claim block:
```text
Project.Framework Settings.Confidence.Necessary Information Threshold[int]{0..1}
Project.Framework Settings.Confidence.Semantic Resolution Threshold[int]{0..1}
Project.Framework Settings.Tool Selections{0}
Project.Framework Settings.Extension Selections{0}
```
- `CA-R-2275@2`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-2275@2`
  - Remaining Claim prose:
    ID **means** a unique identifier used **to** find **`=1`** entity instance, whether Continuant **or** Occurrent, whose uniqueness is bounded **to** its matching prefix namespace. This Claim explicitly introduces the lexical Term instance named ID at `Entity/Object/Continuant/Term//ID`.
- `CA-R-2276@3`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-2276@3`
  - Remaining Claim prose:
    **every** entity represented **in** the Subject Graph **and** **every** declared Relation Type entity **must** have **`=1`** complete canonical name formed from reusable Terms **and** any applicable registered qualification syntax **and** used exactly **in** **every** authored occurrence that mentions it. **every** such complete name **must** identify **`=1`** entity, distinct complete names **must not** identify the same entity, **and** the same complete name **must not** identify distinct entities. Outside `Term`, the complete canonical name **must** be the full admitted expression, **not** a single registered Term; the Subject root `Entity` is the sole exception.
- `CA-R-2278@2`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-2278@2`
  - Remaining Claim prose:
    Each logical model Entity has exactly one canonical defining Requirement of Type Entity Definition. Its governed Subject identifies the defined entity. Relation Definition qualifies through the accepted specialized template without a subtype hierarchy. Additional scoped Requirements may constrain an Entity but are not additional Entity Definitions. This applies to Objects, Aspects, Graph Syntax, Carriers and their dependent properties; a Scope Unit does not change the Entity's identity or defining meaning.
    
    A missing canonical Definition or multiple qualifying Definitions fails this requirement. Derived IS_DEFINED_BY identifies that one Definition. Do not create new entities for every characteristic or nuance merely to multiply Atoms; preserve one coherent Claim and report weak fits of the dedicated-Definition trial. Equivalent property headings denote one logical Entity.
    
    For / specialization, the narrower Definition inherits the broader Definition and states only its differences. For // instantiation, the instance follows its kind Definition and states only instance-specific facts. Reuse the applicable base structure, properties and constraints instead of copying them. Containment > adds no inheritance. A Method Atom is an Atom with Content Role Method, not a repeated definition of Atom.
- `CA-R-380@42`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-380@42`
  - Remaining Claim prose:
    the semantic-resolution Confidence Threshold **must** have an Operator-configurable instance default.
- `CA-R-626@40`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-626@40`
  - Remaining Claim prose:
    **every** Project Scope Unit Graph Projection **must** distinguish declared Scope Unit facts from Project Structure, derived structural values, effective Settings, **and** observed Carrier materialization. a discrepancy, missing Goal, undeclared candidate directory, **or** declared unit with no existing Carrier **must** remain visible as a separate finding **without** silently changing the declaration **or** inventing source authority.
- `CA-R-718@43`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-718@43`
  - Remaining Claim prose:
    an Atom's Claim Target Scope Unit reference **and** applicability restrictions **in** its Main Content **must not**, by themselves, establish an additional edge **in** the Scope Unit tree **or** alter structural-parent ownership.
- `CA-R-740@36`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-740@36`
  - Remaining Claim prose:
    **every** Atom **must** have **`=1`** Content Role.
- `CA-R-833@29`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-833@29`
  - Remaining Claim prose:
    the normative-authority subgraph **must** form an explicit, typed, **and** acyclic hierarchy.
- `CA-R-852@32`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-852@32`
  - Remaining Claim prose:
    **every** AI Agent Delegation **must** identify its Operator, AI Agent, allowed actions, allowed target Scopes, constraints, validity boundary, **and** revocation state.
- `CA-R-853@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-853@27`
  - Remaining Claim prose:
    **every** governed action **must** identify its initiating Actor **and** the approval **or** active delegation that authorized it.
- `CA-R-886@39`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-886@39`
  - Remaining Claim prose:
    **every** Scope Unit reference **in** an Atom whose Atom Scope is a Scope Unit **must** resolve relative **to** that Scope Unit.
- `CA-R-920@33`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-920@33`
  - Remaining Claim prose:
    **every** Atom **must** have **`=1`** Scope.
- `CA-R-924@37`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-924@37`
  - Remaining Claim prose:
    the Core contribution **to** allowed qualified Types of Relational Atom **must** be (`Atom/Content Role: Requirement/Type: Goal`, `Atom/Content Role: Requirement/Type: Demand`, `Atom/Content Role: Plan/Type: Plan`); a Plan is relational **only** **when** its actual Claim target differs under the Relational Atom definition, **not** merely because it has decomposition, blocking, **or** a particular Label.
- `CA-R-926@38`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-926@38`
  - Remaining Claim prose:
    **every** non-Project Scope Unit **must** have **`>=1`** accepted Goal Atom owned by its declared direct parent Scope Unit. this is a Goal-coverage obligation, **not** the source of the child's structural identity; a missing accepted Goal is a reported gap **and** **must not** remove **or** conceal the declared Scope Unit.
- `CA-R-933@33`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-933@33`
  - Remaining Claim prose:
    **every** Demand Atom **must** constrain **`=1`** Producer result on which its Consumer's accepted Goal depends.
- `CA-R-942@32`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-942@32`
  - Remaining Claim prose:
    Subtree-owned Atoms **means** the union of Owned Atoms for the selected Scope Unit **and** **every** descendant Scope Unit.
- `CA-R-944@39`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-944@39`
  - Remaining Claim prose:
    a Demand direction **means** from its Consumer Atom Scope Unit **to** its Producer Claim Target Scope Unit.
- `CA-R-947@39`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-947@39`
  - Remaining Claim prose:
    a Goal Atom **must** identify **`=1`** Claim Target Scope Unit that is a direct child of its Atom Scope Unit according **to** authoritative Project Structure, **or** the Project Scope Unit **if** its Atom Scope **contains** no Scope Unit. a Goal reference assigns a purpose **and** **must not** independently declare **or** change the target's Name, parent, order, **or** Carrier binding.
- `CA-R-951@33`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-951@33`
  - Remaining Claim prose:
    a Consumer Scope Unit **must** own a Demand Atom **only** **when** its accepted Goal authorizes an exact dependency on the demanded Producer result.
- `CA-R-954@33`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-954@33`
  - Remaining Claim prose:
    **every** Demand Atom **must** constrain **`=1`** Implementation result produced by its Claim Scope.
- `CA-R-979@30`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-979@30`
  - Remaining Claim prose:
    **every** new Scope Unit **must** use Unordered as its default Type value.
- `CA-R-981@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-981@28`
  - Remaining Claim prose:
    **every** non-Project Scope Unit **must** receive a default Navigational Order Number equal **to** its one-based chronological creation position among Scope Units created under the same parent.
- `CA-R-983@29`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-983@29`
  - Remaining Claim prose:
    the Operator **may** replace the default Navigational Order Number independently for **every** non-Project Scope Unit.
- `CA-R-999@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-999@26`
  - Remaining Claim prose:
    a Scope Expression **means** one deterministic expression that identifies Governed Entities through atomic references, explicit Atom IDs, parentheses, registered set **or** logical operators, **and** field predicates including **where**.
- `CA-M-113@40`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-113@40`
  - Remaining Claim prose:
    **to** write one Claim **in** CAPRMEDIO Controlled English, the Author **must** satisfy **all** of the following:
    
    - use the controlled English subset of the identified CCE version.
    - name **every** necessary participant **and** relation explicitly.
    - state **every** necessary modality, quantity, condition, **and** boundary explicitly.
    - resolve the entity **and** its full canonical name for **every** named Subject Graph component **or** target **and** **every** source-declared Relation Type named inside `((...))` **before** authoring a mention of it; use the exact full word **or** phrase established by its active Entity Definition Atom. report an unresolved **or** conflicting binding rather than choose a synonym **or** infer an entity from matching spelling alone.
    - use the same exact full canonical name **in** **all** authored mentions of the same entity, including entity names, Claims, Claim Scope, Semantics, Details, instructions, descriptions, **and** explanations. do **not** introduce another full name for stylistic variation **or** use the same full canonical name for a different entity. properties, values, bearers, contexts, **and** registered synonyms provide no exception **to** this rule.
    - read **every** reusable component Term's explicit authoritative Method Atom of Type Term Definition directly **and** use its declared meaning consistently **in** **every** composition. agreement among Entity Definitions **or** their Semantics does **not** define a component Term. report a missing, ambiguous, **or** conflicting Term Definition **without** inventing its meaning. reuse of a Term **in** different full names is **not** a naming collision **when** its meaning remains consistent. outside the Term branch, a complete entity name **must** use the full admitted expression **and** **must not** be just one registered Term, except for the Subject root `Entity`; do **not** infer a new graph entity from a component Term alone.
    - treat repeated references **to** the same entity as repeated uses of its canonical name, **not** duplicate entities. resolve an `@` call payload **to** that entity **without** creating an alias **or** a separate naming object. require source-defined Relation Type authority for a name inside `((...))`; successful parsing alone does **not** admit its meaning **or** Relation Type.
    - keep syntax symbols, delimiters, **and** selector keywords distinct from entity names. resolve the separately named entities using the registered `/`, `//`, `.`, `:`, `+>`, `<+`, `>|`, **and** `|<` constructs, `@` calls to already declared Entities, logical grouping `()`, direct-value Format and count markers, the two independent Relation count positions, **and** the source-defined Relation Type named inside `((...))` under CA-R-1931 **and** CA-R-2244. preserve the contextual topic/code spellings `atom.id` **and** `projection.id` for their respective ID Properties. they are not alternative complete canonical Subject names **or** case-folded aliases; authored Subjects use their full admitted expressions. the dot remains syntax **and** does **not** create an entity by itself. under CA-R-1325, an arbitrary complete composite expression does **not** automatically become another full canonical name **or** entity.
    - resolve the effective CCE Role Profile under CA-M-308-CORE_META_MODEL-CORE-METHOD--resolve-the-effective-cce-role-profile **and** satisfy that profile under CA-M-315-CORE_META_MODEL-CORE-METHOD--validate-claims-against-effective-cce-role-profiles.
    - choose wording under CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning.
    - exclude ambiguous pronouns, anaphora, ellipsis, unstated defaults, **and** mixed logical groupings.
    - make the content understandable under CA-M-444-CORE_META_MODEL-IMPLEMENTATION_METHOD--atom-claims-expose-their-meaning-conditions-and-consequences-clearly **and** render Terms **and** CCE Operators under CA-M-229-CORE_META_MODEL-IMPLEMENTATION_METHOD--render-governed-terms-and-cce-operators-distinctly.
- `CA-M-120@39`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-120@39`
  - Remaining Claim prose:
    **to** compile the optional direct-relation registry Projection, the Generator **must** perform **all** of:
    
    1. read each declared Relation Type from its governing R Claim(s). The Claim(s) must provide the canonical name and meaning; preserve any relevant inverse, derivation, or transitivity semantics when explicitly stated. report missing **or** conflicting defining Claims without inventing a name, meaning, direction, or derivation.
    2. Keep governing Entity Definition constraints separate from descriptive Relation Type metadata. Preserve their endpoint classes, contexts, counts and permissions in the model; a known Type does not require a separate Rule record.
    
    3. derive inverse navigation from the defining Type authority **without** independently authoring an inverse Relation fact. distinguish an independently authored Relation fact from the governing derivation authority and input facts under CA-R-1437; do **not** invent a direct source declaration for a computed result.
    4. retain source traceability for the non-authoritative registry Projection. resolve cross-graph and authoritative-source endpoints against any applicable governing constraint contexts under CA-R-1472. cross-graph references **or** views **must not** admit a foreign Type natively **or** reclassify an external endpoint as a native node of the receiving graph.
- `CA-M-121@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-121@27`
  - Remaining Claim prose:
    **to** evaluate one Scope Expression, the Resolver **must** perform **all** of:
    
    1. resolve **every** exact Atom ID **or** other atomic identity **to** **`=1`** Governed Entity.
    2. interpret **all** `<ENTITY_KIND>` as **every** Governed Entity of that kind within Atom Scope.
    3. interpret **or** as set union.
    4. interpret **and** as set intersection.
    5. interpret **without** as left-side set exclusion.
    6. interpret **where** as retention of **only** members whose field predicate evaluates **to** true according **to** `CA-M-122-CORE_META_MODEL-IMPLEMENTATION_METHOD--evaluate-condition-expressions`.
    7. evaluate the innermost parenthesized set function **before** its containing set function.
    8. use another Scope function **only** **when** an active CCE Method gives that function **`=1`** set meaning.
- `CA-M-122@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-122@28`
  - Remaining Claim prose:
    **to** evaluate one CCE condition expression, the Resolver **must** perform **all** of:
    
    1. evaluate the innermost parenthesized function **before** its containing function.
    2. evaluate **`=`** **and** **`!=`** as exact equality **and** inequality between one governed property **and** one canonical value.
    3. evaluate **`<`**, **`<=`**, **`>`**, **and** **`>=`** **only** for properties with one governed comparison order.
    4. evaluate **in** **and** **not in** as scalar membership **and** non-membership **in** one explicitly parenthesized value list, **or** according **to** CA-M-127-CORE_META_MODEL-IMPLEMENTATION_METHOD--evaluate-set-valued-property-membership **when** the governed property is set-valued.
    5. evaluate **is empty** **and** **is not empty** as absence **and** presence of a governed property value.
    6. evaluate **contains**, **starts with**, **and** **ends with** **only** for governed textual property values.
    7. evaluate **and** as true **only** **when** **every** argument is true.
    8. evaluate **or** as true **when** **`>=1`** argument is true.
    9. evaluate **not** as the inverse truth value of its argument.
    10. evaluate **if** ... **then** as false **only** **when** its antecedent is true **and** its consequent is false.
    11. evaluate **every** as true **only** **when** its predicate is true for **every** member of its population.
    12. evaluate **any** as true **when** its predicate is true for **`>=1`** member of its population.
    13. evaluate **none** as true **only** **when** its predicate is false for **every** member of its population.
    14. evaluate **where** as restriction of one population **to** members whose predicate is true.
    15. use another logical function **only** **when** an active CCE Method gives that function **`=1`** logical meaning.
- `CA-M-127@29`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-127@29`
  - Remaining Claim prose:
    **to** evaluate **in** **or** **not in** for one set-valued governed property, the Resolver **must** evaluate **in** as true exactly **when** **`>=1`** property member **`=`** one listed value **and** **must** evaluate **not in** as true exactly **when** no property member **`=`** **any** listed value.
- `CA-M-135@29`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-135@29`
  - Remaining Claim prose:
    provenance validation inspects **every** recorded change **in** the governed selection. a change contributes an Implementation Relation, implementation coverage, **or** semantic traceability edge **only** **when** it changes **`>=1`** non-generated governed source.
    
    an update **only** **to** generated Projections remains an auditable refresh. it retains its required Journal provenance but cannot become an implementation input **to** the semantic graph that produced the generated Carrier. a mixed change participates **only** through its substantive non-generated governed source changes.
- `CA-M-228@34`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-228@34`
  - Remaining Claim prose:
    Under A1296, follow YAML value interpretation and count null and empty strings as direct values. State any necessary restrictions through the value Format and applicable prose conditions rather than treating them as omitted properties or inventing a universal empty-value policy.
    
    Use prose for cases that do not justify new formal machinery. Keep Tier integer-valued and express its numeric bounds and owner-specific conditions in prose for this review under A1297.
    
    Use string for an Entity value and apply the admitted Entity notation. Do not add a special ref Format or a prior-existence requirement to this basic format check. A defining Atom can introduce its governed entity and path together under CA-A-1285; the path alone supplies no defining authority.
    
    Under CA-A-1283, write a count for each addressed property’s direct values only. Use an explicit {0} on grouping paths such as subjects, while giving their children independent counts. A Claim may carry its formal content directly in a CFEL fence without prose or a separate Formal Claim child. Do not count nested keys as parent values.
    
    Use `{n}` for an exact count, `{n+}` for an unbounded lower limit and `{n..m}` for an inclusive bounded range under CA-A-1280. Use non-negative integer bounds with n <= m; prefer `{0}`, `{0+}`, `{1+}` and `{0..1}` for the common cases. Direct values use `Property[format]{count}`. Relations use two independent slots: `Source {forward-count}RELATION{reverse-count} Target`. For example, `Step {1}+>{1+} Workflow` and `Workflow {1+}<+{1} Step` are equivalent; the first count constrains outgoing links per Source and the second reverse links per Target. Missing slots remain unspecified, and neither slot changes the exactly-one-immediate-whole rule.
    
    **to** write an Entity Expression, start with either a canonical Entity Target reference **or** the exact approved initial lowercase `atom(...)` selector under CA-R-1321, **and** apply `/` in broader-to-narrower order, `//` from an Entity kind to its following named instance, `.` in bearer-to-dependent order, `:` from any X to its allowed value Y, `Part +> Whole` or `Whole <+ Part` for containment, **and** `X >| Y` or `Y |< X` for classification-axis applicability, where Y is the Entity serving as X's Classification. Resolve ordinary named components **other than** the RHS instance name after `//` as Term references under CA-R-1321. The RHS is the instance's name under its separately governed naming/source authority, not an Atom ID and not automatically a Term; the whole qualified path must resolve to exactly one canonical Entity Target that already exists or is explicitly introduced by applicable defining authority under CA-R-1194 and CA-R-1321. In `atom(content_role="Plan").Status`, `Status` is the dependent Property borne by the selected Atom; `Plan` remains the Content Role allowed value qualifying that Atom, **not** Status's bearer **or** Status's allowed value. `.` retains the mechanical native fact Property IS_PROPERTY_OF Bearer; `/` admits no native Entity relation; and `:` does not assign a value. `//` denotes the separate kind/instance Entity connection but syntax alone does not assert or admit an INSTANCE_OF fact, which requires its own Core definition. A defining Atom may introduce the target and path it governs; `@` calls an already declared Entity and `//` names an instance under its applicable source authority. Syntax alone neither creates nor admits a target. The resulting qualified path identifies its canonical target **without** copying it; connecting the Atom **to** that target through GOVERNS **or** DEPENDS_ON creates the Entity Relation, **not** another target Entity.
    
    Use `X/(.Y: Z)` for a Property qualification in this proposal. It identifies an `X` qualified by its own Property `Y` and admitted value `Z`; the qualified `X` is narrower than `X` and inherits applicable `X` features and constraints. `.Y` is neither a primary Entity nor a Property subtype of `X`. The older bare `X/Y: Z` qualification spelling is superseded in this proposal; Current sources and runtime remain unchanged. Method is already a Content Role, so use `Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Method)` as the concrete canonical example; that syntax alone does not admit Method as a Type. Under [CA-D-478](../../07_delivery/CA-D-478-CORE_META_MODEL-ENG_DECISION--store-every-atom-property-in-one-internal-location.md), the qualified Atom Property maps to its existing metadata property such as `content_role` or `type`, without a nested classification object.
    
    `+>` and `<+` are opposite notation writings of the same containment fact, represented by direct IS_CONTAINED_BY and derived CONTAINS; neither denotes inheritance. Use `>|` and `|<` for the HAS_CLASSIFICATION axis, not membership through IS_CLASSIFIED_BY. The Classification endpoint is an Entity serving that role, not a new Classification kind; IS_CLASSIFIED_BY is a separate membership Relation, not the inverse of HAS_CLASSIFICATION. For Status classification, write:
    Here `*` ranges only over admitted Atom Status values, and Current excludes Draft and Archived within that set. This is proposed Draft authoring guidance, not a parser or runtime claim.
  - Fenced Claim block:
```text
Entity/Object/Continuant/Governing Objects/Atom.Status >| Status Group: Draft <+ Draft
Entity/Object/Continuant/Governing Objects/Atom.Status >| Status Group: Archived <+ Archived
Entity/Object/Continuant/Governing Objects/Atom.Status >| Status Group: Current <+ * not in (Draft, Archived)
```
- `CA-M-230@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-230@23`
  - Remaining Claim prose:
    within CCE, a CCE Operator **means** one canonical lowercase word-form token **or** token sequence **or** one canonical symbolic token that one active CCE Method assigns one syntactic **or** logical function.
- `CA-M-232@33`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-232@33`
  - Remaining Claim prose:
    **to** derive an Atom Subjects Graph, the Generator **must** reproduce **every** selected Entity as a direct GOVERNS **or** DEPENDS_ON graph link from its source Atom **to** its target with its exact canonical Entity Target, Entity Path, **and** Relation Kind **without** adding authority, requiring a duplicate target-kind field **in** the Atom's Subjects, **or** creating a separately identified Entity object. a Projection **may** derive a target's kind from its canonical authority **when** the Projection's own Spec calls for that classification; it **must not** independently reauthor that kind **or** require it as duplicated source Subjects metadata. The Subject graph composes selected Entity-root targets according to the governing Entity Definition in CA-R-2462, including the proposed Term and Property branches. Render Package/Project Implementation as the parentless root Package, every Module as belonging to exactly one Package, and nested Packages as belonging to another Package. An unmigrated temporal Carrier admitted temporarily by CA-D-269 retains its source classification as migration evidence **without** changing the direct reference **or** requiring that classification **in** the canonical flat representation.
- `CA-M-233@29`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-233@29`
  - Remaining Claim prose:
    **to** author normative Atom prose, state applicable conditions **and** required behavior positively **when** this preserves the complete Claim; an explicit prohibition is warranted **only** **when** it prevents a real ambiguity **or** protects an important boundary.
- `CA-M-234@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-234@22`
  - Remaining Claim prose:
    the current canonical CCE Operator Registry **must** contain this expandable set:
    
    1. statement form: **to**, **means**.
    2. modality: **must**, **must not**, **may**.
    3. condition: **if**, **then**, **when**, **otherwise**.
    4. temporal condition: **before**, **after**, **until**, **unless**.
    5. quantification: **all**, **every**, **any**, **none**.
    6. logical/set: **and**, **or**, **not**, **without**, **where**.
    7. restriction: **only**.
    8. predicate: **in**, **not in**, **is empty**, **is not empty**, **contains**, **starts with**, **ends with**.
    9. comparison: **`=`**, **`!=`**, **`<`**, **`<=`**, **`>`**, **`>=`**.
- `CA-M-235@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-235@22`
  - Remaining Claim prose:
    **to** author one numeric Cardinality Constraint, the Author **must** serialize one canonical comparison CCE Operator immediately followed by one Nonnegative Integer Literal as a prefix immediately **before** the counted Entity **or** expression; examples: **`=1`** Author, **`>=1`** Requirement Atom, **`<=1`** Type, **`>=0`** Property.
- `CA-M-236@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-236@22`
  - Remaining Claim prose:
    **to** normalize one noncanonical CCE Operator Expression, the Author **must** apply **all** applicable rewrites:
    
    - `each` **to** **every**.
    - `equals` **to** **`=`**.
    - `does not equal` **to** **`!=`**.
    - `both <A> and <B>` **to** `(<A>` **and** `<B>)`.
    - `either <A> or <B>` **to** `(<A>` **or** `<B>)`.
    - `neither <A> nor <B>` **to** **not** `(<A>` **or** `<B>)`.
- `CA-M-240@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-240@28`
  - Remaining Claim prose:
    **to** derive Canonical Signatures from one selected Atom Carrier folder, the Tool **must** inspect **only** active single-statement Atom Claims, identify **every** outermost parenthesized expression that **contains** the **and** Operator **or** the **or** Operator, derive a Canonical Signature **only** **if** the expression satisfies the Restricted Boolean Expression grammar, emit source-identity evidence **and** **every** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, **or** authority decision.
- `CA-M-241@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-241@26`
  - Remaining Claim prose:
    **to** derive Canonical Scope Signatures from one caller-selected Atom Carrier folder, the Tool **must** inspect **only** active Carriers with **`=1`** unwrapped Scope Expression **in** one `## Scope` section, resolve **every** atomic identity against active Atom IDs **in** that selected folder, derive a signature **only** **if** the Scope Expression satisfies the restricted Canonical Scope Signature grammar, emit source identity, source revision, source Carrier digest, source frontier digest, source expression, signature, **and** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, authority decision, **or** dependency relation.
- `CA-M-271@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-271@27`
  - Remaining Claim prose:
    **to** resolve an effective Confidence Threshold, select the first applicable explicit source **in** this precedence:
    
    1. direct Operator input for the current decision context.
    2. an explicit value on the current Plan.
    3. the nearest Hub with an explicit value, walking `IS_CONTAINED_BY` from nearest **to** farthest; read its own current Plan File Carrier under `CA-D-472-CORE_META_MODEL-DELIVERY--serialize-explicit-plan-confidence-overrides`, **not** a separate Objective targeting a folder.
    4. the Framework Instance Settings default.
    
    ### resolution constraints
    
    - an omitted optional override preserves inheritance; another explicit field does **not** stop lookup for the omitted field. a missing mandatory Plan file is invalid, **not** an inherited-setting selection.
    - use current Plan Revisions, **not** historical Carrier copies **or** unrelated nearby files; a Label is **not** an override source.
    - **if** a reached source is invalid **or** ambiguous, **or** no source supplies a value, request Operator disposition **before** the affected autonomous action; do **not** invent a value **or** silently fall through past invalid authority.
    - direct Operator input applies **only** within its stated context.
    - do **not** copy inherited values into Plan overrides. preserve an explicit selection even **when** it **`=`** the inherited value; a later upstream change **must not** overwrite it.
    - this resolution **must not** create another Atom, settings file, **or** execution permission.
- `CA-M-273@38`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-273@38`
  - Remaining Claim prose:
    **to** derive the four Atom sets for a selected Scope Unit, the resolver **must** perform **all** of:
    
    1. establish the complete authoritative source frontier, including Atoms outside the selected subtree that can target a Scope Unit inside it; scanning **only** locally stored Atoms is insufficient for Targeting Atoms **or** Subtree-targeting Atoms.
    2. read **every** candidate Atom's carried current Scope Unit **and** check it against its nearest containing Scope Unit, passing through Atom Collections **and** Plan Hub Carriers **without** treating their nesting as additional Scope Unit ownership. preserve the carried external-Atom Author fallback under CA-D-657-CORE_META_MODEL-ENG_DECISION--use-economical-yaml-frontmatter **when** no containing Scope Unit exists; do **not** invent a Scope Unit owner.
    3. resolve **every** candidate's Claim Target Scope Unit independently of ownership. read the internally carried target; absence of a required value is invalid, **not** permission **to** infer it from placement; apply CA-R-1588-CORE_META_MODEL-RULE--default-plan-target-to-the-enclosing-scope-unit for Plans within Plan containment. an unresolved required target remains unresolved. a reference **to** another Scope Unit **must not** transfer ownership, **and** the target **must** resolve **to** a Scope Unit, **not** a Hub Atom **or** another non-Scope-Unit object. Claim Scope restrictions remain **in** the body sections registered by CA-D-495, including Scope for RMED, **and** do **not** create extra targets.
    4. derive Owned Atoms, Targeting Atoms, Subtree-owned Atoms, **and** Subtree-targeting Atoms under CA-R-1447-CORE_META_MODEL-GENERAL-REQUIREMENT--define-owned-atoms, CA-R-1448-CORE_META_MODEL-GENERAL-REQUIREMENT--define-targeting-atoms, CA-R-942-CORE_META_MODEL-DEFINITION--define-subtree-owned-atoms, **and** CA-R-1449-CORE_META_MODEL-GENERAL-REQUIREMENT--define-subtree-targeting-atoms respectively. use the Scope Unit tree for descendant coverage; do **not** substitute physical subtree membership for Claim targeting **or** inferred inherited applicability for an explicit **or** default Claim target.
    5. retain source Atom **and** Revision references **without** creating additional authoritative Atom copies. apply Content Role, Status, **and** other requested filters **after** resolving the selected set; the alias `spec` selects the Active RMED subset under CA-M-288-CORE_META_MODEL-IMPLEMENTATION_METHOD--use-spec-as-an-alias-for-active-rmed-subtree-targeting-atoms, independently of numeric Tier.
    6. report the exact missing source, owner, target, ancestry, **or** required filter value **and** withhold a complete affected result **when** it is unresolved **or** contradictory. a complete empty set remains empty; an incomplete frontier **must not** be reported as a complete empty set.
- `CA-M-287@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-287@23`
  - Remaining Claim prose:
    **to** name a Content Role, the Author **must not** use a verb, imperative, workflow instruction, Status, **or** activity label.
- `CA-M-291@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-291@24`
  - Remaining Claim prose:
    **to** express Project Structure, use one declaration for **every** non-root Scope Unit, reference its parent by the reserved Project-root reference **or** the parent's unique Name, **and** keep structural Local Order distinct from Navigational Order Number. retain an explicit Label independently of Ordered/Unordered Type. retain a readable derived Scope Unit Path **only** with its checked derivation from declared parentage **and** applicable Carrier conventions; do not author or persist Structural Level, and physical nesting **must not** silently replace logical parentage. use concrete Carrier bindings as declared values rather than repeating them **in** Goal, Requirement, **or** Delivery Atoms. write an Authority Mode override **only** **when** explicitly selected for that unit; an omitted override remains inherited rather than copied as an explicit value. references **and** observations **must** distinguish the declared unit from its existing Carrier **and** Goal coverage.
- `CA-M-295@32`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-295@32`
  - Remaining Claim prose:
    **to** resolve an effective Implementation Retry Limit, select the first applicable explicit source **in** this precedence:
    
    1. direct Operator input for the current execution context.
    2. the current Plan's explicit Implementation Retry Limit.
    3. the nearest Hub with an explicit limit, walking `IS_CONTAINED_BY` from nearest **to** farthest **and** reading its own current Plan File Carrier under CA-D-447-CORE_META_MODEL-DELIVERY--serialize-the-implementation-retry-limit-setting.
    4. Framework Instance Settings, resolving an omitted instance parameter through Default Settings under CA-M-279-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-missing-framework-parameters-from-default-settings.
    
    ### resolution constraints
    
    - an omitted optional retry override preserves inheritance; another explicit field does **not** stop this lookup. a missing mandatory Plan file is invalid, **not** an inherited-setting selection.
    - determine presence, **not** truthiness: **`=0`** is an explicit limit.
    - an invalid **or** ambiguous reached source requires Operator disposition **without** silent fallback; an absent effective value stops the affected retry decision.
    - direct Operator input applies **only** within its stated context.
    - do **not** copy inherited values **or** create separate Objective/settings files. retain explicit overrides even **when** equal **to** the inherited value.
    - use the same Plan identity for a Hub's file **and** folder.
    - resolution does **not** reset the consumed retry count governed by CA-O-024-CORE_META_MODEL-ACTION--control-implementation-retries.
- `CA-M-297@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-297@21`
  - Remaining Claim prose:
    **when** the Operator selects comparison by priority order, the comparison of admissible alternatives **must** use the resolved order of active, applicable criteria as follows:
    
    - an earlier criterion takes precedence over a later criterion.
    - for alternatives tied on **all** earlier criteria, the first criterion that distinguishes them determines their relative preference.
    - later criteria **must not** override a preference established by an earlier criterion.
    - alternatives tied on **all** applicable criteria remain tied.
    - an incomplete criterion order **or** an incomparable result at the current deciding criterion leaves the comparison unresolved; a later criterion **must not** bypass that gap.
    
    this Method defines the comparison technique, **not** priority activation, alternative-selection execution, **or** escalation.
- `CA-M-298@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-298@24`
  - Remaining Claim prose:
    **to** describe a Methodology Source expansion mapping, use **`=1`** explicit mapping description that identifies:
    
    - the source element **and** its provenance;
    - the exact canonical target;
    - the mapping rule;
    - the intended scope of application;
    - the applicable Core Meta-Model distinctions at **any** Local Tier.
    
    apply this same mapping convention **to** Extension **and** Project Configuration sources regardless of provenance. the convention supports CA-R-1375-CORE_META_MODEL-CORE-REQUIREMENT--restrict-methodology-source-expansion-to-core-permission's expansion boundary; it does **not** admit activation **or** reliance. CA-O-054-CORE_META_MODEL-ACTION--admit-methodology-expansion-mappings owns that admission Action **and** re-evaluation following material changes.
- `CA-M-303@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-303@24`
  - Remaining Claim prose:
    **to** author an Atom update Workflow, declare its response **to** identity assessment **in** the Workflow graph rather than **in** the assessment Action **or** executor code.
    
    - reference CA-O-067-CORE_META_MODEL-ACTION--assess-atom-update-identity for the assessment; bind the target Revision, proposed result, applicable authority, **and** evidence **to** that Step. the Action returns its assessment **without** selecting the caller's next Step **or** continuation Workflow.
    - map identity-preserving results **to** the caller's declared update path **and** remaining authorization **and** checks; the assessment alone does **not** perform the update.
    - map replacement-required results **to** a terminal handoff under CA-R-1520-CORE_META_MODEL-RULE--return-workflow-handoffs-through-terminal-results. keep the admitted replacement-continuation binding **in** the Workflow definition, **not** as an assessment Action input. the ending Run does **not** call **or** wait for replacement **or** persist an intermediate update merely **to** replace it.
    - map unresolved results **to** the caller's declared evidence-gathering **or** escalation path; an unresolved result **must not** be treated as approval.
    - include reassessment **when** the proposal changes **or** its evidence becomes stale **before** persistence. a changed Summary remains a replacement under CA-R-1464-CORE_META_MODEL-REQUIREMENT--keep-summary-fixed-for-atom-identity even **when** the request began as an update.
    
    this Method constrains how an Author expresses the caller's graph. it is **not** another Workflow, executable routing service, **or** requirement **to** build the executor through a particular Workflow.
- `CA-M-304@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-304@24`
  - Remaining Claim prose:
    **to** present an Agentic Action for execution, organize its derived instruction around the declared responsibility rather than assumed session memory.
    
    - state the requested outcome, relevant context, exact targets, inputs, available evidence, **and** governing references.
    - distinguish already performed effects from proposed changes, **and** existing permissions from decisions still needed.
    - state the expected result **and** how **to** report uncertainty, failures, partial effects, **or** a request for Operator input. do **not** treat a suggested correction as permission **to** apply it.
    - keep the instruction limited **to** the bound Action. leave next-Step selection **and** cross-Workflow handoff coordination **to** the executor using the governing Workflow.
    - use understandable wording **and** structured points under CA-M-444-CORE_META_MODEL-METHOD--make-atom-claims-easy-to-understand **and** CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning; reference governing definitions rather than copying another authoritative procedure into the prompt.
    - keep internal Tool calls as execution detail under CA-R-1528-CORE_META_MODEL-RULE--record-tool-calls-within-step-runs. **when** an operation needs independently governed routing, checks, **or** approval boundaries, express it as an explicit Step during Workflow authoring rather than inventing Workflow nodes from runtime calls.
- `CA-M-305@20`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-305@20`
  - Remaining Claim prose:
    **to** write a Workflow scheme, express the graph through references **to** its Step Atoms:
    
    - use **`=1`** unambiguous reference for **every** graph node; readable node labels **may** accompany those references.
    - state the entry, declared Step order and structural Relations, Conditional Step routing, **and** terminal outcomes against those nodes.
    - place Action references **and** parameter/input bindings **in** leaf Step Atoms rather than reproducing them **in** the scheme; a containing Step carries its nested substeps and no own Action launch.
    - reference reusable Action behavior from the Steps; do **not** paste it into either the Step **or** graph Claim.
- `CA-M-306@30`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-306@30`
  - Remaining Claim prose:
    **to** author a Plan Atom, apply the common Plan authoring rules independently of Label:
    
    1. resolve **`=1`** effective Author.
    2. state **`=1`** intended work **or** outcome **in** Objective, supported by own work, directly contained Plans, **or** both under CA-R-1575.
    3. resolve its Claim Target Scope Unit under CA-R-1588; keep narrower **or** composite work restrictions **in** Objective, **and** do **not** target an ancestor Scope Unit.
    4. **if** it has own work, resolve **`=1`** effective Assignee **and** assign that work **to** that Assignee. retain the leaf-work bound under CA-R-1589.
    5. write **`=1`** Definition of Done under CA-M-123, carried inside Details under CA-D-470; include applicable own-work and verification conditions. For a containing Plan whose Status is Done **or** Canceled, require every directly contained Plan to be Done **or** Canceled; mixed terminal statuses are allowed, and containment does **not** force a child Status to match the parent.
    6. use a Label **only** for navigation; apply an authoring Subtype **only when** explicitly governed.
    7. express required start dependencies with `BLOCKS`; **when** a Plan is contained by another Plan, declare `IS_CONTAINED_BY` on the child and derive `CONTAINS`; do **not** infer execution dependencies from leading numbers **or** folder placement.
    8. resolve confidence **and** retry values from their applicable sources; store **only** explicitly selected overrides on this Plan.
    9. keep supporting Details within Objective **and** its restrictions **without** another intended outcome. review Objective against the completed Details **and** Definition of Done; explicitly revise Objective **if** needed **and** recheck their agreement.
    10. **only after** that review, derive Summary from the finalized Objective under CA-R-1418 **and** CA-R-2499. retain the established Summary across Revisions; **if** it needs changing, replace the Atom identity under CA-R-1464.
- `CA-M-307@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-307@24`
  - Remaining Claim prose:
    a CCE Role Profile **means** one restriction of shared CCE that identifies the permitted primary Claim contribution, permitted CCE Operator uses, permitted subordinate content slots, **and** prohibited primary contributions for one Content Role **or** one narrower Type **or** content slot.
    
    the current role-specific profiles apply **only** **to** Plan, Requirement, Method, Evaluation, Delivery, **and** Operations Atoms.
    
    Concern **and** Analysis Claims remain subject **to** shared CCE **without** an additional CCE Role Profile. this absence does **not** exempt them from shared CCE **or** authorize normative authority outside their Content Role meanings.
    
    no CCE Role Profile is currently registered for Implementation because the current source set contains no Implementation Atoms. an absent Implementation profile **must not** be replaced by another role's profile **or** treated as role-profile conformance.
    
    a narrower Type **or** content-slot profile **may** restrict its parent role profile **and** define permitted subordinate operator use, but it **must not** change the primary contribution of the Content Role.
- `CA-M-309@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-309@21`
  - Remaining Claim prose:
    **to** write a Plan Claim with the Plan CCE Role Profile, the Author **must** perform **all** of:
    
    1. state the Plan's primary contribution as intended work, an intended outcome, **or** their governed composition under CA-M-306-CORE_META_MODEL-GENERAL-METHOD--author-plan-atoms.
    2. **if** the Plan has own work, identify the action, its object, intended result, Assignee, **and** applicable boundary explicitly. modality, condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators **may** qualify that intended work.
    3. **if** the Plan is supported **only** by decomposition, state its intended outcome **without** inventing own work.
    4. keep reusable procedure authority, normative product boundaries, current realization facts, **and** reusable operational behavior outside the Plan's primary contribution.
    5. write the Definition of Done as the subordinate falsifying Condition Expression under CA-M-123-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-definitions-of-done. condition, temporal, quantification, logical, predicate, restriction, **and** comparison Operators **may** occur **in** that slot **only** to determine whether the Plan remains **not** Done.
    6. keep optional Details subordinate **to** the same intended work **or** outcome; Details **must not** introduce another intended outcome **or** a second Definition of Done.
- `CA-M-310@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-310@23`
  - Remaining Claim prose:
    **to** write a Requirement Claim with the Requirement CCE Role Profile, the Author **must** perform **all** of:
    
    1. state the primary contribution as one Entity model **or** required result by its meaning **and** value under CA-R-2512. express required properties **and** observable boundaries within that model **or** result; an obligation, permission, **or** prohibition alone does **not** select Requirement.
    2. use **must**, **must not**, **may**, **only**, quantification, predicates, comparisons, **and** explicit conditions as applicable **to** state what is required, permitted, prohibited, **or** bounded.
    3. use **means** **only** **when** the Claim defines the governed Requirement subject rather than merely describing it.
    4. express temporal Operators **only** as observable timing boundaries **or** conditions on the required result.
    5. keep procedural selection, ordered execution steps, implementation instructions, **and** reusable operational behavior outside the primary contribution. reference applicable Method **or** Operations authority rather than reproducing it.
- `CA-M-311@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-311@23`
  - Remaining Claim prose:
    **to** write a Method Claim with the Method CCE Role Profile, the Author **must** perform **all** of:
    
    1. state the primary contribution as one reusable authorship, construction, **or** Implementation choice **or** convention for satisfying accepted Spec authority under CA-R-2513.
    2. use **to** for the governed method purpose. identify the applicable inputs, construction **or** selection choices, dependencies, produced result, **and** unresolved-choice handling necessary for reuse. include a performer, order, repetition, **or** stopping condition **only when** the convention requires it; do **not** invent an operational Action **or** Workflow **to** fill a Method template.
    3. use condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators **only** with explicit scope over the affected method content.
    4. use modality **only** to constrain correct performance of the Method; the Method **must not** create an independently governed product outcome **or** permission that belongs **in** Requirement authority.
    5. use **means** **only** **when** defining the governed Method subject **or** one necessary Method-local term.
    6. reference applicable Requirement, Evaluation, Delivery, **and** Operations authority rather than reproducing their independently governed contributions as method steps.
    7. **when** the Method concerns tests, govern how their implementation is constructed **or** selected. the test's checked behavior, fixture, acceptance policy, expected result, **and** disposition remain Evaluation authority; its executable test code is Implementation.
- `CA-M-312@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-312@22`
  - Remaining Claim prose:
    **to** write an Evaluation Claim with the Evaluation CCE Role Profile, the Author **must** perform **all** of:
    
    1. state the primary contribution as one falsifiable check, acceptance criterion, **or** disposition rule against identified checked authority **and** Scope.
    2. state recoverable inputs, the evaluated subject, observable evidence, **and** the condition that yields each result necessary for reproducibility under CA-M-264-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-evaluations-with-reproducible-falsification.
    3. use condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators with explicit scope over the checked evidence **and** result.
    4. use modality **only** to constrain correct evaluation **or** disposition. an Evaluation **must not** create the Requirement that it checks.
    5. specify the checked behavior, case inputs **or** fixture, expected observations, acceptance policy, **and** result disposition required by the check. include a checking procedure **only** as subordinate Evaluation content. reusable test-construction **or** selection conventions belong **in** Method authority; executable test code belongs **in** Implementation; a separately reusable test-running Action **or** Workflow belongs **in** Operations.
    6. report unresolved, unavailable, **or** contradictory evidence as its governed result rather than silently converting it **to** pass **or** fail.
- `CA-M-313@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-313@26`
  - Remaining Claim prose:
    a Delivery Substance **must** use the applicable Delivery CCE Role Profile with these authoring conventions:
    
    1. name the governed Entity or Carrier and state its representation, storage or placement constraint directly.
    2. include format, content, address, placement or lifecycle conditions **when** they are relevant to that contribution.
    3. choose CCE Operators to express the applicable modality, conditions, quantities and comparisons.
    4. use admitted typed Relations when the contribution expresses a representation binding.
    5. keep the Substance about its governed Subject; reference separately governed contributions instead of redefining them.
- `CA-M-314@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-314@22`
  - Remaining Claim prose:
    **to** write an Operations Claim, the Author **must** first resolve its admitted Operations Type **and** **then** apply **`=1`** primary Type profile:
    
    1. for Action, use **means** to define the named reusable operational behavior. state its required inputs, preconditions, operational contribution, returned results, observable effects, **and** failure results. modality, condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators **may** constrain that behavior.
    2. for Workflow, use **means** to define the reusable graph through Step references, entry, typed transitions, result conditions, **and** terminal outcomes. use condition, temporal, logical, restriction, predicate, **and** comparison Operators **only** with explicit transition scope under CA-M-305-CORE_META_MODEL-METHOD--write-workflow-schemes-using-step-references.
    3. for Step, define the invocation binding of **`=1`** referenced Action with its parameters **and** inputs. do **not** copy the Action behavior **or** define another Workflow.
- `CA-M-385@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-385@22`
  - Remaining Claim prose:
    Generate the structural Inherency and selected named declaration views with deterministic code from their selected sources and explicit governing evidence. **Do not** use an LLM to choose nodes, classify edges, invent relations or arrange the output.
- `CA-M-442@3`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-442@3`
  - Remaining Claim prose:
    **to** author one CCE Claim **and** its derived Summary, an Author **must** use these authoring constraints:
    
    - express **`=1`** coherent contribution whose full meaning is covered by one precise Summary using the applicable CCE Content Role profile. carry it under the primary contribution heading registered for the Content Role rather than imposing the literal heading Claim on **every** role.
    - resolve **`=1`** Claim Target Scope Unit independently of ownership. select the current Scope Unit as the authoring default **or** an explicitly permitted different target; carry the resolved value under the target Scope Unit carrier definition. express applicability under the applicability carrier definition. for RMED, describe what the Claim applies **to**, including applicable conditions **and** exclusions, **in** Scope; do **not** merely repeat the carried current **or** target Scope Unit; those restrictions alone do **not** make the Atom Relational.
    - keep Details within the primary contribution. for RMED, read the Claim within its Scope; Details **must not** change either. **if** supporting content reveals an incomplete **or** inaccurate contribution **or** applicability, revise the affected Scope **or** primary contribution explicitly **and** recheck agreement; do **not** hide the change **in** Details.
    - write Summary **only after** the other body sections **and** the contribution review are complete. shorten the finalized primary contribution. use plain wording that expresses the Claim’s meaning. preserve established principle names such as DRY **and** MECE instead of paraphrasing them. a familiar name **or** short instruction **may** be the Summary; do **not** force it into a declarative sentence. for RMED, summarize the Claim within its finalized Scope, **not** the Scope alone; do **not** substitute supporting Results **or** TLDR as the source.
    - for an existing Atom, retain the established Summary **and** check its faithfulness; **if** the Summary needs changing, use a new Atom identity under the Atom identity rule.
    - derive **every** Translation from the full corresponding source content, **not** the Summary.
- `CA-M-443@2`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-443@2`
  - Remaining Claim prose:
    **to** author an Atom, the Author **must** perform **all** of:
    
    1. identify one statement whose complete effect **must** be accepted, replaced, **and** retired together.
    2. check that one precise Summary covers the full contribution's meaning, **not** merely its theme. split distinct contributions when they require separate governance, including when that single Summary cannot cover them faithfully; do **not** create an Atom for **every** characteristic, qualification, list item **or** supporting nuance.
    3. resolve **`=1`** Claim Target Scope Unit independently of ownership. select the current Scope Unit **as** the default during authoring **or** select an explicitly permitted different target; carry the resolved value under the target Scope Unit carrier definition. express applicability **in** the registered body sections under the applicability carrier definition; for RMED, use Scope **and** write the Claim within that applicability; those restrictions alone do **not** make the Atom Relational.
    4. write the complete Claim **in** the current CCE version.
    5. remove **every** duplicate alternate authoritative statement.
- `CA-M-449@3`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-449@3`
  - Semantics:
    `undefined` denotes an omitted input value only; it does not add another supplied value to the admitted set. The literal string `"undefined"` is not Empty. A supplied null value and a supplied empty string `""` are Empty.
    
    Whitespace-only strings, `0`, `false`, `[]`, and `{}` are not Empty. Do not trim, coerce, or apply a general truthiness test to extend this exact set. This definition does not establish programming-language-specific `None` semantics.
  - Remaining Claim prose:
    Empty **means** an omitted input, null, **or** the empty string `""`. This Claim explicitly introduces the lexical Term instance named Empty at `Term//Empty`.
- `CA-M-450@3`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-450@3`
  - Remaining Claim prose:
    ID **means** a unique identifier used **to** find **`=1`** entity instance, whether Continuant **or** Occurrent, whose uniqueness is bounded **to** its matching prefix namespace. This Claim explicitly introduces the lexical Term instance named ID at `Term//ID`.
- `CA-M-451@3`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-451@3`
  - Semantics:
    The modeled Entity at Subject `Entity` is defined by an R / Entity Definition. The lexical instance `Term//Entity` is defined by this M / Term Definition. Entity is the sole exception outside the Term branch whose complete canonical name is also one registered Term, because it is the Subject root. Other entities outside that branch require their complete source-admitted expressions; a component Term alone is not their complete canonical name. The exception does not merge the modeled Entity and the lexical Term instance.
    
    The Term Entity is reusable in a name such as `Entity/Property` and in model statements. That lexical composition does not by itself establish specialization, containment, bearer dependence, or another entity identity. The applicable structural Definitions and Relations establish those facts.
  - Remaining Claim prose:
    Entity **means** the common category for every primary graph node and every dependent property in the framework, as structurally defined by CA-R-2462. This Claim explicitly introduces the lexical Term instance named Entity at `Term//Entity`.
- `CA-M-452@3`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-452@3`
  - Semantics:
    This Method governs the lexical word `Term`. The R / Entity Definition at
    `Term` governs the Term kind and its inherited structure. The matching
    word does not merge those distinct targets.
    
    Self-reference does not require an infinite sequence of lexical instances such
    as `Term Term`, `Term Term Term`, or further repetitions. This one explicit
    Method Atom of Type Term Definition governs `Term//Term`; using the word `Term` in this
    Claim or elsewhere does not introduce another instance.
    
    An Entity outside `Term` uses its full source-admitted expression as its
    complete canonical name. It cannot use one registered Term alone as that name,
    except for the Subject root `Entity`. The target of this Method is within the
    Term branch, so it is not an additional exception.
    
    `Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: X)/(.Type: X)` is a qualified expression that reuses the Term
    `X` in separately qualified value contexts. Each context still requires its
    own governing admission; repeated components neither introduce `X` nor
    transfer an admission.
  - Remaining Claim prose:
    Term **means** a reusable word **or** phrase component of complete **or**
    qualified entity names **and** authored content whose approved Project-specific
    meaning remains consistent across **all** its uses. This Claim explicitly
    introduces the lexical Term instance named Term at `Term//Term`.
- `CA-M-453@3`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-453@3`
  - Semantics:
    The Term names the entity kind `Entity/Property`; it is not that entity kind
    itself. `Property ((IS_PROPERTY_OF)) Bearer` states the direct Relation, and
    `Bearer.Property` is its bearer-to-Property dot display. HAS_PROPERTY is the
    strict derived inverse, not an independently stored reverse fact.
    
    A bearer may itself be a Property, so a qualified expression such as
    `bearer.property.status` remains permitted. This lexical meaning adds no generic lifecycle or update rule. The structural
    Property Definition governs the approved acyclicity constraint on
    IS_PROPERTY_OF, including self-loops. A Property is not another name for a YAML field; applicable
    Delivery rules determine its representation.
  - Remaining Claim prose:
    Property **means** an Entity whose identity depends on its immediate bearer and
    whose direct bearer Relation is IS_PROPERTY_OF from that Property to the
    bearer. This Claim explicitly introduces the lexical Term instance `Property`
    at `Term//Property`.
- `CA-M-454@3`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-454@3`
  - Semantics:
    A file, folder or database row can serve as a Carrier. The Term refers to the
    Entity instance, not its Carrier. An Entity retains its
    identity when referred to as an Artifact, including where more than one
    Carrier represents it. Artifact does not declare another Entity kind,
    classification axis, Property, or second identity.
    
    Entity admission remains governed by the pending Entity Definition; Carrier
    binding remains governed by CARRIES. This lexical Definition adds neither
    admission policy nor Carrier-binding policy.
  - Remaining Claim prose:
    Artifact **means** an Entity instance represented in a Carrier. This Claim
    explicitly introduces the lexical Term instance Artifact at
    `Term//Artifact`.
- `CA-M-455@3`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-455@3`
  - Semantics:
    The Term names this reusable four-member expression; it is not an Entity kind, a Content Role Property, a Selection Entity, or an Atom instance. Each named member remains an admitted Content Role value under its governing authority. Using CAPO in a Claim does not introduce another Term instance or assign a Content Role value to an Atom.
  - Remaining Claim prose:
    Change Content Roles (CAPO) **means** the set (Concern, Analysis, Plan, Operations) used **to** identify, investigate, organize, **and** perform governed Project work, including changes **to** specification **and** Implementation. This Claim explicitly introduces the lexical Term instance named Change Content Roles at `Term//Change Content Roles`.
- `CA-E-006@38`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-006@38`
  - Remaining Claim prose:
    **Claim checked.**
    
    the Framework Instance Settings Artifact **and** Project Settings Artifact accept exactly their registered values, resolve deterministically, **and** fail closed on invalid **or** unknown selections; Project Structure owns current unit declarations **and** explicit per-unit overrides **without** duplicating Settings selections **or** requiring a structural Projection.
    
    ### Applicable conditions
    
    1. resolve **and** load the exact current caprmedio_framework_settings Artifact **and** caprmedio_<project_name>_settings Artifact **and** the Default Settings Artifact; evaluate framework parameter resolution against `CA-E-450-CORE_META_MODEL-POLICY--validate-framework-parameter-fallback`.
    2. accept **only** enabled catalog Artifact Types, Atom Content Roles **and** their qualified Types, **and** Governance Origins.
    3. accept **only** `medium` **or** `high` artifact creation strictness.
    4. accept **only** `silent` **or** `verbose` interaction reporting. select **every** allowed value through Framework Instance Settings **and** confirm that the effective reporting default follows that selection **without** changing source Atoms, using Project Settings as reporting authority, **or** applying an independent Atom-fixed default.
    5. validate initialization inputs against Project Settings field authority **and** default **and** Project Authority Modes against Framework Instance Settings field authority, **and** explicit per-unit overrides against Project Structure field authority; do **not** hard-code this Project's selected values **in** the Evaluation.
    6. reject unknown keys **when** the governing schema marks their table closed.
    7. confirm a second parse produces identical effective settings **and** direct Project Structure resolution uses the same selected declaration bytes **and** consumed Settings revisions, including Default Settings **when** it supplies consumed values; deleting a legacy structural Projection does **not** change those results.
    
    ### Acceptance criteria
    
    **every** valid selection resolves deterministically **and** **every** invalid selection fails closed with the exact key **and** allowed values.
    
    ### Failure disposition
    
    record a Concern naming the accepted invalid value, rejected valid value, **or** non-deterministic result **and** stop settings-schema readiness.
- `CA-E-243@38`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-243@38`
  - Remaining Claim prose:
    a Demand is owned by its Consumer **and** constrains **only** one Producer result authorized by the Consumer's accepted Goal.
    
    ### Test case
    
    create valid Demand Atoms with Consumer **and** Producer Scope Unit references **in** permitted branches **and** with a later ordered sibling as Consumer **and** an earlier ordered sibling as Producer. **then** remove the Goal-authorized need for the Producer result, change ownership, target an ancestor, direct child, deeper descendant, **or** later ordered sibling, use equal Producer **and** Consumer Local Order, target two results, constrain Producer authority outside the selected result, fully define Producer Scope, **and** add a separate Demand-direction relation Kind.
    
    ### Acceptance criteria
    
    **only** fixtures with Consumer ownership, a permitted direction, one exact Goal-authorized need for the Producer result, one exact Implementation result, **and** no additional direction relation pass.
    
    ### Failure disposition
    
    record a Concern naming the invalid Demand fact.
- `CA-E-382@49`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-382@49`
  - Remaining Claim prose:
    The selected native Terms Graph Evaluation **must** preserve the following graph-validity, source-authority **and** Projection-fidelity boundaries.
    
    ### Graph validity
    
    the Evaluation **must** reject a Terms Graph **if** **any** of:
    
    - a native node is **not** a Term under its governing explicit authoritative Method Atom of Type Term Definition.
    - source evidence binds two distinct complete canonical entity names to the same entity **or** one complete canonical entity name to two distinct entities, including synonymous full names registered in different qualified contexts.
    - a native Relation Type has no defining source Claim under CA-R-1246, **or** an external reference violates its selected governing Entity Definition endpoint classes **or** graph contexts.
    - a NARROWER_THAN Relation lacks an explicit authoritative source declaration **or** its governing Term definitions do **not** establish the implication under CA-R-2475. absence of Entity instances does **not** establish this implication.
    - the NARROWER_THAN hierarchy **contains** a directed cycle, including a self-loop.
    - a Root Term classification differs from the **`=0`** direct NARROWER_THAN-parent criterion under CA-R-1347.
    
    the Evaluation **must** accept an acyclic hierarchy with multiple direct parents **or** an isolated Root Term **when** the remaining applicable authority is satisfied. A Relation Type's applicable Entity Definition constraints, when selected, **must not** change Root Term classification **when** the Terms Graph hierarchy is unchanged. the checks **must** distinguish an unknown Type from missing or unresolved governing constraint evidence without inventing a default or treating the known Type as unregistered.
    
    for a governed-only view under CA-R-1454, the Evaluation **must** reject graph validity **if** a displayed native Term node lacks **`=1`** active dedicated Term Definition under CA-R-1319. missing **or** conflicting definitions **and** uncertain Relation or constraint evidence **must** be reported with their affected source references **without** inventing a definition **or** an edge.
    
    filtering out a parent **must not** establish **or** change canonical Root Term classification. **if** the available source evidence is insufficient **to** establish the CA-R-1347 criterion, the classification **must** remain unresolved **without** silently importing source nodes **or** edges from outside the requested selection.
    
    the same NARROWER_THAN implication check applies **when** the Terms name Actions **or** Workflows. those operational Atoms already are Entities; the Evaluation **must not** require **or** create separate Entity identities for them **or** infer a Terms Graph edge merely from their classification. an empty set of observed instances does **not** prove a hierarchy Relation; acceptance requires the governing Term definitions **and** explicit Relation authority.
    
    ### Projection fidelity and source traceability
    
    an admitted source-Atom **or** cross-graph reference under CA-R-1472 **must not** fail **only** because its external endpoint is **not** a Term; that endpoint is **not** a native Terms Graph node. reject a view that imports that endpoint as a Term, erases its graph context, uses an unregistered Relation Type, **or** lets the external reference alter NARROWER_THAN hierarchy **or** Root Term classification.
    
    for a governed-only view under CA-R-1454, the Evaluation **must** reject the view **if** an eligible Term **or** Relation required by CA-R-1454 is omitted, an ineligible node **or** edge is displayed, a displayed native Term node's Term Definition Atom **or** a displayed internal edge's source declaration is outside the requested source selection, a displayed native Term node **or** internal edge lacks exact source Claim **and** Artifact Revision traceability, **or** an internal Term Relation edge is inferred **only** from spelling, capitalization, shared Subject use, **or** compatible endpoints.
    
    the Evaluation **must** reject a graph **or** governed-only view **if** its rendered content is treated as independent vocabulary authority, an upstream Projection substitutes for exact defining **or** Relation-source authority, a Projection chain loses its upstream identity **or** ultimate source traceability, **or** an arbitrary filter is treated as another admitted Projection Type. a source-faithful view derived through an upstream Terms Graph Projection **must** pass these Projection-specific checks **when** the applicable fidelity, selection **and** source-traceability requirements are satisfied; graph validity is assessed separately.
    
    ### Optional source-bound naming checks
    
    the Evaluation **must** check complete canonical entity name-to-entity **and** entity-to-complete-name uniqueness using exact source-backed identity evidence. Repeated references to one established full-name binding are **not** duplicate entities. A valid one-to-one complete-name mapping satisfies only the naming check; the existing hierarchy, authority **and** reference checks still apply. Unknown identity, incomplete required entity-population **or** naming-source coverage, **or** ambiguous target binding **must** remain unresolved, **not** be accepted through spelling, graph position **or** qualification alone. The view **must** preserve **and** expose conflicting bindings with their source Claims **and** Revisions; silently merging entities **or** accepting alternate full names as synonyms fails fidelity. A faithful display of a naming collision **may** pass fidelity while the source graph fails naming validity. A known entity with zero complete canonical entity names under complete evidenced coverage fails missing naming; absence of a required active Definition is a separate defining-authority failure. The Evaluation **must not** invent an entity distinction, equivalence, full name **or** Term to produce a pass.
    
    component Terms are reusable words **or** phrases whose meaning is owned by an explicit dedicated Method Atom of Type Term Definition, **not** inferred from agreement between Semantics sections. They are not complete Entity expressions outside the Term branch, except for the root `Entity`. Consistent use of the Term `Package` in `Entity/Object/Continuant/Package`, `Entity/Object/Continuant/Package/Eval Package`, and `Entity/Object/Continuant/Package/Runtime Package`, and of the Term `Unit` in `Entity/Object/Continuant/Structural Unit/Scope Unit` and `Entity/Object/Continuant/Package <+ Module <+ Code Unit`, passes the component-meaning check. A different complete expression identifies each separately defined entity. Conflicting component meanings fail; unknown component meaning **or** segmentation remains unresolved. No Unit entity **or** synthetic Term node is created merely by splitting an entity's name.
    
    the complete-name check covers **every** named canonical Subject-graph entity: full expressions in admitted `/`, `//`, `.`, `:`, `+>`, `<+`, `>|` **and** `|<` constructs, calls `@(...)` to already declared Entities, plus registered direct Relation tokens inside `((...))`. The reference marker refers to an already declared Entity **without** declaring another target; parsing alone admits no target or Relation. A registered Relation token resolves to one admitted Relation Type under the registered notation, but its bare spelling is not that entity's complete canonical expression; complete-name comparison uses the full qualified expression separately. `Entity/Object/Continuant/Package`, `Entity/Object/Continuant/Package <+ Module`, and `Entity/Object/Continuant/Package <+ Module <+ Code Unit` connect three entities with three full expressions; a component label, the operators, or the chain must not be introduced as another entity node. Operators, delimiters **and** selector syntax are not Terms. Under CA-R-1325, a complete composite Subject Expression is not one lexical Term; parsing arbitrary composite syntax does not automatically establish a complete entity expression or another entity. An Atom expression with independently admitted Content Role and Type values remains valid only with its full admitted canonical prefix. The contextual topic/code spellings `atom.id` and `projection.id` distinguish their respective ID Properties; they are not alternative complete canonical Subject names. Authored Subjects use their full admitted expressions. The three-target chain introduces no fourth entity or fourth complete expression. Check **all** authored mentions against those full-expression bindings: `component` used as a stylistic substitute for the same Module fails naming, while a separately defined Component entity remains distinct. Repeated references to the same entity are not collisions; distinct property, value or bearer-qualified entities using the same complete expression are collisions despite their context. A Relation token must not become an admitted Relation without its governing authority and endpoint permissions. Preserve existing separation of source naming, native Terms Graph membership and Projection fidelity.
    
    ### Result boundary
    
    the Evaluation **must** distinguish Projection fidelity from graph validity **and** keep the two outcomes visible, including **any** unresolved source conditions **and** checked-coverage limits. a graph that faithfully represents a source conflict **may** pass fidelity while failing an applicable graph-validity condition **or** leaving that condition unresolved. a composite acceptance result **must not** pass **if** an applicable check fails **or** remains unresolved; faithful reproduction alone does **not** establish a valid source model.
    
    connectivity **and** cycle checks apply **only** as required by the governing graph authority; the NARROWER_THAN cycle prohibition **and** the admitted isolated Root Term cases above remain distinct. passing graph-structure checks does **not** establish Project-specific meaning **or** consistency of source use **without** the required governing definitions **and** source context.
- `CA-E-383@41`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-383@41`
  - Remaining Claim prose:
    Under A1296, count an omitted property as zero values, a scalar null as one value, and an empty string as one value. Check the parsed value against the declared Format and applicable prose conditions separately. Do not pass a required string merely because a null satisfies the count; do not reject an empty string solely because it is empty unless the applicable rules require substantive/nonempty content.
    
    For the Entity format check under CA-A-1285, check string-valued content and the admitted notation. Do not fail that format check solely because a defining Atom introduces a new governed entity. Target authority and explicit existing-kind reference resolution are separate semantic checks, not consequences of the string Format.
    
    Under CA-A-1283, admit subjects{0} with one governs reference and zero or more dependencies; reject a direct subjects scalar without rejecting its declared children. Require direct prose for claim{1} even when formal_claim{0..1} is present. For property[string]{2}, require two string values under one key; repeated sibling YAML keys do not satisfy cardinality. Do not treat a sequence as one list-formatted value or count child keys as direct parent values.
    
    Accept Package/Project Implementation as the parentless root Package and each Module only when it belongs to exactly one Package; reject the superseded root-under-Implementation and independent-Module cases.
    
    For cardinality under CA-A-1280, accept `{0}`, `{1}`, `{3}`, `{0+}`, `{1+}`, `{2+}`, `{0..1}` and `{2..5}` with their declared counts. Reject negative or fractional bounds, an empty `{}`, a missing range bound such as `{2..}`, repeated plus signs such as `{1++}`, and an inverted range such as `{5..2}`. A Step count of zero fails `Step {1}+>{1+} Workflow`; zero Substeps is admitted by `Sub-step {1}+>{0+} Step`. A containment count must not be read as inheritance or as changing the exactly-one immediate-whole rule.
    
    the Evaluation **must** reject an Entity Expression **if**
    
    - `/` does **not** express the approved broader-to-narrower Entity Path profile,
    - `//` does **not** occur exactly between an Entity kind component and a following named instance component, or the entire path fails to resolve to exactly one canonical Entity Target that already exists or is explicitly introduced by applicable defining authority under CA-R-1194 and CA-R-1321,
    - `.` does **not** encode **`=1`** valid bearer edge from the following Property occurrence **to** the immediately preceding bearer occurrence,
    - `:` does **not** express an admitted allowed value of its preceding X under CA-R-1436-CORE_META_MODEL--define-is-allowed-value-of,
    - `.Type` is interpreted as a primary Entity **or** as a Property subtype of Atom instead of as a Property relative to Atom,
    - `Atom/(.Type: Method)` is used as syntax-only evidence that Method is admitted as a Type,
    - superseded bare `X/Y: Z` qualification spelling is used in this proposal,
    - `>|` or `|<` is interpreted as membership through IS_CLASSIFIED_BY instead of the HAS_CLASSIFICATION axis,
    - `*` ranges beyond admitted Atom Status values in a Status classification,
    - `+>` and `<+` are interpreted as different containment facts, their direction is swapped, **or** either is used as inheritance,
    - Current fails to exclude Draft and Archived within the admitted Atom Status values,
    - a Relation count is interpreted as only an outgoing count despite its two slots, a post-operator slot is treated as outgoing rather than reverse, **or** equivalent forward and reverse writings are given different constraints,
    - allowed-value admission is treated as assignment **to** a particular Property occurrence **or** as determining its cardinality,
    - a Property occurrence lacks **`=1`** immediate bearer,
    - a reusable Term is rejected **only** for changing ordinal position,
    - a Governed Term begins with a lowercase letter,
    - an ordinary named component other than the RHS instance name following `//` fails **to** resolve **to** a Term under CA-R-1321-CORE_META_MODEL--define-subject-expression, **or** an `atom(...)` component is **not** one of that Requirement's registered exact initial selector forms,
    - an ordinary General Term is substituted for a required Term reference,
    - a name uses an unescaped reserved operator character as literal text, or has an unmatched final backslash,
    - a structural containment edge through `+>` or `<+` is used as an inheritance route,
    - an `@` call is used without resolving to its intended already declared Entity,
    - a complete composite Entity Expression is classified as one Term,
    - **or** a registered CCE Operator is redefined as a Governed Term **or** Scope Unit Name.
    
    For example, in `Kind//Instance Name`, the RHS identifies the named instance and is not automatically a Term; require the complete path to resolve to exactly one canonical target that already exists or is explicitly introduced by applicable defining authority. This does not relax the already-declared target requirement for `@`. Recognizing `//` alone does not establish or admit an INSTANCE_OF graph fact. Do not reject or accept the name by an Atom-ID pattern; its source/name authority and exact-target resolution govern.
- `CA-E-387@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-387@27`
  - Remaining Claim prose:
    the Evaluation **must** reject a Type assignment **if** **any** of the following holds:
    
    - an Entity occurrence that bears Type has **`!=1`** direct Type values.
    - the selected value is **not** allowed by its most-specific applicable qualified Type Subject.
    - qualified Type Subjects create **`>1`** Type Property slots for the occurrence.
    
    absence of a Type value **in** an Entity occurrence that does **not** bear Type is **not** a cardinality failure under this Evaluation.
- `CA-E-405@29`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-405@29`
  - Remaining Claim prose:
    the Evaluation **must** reject a Canonical Signature derivation **if** any of the following is true:
    
    - it rewrites one source Claim.
    - it treats one Canonical Signature as authority.
    - it accepts mixed **and** **or** groups.
    - it rewrites negation, implication, **where**, **without**, temporal condition, quantifier, extension-defined CCE Operator, **or** unparseable prose.
    - it fails **to** flatten nested same-operator groups.
    - it retains duplicate atomic predicates.
    - it yields different Canonical Signatures from Boolean groups that differ **only** by operand order.
- `CA-E-407@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-407@28`
  - Remaining Claim prose:
    the Evaluation **must** reject a Canonical Scope Signature derivation **if** **any** of the following holds:
    
    - it rewrites one source Carrier.
    - it treats one Signature as authority **or** Claim equivalence.
    - it accepts mixed **and** **or** groups, **without**, **where**, **all**, **any** other CCE Operator, function, Entity-kind selector, descendant **or** dynamic selector, unresolved identity, changing source frontier, **or** unparseable prose.
    - it fails **to** flatten nested same-operator groups, retains duplicate exact Atom IDs, loses the distinction between **and** **and** **or**, **or** yields different Signatures from same-operator groups that differ **only** by operand order.
- `CA-E-440@34`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-440@34`
  - Remaining Claim prose:
    the governing-Atom change Evaluation **must** return `fail` **if** an Operator-authored Atom changes **without** Operator approval, an AI-authored Atom changes autonomously below the Plan confidence threshold, a permission **or** additional Operator constraint is bypassed, the Author is changed **before** resolving the approval requirement, **or** an omitted **or** unresolved Author is assumed **to** be an AI Agent. it **must** also return `fail` **if** an authorized RMED change is reported against the old unchanged baseline **or** its affected work **and** Evaluations are **not** resolved again. AI authorship **and** sufficient confidence **must not** override an explicit prohibition.
- `CA-E-443@32`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-443@32`
  - Remaining Claim prose:
    the confidence-threshold Evaluation **must** preserve CA-M-271-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-confidence-thresholds-by-source-precedence precedence **and** CA-R-1591-CORE_META_MODEL-RULE--apply-autonomous-confidence-thresholds-to-plan-execution authorization gates.
    
    - supply distinct valid values through Operator input, a Plan, nested Hubs, **and** Framework Instance Settings; omit sources successively **and** confirm nearest explicit source selection.
    - scope direct input **to** one execution; retain the unrelated execution's setting.
    - omit the inner Hub's optional confidence override while retaining its mandatory file **and** a retry override: inherit confidence **without** copying it. reject a missing mandatory file.
    - supply a Hub file with explicit values: require the same Atom identity as its folder **and** its DoD; reject a separate Objective, `epic_overrides`, **or** a nearby unrelated file as an inherited source.
    - use a current Plan Revision **without** taking values from its Archived copies; reject an ambiguous Bundle **or** invalid reached source **without** silent fallback.
    - preserve an explicit override equal **to** the inherited value **after** the upstream source changes; an omitted override follows that change.
    - accept permitted integer values including **`=0`**, **`=87`**, **`=99`**, **and** **`=100`**; reject out-of-range, non-integer, missing effective, **or** ambiguous values.
    - confidence below the effective value requests Operator disposition; equal **or** greater confidence grants no additional authority.
    
    report the selected source, context, expected value, **and** failed condition **without** mutating source values.
- `CA-E-446@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-446@28`
  - Remaining Claim prose:
    settings resolve through their own Project paths **without** cross-Project fallback. Project Settings remain authoritative initialization inputs; Framework Instance Settings remain authoritative instance choices. foundational settings authority defines purpose, content, **and** authority boundaries, shared settings specifications are independently governable **when** needed, **and** concrete settings specifications define concrete sections **or** fields. the declared unit remains visible with missing Carrier **and** Active Goal findings; the undeclared candidate remains an observation **without** becoming a declaration. explicit unit Authority Mode overrides resolve from Project Structure; omitted values inherit Framework Instance Settings. no structural Projection is required. no Projection edit changes Settings, Project Structure, **or** source Atoms. an unresolved authority-backed value does **not** conceal observed structure.
    
    **every** Framework Instance's Methodology Sources **and** Applicable Methodology output **must** resolve beneath its own Project's `000_CAPRMEDIO_framework/` directory. rebuilding one Project's Applicable Methodology **must not** read, replace, **or** modify another Project's sources, settings, **or** compiled results. a missing selected Project instance **must** be reported rather than resolved through another Project **or** the former repository-shared framework root. nesting the framework directory **must not** change source Atom identity **or** make a projected copy a second authoritative Atom.
- `CA-E-449@42`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-449@42`
  - Remaining Claim prose:
    the Evaluation **must** reject an Entities Graph **if** **any** of:
    
    - a node is **not** an Entity under its governing authority, **or** a separate Entity identity is invented for an existing Action **or** Workflow Atom.
    - a selected view includes a node **or** source Relation that fails its declared source selection **or** fails its declared display selection, omits an eligible node **or** source Relation under CA-R-1456-CORE_META_MODEL-GENERAL-REQUIREMENT--derive-entities-views-from-selected-authority, **or** silently imports outside authority **to** complete the view.
    - a displayed node **or** edge lacks its exact governing source Claim **or** Artifact Revision for Entity **or** Relation admission, **or** a represented observed structural **or** recorded historical fact lacks its appropriate Scope Unit **or** Journal source under CA-R-2535-CORE_META_MODEL-CORE-REQUIREMENT--define-projection-artifact-form; derived inverse navigation lacks traceability **to** the original source Relation.
    - display membership, repeated appearance, a reusable Term, **or** a shortened path substitutes for the existing canonical Entity identity **or** complete bearer-qualified Subject Path.
    - multiple governing Atoms are treated as multiple identities for one Entity, **or** the at-most-one GOVERNS target per Atom is treated as permitting **only** one governing Atom per Entity.
    - a tree display is treated as the full combined graph **without** satisfying its declared selection, **or** legitimate sharing is rejected, duplicated, **or** discarded **to** force a tree.
    - a Relation Type is unknown under CA-R-1246-CORE_META_MODEL-RULE--keep-relation-vocabularies-graph-specific.
    - an IS_PROPERTY_OF Relation has an invalid endpoint **or** direction under the pending [IS_PROPERTY_OF Relation Definition](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-is-property-of.md), **or** violates the applicable immediate-bearer cardinality under the pending [Property kind and Formal Constraint](../../04_requirement/draft/CA-R-1193@23-draft-CORE_META_MODEL-DEFINITION--define-property.md) **or** CA-R-1351-CORE_META_MODEL-CORE-REQUIREMENT--give-primary-entity-occurrences-no-bearer.
    - the direct IS_PROPERTY_OF Relations contain a directed cycle, including a self-loop, under the [pending Property Definition](../../04_requirement/draft/CA-R-1193@23-draft-CORE_META_MODEL-DEFINITION--define-property.md).
    - an IS_ALLOWED_VALUE_OF Relation admits a value **without** governing authority for its qualified target Entity context under CA-R-1436-CORE_META_MODEL-CORE-REQUIREMENT--define-is-allowed-value-of.
    - admission **in** one target Entity context is used **to** justify admission **in** another context **without** its applicable authority.
    - allowed-value admission is treated as assigning a value **to** a particular occurrence **or** determining direct-value cardinality.
    - HAS_PROPERTY is independently authored as another primitive Relation Type instead of being derived from IS_PROPERTY_OF under the pending [HAS_PROPERTY Relation Definition](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-has-property.md).
    
    the Evaluation **must not** reject the reuse of one Term as an allowed-value name **in** multiple qualified target Entity contexts **when** the value is separately admitted **in** **every** such context. the checks **must** cover valid **and** invalid bearer endpoints, applicable bearer cardinalities, independent value admission across target Entity contexts, derived inverse navigation, **and** a Relation Type used under another governing constraint context.
    
    native endpoint **and** cardinality checks use the cited governing source facts; a filtered view does **not** establish absence of a bearer, change a qualified identity, **or** alter allowed-value admission. **if** selected evidence cannot establish an applicable source constraint, the Evaluation **must** retain the source-backed limitation as unresolved **without** inventing an edge **or** silently enlarging selection. a truthful limited view does **not** prove that the unexamined source model passes its checks.
    
    the checks **must** also cover exact selected-source node **and** edge provenance, eligible omissions **and** outside-selection additions, repeated appearances of one identity, distinct qualified occurrences sharing a reusable Term, multiple governing Atoms for one Entity, Action **and** Workflow Atoms admitted under their existing Atom identities **when** selected, rejection of duplicate identities **and** type-only exclusion, a legitimate shared value admitted independently **in** two target Entity contexts, **and** explicit hierarchy filtering **without** a universal-tree assumption.
    
    the Evaluation **must** reject a graph **or** filtered view **if**
    
    - its rendered content is treated as independent model authority,
    - a graph specification is used **to** grant source authority **to** its derived contents,
    - an upstream Projection substitutes for the appropriate source facts,
    - an observed Carrier **or** Journal occurrence is used **to** admit an Entity identity, define a Term, **or** admit a Relation Type **without** the required governing source Claims,
    - a Projection chain loses upstream identity **or** ultimate source traceability,
    - **or** an arbitrary display filter is treated as another admitted Projection Type.
    
    a source-faithful view derived through an upstream Entities Graph Projection **must** pass these Projection-specific checks **when** the remaining applicable source, display-selection **and** graph constraints pass.
- `CA-E-458@35`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-458@35`
  - Remaining Claim prose:
    the Evaluation **must** reject Framework Instance Settings **if**
    
    - it is treated as an Atom **or** Projection,
    - has an Atom ID **or** Atom Content Role,
    - resolves outside the current Project's registered instance directory,
    - uses another Project's Settings Carrier,
    - has other than **`=1`** authoritative TOML Carrier,
    - **contains** Project initialization inputs **or** independently editable Project Structure,
    - violates its foundational content boundary, applicable shared settings specifications, **or** applicable concrete field specifications **after** parameter resolution governed by CA-M-279,
    - **or** lacks an exact current Revision, SHA-256 Digest, **and** Work Journal receipt admitted by CA-D-360.
- `CA-E-460@34`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-460@34`
  - Remaining Claim prose:
    **Claim checked.**
    
    ownership **and** Claim targeting produce their respective direct **and** recursive Atom sets, **and** the alias `spec` selects **only** Active RMED Subtree-targeting Atoms.
- `CA-E-466@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-466@28`
  - Remaining Claim prose:
    the Evaluation **must** distinguish authoritative source facts from their secondary graph representations **and** reject a Projection that acquires independent authority for a represented fact.
    
    ### Test cases
    
    | Case | Expected result |
    |---|---|
    | **`=1`** source Claim represented **in** multiple graphs | pass **if** **all** representations retain the same source identity **and** applicable Revision |
    | two independently maintained authoritative declarations for the same fact **in** the same context, even **when** their values agree | fail |
    | different Claims **or** different source facts used by a derived result | no Single Source of Truth failure merely because there are multiple source Atoms |
    | a permitted derived Relation with identified derivation authority **and** source inputs, but no separately authored declaration for its computed result | pass this source-authority check |
    | a derived edge with no admitted derivation authority **or** missing required source evidence | fail **or** report unresolved evidence; do **not** invent a source declaration |
    | a source Atom reached through another Projection | pass **if** ultimate source traceability is retained |
    | a Journal event **or** structural fact represented **in** a graph | pass **if** its existing source authority remains intact; do **not** fabricate an Atom Claim as historical **or** observed evidence |
    | a projected fact corrected independently while its source **and** governing derivation remain unchanged | fail |
    
    passing this source-authority Evaluation does **not** establish graph-specific Relation validity, completeness, **or** the truth of a recorded outcome; those remain subject **to** their applicable Evaluations.
- `CA-E-469@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-469@27`
  - Remaining Claim prose:
    the Evaluation **must** reject Project Structure **if**
    
    - its registered Carrier schema is invalid,
    - a Scope Unit Name is duplicated **or** invalid,
    - a parent is unresolved **or** self-referential,
    - parentage **contains** a cycle,
    - a parent refers **to** another Project,
      - a retained ancestry/path representation disagrees with the declared parent chain,
    - **or** a declaration assigns an invalid Type, Label, order, navigation value, Authority Mode, **or** Carrier binding.
    
    - Ordered siblings **must not** share structural Local Order; Navigational Order Number duplicates alone **must not** fail validation.
    - an Unordered unit **must not** carry structural Local Order.
    - Label **must not** determine Type.
    - retained readable fields **must** agree with governing source fields **and** admitted Carrier exceptions.
    - lexical **and** resolved-path collisions, traversal outside the authorized repository boundary, **and** ambiguous unit lookup **must** fail.
    - the Evaluation **must** test a valid declaration **and** a falsifying example for **every** applicable condition, with explicit failures for unknown fields **or** unsupported schema versions.
- `CA-E-470@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-470@24`
  - Remaining Claim prose:
    the Evaluation **must** fail **if** a consumer requires a structural Projection, promotes an observed folder **or** Goal into a declaration, conceals a declared unit because its Carrier **or** Active Goal is absent, treats a Draft **or** archived Goal as Active coverage, **or** repairs contradictory sources **without** authorization. test declared-and-materialized, declared-but-unmaterialized, undeclared folder candidate, missing Active Goal, mismatched Carrier Name, logical-parent/physical-parent exception, **and** retired structural Projection cases. findings **must** retain their category **and** exact source evidence; an undeclared candidate **or** Goal coverage gap alone **must not** erase a declaration **or** authorize a mutation.
- `CA-E-481@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-481@22`
  - Remaining Claim prose:
    the Evaluation of the active normative-authority subgraph **must** fail **when** **any** declared authority-bearing direct edge lacks its registered typing **or** the directed subgraph **contains** a cycle under CA-R-833.
- `CA-E-486@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-486@21`
  - Remaining Claim prose:
    the Evaluation **must** check Workflow Steps **and** Runs.
- `CA-E-489@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-489@21`
  - Remaining Claim prose:
    the Evaluation **must** check whether a Workflow's declared execution **and** handoff behavior is well formed under CA-R-1519 **and** CA-R-1520, independently of current executor availability.
- `CA-E-490@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-490@21`
  - Remaining Claim prose:
    the Evaluation **must** check that a status-change Workflow follows the target Entity's applicable model under CA-R-1521.
- `CA-E-494@20`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-494@20`
  - Remaining Claim prose:
    the Evaluation **must** check a Workflow Run's declared definition bindings **and** revalidation evidence under CA-R-1525.
- `CA-E-495@19`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-495@19`
  - Remaining Claim prose:
    the Evaluation **must** check that Action Execution Kind **and** Agentic Step Execution Context remain distinct **and** support reuse **without** duplicate definitions.
- `CA-E-497@20`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-497@20`
  - Remaining Claim prose:
    the Evaluation **must** check that an Agentic Step invocation can be understood **and** resumed from its supplied context **without** remembered Workflow procedure.
- `CA-E-500@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-500@24`
  - Remaining Claim prose:
    the Workflow representation Evaluation **must** reject a Carrier arrangement that duplicates definition authority **or** derives execution order from storage order.
- `CA-E-501@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-501@28`
  - Remaining Claim prose:
    the Plan authoring Evaluation **must** reject **any** Plan that violates the common model.
- `CA-E-505@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-505@21`
  - Remaining Claim prose:
    the Label Evaluation **must** reject a qualified use of Label that changes the shared meaning under CA-R-2497.
- `CA-E-511@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-511@23`
  - Remaining Claim prose:
    **Claim checked.**
    
    **every** Atom resolves **`=1`** GOVERNS Subject and zero **or** one Claim Target Scope Unit; applicable Goal and Demand rules, including the Operator-owned Project Goal, retain their required target conditions. Claim Scope remains applicability restrictions **in** the body sections registered by CA-D-495, including Claim scope for RMED, **not** another structural target **or** frontmatter Property.
- `CA-E-621@35`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-621@35`
  - Remaining Claim prose:
    an Operator unfamiliar with the repository can configure framework-instance behavior, including default **and** Project Authority Modes, through Framework Instance Settings **and** Project initialization inputs through Project Settings using the owning Settings Artifacts **and** their in-file documentation, while recognizing authoritative Project Structure as the separate owner of Scope Unit declarations **and** explicit per-unit Authority Mode overrides. no structural Projection is required **to** make these choices.
- `CA-E-624@36`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-624@36`
  - Remaining Claim prose:
    generated-only provenance validation **must not** pass **if** an update **only** **to** generated Projections contributes an Implementation Relation **or** a generated Projection cites itself as its semantic input. the same boundary applies with **or** **without** a version-control integration.
- `CA-E-657@8`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-657@8`
  - Remaining Claim prose:
    the Evaluation **must** reject an Artifact **if** **any** applicable condition holds:
    
    - **when** an explicitly defined Status model applies, its Status domain is resolved outside its complete qualified Type **or** Atom Content Role **and** Type path, its current Status cardinality **`!=1`**, its current Status is **not** an allowed value of that domain, a prior transition coexists as current Status metadata, **or** a second disposition axis duplicates Status.
    
    **when** no explicitly defined Status model applies, absence of a Status is **not** a rejection.
    
    the Evaluation **must not** substitute Active **or** Inactive for a missing, invalid, **or** ambiguous Status. an Artifact outside the applicable qualified Status model **must not** fail merely because it has no Status.
- `CA-E-658@9`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-658@9`
  - Remaining Claim prose:
    the classification Evaluation **must** fail **if** an Atom's Content Role does **not** match its actual contribution under the Specification **and** Change definitions.
    
    - use the evaluated Atom's declared Content Role, complete Main Content, **and** applicable Specification **and** Change definitions as the input evidence.
    - compare the declared Content Role with the contribution expressed **in** that Main Content, using the following classification table.
    - report unresolved **when** required evidence is unavailable, unresolved, **or** contradictory; **otherwise**, report pass **if** the declared Content Role matches the observed contribution **and** fail **if** it does **not**.
    - identify the evaluated Atom **and** report the declared Content Role, relevant content excerpt, applicable definition, **and** comparison result.
    
    | Claim contribution | Expected classification |
    |---|---|
    | a model definition, required property, permission, **or** Actor participation/authorization policy governing a Concern, Analysis, Task, Action, **or** Workflow | Requirement |
    | a convention for authoring **or** constructing that content | Method |
    | a falsifiable correctness check | Evaluation |
    | a Carrier's fields, format, **or** placement | Delivery |
    | a particular unresolved issue, analytical finding, **or** intended Task | the matching Concern, Analysis, **or** Plan role |
    | a particular reusable Action behavior, Workflow graph, **or** Step invocation binding | Operations |
    
    
    reusing the specified content's role as the specification's role **must** fail this check. a long-lived Concern **or** reusable Workflow **must not** fail merely because its lifetime is long.
- `CA-E-659@3`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-659@3`
  - Remaining Claim prose:
    a Term Definition passes well-formedness **only** **when** it is explicitly classified as a Method Atom of Type Term Definition, identifies **`=1`** reusable word **or** phrase as its Term, carries **`=1`** independently replaceable Claim that establishes that Term's meaning within its stated Scope, **and** satisfies the applicable metadata, Subject-binding **and** body-layout rules. An Entity Definition, recurring descriptive wording **or** agreement among Semantics sections **must not** substitute for this dedicated Method Type. Missing **or** unresolved required evidence **must** remain visible **and** **must not** pass; local well-formedness alone **does not** establish unique defining authority **or** consistency of other authored sources.
- `CA-E-661@2`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-661@2`
  - Remaining Claim prose:
    a Tier 0 Atom’s Content Role classification **must** fail this Evaluation **if** its complete Claim's primary contribution does **not** match the applicable Content Role definition.
    
    Numeric Tier `0` is a local Scope Unit foundation and its readable Tier Label is Scope Contract; that label alone does not change an Atom’s Content Role or Type. Its complete primary contribution must satisfy its own Content Role definition. Operations retains its existing Action, Workflow and Step Types where applicable. This Evaluation introduces no Content-Role or Type-to-Tier restriction and does not require all Content Roles in a unit.
- `CA-D-291@31`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-291@31`
  - Remaining Claim prose:
    **every** Project-owned Atom filename **must** serialize the Scope Unit that **contains** its authoritative Carrier **`=1`** time **and** **must** omit that segment **if** the Carrier is **in** the Project Scope Unit.
- `CA-D-292@34`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-292@34`
  - Remaining Claim prose:
    **every** external Project Goal filename **must** begin with the unqualified canonical Atom ID prefix `<CANONICAL_ATOM_ID>-` for a Current Project Goal or the once-qualified canonical Atom ID prefix `<CANONICAL_ATOM_ID>@<VERSION>-` for an Archived Project Goal, followed by `<OPERATOR_NAMES>-DEFINES_GOAL_FOR-<PROJECT_SCOPE>--<SUMMARY_SLUG>.<EXT>`.
    
    The `<OPERATOR_NAMES>` filename token **must** identify the registered Operator; `<PROJECT_SCOPE>` **must** preserve the exact registered Project Settings Name. The canonical current ID or once-qualified archived ID is the identity prefix; no additional Project Prefix, Content Role letter or unrelated number may be inserted into the preserved segment.
    
    ### Current source pin
    
    Proposed N+1 successor of `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/CA-D-292-CORE_META_MODEL-ENG_DECISION--serialize-external-project-goal-filenames.md`, CA-D-292@32, SHA-256 `244cc4f2eca9145cf1e314263f31c9e1cc3d4031a0059f1204d5de1f098c00ed`. Current bytes remain unchanged; this Draft performs no promotion or filename migration.
- `CA-D-329@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-329@26`
  - Remaining Claim prose:
    **every** proof Carrier **must** serialize its machine-readable dependency frontier as a YAML `proof_frontier_refs` list of exact versioned **or** digest-bound references. prose **must** be reserved for additional invalidation conditions that cannot be encoded **without** loss.
- `CA-D-333@32`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-333@32`
  - Remaining Claim prose:
    **if** a Project Scope Unit Graph Projection is retained for compatibility, its Carrier **must** serialize Updated At, generator identity **and** digest, exact consumed Project Structure **and** Settings source states, **and** the source bindings **and** distinct Directory Carrier observations needed **to** explain emitted values **and** unresolved findings. this compatibility format does **not** require production **or** refresh of a separate structural Projection.
- `CA-D-342@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-342@28`
  - Remaining Claim prose:
    **every** Reference **to** a Current external Project Goal Atom **must** use its canonical Current Atom ID, not its current Carrier filename stem.
    
    A Reference **to** an Archived external Project Goal Atom **must** use its canonical Atom ID qualified once with its unchanged numeric Version when historical identity is required. A Current Project Goal reference **must not** omit the canonical ID or fall back to a filename stem; this Delivery creates no ID-less Current exception.
- `CA-D-346@32`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-346@32`
  - Remaining Claim prose:
    **every** Canonical Signature Projection **must** be delivered as **`=1`** non-authoritative report under its Project's `.caprmedio_<project_name>/_projection/` Directory Carrier with the selected source frontier digest, **every** source Atom Identity **and** Revision, **every** source expression occurrence, **every** Canonical Signature, **and** **every** exclusion diagnostic; the Projection **must not** become an Atom Carrier, modify a selected source Carrier, **or** establish Claim equivalence.
- `CA-D-347@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-347@27`
  - Remaining Claim prose:
    **every** Canonical Scope Signature Projection **must** be delivered as **`=1`** non-authoritative JSON report under its Project's `.caprmedio_<project_name>/_projection/` Directory Carrier with the selected source frontier digest, **every** source Atom identity **and** revision, source Carrier digest, source Scope Expression occurrence, Canonical Scope Signature, **and** exclusion diagnostic; the Projection **must not** become an Atom Carrier, modify a selected source Carrier, establish Claim equivalence, **or** create a dependency relation.
- `CA-D-359@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-359@28`
  - Remaining Claim prose:
    the Framework Instance Settings Artifact for a Project named `<project_name>` **must** use `.caprmedio_<project_name>/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml` as its **`=1`** authoritative TOML File Carrier.
- `CA-D-360@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-360@27`
  - Remaining Claim prose:
    the current caprmedio_framework_settings Revision **and** SHA-256 Digest **must** bind **to** its authoritative TOML Carrier through a canonical completed governed-change Work Journal receipt **or** an explicitly authorized canonical recovered-state Work Journal receipt registering its observed baseline; the receipt **must** match the selected Project, exact Carrier path, logical Artifact Revision, **and** Digest. absence, ambiguity, **or** mismatch **must** leave its currentness unknown.
- `CA-D-361@30`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-361@30`
  - Remaining Claim prose:
    the Framework Instance Settings TOML Carrier **must** encode explicit Operator-selected instance choices through sections **and** fields specified by concrete settings-specification Atoms under its foundational content **and** authority boundaries **and** applicable shared settings specifications; it **must not** store Project initialization inputs **or** authoritative Project Structure declarations **or** derived structural values as independently editable settings.
- `CA-D-362@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-362@26`
  - Remaining Claim prose:
    the Identifier of Project Settings for a Project named `<project_name>` **must** be `caprmedio_<project_name>_settings`.
- `CA-D-368@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-368@27`
  - Remaining Claim prose:
    an explicit necessary-information confidence default **in** the Framework Instance Settings TOML Carrier **must** use the integer-percentage field `confidence.necessary_information_threshold_percent`.
- `CA-D-369@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-369@26`
  - Remaining Claim prose:
    an explicit semantic-resolution confidence default **in** the Framework Instance Settings TOML Carrier **must** use the integer-percentage field `confidence.semantic_resolution_threshold_percent`.
- `CA-D-372@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-372@25`
  - Remaining Claim prose:
    the Framework Instance Settings TOML Carrier **must** encode selected active **and** background Tools with their per-Tool settings.
- `CA-D-373@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-373@25`
  - Remaining Claim prose:
    the Framework Instance Settings TOML Carrier **must** encode enabled **or** disabled Extensions with selected revisions **when** applicable **and** retained per-Extension settings; retained settings **must not** activate a disabled Extension.
- `CA-D-374@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-374@24`
  - Remaining Claim prose:
    an explicit Authority Mode selection **in** the Framework Instance Settings TOML Carrier **must** use `authority_modes.default` for the instance default **or** `authority_modes.project` for the Project override. explicit per-unit overrides **must** use **only** that unit's `authority_mode` **in** authoritative Project Structure; legacy per-unit Settings fields **must not** remain a second selectable source.
- `CA-D-376@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-376@26`
  - Remaining Claim prose:
    the Project Settings TOML Carrier **must** encode the Operator-selected Atom prefix as its exact nonempty uppercase TOML string value under CA-D-378 **in** `artifacts.identity.project_prefix` **before** the first Project Atom is created.
- `CA-D-380@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-380@21`
  - Remaining Claim prose:
    **every** Carrier rendering of a Navigational Order Number **must** use decimal digits. the default directory-name rendering of a non-Project Scope Unit **must** use **`>=2`** digits; a typed TOML integer stores the numeric value **without** leading-zero padding.
- `CA-D-383@31`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-383@31`
  - Remaining Claim prose:
    an explicit instance reporting default **in** the Framework Instance Settings TOML Carrier **must** use `reporting_mode` **in** the `[interaction]` section, using an allowed value governed by CA-R-1628-CORE_META_MODEL-RULE--allow-silent-and-verbose-reporting-modes.
- `CA-D-387@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-387@27`
  - Remaining Claim prose:
    an explicit atomic admission strictness selection **in** the Framework Instance Settings TOML Carrier **must** use `creation_strictness` **in** `[artifacts]`, using the allowed values governed by CA-R-1630.
- `CA-D-389@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-389@24`
  - Remaining Claim prose:
    an Analysis Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:
    
    - Rationale: `RATIONALE`.
    - External Analysis Report: `EXTERNAL_ANALYSIS_REPORT`.
    
    these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.
- `CA-D-391@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-391@23`
  - Remaining Claim prose:
    **if** a Project Scope Unit Graph Projection is retained for compatibility, its `authority_mode` **must** be a derived effective value: an explicit unit override from Project Structure, **otherwise** the applicable Framework Instance Settings selection. it **must not** select **or** own that mode, become a required input **to** a direct Project Structure consumer, **or** require creation of a separate structural Projection.
- `CA-D-392@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-392@26`
  - Remaining Claim prose:
    the Project Scope Unit Graph Projections **must** expose Project identity from the Project Settings Artifact with `project.name` as the canonical name **and** `project.obsolete_names` as the registered prior names **without** becoming authority for (Project Settings Name **or** Obsolete Project Name).
    
    ### Current source pin
    
    Proposed N+1 successor of `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/CA-D-392-CORE_META_MODEL-ENG_DECISION--register-obsolete-project-names.md`, CA-D-392@24, SHA-256 `384bfda590d882b143ab76b14854621d123a24026f7d90710da83ea50a3f79ca`. Current bytes remain unchanged; this Draft preserves the `project.obsolete_names` encoding and performs no projection refresh.
- `CA-D-393@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-393@23`
  - Remaining Claim prose:
    **when** an external Type name is derived from an internal Type, the derivation uses `external_<internal_type_name>`. **when** the internal Type is the Content Role's default, the derived name uses that registered default Type. a separately registered explicit external Type name is non-default **and** does **not** modify this derivation rule.
- `CA-D-399@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-399@25`
  - Remaining Claim prose:
    a Requirement Atom File Carrier **must** serialize its effective Label within the Atom filename grammar governed by CA-D-283 and CA-D-284, using the explicit Label when present and the Type name when Label is absent. The effective Label is normalized as an uppercase structured token; an unlabeled Constraint and Boundary therefore use `CONSTRAINT` and `BOUNDARY`. This generic rule covers every admitted Requirement Type and does not rename a Type, admit a new Type, or prescribe a YAML Type value.
- `CA-D-400@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-400@25`
  - Remaining Claim prose:
    an Evaluation Atom File Carrier **must** serialize its effective Label within the Atom filename grammar governed by CA-D-283 and CA-D-284, using the explicit Label when present and the Type name when Label is absent. The effective Label is normalized as an uppercase structured token; an unlabeled Eval Case, Evaluation Control and Evaluation Approach therefore use `EVAL_CASE`, `EVALUATION_CONTROL` and `EVALUATION_APPROACH`. This generic rule covers every admitted Evaluation Type and does not rename a Type, admit a new Type, or prescribe a YAML Type value.
- `CA-D-401@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-401@24`
  - Remaining Claim prose:
    a Concern Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:
    
    - Question: `QUESTION`.
    - Problem: `PROBLEM`.
    - Risk: `RISK`.
    - Opportunity: `OPPORTUNITY`.
    
    these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.
- `CA-D-402@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-402@27`
  - Remaining Claim prose:
    a Delivery Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283-CORE_META_MODEL-ENG_DECISION--serialize-project-owned-markdown-atom-filenames **and** CA-D-284-CORE_META_MODEL-ENG_DECISION--serialize-filename-token-case:
    
    - Eng Policy: `ENG_POLICY`.
    - Eng Decision: `ENG_DECISION`.
    - Release Definition: `RELEASE_DEFINITION`.
    - Environment Definition: `ENVIRONMENT_DEFINITION`.
    
    these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.
- `CA-D-404@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-404@28`
  - Remaining Claim prose:
    a Method Atom File Carrier **must** serialize its effective Label within the Atom filename grammar governed by CA-D-283 and CA-D-284, using the explicit Label when present and the Type name when Label is absent. The effective Label is normalized as an uppercase structured token; an unlabeled Eng Policy, Eng Decision, External Implementation Method and Method Binding therefore use `ENG_POLICY`, `ENG_DECISION`, `EXTERNAL_IMPLEMENTATION_METHOD` and `METHOD_BINDING`.
- `CA-D-407@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-407@25`
  - Remaining Claim prose:
    the Default Settings Artifact **must** use `caprmedio_framework_default_settings.toml` **at** the root of the CORE_META_MODEL source Scope Unit as its **`=1`** authoritative TOML File Carrier.
- `CA-D-408@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-408@24`
  - Remaining Claim prose:
    **every** parameter value **in** the Default Settings TOML Carrier **must** use the same registered section, field path, value type, **and** allowed domain as the corresponding explicit Framework Instance Settings parameter, **without** introducing a separate defaults-field schema.
- `CA-D-440@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-440@21`
  - Remaining Claim prose:
    the authoritative Project Structure Carrier **must** be **`=1`** UTF-8 TOML file named `project_structure.toml` directly inside the owning `.caprmedio_<project_name>/` directory. `<project_name>` resolves from the owning Project Settings. this non-Atom Carrier **must not** carry an Atom ID, Atom Content Role, Atom Frontmatter, **or** non-authoritative Projection metadata. concrete unit paths belong **only** **to** this file, while Delivery Atoms retain general Carrier schema **and** representation authority.
- `CA-D-441@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-441@22`
  - Remaining Claim prose:
    the Project Structure TOML document **must** contain the integer `schema_version = 1` **and** **`=1`** `scope_units` array of tables, with **`>=0`** rows for declared non-Project Scope Units. an empty array **must** use `scope_units = []`; nonempty arrays use `[[scope_units]]`. the root Project is implicit from Project Settings **and** **must not** have a duplicate row. unknown top-level keys, unknown row keys, duplicate TOML keys, **and** unsupported schema versions **must** be rejected rather than ignored. document comments **may** explain authority **and** retained readability fields, **without** introducing additional authoritative fields.
- `CA-D-442@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-442@25`
  - Remaining Claim prose:
    **every** `[[scope_units]]` table **must** use the following field signatures **and** field order for readable serialization. omission is permitted **only** **where** stated; an empty string **or** copied default **must not** substitute for omission.
    
    | Field | TOML value **and** responsibility |
    |---|---|
    | `scope_unit_name` | required nonempty canonical Scope Unit Name string |
    | `parent` | required string: `PROJECT` for the owning root, **otherwise** a declared Scope Unit Name **in** the same Project |
    | `scope_unit_type` | required string **in** (`Ordered`, `Unordered`) |
    | `scope_unit_label` | required nonempty canonical Label string, independent of Type |
    | `local_order` | required integer **only** for Ordered units; absent for Unordered units |
    | `navigational_order_number` | required nonnegative integer, independent of structural Local Order |
    | `authority_path` | required nonempty repository-relative directory path string |
    | `delivery_path` | required nonempty repository-relative Implementation Folder path string |
    | `authority_mode` | optional explicit string **in** (`strict`, `casual`); absence inherits Framework Instance Settings |
    
    both path fields use forward slashes **and** resolve from the repository root, **not** the TOML directory; a trailing slash does **not** establish another binding. absolute paths, parent traversal, escaping symlinks **and** paths resolving **to** another Project's control root are invalid. a native Carrier binding under admitted Delivery authority **may** differ from ordinary physical nesting. `structural_level`, `node_id`, `structural_parent`, `child_composition`, `project_boundary_position`, `authority_materialized`, **and** `numeric_prefix` are **not** authored row fields. Any readable ancestry/path display is derived from `parent` declarations under CA-R-2133 and is not another declaration.
- `CA-D-443@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-443@21`
  - Remaining Claim prose:
    a Project Structure Revision binding **must** identify the exact authoritative TOML bytes by SHA-256 Digest **and** the completed change event **in** the canonical Event Log under applicable Journal authority. the binding **must** distinguish the selected pre-change state, resulting state, **and** actual completion **or** failure; missing **or** conflicting event evidence leaves provenance currentness unknown. the TOML Carrier **must not** duplicate Atom Revision fields **or** store its own self-referential digest. a consumer **may** parse **and** validate the selected bytes **without** claiming completed change provenance **when** that provenance is unresolved.
- `CA-D-444@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-444@23`
  - Remaining Claim prose:
    a staged Project Structure candidate **must** use the filename `project_structure.candidate.toml` inside the explicitly selected migration workspace, outside the canonical active path. no ordinary consumer **may** discover it as active authority; candidate validation requires an explicit candidate path. cutover **must** install the validated candidate at the canonical path **only** **after** freshness, authorization, reference repairs, consumer readiness **and** recoverability checks pass. the old active bytes **must** remain recoverable through accepted change evidence **without** becoming another active structural source. the candidate **must** be retired **after** successful activation **or** rejection; failure **must not** leave two files eligible for normal authority resolution.
- `CA-D-447@30`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-447@30`
  - Remaining Claim prose:
    an explicitly selected Implementation Retry Limit **must** use the integer field assigned **to** its owning source Carrier:
    
    - Framework Instance Settings TOML: `implementation.retry_limit`.
    - Default Settings TOML: the same field under CA-D-408-CORE_META_MODEL-DELIVERY--reuse-framework-parameter-fields-in-default-settings.
    - a Plan Atom's own File Carrier frontmatter: `implementation_retry_limit`, including a Hub's mandatory Markdown File Carrier.
- `CA-D-457@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-457@26`
  - Remaining Claim prose:
    an Operations Atom File Carrier **must** serialize its Type using this filename-token mapping:
    
    | Operations Atom Type | Filename token |
    |---|---|
    | Action | `ACTION` |
    | Workflow | `WORKFLOW` |
    | Step | `STEP` |
- `CA-D-461@29`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-461@29`
  - Remaining Claim prose:
    **every** Plan Carrier Bundle **must** represent its carried Status **in** the following locations:
    
    - Draft: **in** the owning Scope Unit's shared `03_plan/draft` area.
    - Active: directly **in** its local container.
    - Backlog: **in** its `001_backlog` subdirectory.
    - Done: **in** its `done` subdirectory.
    - Canceled: **in** its `canceled` subdirectory.
    - Archived: **in** the owning Scope Unit's shared `03_plan/archived` area.
    
    For a contained Current Plan, the local container for its current-Status placement is the matching Directory Carrier of its declared immediate containing Plan. Draft and Archived areas are shared across the owning Scope Unit, rather than replicated under each Plan container. This rule does **not** decide terminal-Status placement for a Plan without an `IS_CONTAINED_BY` connection. reserved Status directories are **not** Plan nodes. validate folder nesting against the child's direct `IS_CONTAINED_BY` declaration; placement does **not** declare containment.
    
    read Status from the Plan's own Markdown file under CA-D-483 **and** check its local placement; a parent **or** folder name **must not** supply a descendant's Status at read time. **every** admitted parent Status change requires the containment cascade under CA-R-1521: separate single-Atom Actions write the Status prescribed by CA-R-1521 to each selected latest descendant under its own model, without an optional descendant mode. For a containing Plan Atom whose requested Status is Done **or** Canceled, preserve every selected latest contained Plan already Done **or** Canceled and request Canceled for every other selected latest contained Plan. After the cascade, every selected latest contained Plan must be Done **or** Canceled; mixed terminal statuses are allowed, and no contained Plan is forced to match the parent's requested Status merely because the parent is Done **or** Canceled. For other admitted parent Statuses, preserve the applicable cascade. Archive selects all contained latest Atoms; references outside the Carrier tree **and** older archived Revisions are excluded. retain Current descendants inside the parent Carrier tree. Archived Plan Markdown Carriers are placed flat in the owning Scope Unit's shared `03_plan/archived` area, not inside an archived parent's directory.
- `CA-D-465@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-465@23`
  - Remaining Claim prose:
    **every** materialized Structural Entity **must** be carried by **`>=1`** Directory Carrier; a Scope Unit established by Project Structure **may** remain unmaterialized under CA-R-1484-CORE_META_MODEL-RULE--establish-scope-units-through-project-structure-declarations without losing its declaration **or** identity.
- `CA-D-467@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-467@24`
  - Remaining Claim prose:
    a folder-backed Workflow **must** use **`=1`** Workflow Atom Markdown Carrier **and** **`<=1`** optional sibling Directory Carrier with the same filename stem. the Directory Carrier contains separate Markdown Carriers for its Step Atoms; it **must not** contain a second Workflow definition.
- `CA-D-472@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-472@25`
  - Remaining Claim prose:
    an explicit Plan Autonomous Confidence Threshold override **must** use the top-level integer frontmatter field `autonomous_confidence_threshold` **in** that Plan Atom's own mandatory Markdown File Carrier.
    
    - a Hub uses that same file, **not** a separately identified Objective **or** Epic settings file.
    - omit an unselected override **without** copying its inherited value; the mandatory file requirement does **not** turn inheritance into a local selection.
    - retain an explicit override even **when** it equals the inherited value.
    - `epic_overrides` is **not** an alternative canonical encoding.
- `CA-D-473@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-473@25`
  - Remaining Claim prose:
    a Plan File Carrier **may** serialize **`=1`** explicit Assignee override as top-level frontmatter `assignee`; omission **must** preserve CA-R-1585-CORE_META_MODEL-RULE--default-plan-work-assignment-to-an-ai-agent for its own work rather than copying the default.
- `CA-D-475@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-475@24`
  - Remaining Claim prose:
    the Plan Backlog Directory **must** be `03_plan/001_backlog`; it is a Status container, **not** a Plan Atom. a Version-labeled Plan uses the ordinary Plan Carrier grammar under CA-D-469-CORE_META_MODEL-DELIVERY--serialize-plan-carrier-stems rather than an independently identified Version Plan Collection **or** special `version-<VERSION>` container.
- `CA-D-482@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-482@27`
  - Remaining Claim prose:
    a Markdown Atom Carrier **must** carry its resolved Claim Target Scope Unit **in** frontmatter, including a Current-scope Atom whose target is its own Scope Unit.
    
    - choose the current Scope Unit as the default during authoring, **not** by relying on the file's later location.
    - a carried target equal **to** the current Scope Unit does **not** make the Atom Relational. a different target still requires the applicable Relational Atom admission.
    - Claim Scope restrictions use the body sections under CA-D-495-CORE_META_MODEL-CORE-DELIVERY--carry-applicability-in-the-registered-body-sections; the RMED Scope section does **not** replace **or** duplicate `claim_target_scope_unit`.
    
    - encode this Property as the top-level nonempty YAML string `claim_target_scope_unit`, resolving **to** **=1** registered Scope Unit. null, lists, **and** a duplicated `claim_scope` field are **not** this encoding.
    - an external Requirement of Type Project Goal carries its Operator Actor owner using the existing Author fallback under CA-D-657-CORE_META_MODEL-DELIVERY--use-economical-yaml-frontmatter **in** `current_scope_unit`, **and** the Project **in** `claim_target_scope_unit`. This is the explicit Actor-owner exception, not a Project-owned Atom with incidental Actor provenance. Do **not** register the Operator as a Scope Unit **or** infer either value from the filename.
- `CA-D-494@17`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-494@17`
  - Remaining Claim prose:
    the authoritative Operator registry **must** use **`=1`** `operators_registry.toml` file **in** the Project authority root, alongside Project Settings.
    
    - the root has **`=1`** key, `operators`, containing **`>=1`** `[[operators]]` table.
    - **every** table has **`=1`** `name` **and** **`=1`** `role`, both nonempty strings. names are unique. a table may also carry **<=1** `journal_author`, an explicitly registered Journal account name using the Journal's Author format. provided Journal account names are unique; **other** additional keys **or** duplicate identities make the registry invalid.
    - Author membership compares the carried `author` string with registered `name` values exactly, **without** aliases, case folding, trimming, **or** inference from filenames. `role` describes the Operator; it does **not** replace the name **or** independently grant execution permission.
    - concrete Operator names **and** roles belong **only** **in** the Project's registry, **not** **in** reusable methodology **or** Tool code. a missing, unreadable, malformed, **or** stale registry leaves membership unresolved; it is **not** an empty valid registry.
- `CA-D-505@18`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-505@18`
  - Remaining Claim prose:
    the Carrier Property of an Entity **means** its binding **to** the Carrier that stores **or** represents it.
- `CA-D-506@18`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-506@18`
  - Remaining Claim prose:
    Every represented non-ephemeral Entity has at least one declared Carrier or a location within a shared Carrier. Reusable D Policies may define that binding for an entire Object kind and its dependent properties; individual D Decisions govern bounded exceptions. The governed Subject names the represented entity, not an extra representation node.
- `CA-D-507@16`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-507@16`
  - Remaining Claim prose:
    a change **to** Carrier Format **or** File Carrier Extension alone **must not** establish **or** change Entity identity.
- `CA-D-565@18`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-565@18`
  - Remaining Claim prose:
    **when** an Atom Revision newly attains its model-admitted `Archived` Status **and** no more-specific applicable Delivery mapping exists for its Artifact Type, its **`=1`** Markdown Archive Carrier **must** be classified as that Revision's Archive Carrier **and** be placed at `archive/<canonical-ID>@<version>[-<remaining-filename-components>].md`: the owning Content Role's existing `archive/` directory is retained, and the single `@<version>` marker occupies the Atom-ID segment under CA-D-283/CA-D-289. Preserve the archived Atom's numeric Version and prior Updated At; its new Archive Carrier carries `status: Archived`.
- `CA-D-570@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-570@22`
  - Remaining Claim prose:
    A Draft Atom **must not** require `revision_lineage`, a retained Draft-history entry or a trusted Draft head for Create, Update, promotion, another admitted Status change or their success. Every Draft Carrier carries the mandatory Draft `atom_id` marker under CA-D-378/CA-D-446; its filename follows CA-D-650.
    
    Existing `revision_lineage: {history_entry_ref: {history_revision, path}}` metadata and the actual retained records it references may remain as recorded historical data. Their presence, absence, encoding, resolvability, origin, parent chain, head/leaf status or consuming-successor state **must not** become a mutation or completion gate. Do **not** require a caller or writer to register, reconstruct, repair, reserve, append or consume such a record to admit the current operation.
    
    When a Current Atom changes, archive its predecessor with the old numeric Version and Updated At, an Archived status and a version-qualified identity under CA-D-446/CA-D-565; the Current successor follows the normal Version and timestamp rules. Do **not** fabricate history or reinterpret an observed value as evidence of an event that was not observed. Preserve the exact admitted target, ordinary Summary/replacement rules, applicable schema, collision/currentness checks and permissions. No new identity registry, history writer, recovery framework or Journal protocol is introduced.
- `CA-D-634@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-634@21`
  - Remaining Claim prose:
    Deliver the view as a UTF-8 Markdown file under the Project's declared Projection root. Include YAML frontmatter and tab-indented trees inside fenced text blocks.
- `CA-R-1222@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1222@25`
  - Remaining Claim prose:
    the CAPRMEDIO Project's methodology customizations **must** remain **in** PROJECT_CONFIGURATION **until** the Operator accepts a separately identified Extension package containing those customizations.
- `CA-R-1226@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1226@23`
  - Remaining Claim prose:
    **every** Project Customization **must** identify **`=1`** customized Core Meta-Model **or** Extension revision **without** modifying that revision.
- `CA-R-1228@35`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1228@35`
  - Remaining Claim prose:
    the Applicable Methodology source set **must** include CORE_META_MODEL, PROJECT_CONFIGURATION, **and** **every** installed Extension Source applicable under the current Framework Instance Settings. **when** **none** is applicable, the Extension contribution **is empty** **without** a rule requiring zero installed Extensions **or** a Carrier for an empty INSTALLED_EXTENSIONS collection.
- `CA-R-1314@32`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1314@32`
  - Remaining Claim prose:
    **every** Applicable Methodology member **must** retain **`=1`** direct DERIVED_FROM relation **to** its exact source Atom Revision.
- `CA-R-1315@31`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1315@31`
  - Remaining Claim prose:
    the Applicable Methodology membership **must** contain **only** current Atom Revisions whose type-qualified Status **`=`** Active **and** whose Content Role is **in** (Requirement, Method, Evaluation, Delivery, Operations).
- `CA-R-1316@30`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1316@30`
  - Remaining Claim prose:
    Applicable Methodology compilation **must not** synthesize **or** merge source Claims.
- `CA-R-1317@29`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1317@29`
  - Remaining Claim prose:
    **if** an Applicable Methodology conflict remains unresolved **or** its required Operator approval is missing, stale, partial, ambiguous, **or** mismatched, **then** compilation **must** fail **without** changing Applicable Methodology membership.
- `CA-R-1354@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1354@22`
  - Remaining Claim prose:
    **only** the CAPRMEDIO Main Skill **may** load the CAPRMEDIO General System Prompt.
- `CA-R-1355@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1355@22`
  - Remaining Claim prose:
    the CAPRMEDIO Main Skill **must** route **every** requested registered branch **or** leaf through the CAPRMEDIO Routing Tree.
- `CA-R-1356@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1356@24`
  - Remaining Claim prose:
    A CAPRMEDIO Direct Route Skill **must** be an Operator-defined Skill bound **to** **`=1`** branch **or** leaf registered **in** the CAPRMEDIO Routing Tree **and** **must** invoke **only** that bound target.
- `CA-R-1514@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1514@25`
  - Remaining Claim prose:
    **in** the CAPRMEDIO Project, governing RMED **must** fully specify the required Implementation independently of the Workflow used **to** produce it.
- `CA-R-1560@17`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1560@17`
  - Remaining Claim prose:
    the Operator **may** add a CAPRMEDIO Direct Route Skill.
- `CA-R-1612@22`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1612@22`
  - Remaining Claim prose:
    an Evaluation using a Realization Graph **may** return `pass` **before** runtime **only** **when** sufficient evidence establishes the checked Claim for the declared input boundary.
    
    - **if** the Claim requires complete coverage of particular Relation mechanisms, the evidence **must** establish that coverage; a completeness declaration alone is insufficient.
    - the evidence **must** establish the actual acceptance condition. complete provenance **or** graph coverage does **not** itself establish that condition.
    - a possible inferred Relation is **not** an observed occurrence. **when** required runtime evidence is unavailable **or** a material condition remains unresolved, the Evaluation **must not** return a pre-runtime `pass`.
    
    this Claim constrains permission **to** report a result; the applicable E Atoms supply the checks. it does **not** require complete graph coverage for a Claim that needs **only** bounded evidence.
- `CA-R-1620@19`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1620@19`
  - Remaining Claim prose:
    the dependency view of a Realization Graph **means** an optional derived view of the selected declarations, resources, internal dependency targets, external dependency targets, **and** admitted typed Relations among them.
- `CA-R-1621@17`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1621@17`
  - Remaining Claim prose:
    the caprmedio Project Configuration **must** register `realization_graph` as a specialized non-authoritative Projection Type for understanding existing Implementation **and** supporting reverse engineering into proposed RMED.
- `CA-R-1635@39`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1635@39`
  - Remaining Claim prose:
    **every** production-relevant component **or** governed scope **must** define a Production Evaluation Checklist **before** it can pass a production-readiness gate. the checklist states how operators will know that the realized system remains healthy, correct, supportable, **and** within its accepted operating boundaries during real work.
    
    **every** operational condition **or** invariant is owned by one `evaluation_control` Atom. the control identifies:
    
    - the Requirement, Demand For, Constraint, Method, **or** other governed claim being assured;
    - the production signal **and** authoritative data source;
    - the healthy condition, expected range, threshold, **or** failure predicate;
    - the evaluation window, cadence, **and** permitted detection delay;
    - the component, entity, lifecycle state, **or** workflow boundary **to** which it applies;
    - the accountable owner **and** escalation destination;
    - the alert, incident, investigation, degradation, rollback, **or** recovery action triggered by failure;
    - the diagnostic context required **to** investigate the condition;
    - the required factual execution record **and** evidence-retention boundary; **and**
    - known blind spots, sampling limits, unavailable signals, **and** other evaluation limitations.
    
    a Production Evaluation Checklist is a Catalog Projection over the applicable `evaluation_control` Atoms. it organizes **and** navigates those controls **without** absorbing, paraphrasing, **or** replacing their Claims. the Catalog Projection does **not** acquire the Content Role of its source Atoms.
    
    **every** control distinguishes its governed meaning from its realization **and** results:
    
    - the Evaluation Control defines the production evaluation condition;
    - monitors, dashboards, alerts, health checks, **and** operational automation are Implementation;
    - recorded metrics, logs, traces, alerts, incidents, **and** check outcomes are factual execution records, **not** reusable Operations definitions; **and**
    - a Concern Atom of Type `problem` records a material discrepancy requiring disposition.
    
    a Production Evaluation Checklist presents the applicable controls for real production operation **without** becoming their authority. it is **not** a QA Case, **and** passing pre-release Test **or** Evaluation implementations does **not** by itself satisfy the production-evaluation obligation.
- `CA-R-1637@30`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1637@30`
  - Remaining Claim prose:
    The CAPRMEDIO Main Skill **must** be the canonical Skill with identity `ca`.
- `CA-R-1640@31`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1640@31`
  - Remaining Claim prose:
    **`=1`** machine-readable **and** human-readable routing tree **must** be registered as the sole owner of intent concepts, synonyms, entry criteria, route targets, authority effects, outputs, **and** approval requirements.
- `CA-R-1641@31`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1641@31`
  - Remaining Claim prose:
    skill routes **must** resolve by explicit precedence: project-local CAPRMEDIO routes override framework routes, which override provider-global routes.
- `CA-R-1645@37`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1645@37`
  - Remaining Claim prose:
    Governance Origin for the self-hosted caprmedio Project **and** its distributed CAPRMEDIO sources follows the ownership distinction **in** CA-R-1709@38-CORE_META_MODEL-DEFINITION--define-two-governance-origins:
    
    - within the caprmedio Project, its Project-owned Methodology authority, framework authority, **and** other Project-owned Artifacts have internal Governance Origin.
    - a distributed CAPRMEDIO framework source has external Governance Origin relative **to** a consuming Project. that Project's own adaptation authority has internal Governance Origin; creating it does **not** transfer ownership of the external source **or** change that source's origin.
    - graph Relations, version-control authorship, filesystem ownership, **and** byte identity do **not** replace the governing ownership distinction.
- `CA-R-1647@30`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1647@30`
  - Remaining Claim prose:
    CAPRMEDIO generates a non-authoritative proof-currentness Catalog from governed proof dependency frontiers encoded under GOV REQU 010 **and** their additional invalidation conditions. the Catalog reports **every** proof as `current`, `stale`, **or** `unknown`, marks **only** the smallest direct **and** transitive dependency closure affected by a change, never infers currentness from timestamps alone, **and** never mutates the historical proof record.
- `CA-R-1651@33`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1651@33`
  - Remaining Claim prose:
    Governance **must** propose narrower ordered Epics **and** **may** apply the split **only** **after** Operator approval.
- `CA-R-1662@38`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1662@38`
  - Remaining Claim prose:
    Policy, Eval Case, QA Case, **and** Evaluation Control **must** be registered as internal values of `Atom/Content Role: Evaluation/Type`.
- `CA-R-1663@36`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1663@36`
  - Remaining Claim prose:
    Question **and** Problem retain their canonical admission under CA-R-1231@28. Risk **and** Opportunity **must** be registered as additional internal values of `Atom/Content Role: Concern/Type`.
- `CA-R-1665@34`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1665@34`
  - Remaining Claim prose:
    Policy and Decision are the Delivery Type values for reusable delivery rules and bounded delivery choices. Release and Environment describe governed things or applicability; they do not require separate Delivery Types.
- `CA-R-1666@36`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1666@36`
  - Remaining Claim prose:
    the CAPRMEDIO Project Configuration **must** register Action Policy as an additional value of `Atom/Content Role: Plan/Type`; Plan retains its canonical admission under CA-R-1574@21-CORE_META_MODEL-DEFINITION--define-the-common-plan-atom; navigation Labels do **not** add further Type values.
- `CA-R-1668@34`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1668@34`
  - Remaining Claim prose:
    Eng Decision **means** the internal Type value under Content Role Method for one concrete implementation choice bounded **to** an explicit realization target.
- `CA-R-1692@36`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1692@36`
  - Remaining Claim prose:
    a target Version **must** remain mutable **until** its selected authorized release event succeeds **and** the shared Journal records that outcome for the exact released candidate.
    
    - the release record is a factual Journal Record under CA-R-1712, **not** an Operations Atom.
    - its exact manifest binds the released governing Atom Revisions, Implementation **and** Delivery Revisions, applicable Evaluations **and** evidence, **and** release identifier.
    - the selected release policy defines the event boundary. applicable Delivery authority defines the manifest **and** Journal representation; a selected Extension owns mechanism-specific references.
    - planning allocation, implementation completion, readiness acceptance, **or** release-candidate naming does **not** freeze the Version **before** the successful event.
- `CA-R-1736@30`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1736@30`
  - Remaining Claim prose:
    CAPRMEDIO expands **to** Concern, Analysis, Plan, Requirement, Method, Evaluation, Delivery, Implementation, **and** Operations **in** that canonical order.
- `CA-R-1752@31`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1752@31`
  - Remaining Claim prose:
    a Project Adaptation is project-owned PRMEDO authority that adds, specializes, narrows, **or** prohibits capabilities for one Project **without** modifying the Canonical Framework **or** Extension authority it adapts.
- `CA-R-1753@30`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1753@30`
  - Remaining Claim prose:
    the governed definitions of Project Adaptation **and** Extension **must** be owned by their applicable Atoms. the Framework Instance Settings Artifact **may** select, disable, **and** parameterize them, **and** Project Scope Unit Graph Projections **may** expose the effective result, but Framework Instance Settings **and** Project Scope Unit Graph Projection **must not** redefine **or** amend those governed definitions.
- `CA-R-1769@33`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1769@33`
  - Remaining Claim prose:
    a Project **must** apply a Methodology Source update **or** downgrade **only** by selecting an identified source revision **and** reconciling affected Project authority; the selection **must not** silently rewrite other Methodology Sources **or** Project-owned Atoms.
- `CA-R-1778@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1778@27`
  - Remaining Claim prose:
    the Framework name **must** be `CAPRMEDIO`.
- `CA-R-1779@15`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1779@15`
  - Remaining Claim prose:
    **every** production-relevant component **must** define a Logging Policy. that policy:
    
    - governs required log coverage, structure, severity, safety, **and** retention **before** failures occur;
    - supports its Evaluation Controls;
    - is referenced by the Catalog Projection over its applicable Evaluation Control Atoms; **and**
    - identifies the events **and** context required **to** understand normal operation, detect failure, correlate distributed work, **and** investigate real production issues.
- `CA-R-1780@11`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1780@11`
  - Remaining Claim prose:
    a Logging Policy **must** use these four operational levels:
    
    | Level | Required meaning |
    |---|---|
    | `ERROR` | an operation failed, correctness **or** availability **may** be affected, **or** explicit retry **or** intervention is required |
    | `WARNING` | behavior was unexpected **or** degraded but recovered, fell back, **or** remains within an accepted tolerance |
    | `INFO` | a material lifecycle, business, **or** operational milestone occurred, including start, stop, acceptance, state transition, completion, **or** summarized progress |
    | `DEBUG` | sanitized internal state **or** decision detail is useful for bounded investigation but is unnecessary during normal production operation |
- `CA-R-1781@12`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1781@12`
  - Remaining Claim prose:
    logging Implementation **must** bound high-frequency success, polling, **and** progress events through aggregation, sampling, **or** emission as `DEBUG` **where** appropriate rather than creating unbounded `INFO` noise.
- `CA-R-1782@13`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1782@13`
  - Remaining Claim prose:
    logging Implementation **must** keep production DEBUG logging disabled by default. temporary enablement **must** be scoped by component, subject, run, entity, **or** another bounded selector, have an automatic expiry, **and** preserve the same redaction rules as **every** other level.
- `CA-R-1783@11`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1783@11`
  - Remaining Claim prose:
    a production Logging Policy **must** define retention, access, sampling, rotation, maximum size, back-pressure, unavailable-sink behavior, **and** disk-pressure behavior.
- `CA-R-1784@11`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1784@11`
  - Remaining Claim prose:
    logging Implementation **must not** make the primary operation silently fail.
- `CA-R-1785@12`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1785@12`
  - Remaining Claim prose:
    logging Implementation **must** produce an observable failure signal **when** required records are lost **or** suppressed.
- `CA-R-1786@11`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1786@11`
  - Remaining Claim prose:
    important production health counters, thresholds, **and** service-level signals receive explicit monitors.
- `CA-R-1787@11`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1787@11`
  - Remaining Claim prose:
    a production evaluation decision **must not** depend solely on parsing free-form log prose.
- `CA-R-1795@12`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1795@12`
  - Remaining Claim prose:
    CAPRMEDIO **must** reconcile the Development Backlog against its exact released manifest as follows:
    
    - remove a candidate whose promoted Atoms were fully delivered **in** that release.
    - **every** candidate that is unfinished, partially delivered, excluded, **or** newly deferred **must** remain unscheduled **or** move **to** another target version.
    - a candidate **must not** be removed as shipped **unless** the released manifest accounts for its promoted Atoms.
- `CA-R-1796@12`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1796@12`
  - Remaining Claim prose:
    CAPRMEDIO **must** append Journal records for Development Backlog reconciliation.
- `CA-R-1798@13`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1798@13`
  - Remaining Claim prose:
    CAPRMEDIO **must** preserve delivered work, executed work, **and** planning-allocation changes **in** Release Records, Plans under `done/`, **and** Git history.
- `CA-R-1888@13`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1888@13`
  - Remaining Claim prose:
    the CAPRMEDIO Project Configuration **must** register FPF Analysis Report as an additional value of `Atom/Content Role: Analysis/Type` under CA-R-1286. this registration does **not** change the Core contribution under CA-R-1232@28 **or** create another Type Property.
- `CA-M-225@31`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-225@31`
  - Remaining Claim prose:
    **to** retrieve Applicable Methodology for one Subject **or** Workflow query, the Retriever **must** derive GOVERNS **and** DEPENDS_ON indexes on demand from projected Atom Subjects, select matching GOVERNS paths, add DEPENDS_ON authority **only** through transitive prerequisite closure, retain Applicable Methodology membership order, make no inference, **and** return no Atom **if** no matching GOVERNS path exists.
- `CA-M-260@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-260@23`
  - Remaining Claim prose:
    **to** represent a governed statement **in** the Project, maintain **`=1`** authoritative source for that statement **in** the same context **and** make **all** other representations reference **or** derive from that source **without** independent authority.
- `CA-M-277@31`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-277@31`
  - Remaining Claim prose:
    **to** report **in** `silent` mode, answer exploratory input normally **and**, apart from the mandatory information governed by CA-R-1440-CORE_META_MODEL-GENERAL-REQUIREMENT--preserve-mandatory-information-in-every-reporting-mode, report **only** durable Artifacts **or** Project state that CAPRMEDIO created, updated, archived, committed, **or** **otherwise** changed; omit ordinary announcements of mode selection, workflow routing, Skill chaining, **and** gate transitions.
- `CA-M-278@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-278@28`
  - Remaining Claim prose:
    **to** report **in** `verbose` mode, explicitly report relevant workflow modes, mode transitions, selected Skill chains, entry **and** exit gates, **and** planned **or** completed Artifact operations, together with the mandatory information governed by CA-R-1440-CORE_META_MODEL-GENERAL-REQUIREMENT--preserve-mandatory-information-in-every-reporting-mode.
- `CA-M-300@18`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-300@18`
  - Remaining Claim prose:
    **to** select a Requirement Type, the Author **must** use Constraint **only** for a limitation imposed from outside the Project choice boundary.
- `CA-M-345@15`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-345@15`
  - Remaining Claim prose:
    **to** author an FPF Analysis Report, use the common Analysis structure under CA-D-479 and retain the report's bounded question, scope, approach, results, provenance and evidence limits without treating its recommendations as accepted specification.
    
    - carry `role: Analysis` and `form: FPF Analysis Report`, the actual owning Scope Unit, applicable tier, Status and Version Properties. Summary describes the Question; TLDR summarizes the retained analytical record without replacing Results.
    - **when** importing an existing report, preserve its complete original UTF-8 text as quoted Markdown in Results. Quotation is a carrier wrapper, not an edit to the original text. Record its original path, SHA-256 and byte length in Approach so the original bytes can be recovered and checked.
    - identify the original inquiry from its explicit task or question where available; otherwise identify the bounded historical report without inventing a missing execution contract. Preserve all native findings, alternatives, citations, limitations and time-relative statements in the quoted record.
    - distinguish import metadata and its current Revision timestamp from the original report's provenance. Do not infer an original execution timestamp or completed FPF Run merely from a filename or physical file existence.
    - place the Carrier by the applicable Analysis Delivery rules. Resolve real destination links to the new Carrier while retaining historical Journal, archive and frozen-evidence references unchanged.
- `CA-E-207@34`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-207@34`
  - Remaining Claim prose:
    the evaluated behavior passes **if** **all** applicable conditions hold **and** are supported by the evaluated evidence:
    
    - the effective model **and** parameters correspond **to** applicable Operator input; unresolved input is reported **without** activating an invented model **or** preference.
    - **every** selected alternative satisfies active authority **and** non-negotiable constraints.
    - selection follows the Operator-selected model **without** substituting another algorithm.
    - for comparison by priority order, the first deciding criterion governs relative preference; later criteria do **not** reverse it **or** bypass an unresolved earlier comparison.
    - a tie **or** incomparable result is **not** converted into an automatic winner **without** authority from the selected model.
    - unresolved input **or** comparison is returned **to** the Operator with its known inputs, alternatives **when** available, constraints, evidence, **and** exact unresolved point.
    
    ### Falsification
    
    the evaluated behavior fails **if** **any** applicable acceptance condition is false. missing evidence for an applicable condition leaves that condition unevaluated, **not** passed.
- `CA-E-379@46`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-379@46`
  - Remaining Claim prose:
    the Applicable Methodology Compilation Validation **must not** pass **if** **any** of:
    
    - CORE_META_MODEL, PROJECT_CONFIGURATION, **or** an applicable installed Extension Source under CA-R-1228 is omitted; an unselected **or** inactive Extension revision contributes.
    - an eligible current active source Atom under CA-R-1315 is omitted, **or** an ineligible Atom Revision contributes.
    - compilation requires a hard-coded Extension name **or** particular Project-specific Project Configuration contents, rejects a conforming source merely because its contents are new, **or** requires an empty INSTALLED_EXTENSIONS Carrier **when** no Extension is applicable.
    - a selected Atom ID, exact source Revision, authority owner, **or** Claim changes; Claims are synthesized **or** merged; a projected member loses its required source traceability **or** Carrier form.
    - the `projection.source_carrier_path` binding required by CA-D-305 is missing, malformed, ambiguous, **or** resolves anywhere other than the selected original source Atom Carrier; it is resolved from the repository root rather than the projected file's directory.
    - removing **only** the generated binding does **not** restore the exact selected source bytes; Atom ID, Version, authored Frontmatter, **or** Main Content disagrees with the selected Revision; a changed source is accepted as current **without** regeneration.
    - the binding is copied **to** source authority, treated as another Atom identity, **or** duplicated as an inverse source-to-projection Atom Relation.
    - the conflict report omits a Core expansion-boundary violation, duplicate Atom identity, unresolved replacement, incompatible retained Candidate, **or** unresolved priority; source Atoms are silently discarded **to** hide a conflict.
    - a conflict is resolved **without** an unambiguous actual Operator approval recorded **in** the Journal under CA-O-007 **and** bound **to** the exact proposal, conflict, **and** source-frontier digest; an approval is stale, partial, missing, ambiguous, **or** mismatched; a prohibited Extension **or** Project Configuration override is accepted as conforming.
    - source order **or** LLM inference resolves a conflict, projected Claims are directly corrected, **or** the same resolved source frontier produces different Applicable Methodology membership.
    
    the Evaluation **must** cover an empty Extension contribution, a newly installed conforming Extension with a previously unknown name, changed conforming Project Configuration contents, **and** an expansion that violates Core authority. conforming input changes **must not** require edits **to** generic Core compilation rules merely **to** recognize their names **or** contents.
    
    check the decision **and** correction boundary:
    
    - a valid actual approval recorded **in** the Journal **must not** require a separate approval Atom **in** Project Configuration.
    - a copied approval Claim, an inferred decision, **or** a Journal record **without** evidence of the actual applicable Operator decision **must not** qualify as approval.
    - approved source corrections **must** run through CA-O-008, preserve current rules **and** selections **in** their owning source Atoms **or** settings, **and** record actual outcomes **in** the Journal.
    - rejection, requested revision, missing decisions, failed corrections, **and** partial effects **must** remain distinguishable; **none** **may** be reported as a successfully approved **and** completed correction.
    
    check source-binding fixtures with nested output directories, missing targets, a target for a different Atom, a stale source Revision, tampered body content, **and** a valid current source. **only** the valid source-faithful case **may** pass the source-binding check; historical output **may** remain preserved **without** being reported as current.
- `CA-E-439@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-439@27`
  - Remaining Claim prose:
    within the caprmedio Project, the implementation-loop Evaluation **must** return `fail` **if**
    
    - unchanged mode, RMED, **and** complete execution inputs yield different applicable tasks **or** ordering,
    - a consumer runs **before** its prerequisite,
    - Atom ID overrides a prerequisite,
    - a cycle is admitted,
    - feasible Evaluation-preparation precedence is omitted **or** left implicit,
    - **or** an absolute E-first barrier prevents preparation of an Evaluation prerequisite.
    
    it **must** also return `fail` **if**
    
    - applicable Methods **or** Delivery boundaries are omitted from Evaluation **or** Requirement implementation,
    - Atom ID resolves a Method conflict,
    - preparation of an Evaluation is reported as its execution,
    - **or** completion is reported with **any** applicable Evaluation failed, blocked, **or** unevaluated.
    
    repeated evaluate-fix execution **and** runtime loops alone **must not** be rejected as prerequisite cycles.
- `CA-E-441@33`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-441@33`
  - Remaining Claim prose:
    the retry-policy Evaluation **must** return `fail` **if** **any** of the following occurs:
    
    - the initial failed Evaluation consumes a retry.
    - an automatic retry exceeds the effective Implementation Retry Limit resolved under CA-M-295-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-implementation-retry-limits-by-source-precedence **and** enforced by CA-O-024-PROJECT_CONFIGURATION-ACTION--control-implementation-retries.
    - starting a permitted fix-and-evaluate round is **not** counted once, **or** checking its permission again consumes another retry.
    - a changed failure set **or** automatic next loop silently resets the budget.
    - the last permitted retry fails **without** pausing **and** reporting remaining failures **to** the Operator.
    - retrying bypasses a confidence gate, governing-Atom approval rule, **or** additional Operator constraint.
    - successful completion under CA-O-016-PROJECT_CONFIGURATION-WORKFLOW--implement-evaluations-before-required-behavior still triggers another automatic repair retry.
    
    earlier escalation required by governing authority **must not** be rejected merely because retries remain.
- `CA-E-445@27`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-445@27`
  - Remaining Claim prose:
    the Methodology Scope Units belong **to** the caprmedio Project Scope Unit tree **and** remain governed by its active Project-owned Tier 0 Atoms.
- `CA-E-471@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-471@25`
  - Remaining Claim prose:
    the Evaluation **must** fail a structural change **if** it:
    
    - starts from stale declarations;
    - exceeds authorization;
    - bypasses the effective confidence gate;
    - loses a Goal **or** reference;
    - violates post-change consistency;
    - changes another Project;
    - silently overwrites concurrent changes; **or**
    - reports completion **after** partial failure.
    
    test the following groups:
    
    - create, rename, reparent, reorder, rebind, reconciliation **and** declaration removal against their exact before/after states;
    - rejection, invalid proposal, stale-state failure, injected apply failure **and** authorized recovery.
    
    the following conditions also apply:
    
    - a no-change repeat **must** preserve authority bytes **and** have no additional structural effects.
    - declaration removal **must not** delete a folder **unless** that exact deletion is authorized.
    - a missing structural Projection **must not** prevent an **otherwise** valid change.
- `CA-E-473@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-473@26`
  - Remaining Claim prose:
    **every** case **must** preserve the selected source, effective limit, inherited-versus-explicit distinction, **and** CA-O-024 accounting **without** changing source values **or** granting additional authority.
- `CA-E-474@25`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-474@25`
  - Remaining Claim prose:
    Configurable release readiness is validated by the following cases.
    
    **Cases.**
    
    1. use a Project with no selected release-readiness Workflow; execute its admitted implementation mode under CA-O-016-CORE_META_MODEL-WORKFLOW--implement-evaluations-before-required-behavior.
    2. select CA-O-025 for a candidate with complete passing current evidence **and** required approvals; contrast it with failed, blocked, missing, **or** stale required checks.
    3. provide one required stale Projection **and** one enabled but unrequired Projection. repeat with already-current required output, a source conflict, failed refresh, **and** a changed source Revision.
    4. change a material candidate input **after** Evaluation. separately change an unrelated Artifact **without** changing the evaluated dependency set **or** an additional invalidation condition.
    5. approve a source correction, **then** complete it. separately omit approval **or** exhaust the accepted revisit allowance.
    6. complete readiness **without** executing the configured release event; compare with a successful authorized release recorded **in** the shared Journal.
    7. use a non-Git candidate binding satisfying the selected gates. inspect the selected Workflow's Step bindings **and** its dependency on the existing Core implementation flow.
- `CA-E-483@18`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-483@18`
  - Remaining Claim prose:
    the Evaluation of the CAPRMEDIO Routing Tree registered under CA-R-1640-PROJECT_CONFIGURATION-RULE--register-one-canonical-routing-tree **must** reject a routing tree **when** **any** of the following is present:
- `CA-E-487@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-487@26`
  - Remaining Claim prose:
    the Evaluation of a CAPRMEDIO implementation Spec **must** reject dependence on a production Workflow under CA-R-1514-PROJECT_CONFIGURATION-RULE--keep-implementation-specifications-independent-of-production-workflows.
- `CA-E-491@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-491@23`
  - Remaining Claim prose:
    the Evaluation **must** check that an update Workflow owns the routing of CA-O-067 assessment results under CA-M-303.
- `CA-E-510@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-510@24`
  - Remaining Claim prose:
    the Evaluation accepts a navigation-migration result **only** **if** it conforms **to** CA-O-078 **and** the identified Project Structure authority, preserves declared values **unless** an authorized change selects replacements, **and** distinguishes a ready candidate from unresolved **or** failed preparation.
- `CA-E-588@15`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-588@15`
  - Remaining Claim prose:
    an FPF Analysis Report import **must** pass all of the following checks before the original Carrier is retired:
    
    - the exact Type and filename token are admitted, the carried Atom ID is unique, and the declared Role, owning Scope Unit, tier, Status and Version metadata match the selected authority;
    - exactly one Summary and the ordered Question, Scope, Approach, Results and TLDR sections occur outside the quoted source content, with nonempty values;
    - removing only the quotation wrapper recovers every original source byte, including Unicode, line endings, nested headings, code fences and terminal-newline state; its SHA-256 and byte length match the frozen source;
    - every selected source has exactly one destination, no existing destination is overwritten, stale inputs and destination collisions stop the batch, and a failed batch does not retire an unverified source;
    - rewritten current navigation/source links resolve to the intended new Carriers; historical Journals, archived Revisions, frozen receipts and the quoted report's own historical text remain unchanged.
- `CA-E-652@20`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-652@20`
  - Remaining Claim prose:
    the shared-context implementation **and** Method-learning Workflow check **must** reject any definition **or** Run that conflates their separate completion conditions **or** bypasses their evidence gates.
    
    - exercise selected R/M/D obligations with missing substantive E coverage, an unrelated green linter, and stale optional Method/review projections; reject false coverage. Require current direct source rows, justified inapplicability or current predicates, selected checks, and evidence for each applicable obligation.
    - exercise preliminary_clear with pending checks: it must not complete or pass the candidate. Require final tests and final read-only review on the same candidate and bindings. Inject a review finding, repair, changed test definition, or changed authority; affected earlier evidence must become stale and the required review/check phases must rerun through existing finite diagnosis/retry control.
    - exercise terminal completion followed by an explicitly requested separate release handoff. Reject a cross-Workflow Step route, implicit release execution, missing release admission, and acceptance from definition-only checks. Standalone CA-O-229 remains Isolated.
- `CA-E-666@2`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-E-666@2`
  - Remaining Claim prose:
    The Evaluation **must** check whether RMEDO Conflict Resolution follows CA-O-028-PROJECT_CONFIGURATION-WORKFLOW--resolve-rmedo-conflicts-without-leaving-gaps **and** its reused Actions **without** losing required authority.
- `CA-D-253@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-253@28`
  - Remaining Claim prose:
    the Applicable Methodology Carrier topology **must** separate authoritative Methodology Source Carriers from non-authoritative projected member Carriers.
- `CA-D-305@30`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-305@30`
  - Remaining Claim prose:
    **every** Applicable Methodology projected Atom Carrier **must** retain a one-way source binding **to** the selected authoritative Atom Revision **without** creating another Atom identity:
    
    - preserve the source Atom's authored Frontmatter **and** Main Content unchanged; the **only** compiler-added block is the source binding below.
    - store **`=1`** `projection.source_carrier_path` value **in** the projected Carrier's Frontmatter. resolve it relative **to** the projected Markdown file's directory **to** the original Atom Carrier **in** the selected Methodology Sources.
    - retain the source Atom ID **and** Version; together with the source binding, they identify the selected source Revision. verify source fidelity under CA-E-379 rather than assuming that an existing path proves currentness.
    - treat this block as Projection metadata, **not** an authored Atom Property **or** a new Atom-to-Atom Relation. do **not** copy it upstream **or** add inverse links **to** source Atoms.
    
    **after** removing **only** the generated source-binding block, the projected Carrier bytes **must** equal the selected source Carrier bytes. missing, ambiguous, wrong-source, **or** stale bindings **must not** be accepted as current Applicable Methodology.
- `CA-D-306@28`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-306@28`
  - Remaining Claim prose:
    Applicable Methodology **must** be materialized as its selected projected RMEDO Atom File Carriers **and** **must not** be replaced by one monolithic JSON Carrier.
- `CA-D-307@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-307@26`
  - Remaining Claim prose:
    Applicable Methodology **must not** store a persistent GOVERNS **or** DEPENDS_ON Subject Index Carrier.
- `CA-D-344@21`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-344@21`
  - Remaining Claim prose:
    for the CAPRMEDIO Main Skill, the Host Invocation **must** serialize as `$ca` **in** Codex; **if** a Claude compatibility Extension **or** Operator-provided compatibility layer is separately authorized by the Operator, **then** its Host Invocation **must** serialize as `/ca` **in** Claude.
- `CA-D-397@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-397@24`
  - Remaining Claim prose:
    the following fixed lowercase prefixes **must** be registered **only** for the listed Type values under Artifact; Atom identities use class short names instead.
    
    | Artifact form | Type | Prefix |
    |---|---|---|
    | `projection` | `catalog` | `catl` |
    | `projection` | `map` | `maps` |
    | `projection` | `hub` | `hubs` |
    | `projection` | `implementation_record` | `irec` |
- `CA-D-453@19`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-453@19`
  - Remaining Claim prose:
    **if** the CAPRMEDIO Project's versionless Project Scope Unit Graph Sources Projection is retained as historical migration evidence, **then** it **must** reside at `.caprmedio_caprmedio/_projection/project_scope_unit_graph_sources.projection.toml`.
- `CA-D-454@19`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-454@19`
  - Remaining Claim prose:
    **if** the CAPRMEDIO Project's versionless Project Scope Unit Graph Projection is retained as historical migration evidence, **then** it **must** use its centralized Carrier location at `.caprmedio_caprmedio/_projection/project_scope_unit_graph.projection.toml`.
- `CA-D-496@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-496@24`
  - Remaining Claim prose:
    the Run **must** store its temporary evidence under **`=1`** caller-admitted directory using this layout:
    
    - `progress.json`: the original selection, per-Atom path **and** identity, current Step, state, report path, assigned worker, applicable context setting, **and** any blocked **or** unfinished work. a short handoff records the current Atom, completed edits, **and** next work **in** this file.
    - `reports/<ordinal>.json`: **`=1`** report per selected Carrier, using its fixed four-digit ordinal. retain the check result **and** later applied corrections **in** this same file.
    
    **every** report **must** contain the source path, carried Atom ID **and** Version, source observation, **all** **`=6`** local check outcomes, concise evidence, confirmed findings, unresolved coverage, applied corrections, **and** current state. a confirmed finding includes its location, source passage, applicable rule, **and** proposed fix. record the original checked source digest once so the fixer can notice concurrent changes.
- `CA-D-497@18`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-497@18`
  - Remaining Claim prose:
    RMED review batch limits **must** use these TOML parameters:
    
    | Parameter | Encoding |
    |---|---|
    | `rmed_review.context_headroom_fraction` | finite TOML number strictly between zero **and** one; fraction of each worker's effective context capacity reserved rather than planned for use |
    | `rmed_review.max_atoms` | optional positive integer; an explicit cap on selected Atoms, with no default **when** omitted |
    
    resolve **every** parameter independently from explicit Operator Run input, **then** Framework Instance Settings, **then** Default Settings. report the selected value **and** source; do **not** silently coerce invalid values **or** store the same default **in** prompt text as independent authority.
- `CA-D-581@14`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-D-581@14`
  - Remaining Claim prose:
    a project-owned Analysis Atom with `type: FPF Analysis Report` **must** serialize its Type filename component as `FPF_ANALYSIS_REPORT` within the filename grammar governed by CA-D-283 and CA-D-284.
- `CA-R-1174@24`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1174@24`
  - Remaining Claim prose:
    CORE_META_MODEL **must** provide the minimal self-applicable canonical model necessary **and** sufficient **to** represent, govern, validate, **and** compile CAPRMEDIO Methodology authority.
- `CA-R-1175@23`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1175@23`
  - Remaining Claim prose:
    INSTALLED_EXTENSIONS **must** preserve exact installed Extension source revisions **and** their provenance as immutable candidate inputs **to** methodology compilation **without** activating **or** modifying them.
- `CA-R-1176@26`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-1176@26`
  - Remaining Claim prose:
    PROJECT_CONFIGURATION **must** state Project-owned Customizations **and** composition decisions that select CORE_META_MODEL **and** PROJECT_CONFIGURATION for Applicable Methodology compilation.
- `CA-M-445@2`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-M-445@2`
  - Semantics:
    Readable model language includes technical Subjects. Technical key spelling belongs to the file-adapter Method; Carrier fields and encodings remain governed by Delivery authority. The choice of presentation does not change the identified concept or its permitted values.
  - Remaining Claim prose:
    **when** writing model concepts in Subjects, Formal claims **or** authored model text, the Author **must** use their governed readable model names. For example, name the applicable model concepts:
    
    - Content Role;
    - Local Scope Unit; **and**
    - Updated At.
    
    **when** explaining an encoding, show the exact technical spelling as a Carrier key **or** serialization example. Preserve each canonical model name **and** do **not** invent aliases through stylistic changes.
- `CA-R-2468@2`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-2468@2`
  - Remaining Claim prose:
    Declaration is a Requirement Form.
    
    Its Claim uses:
    
    - CFEL for expressible constraints.
    - Prose for the remaining constraints.
    
    A Primary Node has brief Semantics. A Property has none.
    
    A Property Declaration specifies:
    
    1. Property occurrence, where constrained.
    2. Allowed value Format.
    3. Value cardinality.
    4. Dependent-name Format.
    5. Dependent-name cardinality.
    
    An unchanged inherited Property keeps its original Declaration. An explicit local MODEL override selects its effective replacement.
- `CA-R-2483@2`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-2483@2`
  - Remaining Claim prose:
    CAPRMEDIO's PROJECT STRUCTURE has:
    
    - Scope Structure.
    - Aspects.
    - Other declared components.
    
    Its Scope Structure retains the proposed ordered Units:
    
    1. META_MODEL.
    2. ENGINE.
    3. CORE EXTENSIONS.
    4. DOCUMENTATION.
    
    Its Core Meta-Model Unit contains the Atoms defining MODEL//CAPRMEDIO, including the Declarations for MODEL and PROJECT STRUCTURE. The MODEL and its defining Scope Unit have separate identities.
    
    Each constrained Unit's formal Scope is declared outside that Unit. It states permitted active and passive Subjects, Relations, endpoints and cardinalities.
    
    CAPRMEDIO's PROJECT STRUCTURE records ENGINE's base formal Scope:
    
    - Implementation RMED uses ENGINE's declared implementation Subjects.
    - Instance creation follows that Scope's permissions.
    - ENGINE references metamodel Declarations only through passive Subjects.
    - Active metamodel definitions use the declared model-defining Scope.
    - A local MODEL changes ENGINE's Scope only through an explicit Scope-contract replacement.
    
    Declared Unit order governs this Scope Structure.
- `CA-R-2484@2`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-2484@2`
  - Remaining Claim prose:
    Container is a classification whose admitted value cases are yes and no:
    The yes case permits the Node to be the whole endpoint of CONTAINS, subject to its effective Relation whitelist and cardinalities. It does not by itself require a part. The no case forbids that endpoint role. Whether a part may belong to a whole is distinct from whether that part may itself have parts.
    
    Use `Node// >| Container = yes` when selecting eligible whole instances. Container is not a required Boolean Property authored on every instance. This Draft does not assign an implicit default or require a classification annotation for every Node.
  - Fenced Claim block:
```CFEL
Node >| Container: yes;
Node >| Container: no
```
  - Unresolved CFEL: `Node >| Container: yes`
  - Unresolved CFEL: `Node >| Container: no`
- `CA-R-2452@2`: Active Subject has no exact declared target in this selection.
- Unbound source evidence: `CA-R-2452@2`
  - Remaining Claim prose:
    The caprmedio Project **must** create **and** evolve a working CAPRMEDIO Framework. Given enough resources, that Framework **must** let **any** Operator use AI Agents **to** do **all** of the following for **any** feasible Project:
    
    - create the Project;
    - deliver the Project;
    - run the Project; **and**
    - maintain the Project.
- Duplicate primary_node Declaration `CFEL`: CA-R-2244@3, CA-R-2487@2
- Relation `((DERIVED_FROM))` lacks Semantics: `CA-R-1639@35`
- Relation `((HAS_ACTIVE_SUBJECT))` lacks Semantics: `CA-R-2479@2`
- Relation `((HAS_CLASSIFICATION))` lacks Semantics: `CA-R-2477@2`
- Relation `((HAS_EVENT_AUTHOR))` lacks Semantics: `CA-R-2583@2`
- Relation `((HAS_INVERSE))` lacks Semantics: `CA-R-2485@2`
- Relation `((INSTANCE_OF))` lacks Semantics: `CA-R-2476@2`
- Relation `((IS_ALLOWED_VALUE_OF))` lacks Semantics: `CA-R-1436@25`
- Relation `((IS_CONTAINED_BY))` lacks Semantics: `CA-R-2478@2`
- Relation `((IS_PROPERTY_OF))` lacks Semantics: `CA-R-2473@2`
- Relation `((NARROWER_THAN))` lacks Semantics: `CA-R-2475@2`
- Relation `((RUN))` lacks Semantics: `CA-R-2480@2`
- Relation `((depends_on))` lacks Semantics: `CA-R-1026@30`
- `CA-R-2462@2`: IF ((Node, Node.**) {=0}((IS_PROPERTY_OF)))
THEN ((Node, Node.**) >| (Independence == Primary Node))
- `CA-R-2462@2`: IF ((Node, Node.**) {=1}((IS_PROPERTY_OF)))
THEN ((Node, Node.**) >| (Independence == Property))
AND ((Node, Node.**) {==0}((HAS_NARROWER)))
AND ((Node, Node.**) {==0}((HAS_INSTANCE)))
- `CA-R-2463@2`: Atom/(.Role: Operations)
- `CA-R-2464@2`: Atom/(.Role: Operations)/Workflow
- `CA-R-2465@2`: Atom/(.Role: Operations)/Step
- `CA-R-2465@2`: ((Step//{:1+}((CONTAINS)) Substep//)
AND (Step//{:0}((RUN)) Action//))
OR
((Step//{:0}((CONTAINS)) Substep//)
AND (Step//{:1}((RUN)) Action//))
- `CA-R-2466@2`: Atom/(.Role: Operations)/Substep
- `CA-R-2467@2`: Atom/(.Role: Operations)/Action
- `CA-R-2477@2`: (Node, Node/**, .**) >| Axis
- `CA-R-2489@2`: Atom//$atom.Updated At == MAX(Event Record//(.object_output{=1}, .object_output.version{=1}, .object_output.id = $atom.ID, .object_output.version = $atom.Version, (.action = create OR .action = update)).happened_at)
- `CA-R-2493@2`: IF ((Atom.Status >| Status Group = Current) OR (Atom.Status >| Status Group = Archived))
THEN (IMMUTABLE(Atom.ID))
- `CA-R-2496@2`: Atom.Version >= 1
- `CA-R-2497@2`: Atom.Label ?= Atom.Form
- `CA-R-2499@2`: DETERMINES(
  Atom//,
  (.ID),
  (.Content.Summary),
  (Atom.Status >| Status Group = Current) OR (Atom.Status >| Status Group = Archived)
)
- `CA-R-2500@2`: Atom/(.Role in RMED).Content.Claim{:1}: [markdown]{:1}
- `CA-R-2500@2`: Atom/(.Role in RMED).Content.Claim.*[]{:0}
- `CA-R-2500@2`: FENCED_LABELS(Atom/(.Role in RMED).Content.Claim): [in (CFEL)]{:0..1}
- `CA-R-2501@2`: Atom/(.Role in RMED).Content.Claim Scope{:0..1}: [markdown]{:1}
- `CA-R-2501@2`: Atom/(.Role in RMED).Content.Claim Scope.*[]{:0}
- `CA-R-2502@2`: Atom/(.Role in RMED).Content.Semantics{:0..1}: [markdown]{:1}
- `CA-R-2502@2`: Atom/(.Role in RMED).Content.Semantics.*[]{:0}
- `CA-R-2503@2`: Atom/(.Role in RMED).Content.Details{:0..1}: [markdown]{:1}
- `CA-R-2503@2`: Atom/(.Role in RMED).Content.Details.*[string]{:0+}
- `CA-R-2504@2`: Atom.Tier >= -1
- `CA-R-2505@2`: IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 0)) THEN (Atom.Tier.Label == Scope Contract)
- `CA-R-2505@2`: IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 1)) THEN (Atom.Tier.Label == Core)
- `CA-R-2505@2`: IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 2)) THEN (Atom.Tier.Label == General)
- `CA-R-2505@2`: IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 3)) THEN (Atom.Tier.Label == Standard)
- `CA-R-2505@2`: IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 4)) THEN (Atom.Tier.Label == Detail)
- `CA-R-2506@2`: COUNT(Atom.Subjects.Passive: $) = COUNT(DISTINCT Atom.Subjects.Passive: $)
- `CA-R-2508@2`: Atom
- `CA-R-2508@2`: UNIQUE(Atom//, (.ID, .Version))
- `CA-R-2509@2`: Atom/(.Role: Concern)
- `CA-R-2510@2`: Atom/(.Role: Analysis)
- `CA-R-2511@2`: Atom/(.Role: Plan)
- `CA-R-2511@2`: IF ((Atom/(.Role: Plan).Status = Active) AND (Atom/(.Role: Plan).Work Sequence Number{=1}))
THEN (Atom/(.Role: Plan).Relations.contained_by{==1})
- `CA-R-2512@2`: Atom/(.Role: Requirement)
- `CA-R-2513@2`: Atom/(.Role: Method)
- `CA-R-2514@2`: Atom/(.Role: Evaluation)
- `CA-R-2515@2`: Atom/(.Role: Delivery)
- `CA-R-2516@2`: Atom/(.Role: Requirement)/(.Form: Declaration)
- `CA-R-2517@2`: Atom/(.Role: Requirement)/(.Form: Relation Definition)
- `CA-R-2518@2`: Atom/(.Role: Concern).Priority{:1}: [string]{:1}
- `CA-R-2518@2`: Atom/(.Role: Concern).Priority.*[]{:0}
- `CA-R-2518@2`: Atom/(.Role: Concern).Priority: High
- `CA-R-2518@2`: Atom/(.Role: Concern).Priority: Medium
- `CA-R-2518@2`: Atom/(.Role: Concern).Priority: Low
- `CA-R-2519@2`: Atom/(.Role: Plan).AI Agent Confidence Threshold{:0..1}: [int]{:1}
- `CA-R-2519@2`: Atom/(.Role: Plan).AI Agent Confidence Threshold.*[]{:0}
- `CA-R-2519@2`: Atom/(.Role: Plan).AI Agent Confidence Threshold
  ?= LOOKUP(IS_CONTAINED_BY, Atom/(.Role: Plan).AI Agent Confidence Threshold)
  ?= Scope Unit/Project//$project.Settings.AI Agent Confidence Threshold
- `CA-R-2520@2`: Atom/(.Role: Plan).Work Sequence Number{:0..1}: [int]{:1}
- `CA-R-2520@2`: Atom/(.Role: Plan).Work Sequence Number.*[]{:0}
- `CA-R-2520@2`: IF (Atom/(.Role: Plan).Work Sequence Number{=1})
THEN (Atom/(.Role: Plan).Work Sequence Number > 0)
- `CA-R-2520@2`: UNIQUE(
  Atom/(.Role: Plan)//,
  (.Relations.contained_by.atom, .Work Sequence Number),
  (.Status = Active) AND (.Work Sequence Number{=1}) AND (.Relations.contained_by.atom{=1})
)
- `CA-R-2520@2`: UNIQUE(
  Atom/(.Role: Plan)//,
  (.Relations.contained_by.scope_unit, .Work Sequence Number),
  (.Status = Active) AND (.Work Sequence Number{=1}) AND (.Relations.contained_by.scope_unit{=1})
)
- `CA-R-2521@2`: Atom/(.Role: Operations)/Action.Execution Kind{:1}: [string]{:1}
- `CA-R-2521@2`: Atom/(.Role: Operations)/Action.Execution Kind.*[]{:0}
- `CA-R-2521@2`: Atom/(.Role: Operations)/Action.Execution Kind: Programmatic
- `CA-R-2521@2`: Atom/(.Role: Operations)/Action.Execution Kind: Agentic
- `CA-R-2522@2`: Atom/(.Role: Requirement)/(.Form: Relation Definition).Content.notation_for_subject{:0..1}: [string]{:1}
- `CA-R-2522@2`: Atom/(.Role: Requirement)/(.Form: Relation Definition).Content.notation_for_subject.*[]{:0}
- `CA-R-2523@2`: IF (Scope Unit//$unit not in (Scope Unit/Project//))
THEN ($unit {==1}((IS_CONTAINED_BY)) Scope Unit//)
- `CA-R-2524@2`: Scope Unit/Project
- `CA-R-2525@2`: IF (Package//$package not in (Package/Implementation//))
THEN ($package {==1}((IS_CONTAINED_BY)) Package//)
- `CA-R-2537@2`: DETERMINES(Projection//, (.Form, .Source.Named Selection), (.ID))
- `CA-R-2537@2`: DETERMINES(Projection//, (.ID), (.Form, .Source.Named Selection))
- `CA-R-2539@2`: Projection//$projection.Updated At == MAX(Event Record//(.object_output{=1}, .object_output.version{=0}, .object_output.id = $projection.ID, (.action = create OR .action = update)).happened_at)
- `CA-R-2542@2`: Actor
- `CA-R-2543@2`: Aspect
- `CA-R-2546@2`: IF (Atom.Status >| Status Group = Current)
THEN (Atom.Subjects.Active{==1})
- `CA-R-2553@2`: Package/Implementation
- `CA-R-2554@2`: Scope Unit.structural_level >= 0
- `CA-R-2554@2`: Scope Unit/Project//$project.structural_level = 0
- `CA-R-2554@2`: IF (Scope Unit//$contained ((IS_CONTAINED_BY)) Scope Unit//$container)
THEN ($contained.structural_level = $container.structural_level + 1)
- `CA-R-2555@2`: Package.structural_level >= 0
- `CA-R-2555@2`: Package/Implementation//$implementation.structural_level = 0
- `CA-R-2555@2`: IF (Package//$contained ((IS_CONTAINED_BY)) Package//$container)
THEN ($contained.structural_level = $container.structural_level + 1)
- `CA-R-2558@2`: UNIQUE(Event Record//, (.ID))
- `CA-R-2589@2`: Node/Continuant
- `CA-R-2590@2`: Node/Occurrent
- `CA-D-664@2`: Atom >> @Carrier//Markdown file
- `CA-D-664@2`: Atom.**!(.Content, .Content.**) >> @Carrier//Markdown file.frontmatter
- `CA-D-664@2`: Atom.Content.** >> @Carrier//Markdown file.markdown
- `CA-D-664@2`: @Carrier//Markdown file.filename{:1}: [string]{:1}
- `CA-D-664@2`: @Carrier//Markdown file.location{:1}: [string]{:1}
- `CA-D-664@2`: @Carrier//Markdown file.frontmatter.author{:0}
- `CA-R-2472@2`: CFEL fence is outside Claim; its contents were not interpreted.
- `CA-R-2472@2`: CFEL fence is outside Claim; its contents were not interpreted.
- `CA-R-2549@2`: CFEL fence is outside Claim; its contents were not interpreted.
- `CA-R-2550@2`: CFEL fence is outside Claim; its contents were not interpreted.
- `CA-R-2550@2`: p ?= expression
- `CA-R-2552@2`: CFEL fence is outside Claim; its contents were not interpreted.
- `CA-R-2585@2`: CFEL fence is outside Claim; its contents were not interpreted.
- `CA-R-2588@2`: CFEL fence is outside Claim; its contents were not interpreted.
- `CA-R-2588@2`: CFEL fence is outside Claim; its contents were not interpreted.
- `CA-R-2588@2`: CFEL fence is outside Claim; its contents were not interpreted.
- `CA-D-665@2`: Projection// >> Carrier/Markdown_file//
- `CA-D-662@2`: Atom.Role >> @Carrier//Markdown file.frontmatter.role
- `CA-D-662@2`: Atom.Form >> @Carrier//Markdown file.frontmatter.form
- `CA-D-662@2`: Atom.Subjects.Active >> @Carrier//Markdown file.frontmatter.subjects.active
- `CA-D-662@2`: Atom.Subjects.Passive >> @Carrier//Markdown file.frontmatter.subjects.passive
- `CA-D-662@2`: Atom.Relations >> @Carrier//Markdown file.frontmatter.relations
- `CA-R-2484@2`: Node >| Container: yes
- `CA-R-2484@2`: Node >| Container: no
- Narrowing evidence: Event Record: no explicit NARROWER_THAN parent; rendered as a root.
