---
subjects:
  governs: artifact-validation
  depends_on:
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - Atom/Type
  - Atom/Status
  - Subject/Engineering/Carrier
version: 13
updated_at: 2026-10-23 03:18:40 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1308
  - CA-R-1137
atom_id: CA-E-129@13
status: Archived
---
# Reject unknown lifecycle directory

## Test case

**Fixture:** add a lifecycle directory whose Status is **not** admitted by the complete qualified Content Role **and** Type path of its owning Atoms. include a directory admitted by that exact path as a control; do **not** substitute a universal Content Role-only Status domain.

**Expected result:** fail the unregistered lifecycle directory with the stable unknown-lifecycle-directory diagnostic **and** a non-zero exit. do **not** reject the admitted control on this domain check; retain its other applicable placement rules.
