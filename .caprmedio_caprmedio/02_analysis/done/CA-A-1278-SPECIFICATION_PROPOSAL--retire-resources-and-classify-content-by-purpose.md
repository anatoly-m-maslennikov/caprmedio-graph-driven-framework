---
atom_id: CA-A-1278
ref_id: CA-A-1278
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Model::CAPRMEDIO::Continuant/Package
tier: 3
status: Done
version: 3
updated_at: 2026-11-02 15:49:28 +0400
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Retire Resources and classify content by purpose

## Decision

Remove Resources: it is too broad to remain a primary kind. Prepare CA-R-2189 for retirement without a replacement umbrella.

Non-executable runtime/evaluation configuration, schemas, templates and fixtures are Assets. Instructions executed by an LLM are Prompts. Explanatory/reference material is Documentation. Classify actual content by purpose rather than filename or the broad word Resource.

Governing Configuration remains separate: it governs the Project or methodology rather than configuring an implementation runtime or evaluation.

## Prepared changes

- CA-R-2190 Configuration → Package>Asset/Configuration.
- CA-R-2191 Schema → Package>Asset/Schema.
- CA-R-2192 Template → Package>Asset/Template.
- CA-R-2193 Test Fixture → Package>Asset/Test Fixture.

These four retained Definitions cover non-executable implementation inputs. An executable Prompt is not an Asset merely because it is parameterized or stored as text. Documentation describing a schema or configuration is distinct from that schema or configuration itself.

## State

Four next-version Definition Drafts, the Asset Definition Draft, the Model proposal and thin migration tracking are prepared. Current definitions and repository implementation files are unchanged. Retirement and promotion remain pending.
