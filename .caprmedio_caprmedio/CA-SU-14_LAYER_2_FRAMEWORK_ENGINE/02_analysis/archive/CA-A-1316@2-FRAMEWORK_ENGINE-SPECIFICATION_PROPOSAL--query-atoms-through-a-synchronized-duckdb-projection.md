---
atom_id: CA-A-1316@2
current_scope_unit: FRAMEWORK_ENGINE
claim_target_scope_unit: FRAMEWORK_ENGINE
status: Archived
version: 2
author: Anatoly Maslennikov
role: Analysis & Advisory
form: Specification Proposal
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  depends_on:
  - CA-R-2719
  - CA-R-2498
  - CA-R-2500
  - CA-R-2721
  - CA-R-2722
  - CA-R-2547
  - CA-D-663
updated_at: 2026-11-03 21:23:06 +0400
carrier_destination:
  file:
    name: CA-A-1316@2-FRAMEWORK_ENGINE-SPECIFICATION_PROPOSAL--query-atoms-through-a-synchronized-duckdb-projection.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis/archive
---

## Summary

Query Atoms through a synchronized DuckDB Projection

## Proposal

Put a query Projection of Atom files into DuckDB. Use standard DuckDB SQL, a small connector with CAPRMEDIO helpers, and a background synchronizer. Provide an MCP query tool and a simple web page.

Atom files remain the source of truth. The database can be rebuilt from them. The reader and synchronizer never edit, move, archive or promote source Atoms.

```text
Atom files → reader → DuckDB Projection → SQL connector → MCP / web page
                 ↑
       background synchronizer
```

Start without custom result views or a renderer. TABLE, DOC and TREE modes remain deferred. Ordinary SQL results are enough for the first version.

CFEL continues to describe the model and Formal Claims. This proposal uses an existing SQL engine for queries instead of adding a SQL-like parser to CFEL.

## DuckDB in Docker

- Include DuckDB in the existing project Docker image.
- Keep one DuckDB owner per Project, in the existing long-lived server process. The query connector and background synchronization task share that owner.
- Serialize query runs and database-update batches through that owner. The scanner may collect source changes while a query runs, but database updates wait until that query finishes.
- Open the database in read-write mode for trusted setup and synchronization, and in native read-only mode for public query execution. Close all handles for the previous mode before opening the next. Never overlap read-only and read-write connections to the same file.
- Keep the owner outside reloadable implementation generations, or close the old owner before starting its replacement. Hot reload must not start two independent writers for the same database.
- Keep query database state separate from scheduler state and outside Atom source folders.
- Do not add a separate database server or watcher service.

Enforce public read-only access with DuckDB's read-only connection mode, not a keyword check. This also rejects writes nested inside a WITH query. Register the required helpers during trusted setup. Disable external access and lock configuration before accepting public SQL, so queries cannot turn file/network access back on. Native read-only mode prevents database changes; disabling external access prevents unrelated file/network access. Both are needed.

Database updates belong to the synchronizer. A long query delays the next database update; source edits remain allowed and are reconciled afterward. The first version does not promise concurrent query/write execution or a fixed synchronization delay.

## Atom reader

Use the Project's governed source inventory. Read canonical Atom carriers, not every Markdown file in the repository. Exclude delivery copies, generated Projections, temporary files and implementation documentation from that inventory.

Retain each valid carrier's source path and source bytes. Read YAML frontmatter as Header Properties and the Markdown body as Content. Preserve all Atom roles. Keep lifecycle groups distinct; Current includes statuses such as Done and Canceled, not only Active. SQL can select the required group explicitly.

Retain identity from the Header and governed source context, not from the filename alone. An indexed row has a source locator as well as its Atom reference and Version. Historical or Draft carriers must not overwrite a Current row with the same base ID. Do not invent an ID for a source that does not have one.

Check the carrier's readable syntax and unambiguous Property mapping. Do not interpret prose or execute CFEL Claims to decide whether an Atom is true, sufficient or well written.

