---
cce_version: cce_1
cce_form: method
version: 21
updated_at: 2026-10-29 07:17:15 +0400
relations:
  child_of:
  - CA-M-261
subjects:
  governs: Entity/Object/Continuant/Package/Project Implementation
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Method'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Evaluation'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery'
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-262@21
status: Archived
content_role: Method
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Implementation Method
tier: 2
---
# Preserve sufficient authority for reconstruction

**to** rebuild the Implementation, use the current RMED as sufficient authority for reproducing its required behavior **and** passing its applicable Evaluations **without** the previous Implementation **or** additional specification preparation; **if** the implementation language changes, **then** update the affected Method **and** Delivery authority **before** rebuilding against the resulting current RMED. a ready-made alternative Implementation is **not** required.

under unchanged governing RMED, reconstruct runtime behavior that produces the same output for the same complete runtime input, including relevant starting state, configuration, time, randomness, **and** external-service responses. preserve the applicable Method **and** Delivery constraints; identical source code **or** identical source-file bytes are **not** required. judge fresh reconstruction **and** repeated implementation by this runtime equivalence, **not** by a requirement **to** leave already-conforming code untouched. an authorized RMED change establishes a new comparison baseline **and** **must not** be reported as reconstruction against unchanged RMED.
