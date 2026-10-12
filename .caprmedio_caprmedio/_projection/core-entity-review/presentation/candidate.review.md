# CA-P-1908 candidate Entities Graph review

This is a **CANDIDATE** derived from the Operator-selected captured Core snapshot `a971d0e00c33c779f485fc8cad63194894d440fb`. It is not current-Core evidence, native admission, Operator acceptance, a Subject migration, a source change, or a completed Run. The next action is the CA-P-1909 Operator approval gate.

## Read first

- [Primary 706-identity candidate inventory](candidate.entities.indented.txt) is a two-space display tree. Every original identity appears once as an annotation; prefix labels support display only.
- The preserved, source-pinned details remain in [node-disposition ledger](../nodes/nodes.dispositions.json) and [occurrence-to-proposed-relation ledger](../nodes/relations.marked.ledger.json). Those files retain all reasons, five checks, source evidence, questions, effects, and non-native boundaries.
- The two pointer views remain shared rather than copied: [R/M/E/D role-centred tree](../design/rmed.roles.indented.txt), [Entity-centred pointer tree](../design/rmed.entities.indented.txt), and [machine-readable RMED view](../design/rmed.views.json). GOVERNS and DEPENDS_ON are separate; M/E/D associations are not proven applicability.

## Before and candidate accounting

| Measure | Value |
| --- | ---: |
| Original identities retained in primary inventory | 706 |
| Before literal syntactic roots | 346 |
| Before standalone roots | 293 |
| Continuant display members | 17 |
| Occurrent display members | 3 |
| Broad non-temporal model anchors | 4 |
| Explicitly unclassified identities | 682 |
| Rendered top-level display labels | 359 |
| Retain marks | 584 |
| Consolidate candidates | 3 |
| Generalize candidates | 2 |
| Questions retained | 117 |
| Unresolved drop annotations | 2 |

The rendered-label count is a display calculation from the explicit crosswalk, not a candidate literal-root count or a claim of independent ontology roots. Continuant and Occurrent are local display lenses, not BFO adoption or taxonomy admission.

## Compact notation and boundaries

`/` presents broader-to-narrower only where a separately evidenced display decision says so (canonical direction would be narrower-to-broader); `.` presents bearer qualification; `:` presents an allowed value; `@` is a carrier binding only where separately evidenced. A `LEGACY RELATION UNRESOLVED` path preserves old syntax without classifying it. Display formatting does not serialize Subjects or admit a relation; a retained node does not approve a relation. Entity and Term graph ownership stay distinct: the ten `/` proposals below are Term-graph candidates only.

## Candidate marks requiring an Operator decision

- `Applicable Methodology` — **GENERALIZE CANDIDATE** (95%): display target: `Projection`; broad Operator direction to consider Applicable Methodology under Projection; no exact source selects this display mapping; risk retained: Treating the compiled Projection as its source collection would erase non-authoritativeness, selection provenance, and source/member boundaries.
- `Artifact/Revision` — **CONSOLIDATE CANDIDATE** (95%): display target: `Revision`; broad Operator Revision review direction; no exact source selects this family consolidation; risk retained: A flat merge could erase the Artifact semantic-state/lifecycle distinction or falsely project Atom-only Version/Updated At constraints onto Artifact Revisions.
- `Atom/Revision` — **CONSOLIDATE CANDIDATE** (95%): display target: `Revision`; broad Operator Revision review direction; no exact source selects this family consolidation; risk retained: A generic merge could erase author, status, lineage, history-entry, carrier-bundle, version, and timestamp evidence.
- `Claim` — **GENERALIZE CANDIDATE** (95%): display target: `Substance`; later Substance direction informs a reviewer-proposed display umbrella; the captured Core does not select a rename; risk retained: A direct rename could collapse registered role headings, Claim Target Scope Unit references, or required Plan/Analysis sections.
- `Journal/Revision` — **CONSOLIDATE CANDIDATE** (95%): display target: `Revision`; broad Operator Revision review direction; no exact source selects this family consolidation; risk retained: Merging it with Artifact/Revision would falsely treat Journal chronology as immutable governed meaning.

The two **DROP CANDIDATE unresolved** annotations remain questions for `Applicable Methodology Revision` and `Projection/Revision`; neither identity is deleted. All 117 questions retain a null semantic proposal and their specific question in the node-disposition ledger.

## Conditional inherited constraints — display only