### YAML and nested Header Properties

Keep the complete parsed Header as a nested value, alongside its original frontmatter text. Preserve scalars, lists and mappings. A YAML mapping represents nested Properties; a reference value does not become an embedded copy of the referenced object.

Keep these cases distinct:

- An absent key.
- An explicit YAML null.
- An empty string.
- An empty list or mapping.
- A scalar and a one-item list.
- False and zero.

Reject duplicate mapping keys instead of silently keeping the last value. Use the declared Header/Carrier mapping and admitted aliases; do not guess new aliases from similar spellings.

### Markdown and nested Content Properties

Keep the complete Markdown body unchanged. For every mapped Content Property, retain:

- Its complete path and parent path.
- Its original heading, heading level and position.
- Its direct Markdown value, if present.
- Its complete section Markdown, including the heading and descendants.

Direct text and child Properties are separate. Fetching a complete section includes its descendants; counting its direct values does not count their text.

Use real Markdown heading structure. Skipped heading levels create no empty intermediate Properties. Heading-like text inside a code fence creates no section. Preserve lists, links, tables, fences, fence labels, indentation and line breaks.

Follow applicable declarations when distinguishing a nested Property from a heading inside a Markdown value. In the current RMED model, Claim is a container with Formal Claim and/or Prose Claim. A heading inside Prose Claim stays part of its Markdown value unless a declaration admits it as a child Property.

For example, this source has one Claim container and two child values:

````markdown
## Claim
### Prose Claim
Keep the source wording.
### Formal Claim
```CFEL
Atom.Header.Version{:1}: [int, >=1]{:1}
```
````

The Claim container has no direct value. Retrieving its complete section returns both children. Formal Claim's value retains the CFEL code fence. For any Property that permits both its own text and children, preserve both without concatenating the children into its direct value.

Normalize heading keys using the existing Markdown Carrier rule. Equal normalized keys under one parent are errors; equal names under different parents have different paths. Never merge colliding sections.

## Proposed database mapping

The first schema separates source records, nested Properties and graph links. These are database structures, not new model entities.

| SQL data | Contents |
| --- | --- |
| `atoms` | One record per valid canonical carrier: source path, identity, Version, lifecycle group, convenient Header columns, complete nested Header and complete Markdown body. |
| `atom_content_properties` | One mapped section occurrence: source path, Property path, parent path, heading, position, direct Markdown and complete section Markdown. |
| `relation_edges` | Registered typed links with source and target kinds/references, including their owning source record. |

Header columns are derived from the retained Header, not separately maintained facts. Keep complete source bytes so this mapping does not lose comments or source spelling.

Store Property paths as segments, not only as a string split on dots. Do not force a Property's direct value and its children into one JSON field, or introduce a reserved model Property such as `$value` to work around that problem. The section records preserve those two parts separately.

For example:

```sql
SELECT id, status, content_markdown
FROM atoms
WHERE status_group = 'Current';
```

```sql
SELECT a.id, p.direct_markdown, p.section_markdown
FROM atoms AS a
JOIN atom_content_properties AS p USING (source_path)
WHERE a.status_group = 'Current'
  AND p.property_path = ['content', 'claim', 'formal_claim'];
```

These illustrate the proposed SQL mapping, not an implemented schema. Nested Header queries use DuckDB's existing nested-data/JSON functions. Selecting direct values, complete sections, keys or descendant paths does not require another query language.

## Query connector and graph expansion

Use native SQL for SELECT, FROM, WHERE, CTEs, subqueries, aggregation, GROUP BY, HAVING, sorting, string functions and regular expressions. Follow the selected SQL engine's rules rather than reproducing them in a second evaluator.

Expose only the small CAPRMEDIO helpers that SQL lacks. Start with `expand` as a table-returning helper or SQL macro over recursive traversal:

