---
atom_id: CA-D-539
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-09 19:48:52 +0400"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/Contract"
  depends_on: [Tool, Projection, Artifact, Journal]
relations:
  delivery_for: [CA-R-1835, CA-R-1836, CA-R-1837, CA-R-1838]
---
# Summary

Bind strict graph request and result contract

## Scope

The minimum Tool/MCP request-result boundary for one graph projection request.

## Claim

The Tool **must** reject ambiguous or mixed graph requests and return a result that makes source lineage, graph quality, namespace, effects, and non-authoritative state inspectable.

## Details

### Caller request and trusted invocation

The serializable caller request has `graph_kind`, `source_frontier`, `selection`, optional `display_selection`, `representation_configuration`, optional `output_destination`, optional `existing_projection_evidence`, and `capability_permission_evidence`. Unknown fields, absent/ambiguous frontiers, mixed graph kinds, and unbound destination inputs are errors or blocking conditions. A caller cannot supply `source_fact_context`, `run_recording_context`, passed admission decisions, or a fabricated receipt.

`selection` is closed: required sorted unique `atom_ids`, and optional sorted unique `scope_unit_names`; both contain nonempty identity strings and may be empty. `representation_configuration` is exactly `{"format":"canonical-json"}` in this contract version. `existing_projection_evidence`, when supplied, is exactly `{"sha256":"<current-prior-output-sha256>"}` for the resolved output destination. `capability_permission_evidence` is exactly `{"authorized":true}` or `{"authorized":false}` as a request assertion; the executor revalidates actual permission, and that assertion alone grants no capability. Unsupported fields or formats cannot affect settings/no-op hashes silently.

The shared executor adds an actual `run_recording_context` only after confirmed Action-start recording. The graph provider adds an immutable `source_fact_context` only after validating its inputs and executing its admitted recognition/admission profiles. These two internal objects are not caller JSON capabilities. Queue-wrapper normalization preserves the actual executor-bound objects and cannot replace them with nested caller data. The builder rechecks their bindings rather than accepting a Boolean assertion of admission.

An explicitly present selection with `atom_ids: []` is admissible when the current source frontier proves its empty membership. Absence, unreadability, duplicate identities, unsupported selection, or unknown coverage is not evidenced emptiness. `scope_unit_names` selects declared Project Structure records separately; folder nesting and target Scope do not select native Atoms.

Omitting `output_destination` permits a non-persisting Tool description/construction result with `output_effects.state: none`; it does not invent a destination or prove a completed graph Action. Persist only to an explicitly authorized derived path or a current, unambiguous registered destination. A configured projection root or conventional filename alone is not registration. An existing destination with different bytes requires current evidence for that exact prior output before replacement. Actual destination existence and before/after bytes determine `created`, `replaced`, or `unchanged`, not presence of an optional request field.

### Derived fact context

On 2026-10-09 the Operator approved a derived, source-pinned fact context built from authoritative Atoms. It is a checked intermediate representation, not a source of truth, a new Atom type, or new frontmatter authority. Source pins prove current bytes, not their semantic admission. The provider recognizes candidates only through a concrete reviewed profile for one of the three closed source locator forms below: role-primary Claim/Operation content, a source-owned direct Relation declaration under CA-D-268, or a canonical Atom Property at its Delivery-assigned location under CA-D-478. Recognition is separate from evaluation against current governing definitions and graph-qualified Relation metadata. Unsupported or undecidable source contributions stay unresolved; a model guess or caller-authored `pass` cannot establish a fact.

The internal context has the following closed object structure:

```json
{
  "schema_version": 1,
  "context_kind": "caprmedio.derived_fact_context",
  "graph_kind": "entities",
  "source_binding": {
    "source_frontier_sha256": "<sha256>",
    "selection_sha256": "<sha256>",
    "authority_frontier_sha256": "<sha256>"
  },
  "provider": {"id": "<admitted-provider-id>", "version": "<version>", "profile_sha256": "<sha256>"},
  "authority_sources": [],
  "relation_registry": [],
  "coverage": [],
  "candidates": [],
  "admission_decisions": [],
  "admitted_facts": [],
  "derivations": [],
  "diagnostics": [],
  "context_sha256": "<digest-without-this-field>"
}
```

