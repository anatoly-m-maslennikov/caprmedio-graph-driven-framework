---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-SPEC-001
scope_path: layer:spec
subject_scopes:
  - skill
priority: medium
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - DSET-REQUIREMENT-SKILL-011
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-GOV-136
      - CARMADIO-REQUIREMENT-GOV-137
---

# Requirement — Provide the co-refactoring skill

CARMADIO provides `co-refactoring` as the public orchestration skill for one
bounded governed refactoring cycle.

The skill resolves the target repository or Work Area and its project-local
governance, then checks these entry criteria:

- the refactoring target and structural scope are explicit;
- applicable behavior and obligations to preserve are identified;
- any intended behavior change is governed by a separate Requirement; and
- no unresolved ambiguity would change the selected strategy materially.

When no accepted Refactoring Plan exists, the skill may chain the registered
atomic-recording capability to create one `refactoring_plan` Atom after the
operator accepts its claim. It then chains the applicable implementation and
assurance capabilities. It stops when an entry criterion, authorization gate,
or governed downstream capability is unavailable.

`co-refactoring` remains a thin, provider-agnostic wrapper. It contains no
project methodology, refactoring rules, implementation algorithms, host-only
policy, or duplicated shared runtime. Codex, Claude, and other supported hosts
must resolve and apply the same repository-local rules.

## Primary claim

CARMADIO exposes `co-refactoring` as a thin orchestration skill for a governed
Refactoring Plan, implementation, and assurance cycle.

## Rationale

One public entrypoint lets an operator request a refactoring in natural
language while keeping planning authority in project Atoms, mechanical work in
shared capabilities, and methodology in the target repository.
