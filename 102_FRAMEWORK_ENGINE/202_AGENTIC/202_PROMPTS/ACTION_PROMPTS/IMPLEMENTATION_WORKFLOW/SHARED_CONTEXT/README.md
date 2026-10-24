# Shared implementation Step prompt definitions

This folder is a **definition-only** prompt package for the current
Implementation Workflow graph. Native realization is pending. These files are
not admitted to the existing adapter, are not a replacement for the parent
Workflow's source bindings, and **must not be dispatched through the old
adapter**.

## Common input packet

Every prompt receives one complete, caller-owned packet. The prompt may read
the packet but cannot expand it, infer missing authority, or replace it with
the prompt package's own files:

- `selected_project`: the frozen Project binding and its current source
  references;
- `plan`: the selected persistent Plan (P/Plan), including its instruction,
  owner, dependencies, source context, and Definition of Done;
- `requirements_and_delivery`: the selected R/D targets, with complete
  frontmatter, Markdown, identity, revision, path, digest, and independently
  validated source binding;
- `methods`: the complete current active-M **SourceRows** for the declared
  input universe. Every row carries its Atom ID, version, project-relative
  path, SHA-256, complete frontmatter, and complete Markdown body. These rows
  are the canonical Method input and are validated independently against the
  selected Project source root;
- `method_projection` (optional legacy): a derived compatibility projection
  may accompany `methods`, but is not required and cannot replace, summarize,
  or authorize the canonical Method SourceRows. No paragraph compiler or
  generation step is required to produce the canonical Method input;
- `applicable_evaluations`: the applicable E Atoms and their complete source
  bindings, kept separate from R/D and M and independently validated against
  the selected Project source root;
- `source_revisions`: the current Workflow, Step, Action, R/D, M, and E
  revisions and hashes actually read for this invocation;
- `candidate`: the candidate identity, owned paths, phase, and retained
  implementation state;
- `permissions`: the caller-granted capabilities and allowed commands;
- `retry`: the effective limit, consumed count, provenance, and current
  admission state;
- `evidence`: actual test, diagnosis, handoff, and retained-run evidence.

At initial CA-O-231 preparation, `plan` may explicitly state that no Plan was
supplied; CA-O-017 then creates the admitted persistent Plan before code work.
Later implementation Steps require that admitted Plan binding. This package
does not change standalone CA-O-223's separately admitted input forms.

Every contract in this folder declares `Integrated` context. That context is
authoritative for its Step and is not inherited from the Workflow. Do not
dispatch a future Step, grant hidden permissions, create release effects, edit
authority, or claim a result for an unperformed check. A missing, stale,
conflicting, incomplete, or unauthorized packet returns the Step's blocked or
unresolved result.

## Authority, applicability, and trace branches

The selected Project's authorized source root is the only authority boundary.
Validate each applicable parent R/D/E/Method source row independently by its
current Atom ID, version, relative path, SHA-256, and complete source bytes;
never authenticate one source row from another row, a projection, a prompt
file, or an aggregate hash. A projection may enumerate candidates but has no
authority and does not make an unrelated parent or child applicable.

When an implementation trace is required, use only current Atom IDs and the
role lines `Requirement:`, `Method:`, `Evaluation:`, and `Delivery:`. Select
the narrowest direct leaf for each independent `child_of` or `parent_of`
branch, include applicable policy leaves such as error, retry, or logging
rules, omit an ancestor already covered by that leaf, and preserve separate
blocks for independent branches. Many-to-many realization is valid only when
each cited branch is substantive.

## Integrated continuation handoff

An Integrated prompt that returns a pending handoff is still an in-progress
Step, not a completed Step. The main session or its assigned subagent performs
the supplied work, then submits the result through the same MCP operation
`submit_result`, bound to the retained Run/Step/Action and continuation. Only
that accepted submission can produce the next prompt. A pending handoff does
not complete the Plan, bypass test-first preparation, replace evidence,
consume or reset retry accounting, or skip the declared review phase.

## Status

These definitions are staged for review. `definition_frontier.projection.json`
records the published Workflow/Step/Action definition frontier only, not a native
binding or runtime admission. Revalidate its exact sources before use; resolve
current R/M/E/D SourceRows and refresh derived views for each invocation. In
particular, do not add this folder to production `source_bindings.json` as a
shortcut or use an old Method snapshot after source revisions change.

## Definitions

| Step | Action | Context | Definition |
| --- | --- | --- | --- |
| CA-O-231 | CA-O-017 | Integrated | [prepare work](CA-O-231.prompt.md) |
| CA-O-232 | CA-O-018 | Integrated | [prepare tests](CA-O-232.prompt.md) |
| CA-O-233 | CA-O-019 | Integrated | [implement requirements](CA-O-233.prompt.md) |
| CA-O-094 | CA-O-020 | Integrated | [run checks](CA-O-094.prompt.md) |
| CA-O-234 | CA-O-089 | Integrated | [diagnose](CA-O-234.prompt.md) |
| CA-O-096 | CA-O-024 | Integrated | [admit retry](CA-O-096.prompt.md) |
| CA-O-099 | CA-O-021 | Integrated | [repair](CA-O-099.prompt.md) |
| CA-O-230 | CA-O-225 | Integrated | [review candidate](CA-O-230.prompt.md) |

CA-O-230 reuses the CA-O-225 read-only review semantics. Its `final` phase
keeps CA-O-225's default result behavior. Its explicit `preliminary` phase
may return `preliminary_clear`, but `preliminary_clear` is not `passed` and
cannot admit completion.
