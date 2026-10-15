# Installed source copies and original identity

Derived verification record, 2026-10-12. This is not migration approval.

The original-identity guard counted raw installed Methodology source copies as
authored originals. The existing release layout and Project Structure already
distinguish those collections. No cleanup or new methodology policy is needed.

## Bounded correction

The shared Subject planner uses that existing layout to exclude only the
installed source-copy collection from its original-identity match count.
It pins and rechecks Settings and Project Structure. It still parses and
fingerprints the copies, rejects selecting them as originals, and rejects
genuine or malformed duplicate originals. An absent or invalid release layout
grants no exemption. No public payload, installed files or Core Atoms changed.

Current CA-R-866 v18, CA-M-371 v6, CA-E-304 v17, CA-D-425 v13 and
CA-O-030 v11 already require the original/delivered distinction.

## Checks

- Producer: all 87 ATOM_UPDATE tests passed.
- Independent verification: 13 cases passed, covering known installed copies,
  duplicate/malformed originals, ineligible installed targets, generic Projects,
  source/membership/Structure drift, and symlink refusal.
- The real checkout's approved no-op preview for CA-R-728 now succeeds; its
  original and installed bytes, all 18 validator authority sources, Settings
  and Project Structure remain unchanged.
- The existing staging route repeats the preview and compares its output; it
  does not gain a new long-lived approval seal or publication permission.
- No staged migration exports, history/Journal changes or live publication.

## Verified implementation pins

- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_subject_patch.py`:
  `6f6b80a7c365707e1d736bda2d18e0c3a4709e594a97c38d99c4d76e1a1f86c0`.
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_UPDATE/tests/test_nonarchived_subject_preview.py`:
  `aa90044556d63a986dd88541d0facdeb54045efe1b11f6da16762c68308e69a0`.
- Real no-op preview:
  `00dd6b10bbfccacf9934e81501a2785669988fb2c87b835f57f68261eb0cd6fd`.

The full Subject ledger and its independent acceptance remain prerequisites for
migration staging. This tool fix does not complete that ledger.
