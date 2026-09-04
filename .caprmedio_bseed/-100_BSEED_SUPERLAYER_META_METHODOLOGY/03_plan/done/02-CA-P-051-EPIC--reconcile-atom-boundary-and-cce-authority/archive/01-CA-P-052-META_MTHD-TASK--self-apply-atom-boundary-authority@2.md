---
atom_id: CA-P-052
cce_version: cce_1
cce_form: obligation
subjects:
  - development-flow
  - atom-boundary
version: 2
updated_at: 2026-08-23 02:41:00
---
# Self-apply Atom-boundary authority

THE Operator MUST make every Atom in Task Scope comply with the active Atom-boundary authority.

## Scope

`(ALL Atoms WHERE (subjects IN (atom-boundary) AND Content Role != PLAN))`

## Definition of Done

THE Task is NOT DONE IF (ANY Atom in Task Scope violates active authority for one Atom, one Claim, one Claim Scope, Current-scope Atoms, or Relational Atoms OR ANY semantic resolution below 98 percent lacks an Operator disposition OR the Task Scope Resolution is not recorded).

## Details

Apply CA-M-119 to every changed Atom and preserve each accepted Claim while resolving conflicts among the Atom-boundary authorities.

## Task Scope Resolution

THE Task Scope Resolution uses Project Revision `5916b59f90d89feaa9800a3792f6b7ea04d8d2ec` and contains EXACTLY 87 BSEED Atoms.

The exact Atom set is:

- `CA-R-1001`, `CA-R-1004`, `CA-R-1012`, `CA-R-1013`, `CA-R-1014`, `CA-R-117`
- `CA-R-118`, `CA-R-121`, `CA-R-151`, `CA-R-154`, `CA-R-655`, `CA-R-718`
- `CA-R-771`, `CA-R-772`, `CA-R-918`, `CA-R-919`, `CA-R-920`, `CA-R-921`
- `CA-R-922`, `CA-R-923`, `CA-R-924`, `CA-R-925`, `CA-R-926`, `CA-R-927`
- `CA-R-928`, `CA-R-929`, `CA-R-932`, `CA-R-933`, `CA-R-934`, `CA-R-935`
- `CA-R-936`, `CA-R-939`, `CA-R-960`, `CAPRMEDIO-META-REQU-714`, `CAPRMEDIO-META-REQU-788`, `CA-R-1007`
- `CA-R-126`, `CA-R-643`, `CA-R-796`, `CA-R-914`, `CA-R-915`, `CA-R-916`
- `CA-R-943`, `CA-R-944`, `CA-R-945`, `CA-R-946`, `CA-R-976`, `CA-M-125`
- `CA-M-126`, `CAPRMEDIO-A-034-RATIONALE-GOV`, `CA-R-1011`, `CA-R-1015`, `CA-R-295`, `CA-R-326`
- `CA-R-380`, `CA-R-747`, `CA-R-806-REQUIREMENT-BSEED_GOVERNANCE`, `CA-R-807-REQUIREMENT-BSEED_GOVERNANCE`, `CA-R-808-REQUIREMENT-BSEED_GOVERNANCE`, `CA-R-838`
- `CA-R-877`, `CA-R-878`, `CA-R-879-REQUIREMENT-BSEED_GOVERNANCE`, `CA-R-885`, `CA-R-947`, `CA-R-948`
- `CA-R-949`, `CA-R-950`, `CA-R-951`, `CA-R-954`, `CA-R-955`, `CAPRMEDIO-GOV-REQU-310`
- `CAPRMEDIO-GOV-REQU-312`, `CAPRMEDIO-GOV-REQU-325`, `CAPRMEDIO-GOV-REQU-377`, `CAPRMEDIO-GOV-REQU-381`, `CAPRMEDIO-GOV-REQU-611`, `CAPRMEDIO-GOV-REQU-712`
- `CAPRMEDIO-GOV-REQU-714`, `CAPRMEDIO-GOV-REQU-717`, `CAPRMEDIO-GOV-REQU-718`, `CAPRMEDIO-GOV-REQU-767`, `CAPRMEDIO-GOV-REQU-768`, `CA-M-120`
- `CA-E-239`, `CA-E-243`, `CA-E-246`

## Execution Result

THE review classified 82 Atoms as `compatible` and classified `CAPRMEDIO-GOV-REQU-310`, `CAPRMEDIO-GOV-REQU-312`, `CAPRMEDIO-GOV-REQU-325`, `CA-R-879-REQUIREMENT-BSEED_GOVERNANCE`, and `CAPRMEDIO-GOV-REQU-768` as `update_required` because each contained independently replaceable Claim content.

THE five updated Atoms preserve one Claim each, and their extracted Claim content is preserved by 25 new Requirement Atoms and two new Rationale Atoms that each have one Current-scope Claim and one Claim Scope.

NO reviewed semantic resolution was below 98 percent confidence.
