---
atom_id: CA-P-032@6
cce_version: cce_1
cce_form: classification
subjects:
  governs:
    continuant:
    - Actor/Type
  depends_on:
    continuant:
    - Actor
    - Type
    - Operator
    - AI Agent
version: 6
updated_at: 2026-10-24 06:04:21 +0400
relations:
  child_of:
  - ANATOLY-MASLENNIKOV-DEFINES_GOAL_FOR-CAPRMEDIO--create-and-evolve-a-working-caprmedio-framework
status: Archived
author: Anatoly Maslennikov
current_scope_unit: caprmedio
tier: 3
---
# Distinguish human Operators from AI Agents

**every** Actor that performs **or** authorizes a governed action **must** have **`=1`** Type **in** (Operator, AI Agent).
