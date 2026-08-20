---
subject_scopes:
  - provenance
version: 11
updated_at: 2026-08-20 20:01:00
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
# Use typed-upstream change-set commit messages

Every governed Git commit changes exactly one repository file identity through one change set and uses exactly one line as its complete commit message:

```text
<upstream-relations> | <CHANGES> | <affected-file>
```

## Upstream relations

The left field preserves every direct typed upstream relation from the affected file to its closest upstream Atom Revisions. Relations may be authored or programmatically derived from the current graph. The relation registry declares the authored direction, derived inverse name, and upstream endpoint for each kind; the generator must not infer direction from a relation's spelling. Each entry uses the canonical relation kind, target carrier filename, and target version:

```text
<relation-kind>=<filename>@<version>
```

Targets of the same relation kind are separated by a comma followed by one space. Relation groups are separated by a semicolon followed by one space and sorted first by relation kind and then by filename. `0` represents no direct upstream typed relation. Transitive ancestors and association-only relations are excluded. A derived inverse relation is included when its registered direction is upstream for the affected file.

`ADD`, `UPDATE`, and `MOVE+UPDATE` resolve relations from the resulting staged graph, `MOVE` resolves them from the unchanged Artifact graph, and `REMOVE` resolves them from the last committed graph. Target versions must be current immediately before the change. `updated_at` is omitted because the Git commit already records the change time.

## Changes

The change set is exactly one of `ADD`, `MOVE`, `UPDATE`, `MOVE+UPDATE`, or `REMOVE`. `ADD` and `REMOVE` are exclusive lifecycle changes. `MOVE` means that the directory or Structural location changes. `UPDATE` means that content, filename, or other governed carrier state changes. `MOVE+UPDATE` means that both changes occur for the same file identity.

An add creates one file and names its resulting Revision:

```text
child_of=parent.md@2 | ADD | new-file.md@1
```

A move changes the carrier's structural location without changing content or filename and preserves the version:

```text
child_of=parent.md@2 | MOVE | old/path/file.md@3 -> new/path/file.md@3
```

An update names the resulting Revision when the carrier filename is unchanged:

```text
child_of=parent.md@2; derived_from=analysis.md@1 | UPDATE | file.md@4
```

A rename is an update of the same file identity and records both filenames. A rename-only update preserves the version:

```text
child_of=parent.md@2 | UPDATE | old-file.md@3 -> new-file.md@3
```

A move and update may occur together for one file identity:

```text
child_of=parent.md@2 | MOVE+UPDATE | old/path/old-file.md@3 -> new/path/new-file.md@4
```

A remove names the Revision removed from the active carrier address:

```text
child_of=parent.md@2 | REMOVE | file.md@4
```

Replacement uses the same typed-relation syntax as every other governed relation. First add the successor as an active Atom without authoring an inverse replacement edge:

```text
child_of=parent.md@2 | ADD | replacement-file.md@1
```

Then add the direct `replaced_by` edge to the predecessor while moving that predecessor into its archive location:

```text
replaced_by=replacement-file.md@1 | MOVE+UPDATE | active/old-file.md@4 -> archive/old-file.md@5
```

The successor must already be active before the predecessor change. The resulting archived predecessor stores direct `replaced_by`; the graph derives `replacement_of` for inverse navigation and never writes it into the successor. Adding each successor and archiving each predecessor remain separate one-file commits.

An affected governed file uses `<filename>@<version>` and includes repository-relative path when the change set changes structural location. A governed native file without embedded Revision properties uses the version from its external revision binding. `UPDATE` may change content, filename, or both while preserving one file identity; content changes advance the version, while a rename-only update preserves it. `MOVE` changes structural location only. `MOVE+UPDATE` changes structural location and also performs an update. No governed commit may change more than one repository file identity.

The message contains no parentheses, free-form labels, summary, description, body, or trailers. Canonical relation kinds and change tokens are structural syntax rather than prose labels. Once another commit references an upstream Revision, the referenced Git history must remain reachable and unchanged.

## Rationale

One explicit file change set per commit makes hook logic deterministic, preserves the exact typed upstream graph consumed by the change, and prevents unrelated changes from sharing one recovery boundary.
