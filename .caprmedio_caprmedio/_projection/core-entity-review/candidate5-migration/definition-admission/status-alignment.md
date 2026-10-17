# Candidate #6 — minimal Status source alignment

Status: review proposals only. No source edit, retirement, ID allocation, activation or MCP mutation.

Reviewed: 2026-10-16 against Candidate #6 decisions 1–31 and `candidate6-definition-drafts.md`. This lane covers the Status definition's admission blockers, not every legacy Status reference or the other 44 definition drafts.

## Accepted basis

Atom.Status admits Draft, Active and Archived. Narrower Atom kinds inherit these values and may add values. Inherited values do not need separate declarations for every descendant. This does not choose or change any existing Atom's Status, invent transitions, or make every non-Active Atom archived.

The proposed base definition is `../empty-r-drafts/CA-R--CORE_META_MODEL--define-atom-status-allowed-values.md`. Its admission needs the conflicting exact domains below aligned; it does not require rewriting compatible cardinality and domain rules. The current rule-alignment request includes governing Rs about Analysis/Concern. The deferred C/A work is migration of C/A Atom content and carriers, not these governing-R repairs; C/A instances remain unchanged.

All source paths in the table are relative to:

`.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/`

## Source inventory

| Source | Current Version | Exact basename | Disposition |
| --- | --- | --- | --- |
| CA-R-1539 | 6 | `CA-R-1539-CORE_META_MODEL-GENERAL--register-core-plan-status-values.md` | Required: exact Plan domain excludes Draft |
| CA-R-1875 | 3 | `CA-R-1875-CORE_META_MODEL-GENERAL-REQUIREMENT--register-core-analysis-status-values.md` | Required governing-R alignment; exact Analysis domain excludes Active; C/A instances unchanged |
| CA-R-1608 | 5 | `CA-R-1608-CORE_META_MODEL-GENERAL-REQUIREMENT--register-core-concern-status-values.md` | Required governing-R alignment; exact Concern domain excludes Archived and uses old lowercase value spellings; C/A instances unchanged |
| CA-R-1727 | 17 | `CA-R-1727-CORE_META_MODEL-CORE-REQUIREMENT--analyses-have-draft-and-done-states.md` | Required governing-R alignment; unfinished/complete wording assigns an exhaustive two-state model; C/A instances unchanged |
| CA-R-1308 | 12 | `CA-R-1308-CORE_META_MODEL-CORE-REQUIREMENT--resolve-status-domains-from-complete-qualified-paths.md` | Narrow clarification of inherited values during qualified resolution |
| CA-R-1412 | 11 | `CA-R-1412-CORE_META_MODEL-CORE--give-every-atom-revision-one-status.md` | Compatible cardinality; no admission patch |
| CA-R-1309 | 14 | `CA-R-1309-CORE_META_MODEL-GENERAL-REQUIREMENT--register-core-requirement-status-values.md` | Compatible Requirement domain; no admission patch |
| CA-R-1397 | 11 | `CA-R-1397-CORE_META_MODEL-GENERAL--register-core-method-status-values.md` | Compatible Method domain; no admission patch |
| CA-R-1398 | 11 | `CA-R-1398-CORE_META_MODEL-GENERAL--register-core-evaluation-status-values.md` | Compatible Evaluation domain; no admission patch |
| CA-R-1399 | 11 | `CA-R-1399-CORE_META_MODEL-GENERAL--register-core-delivery-status-values.md` | Compatible Delivery domain; no admission patch |
| CA-R-1874 | 3 | `CA-R-1874-CORE_META_MODEL-GENERAL-REQUIREMENT--register-core-operations-status-values.md` | Compatible Operations base domain; other old wording deferred |
| CA-R-1313 | 13 | `CA-R-1313-CORE_META_MODEL-CORE-REQUIREMENT--keep-qualified-status-domains-open.md` | Already permits qualified additions; no admission patch |
| CA-R-1306 | 13 | `CA-R-1306-CORE_META_MODEL-CORE-REQUIREMENT--define-status-as-an-artifact-revision-property.md` | Cross-lane dependency: Revision alignment proposal owns its Artifact Revision property conflict |
| CA-R-1312 | 16 | `CA-R-1312-CORE_META_MODEL-CORE--separate-governed-transitions-from-status-values.md` | Compatible distinction between a value and the operation establishing it |

