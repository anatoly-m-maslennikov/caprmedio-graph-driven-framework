---
subject_scopes:
  - provenance
version: 8
updated_at: 2026-08-20 19:14:38
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
    - CAPRMEDIO-META-REQU-110--bind-governed-transactions-to-stable-artifact-revisions
  replacement_of:
    - CAPRMEDIO-GOV-REQU-465--atomic-id-only-commit-messages
  relates_to:
    - CAPRMEDIO-META-REQU-125--three-artifact-forms-with-generated-projections
    - CAPRMEDIO-META-REQU-154--semantic-irreducibility
---
# Use typed-upstream action commit messages

Every governed Git commit changes exactly one repository file through exactly one action and uses exactly one line as its complete commit message:

```text
<upstream-relations> | <ACTION> | <affected-file>
```

## Upstream relations

The left field preserves every direct typed upstream relation from the affected file to its closest upstream Atom Revisions. Relations may be authored or programmatically derived from the current graph. Each entry uses the canonical relation kind, target carrier filename, and target version:

```text
<relation-kind>=<filename>@<version>
```

Targets of the same relation kind are separated by a comma followed by one space. Relation groups are separated by a semicolon followed by one space and sorted first by relation kind and then by filename. `0` represents no direct upstream typed relation. Transitive ancestors and association-only relations are excluded. A derived inverse relation is included when its registered direction is upstream for the affected file.

`ADD` and `UPDATE` resolve relations from the resulting staged graph, while `REMOVE` resolves them from the last committed graph. Target versions must be current immediately before the action. `updated_at` is omitted because the Git commit already records the action time.

## Actions

The action is exactly one uppercase token: `ADD`, `UPDATE`, or `REMOVE`.

An add creates one file and names its resulting Revision:

```text
child_of=parent.md@2 | ADD | new-file.md@1
```

An update names the resulting Revision when the carrier filename is unchanged:

```text
child_of=parent.md@2; derived_from=analysis.md@1 | UPDATE | file.md@4
```

A rename is an update of the same file identity and records both filenames. A rename-only update preserves the version:

```text
child_of=parent.md@2 | UPDATE | old-file.md@3 -> new-file.md@3
```

A remove names the Revision removed from the active carrier address:

```text
child_of=parent.md@2 | REMOVE | file.md@4
```

Replacement uses the same typed-relation syntax as every other governed relation. Adding a replacement file records its authored `replacement_of` edge:

```text
child_of=parent.md@2; replacement_of=old-file.md@4 | ADD | replacement-file.md@1
```

Removing the replaced file later uses the derived inverse `replaced_by` edge:

```text
replaced_by=replacement-file.md@1 | REMOVE | old-file.md@4
```

The committed replacement file and its authored `replacement_of` relation must already exist before removal so the graph can derive `replaced_by`. Adding each replacement and removing the replaced file remain separate one-file actions.

An affected governed file uses `<filename>@<version>`. A governed native file without embedded Revision properties uses the version from its external revision binding. An update may change content, filename, address, or any combination while preserving one file identity; content changes advance the version, while a rename-only update preserves it. No governed commit may combine actions or change more than one repository file identity.

The message contains no parentheses, free-form labels, summary, description, body, or trailers. Canonical relation kinds and action tokens are structural syntax rather than prose labels. Once another commit references an upstream Revision, the referenced Git history must remain reachable and unchanged.

## Rationale

One explicit file action per commit makes hook logic deterministic, preserves the exact typed upstream graph consumed by the action, and prevents unrelated changes from sharing one recovery boundary.
