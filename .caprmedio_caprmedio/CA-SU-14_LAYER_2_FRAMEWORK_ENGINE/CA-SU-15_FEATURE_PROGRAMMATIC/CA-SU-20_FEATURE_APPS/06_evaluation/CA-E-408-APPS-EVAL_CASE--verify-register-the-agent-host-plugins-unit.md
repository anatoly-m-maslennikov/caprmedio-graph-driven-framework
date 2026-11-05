---
atom_id: CA-E-408
ref_id: CA-E-408
container:
  scope_unit: CA-SU-20
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
tier: 3
relations:
  evaluation_for:
  - CA-M-242
status: Active
version: 13
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: APPS
---
# Verify register the AGENT_HOST_PLUGINS unit

## Claim checked

CA-M-242 registers AGENT_HOST_PLUGINS as one immediate unordered APPS unit with the exact required boundary **and** no provider-neutral CAPRMEDIO authority.

## Applicable when

Apply whenever AGENT_HOST_PLUGINS's APPS ownership, structural identity, responsibility boundary, **or** realization path changes.

## Test case

Examine the current active APPS **and** AGENT_HOST_PLUGINS authority, using **any** available derived representation **only** as supporting evidence. Determine whether the AGENT_HOST_PLUGINS declaration has one immediate typed owner, the declared prefix, level, address, path, host-specific responsibility boundary, **and** provider-neutral non-duplication condition.

## Acceptance criteria

AGENT_HOST_PLUGINS is the sole matching immediate unordered child of APPS at Structural level `4`, addressed by `002_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS` **and** realized at its declared source path; it owns installable agent-host-specific packages **and** host wiring, while **every** provider-neutral CAPRMEDIO Skill, Tool, **and** Methodology behavior remains a reference **to** its existing owner.

## Failure disposition

Reject the AGENT_HOST_PLUGINS registration **and** preserve the examined authority, **any** supporting derived representation, the observed owner **and** identity facts, **and** **every** missing, duplicate, **or** copied provider-neutral claim.
