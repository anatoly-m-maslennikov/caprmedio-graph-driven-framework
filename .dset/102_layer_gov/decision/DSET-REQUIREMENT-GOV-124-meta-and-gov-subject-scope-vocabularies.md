---
artifact_type: requirement
artifact_id: DSET-REQUIREMENT-GOV-124
scope_path: layer:gov
subject_scopes:
  - subject-scope
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - DSET-REQUIREMENT-GOV-122
  - type: relates_to
    targets:
      - DSET-REQUIREMENT-META-071
      - DSET-REQUIREMENT-GOV-123
---

# Requirement — Register META and GOV subject scopes

Atomic Artifacts owned by `layer:meta` use only these subject scopes:

| Subject scope | Governed subject |
|---|---|
| `artifact-model` | Atomic structure, semantic routes, properties, and artifact distinctions |
| `assurance` | Test, Evaluation, evidence, verification, and assurance boundaries |
| `authority` | Constitutional ownership, precedence, and rule placement |
| `external-boundary` | Obligations imposed by systems or authorities outside the project |
| `governance-surface` | Activation and composition of the governed control surface |
| `interaction` | Operator input, Exploration Mode, and interaction behavior |
| `lifecycle` | Admission, archive, replacement, and temporal claim rules |
| `profile` | Optional applicability and product or implementation profiles |
| `scope` | Structural ownership, Work Areas, features, and subject scoping |
| `self-hosting` | Recursive application of DSET to its own repository |
| `topology` | Layer order, handoffs, and forward-only propagation |

Atomic Artifacts owned by `layer:gov` use only these subject scopes:

| Subject scope | Governed subject |
|---|---|
| `artifact-catalog` | Type, subtype, route, whitelist, and naming catalogs |
| `assurance` | QA Cases, assurance standards, review protocols, evidence, and verification |
| `carrier-format` | Markdown properties and other governed storage carriers |
| `external-boundary` | External constraints, references, reviews, and legal boundaries |
| `interaction` | Operator-facing settings and artifact admission behavior |
| `layout` | Control-plane folders, placement, discovery, and architecture views |
| `lifecycle` | Atomic admission, archive, recurrence, replacement, and release readiness |
| `methodology` | Methodology installation, synchronization, and governing constitution |
| `priority` | Priority vocabulary and conflict selection |
| `provenance` | Git, session, commit, and evidence provenance |
| `relation-model` | Artifact relations, endpoints, conflicts, and lineage |
| `runtime` | Runtime state, journals, scratch storage, and execution boundaries |
| `settings` | Project settings, configuration selection, and enabled governance surfaces |
| `subject-scope` | Subject-scope vocabulary, cardinality, and validation |

The vocabularies are closed for their respective structural owners. A new
subject requires a new Atomic Artifact that updates this authority through the
normal immutable replacement mechanism.

## Primary claim

META and GOV Atomic Artifacts use only the registered layer-local subject
scopes defined here.

## Rationale

A small governed vocabulary makes subject scopes useful for bounded searches
and obsolete-atom reviews. Free-form or per-file labels would satisfy syntax
while recreating an unbounded tag system with no stable retrieval meaning.
