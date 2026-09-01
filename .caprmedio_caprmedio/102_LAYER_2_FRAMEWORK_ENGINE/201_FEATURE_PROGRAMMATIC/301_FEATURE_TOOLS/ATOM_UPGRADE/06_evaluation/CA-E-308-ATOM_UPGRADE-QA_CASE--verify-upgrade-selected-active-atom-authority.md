---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-operations
    occurrent:
      - evaluation
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  evaluation_for:
    - CA-M-190
---
# Verify upgrade selected active atom authority

## Claim checked

CA-M-190 moves one active Atom to a strictly higher enabled authority Tier while preserving one stable identity.

## Applicable when

Apply to any ATOM_UPGRADE realization before it can change an active Atom's Tier or authority location.

## Test case

Select one active standard-tier Atom. Preview an upgrade first to the same Tier and then to an enabled higher Tier in an explicit ancestor Scope Unit; apply both requests in sequence and inspect identity, revision, placement, and active duplicates.

## Acceptance criteria

The same-Tier request changes nothing; the valid request creates one canonical higher-Tier carrier in the approved ancestor, preserves Atom ID, advances revision once, removes the former carrier, and leaves no second active owner of the ID.

## Failure disposition

Reject the realization and preserve Tier and ancestry evidence, dry-run map, identity scan, revisions, and any duplicate or stale authority carrier.