`graph_kind` is exactly `entities` or `terms`. Every nested object is closed. Canonical serialization is UTF-8 JSON with deterministic, duplicate-free record arrays. Its exact byte rule is Python `json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")`, with no indentation, BOM, trailing newline, or Unicode normalization; reject unpaired surrogates, duplicate object keys and every floating-point value before serialization. This rule fixes escaping, whitespace, Unicode-key order and integer spelling. No generated time enters canonical semantic data. Every named context/record digest hashes these exact bytes after removing only its own digest field. A digest is integrity evidence, never admission by itself.

Sort `authority_sources`, `authority_inputs` and `source_refs` by Atom identity, revision, path, contribution kind, section/property path, canonical target reference, start/end line and digest; `relation_registry` by graph kind and canonical name; `coverage` by fact class; `candidates` and `admission_decisions` by candidate ID; `admitted_facts` by fact ID; `derivations` by derivation ID; `checks` by code; `diagnostics` by code, source-evidence sort key and canonical details. Missing inapplicable sort components are the empty string, never inferred fields. Reject duplicate record identities rather than silently selecting a winner. `selection_sha256` hashes the canonical closed `selection` object, normalized with explicit `scope_unit_names: []` when omitted; `authority_frontier_sha256` hashes the exact sorted `authority_sources` array. `source_frontier_sha256` binds the existing sealed carrier-frontier digest and the separately checked Project Structure evidence; it does not replace either currentness check.

Each `authority_sources` member binds one exact authoritative Atom using `atom_id`, integer `atom_revision`, repository-relative `carrier_path`, `carrier_sha256`, and a closed tagged `contribution` object. Every contribution has positive integer `start_line`/`end_line` (with `end_line >= start_line`) and `text_sha256`, hashing the exact UTF-8 carrier bytes in that inclusive line span, including their original line endings. Supported locator forms are:

- `kind: primary_content`, plus `section: Claim` or `section: Operation`, for the applicable role-primary contribution. The span excludes its heading and stops before the next same-or-higher-level section; fenced/quoted examples are not declarations merely because they occur inside the pinned span.
- `kind: authored_direct_relation`, plus `property_path: relations.<RELATION_KIND>` and `canonical_target_reference`, locating that exact source-owned target member under CA-D-268. The member identity is the canonical target, not collection position. This existing serialization does not prove graph-kind admission or authorize copying an inverse.
- `kind: canonical_atom_property`, plus `property_path`, locating one canonical frontmatter Property field, or `section` locating its one assigned Main Content section; exactly one of `property_path`/`section` is present. This form requires the actual Property's Delivery assignment under CA-D-478 and a concrete owner/value profile; it does not admit generic metadata transfer or a new source syntax.

The provider verifies the Atom identity, revision, source path, bytes, exact locator, assigned Property/Relation location and applicable scope. Referenced definitions and Relation-kind metadata retain their own ultimate source evidence. Selected non-Atom Project Structure facts retain the separate frontier-bound record/path/digest evidence required by CA-R-1835; they do not become fictitious Atom Claims.

Every `source_refs` or `authority_inputs` array contains those exact source-evidence objects, deduplicated and sorted by Atom identity, revision, path and contribution span. It does not contain an unattested free-text reference. Hashes are lowercase 64-character SHA-256 hex values; counts and line/revision integers are nonnegative, with revisions and line bounds positive. Identity/profile strings are nonempty. Candidate/fact/check identities are unique within their record array; an unknown referenced identity is an error.

