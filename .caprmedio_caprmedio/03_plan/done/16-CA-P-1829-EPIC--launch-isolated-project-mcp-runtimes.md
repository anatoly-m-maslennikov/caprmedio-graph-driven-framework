---
atom_id: CA-P-1829
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 16
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Done
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-09 03:46:50 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on:
    - "Project"
    - "Project Settings"
    - "Project Structure"
    - "Framework Instance Settings"
    - "Tool"
    - "Action"
    - "Workflow Run"
    - "Carrier"
    - "Evaluation"
    - "AI Agent"
    - "Operator"
relations: {}
---
# Summary

Launch isolated Project MCP runtimes

## Objective

the intended outcome is a Python launcher that gives the Operator an authenticated localhost MCP endpoint for the selected Project, using a compatible image **and** isolated reusable runtime state.

## Details

- scope: the Project MCP runtime launcher **and** the minimum selected-Project reader/state changes needed **to** support it. reuse the existing Python launcher under `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker`.
- intended flow: resolve Project, admit compatible image **or** build it **if** missing, reuse **or** start the selected runtime, discover the Docker-allocated localhost port, check authenticated readiness, **and** return the MCP URL.
- cover separate repositories **and** two named Projects **in** one repository. Project selection **and** runtime state **must** identify the selected Framework Instance, **not** merely the repository directory.
- the input path is the Project root folder. its `.caprmedio_<project>` folder is directly **in** that Project root. Projects **in** the same repository have their own Project root folders; the repository root is **not** an implicit Project selector. image build sources are a separate Framework input.
- the file **and** matching directory are the Carriers of this Epic; each contained Task stores its explicit `is_decomposition_of` Relation. prerequisite Tasks store `blocks`; numbering is navigation, **not** a second execution-order source.
- start with source RMED **and** the bounded O launcher Action, then test-first implementation, real-Docker proof, documentation, **and** independent final review. implementation Tasks **must not** silently bypass an unresolved authority conflict.
- leaf estimates are **`<=15`** minutes for **`=1`** AI Agent. **if** a leaf cannot remain within that boundary, decompose it **before** execution; preserve its Objective **and** DoD.
- retain one healthy runtime per selected Project by default. running-runtime replacement, worker startup, queue dispatch, a proxy service, **and** a full Release Version campaign are outside this Epic's startup authorization.
- use synthetic fixtures **and** accepted resource limits. secrets remain **in** admitted credential storage **and** separate from the URL **and** reports. existing runtime/HTTP capabilities **and** tests are inputs, **not** work **to** rebuild independently.
- authoring this Epic creates planned work **only**. this creation does **not** start a Task, build an image, change a running container, **or** advertise a live MCP URL.

### Definition of Done

the Plan is **not** Done **if** ((**any** decomposing Task is **not** Done) **or** (a required launcher behavior lacks applicable golden **and** real-Docker evidence) **or** (an unresolved Project-isolation, readiness, credential, image, **or** reuse finding remains) **or** (the packaged command **and** connection documentation are missing)).

- completion evidence: **all** **`=18`** decomposing Tasks are Done. the frozen Engine frontier `fd10b3e2f` has **`=60`** current passing host checks **and** a terminal exit-**`=0`** real-Docker proof for separate repositories **and** two Project roots in one repository: `.caprmedio_tmp/launcher-epic-1829/e2e/launcher-proof-0omrljbe/result.json`. the default command built the exact missing compatible image; authenticated startup, Project isolation, dynamic/explicit ports, safe refusals, reuse, **and** reload isolation passed. independent RMED/O, live-proof, **and** documentation/package reviews accepted the result. retained runtime N **and** every pre-existing Docker resource in the captured inventory remained unchanged; no fixture container remains. final mapping: `.caprmedio_tmp/launcher-epic-1829/final-review.md`.
