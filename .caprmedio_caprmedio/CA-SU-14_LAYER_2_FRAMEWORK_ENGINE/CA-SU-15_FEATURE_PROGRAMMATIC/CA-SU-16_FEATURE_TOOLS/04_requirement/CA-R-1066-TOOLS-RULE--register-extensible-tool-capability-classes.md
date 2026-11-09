---
atom_id: CA-R-1066
ref_id: CA-R-1066
container:
  scope_unit: CA-SU-16
role: Requirement
form: Rule
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication"
tier: 1
status: Active
version: 28
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Register extensible Tool capability classes

**every** Tool **must** register **=1** primary Tool kind: `finder` for strictly read-only retrieval **or** evaluation, **or** `doer` for governed mutation **or** materialization. `checker` is a registered Finder specialization that applies explicit Evaluation criteria **and** returns issues, evidence, **or** a verdict; additional specializations **may** extend a primary kind **only** through explicit registration of their semantics **and** interface obligations.

capability class is **not** an operation-semantics owner. the registered canonical Tool owns the behavior of its public operation; generic Artifact Tools own **only** form-agnostic mechanics, while CAPRMEDIO Markdown Atom Tools own Atom-specific identity, admission, lifecycle, **and** mutation behavior. a Doer **must** default **to** dry run **and** require explicit `--apply`; a Finder **must** never mutate.
