---
subjects:
  governs: "Agentic Action Instruction"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow", "Entity/Continuant/Actor/Type: Operator", "Tool", "Atom/Content Role: Operations/Type: Action/Execution Kind: Agentic", "Tool Call"]
version: 6
updated_at: "2026-10-15 18:48:30 +0000"
relations: {"method_for": ["CA-R-1789", "CA-R-1790", "CA-R-1791", "CA-R-1792", "CA-R-1793"]}
atom_id: "CA-M-304"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/05_method/CA-M-304-CORE_META_MODEL--write-self-contained-agentic-action-instructions.md
  source_atom_id: CA-M-304
  source_atom_revision: 6
  source_sha256: 19bc1f7cc931b584e1bf7e6d5410988d002f73434041bf216512bed9e9549d1e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
- keep internal Tool calls as execution detail under CA-R-1528-CORE_META_MODEL-GENERAL-REQUIREMENT--record-tool-calls-within-step-runs. **when** an operation needs independently governed routing, checks, **or** approval boundaries, express it as an explicit Step during Workflow authoring rather than inventing Workflow nodes from runtime calls.

## Details
