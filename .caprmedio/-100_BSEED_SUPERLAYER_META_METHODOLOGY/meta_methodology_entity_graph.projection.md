---
artifact_form: projection
artifact_type: map
projection_scope: META_METHODOLOGY
projection_mode: working_current
source_states:
  - active
  - draft
excluded_states:
  - archived
  - solved
source_count: 608
source_frontier_sha256: 046fc2d87dc97388d17c54165688b963b93dd34a5a59a5fa0b51a9bf91803f7e
generation_procedure: llm_inference_from_current_atom_claims
updated_at: 2026-08-25 03:57:11+0400
authority: non_authoritative
---
# META_METHODOLOGY Entity Graph

This Map is a non-authoritative working Projection of Entity bearer paths derived from the Project-owned META_METHODOLOGY Goal and current active and draft Atoms in META_METHODOLOGY, METAMODEL, SEMANTICS, and GOVERNANCE. `/` represents only bearer qualification. Classification, set membership, and structural relations are listed separately and do not create `/` edges.

## Bearer graph

```text
Artifact
├── Artifact Form
├── Artifact Identity
├── Carrier
│   ├── Format
│   └── Placement
└── Lifecycle

Atom
├── Project Atom ID
├── Current Scope
├── Claim
│   ├── Claim Scope
│   └── Subject
│       ├── Claim Role [active]
│       │   ├── Declared
│       │   └── Prerequisite
│       ├── Claim Participant Temporal Form [active]
│       │   ├── Continuant
│       │   └── Occurrent
│       ├── Claim-Subject Relation [draft]
│       │   ├── Governs
│       │   └── Depends On
│       ├── Subject Temporal Form [draft]
│       │   ├── Continuant
│       │   └── Occurrent
│       └── Subject Path [draft]
│           ├── Separator
│           ├── Terminal
│           └── Dependent Entity Term Position
├── Summary
├── Content Role
│   └── Spec Content Roles [draft]
│       ├── Evaluation
│       │   └── Evaluation Target Content Role [draft]
│       └── Status [draft]
│           ├── Draft
│           ├── Active
│           └── Archived
├── Type
├── Local Tier
│   ├── Principle
│   ├── Core
│   └── Standard
├── Version
├── Updated At
└── Carrier
    ├── Filename
    │   └── Summary Slug
    └── H1

Task
├── Task Scope
├── Task Goal
├── Definition of Done
├── Task Details
├── Task Scope Resolution
├── Task Dependency
├── Autonomous Confidence Threshold
├── Author
└── Assignee

Scope Unit
├── Scope
├── Goal
├── Unit Name
├── Scope Unit Type
├── Scope Unit Type Name
├── Structural Level
├── Navigational Order Number
├── Local Order
├── Child Composition
├── Project Boundary Position
├── Structural Parent
└── Previous Unit

Project
├── Goal
├── Project Name
├── Project Prefix
├── Project Configuration
└── Project Scope Unit Graph

Projection
├── Projection Element
├── Updated At
├── Generator
└── Source Frontier

Journal
└── Record
    ├── Event
    ├── Occurred At
    └── Result

CCE Language
├── CCE Operator
│   ├── CCE Operator Identity
│   └── CCE Operator Validation
└── Terminology
    ├── Term
    │   └── Term Identity
    └── Terminology Validation

Realization Graph
├── Carrier Face
├── Dependency Face
└── Relation
    └── Relation Derivation Class
        ├── Source Declared
        ├── Pre-runtime Resolved
        ├── Inferred Possible
        └── Runtime Observed

Project Graph
└── Node
```

## Non-bearer relations

| Source | Relation | Targets |
|---|---|---|
| Artifact Form | has members | Atom, Journal, Projection |
| Project Graph Node | has kinds | Scope Unit, Artifact |
| Content Role | has members | Concern, Analysis, Plan, Requirement, Method, Evaluation, Delivery, Implementation, Ops |
| Spec Content Roles | has members | Requirement, Method, Evaluation, Delivery |
| Scope Unit Type | has members | Layer, Feature |
| Child Composition | has values | None, Layers, Features, Mixed |
| Project Boundary Position | has values | Project, Bootstrap Seed |
| Claim Role | has values | Declared, Prerequisite |
| Claim-Subject Relation | has values | Governs, Depends On |
| Claim Participant Temporal Form | has values | Continuant, Occurrent |
| Subject Temporal Form | has values | Continuant, Occurrent |
| Status under Spec Content Roles | has values | Draft, Active, Archived |
| Evaluation Target Content Role | has values | Requirement, Method, Delivery |
| Evaluation Atom | is qualified by target role as | E_R for Requirement, E_M for Method, E_D for Delivery |
| Evaluation Atom | owns direct relation | `evaluation_for` to one or more Atoms of its one Evaluation Target Content Role |
| Local Tier | has values | Principle, Core, Standard |
| Relation Derivation Class | has values | Source Declared, Pre-runtime Resolved, Inferred Possible, Runtime Observed |

