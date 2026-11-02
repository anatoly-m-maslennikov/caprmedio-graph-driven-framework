---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: feature-boundary
  depends_on: []
version: 11
updated_at: 2026-10-24 02:14:24 +0400
relations:
  evaluation_for:
  - CA-M-197
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-315@11
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: APPS
type: Eval Case
tier: 3
---
# Verify register the codex_plugin unit

## Claim checked

CA-M-197 registers one CODEX_PLUGIN child under AGENT_HOST_PLUGINS **without** duplicating provider-neutral CAPRMEDIO Skill, Tool, **or** Methodology behavior.

## Applicable when

Apply whenever CODEX_PLUGIN structure, package boundary, **or** host wiring changes.

## Test case

Examine the current active AGENT_HOST_PLUGINS **and** CODEX_PLUGIN authority, using **any** available derived representation **only** as supporting evidence. Determine CODEX_PLUGIN's immediate typed ownership, identity, path, host-specific contents, **and** **every** reference **to** provider-neutral CAPRMEDIO behavior.

## Acceptance criteria

Exactly one immediate typed ownership edge connects AGENT_HOST_PLUGINS **to** CODEX_PLUGIN; its address **and** path are valid; its owned content is Codex-specific package **or** host wiring; **and** **every** provider-neutral CAPRMEDIO Skill, Tool, **or** Methodology behavior appears **only** as a reference **to** its existing owner.

## Failure disposition

Reject the registration **and** preserve the examined authority, **any** supporting derived representation, path evidence, **and** **every** duplicated **or** misowned behavior claim.