- Accept a seed reference and one or more registered Relation Types.
- Include the seed and each reachable reference once.
- Follow the selected directions; terminate on cycles.
- Return references, not fetched copies of objects. Use SQL queries or CTEs to retrieve the referenced objects.
- Resolve the seed unambiguously. Require reference kind/context where a name alone is ambiguous.
- Use only indexed links. Do not infer links from prose or interpret every Formal Claim as a graph declaration.

Keep direct relation facts once. Resolve a declared derived counterpart, such as CONTAINS, from the corresponding direct fact. The database does not create another source relation or update a container Atom because its children changed.

Structural links for Scope Units must come from their governed declarations/inventory, not guessed folder names or the retired Project Structure TOML. Implementing arbitrary semantic CFEL evaluation is outside this proposal.

## Background synchronization

Start with one background task in the existing server. Periodic reconciliation is enough; filesystem notifications may later wake it sooner but are not required for correctness.

1. On startup, scan the complete governed source inventory. Reconcile existing database state before exposing it as the current query Projection.
2. Compare source paths and content fingerprints. Read changed sources into memory using the existing stable-read approach.
3. If a source changes while being read, retry it on a later pass. Do not publish a mixture of reads.
4. Update an Atom record, its Content Properties and its owned relation rows together in one database transaction.
5. Reconcile creates, edits, renames, moves and deletions. A move changes the indexed locator; it does not itself create a new source Version. Confirm absence before removing a deleted source's derived records.
6. Repeat reconciliation after restart and while running, including edits made while Docker was stopped. A missed notification must not permanently leave old rows in DuckDB.

Queries see one committed database state. That state reflects completed synchronization work; it is not a promise that the live filesystem cannot change during a query. Exact polling intervals and the derived database path are implementation choices to settle from the existing runtime and measured cost.

## Errors

Return valid query results. Send source-file errors to stderr, including the path, error and available line/column. Do not add diagnostics as fake result rows.

If a new or edited file is invalid, exclude its indexed data and owned derived rows until it is fixed. An old valid version must not continue to appear as the current file. Re-read the file after later changes and restore its rows when it becomes valid. Do not repair or rewrite the source automatically.

Examples include invalid YAML, duplicate keys, undecodable source text, conflicting normalized heading paths and ambiguous Current identities. Do not pick one duplicate Current Atom arbitrarily. A source read error is not proof that the source was deleted.

One invalid file does not stop valid files from being indexed or queried. Results can therefore omit invalid sources; stderr is the error channel. Synchronization failures leave database transactions uncommitted, report the failure and retry rather than exposing half-updated rows.

SQL errors are separate from source-file errors. Return them to the caller; do not return an empty successful result for an invalid query.

## MCP tool

Provide one query tool with Run and Check operations, backed by the same SQL connector.

- Run returns the full query result, column names/types, row count and column count.
- Check reports whether the query is valid, its exact row count and column count, or its error. Exact row counts require executing the read-only query; a successful Check does not modify the Projection or source files.
- Neither operation silently adds LIMIT or truncates rows. If the transport cannot carry the complete result, report that explicitly instead of claiming a complete result.
- Query errors must be returned through MCP as errors as well as being available in server diagnostics. Background file errors go to stderr.

The counts and rows describe the same query execution. Check does not guarantee that a later Run sees the same source state.

## Simple web interface

Serve one small query page from the existing application. Include a SQL text area, Check and Run buttons, row/column counts, ordinary result rows and query errors. Use the same connector as MCP; do not implement another query evaluator.

Keep the interface within the existing local server boundary. No separate frontend application or extra web service is needed. Showing ordinary rows on the page does not introduce custom TABLE, DOC or TREE modes.

## Implementation and acceptance

1. Add the DuckDB dependency to the Docker runtime and make its derived state rebuildable.
2. Extend/reuse the Atom reader for nested Header data and the Markdown Property mapping above.
3. Add the single-owner synchronizer and source-error handling.
4. Add read-only SQL and the graph helper.
5. Add the MCP Run/Check tool and simple query page.

