---
subjects:
  governs: project-settings
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Structure
  - Subject/Domain/Node/Continuant/Project.Settings
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Subject/Domain/Node/Continuant/Projection
version: 19
updated_at: 2026-10-24 01:18:03 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-M-149
  - CA-R-1070
atom_id: CA-E-167@19
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
---
# Bind admitted Scope Unit Graph sources in canonical order

## Test case

provide a fixed valid Project Structure Artifact with multiple accepted Scope Unit declarations **and** a fixed set of admitted Settings, Atom, directory-observation **and** Journal inputs. discover the input Carriers **in** different filesystem orders **without** changing their identities, content **or** declared structural **and** navigational order.

## Acceptance criteria

- **every** run emits the same Project Scope Unit Graph **and** Sources bindings **in** canonical source-identity order.
- Project Structure remains the sole authority for accepted declarations **and** bindings under CA-R-1070; an Atom-owned contribution map cannot redefine them.
- Project Settings **and** Framework Instance Settings retain their own selected-value authority; observations **and** generated views do **not** select Settings.
- filesystem enumeration order does **not** rewrite declared structural order **or** navigational order. **all** source Carriers remain unchanged.
