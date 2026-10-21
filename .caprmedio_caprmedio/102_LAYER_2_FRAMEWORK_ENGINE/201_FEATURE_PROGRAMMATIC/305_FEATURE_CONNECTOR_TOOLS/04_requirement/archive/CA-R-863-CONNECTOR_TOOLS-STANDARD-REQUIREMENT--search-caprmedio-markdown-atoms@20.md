---
atom_id: CA-R-863
content_role: Requirement
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Tool/ATOM_SEARCH"
  depends_on:
    - "Atom"
    - "Artifact/Carrier"
    - "Scope Unit"
version: 20
updated_at: "2026-10-14 10:04:27 +0400"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Search CAPRMEDIO Markdown Atoms

## Scope

Explicit query operations of the ATOM_SEARCH connector, including its Markdown storage binding.

## Claim

The ATOM_SEARCH connector **must** execute a caller-supplied logical `query` through CA-R-1936-CONNECTOR_TOOLS-CORE-REQUIREMENT--use-one-coherent-connector-interface and CA-D-625-CONNECTOR_TOOLS-CORE-DELIVERY--deliver-coherent-connector-interface. It returns matching data and observed current source-state evidence; it does not choose the Workflow's target set or infer permission.

Accept explicit conjunctive filters for Scope Unit, Content Role, Type, direct `subjects.governs` or `subjects.depends_on` values, lifecycle and any requested narrower source frontier under the admitted query schema. The Workflow supplies defaults and any Active, non-archived or historical selection. The connector **must not** add a hidden lifecycle, whole-Project or ownership filter, silently widen the supplied query or perform Read or Modify as a Workflow effect.

Validate the supplied request, schema/context and any supplied source-state preconditions. A malformed or unsupported query fails without effects. For Subject matching, apply literal `exact`, `prefix`, `suffix` or `contains` only as explicitly requested. A supplied `legacy` or `approved` profile determines lexical syntax: legacy prefix boundaries are `/` and `:`; approved additionally recognizes `.`. Suffix and contains compare literal scalar text. Reject unsupported Subject syntax under the supplied profile without inferring ontology, relations or native endpoint admission. Do not choose a profile when one is required but absent.

Return stable ordered matches with the supplied projection, matching facts and actual source-state evidence. Expose invalid or unreadable selected source data and bounded/truncated coverage explicitly under the result schema; do not disguise either as complete successful coverage. Storage paths, Markdown parsing and physical lookup bindings remain connector details; logical Workflow targets are declared identities and query fields.

## Details

### Delivered direct Subject subset

CA-D-424 also declares a bounded direct read-only Subject lookup with explicit owning Scope Unit, Content Roles, lifecycle, profile, one field/value/mode criterion and optional full Atom IDs. Apply the narrow direct-call exception in CA-R-1936; do not require a Session or create Action Run or Journal records for this observation. An actual enclosing Workflow retains applicable Tool-call recording. Type, target Scope Unit, arbitrary projection and other generic Find filters are not supported by this direct subset and must be rejected rather than ignored. The broader requirements above remain separate and are not established by accepting this subset. Suffix and contains criteria may be literal fragments; complete selected source Subjects still require validation under the explicit profile.

CA-M-370 owns direct-field matching; CA-E-301 and CA-D-424 own validation and representation. The existing physical code binding under `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/` is not moved by this source revision. This is the required connector contract; current CLI behavior and historical fixture results do not establish its implementation.
