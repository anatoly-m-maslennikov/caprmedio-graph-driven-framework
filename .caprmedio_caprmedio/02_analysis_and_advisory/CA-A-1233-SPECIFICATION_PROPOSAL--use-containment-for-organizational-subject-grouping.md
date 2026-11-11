---
atom_id: CA-A-1233
ref_id: CA-A-1233
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Subject
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 15:49:28 +0400
carrier_destination:
  file:
    name: CA-A-1233-CAPRMEDIO-SPECIFICATION_PROPOSAL--use-containment-for-organizational-subject-grouping.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Use containment for organizational Subject grouping

## Operator decision

“Project Model > Actor, etc, not "/"”

“Project Model CONTAINS Actor, etc”

## Meaning

Use the existing CONTAINS relation and its `>` notation for organizational Subject membership. Such containment does not imply broader-to-narrower classification or property inheritance. Keep `/` for real broader-to-narrower classification and preserve legitimate inheritance there. The existing direct IS_CONTAINED_BY / derived CONTAINS convention remains unchanged.

Project Model remains a vocabulary grouping. Its containment of the Actor Subject does not duplicate an Actor, create a Scope Unit ownership claim, or merge an occurrence with its record.

## Review disposition

This selects the semantic correction for SG3-I02 / SG3-F02. The affected path inventory and source migration still need review. Other FPF findings and the distinction between Aspect subtopics, classifications and part structures remain separate.

## Preparation

Successor Drafts are prepared for R2209, R1931, R2150 and R2222. Current sources and generated Projections are unchanged; no renderer, Tool, MCP or runtime code is changed. This file records the decision; Draft preparation is not promotion or migration.
