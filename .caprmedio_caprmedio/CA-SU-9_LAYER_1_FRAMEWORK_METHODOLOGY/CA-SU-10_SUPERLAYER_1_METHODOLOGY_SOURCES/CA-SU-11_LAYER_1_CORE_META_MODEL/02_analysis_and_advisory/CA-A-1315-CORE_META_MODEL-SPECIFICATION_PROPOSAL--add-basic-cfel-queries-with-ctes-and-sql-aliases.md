---
atom_id: CA-A-1315
ref_id: CA-A-1315
container:
  scope_unit: CA-SU-11
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
tier: 3
relations:
  depends_on:
  - CA-R-2487
  - CA-R-2549
  - CA-R-2768
  - CA-R-2552
  - CA-R-2566
  - CA-R-2585
status: Active
version: 4
updated_at: 2026-11-04 20:33:16 +0400
carrier_destination:
  file:
    name: CA-A-1315-SPECIFICATION_PROPOSAL--add-basic-cfel-queries-with-ctes-and-sql-aliases.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/02_analysis_and_advisory
---

## Summary

Add basic CFEL queries with CTEs and SQL aliases

## Proposal

Extend CFEL with read-only queries. Use CFEL selectors in FROM, ordinary query names, reusable selection functions, and two result views: TABLE and FULL.

The Operator's latest example is the main query shape:

```CFEL
SELECT id, status, content
FROM atom//
WHERE atom in expand(CA-P-123, CONTAINS)
VIEW FULL;
```

SELECT chooses the Properties. FROM chooses the instances. WHERE filters them. VIEW controls how the selected data is shown.

## Sources and context

The query context supplies one Project snapshot and the selected source scope. CAPRMEDIO_MODEL and CAPRMEDIO_STRUCTURE name the two logical contexts: declared model and actual Project structure. They do not have to occupy FROM. This replaces the earlier suggestion that FROM could contain only those two names. No extra context keyword is proposed here.

FROM accepts a CFEL instance selector such as `atom//`, or a CTE name. `atom//` selects Current Atom instances and their narrower kinds. Current includes Done and Canceled where applicable; it is not the same as Status = Active. History queries remain separate.

A short selector is resolved against the model catalog in the supplied context. Ambiguous or unresolved names are errors. Sources are logical selections, not filenames, folders, database tables or physical columns.

## Names and optional aliases

With one source, bare Property names refer to its current item: `id`, `status`, `content.summary`. `atom` is the implicit item name for `FROM atom//`. It names the selected instance in this query, not the Atom kind or its Property declaration.

An explicit alias is optional:

```CFEL
SELECT atom.id, atom.content.summary AS summary
FROM atom// AS atom
WHERE atom.status = Active
VIEW TABLE;
```

An explicit AS alias replaces the implicit source name. Bare Property references remain available. Query aliases are ordinary names without `$`; existing `$` bindings in Formal Claims keep their meaning. A CTE can be read through bare output names or an explicit alias.

The examples propose these readable query aliases for existing model names:

| Query name | Model name |
| --- | --- |
| atom | Atom |
| id | ID |
| role | Role |
| form | Form |
| status | Status |
| content | Content |
| summary | Summary |

These aliases do not rename the model or its Carrier keys. This is an explicit alias set, not a general case-folding or underscore-conversion rule. Other names use their declared spelling or an admitted alias. Data values and Relation names keep their declared spelling.

## Views

SELECT controls the data in both views. Changing VIEW does not change which instances match or which Properties were selected.

| View | Output |
| --- | --- |
| TABLE | One row per result, with the selected expressions as columns. |
| FULL | One Atom block per result, with the selected Properties and Markdown content sections. |

The same selection can use either view:

```CFEL
SELECT id, status, content
FROM atom//
WHERE atom in expand(CA-P-123, CONTAINS)
VIEW TABLE;
```

Change only the last clause to `VIEW FULL;` to render Atom blocks. Do not add another Property list to VIEW.

