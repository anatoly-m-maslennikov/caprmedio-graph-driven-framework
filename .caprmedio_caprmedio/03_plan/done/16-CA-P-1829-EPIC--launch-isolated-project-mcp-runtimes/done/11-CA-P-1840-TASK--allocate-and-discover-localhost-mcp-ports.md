---
atom_id: CA-P-1840
content_role: Plan
type: Plan
label: Task
work_sequence_number: 11
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Done
author: Anatoly Maslennikov
version: 1
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
relations:
  is_decomposition_of:
    - CA-P-1829
  blocks:
    - CA-P-1841
---
# Summary

Allocate **and** discover localhost MCP ports

## Objective

the AI Agent makes Docker reserve the MCP host port **and** implements exact publication discovery.

## Details

- input: the admitted selected-Project namespace, compatible image, startup golden tests, **and** revised HTTP Delivery authority.
- output: Compose publication on `127.0.0.1` with Docker-owned allocation **and** a reader for the actual container/service/publisher mapping. preserve an explicitly selected port **only** **when** the reviewed contract admits it.
- verification: prove allocated-port discovery **and** rejection of missing, duplicate, non-loopback, wrong-service, **or** wrong-target-port mappings; avoid a scan-release-bind reservation race.
- effort: **`<=15`** minutes for **`=1`** AI Agent; the Epic's decomposition rule applies **before** execution **if** the estimate no longer holds.

### Definition of Done

- completion evidence: the exact single `8092/tcp` loopback publisher tests passed; the Docker backend observes the actual allocated port without reserving a socket or starting another service.

- reopened **after** independent final review: CA-O-188 **and** CA-M-356 admit an explicit port, **but** the Project startup path then exposed **only** dynamic allocation. preserve Docker-owned allocation by default; implement the admitted explicit-port branch, safe reuse mismatch, **and** failure without replacing unrelated resources.

the Plan is **not** Done **if** ((host-port selection requires an unreserved free-port scan) **or** (publication is admitted on a non-loopback address) **or** (the publisher-admission tests fail)).

- final completion evidence: `launcher-proof-0omrljbe/result.json` completed both layouts on frozen source `fd10b3e2f`. dynamic ports were `53331` **and** `53566`; explicitly requested ports `53342` **and** `53575` were published exactly **and** preserved on reuse. mismatched reuse returned `RUNTIME_MISMATCH`. occupied-port attempts returned the O188-permitted `DOCKER_PUBLICATION_FAILED` for exactly one healthy selected container with no host publisher, no ready URL, **and** no remap; scoped cleanup removed those resources while preserving the original runtime. host publisher/bounds tests pass, **and** production performs no free-port scan.
