---
atom_id: CA-E-587
content_role: Evaluation
type: QA Case
current_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-11 16:51:04 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Sealed suite reference-context QA"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Project Structure, Operator, Workflow, Action, Source Carrier, Digest, JUnit Report]
relations:
  evaluation_for: [CA-R-1887, CA-M-344, CA-D-580, CA-D-579]
---
# Summary

Verify sealed Release-suite reference context and currentness

## Scope

Positive and refusal checks for private control-reference capture, read-only workspace copying, and post-run revalidation.

## Claim

The QA case **must** prove that the Suite Owner passes only with one exact, allowlisted, read-only reference closure bound to the trusted candidate, compiled root, selected N, and image context; every changed or injected control reference is non-passing.

## Details

Verify a positive local closure containing the generated release-only execution snapshot, Operator registry, Project settings, Project Structure, current CA-D-572 and exact captured Workflow, Step, Action and RMED pins, and the two Unit-deadline settings carriers. Assert typed source-path ordering, exact byte SHA-256 and mode verification, canonical `control_context_digest`, workspace copy preservation, and its inclusion in actual suite evidence and the schema-2 envelope. Each admitted filesystem pin is captured from its current carrier at Run start; identical shared pins occur once. The generated snapshot row is materialized only in the private reader/workspace, with no Project control carrier write.

Independently reject an empty, duplicate, unknown, caller-added, runtime, Journal, secret-shaped, absolute, escaping, symlinked, non-regular, unreadable, wrong-mode, stale-digest, or tampered captured-definition row. Mutate a protected settings root or captured release-definition byte between capture and execution, and again before post-run verification; neither case may pass or replay. Reject candidate SHA, compiled-root, selected-N, or image-context mismatch. Verify no arbitrary caller file reaches the workspace, no control carrier is written, and failure retains N and truthful non-passing evidence.

Reject caller-added bindings, changed generated snapshot bytes, missing captured Atom pins, duplicate declarations and conflicting shared pins. A later authoring revision must not replace the captured release bytes. Verify that unrelated Prompt bindings, fixed selected-source refresh pins and the legacy multi-route manifest are not required for this local context. Their independent Tools and tests retain their own authority. Verify the unchanged schema-1 member set and retained N proof remain readable, without admitting obsolete Plan carriers or expanding to an entire Project folder; the complete declared suite and candidate source/image gates remain required.