Each `relation_registry` member has `kind` (`graph_kind`, `canonical_name`), `metadata`, `authority_inputs`, `evaluator`, `checks`, and `registry_record_sha256` (canonical digest excluding its own field). The closed `metadata` object retains all CA-R-806 fields: `meaning`, `direction`, `inverse`, `source_class`, `target_class`, `source_graph_context`, `target_graph_context`, `cardinality`, `authority_effect`, `transitivity`, `applicability`, `status`, and `exclusive_purpose`; the owning graph and canonical name are in `kind`. Values preserve the governed semantics in canonical JSON and are interpreted only by the concrete reviewed registry profile. `inverse` is a closed tagged object: `{"kind":"none"}` for source-proven absence, `{"kind":"reverse_navigation"}` for source-proven reverse navigation without a separately declared name, or `{"kind":"declared","graph_kind":"<owner>","canonical_name":"<name>"}` for a declared inverse view. Reverse navigation transposes the owning Relation's direction; it does not invent a primitive Relation Kind or its constraints. Neither an omitted field nor a guessed name proves absence. Raw text, presence of fields or a matching digest does not constitute resolved cardinality/endpoint/semantic admission. Missing, conflicting or unsupported registry metadata keeps dependent fact admission unresolved. The same evaluator/check/source-evidence shape described below applies, and every used Relation fact references exactly one current complete registry member. The registry's `status` needs an explicit governing Kind declaration; an Active source Atom does not by itself declare an Active Relation Kind.

Each `diagnostics` member is closed with `code` (nonempty string), `severity` (`error`, `warning`, or `info`), `source_refs` (exact evidence objects, possibly empty), and `details` (canonical JSON object). Diagnostics exclude secret values and unsupported raw source text. A missing contribution or parse failure can use carrier-level path/hash inside safe details without fabricating an exact contribution.

Each `coverage` member has `fact_class`, `disposition` (`complete`, `incomplete`, or `unknown`), `selected_result` (`nonempty`, `empty`, or `unknown`), integer `candidate_count`, integer `admitted_count`, and `source_refs`. Required classes are `entity_admission`, `entity_property`, and `relation` for Entities; `definition` and `relation` for Terms. Each applicable class has exactly one row. `selected_result` describes the admitted requested result: complete/empty requires zero admitted facts and proven exhaustive assessment; complete/nonempty requires an admitted count greater than zero. Incomplete/unknown coverage uses `selected_result: unknown`, never evidentiary empty. Counts equal the actual class's candidate records plus applicable derivation attempts, and admitted facts plus admitted derivations, respectively. Zero recognized candidates, an absent provider, or unsupported syntax is not exhaustive assessment.

Each `candidates` member has `candidate_id`, `fact_class`, `payload`, `recognizer` (`id`, `version`, `profile_sha256`), and `source_ref`, the one exact source evidence object described above. Fact classes are `entity_admission`, `definition`, `classification`, `entity_property`, and `relation`. A candidate retains its actual declaration without asserting native graph membership. The provider's current admitted profile determines the bounded source grammar; this contract introduces no generic prose or frontmatter fact syntax. A profile inventory identifies supported families and unsupported regions before coverage is accepted.

Each `admission_decisions` member has `candidate_id`, `disposition` (`admitted`, `rejected`, or `unresolved`), `evaluator` (`id`, `version`, `profile_sha256`), `authority_inputs` (exact source evidence), `checks` (closed rows with `code`, `disposition`, and `source_refs`), and `decision_sha256`. Check dispositions are `pass`, `fail`, `unresolved`, or `not_applicable`; the digest excludes its own field. An admitted decision requires every applicable source/form, identity, ownership, definition, registry, endpoint/context, cardinality and semantic implication check to pass under a concrete reviewed evaluator. Unperformed checks are unresolved. If a semantic check has no admitted executable evaluator, the provider keeps it unresolved; it cannot substitute an ephemeral model judgment or an invented approval record.

Every candidate has exactly one admission decision. Every admitted decision has exactly one admitted fact, and every rejected/unresolved decision has zero admitted facts. Reject orphan or duplicate records, changed payloads, mismatched fact classes and invalid decision/source references. A derived fact has its separately checked derivation record below, not a fabricated candidate or direct decision.

Each `admitted_facts` member has `fact_id`, `candidate_id`, `fact_class`, `payload`, and `decision_sha256`. It refers to exactly one current admitted decision and its source-backed candidate; no unattested fact is serialized. Payload shapes are:

