---
atom_id: CA-A-1315@1
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
version: 1
author: Anatoly Maslennikov
relations:
  depends_on:
  - CA-R-2487
  - CA-R-2549
  - CA-R-2550
  - CA-R-2552
  - CA-R-2566
  - CA-R-2585
tier: 3
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL
role: Analysis & Advisory
form: Specification Proposal
updated_at: 2026-11-03 17:23:56 +0400
---

## Summary

Add basic CFEL queries with CTEs and SQL aliases

## Proposal

Extend CFEL with read-only queries. Use existing CFEL addresses, instance selectors, Properties, conditions and Relation expressions. Add a small query structure with familiar SQL words.

Include Common Table Expressions (CTEs) from the start:

```CFEL
WITH name AS (
  SELECT ...
  FROM ...
  WHERE ...
)
SELECT ...
FROM name AS row;
```

CTEs name results within one query. They do not declare a stored Selection, create a model entity, or change a source.

## Starting points

| Reference | Use in CFEL queries |
| --- | --- |
| Obsidian Dataview | Read Properties and content through a logical model; select fields, filter, sort and limit results. |
| Jira Query Language (JQL) | Keep simple conditions readable: field, operator, value; combine them with AND, OR, NOT and parentheses. |
| PostgreSQL | Use SELECT, FROM, WHERE, AS, ORDER BY, LIMIT and non-recursive WITH queries. |
| ClickHouse | Keep the same readable query clauses while leaving execution and storage choices outside the language. |

These are design references, not compatibility targets. CFEL keeps its own value, identity and absence rules.

