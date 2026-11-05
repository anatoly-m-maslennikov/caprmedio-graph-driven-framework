---
atom_id: CA-A-1275
ref_id: CA-A-1275
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Model
tier: 3
status: Done
version: 3
updated_at: 2026-11-02 15:49:28 +0400
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Place Package API Self Documentation in Engineering

## Decision

Self Documentation belongs to the Engineering branch and describes a Package API so its callers can use it. The aspect is placed under Engineering / Architecture / Communication / API. CLI help, API schemas and RPC discovery are possible forms, not mandatory mechanisms. The older machine-readable Tool Self Description is one case of this broader aspect.

Whether a particular Package must expose an API and which Self Documentation it must supply belongs to that Package's applicable specification. This decision does not add required API or Self Documentation properties to every Package, mandate generation from code, or choose an implementation mechanism.

## State

Model/Definition preparation only. Current methodology, Engine code and runtime are unchanged.
