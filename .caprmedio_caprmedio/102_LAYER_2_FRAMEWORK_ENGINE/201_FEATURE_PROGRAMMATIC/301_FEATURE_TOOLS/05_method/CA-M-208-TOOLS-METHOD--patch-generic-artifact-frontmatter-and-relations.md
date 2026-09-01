---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - artifact-operations
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-1130
    - CA-R-1131
  derived_from:
    - CA-A-058
---
# Patch generic Artifact frontmatter and relations

## Applicable when

Use this Method when a governed Tool needs the shared mechanics for patching generic Artifact metadata or authored direct relations.

## Procedure

1. Resolve the exact Artifact and seal its path, revision, digest, schema, and current frontmatter while preserving the body bytes.
2. Apply only declared add, replace, or remove operations to registered fields and authored direct relation targets.
3. Canonicalize Atom references and relative Scope Unit references, then validate relation kind, endpoint classes, direction, lifecycle, cardinality, role, and identity.
4. Reject unknown fields, invalid relation types, failed preconditions, and any patch that would rewrite body content.
5. Advance the revision once, expose the exact dry-run, and on authorized apply replace the carrier atomically and verify the unchanged body.

## Outcome

The Artifact receives one schema-valid metadata and relation revision while its body and identity remain unchanged.

## Failure or stop

Stop or roll back on stale preconditions, unknown fields, invalid endpoints, relation-policy violations, or any body-byte change.
