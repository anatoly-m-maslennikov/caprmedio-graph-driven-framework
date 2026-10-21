---
atom_id: CA-P-2561
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Done
version: 2
updated_at: "2026-10-21T19:05:01Z"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2557]
  depends_on: [CA-P-2558, CA-P-2559, CA-P-2560]
  relates_to: [CA-M-396, CA-M-397, CA-M-398, CA-M-399, CA-M-400]
---
# Summary

Verify shared error-handling functional contracts

## Objective

Review and exercise the bounded functional matrix across shared sync/async handling, Tool/MCP public callers and AtomSearch partial responses. Use self-contained fixtures; verify code/response/log severity distinction, safe context, cancellation, one invocation, no retry and no technical Journal records.

## Details

One Task per file. After completion, review and update dependant Tasks before their execution. Actual business Workflow lifecycle recording remains with its declared executor; this Task does not invent it in an error decorator.

### Definition of Done

Retain exact focused commands/results and independent review; update next tasks from observed gaps. No full suite, live production test or deployment. At most 15 minutes own work.

### Execution checkpoint

Reviewed predecessor fixes and the frozen integration before final acceptance. The retained focused portfolio contains 117 unique passing cases across ten modules: 64 Tools/core/AtomSearch/CLI and 53 MCP. The initial Tools run had one stale expected empty-error assertion; corrected the assertion, not the implementation, and reran its 10-case provider module successfully. The final synthetic-warning suffix fix then passed a 32-case broken/related rerun in 1.823 seconds. These repeated cases are not added to the 117 unique-case total. Independent final review: APPROVED; no remaining bounded blocker. Core/logger Ruff and changed-file F checks pass. Existing non-failing TemporaryDirectory ResourceWarnings are not silent failures. No full suite, production endpoint test, Docker build, release, deployment or push.

### Exact focused commands

```sh
.caprmedio_runtime/launcher-venv/bin/python -B -m unittest 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_operation_error_boundary.py 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/tests/test_invalid_atom_schema_warnings.py 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/tests/test_runtime_warning_logging.py 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/tests/test_atom_operations.py 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/tests/test_subject_lookup_provider.py

.caprmedio_runtime/launcher-venv/bin/python -B -m unittest 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests/test_public_tool_error_contract.py 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests/test_registered_tool_registry.py 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests/test_implementation_server.py 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests/test_selected_routes_mcp.py 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests/test_direct_subject_lookup_protocol.py

PYTHONPATH=102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/tests .caprmedio_runtime/launcher-venv/bin/python -B -m unittest 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/tests/test_subject_lookup_provider.py

.caprmedio_runtime/launcher-venv/bin/python -B -m unittest 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_operation_error_boundary.py 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests/test_public_tool_error_contract.py 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/tests/test_invalid_atom_schema_warnings.py 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/tests/test_runtime_warning_logging.py
```
