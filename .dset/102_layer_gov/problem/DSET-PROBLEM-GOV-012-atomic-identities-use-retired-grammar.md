---
artifact_type: problem
artifact_id: DSET-PROBLEM-GOV-012
scope_path: layer:gov
subject_scopes:
  - artifact-catalog
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - DSET-REQUIREMENT-GOV-108
      - DSET-REQUIREMENT-GOV-113
      - DSET-REQUIREMENT-GOV-114
      - DSET-REQUIREMENT-GOV-119
      - DSET-PROBLEM-GOV-011
---

# Problem — Atomic identities use the retired grammar

Active META and GOV atomic filenames still use legacy verbose identity shapes
such as:

```text
DSET-REQUIREMENT-META-070-total-one-to-one-semantic-route-catalog.md
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
