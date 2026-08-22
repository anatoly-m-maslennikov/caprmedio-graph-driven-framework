+++
artifact_subtype = "external_audit_analysis"
priority = "high"
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]

[[relations]]
type = "analysis_of"
target = "CAPRMEDIO-GOV-REQU-395--verbose-project-settings"

[[relations]]
type = "relates_to"
target = "CAPRMEDIO-SPEC-TOOLS-CONC-058--immutable-toml-migration"

[[relations]]
type = "relates_to"
target = "CAPRMEDIO-SPEC-TOOLS-CONC-059--relation-bound-health"

[[relations]]
type = "relates_to"
target = "CAPRMEDIO-GOV-CONC-023--classification-enforcement"

[[relations]]
type = "relates_to"
target = "CAPRMEDIO-SPEC-TOOLS-CONC-060--conflict-source-truth"

[[relations]]
type = "relates_to"
target = "CAPRMEDIO-GOV-CONC-024--evidence-record-contract"
+++

# External audit analysis — Framework coherence and FPF alignment

## Scope and method

Three independent subagents reviewed DSET at `6a6446e` for internal
consistency/MECE, alignment with pinned FPF revision `afa4936`, and readiness
for the canonical TOML migration. The main session reproduced the migration
inventory and reconciled overlapping findings.

## Accepted findings

- Three active requirements still named the retired settings carrier. They
  require immutable successors and lifecycle absorption, not edits.
- The migration preview included immutable atoms, promoted proof, and legacy
  Decision carriers. Applying it would destroy the history used to authorize
  the migration.
- Health coverage trusted textual mentions instead of validated relations.
- Missing artifact classification could be skipped, so MECE completeness was
  not enforceable.
- Conflict resolution trusted caller-asserted repository facts.
- Evidence Record requirements existed in prose without an executable schema.
- Delivery subtype role mapping, replacement terminology, public artifact
  taxonomy, skill routing language, triage language, README status, and
  configurable-priority schemas contained bounded drift.

## FPF disposition

DSET retains four semantic Types, its separate artifact-role axis, immutable
source atoms compiled into evergreen projections, and the separation of QA
definition, execution evidence, Verification, and release readiness. These are
aligned adaptations, not imported FPF ontology or a claim of FPF conformance.

FPF sharpened the corrections: coverage must be a validated because-graph;
classification must fail closed; conflict precedence must come from authority;
and representation transition must preserve identity, claims, provenance,
loss boundaries, admissible use, and return conditions.

## Deferred decision

Acceptance-act representation remains the existing open
`CAPRMEDIO-GOV-CONC-042--should-decision-lifecycle-be-schema-enforced`. This audit does not create a duplicate Problem or
silently choose a lifecycle design.
