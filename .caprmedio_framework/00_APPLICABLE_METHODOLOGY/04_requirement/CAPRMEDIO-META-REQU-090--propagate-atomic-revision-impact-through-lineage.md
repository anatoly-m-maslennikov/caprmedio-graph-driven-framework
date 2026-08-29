---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - lifecycle-traceability
tier: core
version: 9
updated_at: 2026-08-29 01:16:37 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-E-002-PRINCIPLE-EVALUATION--bound-every-reliance
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-META-REQU-090--propagate-atomic-revision-impact-through-lineage.md
---
# Propagate atomic revision impact through lineage

**when** an Atom receives a new committed revision, is replaced by a successor, **or** moves to the archive, CAPRMEDIO **must** assess **every** reachable descendant lineage branch recursively **until** **every** branch has an explicit impact disposition.
