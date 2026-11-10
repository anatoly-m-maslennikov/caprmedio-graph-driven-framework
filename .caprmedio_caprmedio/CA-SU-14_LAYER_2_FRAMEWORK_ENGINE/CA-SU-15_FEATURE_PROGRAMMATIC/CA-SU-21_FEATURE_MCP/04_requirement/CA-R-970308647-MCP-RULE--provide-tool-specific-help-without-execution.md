---
atom_id: CA-R-970308647
ref_id: CA-R-970308647
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication
tier: 1
status: Active
version: 1
updated_at: 2026-11-11 00:16:05 +0400
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-R-970308647-MCP-RULE--provide-tool-specific-help-without-execution.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
---

## Summary

Provide tool specific help without execution

## Claim

### Prose Claim

Every public MCP Tool must accept `help: true` without requiring its normal business inputs. For an admitted Tool and valid trusted Project binding where applicable, return only that Tool's purpose and when to use it, input parameters including format and allowed values, minimal examples, output contract, and common errors. The response must describe that specific Tool, not a general catalog or another Tool.

Handle help before normal business input validation and execution. Help must not run the Tool, start a Workflow, issue a query or query run, write source, invoke an approval or other business gate, or create a business Journal Run. Technical diagnostics may be recorded. Preserve the trusted Project binding envelope and reject missing, unknown or mismatched binding as applicable; never fall back across Projects. Apply the global blacklist and bound Project exclusions before providing help: unavailable or excluded Tools must not expose their capability through help.

Each generated public input schema must admit the `help: true` request shape with the framework Project binding envelope where required, without normal business-required fields, so protocol schema validation accepts it before the shared help handler runs.
