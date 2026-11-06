# Header grouping source census and migration preparation

Read-only census of the root-owned native Current/Draft source set. The deterministic preparer computes a nested-header candidate in memory and verifies that inverse flattening restores the exact parsed metadata values and byte-identical Markdown body. It does not write native sources.

## Source set

- 4,677 pinned native sources: 4,412 Current and 265 Draft.
- Scope is exactly the path set in [`native-snapshot.json`](../native-snapshot.json); archives, generated `000`/applicable copies, tests, Journal, projections, and analysis packet descendants are excluded by that selection.
- Current path/hash pins are in [source-paths.json](source-paths.json). 0 source hashes differ from the root snapshot (); the census uses directly observed live bytes and records refreshed preimage pins. Refresh and review them before application.
- YAML parsing found 0 duplicate-key errors, 0 malformed/missing sources, and 0 symlinks in the pinned set.
- Compared with the previous source snapshot, 55 paths were added, 47 removed, and 177 common paths changed. The current snapshot lists 8 supplemental Draft sources, each checked against its pinned path, hash, ID, version, Draft Ref ID, and status.

## Approved grouping

The preparer maps common fields to `identity`, `context`, `relations`, `state`, and `destination`. The full per-field counts are in [summary.json](summary.json). Concern `priority` maps to `context.concern.priority` for Concern Role sources or the approved CA-C ID fallback. Plan `autonomous_confidence_threshold` maps to the canonical `context.plan.ai_agent_confidence_threshold` and `work_sequence_number` maps to `context.plan.work_sequence_number`.

- Concern priority: 209 values mapped (84 by explicit Role, 125 by CA-C ID fallback). 4 Plan `priority` values remain flat because no Plan priority slot is authorized.
- Plan context: 284 existing `autonomous_confidence_threshold` values map to `ai_agent_confidence_threshold`; 1463 `work_sequence_number` values map. The physical source key is retained by inverse flatten for exact-value verification. No exact physical `ai_agent_confidence_threshold` key occurs.
- Canonical field authority is Current D657 (`CA-D-657-CORE_META_MODEL-DECISION--yaml-frontmatter-encodes-atom-properties-with-minimal-syntax.md`, SHA-256 `f0feb98ead15990e4d8f3528f8fc6a181625812465a300e037e07e34576bb830`). No source has both the legacy and canonical Plan threshold keys.
- Other unmapped keys remain at the top level after the approved groups. Counts are in `header-census.json`; notable extras include `author` (3,164), `current_scope_unit` (4,224), `claim_target_scope_unit` (3,114), `assignee` (1,123), and CCE legacy keys `cce_form`/`cce_version` (574 each). Four Plan priority values remain flat. No unapproved group is inferred.
- 32 sources lack Role without an approved Concern/Plan ID fallback; no Role or Form is synthesized.

## Shape and preservation checks

- Omit a group when it has no mapped leaf. Empty groups found: Context 15, Relations 1,832, Destination 1,514. State and Identity are populated in all sources. Explicit Relations values are preserved; none is an empty mapping.
- Deterministic transform/inverse-flatten checks passed for 4,677 sources; 0 are held. Candidate and source hashes are per record in [header-census.json](header-census.json).
- [representation-example.yaml](representation-example.yaml) illustrates Concern and common group shape. Unsupported extras remain flat.
- YAML serialization canonicalizes frontmatter layout and scalar presentation; it preserves parsed metadata values and the exact body. Preserving frontmatter comments or original quoting style would require a token/span-preserving writer.
- Runtime readers that expect flat `atom_id` and `status` require the separate CA #3 adapter/readiness gate before any cutover. Current Workbench readiness is NotReady. This preparation does not establish runtime compatibility, schema admission, or promotion.

Run `./.venv/bin/python .caprmedio_caprmedio/02_analysis/draft/header-groups-20261106/data/prepare_groups.py` from the repository root to refresh the census and in-memory round-trip hashes against the root-pinned source list.
