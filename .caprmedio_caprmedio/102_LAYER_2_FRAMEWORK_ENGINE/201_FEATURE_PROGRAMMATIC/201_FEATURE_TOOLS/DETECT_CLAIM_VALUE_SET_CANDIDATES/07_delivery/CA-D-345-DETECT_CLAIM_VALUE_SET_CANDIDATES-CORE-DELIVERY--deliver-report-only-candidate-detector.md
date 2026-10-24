---
cce_version: cce_1
cce_form: delivery
subjects:
  governs: Subject/Engineering/Carrier
  depends_on:
  - Subject/Engineering/Tool//DETECT_CLAIM_VALUE_SET_CANDIDATES
version: 10
updated_at: 2026-10-24 02:14:24 +0400
relations:
  delivery_for:
  - CA-M-238
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-D-345
status: Active
content_role: Delivery
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eng Decision
tier: 2
---
# Deliver Report-Only Candidate Detector

the `DETECT_CLAIM_VALUE_SET_CANDIDATES` Tool **must** deliver its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/DETECT_CLAIM_VALUE_SET_CANDIDATES/detect_claim_value_set_candidates.py` with focused tests **in** its sibling `tests/` directory.
