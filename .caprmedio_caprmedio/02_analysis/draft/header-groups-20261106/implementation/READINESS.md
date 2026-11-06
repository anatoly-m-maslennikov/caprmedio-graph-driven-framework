# Nested Header implementation readiness

Shared implementation and focused local verification are complete. This report
does not authorize source cutover or claim installed runtime readiness.
Source/model preparation and Workbench changes remain with their assigned owners.

| Deliverable | Owner | Exclusive edit scope | Dependency | Acceptance | State |
|---|---|---|---|---|---|
| Shared read/path/scalar boundaries | header_shared_boundary | carrier_aliases, header_groups, header_yaml, header_yaml_nodes and tests | Approved handoff | Nested/flat reads; conflict refusal; ordered writes; residue preserved | Done; review corrections verified |
| Lifecycle writers | header_lifecycle_writers | atom_operations, lifecycle_intents, subject_batch_drafts, atom_subject_patch, ATOM_UPDATE/atom_update and tests | Shared API | Nested create/update/promote/move; archive bytes preserved | Done |
| Validation | header_validation_contracts | VALIDATE_ATOMS | Shared API and reviewed encoding | Declared nested paths, safe parsing, source binding, admission | Done |
| Locators, status sources and compilation | header_locators_compile | current_atom_locator, atom_subject_lookup, authoritative_status_models, COMPILE_APPLICABLE_METHODOLOGY and tests | Shared API | Nested discovery, status resolution and source-preserving compilation | Done |
| Entity graph readers | header_graph_readers | GENERATE_ENTITY_GRAPH | Shared API | Nested detection, pins and containment; raw evidence retained | Done |
| Metadata and connectors | header_metadata_connectors | artifact_metadata, section/scope receivers, Property guard and tests | Shared API | Nested revisions; TOML preserved; Property identity guard | Done |
| Retained workflow callers | header_metadata_connectors | Orchestrator engine, replacement, shared_context_validation_loader and tests | Shared API | Nested selection/identity guards and replacement retain layout | Done |
| Independent safety review | header_adapter_review, header_validation_review | Read-only shared helpers and admission | Stable implementation | Reproduce correctness and preservation defects | Done; no outstanding must-fix findings |
| Cross-boundary verification and integration | root | Public lookup/Atom read/Settings/Artifact query integration; this report | Completed lanes | Focused functional regression checks and explicit remaining gaps | Done |

## Boundaries

- Parsed carrier metadata retains the actual YAML mapping. Semantic readers use
  the shared compatibility view; no second authored flat copy is introduced.
- Existing flat archives remain readable and exact archived bytes are preserved.
- Nested field placement follows the handoff, including Concern-only Priority,
  Plan sequence/confidence fields and preserved legacy root residue.
- No live Atom Headers, native model declarations, frozen fixture oracle,
  Workbench implementation, journals or execution state are migrated here.
- Verification uses the Project virtual environment and focused related tests.
  No full-suite run, deployment, release, commit or push is part of this increment.

## Shared reader contract for integration owners

`VALIDATE_ATOMS.validate_atoms_workers.parsing.parse_carrier(...).metadata`
continues to return the actual source mapping. Workbench Property indexing and
fully qualified SQL Property names must derive from that mapping, retaining
`identity.atom_id`, `context.role`, `state.status`, etc. It must not flatten the
semantic compatibility view into authored or indexed source Properties.

`carrier_aliases.carrier_read_view(raw)` is a separate, non-mutating semantic
read projection. It exposes legacy identity/state/Role/Form keys for existing
consumers, `container`, `topics`, `carrier_destination`, and the declared
Role-specific fields. Topics also expose read-only Subject aliases:
`main_subject` -> `active`/`governs`; `dependencies` -> `passive`/`depends_on`.
Unequal or type-conflicting old/new values raise `ValueError`. No Source Header
is rewritten by this function. Container Scope Unit IDs remain distinct from
legacy `current_scope_unit` names; the latter is never synthesized by the view.

`header_groups.nested_header(raw)` provides ordered canonical authored groups
while preserving unmapped root residue and missing values. `header_path` and
`header_field_paths` identify actual/canonical paths. `header_yaml` exports
`parse_header`, `header_scalar`, `header_scalar_node`, `replace_header_scalar`
and `remove_header_scalar`; scalar edits retain the existing layout and source
spans. `parse_header` returns actual keys, with duplicate/alias/resource checks.

