---
subject_scopes:
  - provenance
version: 4
updated_at: 2026-08-20 19:03:55
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
# Use revision-bound parent and child commit messages

Every governed Git commit changes exactly one repository file through exactly one action and uses exactly one line as its complete commit message:

```text
<parents> | <ACTION> | <affected-file>
```

## Parents

Parents are the closest upstream Atom frontier of the affected file. The frontier is derived programmatically from typed graph relations: follow each registered upstream direction, stop at the first Atom on each path, exclude more distant ancestors on that path, remove duplicates, and sort the resulting current committed Revisions by filename. Each parent uses its carrier filename and version:

```text
<filename>@<version>
```

Multiple parents are separated by a comma followed by one space. `0` represents an empty upstream frontier and is reserved from use as a filename. A parent may belong to a different Structural scope from the affected file. Association-only relations do not contribute to the upstream frontier.

`ADD` and `UPDATE` resolve the frontier from the resulting staged graph, `MOVE` resolves it from the unchanged Artifact graph, and `REMOVE` resolves it from the last committed graph. Parent versions must be current immediately before the action. `updated_at` is omitted because the Git commit already records the action time.

## Actions

The action is exactly one uppercase token: `ADD`, `MOVE`, `UPDATE`, or `REMOVE`.

An add creates one file and names its resulting Revision:

```text
parent.md@2 | ADD | new-file.md@1
```

A move changes only the carrier filename or address and preserves the version:

```text
parent.md@2 | MOVE | old-file.md@3 -> new-file.md@3
```

An update preserves the carrier filename and names its resulting Revision:

```text
parent.md@2 | UPDATE | file.md@4
```

A remove names the Revision removed from the active carrier address:

```text
parent.md@2 | REMOVE | file.md@4
```

When the removal completes an explicit replacement, the message appends the uppercase literal `REPLACED BY` and the current committed replacement Revisions:

```text
parent.md@2 | REMOVE | old-file.md@4 | REPLACED BY | replacement-a.md@1, replacement-b.md@1
```

The replacement set is derived programmatically by reverse-querying committed `replacement_of` relations that target the removed Artifact. Every replacement file must already exist in an earlier commit, and multiple replacements are sorted by filename. Adding each replacement and removing the replaced file remain separate one-file actions.

An affected governed file uses `<filename>@<version>`. A governed native file without embedded Revision properties uses the version from its external revision binding. Changing file content while moving it requires two ordered commits: one `MOVE` with unchanged version and one `UPDATE` with an advanced version. No governed commit may combine actions or change more than one repository file.

The message contains no parentheses, labels, summary, description, body, or trailers. Once another commit references a parent Revision, the referenced Git history must remain reachable and unchanged.

## Rationale

One explicit file action per commit makes hook logic deterministic, preserves the authority consumed by the action, and prevents unrelated changes from sharing one recovery boundary.
