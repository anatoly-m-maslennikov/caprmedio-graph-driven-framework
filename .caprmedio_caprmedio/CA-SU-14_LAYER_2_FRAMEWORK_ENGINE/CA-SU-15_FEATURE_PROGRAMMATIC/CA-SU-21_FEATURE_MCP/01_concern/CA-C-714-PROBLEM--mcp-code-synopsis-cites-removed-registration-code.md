---
identity:
  id: CA-C-714
  ref_id: CA-C-714
context:
  container:
    scope_unit: CA-SU-21
  role: Concern
  form: Problem
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Active
  version: 1
  updated_at: 2026-11-09 23:01:48 +0400
destination:
  file:
    name: CA-C-714-PROBLEM--mcp-code-synopsis-cites-removed-registration-code.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/01_concern
author: Anatoly Maslennikov
relations:
  concern_about:
  - CA-I-9
---

## Summary

MCP Code Synopsis cites removed registration code

## Concern

Current I9 cites selected_route_registration.py, which was removed during a concurrent MCP refactor. direct_gateway.py and hot_reload.py also changed during the bounded review. The fingerprint gate stopped I9 adoption before any Current replacement or archive was written.

## Details

The reviewer located replacement registration evidence in shared_project_catalog.py and shared_gateway.py. The owned I9 Draft now uses that location, but it remains held because the MCP tree changed again during the check. Current I9 remains at Version 1. Capture a consistent MCP source snapshot and verify the revised Claim and code links before promotion. This records stale source evidence; no runtime failure, missing integration or required code rollback is inferred.
