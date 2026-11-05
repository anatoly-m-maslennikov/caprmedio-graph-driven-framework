---
atom_id: CA-P-006
ref_id: CA-P-006
container:
  scope_unit: CA-SU-00
role: Plan
form: Plan
tier: 3
status: Canceled
version: 2
updated_at: 2026-10-24 06:26:31 +0400
artifact_subtype: change_plan
priority: medium
author: Anatoly Maslennikov
current_scope_unit: caprmedio
---

# Establish Projection generation subtypes

1. Projection has two subtypes: `programmatic-generated` and `llm-generated`.
2. Example for `programmatic-generated`: list of Rs grouped by subject and
   ordered by tier (Principle → Core → Standard).
3. Examples for `llm-generated`:
   - Mermaid scheme about some entity lifecycle.
   - Entry/exit criteria for each entity status/state.
   - The actual code (I).