- Entity admission: `entity_identity`, retaining the admitted canonical/bearer-qualified identity.
- Definition: `term_identity` and `subject_path`; the Term name is fixed by the defining Claim, and the Subject Path binds its governed occurrence. Reused Term names in qualified Entity paths do not create new qualified Terms.
- Classification: `entity_identity` and `class_identity`; classification is support evidence, not a definition or Property value.
- Entity Property: `entity_identity`, `property_identity`, and `value` (`type`, `data`). The concrete governed Property family defines its value type, ownership and cardinality. `data` is canonical JSON; absence is not an asserted null value. Generic Atom/Carrier metadata never transfers to its GOVERNS target.
- Relation: `kind` (`graph_kind`, `canonical_name`), `registry_record_sha256`, `source` and `target` (each `identity`, `graph_kind`, `node_class`), and `representation` (`native` or `external_reference`). Native means both endpoints are admitted native members of the source-selected graph; external_reference means at least one endpoint remains external. Display filtering does not reclassify source graph admission. Direction, endpoint classes/contexts, cardinality and purpose come from the one complete current CA-R-806/CA-M-120 registry entry. Matching names or compatible endpoints cannot fill missing metadata. `NARROWER_THAN` requires explicit declaration plus governing-definition implication; `SUBKIND_OF` is not an alias.

Direct facts retain their single authoritative declaration. Each `derivations` member is closed with `derivation_id`, `fact_class: relation`, the same Relation `payload`, sorted unique `input_fact_ids`, `authority_inputs`, `evaluator`, `checks`, `disposition` (`admitted`, `rejected`, or `unresolved`), and `derivation_sha256`. Its evidence/evaluator/check shapes and canonical digest rules are the same as direct admission. Input IDs refer to actual admitted direct fact IDs or admitted derivation IDs; IDs are globally unique, inputs are nonempty, and the derivation graph is acyclic. Only an admitted derivation with all applicable checks passing may contribute a represented fact. A derived inverse such as `BEARS` retains its admitted `IS_BORNE_BY` input and governing derivation authority; it is not fabricated as a second authored candidate. Its `registry_record_sha256` binds the complete owning `IS_BORNE_BY` registry member, whose declared inverse view authorizes the reversed name/direction. It does not require or create an independently authored primitive `BEARS` registry entry. Atom `GOVERNS`/`DEPENDS_ON` rows stay in incidence/provenance and never enter native Relation arrays by themselves. Foreign graph contexts stay external and cannot create native nodes.

The provider recomputes decisions with its actual reviewed profiles, and the builder validates schema, canonical digest, exact source/selection/authority/profile bindings, full required coverage and every admitted-fact reference. It does not deserialize a caller's claimed admission into trusted context. Recheck every bound source, definition, registry and profile digest before publication. Missing context or required unsupported families makes quality incomplete/unresolved and cannot return `built`/`no_op`. Complete successful delivery remains required by CA-E-555/CA-E-556 and CA-D-540; implementing this truthful partial path does not complete those cases.

### Narrower display selection

Omit `display_selection` for the full source-selected view. The sole admitted narrower selector is a closed object with `mode: explicit_native_identity_set` and `native_identities`, a sorted unique array of full admitted canonical identities already inside the source selection. An empty array is an explicitly empty display, not unknown source coverage. Reject outside-selection identities, prefixes, folders, regular expressions, depth queries, edge allowlists, and unknown fields.

The displayed native graph is the induced subset: a native Relation needs both selected endpoints, and a Property needs its selected bearer. Retain external/incidence/source evidence separately with its actual context; it does not expand native membership. A hidden parent remains in canonical hierarchy evidence, so display filtering cannot invent a Root Term or relax source cardinality. Source and display coverage/validity remain separate dispositions.

### Result and completion

