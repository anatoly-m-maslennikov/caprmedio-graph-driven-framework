---
subject_scopes:
  - runtime
version: 3
updated_at: 2026-08-20 21:21:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-158--make-journals-canonical-for-governed-provenance
    - CAPRMEDIO-META-REQU-110--bind-governed-transactions-to-stable-artifact-revisions
---
# Register Work Journal events

GOV must register `started`, `progressed`, `completed`, `failed`, `interrupted`, `abandoned`, and `recovered` Work Journal events. Every newly accepted schema-version `2` event identifies its `event_id`, `action_id`, lifecycle `event`, `kind`, full GitHub `author`, timezone-qualified `occurred_at`, session provenance, and structural scope. `preceding_event`, when present, links lifecycle events inside one action and must not be used as an Artifact-state predecessor. Commit and pull-request provenance remain optional bindings.

A `governed_file_change` event is one `completed` event with:

- `action_type` equal to `ADD`, `MOVE`, `UPDATE`, `MOVE+UPDATE`, or `REMOVE`;
- `sources`, a deterministically ordered array containing every direct typed upstream reference exactly once as `relation_type`, source `filename`, and source `version`, or an empty array when none exists;
- singular `result`, identifying the one governed subject outcome by `state`, `filename`, and `version`; a `present` result also requires its resulting repository-relative `path` and `sha256`, while a `removed` result omits them; and
- `previous_result_event`, omitted for an `ADD` or first known state and otherwise identifying the latest accepted event whose `result` is the state immediately before this result.

When an existing governed subject has no prior accepted result event, a separate `recovered` `governed_file_state` event may establish the evidenced prior `result` under the Work Journal recovery rule; the change event then names that event as `previous_result_event`. A file-change or file-state event must not store `action_message`, `before_path`, `before_sha256`, or another copy of prior result state. The canonical Git message is a deterministic Projection of the structured change event and its referenced previous result when the change syntax requires the prior carrier address. Previously accepted events remain valid under their declared schema version.
