---
subjects:
  governs: Subject/Graph Node/Engineering/Architecture/Communication
  depends_on:
  - Subject/Graph Node/Implementation/Code/Tool
  - Subject/Graph Node/Domain/Continuant/Projection
version: 29
updated_at: 2026-10-27 06:04:45 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  method_for:
  - CA-R-1063
  - CA-R-1064
  - CA-R-1065
  - CA-R-1066
  - CA-R-1067
atom_id: CA-M-144@29
status: Archived
content_role: Method
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eng Policy
tier: 2
---
# Route and invoke Tools through the common CLI

use this flow for **every** Tool invocation:

1. the LLM declares the intended capability **without** naming an implementation; the router classifies it as `finder` **or** `doer` **and** **may** refine it **to** a registered subtype such as `checker`.
2. the router resolves as many registered decision steps as required **and** returns **every** applicable Tool with identity, purpose, inputs, preconditions, effects, success checks, failure modes, command shape, **and** representative examples.
3. **after** the LLM selects one Tool, pass either composable structural-unit, Type, **and** subtype filters **or** explicit canonical Atom filenames through the common target selector **and** return the resolved target set **before** execution.
4. execute the selected Tool from its selected immutable release under `.caprmedio_runtime/tools`. use other owned `.caprmedio_runtime/` descendants for persistent logs, sessions, databases, service state, **and** resumable state. use `.caprmedio_tmp/` **only** for disposable scratch, staging, caches, builds, Evaluations, atomic-write intermediates, **and** cleanup remnants. **every** Finder, including **every** Checker, receives no mutation capability **and** **must not** mutate authoritative sources **or** derived outputs, while **every** Doer first returns a complete mutation-free dry run **and** **then** writes **only** its declared authoritative source **or** derived output **after** explicit application.
5. return the common result envelope, stable diagnostics, exit status, resolved targets, observed effects, **and** applicable currentness information.
