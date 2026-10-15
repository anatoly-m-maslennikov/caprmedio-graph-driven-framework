# Candidate #5 migration verification baseline

This is an independent read-only check, before promotion. The original-Atom inventory belongs to the packet worker; no additional source inventory or source mutation was performed.

## Prepared packet

- Original checkpoint: `9ef71f469b6d8b9d8dbc9a96661a9e11d7eb8152`
- Packet: `execution/prepared-targets.json`
- Packet SHA-256: `772835c86dc8683c7de4150bc902abfdf4a462f30c7f003e7d7d4c45ae3c74c5`
- Targets: **750**, with unique Atom IDs and paths.
- One `git cat-file --batch` read checked all 750 checkpoint blobs.
- **750/750** checkpoint blob SHA-256 values match packet target digests.
- **750/750** current target files still equal their checkpoint bytes at this observation.
- No source mismatch found.

## Missing-R placeholders

- **54/54** manifest-listed draft files exist.
- **54/54** have no Atom ID, retain Draft Status, and have empty Scope, Claim and Details.
- Each draft's governed Subject equals the manifest's intended governed Subject.
- All 54 governed Subjects are unique.
- Missing-draft manifest SHA-256: `db65c02e09a3d0214b037045d2e3b40812bd2bc50b423c8d023fe81adef33dba`
- Ordered draft-record digest: `9d94d237b3836e5cc9bc94d1f6812fe550f97bd0336fa3e82c8e1f1149d69106`

These hashes match the earlier independent baseline. Staging versioned edit proposals has not changed the missing-definition drafts.

## Inheritance check

The draft set has no duplicate definitions for inherited properties on every descendant:

- Atom Status domain is one placeholder on Atom, not one per Content Role.
- Contains capability and its Boolean allowed values share one Atom-level placeholder.
- Execution ID is declared once on Execution, not repeated for each Run kind.
- Carrier shared properties are declared once on Carrier; File and Directory drafts contain only their own declarations.
- Actor Name and Scope Unit ID each have one general declaration.
- No inherited Status or Local Tier values were turned into separate descendant drafts.

Different direct fields with the same short name, such as File Carrier.Path and Directory Carrier.Path, remain separate because this candidate declares no shared Carrier.Path property to inherit.

This verifies placement and emptiness only. It does not invent the missing R content or resolve the already recorded source-content conflicts.

## Next check

Wait for explicit promotion completion, then use the prepared packet and this checkpoint for exact Subjects-only readback under `verification-plan.md`. Do not treat staging completion as source migration completion.

