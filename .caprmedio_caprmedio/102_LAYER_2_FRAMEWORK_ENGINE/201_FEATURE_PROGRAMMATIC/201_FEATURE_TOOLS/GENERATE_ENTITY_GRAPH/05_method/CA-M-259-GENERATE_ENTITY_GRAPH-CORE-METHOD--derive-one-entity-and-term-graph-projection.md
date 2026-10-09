---
atom_id: CA-M-259
content_role: Method
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "projection-pipeline"
  depends_on: []
version: 8
updated_at: "2026-10-09 19:23:34 +0400"
relations:
  method_for:
    - CA-R-1387
---
# Summary

Derive one Entity and Term graph Projection

## Scope

The source-bound construction and optional derived-output persistence of one caller-selected graph kind at the existing GENERATE_ENTITY_GRAPH entrypoint.

## Claim

**to** derive one non-authoritative graph Projection, bind the exact selected source frontier and governing graph authority, recognize source-backed candidates separately from their admission, construct only admitted selected native facts with retained limitations and lineage, validate the applicable graph/coverage/currentness conditions, and return deterministic truthful evidence; persist **only when** an explicit authorized or unambiguous registered derived destination is supplied and the governing quality conditions permit the actual output.

## Details

1. Resolve exactly one caller-selected folder **or** equivalent source frontier, its settings, **and** its Carrier digests. Reject an absent, ambiguous, escaping, **or** unreadable frontier.
2. Parse each readable Carrier **without** mutation. Record **every** unknown **or** unparseable region with its path **and** diagnostic instead of dropping it.
3. Recognize only the three closed source forms bound by CA-D-539: the applicable role-primary Claim/Operation span, an exact source-owned relations.<RELATION_KIND> target member, **or** one canonical Atom Property at its Delivery-assigned frontmatter/section location. Retain actual source span, Revision **and** digest evidence. Candidate recognition is **not** Entity, Property, Term **or** Relation admission. Use the derived source-fact context contract in CA-D-539; keep source metadata **and** Atom incidence separate from native graph facts. Unsupported regions remain explicit.
4. Admit each represented fact under its current governing definitions **and** graph-qualified Relation registry. Preserve declared hierarchy, admitted native dependency Relations, external references **and** every source/derivation path separately. NARROWER_THAN requires defining-authority implication; no SUBKIND_OF alias **or** Subject-dependency inference supplies it. A missing executable admission profile stays unresolved, never complete/empty.
5. Build the admitted directed hierarchy **and** applicable dependency closures, **not** a forced tree. Detect native hierarchy cycles, self-reference, unresolved endpoints **and** actual declared cardinality violations. Multiple parents are **not** themselves a defect. A narrower display does **not** change canonical roots **or** source validity.
6. Sort **every** node, edge, diagnostic, **and** lineage entry by stable canonical keys. Mark the result non-authoritative **and** bind it **to** the complete source, selection, authority, profile **and** settings digests. Apply CA-R-1837's truthful quality dispositions; unsupported required coverage prevents built/no_op.
7. Return construction/description evidence **without** mutation **unless** an explicit output path **or** one registered unambiguous destination was supplied. On authorized persistence, recheck the bound inputs, reject an authority destination, preserve proven prior-output boundaries **and** replace exactly one allowed Projection Carrier atomically. A root folder **or** conventional filename is **not** destination registration.
8. Keep pure construction free of Journal writes. The shared executor owns actual start/terminal append-only recording under CA-R-1838/CA-D-539. A start context **or** generated output is **not** durable terminal completion; recording-only recovery does **not** replay construction.

### Outcome

the result is reproducible as-is graph data that `GRAPH_SERVER` **may** consume read-only **and** `GRAPH_UI` **may** present; it is neither an Atom nor an analysis **and** has no authority.
