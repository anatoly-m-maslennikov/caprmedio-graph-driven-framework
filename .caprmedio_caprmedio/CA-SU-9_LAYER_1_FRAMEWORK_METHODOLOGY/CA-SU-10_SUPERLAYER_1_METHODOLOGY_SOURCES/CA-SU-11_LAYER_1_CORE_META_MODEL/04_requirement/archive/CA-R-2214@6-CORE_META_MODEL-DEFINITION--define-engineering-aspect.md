---
atom_id: CA-R-2214@6
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Aspect/Engineering
version: 6
updated_at: 2026-10-29 10:44:58 +0400
relations: {}
tier: 1
---
## Summary

Define Engineering Aspect

## Claim scope

Engineering Aspect in the Subject model.

## Claim

The retained detailed candidate also declares these reusable Engineering topics. Code Authoring concerns writing source code, with Python Code Authoring as its language-specific refinement. Data Handling covers parsing, serialization, retrieval and publication as well as selection, validation and transformation. Delivery concerns delivering capabilities and their changes; Extension Lifecycle and Git Commits narrow that topic without naming particular workflow instances. Recovery concerns resuming or restoring execution after interruption. Storage concerns representation layout. Verification distinguishes dynamic execution checks, static code analysis, test design, coverage and test data; Golden Corpora narrows Test Data. These topics classify governed concerns, not Scope Unit or Tool identities.

The Engineering Aspect addresses technical architecture, authoring, verification, delivery, storage, data handling, execution control, traceability and observability.

### Formal claim

```text
Engineering/Architecture
Engineering/Architecture/Communication
Engineering/Architecture/Communication/API
Engineering/Architecture/Component Structure
Engineering/Authoring
Engineering/Authoring/Controlled English
Engineering/Authoring/Prompt Authoring
Engineering/Data Handling
Engineering/Data Handling/Data Transformation
Engineering/Data Handling/Data Validation
Engineering/Data Handling/Source Selection
Engineering/Execution Control
Engineering/Execution Control/Decision Confidence
Engineering/Execution Control/Effect Authorization
Engineering/Execution Control/Failure Handling
Engineering/Observability
Engineering/Observability/Logging
Engineering/Observability/Monitoring
Engineering/Traceability
Engineering/Verification
Engineering/Verification/Coverage
Engineering/Verification/Static Analysis
Engineering/Verification/Test Design
Entity/Aspect/Engineering/Authoring/Code Authoring
Entity/Aspect/Engineering/Authoring/Code Authoring/Python Code Authoring
Entity/Aspect/Engineering/Data Handling/Output Publication
Entity/Aspect/Engineering/Data Handling/Parsing
Entity/Aspect/Engineering/Data Handling/Serialization
Entity/Aspect/Engineering/Data Handling/Source Retrieval
Entity/Aspect/Engineering/Delivery
Entity/Aspect/Engineering/Delivery/Extension Lifecycle
Entity/Aspect/Engineering/Delivery/Git Commits
Entity/Aspect/Engineering/Execution Control/Recovery
Entity/Aspect/Engineering/Storage
Entity/Aspect/Engineering/Storage/Directory Layout
Entity/Aspect/Engineering/Verification/Dynamic Testing
Entity/Aspect/Engineering/Verification/Static Analysis/Python Static Analysis
Entity/Aspect/Engineering/Verification/Test Data
Entity/Aspect/Engineering/Verification/Test Data/Golden Corpora
```

## Semantics

This names technical topics, not Tool or Scope Unit copies. Requirements can govern engineering outcomes; Methods can govern how those outcomes are achieved.
