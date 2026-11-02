---
subjects:
  active: CFEL <+ Relation//depends_on
  passive:
  - CFEL <+ Relation
  - Term//Artifact
  - CFEL <+ Relation//required_by
version: 30
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1026@30
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 1
role: Requirement
form: Relation Definition
---
## Summary

Register depends_on and required_by relation pair

## Claim scope

the `depends_on` **and** `required_by` relation pair.

## Claim

`depends_on` **means** a direct dependency-ordering relation from a dependent Artifact **to** its prerequisite Artifact, with `required_by` as its inverse-derived view. Plan start dependencies use the Plan Graph's `BLOCKS` under CA-R-1580 instead; this Relation Kind **must not** duplicate that scheduling fact.

### Formal claim

```text
CFEL <+ Relation//depends_on
CFEL <+ Relation//required_by
```