The outward result is closed: required `outcome`, the requested graph namespace, `source_frontier_evidence`, `selection_evidence`, `source_fact_context_evidence`, `lineage`, `quality_dispositions`, `diagnostics`, `non_authoritative: true`, `output_effects`, `completion`, and `run_receipt_refs`; optional `projection_revision` is allowed only for a known persisted output. Unknown result fields are not silently discarded. `outcome` is exactly `built`, `no_op`, `incomplete`, `conflicting`, `stale`, `blocked`, `failed`, or `canceled`. Source/selection/context evidence may be empty objects when unavailable, with the missing condition diagnosed and unresolved; an empty evidence object cannot prove complete empty coverage.

`quality_dispositions` has exactly `coverage`, `fidelity`, `validity`, `currentness`, `permission`, `persistence`, and `recording`, each `pass`, `fail`, `unresolved`, or `not_applicable`. Every required condition needs its actual governing evidence; not_applicable cannot disguise an applicable unperformed check. `diagnostics` is a sorted array of closed rows with `code`, `severity` (`error`, `warning`, or `info`), `message` (safe descriptive text), `details` (canonical JSON object), and optional exact `source_refs`. It retains the affected frontier and source locator without secret values or raw exception disclosure.

`output_effects` is closed with `state` (`none`, `created`, `replaced`, `unchanged`, or `uncertain`), `paths` (sorted unique repository-relative paths), `before`, and `after`. `before`/`after` are either null or a closed `carrier_path`/`carrier_sha256` pair proving observed output bytes. None means no output effect was attempted and has empty paths; unchanged means a proven existing output was preserved, including no-op or rejected replacement, and has empty changed paths. Created/replaced identifies the one observed changed derived path and actual after evidence; replaced also retains before evidence. An unconfirmed effect is uncertain, retains the exact attempted path and available before/after evidence, and cannot claim successful publication. Failed/canceled/stale outcomes describe execution disposition, not a fabricated effect. A failure after proven replacement still reports replaced; a failure before replacement preserves the prior bytes as unchanged. `projection_revision`, when present, equals the proven after digest or proven unchanged existing output digest.

`completion` is closed with `state` (`construction_only`, `awaiting_terminal_recording`, `recording_pending`, `recorded`, or `blocked`), optional `terminal_receipt_ref`, and optional `pending_receipt_ref`. References are nonempty actual shared-support identifiers, not newly defined Journal records. Construction-only/awaiting/blocked evidence grants no terminal completion. Recorded requires the confirmed actual terminal receipt; recording_pending requires the actual shared pending event reference and forbids a terminal-completion assertion. `run_receipt_refs` is a sorted unique array of actual shared receipt identifiers. The shared executor owns transitions and recovery; the pure builder does not manufacture a terminal/pending identifier to satisfy this shape. Final built/no_op requires recorded completion and all other required conditions; a construction-ready result with awaiting/pending recording remains incomplete or blocked even after publication.

Both graph namespaces retain native fact records using the validated context's typed payloads and direct/derived fact identifiers, with their exact source/admission lineage. Rejected/unresolved candidates, Atom incidence, source metadata, external references and non-Atom Project Structure records are separate collections, never disguised native Properties/Relations. Missing or unadmitted graph data is an empty namespace plus a non-complete disposition, not an invented successful schema. Canonical graph data and actual completion/effects/receipt references are separate: repeating identical source/context/configuration bytes yields identical semantic graph bytes without reusing a Run identity or its receipts.

`source_fact_context_evidence` is closed with `context_sha256`, `provider`, `source_binding`, and `coverage`, copied exactly from the validated internal context. If context admission is unavailable, it is an empty object with the missing evidence explicitly diagnosed; it cannot resemble confirmed context. Retain unresolved/rejected candidates and derivation evidence separately in lineage/diagnostics, not native fact arrays. The pure builder does not write Journal events. An actual start context proves only the start boundary. After construction/publication, the shared executor records the actual terminal event. Pending or failed terminal recording preserves the produced output and truthful effects and exposes blocked/incomplete completion with the same pending receipt identity; a nested construction result is not a completed Run. Recovery reconciles that event identity/payload only and never reruns construction to recover recording.
