---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Read Atom Carriers"
  depends_on:
    - "Action"
    - "Tool/ATOM_READ"
    - "Atom"
    - "Artifact/Carrier"
    - "Scope Unit"
version: 3
updated_at: "2026-10-12 23:17:22 +0400"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Read selected CAPRMEDIO Atom carriers

Read Atom Carriers **means** the reusable read-only Action that returns the full faithful logical Atom for one explicitly supplied Atom ID and Version under CA-R-864. It is callable independently of Find or Modify; missing or ambiguous identity never permits another target to be substituted.

## Action

1. resolve exactly the supplied Atom ID and Version against the declared owning Scope Unit and current or historical authority selected by the request. Do not use a path, filename stem, hidden search, guessed latest Version or reference retargeting as a public selector.
2. recheck the exact identity and source evidence and read the complete Atom, including all Properties and Sections, once. Preserve source values and attribution; do not normalize or repair them.
3. return the full Atom ID, Version, owning Scope Unit, Properties, Sections and current or historical lifecycle meaning. Optional private Carrier display is diagnostic evidence, not a replacement for the logical result or part of its public targeting contract.
4. for an explicit ordered list, return each successful full read separately. Stop at the first failed read, preserve earlier results and leave later targets unread; do not widen any selector or fabricate an all-or-nothing result.

## Outcome and stops

Return the exact full Atom or the precise missing, ambiguous, stale, unreadable or out-of-scope outcome. No Find prerequisite, write, mutation, implicit substitution, runtime capability or new recovery policy follows from this definition.