- `entity-identity-and-bearer` — applies when: The current governing Entity definition applies. Rule: Preserve independently identified versus bearer-qualified Entity identity. A Dependent Entity requires exactly one immediate bearer; a Property represents one characteristic of its bearer. Do not turn this into a universal concrete IS_BORNE_BY fact.
- `non-ephemeral-carrier-obligation` — applies when: An Entity is non-ephemeral under applicable authority. Rule: Require at least one Carrier through that Entity/Carrier binding. A Shared Carrier and a location may satisfy the binding; being an Entity does not require a separate file.
- `atom-revision-bundle` — applies when: The node denotes an Atom Revision, including an admitted Role/Type specialization of Atom. Rule: Require exactly one authoritative Carrier Bundle with exactly one Markdown File Carrier and zero or more additional Carriers admitted by Delivery authority.
- `carrier-format-not-identity` — applies when: A Carrier Format or File Extension changes. Rule: That change alone does not establish or change the Entity Identity.
- `defaults-not-inherited-settings` — applies when: Applicable Delivery rules distinguish defaulted Atom Properties and externally inherited Settings. Rule: Carry required defaulted Property values; keep unselected optional overrides absent rather than copying an inherited effective Setting; preserve an explicitly selected override even if equal to the inherited value.
- `qualified-status-domains` — applies when: An Analysis or Plan Atom uses its applicable Status model. Rule: Keep the exact Role/Type domain. The default Analysis domain is Draft/Done/Archived and admits only a governed more-specific override under the exact path; the Core Plan domain is Active/Backlog/Done/Canceled/Archived, without Planned.
- `definition-view-run-separation` — applies when: Reusable operational definitions, information views and actual invocations are displayed together. Rule: Keep Action/Step/Workflow definitions, their actual Runs, generated views and Journal evidence distinct. Reference/reuse of a definition is not proof of an invocation or effect, and recording an attempt/failure is not successful completion.

These are conditional shared rules, not concrete Carrier inheritance, actual bindings, default Settings copies, or universal IS_BORNE_BY facts.

## Ten separately evidenced Term-taxonomy proposals

- `Entity` / `Primary Entity` — `/` display; canonical `NARROWER_THAN` `Primary Entity → Entity` (narrower→broader; terms candidate; not_performed).
- `Entity` / `Dependent Entity` — `/` display; canonical `NARROWER_THAN` `Dependent Entity → Entity` (narrower→broader; terms candidate; not_performed).
- `Primary Entity` / `Artifact` — `/` display; canonical `NARROWER_THAN` `Artifact → Primary Entity` (narrower→broader; terms candidate; not_performed).
- `Primary Entity` / `Actor` — `/` display; canonical `NARROWER_THAN` `Actor → Primary Entity` (narrower→broader; terms candidate; not_performed).
- `Primary Entity` / `Carrier` — `/` display; canonical `NARROWER_THAN` `Carrier → Primary Entity` (narrower→broader; terms candidate; not_performed).
- `Carrier` / `File Carrier` — `/` display; canonical `NARROWER_THAN` `File Carrier → Carrier` (narrower→broader; terms candidate; not_performed).
- `Carrier` / `Directory Carrier` — `/` display; canonical `NARROWER_THAN` `Directory Carrier → Carrier` (narrower→broader; terms candidate; not_performed).
- `Artifact` / `Atom` — `/` display; canonical `NARROWER_THAN` `Atom → Artifact` (narrower→broader; terms candidate; not_performed).
- `Dependent Entity` / `Property` — `/` display; canonical `NARROWER_THAN` `Property → Dependent Entity` (narrower→broader; terms candidate; not_performed).
- `Actor` / `Operator` — `/` display; canonical `NARROWER_THAN` `Operator → Actor` (narrower→broader; terms candidate; not_performed).

## Parallel RMED and Entity-centred pointer views

- **R** — model skeleton and required results: 524 GOVERNS pointers to 283 identities; 1535 DEPENDS_ON pointers to 226 identities.
- **M** — construction and authoring conventions; excludes Operations-specific actions and workflows: 59 GOVERNS pointers to 55 identities; 292 DEPENDS_ON pointers to 132 identities.
- **E** — checks and acceptance evidence: 77 GOVERNS pointers to 67 identities; 588 DEPENDS_ON pointers to 181 identities.
- **D** — Carrier model, formats, and placement or storage; a direct Delivery definition can also be a model-skeleton input: 145 GOVERNS pointers to 122 identities; 429 DEPENDS_ON pointers to 155 identities.

Across the shared view there are 805 GOVERNS and 2844 DEPENDS_ON pointers. Sources remain shared Claim/provenance records, not duplicate Entity nodes. R supplies model skeleton/required results, M construction conventions, E checks, and D Carrier/formats/placement; Operations and Concern remain outside RMED construction guidance.

## Content presentation direction

Candidate Atom body: `Substance`, `Substance Scope`, and optional `Details`. Role labels are `Claim` (RMED), `Objective` (Plan), `Question` (Analysis), `Issue` (Concern), and `Operation` (Operations). They are presentation labels, not new native kinds. An omitted Substance Scope means the full governed Subject **and** full owning Scope Unit only; otherwise Scope must remain explicit. It is applicability, not ownership. This Operator direction is separately pinned and is not retroactive Core evidence.

## Reproducibility and limits

Use [candidate.manifest.json](candidate.manifest.json) with `support/render_candidate.py --verify-output`. The manifest pins the exact accepted review inputs, captured snapshot, Scope decision, source context, producer, outputs, canonical candidate JSON, and the CA-P-1907/CA-P-1938 receipt commit. It does not rebind to current Core or infer a new root/taxonomy/Carrier relation.

**Approval gate:** no source, Subject, Core, native graph, runtime, or history change is authorized until the Operator accepts a separately reviewed candidate and a later exact migration preview.
