# Bounded Core graph design contract

Latest Operator input wins. Deliver both derived RMED views, using the shared Entity model, without changing Core or Subjects. The immediate work is local without MCP or FPF.

Baseline: .caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json
Current baseline fingerprint: 23394abaf6e9c18a585cf3146aedd0a80df166c9dd82be6e86ed7c3c56780bdc
Current baseline review: .caprmedio_caprmedio/_projection/core-entity-review/baseline.review.md
Your Plan is CA-P-1913 through CA-P-1920 under CA-P-1906; read your Plan.
CA-P-1905 is Done. These eight Tasks may run independently; no other top-level review Task is ready yet.

## Batch JSON contract

Output JSON envelope: source_task, batch_number, baseline_inventory_sha256, source_binding, partition_sha256 (from input), non_authoritative=true, source_migration="not_performed", semantic_admission="not_performed", cases. Each case: case_id, old_parent, old_child, disposition ("proposed"|"unresolved"|"not-native"), confidence_percent integer 0..100, proposal (null for unresolved/not-native; otherwise {display_operator, canonical_relation, graph_kind, canonical_direction, qualified_parent:old_parent, qualified_child:old_child, semantic_intent, native_admission:"not_performed"}), evidence[], checks_performed[], reason, question (string or null). Treat qualified references as baseline IDs to be rebased by integration, not serialized new identities. Native relation proposal is not admission. If only display evidence exists without native kind coverage, mark not-native and optionally include display_candidate separately, with no proposal.
Evidence item: atom_id, atom_revision, carrier_path, carrier_sha256, start_line, end_line, quote (inclusive lines joined with newline), text_sha256 (SHA256 of quote UTF8). Quote Main Content, not Subjects alone. Verify pin matches current selected source. "/" proposal requires same-referent/narrower Core evidence and owns Terms Graph; "." proposal requires bearer/dependent Core evidence and owns Entities Graph. General bearer qualification is approved but does not itself prove all instances of IS_BORNE_BY. Only current Main Content evidence, no filename/metadata-derived semantic facts.
No source writes; no Plans/Git/MCP/FPF/runtime edits; output only your JSON and optional unique helper in design dir. Use apply_patch for authored outputs/scripts, uv for Python. You are not alone; preserve other agents' and user's work. Each batch <=15min; explicit uncovered cases stay unresolved with checks/reason/question, never fill them mechanically to claim certainty.

## Grouping JSON contract

CA-P-1919 owns only structure.design.json and a uniquely named helper if needed. Source pins and Main Content spans use the same evidence item format as the batch contract. Output proposed display_groups, separately evidenced additional_relations (not fabricated old Subject occurrences), inherited_constraints, root_counts with method, coverage and questions. Preserve all baseline identities through explicit reference to the pinned inventory; do not imply unreviewed roots were assessed. Continuant/Occurrent are local display groups, not BFO import. Definition, information artifact and Run must remain distinct. Preserve concrete Carrier identities and treat inherited rules, not concrete bindings, as shared.

## RMED views JSON contract

CA-P-1920 owns only rmed.views.json and rmed.views.md and a uniquely named helper if needed. Build both role-centered overview and Entity-centered applicable M/E/D pointer views. Keep source Atom references as Claims/provenance distinct from model Entity identities. Each row has source ref and exact GOVERNS/DEPENDS_ON role; no dependency becomes a governing Claim or inferred native applicability. Shared sources are referenced, not copied. Show concrete examples and omit empty M/E/D slots. Qualify view membership as pointer-derived where applicability is not explicitly proven.
R is the model skeleton/required results; M construction and authoring conventions (not O's particular actions/workflows); E checks/acceptance; D Carrier model, formats and placement/storage. Source D definitions may also contribute to the Entity-model skeleton; do not restrict model inputs to R-only.
Internal/External/Relational is orthogonal; do not guess locus from role, filename or source incidence.
No new native relation types, root semantics or authoritative definitions are admitted here.

## Return

Report output paths, exact case/coverage counts, checks, unresolved questions and confidence. Complete your assigned batch within the 15-minute work estimate; write explicit unresolved cases rather than continuing unbounded. Do not update Plan Status or Git: root independently validates and owns receipts. Do not touch another worker's outputs. No deletes, source changes, baseline overwrites, YAML renames, MCP, runtime, push or PR.
