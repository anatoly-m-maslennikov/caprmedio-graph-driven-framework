---
subject_scopes:
  - provenance
version: 2
updated_at: 2026-08-21 01:09:53
relations:
  delivery_for:
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--append-governed-file-change-journal-records
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-520--own-deterministic-scripts-in-tools
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-602--use-a-common-tool-cli-interface
---
# Deliver the change-record appender script

Realize `APPEND_CHANGE_RECORDS` through the canonical source script `.caprmedio/200_LAYER_2_FRAMEWORK_ENGINE/TOOLS/APPEND_CHANGE_RECORDS/append_change_records.py` and its content-identical installed runtime carrier. It must expose the common Doer CLI contract with dry-run and apply modes and use the runtime-local shared non-executable Journal append implementation. That shared implementation is a library, not a fifth Tool or executable entry point.
