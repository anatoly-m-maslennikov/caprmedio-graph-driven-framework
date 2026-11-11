# Nested Header adapter handoff

The Operator approved nested Header Properties, in-place Current/Draft migration, and Role/Form-specific Context groups. Source preparation is in this packet; live YAML has not yet been cut over.

## Serialized Header

YAML frontmatter is Header, without a `header` wrapper. Group order:

1. `identity`: `atom_id`, `ref_id`.
2. `context`: `container`, `role`, `form`, optional `label`, `topics`, `tier`, then declared Role groups.
3. Optional `relations`: existing direct Relation keys and their nonempty target lists.
4. `state`: `status`, `version`, `updated_at`.
5. `destination`: `file.name`, `file.path`.

Role groups:

- `context.concern.priority`: existing Concern Priority.
- `context.plan.work_sequence_number`: existing Plan number.
- `context.plan.ai_agent_confidence_threshold`: existing Plan threshold. The migration preserves values from the old physical `autonomous_confidence_threshold` key and uses the already-declared canonical name.
- Form-specific groups belong under `context.<role>.<form>` when declared. No arbitrary groups or fields are admitted by this pattern.

Unmapped legacy fields remain at the end, unchanged. Four old Done/Canceled Plans retain their undeclared top-level `priority`; no Plan Priority is introduced. Existing missing values remain missing, and absent groups remain absent. Carrier filename/path values and every other business value are preserved except the explicitly reviewed model identity/Version changes.

## Adapter outcomes

- Current/Draft identity, lifecycle, topics, containment and destination readers resolve the nested locations.
- Writers preserve the nested layout and apply the declared ordering.
- Frozen archives keep their existing bytes and may retain flat historical layouts.
- Workbench indexes the actual nested source Properties faithfully. Existing typed/public identity and status columns continue to identify their source values.
- No second authored flat copy is added to live frontmatter.
- Journals and execution state are not rewritten by the source migration.

The Operator's newer Workbench decision is: Header columns use all fields found in valid files; Content columns use model declarations. Header SQL names flatten path levels with underscores. Content SQL names keep dots between levels and use snake_case within each segment, such as `content.claim.formal_claim`. This supersedes the earlier declared-only Header-column request and all-underscore Content naming. Observing a retained legacy field does not admit it as a new model Property. The Header source migration and model constraints stay within the mapping above.

## Observed callers

The source lane inspected `current_atom_locator.py` and `atom_subject_lookup.py`: both currently read flat `metadata.get("atom_id")` and lifecycle fields. The shared carrier/parser, locator, lifecycle writers, validation, compilation and Workbench source readers need the implementation owner's compatibility review before live source cutover.

Source preparation and source-level assertions do not establish adapter/runtime readiness. CA #3 owns shared implementation and test work; Workbench code remains with its existing owner. Source lane owns the model, prepared source edits and the guarded source application.
