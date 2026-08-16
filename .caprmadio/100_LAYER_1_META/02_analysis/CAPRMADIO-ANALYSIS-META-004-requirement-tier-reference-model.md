---
artifact_type: analysis
artifact_id: CAPRMADIO-ANALYSIS-META-004
scope_path: layer:meta
subject_scope: authority
relations:
  analysis_of:
    - CAPRMADIO-REQUIREMENT-169-classify-rmad-atoms-by-applicability-tier
    - CAPRMADIO-REQUIREMENT-GOV-162-encode-rmad-applicability-tiers
    - CAPRMADIO-PLAN-008--complete-rmad-tier-parent-links
---

# Requirement tier reference model

## Question

How should Principle, Core, and Standard Requirements refer to one another, and what must be added when the required parent tier is missing?

## Analysis

The proposed structure makes the tier hierarchy explicit: Core Requirements refer upward to Principle Requirements, while Standard Requirements refer upward to Core Requirements. This produces a direct, inspectable chain of Principle → Core → Standard instead of relying only on derived inheritance.

The restriction should apply to the hierarchical parent reference, not to every relation on a Requirement. Replacement, currentness, analysis, implementation, and other precise relation kinds may legitimately target artifacts outside the parent tier. Treating every relation as a tier reference would erase those independent meanings.

The current applicability rule says that Core obeys applicable Principles and Standards obey applicable Principles and Core rules, but that this inheritance is derived and should not be duplicated as blanket relations. Explicit parent references therefore require changing that rule rather than silently adding contradictory links.

Missing Principle and Core Requirements should be added where the hierarchy has a real semantic gap. A Principle should express the broader invariant that constrains its Core children. A Core Requirement should express the complete rule for its declared scope and provide the direct parent needed by narrower Standard Requirements. Placeholder parents created only to satisfy structure would add no governed meaning.

Historical archived Requirements should retain their original relations. The new hierarchy applies to the current Requirement model and should not rewrite preserved history merely to make old carriers match the new rule.

## Conclusion

Use the hierarchical parent relation for direct Principle-to-Core and Core-to-Standard references, preserve other relation kinds for their own meanings, and add missing Principle or Core Requirements only when they carry necessary upstream authority.
