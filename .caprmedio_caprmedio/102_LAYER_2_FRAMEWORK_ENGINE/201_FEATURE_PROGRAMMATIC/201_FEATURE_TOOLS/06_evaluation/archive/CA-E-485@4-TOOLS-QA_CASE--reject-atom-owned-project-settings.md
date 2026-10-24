---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Settings
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Structure
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Projection
version: 4
updated_at: 2026-10-24 00:28:02 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1070
  - CAPRMEDIO-META-REQU-619
atom_id: CA-E-485@4
status: Archived
---
# Reject Atom-owned Project Settings

## Test case

retain valid authoritative Project Settings **and** Project Structure. add a project_settings map **to** an active Atom that attempts **to** select a Project Settings value, including a conflicting value **in** a separate fixture. run the Scope Unit Graph generator **without** granting authority **to** that map.

## Acceptance criteria

- report the attempted second Settings owner **and** do **not** publish Graph **or** Sources outputs from that invalid authority selection.
- do **not** accept the map because its Atom is called Configuration **or** because its value equals the authoritative value.
- Project Settings remains authoritative for its own selected values, **and** Project Structure remains authoritative for accepted declarations **and** bindings. neither Artifact is changed.
- this check does **not** prohibit an Atom from defining a parameter **or** a rule about Settings; it rejects an independent current-value owner.
