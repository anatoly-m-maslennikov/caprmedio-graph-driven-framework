---
atom_id: CA-R-863@24
content_role: Requirement
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
author: Anatoly Maslennikov
status: Archived
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Tool/ATOM_SEARCH
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Scope Unit
version: 24
updated_at: 2026-10-24 00:38:25 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
tier: 3
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

### Individual schema-invalid Atom disposition

When one selected Atom fails schema validation but the scan can still preserve its
source frontier and safety checks, omit only that Atom, continue the bounded scan,
and return the valid matches with a technical warning containing the repository-
relative path and reason. The result **must** set `complete: false`; the warning
must not be presented as complete successful coverage. This warning is diagnostic
evidence, not a business Journal record, and it does not authorize repair or any
mutation. Fatal I/O, security, duplicate-identity, stale, ambiguous, or otherwise
incomplete-frontier conditions remain refusal/error dispositions with no partial
successful result.

## Details

### Delivered direct Subject subset

CA-D-424 also declares a bounded direct read-only Subject lookup with explicit owning Scope Unit, Content Roles, lifecycle, profile, one field/value/mode criterion and optional full Atom IDs. Apply the narrow direct-call exception in CA-R-1936; do not require a Session or create Action Run or Journal records for this observation. An actual enclosing Workflow retains applicable Tool-call recording. Type, target Scope Unit, arbitrary projection and other generic Find filters are not supported by this direct subset and must be rejected rather than ignored. The broader requirements above remain separate and are not established by accepting this subset. Suffix and contains criteria may be literal fragments; complete selected source Subjects still require validation under the explicit profile.

CA-M-370 owns direct-field matching; CA-E-301 and CA-D-424 own validation and representation. The existing physical code binding under `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/` is not moved by this source revision. This is the required connector contract; current CLI behavior and historical fixture results do not establish its implementation.
