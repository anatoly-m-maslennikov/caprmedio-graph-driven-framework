---
atom_id: CA-R-1065
ref_id: CA-R-1065
container:
  scope_unit: CA-SU-16
role: Requirement
form: Rule
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage/Directory Layout"
tier: 1
status: Active
version: 28
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Separate project-local runtime and temporary state

**all** Tools **in** one CAPRMEDIO Project **must** use one project-local runtime rooted
at `.caprmedio_runtime/` **and** one project-local temporary-state root at
`.caprmedio_tmp/`. the runtime **contains** content-addressed executable releases,
shared non-executable libraries, machine-readable registries, declared
dependencies, stable launchers, Hook Carriers, logs, sessions, databases,
service state, **and** resumable state. the temporary-state root **contains** **only**
disposable scratch, staging, cache, build, Evaluation, atomic-write
intermediate, **and** interrupted-cleanup Carriers.

an installed Tool **must** import executable **and** non-executable implementation
**only** from its selected release under `.caprmedio_runtime/tools/`; it **must not**
import Framework implementation from the canonical source tree, the configured
Project control root, `.caprmedio_tmp/`, **or** another Project path. host
interpreters **and** Git remain declared substrate dependencies rather than copied
Framework implementation. a host-required discovery Carrier **may** point into
`.caprmedio_runtime/tools/`, but it **must** contain no independent Framework
behavior **and** **must not** become dependency authority.