Selecting `content` includes the complete Markdown content subtree. Selecting `content.claim` includes just that section. A Property container is projected as its nested Properties; this does not give the container a direct scalar value. TABLE keeps such a value in one column rather than expanding it into extra rows. FULL keeps the Atom's content structure and shows only the selected material; it is a result view, not a new authoritative Atom Carrier.

FULL needs one unambiguous source Atom per result. Plain Atom Property projections and AS labels retain that source identity through CTEs. A derived row without a unique Atom reference cannot use FULL. If DISTINCT combines results from different Atoms, FULL must report that ambiguity rather than choose an Atom. TABLE remains usable for those rows.

VIEW belongs to the final query. CTEs produce logical results, not rendered tables or Atom text. If VIEW is omitted, the caller receives the logical result without this proposal prescribing a presentation.

## Global selection functions

Define reusable functions in the CFEL query vocabulary, rather than copying a traversal into every query. They operate on the current query context; they do not register a stored Selection or change source objects.

Start with:

```CFEL
expand(CA-P-123, CONTAINS)
```

This returns the seed Atom and every instance reachable by following CONTAINS repeatedly, at all depths.

- Resolve the seed ID in the selected Current Project snapshot. A missing or ambiguous seed is an error.
- Include the seed.
- Follow only the selected Relation, in its stated direction, including a legitimately derived counterpart such as CONTAINS.
- Return each logical instance once, even when several paths reach it. Do not revisit a seen instance, so cycles terminate.
- Use the same snapshot for the seed, edges and returned instances.
- Return existing instance references. The function creates no Nodes, Relations, lifecycle changes or stored inverse links.

The second argument accepts one Relation name or a parenthesized, comma-separated list: `expand(seed, (relation1, relation2))`. Here the names stand for registered Relations. Treat the list as a set of permitted edge types; each hop may follow any member. An empty list is an error. A bounded-depth argument remains deferred.

The result can be used in identity membership:

```CFEL
WHERE atom in expand(CA-P-123, CONTAINS)
```

This is a function, rather than a simple alias, because it takes a seed and Relation as parameters. It is a proposed global selection function, not arbitrary user code or a storage-specific function.

## CTEs from the start

Include non-recursive WITH queries in the first version. A query can have several CTEs, separated by commas; each can read earlier CTEs in the same block.

```CFEL
WITH EpicTree AS (
  SELECT id, status, content
  FROM atom//
  WHERE atom in expand(CA-P-123, CONTAINS)
),
ActiveAtoms AS (
  SELECT id, status, content
  FROM EpicTree
  WHERE status = Active
)
SELECT id, status, content
FROM ActiveAtoms
ORDER BY id
LIMIT 20
VIEW FULL;
```

CTE names must be unique within the WITH block. Self-reference, forward references and cycles between CTEs are errors in this first version. Each body uses the same SELECT structure, without a nested WITH or a trailing semicolon. The final query ends with a semicolon.

A CTE returns named values or instance references. Source aliases and output fields have query-local scope and do not declare model entities. Plain Property projections preserve their source Atom identity; arbitrary computed rows do not acquire an Atom identity merely by having an ID column. Source or output aliases cannot be query keywords. Output column names must be unique.

Recursive graph selection through expand is included; recursive CTE evaluation remains deferred. These are different operations.

Do not require a particular materialization or number of executions. All reads and reused results must have the same logical meaning and errors within the selected snapshot. PostgreSQL and ClickHouse make different planning choices; their behavior is a reference, not an execution requirement for CFEL.

## First query structure

```text
[WITH name AS (query), ...]
SELECT [DISTINCT] expression [AS column], ...
FROM selector_or_cte [AS alias]
[WHERE condition]
[(SORT | ORDER BY) expression [ASC | DESC], ...]
[LIMIT number]
[VIEW TABLE | VIEW FULL];
```

This is an outline: brackets show optional parts and bars show alternatives. They do not introduce CFEL Format brackets or operators.