## Principal source bindings

| Graph branch | Principal source Atoms |
|---|---|
| Artifact and Artifact forms | `CAPRMEDIO-META-REQU-125`, `CA-R-655`, `CAPRMEDIO-META-REQU-656`, `CAPRMEDIO-META-REQU-657` |
| Atom identity, Claim, scope, Content Role, Type, tier, revision, and carrier | `CA-R-165`, `CA-R-728`, `CA-R-740`, `CA-R-918`, `CA-R-920`, `CA-R-921`, `CA-R-155`, `CA-R-356`, `CA-R-731`, `CA-R-811`, and the current Atom-boundary drafts |
| Active Subject model | `CA-R-1012`, `CA-R-1013`, `CA-R-1014`, `CA-R-1015`, `CA-R-1084` through `CA-R-1092` |
| Draft qualified Subject model | the current METAMODEL Subject, Subject Path, Claim-Subject Relation, Subject Temporal Form, and Dependent Entity Term position drafts |
| Spec Content Role Status branch | `CA-R--SEMNTC-CORE-REQUIREMENT--define-spec-content-roles` and the current qualified-Subject and composite-Claim evaluation drafts |
| Evaluation Target Content Role and qualified labels | `CA-R-1018` and the current META_METHODOLOGY drafts that register R, M, and D targets, require one shared target Content Role, and classify E_R, E_M, and E_D |
| Task | `CA-R-989`, `CA-R-1000` through `CA-R-1011`, `CA-R-1043` through `CA-R-1046`, and `CA-R-1078` through `CA-R-1083` |
| Scope Unit and Project | `CAPRMEDIO-META-REQU-708` through `CAPRMEDIO-META-REQU-720`, `CA-R-913`, `CA-R-960` through `CA-R-984`, `CA-R-1169` through `CA-R-1172`, and current Project Configuration authority |
| Projection and Journal | `CAPRMEDIO-META-REQU-166`, `CAPRMEDIO-META-REQU-656`, `CAPRMEDIO-META-REQU-657`, and current Projection and Journal governance |
| CCE Language | `CA-M-113`, `CA-M-114`, and the current CCE Language, CCE Operator, Terminology, and lexical evaluation drafts |
| Realization Graph | the current METAMODEL, SEMANTICS, and GOVERNANCE Realization Graph drafts |
| Project Graph Node kinds | `CA-R-834`, `CA-R-835`, `CA-R-836`, and `CA-R-837` |

## Current carrier coverage

| Layer | Active Atoms | Draft Atoms | Total |
|---|---:|---:|---:|
| CAPRMEDIO (META_METHODOLOGY Goal owner) | 1 | 0 | 1 |
| META_METHODOLOGY | 3 | 3 | 6 |
| METAMODEL | 125 | 39 | 164 |
| SEMANTICS | 135 | 27 | 162 |
| GOVERNANCE | 257 | 18 | 275 |
| Total | 521 | 87 | 608 |

All 608 source carriers still serialize Subjects through the active `declared/prerequisite` schema. No current source carrier serializes the draft canonical `governs/depends_on` Subject Path schema. The graph therefore derives bearer paths from Claims and records the active and draft Subject models separately; it does not reinterpret the existing flat Subject tokens as canonical paths.

## Current diagnostics

- The active `Claim Role` and `Claim Participant Temporal Form` branches coexist with their draft replacements, `Claim-Subject Relation` and `Subject Temporal Form`.
- The `Atom/Content Role/Spec Content Roles/Status/{Draft, Active, Archived}` branch is draft-only.
- Active `CA-R-1018` permits only Requirement and Method targets; its META_METHODOLOGY replacement draft adds Delivery targets.
- Active `CA-E-245` and `CA-E-246` mix Requirement and Method targets and must be split before the one-Target-Content-Role draft can become active.
- `Atom/Status` is not present because it skips the required bearer chain.
- `Draft` occurs only at position four after a Base Entity. A pair such as `Something1/Draft` and `Something2/Status/Draft` would violate the fixed Dependent Entity Term position rule.
- Remaining flat Subject tokens require Atom-by-Atom qualification before the Entity Graph can become a mechanically reproducible complete Subject Path Projection.
