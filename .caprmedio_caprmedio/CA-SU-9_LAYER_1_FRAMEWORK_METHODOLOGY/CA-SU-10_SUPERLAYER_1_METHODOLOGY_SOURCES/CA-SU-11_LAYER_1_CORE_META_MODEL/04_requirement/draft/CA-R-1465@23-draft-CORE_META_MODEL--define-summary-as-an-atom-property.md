---
atom_id: CA-R-1465@23-draft
ref_id: CA-R-1465@23-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Definition
topics:
  main_subject: Model::CAPRMEDIO::Continuant/Governing Objects/Atom.content.summary
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
  - Subject/CAPRMEDIO/Carrier/File.Main Content
tier: 1
status: Draft
version: 23
updated_at: 2026-10-29 00:04:17 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---
# Summary

Define Summary as an Atom Property

## Claim scope

The Summary property of an Atom.

## Claim

A Summary means the short, non-authoritative navigation property derived from the finalized primary contribution of one Atom, read within its applicability. Its Markdown carrier uses the literal heading # Summary, followed by the Summary value; the Summary value itself is not the heading.

## Details

For every RMED Atom, including a Model Definition, the source is its sole content.claim read within any applicable Claim scope. Summary is authored last and displayed first. For other Content Roles the existing primary-contribution sources remain: Analysis Question, Concern Concern, Plan Objective and Operations Operation. Analysis TLDR is separate. Changing a Summary continues to follow the existing new-Atom identity rule.
