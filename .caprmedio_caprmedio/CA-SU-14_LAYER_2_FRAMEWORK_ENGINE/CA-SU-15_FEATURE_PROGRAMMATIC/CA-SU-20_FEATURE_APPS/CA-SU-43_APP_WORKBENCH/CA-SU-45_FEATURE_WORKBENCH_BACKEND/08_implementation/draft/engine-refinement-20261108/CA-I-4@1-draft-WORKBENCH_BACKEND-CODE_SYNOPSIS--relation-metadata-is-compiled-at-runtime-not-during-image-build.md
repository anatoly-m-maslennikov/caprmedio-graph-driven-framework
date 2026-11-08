---
identity:
  id: CA-I-4
  ref_id: CA-I-4@1-draft
context:
  container:
    scope_unit: CA-SU-45
  role: Implementation
  form: Code Synopsis
  tier: 8
  topics:
    main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation
state:
  status: Draft
  version: 1
  updated_at: 2026-11-08 20:17:39 +0400
destination:
  file:
    name: CA-I-4@1-draft-WORKBENCH_BACKEND-CODE_SYNOPSIS--relation-metadata-is-compiled-at-runtime-not-during-image-build.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/08_implementation/draft/engine-refinement-20261108
author: Anatoly Maslennikov
---

## Summary

Relation metadata is compiled at runtime, not during image build

## Claim

### Prose Claim

At the code state identified below, Workbench builds its relation registry from captured Current Requirement declarations. The registry accepts the supported Declaration Forms, including Relation Declaration. It reads unqualified literal HAS_INVERSE bindings and the written counterpart notation. Both binding names must already be registered. It does not read IS_INVERSE_ALIAS_FOR bindings.

Materialization resolves an authored relation key to a registered name and adds the declared inverse. It does not normalize authored inverse writing to one canonical direct fact. Case-colliding registered names are warned about and omitted.

Image identity covers the selected framework files. Image context assembly copies those admitted inputs. Local release generates the code/config MCP tool registry while preparing its package. These build paths do not generate or verify a declaration-derived canonical relation registry asset.

## Details

The following Project-relative code locations and SHA-256 values identify the observed state. This describes implementation, not a test result.

| Code location | Area | SHA-256 |
| --- | --- | --- |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/relations.py` | registry_contribution, registry_from_contributions, _literal_bindings | `9d1161359a218ae52f9520c9b453659eff49e4bdb06863f0920cf605dc6b72c7` |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/source_reader.py` | SourceReader source capture and retained registry contributions | `fcb17ed7d9eb2e082a89907bfd4b06a2a66e0a11080b2955912cf1ec75c3917f` |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/incremental_relations.py` | incremental relation materialization | `59cc75e634e0daab27f2b1c3678b423427977e7d532e60d72f9f962d9fd5f49b` |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/docker/runtime_images.py` | ImageManager.identity and _assemble | `073a696ca96f4173e0a7c4296a47e5f6de0c3be3a8bf3594df6e6d4a71568dcf` |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_PROJECT_TOOLS/RELEASE_VERSION/release_support.py` | _prepare_package and _generate_tool_registry | `770a78fafea180cfecd1d3300eb9303dec61e0bd288f4408af573b2168f91913` |
