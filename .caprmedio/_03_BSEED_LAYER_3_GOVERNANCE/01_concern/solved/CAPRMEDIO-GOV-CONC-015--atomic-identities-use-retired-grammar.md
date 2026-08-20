---
artifact_subtype: problem
subject_scopes:
  - artifact-catalog
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CAPRMEDIO-GOV-REQU-300--semantic-immutability-and-lossless-recoding
      - CAPRMEDIO-GOV-REQU-303--optional-project-prefix
      - CAPRMEDIO-GOV-REQU-304--expandable-scope-path-identities
      - CAPRMEDIO-GOV-REQU-474--register-current-type-prefixes
      - CAPRMEDIO-GOV-CONC-014--atomic-carriers-are-not-role-local
---

# Problem — Atomic identities use the retired grammar

Active META and GOV atomic filenames still use legacy verbose identity shapes
such as:

```text
CAPRMEDIO-META-REQU-239--total-one-to-one-semantic-route-catalog.md
```

They do not yet use the accepted shape:

```text
<PROJECT>-<SCOPE_PATH>-<TYPE_PREFIX>-<NNN>[-<SUBTYPE>]--<SUMMARY>.md
```

No active META or GOV atomic filename currently uses the required `--`
identity-to-summary separator. Existing relations and frontmatter therefore
also retain the legacy identities.

The migration must be one lossless whole-graph cutover across active and
archived carriers, relation targets, QA, implementation references, evidence,
and commit-provenance consumers. Partial aliasing or mixed current grammars are
not acceptable.

## Primary claim

The active and archived atomic graph still uses the retired identity grammar
instead of the accepted four-character Type-prefix grammar.

## Rationale

Recording the gap avoids presenting a prospective naming requirement as
already implemented and prevents a piecemeal rename from creating two current
identity vocabularies.
