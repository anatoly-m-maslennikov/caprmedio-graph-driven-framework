---
atom_id: CA-P-1723@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Archived
version: 5
updated_at: 2026-10-24 11:29:41 +0400
subjects:
  governs: Release suite delivery/Test the source-bound Release suite driver
  depends_on:
  - Subject/Engineering/Implementation
  - Subject/Engineering/Implementation Evaluation
  - Methodology
  - Manifest
  - Subject/Engineering/Release Testing/Executor Admission
relations:
  is_decomposition_of:
  - CA-P-1717
tier: 3
---
# Summary

Test the source-bound Release suite driver

## Objective

Build deterministic E2E golden fixtures for the accepted suite driver before accepting its implementation.

## Details

Own only RELEASE_VERSION/tests/test_run_release_suite.py and tests/full_suite_golden/. Exercise the exact sealed CLI environment: complete testcase discovery, source digests, immutable envelope, six groups and compiled evidence, and failure/skip/omission/duplicate/unsafe input. Keep the fixture outputs retained. Expected bounded work: <=15 minutes; decompose if needed.

## Definition of Done

The unchanged golden corpus passes against the implemented driver; positive cases are executed and negative cases cannot produce a passing gate.

## Results

Twelve golden driver cases pass with the exact host interpreter. Stored intentional test payloads use fixture-prefixed names; the disposable loader restores their intended names. Positive discovery and negative failure, skip, zero-case, duplicate, unsafe-input and schema-2 cases remain covered without production exclusions.
