---
subjects:
  governs: Subject/Graph Node/Engineering/Authoring/Prompt Authoring
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Engineering/Authoring/Prompt Authoring
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action/Execution Kind: Agentic'
  - Subject/Graph Node/Domain/Occurrent/Execution
version: 18
updated_at: 2026-10-27 06:04:45 +0400
relations:
  method_for:
  - CA-R-1789
  - CA-R-1790
  - CA-R-1791
  - CA-R-1792
  - CA-R-1793
atom_id: CA-M-304@18
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Implementation Method
tier: 3
---
# Summary
Write self-contained agentic Action instructions

## Scope
derived instructions that present an Agentic Action for execution.

## Claim

**to** present an Agentic Action for execution, organize its derived instruction around the declared responsibility rather than assumed session memory.

- state the requested outcome, relevant context, exact targets, inputs, available evidence, **and** governing references.
- distinguish already performed effects from proposed changes, **and** existing permissions from decisions still needed.
- state the expected result **and** how **to** report uncertainty, failures, partial effects, **or** a request for Operator input. do **not** treat a suggested correction as permission **to** apply it.
- keep the instruction limited **to** the bound Action. leave next-Step selection **and** cross-Workflow handoff coordination **to** the executor using the governing Workflow.
- use understandable wording **and** structured points under CA-M-301-CORE_META_MODEL-METHOD--make-atom-claims-easy-to-understand **and** CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning; reference governing definitions rather than copying another authoritative procedure into the prompt.
- keep internal Tool calls as execution detail under CA-R-1528-CORE_META_MODEL-RULE--record-tool-calls-within-step-runs. **when** an operation needs independently governed routing, checks, **or** approval boundaries, express it as an explicit Step during Workflow authoring rather than inventing Workflow nodes from runtime calls.

## Details
