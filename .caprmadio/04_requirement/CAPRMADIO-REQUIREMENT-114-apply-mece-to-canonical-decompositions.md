---
subject_scopes:
  - principles
tier: principle
principle_order: 6
version: 5
updated_at: 2026-08-17 20:02:25
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-GOAL-001--enable-any-operator-to-build-a-working-system
---
# Apply MECE to canonical decompositions

Every canonical CAPRMADIO taxonomy or decomposition that claims to cover a declared universe must be mutually exclusive and collectively exhaustive within that universe and at that level of abstraction.

Each governed decomposition declares or makes unambiguous:

- the bounded universe it classifies;
- the single discriminating question answered by each axis or partition;
- non-overlapping values or responsibilities at the same level; and
- coverage of every admissible member of the declared universe.

Every in-scope member resolves to exactly one value on each applicable axis. An aspect that answers a different discriminating question belongs on an independent orthogonal axis or in a typed relation. If a member genuinely spans multiple values on one axis, the member must be split at the governed boundary or the taxonomy must be refined. If no value applies, the decomposition is incomplete and fails closed until corrected; a member must not be assigned to an arbitrary near match.

MECE applies independently to each declared axis, taxonomy, lifecycle, structural-level decomposition, or other complete partition. It does not require every Cartesian combination of independent axes to be enabled, nor does it require one unique Artifact Type for every possible semantic coordinate. Optional capabilities may remain disabled while the enabled model stays complete for its declared boundary.
