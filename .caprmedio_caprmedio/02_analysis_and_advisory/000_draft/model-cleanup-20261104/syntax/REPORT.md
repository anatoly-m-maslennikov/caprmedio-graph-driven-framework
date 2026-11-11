# MODEL Subject syntax triage

Input: `projections-publication/audit-data.json`, SHA-256 `e30ff6078188c4574f71eb69dac29d3af4c124eb9aabf59f92d0ea0635d8202f`.

- **13 syntax failures:** cases 1–13.
- **21 contextual MODEL selections:** cases 14–34 lack an explicit namespace; supplied MODEL default inheritance applies, so no rewrite is inferred.
- **17 parsed, non-direct selections:** cases 35–51; no target mapping is inferred.

`triage.json` records all pins, source paths and source hashes. All 199/199 occurrence hashes match current bytes.

## Syntax findings

Case 1 needs the approved selector spelling `(Node, Node.**)`; the shared parser still rejects comma-separated selector groups. Root owns that parser issue in `_ExpressionParser.head` and `FEATURE_TOOLS/ATOM_SEARCH/tests/test_subject_notation.py`.

Cases 2–3 remain held: their relation cardinality direction is unresolved. Cases 4–11 use obsolete `CFEL > Relation` composition; Current CA-R-2247 establishes `CFEL <+ Relation`. Cases 12–13 use obsolete whole-to-part `>` and normalize to `<+`.

Current authority checked: `CA-R-2247@7` (`.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2247-CORE_META_MODEL-ENTITY_DEFINITION--define-relation.md`), SHA-256 `e94d4c0b78e0a1fbcb83e0070b323017b836335d188191729a75325d4c7f6e27`. The Current source declares `CAPRMEDIO_MODEL <+ CFEL <+ Relation`.

## Candidate overrides

Generated 73 full-source `.txt` candidates for exact pins. They change only `subjects.active` or `subjects.passive`, preserve all other bytes, and are not applied to Current sources. Pins and candidate hashes are in `overrides/manifest.json`.

Examples: `CAPRMEDIO_MODEL <+ CFEL > Relation` → `CAPRMEDIO_MODEL <+ CFEL <+ Relation`; `CAPRMEDIO_MODEL <+ CFEL > Relation//CARRIES` → `CAPRMEDIO_MODEL <+ CFEL <+ Relation//CARRIES`. Cases 2–3 have no candidate. Case 1 is a source spelling candidate only; parser support remains outstanding.
