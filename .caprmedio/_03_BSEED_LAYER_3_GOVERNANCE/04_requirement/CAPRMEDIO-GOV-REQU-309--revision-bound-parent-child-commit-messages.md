---
subject_scopes:
  - provenance
version: 3
updated_at: 2026-08-20 19:01:20
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
<parents> | <action> | <affected-file>
```

## Parents

Parents are the current committed Atom Revisions whose meaning the action consumes. Each parent uses its carrier filename and version:

```text
<filename>@<version>
```

Multiple parents are separated by a comma followed by one space. `0` represents no governed parent and is reserved from use as a filename. A parent may belong to a different Structural scope from the affected file.

The parent version must be current immediately before the action. `updated_at` is omitted because the Git commit already records the action time.

## Actions

The action is exactly one lowercase token: `add`, `move`, `update`, or `remove`.

An add creates one file and names its resulting Revision:

```text
parent.md@2 | add | new-file.md@1
```

A move changes only the carrier filename or address and preserves the version:

```text
parent.md@2 | move | old-file.md@3 -> new-file.md@3
```

An update preserves the carrier filename and names its resulting Revision:

```text
parent.md@2 | update | file.md@4
```

A remove names the Revision removed from the active carrier address:

```text
parent.md@2 | remove | file.md@4
```

An affected governed file uses `<filename>@<version>`. A governed native file without embedded Revision properties uses the version from its external revision binding. Changing file content while moving it requires two ordered commits: one move with unchanged version and one update with an advanced version. No governed commit may combine actions or change more than one repository file.

The message contains no parentheses, labels, summary, description, body, or trailers. Once another commit references a parent Revision, the referenced Git history must remain reachable and unchanged.

## Rationale

One explicit file action per commit makes hook logic deterministic, preserves the authority consumed by the action, and prevents unrelated changes from sharing one recovery boundary.