This is shared-library compatibility evidence, not Workbench schema, installed
image, source-cutover or deployment readiness. See the independently owned
`../workbench-readiness.md` for Workbench state.

## Evidence

Completed focused evidence (counts are suite executions, not unique-test totals):

- Shared helper golden cases: 18; existing aliases: 7. Ruff and strict Mypy pass
  the four shared source modules.
- Metadata/connectors: 89 focused checks pass, including independent frozen
  section/scope fixtures, Property carrier and engine writer exclusions.
  The final metadata suite has 13 passing cases after adding a Projection-kind
  regression: Projection timestamps remain at root and arbitrary Context/State
  data is not interpreted as an Atom Header. TOML behavior remains intact.
- Retained workflow callers: 41 focused checks pass, including nested selection
  guards, replacement bytes, complete Method parent closure and error handling.
- Locators: 21 pass; Subject owner lookup: 7 pass. Compiler suite executed 79:
  78 passed initially, one test-only expected-diagnostic correction passed in a
  separate targeted rerun. Updated nested compilation cases passed separately.
- Graph readers: 105 focused checks pass, including nested Topics provenance,
  source seals/body offsets, current source discovery and container selection.
- Status readers: 12 authority tests and 16 status-family tests pass; the full
  nested authority closure also passes 3 functional admission regressions.
- Parent integration: nested public lookup 3, full/query Atom reads 2, existing
  Atom reads 12, Settings Reader 14 and schema-warning behavior 7 pass. Final
  integration reruns passed the 15 nested validator cases, 3 public lookup cases,
  2 full/query read cases, 5 native lifecycle cases and 13 metadata cases.
- Generic Artifact query: 18 checks pass. Nested logical identity is resolved
  separately while actual query Property paths remain source-faithful; arbitrary
  non-Atom Artifact Context/State fields retain their existing semantics.
- Existing oversized modules retain baseline Ruff diagnostics; these are not
  represented as full source-boundary conformance or a new accepted exception.
- Validation: 92 focused successful cases (15 new nested, 8 Current encoding,
  41 schema and 28 unchanged public-command golden cases). Exact predecessor
  safety checks passed again after excluding both `archive/` and legacy
  `archived/` paths. Direct current Archived carriers outside history folders
  remain supported. See [validation details](validation-readiness.md).
- Lifecycle: 5 new functional cases pass for native create/update/archive,
  actual move, Draft/promotion preparation, nested Topics/state materialization,
  canonical creation ordering and refusal of new undeclared residue. Existing
  subject materialization's 10 cases also pass. History bytes and unchanged root
  residue, including Plan Priority and comments, are checked independently.

The shared-adapter review found that malformed scalar `relations` was accepted;
it is now rejected before reading, canonical emission or metadata mutation.
Four safety regressions also verify YAML depth/event checks before construction.
The reviewer reran those four cases and confirmed the correction. Independent
admission review found no must-fix issue in nested field admission, exact
predecessor preservation or the mutation callers' bound predecessor handling.

Known historical fixture failures were checked against an isolated `git archive
HEAD` baseline, now retained at
`.caprmedio_tmp/header-groups-20261106/head-baseline/`:

- `test_current_type_admission.py`: the same failure/error in two existing
  Current fixture setups, missing required containment authority.
- `test_draft_marker_formats_golden.py`: the same 12 errors across 11 existing
  tests, caused by the frozen D276/D378 authority closure.

Those existing oracle bytes and expected outcomes were not rewritten. These
results are known limits of the existing test harness, not green-suite claims.

## Remaining integration limits

- Workbench source-property indexing/schema and the actual source cutover are
  independently owned and were not executed here. No installed image, MCP
  replacement, release, commit or push is claimed.
- Frozen exact-pin graph admission profiles retain their original historical
  source/Subject locators. They do not automatically admit changed live authority
  pins; that is an explicit compatibility boundary, not a rewritten oracle.
- Equal physical Topics/legacy Subjects copies remain read-compatible. A Subject
  edit that would diverge those copies is refused rather than silently writing
  inconsistent data. The prepared source migration does not add such copies.
- Whole-tree Mypy remains blocked by existing duplicate imports of the same
  validator modules under two package names. The new shared helpers pass strict
  Mypy and the new validation module passes its direct check. Existing oversized
  modules/complexity diagnostics remain outside a claim of complete conformance.
- No full repository suite was rerun. The known original fixture failures above
  remain documented against the unchanged-HEAD baseline.