Check these behaviors with small source fixtures: scalar/list/null/absence distinctions; a section with both direct text and a child; Claim with Prose Claim and Formal Claim; headings inside code fences and Prose Claim values; duplicate normalized headings; invalid edit followed by repair; rename/move/delete; duplicate Current identities; restart reconciliation; cyclic traversal; exact query counts; full results; SQL errors; and owner handoff during hot reload.

Also check the query boundary: writes, including data-modifying CTEs, fail; unrelated file/network reads fail; SQL cannot re-enable external access; a query finishes before synchronization opens a read-write handle; and the synchronizer can resume after a failed query. Do not implement a separate SQL parser to enforce this.

Do not add source-writing queries, a custom CFEL query parser, general Formal Claim execution, custom result views or a renderer in this first version.

## Existing components and references

- `connector_atom_read.py` already returns an Atom's source, frontmatter and Markdown content. It does not yet supply the nested Content Property index proposed here.
- Existing reader stable-read and inventory helpers are reuse candidates. Their presence does not establish database synchronization support.
- Keep scheduler storage and query storage separate.
- [DuckDB concurrency](https://duckdb.org/docs/stable/connect/concurrency): one-process ownership for native read/write access.
- [Python connection modes](https://duckdb.org/docs/stable/clients/python/dbapi) and [configuration](https://duckdb.org/docs/stable/configuration/overview): native read-only query execution, external-access settings and configuration locking.
- [Recursive CTEs and graph traversal](https://duckdb.org/docs/stable/sql/query_syntax/with), [table macros](https://duckdb.org/docs/stable/sql/statements/create_macro), [JSON](https://duckdb.org/docs/stable/data/json/overview) and [regex](https://duckdb.org/docs/stable/sql/functions/regular_expressions): existing engine capabilities to reuse.

This is a new Specification Proposal. Docker, reader, synchronization, MCP and web implementation remain future work.

## RMEDO Draft index

- [CA-R-2723](../04_requirement/draft/duckdb-query-projection/CA-R-2723@1-draft-FRAMEWORK_ENGINE-RULE--derive-query-projection-only-from-governed-atom-sources.md)
- [CA-R-2724](../04_requirement/draft/duckdb-query-projection/CA-R-2724@1-draft-FRAMEWORK_ENGINE-RULE--expand-indexed-relation-references-with-complete-cycle-safe-results.md)
- [CA-R-2725](../04_requirement/draft/duckdb-query-projection/CA-R-2725@1-draft-FRAMEWORK_ENGINE-RULE--expose-only-valid-synchronized-source-state-through-query-projection.md)
- [CA-R-2726](../04_requirement/draft/duckdb-query-projection/CA-R-2726@1-draft-FRAMEWORK_ENGINE-RULE--preserve-atom-header-and-markdown-content-faithfully-in-query-projection.md)
- [CA-R-2727](../04_requirement/draft/duckdb-query-projection/CA-R-2727@1-draft-FRAMEWORK_ENGINE-RULE--provide-a-simple-web-query-interface-over-the-shared-query-capability.md)
- [CA-R-2728](../04_requirement/draft/duckdb-query-projection/CA-R-2728@1-draft-FRAMEWORK_ENGINE-RULE--provide-native-sql-query-capability-over-query-projection.md)
- [CA-R-2729](../04_requirement/draft/duckdb-query-projection/CA-R-2729@1-draft-FRAMEWORK_ENGINE-RULE--return-complete-consistent-results-for-query-run-and-check.md)
- [CA-M-462](../05_method/draft/duckdb-query-projection/CA-M-462@1-draft-FRAMEWORK_ENGINE-ENG_DECISION--constrain-public-duckdb-queries-to-native-read-only-access.md)
- [CA-M-463](../05_method/draft/duckdb-query-projection/CA-M-463@1-draft-FRAMEWORK_ENGINE-ENG_DECISION--keep-duckdb-projection-ownership-in-the-existing-server.md)
- [CA-M-464](../05_method/draft/duckdb-query-projection/CA-M-464@1-draft-FRAMEWORK_ENGINE-ENG_DECISION--preserve-governed-atom-data-and-reuse-native-sql.md)
- [CA-M-465](../05_method/draft/duckdb-query-projection/CA-M-465@1-draft-FRAMEWORK_ENGINE-ENG_DECISION--reconcile-duckdb-derived-state-from-stable-governed-inventory.md)
- [CA-E-673](../06_evaluation/draft/duckdb-query-projection/CA-E-673@1-draft-FRAMEWORK_ENGINE-EVAL_CASE--align-mcp-run-check-and-web-results.md)
- [CA-E-674](../06_evaluation/draft/duckdb-query-projection/CA-E-674@1-draft-FRAMEWORK_ENGINE-EVAL_CASE--enforce-native-read-only-and-exclusive-owner-handoff.md)
- [CA-E-675](../06_evaluation/draft/duckdb-query-projection/CA-E-675@1-draft-FRAMEWORK_ENGINE-EVAL_CASE--preserve-nested-header-and-markdown-property-distinction.md)
- [CA-E-676](../06_evaluation/draft/duckdb-query-projection/CA-E-676@1-draft-FRAMEWORK_ENGINE-EVAL_CASE--query-native-sql-results-and-typed-relation-expansion.md)
- [CA-E-677](../06_evaluation/draft/duckdb-query-projection/CA-E-677@1-draft-FRAMEWORK_ENGINE-EVAL_CASE--reconcile-source-lifecycle-and-invalid-repair-state.md)
- [CA-D-672](../07_delivery/draft/duckdb-query-projection/CA-D-672@1-draft-FRAMEWORK_ENGINE-ENG_DECISION--deliver-duckdb-atom-content-and-relation-records.md)
- [CA-D-673](../07_delivery/draft/duckdb-query-projection/CA-D-673@1-draft-FRAMEWORK_ENGINE-ENG_DECISION--deliver-shared-query-run-and-check-results.md)
- [CA-D-674](../07_delivery/draft/duckdb-query-projection/CA-D-674@1-draft-FRAMEWORK_ENGINE-ENG_DECISION--deliver-simple-sql-query-page.md)
- [CA-D-675](../07_delivery/draft/duckdb-query-projection/CA-D-675@1-draft-FRAMEWORK_ENGINE-ENG_DECISION--place-duckdb-projection-in-rebuildable-runtime-state.md)
- [CA-O-240](../09_operations/draft/duckdb-query-projection/CA-O-240@1-draft-FRAMEWORK_ENGINE-ACTION--execute-one-read-only-duckdb-query.md)
- [CA-O-241](../09_operations/draft/duckdb-query-projection/CA-O-241@1-draft-FRAMEWORK_ENGINE-ACTION--reconcile-the-duckdb-query-projection.md)
- [CA-O-242](../09_operations/draft/duckdb-query-projection/CA-O-242@1-draft-FRAMEWORK_ENGINE-STEP--execute-the-shared-read-only-duckdb-query.md)
- [CA-O-243](../09_operations/draft/duckdb-query-projection/CA-O-243@1-draft-FRAMEWORK_ENGINE-STEP--reconcile-governed-sources-in-the-duckdb-query-projection.md)
- [CA-O-244](../09_operations/draft/duckdb-query-projection/CA-O-244@1-draft-FRAMEWORK_ENGINE-WORKFLOW--reconcile-the-duckdb-query-projection.md)
- [CA-O-245](../09_operations/draft/duckdb-query-projection/CA-O-245@1-draft-FRAMEWORK_ENGINE-WORKFLOW--run-or-check-a-duckdb-query.md)
