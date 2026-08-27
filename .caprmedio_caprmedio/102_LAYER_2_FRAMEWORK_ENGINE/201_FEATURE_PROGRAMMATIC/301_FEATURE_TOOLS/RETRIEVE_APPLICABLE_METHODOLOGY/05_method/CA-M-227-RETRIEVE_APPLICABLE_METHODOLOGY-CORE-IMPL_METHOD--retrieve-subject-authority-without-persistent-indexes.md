---
atom_id: CA-M-227
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Applicable Methodology Retrieval Tool/Execution
  depends_on:
    continuant:
      - Applicable Methodology Retrieval Tool
    occurrent:
      - Applicable Methodology Retrieval
version: 1
updated_at: 2026-08-27 21:45:57 +0400
relations: {}
---
# Retrieve Subject Authority Without Persistent Indexes

to retrieve applicable authority, the Tool **must** validate every projected Carrier against its relative `projection.source_carrier_path`, derive `GOVERNS` and `DEPENDS_ON` indexes in memory, seed exact matching governed Subject Paths, close every prerequisite transitively, fail closed on an unresolved prerequisite, emit ordered Source-backed Carrier records, and write no persistent Subject Index Carrier or cache.
