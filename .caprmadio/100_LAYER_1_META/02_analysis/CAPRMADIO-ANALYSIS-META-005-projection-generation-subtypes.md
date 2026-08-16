---
artifact_type: analysis
artifact_id: CAPRMADIO-ANALYSIS-META-005
scope_path: layer:meta
subject_scope: artifact-model
relations:
  analysis_of:
    - CAPRMADIO-REQUIREMENT-META-137-use-implementation-record-as-a-projection
    - CAPRMADIO-REQUIREMENT-META-154-three-artifact-forms-with-generated-projections
    - CAPRMADIO-REQUIREMENT-GOV-133-govern-catalog-map-and-hub-projections
    - CAPRMADIO-REQUIREMENT-GOV-151-register-implementation-record-projection
    - CAPRMADIO-PLAN-009--establish-projection-generation-subtypes
---

# Projection generation subtypes

## Question

How should programmatic-generated and LLM-generated Projections differ, and how do the proposed examples fit the existing Projection and Implementation boundaries?

## Analysis

The two subtypes distinguish how a Projection is produced. A programmatic-generated Projection is produced by deterministic code over declared inputs. An LLM-generated Projection is produced through model inference over declared inputs and therefore needs the model, prompt, configuration, and generation provenance in addition to its source frontier.

The Requirement list grouped by subject and ordered Principle → Core → Standard is a natural programmatic-generated Projection. Its grouping and ordering can be reproduced exactly from Requirement metadata without adding new semantic claims.

A Mermaid entity lifecycle and entry/exit criteria for every entity state or status are natural LLM-generated Projections when they synthesize an already governed model. They remain views: if the generated diagram or criteria introduce a new state, transition, obligation, or criterion, that new meaning must first be governed in an authoritative Atom.

Actual generated code has a different boundary. When the LLM writes executable code into the repository, that code is native Implementation rather than a Markdown description of Implementation. An LLM-generated Projection can show its source-to-code bindings, generation provenance, currentness, and coverage, but a code block inside the Projection is not a substitute for the actual Implementation.

This means the actual-code example has two connected outputs: native code in the Implementation location and an LLM-generated Implementation Projection describing how that code was derived from the governed source frontier. The distinction preserves both the reality of the code and the reproducibility of the generated view.

## Conclusion

Use programmatic-generated for deterministic projections and LLM-generated for model-produced projections. Keep generated diagrams and criteria non-authoritative views of governed sources, and treat generated executable code as native Implementation accompanied by an LLM-generated Projection of its lineage and currentness.
