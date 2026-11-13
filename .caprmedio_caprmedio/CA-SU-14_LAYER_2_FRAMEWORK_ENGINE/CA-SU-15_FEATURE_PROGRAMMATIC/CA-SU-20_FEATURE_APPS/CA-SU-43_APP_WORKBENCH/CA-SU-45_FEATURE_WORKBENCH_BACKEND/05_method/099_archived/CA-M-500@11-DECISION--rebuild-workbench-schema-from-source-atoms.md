---
identity:
  atom_id: CA-M-500
  ref_id: CA-M-500@11
context:
  container:
    scope_unit: CA-SU-45
  role: Method
  form: Decision
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Schema
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2726
state:
  status: archived
  version: 11
  updated_at: '2026-11-12T01:59:14.433341+00:00'
destination:
  file:
    name: CA-M-500@11-DECISION--rebuild-workbench-schema-from-source-atoms.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method/099_archived
author: Anatoly Maslennikov
---
## Summary

Rebuild the Workbench schema from source Atoms.

## Claim scope

The schema asset and source tables used by WORKBENCH_BACKEND.

## Claim

### Prose Claim

Keep the Workbench schema a rebuildable asset, not a handwritten Python property list. Header/Markdown SQL names use dotted path levels and lowercase snake_case segments (`header.identity.atom_id`, `header.context.container`, `content.claim.formal_claim`); the asset, SQL interface, MCP results and `query_schema` use those same names.

Mode 1 derives canonical Header names and formats from the existing grouped Header carrier adapter and Current declarations, using accepted aliases only for reads and rejecting conflicts. `Header.ID` binds to `identity.atom_id`; timestamps retain existing offset-bearing `TIMESTAMPTZ` rules. Mode 2, enabled now, retains every observed raw Header path from valid sources—distinct source spellings stay distinct—while Content remains Current-model-declared. It retains empty paths, uses `header.context.container` JSON as the sole grouping-node exception, and exposes `header.relations` as one native direct/derived JSON projection. Neither mode adds a full Form validator or rewrites source Headers.

Generate `workbench_schema.json` at image build. Load it at startup and keep the declared Header and Content schemas fixed. Apply declaration changes by rebuilding the image. Report a missing or invalid asset; do not compile from live declarations as a fallback. Mode 2 observes Header paths from valid files at cold start. In both modes, ordinary data changes update the projection under the loaded schema.

On every image rebuild, regenerate the rebuildable query model and schema asset from Current Declarations, including Role and Form applicability, Content wildcards and more specific Content rules. Resolve applicable explicit property declarations, including inherited declarations, and retain exact provenance. Bracketed formats and conditions and wildcard constraints do not create named properties; observed headings and finite name lists are not declaration substitutes. A declared Content column remains in the schema when its current values are empty. This model supports queryable Content across Concern, Analysis & Advisory, Plan, Requirement, Method, Evaluation, Delivery and Operations without a fixed RMEDO or Claim-heading whitelist. Do not relabel other Roles’ bodies as Claims. Keep source files that can be parsed as separate Atom rows. Report schema violations and duplicate logical revisions through the audit tables. For model compilation, select eligible declarations and resolve competing declarations separately. Rereading data does not reload or compile the declared schema.


Generate declaration-derived model facts only from CFEL-labelled code blocks in `Content.Claim.Formal Claim`. Ignore `#` comments outside quoted strings, including section markers such as `# model`; comments are not declarations or parsing gates. Prose Claim, Semantics, Details, examples and Header Topics do not supply model facts. Source identity, lifecycle and provenance metadata may select and bind inputs. Mode 2 still observes factual Header data as separately admitted; that is not a substitute for declaration-derived model facts.
