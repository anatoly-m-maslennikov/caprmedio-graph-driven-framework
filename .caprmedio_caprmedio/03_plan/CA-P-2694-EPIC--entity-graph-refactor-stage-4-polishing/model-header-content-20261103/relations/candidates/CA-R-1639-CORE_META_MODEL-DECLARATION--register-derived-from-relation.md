---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//DERIVED_FROM
  passive:
  - CAPRMEDIO_MODEL <+ Term//Artifact
version: 37
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1639
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
---
## Summary

Register derived_from relation

## Claim

### Formal Claim

```CFEL
Relation//DERIVED_FROM ((HAS_CLASSIFICATION)) Derivation == Direct;

$derived_content_version ((DERIVED_FROM)) $source_content_version
```

### Prose Claim

#### Applicability
direct derivation relations between exact represented content versions.

DERIVED_FROM means the directed Relation from a derived represented content version to an exact source content version used to derive it. Version references identify the relevant states; this does not introduce a Revision entity.

The Host is a derived represented-content version and the Target is the exact source content version used to derive it.
Forward `Host ((DERIVED_FROM)) Target` and reverse `Target <((DERIVED_FROM)) Host` are views of the same Relation fact.
DERIVED_FROM relates derived represented content version to exact source content version.
