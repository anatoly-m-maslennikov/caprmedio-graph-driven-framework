---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-067
scope_path: layer:meta
subject_scope: scope-topology
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-024
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-065
      - CAPRMADIO-REQUIREMENT-META-096
---

# Requirement — Define current layer handoffs

Each adjacent boundary owns a handoff:

| Boundary | Accepted input | Produced output |
|---|---|---|
| META → GOV | Semantic invariants and layer constitution | Governable carriers, identities, settings, lifecycle, and conflict policy |
| GOV → SPEC | Governed project scopes, enabled artifact vocabulary, and authoring constraints | Current project obligations, technical choices, integration boundaries, and assurance definitions |
| SPEC → PROFILES | Required outcomes, boundaries, and assurance obligations | Applicable selectable implementation rules |
| PROFILES → IMPL | Selected environments, dependency policy, authoring practices, and profile gates | Concrete implementation, configuration, Tests, Evaluations, and traceability |
| IMPL → OPS | Verified and supportable implementation | Deliverable, releasable, operable, and diagnosable output |

Every handoff declares entry criteria, exit criteria, and blocker behavior.
Adjacent handoffs are preferred. A direct forward skip is allowed only when
the intermediate layers have no meaningful transformation or ownership to add.
CAPRMADIO does not create placeholder artifacts merely to simulate an unnecessary
handoff.

## Primary claim

Every adjacent boundary in the current CAPRMADIO topology declares its accepted
input, produced output, entry criteria, exit criteria, and failure behavior.

## Rationale

The predecessor's general handoff invariant remains valid, but its concrete
TOOL and SKILL boundaries were retired when those concerns became project
scopes realized through SPEC, PROFILES, and IMPL.
