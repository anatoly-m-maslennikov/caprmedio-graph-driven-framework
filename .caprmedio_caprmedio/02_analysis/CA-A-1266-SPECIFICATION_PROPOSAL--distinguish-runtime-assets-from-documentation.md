---
atom_id: CA-A-1266
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Formal Model
version: 1
updated_at: 2026-10-28 23:28:59 +0400
relations: {}
tier: 3
---
# Summary

Distinguish runtime Assets from Documentation

## Decision

Asset is a file-level, non-executable Implementation item necessary at runtime. Documentation is also non-executable Implementation content, but documents the project/framework and is not necessary for that runtime. Documentation is therefore not a subtype of Asset under this distinction.

Use separate Package parts:

```text
Package > Asset
Package > Documentation
```

This narrows the former Asset definition that included all non-executable Implementation content. Prompt remains executable instructions for an LLM AI Agent engine; Module remains executable on a language engine. Logical items remain distinct from their Carriers.

## Resources disposition

The old Resources definition covers non-Code/Prompt/Documentation data used to construct, configure, evaluate or render a result. Its current examples include Configuration, Schema, Template and Test Fixture. That umbrella is broader than the new runtime-only Asset boundary. Keep it in the unresolved list until its members are classified; do not silently rename all Resources to Asset or retire their definitions.

The remaining question is whether runtime includes build/test tool runtimes or only the running product. Do not choose that scope or reclassify those remaining members without the Operator's answer.

## State

Asset and Documentation Definition Drafts and the proposal tree are updated. Current definitions and implementation files remain unchanged.
