# Declaration-driven graph repair acceptance

Status: PASS — bounded implementation and independent read-only verification, 2026-10-13.

Author: `/root/epic_compatibility_inventory`. Independent reviewer: `/root/epic_property`. Scope: CA-P-2272's explicit Delivery bindings and CA-P-2302–2304's declaration-driven topology, separate directory observations and exact source attribution. Code commit: `7a04f8a2e`.

## Evidence

The author ran 23 focused tests. The independent reviewer added and ran seven separate tests; root reran all 30 successfully. The earlier committed generator failed four positive cases with the legacy `201` ancestry refusal while two safety cases passed. The final candidate also refuses stale Structure rebinding instead of attaching new source hashes to old semantics.

A read-only current-checkout probe returns 29 declared Scope Units and 35 observations. TOOLS uses declared level 3 and navigation 1 while keeping physical prefix `201` as an observation. Declared missing APPLICABLE_METHODOLOGY and untyped authority paths remain visible. Semantic topology does not come from folder names. Scope semantic fields bind to Project Structure; inherited authority mode binds to Settings. Serializers are deterministic. Authority and production graph files were unchanged.

## Pins

Code paths are relative to `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_PROJECT_GRAPH_STATE/`.

| Source | SHA-256 |
| --- | --- |
| `generate_project_graph_state.py` | `c0f4d379c68da0daced72f09f9877212d784a2774f1bcf4ba90106f1b864b5c8` |
| `tests/test_generate_project_graph_state.py` | `338777d2173f2cc38569f0980475668f400dd0e28617e24ccd0a33bb308fc65f` |
| `tests/test_declaration_graph_independent.py` | `c735e724e71060a41f81b3b7e3e05344c749403b935dcb489c1ef9976007b49f` |
| `.caprmedio_caprmedio/project_structure.toml` (repository-relative) | `89ac3ee9ede4e2af60e8e165abc5d06e2dcb2ad53e651228704cd76a1e0f0494` |
| CA-R-1070 | `7b7b908bd4a4462ac319bb1c466722b0c0b765147d3c7b013252d8111d2ec9c3` |
| CA-M-149 | `1b0d6fd619efc8d6e45600c83e69ec40dd69807a1a36049929bdd295b92d4cfb` |
| CA-E-295 | `be62f865dba9e589817bab0181be0f492a1345ceede5f4f9e5bf860cecbfeb73` |

## Unresolved boundaries

Full CLI generation stops earlier with `Settings current revision binding is unresolved or ambiguous`: both Project and Framework Settings revision receipts remain unresolved. This packet does not repair those receipts or certify full generation, installed execution, publication, release or runtime readiness.

A separate pre-existing shared path-validation gap remains: a declared authority path `nested/.caprmedio_other`, containing another Project's Settings and control-root declaration, is accepted. CA-D-442 v6 (`caa3df94215a7ae1e3e516c0bf94cae1295c79270f0f521e6f75a1eb51d70a2f`) forbids paths resolving to another Project control root. The unchanged Project Structure `_relative_path` helper checks repository containment, but not that boundary; the graph reuses it. This acceptance does not certify complete path-policy conformance. Diagnose and fix the shared gap separately before affected runtime readiness.

This receipt is derived evidence. No source/Subject migration, folder movement, graph output publication, stale historical-pin replacement or new native relation is included.

Read-only follow-up by `/root/epic_scope_read` confirms that ProjectSelection, structural actions, source admission and Scope reads share the boundary gap. A correction belongs in declaration-path validation for both authority and Delivery, not every generic relative-path operation. It needs explicit owning-control identity and current Settings evidence, including revalidation. Current Core D363/D364 use named Settings files, while native helpers still use `caprmedio_project_settings.toml`; that binding mismatch must be settled before implementing a guessed boundary policy. Do not reject folders solely by prefix or require a complete foreign Project Structure before recognizing its Settings-defined identity.
