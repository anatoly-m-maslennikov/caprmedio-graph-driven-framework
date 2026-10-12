---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Tool/ATOM_READ"
  depends_on:
    - "Atom"
    - "Artifact/Carrier"
    - "Scope Unit"
    - "Read Atom Carriers"
version: 13
updated_at: "2026-10-12 23:13:13 +0400"
relations: {"evaluation_for":["CA-R-864","CA-O-047"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify read selected caprmedio atom carriers

## Claim checked

CA-O-047 reads one logical Atom by its full ID and explicit Version and returns that complete state faithfully, without invoking Find or Modify or changing it.

## Applicable when

Apply before relying on the logical Read connector. These are required future checks; this source records no observed implementation pass.

## Test case

Prepare two identified Atoms and an archived historical Version of one. Independently read each exact ID/Version pair. Compare all returned Properties, sections and identity/lifecycle facts with independently authored expected complete states. A current-state request must not silently return a historical state, and a historical request must not silently substitute the current Version. The file adapter may use a physical locator internally; path, filename and filename stem are not substitutes for the logical ID/Version pair.

## Additional resolution cases

Request a missing ID, missing or wrong Version, ambiguous identity, unreadable state, unsupported output shape and denied read scope. Attribute each failure to the exact request; never guess or widen the selection. A list of reads is ordered independent requests: stop at the first failure, retain earlier returned states and leave later requests unperformed. Read performs no mutation. Find returns matches only, and no read result triggers Modify.

## Acceptance criteria

Each accepted result is the complete requested Atom state with its exact ID, Version and source-state evidence. Properties and sections are faithful; physical storage details do not change logical identity. Invalid or unresolved targets produce explicit failures, and every source byte and existing history item remains unchanged.

## Failure disposition

Reject on wrong identity/Version, incomplete content, hidden ambiguity, implicit Find/Modify, widened access or any mutation. Retain requests, expected/actual complete states, source pins and independent before/after observations.