Versions are observed evidence, not permanently fixed tool pins. Re-read affected originals before applying any proposal.

## Exact proposals

Only the replacements explicitly shown below are proposed. Keep existing Summary, Subjects, Scope, Details, relations and other metadata unless a section explicitly says otherwise. Normal applied-update Version/Updated At handling is outside this review file.

### CA-R-1539 — add Plan values to the inherited base

Evidence: current Claim says the Core Plan values are **exactly** `(Active, Backlog, Done, Canceled, Archived)`, excluding inherited Draft.

Subject remains `Entity/Continuant/Object/Atom/Content Role: Plan.Status`.

Replace Claim with:

> the Core Plan Status model **must** inherit the allowed values of Atom.Status and add (Backlog, Done, Canceled). Planned **must not** be a distinct Plan Status.

No Scope or Details replacement. This keeps the existing registered Plan-domain claim, including the prohibition of a separate Planned value; it does not redefine Plan or its completion criteria.

### CA-R-1875 — preserve Done and inherit Active

Required governing-R alignment within the current request; C/A instances unchanged.

Evidence: current Claim declares **exactly** `(Draft, Done, Archived)` and permits a more-specific domain. The exact set excludes inherited Active.

Subject remains `Entity/Continuant/Object/Atom/Content Role: Analysis.Status`.

Replace Claim with:

> the Core Analysis Status model **must** inherit the allowed values of Atom.Status and add Done. That Content Role Status model applies to Analysis Atoms with Type Analysis Report or Rationale. An admitted Extension or Project Configuration **may** add values under the applicable complete Content Role and Type path; it **must not** remove inherited values.

Replace Details with:

> this Status belongs to the Analysis Atom itself. It does **not** define a Status transition, carrier placement, setting, or a Workflow, Step, or Action Run outcome, receipt, retry state, result, or completion state. CA-R-1727 defines the meanings of Draft and Done for Analysis and the meaning of its archival.

Scope remains the existing default Analysis Report/Rationale domain. The Details replacement removes the old assertion that this is an Artifact Revision Property and updates the R1727 reference without creating a separate Analysis lifecycle procedure.

### CA-R-1608 — inherit the base and retain Concern additions

Required governing-R alignment within the current request; C/A instances unchanged.

Evidence: current Claim requires **exactly** lowercase `(draft, active, resolved, canceled)`. It omits Archived. The accepted base uses Draft, Active, Archived; the accepted Concern additions are Resolved and Canceled.

Subject remains `Entity/Continuant/Object/Atom/Content Role: Concern.Status`.

Replace Scope with:

> the Core Concern Status model.

Replace Claim with:

> the Core Concern Status model **must** inherit the allowed values of Atom.Status and add (Resolved, Canceled).

No Details replacement. These are model value names, not an instruction to rewrite existing Concern carriers or change their Status. YAML spelling/serialization and current C/A content migration remain outside this packet.

### CA-R-1727 — keep meanings without requiring only Draft or Done

Required governing-R alignment within the current request; C/A instances unchanged.

Evidence: current Claim says an admitted Analysis **is** draft while unfinished and done when complete. Read literally, this assigns one of those statuses to every admitted Analysis despite the inherited Active value. Merely adding Active to R1875 leaves this constraint behind.

Subject remains `Entity/Continuant/Object/Atom/Content Role: Analysis.Status`.

Replace Scope with:

> Draft, Done and archival meanings for admitted Analyses and their bounded inquiry or interpretation products.

Replace Claim with:

> Draft on an Analysis **means** its bounded inquiry or interpretation product remains unfinished. Done on an Analysis **means** that product is complete. A Done Analysis remains a factual record of its completed reasoning rather than current normative authority; archival preserves one that is obsolete, invalidated, duplicated, or absorbed.

No Details replacement. This retains the existing meanings of Draft, Done and archival, but no longer requires every unfinished/complete Analysis to use only the two listed values. It does not define new semantics for Active or give Analyses normative authority.

### CA-R-1308 — qualify resolution without suppressing inheritance

Evidence: current Claim says a global Status domain must not override the domain resolved from the complete qualified path. It does **not** explicitly prohibit inheritance. It is therefore not grounds for wholesale replacement or retirement.

Leave Subject, Scope and Claim unchanged in this narrow packet. Replace its currently empty Details with:

> for Atoms, resolution from the complete qualified Content Role and Type path includes the allowed values inherited from Atom.Status and the additional values admitted for that path. Inheritance does **not** replace the qualified model with a flat global domain or remove its additions. A narrower Atom kind **must not** remove inherited Status values.

This clarifies how the approved base participates in the existing resolution rule. Its old Artifact/Type Subjects are a separate Terms/owner-specific mapping issue; do not substitute a generic Term or broaden Atom.Status to non-Atom kinds merely to clean them up here.

## Identity and history treatment

The five proposals above evolve the same respective claims: registering the role's Status model, defining Analysis Status meanings, and resolving qualified domains. Preserve their current Summaries and Atom IDs; applied changes would each receive the normal next Version, with the previous version preserved by the existing update workflow. No new ID or source retirement is proposed solely because an allowed domain changes.

If an implementation instead rewrites CA-R-1306 into an Atom-only definition, changes a Summary, or repurposes any source to an unrelated claim, that is not this proposal. It needs the appropriate new-ID/replacement treatment and preservation of its still-valid scope. Do not allocate such IDs here.

## No-change evidence and later work

- CA-R-1412 already requires exactly one Status. That is compatible with inheritance; its old “Atom Revision” wording is not a missing allowed-value definition and does not justify replacing its Summary during this packet.
- CA-R-1309 and CA-R-1397–1399 already declare the same three base values for their roles. Duplication may be simplified later, but it does not contradict the proposed base. Do not retarget those role-specific rules to every Atom.
- CA-R-1874 already includes Draft, Active and Archived. Its legacy Operations Type Actor and Artifact Revision wording remain separate content work; inherited values are not a reason to recreate the Operations model now.
- CA-R-1313 already permits qualified additions. Its old Artifact terminology and qualification wording do not require another extension/configuration authorization mechanism. Leave its transition reference alone here; this packet does not define transitions.
- CA-R-1306 defines the old shared Status term through Artifact Revision. The parallel Revision-alignment proposal owns this source conflict; this Status proposal must be integrated with that result and supplies no competing replacement. Do not create a separate authoritative Terms-definition layer to resolve it.
- CA-R-1312 separates a Status value from the Action/Workflow establishing it. Preserve that distinction; its old Artifact wording can be aligned later.
- Current C/A Atoms, their statuses and their contents are untouched. R1875/R1727/R1608 are Requirement sources about those roles; aligning these schemas does not itself migrate C/A carriers.
- Existing untyped `relates_to` fields are not converted or removed in this Status admission proposal. Their separate typed-relation cleanup must not be silently bundled in.
- This review does not admit the other definition drafts, repair collection/Revision/Carrier conflicts, validate runtime code, or claim every project Status rule has been audited.

## Remaining decision

No new Status-domain decision is needed: the proposals follow the accepted additive inheritance rule. R1875/R1608/R1727 are governing Requirement repairs included in the current alignment request; their governing C/A does not create an additional approval requirement. C/A Atom content, carriers and actual Status values remain untouched. The actual source-mutation route remains unexecuted and must not be represented as complete by this review file.
