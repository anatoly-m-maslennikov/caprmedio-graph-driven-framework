---
subject_scopes:
  - provenance
version: 5
updated_at: 2026-08-20 19:10:37
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

The left field preserves every direct typed upstream relation from the affected file to its closest upstream Atom Revisions. Each entry uses the canonical relation kind, target carrier filename, and target version:

```text
<relation-kind>=<filename>@<version>
```

Targets of the same relation kind are separated by a comma followed by one space. Relation groups are separated by a semicolon followed by one space and sorted first by relation kind and then by filename. `0` represents no direct upstream typed relation. Transitive ancestors, inverse relations, and association-only relations are excluded.

`ADD` and `UPDATE` resolve relations from the resulting staged graph, `MOVE` resolves them from the unchanged Artifact graph, and `REMOVE` resolves them from the last committed graph. Target versions must be current immediately before the action. `updated_at` is omitted because the Git commit already records the action time.

## Actions

The action is exactly one uppercase token: `ADD`, `MOVE`, `UPDATE`, or `REMOVE`.

An add creates one file and names its resulting Revision:

```text
child_of=parent.md@2 | ADD | new-file.md@1
```

A move changes only the carrier filename or address and preserves the version:

```text
child_of=parent.md@2 | MOVE | old-file.md@3 -> new-file.md@3
```

An update preserves the carrier filename and names its resulting Revision:

```text
child_of=parent.md@2; derived_from=analysis.md@1 | UPDATE | file.md@4
```

A remove names the Revision removed from the active carrier address:

```text
child_of=parent.md@2 | REMOVE | file.md@4
```

When the removal completes an explicit replacement, the message appends the uppercase literal `REPLACED BY` and the current committed replacement Revisions:

```text
child_of=parent.md@2 | REMOVE | old-file.md@4 | REPLACED BY | replacement-a.md@1, replacement-b.md@1
```

The replacement set is derived programmatically by reverse-querying committed `replacement_of` relations that target the removed Artifact. Every replacement file must already exist in an earlier commit, and multiple replacements are sorted by filename. Adding each replacement and removing the replaced file remain separate one-file actions.

An affected governed file uses `<filename>@<version>`. A governed native file without embedded Revision properties uses the version from its external revision binding. Changing file content while moving it requires two ordered commits: one `MOVE` with unchanged version and one `UPDATE` with an advanced version. No governed commit may combine actions or change more than one repository file.

The message contains no parentheses, free-form labels, summary, description, body, or trailers. Canonical relation kinds, action tokens, and `REPLACED BY` are structural syntax rather than prose labels. Once another commit references an upstream Revision, the referenced Git history must remain reachable and unchanged.

## Rationale

One explicit file action per commit makes hook logic deterministic, preserves the exact typed upstream graph consumed by the action, and prevents unrelated changes from sharing one recovery boundary.
