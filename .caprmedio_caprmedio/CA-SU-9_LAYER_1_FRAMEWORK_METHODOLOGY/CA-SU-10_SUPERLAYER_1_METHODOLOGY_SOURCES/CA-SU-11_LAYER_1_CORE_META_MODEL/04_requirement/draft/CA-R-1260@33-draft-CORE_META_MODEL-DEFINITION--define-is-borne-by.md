---
atom_id: CA-R-1260@33-draft
ref_id: CA-R-1260@33-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Relation Definition
topics:
  main_subject: Entity/Graph Syntax > Relation//IS_BORNE_BY
  dependencies:
  - Entity/Graph Syntax > Relation
  - Entity/Term//Dependent Entity
  - Entity/Dependent Entity
  - 'Entity/Object/Continuant/Projection/Type: Entities Graph'
tier: 1
status: Draft
version: 33
updated_at: 2026-10-29 21:54:09 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---
## Summary

Define IS_BORNE_BY

## Claim scope

an IS_BORNE_BY Relation from Entity A **to** Entity B **in** the Entities Graph.

## Claim

an IS_BORNE_BY Relation from Entity A **to** Entity B **in** the Entities Graph **means** that A is a Dependent Entity whose identity requires B as its immediate bearer.

### Formal claim

```text
Entity/Graph Syntax > Relation//IS_BORNE_BY
Entity/Graph Syntax > Relation//BEARS
```

## Semantics

Primary means that identity does not require another Entity occurrence as bearer. Dependent means that identity requires an immediate bearer, as expressed by IS_BORNE_BY. The proposed kind `Entity/Dependent Entity` classifies entities with that identity dependence; `Entity/Term//Dependent Entity` names its separate lexical Term. An absent edge in an incomplete view does not establish independence or remove source-established dependence.

The direct Relation is `X IS_BORNE_BY Y`, from the dependent entity X to its immediate bearer Y. The qualified path is `Y.X`, read from bearer to dependent. `Y BEARS X` is the derived inverse under CA-R-2416, not an additional independently stored fact. The canonical Relation name remains `IS_BORNE_BY`; the earlier conversational spellings do not create aliases. Generic prerequisite dependence does not establish bearer-qualified identity.

## Notation for subject

```text
.
```

## Details

This Draft incorporates the Operator-confirmed relational meaning and direct `Entity/Dependent Entity` kind. The kind and its separate lexical Method definition remain pending Draft dependencies, not Current admission. No Primary Entity branch is introduced.

### Withdrawn preparation — Property consolidation

The Operator approved IS_PROPERTY_OF and derived HAS_PROPERTY. New unallocated Relation Definition Drafts replace this proposed old-name successor; Current R1260 is not renamed or retired by this marker. The prior preparation is retained as historical review evidence. Do not promote this Draft as written or treat this marker as Current-source retirement.
