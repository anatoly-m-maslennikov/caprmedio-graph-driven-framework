# Full proposal and Draft review — 2026-10-31

All three confirmed consistency defects were fixed after this review. The original findings below describe the reviewed snapshot. This is not an adoption verdict.

## Scope

- Full [A/Spec Proposal](../CA-A-draft-CORE_META_MODEL-SPEC_PROPOSAL--declare-node-branch-and-formal-graph-rules.md).
- All 98 registered Drafts: 69 Declarations (23 Primary, 46 Property) and 29 other Drafts.
- Latest decisions govern: Object is a Term meaning Node instance; `Node//` remains the instance notation. No Object classification or `Node//**` construct is introduced.
- Read-only source review. Only review evidence was written.

## Findings

1. **P2 — Remove the superseded branch selector from the proposal.** [Proposal](../CA-A-draft-CORE_META_MODEL-SPEC_PROPOSAL--declare-node-branch-and-formal-graph-rules.md), lines 49 and 53, still uses `Node/` as the root-inclusive branch selector. Line 39 and the governing CFEL Draft instead use `Node/**, .**`, adding `Node` for root coverage. A reader following the later text would use a superseded selector and miss the explicit Property expansion. Use `(Node, Node/**, .**)` in the affected root-inclusive statements.

2. **P2 — Replace the obsolete Property contract syntax.** [Proposal](../CA-A-draft-CORE_META_MODEL-SPEC_PROPOSAL--declare-node-branch-and-formal-graph-rules.md), line 54, still teaches `property[value domain]{value count}.[child condition]{child count}`. It conflicts with line 41 and the governing Property notation Draft. Use separate expressions: `p: [value format]{value count}; p.*[name format]{child count}`. Add `p{occurrence count}` where presence is constrained. Following the old expression would put value constraints in the wrong position and omit the explicit child-name selector.

3. **P2 — Include Substep in the Operations description.** [Operations Declaration](../../../04_requirement/draft/node-declaration-20261031/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-operations.md), line 29, lists Action, Workflow and Step as the reusable work an Operations Atom can define. The selected inventory also declares Substep as an Operations sibling. Add Substep so the description matches the declared model.

## Checks passed

- All 98 registered carriers exist; their hashes, Atom IDs and Draft status match the register.
- All local links checked in the Drafts and proposal resolve.
- All 69 Declaration Subjects are distinct.
- The full Declaration review found no further contradictions. Step alternatives remain exclusive. Inherited Properties are not redeclared. Property Declarations have no Semantics sections. The repaired Node classification conclusions cover the same selection as their conditions.
- All 750 snapshotted Current Core Requirement sources and Current Epic version 37 remain unchanged.

Register SHA-256: `8d14ad30e1b385325e7c8d1976f2e9c911c22239343247f4d16f9b6eba0a1ec1`.

## Adjudication

Filename/location Format and occurrence constraints are not filename/location formulas. The proposal may therefore correctly leave formula details unresolved.

The Markdown mapper's reference to preserving an existing Formal claim heading describes arbitrary/legacy Markdown ancestry; it does not require that heading in the new Claim contract. Replacing that example with an ordinary heading would improve clarity, but it is not a confirmed semantic contradiction.

## Existing adoption gaps

- Complete effective Relation whitelists and source-to-Declaration mappings.
- Exact Subject bindings and Author/Assignee/Target reference mappings.
- Remaining omitted-domain and Markdown normalization/retrieval decisions.
- Allocation of unique new Atom IDs before governed references are rebound.

These remain explicit open gates. This review does not establish readiness to promote the packet.

## Review lanes

| Deliverable | Owner | Edit scope | Dependency | Acceptance check | Status |
|---|---|---|---|---|---|
| 69 Declarations | Terra consistency reviewer | None | Registered packet | All bodies inspected; concrete evidence | done |
| Proposal and 29 other Drafts | Terra proposal reviewer | None | Registered packet | Decision alignment and cross-file consistency | done; findings adjudicated by root |
| Integrity and final report | Root | Review evidence only | Reviewer returns | Hashes, links, coverage and evidence | done |

No parser, runtime, actual-instance migration, promotion or Definition retirement was tested or performed. Structural checks alone do not prove CFEL implementation conformance.

## Resolution — 2026-10-31

1. Replaced both obsolete `Node/` selectors in the proposal with the root-inclusive `(Node, Node/**, .**)` scope.
2. Replaced the obsolete combined Property contract with separate occurrence, value and dependent-name expressions.
3. Added Substep to the Operations description.

Focused content checks passed. The 98-Draft structure check passed: 23 Primary Declarations, 46 Property Declarations, no incomplete selected Property contracts, no duplicate Declaration Subjects, and valid metadata, register hashes and local links. All 750 snapshotted Current Core Requirement sources and Current Epic version 37 remain unchanged.

Post-fix register SHA-256: `62886136c9e8ba4fced73908719e25b492038966e07915adaba129b02980ffac`.

The existing adoption gaps and runtime-check limits still apply.
