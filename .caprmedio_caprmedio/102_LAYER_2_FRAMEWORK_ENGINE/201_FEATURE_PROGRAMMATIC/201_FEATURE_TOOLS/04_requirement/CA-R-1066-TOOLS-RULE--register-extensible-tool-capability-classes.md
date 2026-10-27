---
subjects:
  governs: Subject/Graph Node/Engineering/Architecture/Communication
  depends_on: []
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 26
updated_at: 2026-10-27 06:04:45 +0400
atom_id: CA-R-1066
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
tier: 1
---
# Register extensible Tool capability classes

**every** Tool **must** register **=1** primary Tool kind: `finder` for strictly read-only retrieval **or** evaluation, **or** `doer` for governed mutation **or** materialization. `checker` is a registered Finder specialization that applies explicit Evaluation criteria **and** returns issues, evidence, **or** a verdict; additional specializations **may** extend a primary kind **only** through explicit registration of their semantics **and** interface obligations.

capability class is **not** an operation-semantics owner. the registered canonical Tool owns the behavior of its public operation; generic Artifact Tools own **only** form-agnostic mechanics, while CAPRMEDIO Markdown Atom Tools own Atom-specific identity, admission, lifecycle, **and** mutation behavior. a Doer **must** default **to** dry run **and** require explicit `--apply`; a Finder **must** never mutate.