The logical order is FROM, WHERE, SELECT, DISTINCT, SORT, LIMIT, VIEW. WHERE reads source Properties and aliases, not SELECT aliases. SELECT expressions are evaluated for every surviving row before DISTINCT or LIMIT removes a row. Guarded conditions retain left-to-right CFEL short-circuiting.

SORT can read output names and source bindings. After DISTINCT it can read only output names, so it cannot choose an arbitrary source from a merged row. ASC is the default. Numeric and datetime order reuse the declared Format. Exact Unicode code-point text order is a new query proposal; it does not extend the existing MAX function. Without ordering, result order is unspecified. Use a unique final sort key when a repeatable limited subset matters.

## CFEL meanings and SQL aliases

Keep the existing meanings of `/`, `//`, `.`, `=`, `==`, `:`, `:=`, Relation expressions, guarded reads, identity membership and absence. The query aliases and functions are additions to the query context, not changes to existing Formal Claims.

| Query spelling | SQL alias | Meaning |
| --- | --- | --- |
| SORT | ORDER BY | Order the same result. |
| != | <> | The same inequality test. |
| in / not in | IN / NOT IN | Existing instance-identity membership. |

Keywords may use either case. Value spelling does not change with keyword case.

An evaluated missing, invalid or unresolved value remains an error; it is not false. Omission is distinct from authored null, empty text, false and zero. Optional reads need an admitted guard or fallback. Collections remain collections: projection does not expand them into rows and scalar comparisons do not broadcast over them.

DISTINCT compares corresponding selected values using their Format's equality, and instance references by identity. An undefined equality rule is an error. It does not silently discard the Atom-identity ambiguity relevant to FULL.

COUNT of direct Property values and scalar MAX keep their existing CFEL meanings. The first version does not add SQL row COUNT, SELECT *, COUNT(*), or scalar-list IN. `*` and `**` retain their existing Property meanings. New row projection, global selection functions, CTEs and views need their own accepted query contract.

An empty result is valid. Unknown selectors, fields, aliases, CTEs or functions are errors, not a successful empty result.

## Starting references

| Reference | Starting point |
| --- | --- |
| [Dataview query structure](https://blacksmithgu.github.io/obsidian-dataview/queries/structure/) and [query types](https://blacksmithgu.github.io/obsidian-dataview/queries/query-types/) | Logical fields, readable filters, selected columns, sorting, limits and presentation. |
| [JQL clauses](https://support.atlassian.com/jira-service-management-cloud/docs/what-is-advanced-search-in-jira-cloud/), [keywords](https://support.atlassian.com/jira-service-management-cloud/docs/jql-keywords/) and [operators](https://support.atlassian.com/jira-service-management-cloud/docs/jql-operators/) | Readable field/operator/value conditions and Boolean composition. |
| [PostgreSQL SELECT](https://www.postgresql.org/docs/current/sql-select.html) and [WITH](https://www.postgresql.org/docs/current/queries-with.html) | Query clauses, aliases and chained non-recursive CTEs. |
| [ClickHouse SELECT](https://clickhouse.com/docs/sql-reference/statements/select) and [WITH](https://clickhouse.com/docs/sql-reference/statements/select/with) | Similar query clauses with different storage and CTE execution choices. |

Use these as references, not full compatibility targets. Do not import their missing-value, coercion or storage rules into CFEL.

## Adoption work

1. Review this query shape, aliases, FULL/TABLE views and expand semantics.
2. Define the accepted query components and reusable functions in Core CFEL RMED.
3. Add examples for bare Properties, optional aliases, Current versus Active, guarded reads, nested content, both views, containment expansion, duplicate paths, cycles, chained CTEs, invalid inputs and empty results.
4. Implement the accepted contract in separate Engine work. Keep file, database, CLI and MCP connectors outside the logical language contract.

Defer joins, recursive CTEs, arbitrary subqueries, GROUP BY, HAVING, window functions, scalar-list IN, SQL row aggregates, full-text search, user-defined function bodies, writes and materialization controls. A registered selection helper such as expand is included; this does not open arbitrary function execution.

This is an Active Specification Proposal. It does not adopt the language changes or claim parser, evaluator or runtime support.
