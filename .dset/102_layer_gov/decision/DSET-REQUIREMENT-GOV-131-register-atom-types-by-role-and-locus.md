---
artifact_type: requirement
artifact_id: DSET-REQUIREMENT-GOV-131
scope_path: layer:gov
subject_scopes:
  - artifact-catalog
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - DSET-REQUIREMENT-GOV-121
  - type: child_of
    targets:
      - DSET-REQUIREMENT-META-082
      - DSET-REQUIREMENT-META-083
  - type: relates_to
    targets:
      - DSET-REQUIREMENT-META-049
      - DSET-REQUIREMENT-META-051
      - DSET-REQUIREMENT-META-056
      - DSET-REQUIREMENT-GOV-102
---

# Requirement — Register Atom Types by Content role and Governance locus

The GOV artifact catalog registers this canonical Atom-form Type surface:

| Content role | Internal Atom Type | External Atom Type | Relational Atom Type |
|---|---|---|---|
| `concern` | `concern` | `external_problem` | `conflict` |
| `analysis` | `analysis` | `external_analysis_report` | `conflict_analysis` |
| `requirement` | `requirement` | `constraint` | `contract` |
| `method` | `method` | `implementation_methodology` | `integration_decision` |
| `assurance` | `assurance` | `assurance_standard` | `review_protocol` |
| `implementation` | `implementation` | `external_git_commit` | `pull_request` |
| `observation` | `observation` | `external_evidence_record` | `verification_record` |

The seven internal names are derived by META and cannot be renamed or replaced by project policy. GOV owns the external and relational names and may revise them through governed successors without changing their Content roles or Governance loci.

Every relational Atom declares explicit endpoints appropriate to its meaning. Every external Atom identifies the outside authority, system, repository, or other origin that owns or imposes its meaning. Authority, provenance, priority, lifecycle, and `scope_path` remain separate metadata.

## Assurance boundary

An internal `assurance` Atom that defines a deterministic check declares direct subtype `test_case`. An internal `assurance` Atom that defines a qualitative, probabilistic, statistical, rubric-based, or model-judged assessment declares direct subtype `eval_case`. A Test Case or Eval Case owns one independently replaceable check and states its conditions, criteria, and disposition rule.

Executable test or evaluation code is internal `implementation`, not Assurance. A test result, evaluation result, or verification outcome is `observation`. Test and evaluation chains remain separate even when they assure the same Requirement.

Other Assurance patterns may use the top-level `assurance` Type until GOV admits another direct subtype. A subtype is never a sub-subtype and never replaces the canonical top-level Type.

## Method and Implementation boundaries

An internal `method` Atom selects how accepted Requirements will be approached or realized. An internal `implementation` Atom identifies one governed realized change or executable/configured realization. Native code and configuration remain normal project carriers and may realize an Implementation Atom without becoming control-plane documents.

A Pull Request remains a relational Implementation connecting declared source and target endpoints. Its rationale, assurance, and observations retain their own roles and do not become Implementation merely because the Pull Request contains links or summaries.

## Primary claim

GOV registers the canonical Atom-form Type for each Content-role and Governance-locus coordinate, deriving all internal names directly from their Content roles and retaining Test Case and Eval Case as Assurance subtypes.

## Rationale

The predecessor used special internal names such as Problem, Technical Decision, QA Case, Git Commit, and Evidence Record. Direct role-equals-Type naming makes internal Atoms predictable, while GOV retains the contextual names required at external and relational boundaries.
