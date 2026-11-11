# REPLACEMENT_FOR model update

Latest decision: REPLACEMENT_FOR uses base Atom IDs without Versions, like every other Header.Relations child.

The replacement Atom stores one or more predecessor Atom IDs. Draft links record intent. Links remain after promotion and predecessor archival. Reverse navigation reads the same stored fact.

```yaml
relations:
  REPLACEMENT_FOR:
    - CA-R-101
    - CA-R-102
```

## Verification

[Latest source check](base-id-source-check.json): eight Current model sources checked; seven corrected in place. Source metadata and Summaries remain unchanged by this correction. Exact preimage and readback checks pass. The Atom outgoing permission remains admitted.

[Correction receipt](base-id-correction-receipt.json) and [model review cases](base-id-cases.json) record the base-ID result. The initial version-qualified plan, receipt, checks and examples remain historical evidence and are superseded by this correction.

## Boundary

Engine, Workbench, Workflows, installed copies and projections were not changed by this update. Native REPLACEMENT_FOR validation and navigation remain unverified. No native Run or Journal record was fabricated.