Dataview documents its query structure and command order in [Structure of a Query](https://blacksmithgu.github.io/obsidian-dataview/queries/structure/). Its [Query Types](https://blacksmithgu.github.io/obsidian-dataview/queries/query-types/) show field selection and AS labels. JQL documents its [clause structure](https://support.atlassian.com/jira-service-management-cloud/docs/what-is-advanced-search-in-jira-cloud/), [keywords](https://support.atlassian.com/jira-service-management-cloud/docs/jql-keywords/) and [operators](https://support.atlassian.com/jira-service-management-cloud/docs/jql-operators/).

PostgreSQL provides the reference [SELECT structure](https://www.postgresql.org/docs/current/sql-select.html) and [WITH examples](https://www.postgresql.org/docs/current/queries-with.html). ClickHouse provides another [SELECT implementation](https://clickhouse.com/docs/sql-reference/statements/select) and [WITH implementation](https://clickhouse.com/docs/sql-reference/statements/select/with).

## First version

| Construct | Meaning |
| --- | --- |
| FROM | Select one source: a CFEL instance selector, or a named CTE result. |
| WHERE | Keep rows for which the condition is true. Use existing CFEL conditions. |
| SELECT | Return an existing instance reference or selected expressions. |
| AS | Give an output column or CTE a local name; bind a CTE row to a query variable. |
| DISTINCT | Remove duplicate output rows using component-wise equality of their selected values. |
| SORT | Order rows by one or more scalar expressions. ASC is the default; DESC reverses it. |
| LIMIT | Return at most the given nonnegative integer number of rows. |
| WITH name AS (query) | Name a query result for use by a later CTE or the final SELECT. |

Use one fixed clause structure:

```CFEL
[WITH name AS (query), ...]
SELECT [DISTINCT] expression [AS column], ...
FROM source
[WHERE condition]
[(SORT | ORDER BY) expression [ASC | DESC], ...]
[LIMIT number];
```

Square brackets in this outline show optional syntax; a vertical bar shows alternatives. These are outline conventions, not CFEL Format brackets or new operators. The final semicolon ends the complete query; CTE bodies have no trailing semicolon.

The source alternatives have distinct binding types:

| Source form | Required result kind |
| --- | --- |
| `FROM full-kind-address//$atom` | Existing model instances bound to `$atom`. |
| `FROM InstanceCTE AS $atom` | A CTE returning existing instance references. |
| `FROM RowCTE AS row` | A CTE returning named value rows. |

Using an instance binding for a named row, or a row alias as a model instance, is an error.

The logical order is FROM, WHERE, SELECT, DISTINCT, SORT, LIMIT. This is a fixed query structure, rather than Dataview's freely repeated data-command sequence. LIMIT does not turn an earlier invalid expression into a valid result.

WHERE can read source bindings, not SELECT aliases. SELECT expressions are evaluated for every row that survives WHERE, before DISTINCT or LIMIT removes any row. SORT can read output column names and source bindings; with DISTINCT, it can read only output column names. Guarded conditions retain CFEL short-circuiting. An execution plan must not change these results or errors by moving a field read across its guard or limit.

The initial source context is one explicitly selected Project snapshot. Atom selectors use Current Atoms, including Done or Canceled where applicable. Current does not mean Status = Active. Drafts and archived versions require a later explicit history-query extension.

FROM names logical model entities or CTEs, not filenames, folders, SQL tables or storage-specific columns. The caller selects the source scope; the query does not invent a storage connection.

## CFEL syntax and SQL aliases

Preserve existing CFEL meanings:

- `/` narrows a kind; `//` selects its existing instances.
- `$atom` keeps the selected instance binding; `.Property` reads its logical Property.
- `=` tests equality. It is not assignment. `==`, `:` and `:=` keep their existing meanings.
- `AND`, `OR`, `NOT` and parentheses form conditions. Existing guarded reads and left-to-right short-circuiting still apply.
- `in` and `not in` retain instance-identity membership. They do not silently become scalar-list comparisons.
- `((RELATION))` and its reverse notation test existing Relations where the current CFEL expression permits them.
- `?=`, COUNT and MAX keep their existing CFEL meanings. In particular, COUNT of direct Property values is not SQL row COUNT.
- `*` and `**` keep their Property meanings. The first version does not add SELECT * or COUNT(*).

Add only these spelling aliases initially:

| CFEL query spelling | SQL spelling | Meaning |
| --- | --- | --- |
| SORT | ORDER BY | The same ordering clause. |
| != | <> | The same inequality test. |
| in / not in | IN / NOT IN | The same existing instance-membership operation. |

SELECT, FROM, WHERE, WITH and AS are new query clauses, not new meanings for existing CFEL operators. Query keywords may be written in either case. Model names, Property names, values and local names retain their exact spelling; keyword handling does not add case folding to them.

Use model-level names such as `.Content.Summary`, rather than frontmatter keys or physical storage paths. AS changes only the returned column name or a local binding. It does not rename the model Property.

## CTEs from the start

- A query may have several CTEs, separated by commas.
- Each CTE name is unique within that WITH block.
- A CTE may read model sources and earlier CTEs in the same block.
- Each CTE body uses the same SELECT structure shown above, without another WITH block. Nested WITH is deferred.
- Self-reference, forward reference and cycles are errors in the first version.
- The final statement is SELECT. Data-changing CTEs are out of scope.
- Every CTE uses the same Project snapshot and source scope as the final query.
- A CTE can return existing instance references or rows of named values. A later FROM binds each result to an explicit variable with AS.
- Names exist only within this query. Reusing a CTE does not create a persistent instance or register a named Selection.
- A CTE's internal SORT can decide which rows its LIMIT keeps. The final query needs its own ordering if final presentation order matters.

Keep the two result forms explicit. `SELECT $atom` by itself returns an instance-reference stream, without named columns; a later `FROM name AS $atom` binds those same instances. A field projection returns named result rows; `FROM name AS row` binds one such row, and `row.Column` reads its output field. An instance reference can also be a named column: `SELECT $atom AS Atom, $atom.Status AS Status` returns rows. In a named-row projection, a whole instance expression needs AS.

`AS $atom`, `AS row` and `row.Column` are proposed query-only forms. They add binding sites and access to derived row fields; existing Formal Claims keep their current binding and Property rules. `$` still binds only existing model instances. A result row is not a declared model Node or a valid graph Relation endpoint.

CTE names belong to the WITH block; source aliases belong to their SELECT; output names belong to its result schema. Local names cannot be query keywords. Resolve a local name only within its stated query scope. Model sources retain their full CFEL addresses, so a local name never silently shadows or replaces a model reference.

Do not promise that a CTE executes once or is materialized. PostgreSQL and ClickHouse make different execution choices: [PostgreSQL WITH](https://www.postgresql.org/docs/current/queries-with.html) describes folding and materialization, while [ClickHouse WITH](https://clickhouse.com/docs/sql-reference/statements/select/with) describes CTE substitution and re-execution. CFEL requires the same logical result and errors within the snapshot, not a particular execution plan.

## Examples

Select Active Requirements and return their IDs and Summaries:

```CFEL
SELECT $atom.ID, $atom.Content.Summary AS Summary
FROM CAPRMEDIO <+ MODEL <+ Atom//$atom
WHERE $atom.Role = Requirement AND $atom.Status = Active
ORDER BY $atom.ID ASC
LIMIT 20;
```

Keep a reusable intermediate set, then filter it:

```CFEL
WITH Requirements AS (
  SELECT $atom
  FROM CAPRMEDIO <+ MODEL <+ Atom//$atom
  WHERE $atom.Role = Requirement
)
SELECT $atom.ID, $atom.Content.Summary AS Summary
FROM Requirements AS $atom
WHERE $atom.Status = Active
SORT $atom.ID ASC
LIMIT 20;
```

Chain two CTEs and read named output fields:

```CFEL
WITH Requirements AS (
  SELECT $atom
  FROM CAPRMEDIO <+ MODEL <+ Atom//$atom
  WHERE $atom.Role = Requirement
),
ActiveRequirements AS (
  SELECT $atom.ID AS ID, $atom.Content.Summary AS Summary
  FROM Requirements AS $atom
  WHERE $atom.Status = Active
)
SELECT row.ID, row.Summary
FROM ActiveRequirements AS row
ORDER BY row.ID ASC
LIMIT 20;
```

Get the distinct Roles present in the selected Current Atom sources:

```CFEL
SELECT DISTINCT $atom.Role AS Role
FROM CAPRMEDIO <+ MODEL <+ Atom//$atom
ORDER BY Role ASC;
```

## Values, results and errors

- A false condition excludes a row. An evaluated missing, invalid or unresolved value remains an error under the existing CFEL rules.
- An omitted Property is not an authored null, empty string, false or zero. Do not import SQL NULL rules or JQL EMPTY rules under another spelling.
- Optional Properties need an existing CFEL guard or fallback before a read that requires a value.
- A multi-value Property remains a collection. Projection does not expand it into extra rows, and scalar comparison does not broadcast over it.
- Output keeps one row per source row unless DISTINCT is requested. A CFEL instance selector still counts each logical instance once across Carrier representations.
- DISTINCT compares corresponding output columns. Scalar and collection values use their declared Format's equality; instance references use identity. Whole-instance results also use identity. An undefined equality rule is an error.
- Each output column needs a unique name. A plain Property projection defaults to its final Property name; a calculated expression needs AS. Duplicate column names require explicit distinct aliases.
- CTE names, query bindings and column names are local query names. They do not change the global model-name rules.
- Numeric and datetime sorting reuse their Format-defined ordering. As a new query-only rule, text sorting uses exact Unicode code-point order, without locale rules or case folding. This does not make text orderable by the existing MAX function. Mixed or non-orderable values are errors.
- Without SORT or ORDER BY, row order is unspecified. For a repeatable limited subset, provide an explicit order and a unique final tie-break key.
- An empty result is valid. Unknown sources, unknown fields, unbound variables, invalid CTE references and invalid expressions are errors; they must not return a misleading successful empty result.

Result-row projection, AS bindings, row-level DISTINCT, sorting and CTEs are proposed query behavior. They are not claimed as already admitted CFEL. The unique-column rules apply to named-row results, not the column-free instance-reference result.

## Later extensions

Defer joins and Cartesian products, recursive CTEs, arbitrary subqueries, GROUP BY, HAVING, window functions, scalar-list IN, SQL row aggregates, full-text search, regular expressions, automatic collection expansion, user-defined functions, storage-dialect functions, writes and materialization controls.

Keep existing CFEL expressions usable in SELECT and WHERE where their current rules admit them. Deferring SQL aggregation does not remove the current per-bearer COUNT or scalar MAX functions.

## Adoption work

1. Review the proposed clauses, SQL aliases and CTE result bindings.
2. Add the accepted query and operator Definitions or Declarations to Core CFEL RMED. Preserve the existing operators' meanings.
3. Add examples covering plain queries, both ordering spellings, chained CTEs, instance and row results, Current versus Active, guarded optional reads, collections, duplicate column names, errors and empty results.
4. Implement the accepted contract in separate Engine work. Keep logical query semantics independent of file, database, CLI or MCP connectors.

This is an Active Specification Proposal. It does not adopt the query extension or claim parser, evaluator, MCP or database support.
