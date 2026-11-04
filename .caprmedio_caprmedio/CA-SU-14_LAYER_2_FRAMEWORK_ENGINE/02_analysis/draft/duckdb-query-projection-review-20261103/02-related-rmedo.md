# Related Current-RMEDO review — DuckDB query Projection

## Result

**Verdict: substantively aligned; one implementation/instantiation binding,
one unresolved Current-versus-Draft alignment, and one filename supersession
remain.** The 26 new RMEDO Drafts are a coherent local specialization of the existing
`CAPRMEDIO_MODEL <+ Projection` model. They do not create a new domain entity,
query language, relation kind, source authority, or result-view authority.
Their `atoms`, `atom_content_properties`, and `relation_edges` are explicitly
database representations, not model entities (CA-A-1316:119-131).

The intended boundary is clear: Atom carriers remain authoritative; DuckDB is
rebuildable derived state; source-file diagnostics are not SQL result rows; and
ordinary native-SQL rows are the first delivery. This matches the Current
definition of a Projection as a non-authoritative view of source Atoms
(CA-R-2535:21-30), Current relation-source rules, and the existing
failure-observability policy.

Scope: this review read all 27 snapshot inputs, then only related Current
Core/Engine RMEDO source carriers. Drafts, archived carriers, generated
projections, delivery copies, implementation code, Docker, and tests were not
treated as authority. CA-A-1315 is considered only as a non-governing
alternative proposal.

Snapshot baseline: `/private/tmp/duckdb-rmedo-review-input-snapshot-20261103.json`
was captured at `2026-11-03T21:31:20.600449+04:00`; it records CA-A-1316@2
(`f63a6754…81ffd`) and 26 `@1-draft` RMEDO files. The recorded hashes are a
review baseline, not an approval or promotion receipt.

## Findings

### 1. Implementation/instantiation binding gap — identify the concrete Projection when one is created

**Draft evidence.** CA-R-2723 derives the query Projection only from canonical
Atom carriers in “the governed source inventory” and keeps locator, identity,
Version, lifecycle group, Header, and Content (CA-R-2723:24-38). CA-M-465
makes that inventory the complete input to startup and periodic reconciliation
(CA-M-465:28-42). CA-D-675 correctly keeps the database outside authority roots
and rebuildable from governed carriers (CA-D-675:28-40). None names the
particular existing Selection/source-of-truth record that defines this
inventory, nor the stable identity of a concrete runtime Projection instance.

**Related Current authority.** Every Projection has one stable ID, determined
by its Type, named source selection, and source of truth (CA-R-1943:30-40).
Its generator/procedure and declared configuration must say how it is rebuilt
(CA-R-1493:19-29), and a refresh may happen only after every declared source
Atom exists (CA-R-1507:19-31). Current separates governing derivation from
carrier persistence (CA-R-1460:19-31). That supports DuckDB and does not
require a Markdown Projection file or CA-D-635 file-carrier metadata.

**What this does and does not mean.** These Drafts define generic RMEDO
behaviour. CA-R-1943 requires an ID when there is a Projection instance, but no
Current source reviewed requires a generic RMED Draft to materialize that
instance, its ID, or its named Selection before the RMED definition itself can
be promoted. The Drafts therefore inherit Projection identity rules without
yet supplying a runtime binding. That is a gap to resolve when the service is
instantiated, not a promotion blocker for the generic Claims.

**Concrete consequence at instantiation.** If two Projects call their database “the DuckDB
query Projection” but select different inventories—for example, one includes a
history carrier and the other excludes it—the Draft language cannot establish
whether they are one Projection rebuilt at different times or two distinct
Projections. The first has one ID; the second must not silently share it. A
later implementation would make that authority choice itself.

**Smallest resolution.** Before exposing a concrete runtime instance, add one
implementation/instantiation binding—not a new model entity or database
table—that names: (1) the existing Project-local
governed Atom-inventory/selection authority; (2) the query Projection's stable
ID, source of truth, and existing Projection Type; and (3) its
generator/configuration owner. State that Current, Draft, and historical
carriers are distinct members only where this named inventory includes them.
This lets CA-R-2723/CA-M-465 inherit Current rules without making the database
authoritative.

### 2. Unresolved Current-versus-Draft alignment — Journal and exact-revision recording

**Draft evidence.** The Operations chain deliberately does not turn a public
query or background reconciliation into business journaling: CA-O-240 returns
the exact SQL result and says it does not create a business Journal
(CA-O-240:42-46); CA-O-241 returns actual reconciliation counts and retry state
(CA-O-241:44-48); and CA-O-244 says its server background Workflow
does not write business Journals (CA-O-244:40-44). CA-A-1316 defines a query
result as one committed database state, not a promise that the live file system
cannot change during a query (CA-A-1316:168-179).

**Related Current authority.** CA-R-1525 makes every semantic Workflow Run
retain exact Workflow/Step/Action revisions in the Project Journal
(CA-R-1525:29-45). CA-R-1649 requires one Work Journal Action per Projection
rebuild (CA-R-1649:24-34), and CA-R-1728 requires every rebuild attempt to bind
exact source revisions and Journal records (CA-R-1728:23-29). If O-244/O-245
are admitted as those generic semantic Workflow Runs and Projection Rebuilds,
Current and Draft authority command incompatible observability.

The packet design is clear that the database exposes committed state and does
not write a business Journal. CA-A-1316 itself, however, neither requires nor
forbids Journal provenance. The earlier rejection of fixed tool-file pins is
not a blanket rejection of recording actual semantic Workflow versions or
history. Consequently, the relation between these O Drafts and CA-R-1525/1649/
1728 is unresolved; this report cannot treat it as an already approved
exception.

**Required alignment question, not a prescribed resolution.** On adoption,
decide whether the public query/reconciliation invocation is within the Current
semantic Workflow Run/Projection Rebuild scope, and, if it is, how the Draft's
no-business-Journal wording coexists with that scope. A service-routine scope
boundary and a narrowly governed exception are possible dispositions, but this
review does not choose between them. Do not add a Journal gate, source-version
pin, or stale-row rule to the Draft merely from this report; equally, do not
silently assume the Current generic rules are inapplicable.

### 3. Adoption conflict, intentionally superseded — new-Atom Draft filename form

**Draft evidence.** Every new record has a base `atom_id` in frontmatter and a
matching `CA-…@1-draft` filename. CA-R-2723, for example, has
`atom_id: CA-R-2723` and filename `CA-R-2723@1-draft-…` (CA-R-2723:1-18).
The same pattern holds across R, M, E, D, and O. A Current-source search found
no non-Draft carrier for any of the 26 base IDs, so these are new Atoms, not
revisions.

**Related Current authority.** CA-D-650 requires `ID@proposed-version-draft`
for a Draft that revises an existing Atom, but retains a role-only marker for a
new Atom (CA-D-650:27-36). Its current-version-plus-one statement therefore
does not apply to these IDs. The latest explicit user decision nevertheless
settled the general filename form as `ID@version-draft`, with base IDs in
Header/index positions.

**Smallest resolution.** Preserve the 26 filenames and headers. At adoption,
replace or supersede CA-D-650's new-Atom role-only branch with the settled
form, explicitly keeping its N+1 rule limited to genuine revisions. This is a
concrete receiving-rule conflict, not a reason to mutate Draft headers to
version-qualified IDs or rename them back to role-only filenames.

## Alignment evidence

The local specialization is necessary rather than a duplicate general
definition. Current Core says Header is YAML-frontmatter Properties, including
Drafts (CA-R-2719:23-34); Content is a nested Markdown property tree
(CA-R-2498:23-31); and an RMED Claim is a container with Formal Claim and/or
Prose Claim children (CA-R-2500:23-36). CA-D-663 preserves actual heading
ancestry, direct values, skipped-level behaviour, and fenced text
(CA-D-663:19-55). CA-R-2726/CA-M-464/CA-D-672 do not redefine these. They say
how one query Projection preserves original bytes, nested values,
direct-versus-section Markdown, and collision rejection.

The invalid-file rule is compatible, not a conflict. CA-D-663 leaves failed
mapping source Markdown intact (CA-D-663:51-55); CA-R-2725/CA-O-241 exclude
only that source's *derived query rows* until repair, retain the source itself,
write its path/error to stderr, and continue indexing valid carriers
(CA-R-2725:32-40; CA-O-241:45-48). A bad heading map therefore neither
overwrites the source nor becomes a fake SQL row.

The RMEDO structure matches Current role, tier, and relation boundaries.
`method_for`, `evaluation_for`, `delivery_for`, and `depends_on` are registered
direct relations (CA-R-1017:27-43; CA-R-1018:32-48; CA-R-1019:27-43;
CA-R-1026:29-47). The Drafts use Requirements at Tier 3, Methods/Deliveries at
Tier 4, Evaluations at Tier 5, and Operations at Tier 6. No unexpected
same-tier RMED governing link was observed; CA-R-2149's lower-tier/ancestor
rule applies only to selected governing relations (CA-R-2149:25-35).

The Workflows also have the intended separation. CA-O-244/O-245 own trigger or
request routing and terminal handling; CA-O-243/O-242 each identify one Step
and bind inputs; CA-O-241/O-240 own the Actions. That matches Current Workflow
graph separation (CA-R-1570:19-33), `RUNS` semantics (CA-R-2638:23-36), and
Step-owned parameter binding (CA-R-2639:23-39). It adds no relation kind or
action executor.

The direct/complete Markdown distinction is a necessary query specialization,
not a silent change to the general model. Current markdown Format says a
retrieved section includes its heading and descendants (CA-R-2547:19-24), while
CA-D-663 says direct-value cardinality excludes child values
(CA-D-663:48-53). CA-R-2726 turns that existing distinction into two queryable
values, `direct Markdown` and `complete section Markdown`; it does not invent a
`$value` model property, merge children into parents, or claim that the
Projection's tables are source facts. That is compatible inheritance.

The same is true of graph expansion. CA-R-1437 requires one authoritative
source for every independently authored relation fact and traceability for a
derived relation (CA-R-1437:24-36). CA-R-2486 says a relation signature
constrains links but does not create them (CA-R-2486:19-35). CA-R-2724 and
CA-M-464 therefore correctly restrict `expand` to indexed, registered direct
facts; the derived counterpart is resolved from that direct fact and prose is
not mined into an edge. The helper returns references, leaving an ordinary SQL
join or CTE to fetch projected Atom data. No separate graph model is needed.

The MCP/web delivery boundary also remains local. CA-D-673 requires the same
native-SQL connector for Run and Check and separates source-file errors from
SQL errors (CA-D-673:28-42); CA-D-674 requires the web page to reuse that
connector rather than add an evaluator (CA-D-674:27-37). This fits the Current
shared public-operation boundary: reuse one error owner, preserve the
transport's own result/error contract, and do not turn an error into false
success (CA-M-400:21-38). The Draft packet therefore has enough local
specificity to prevent duplicate query semantics without taking ownership of a
general Runtime error model.

## Sources

The authoritative comparison sources were Current Markdown carriers in the
Core Meta Model and Framework Engine roots, not their copies under
`000_CAPRMEDIO_framework`, `applicable_methodology`, or `_projection`.
Projection authority: CA-R-2535, CA-R-1460, CA-R-1493, CA-R-1507, and
CA-R-1943. Header/Content/Claim/heading authority: CA-R-2719, CA-R-2498,
CA-R-2500, CA-R-2721, CA-R-2722, CA-R-2547, and CA-D-663. RMED relation,
tier, and Operations authority: CA-R-1017/1018/1019/1026, CA-R-1570,
CA-R-2149, CA-R-2463/2464/2465, CA-R-2638/2639, and CA-D-467. The potential
receiving-rule conflicts were checked against CA-R-1525, CA-R-1649,
CA-R-1728, and CA-D-650. Engine error/source-snapshot comparators were
CA-M-396, CA-M-400, CA-R-1849, and CA-R-1866. All 27 snapshot hashes matched
their recorded SHA-256 values during this review.

## Rejected candidates

- **CA-A-1315 CFEL custom-query proposal is not governing authority.** It is
  an Active Specification Proposal and itself says adoption/implementation are
  future work (CA-A-1315:214-223). Its CFEL `TABLE`/`FULL` views are an
  alternative, not a reason to require them, a renderer, or a custom parser
  here. CA-A-1316 and CA-D-673 deliberately defer them.
- **The sealed source snapshot of `FIND_AND_FETCH_JOURNAL_EVENTS` is out of
  scope.** CA-R-1866 governs that named journal-event tool
  (CA-R-1866:20-43). CA-R-1849 governs a bounded Markdown artifact tool
  (CA-R-1849:20-50). Neither creates a general fixed-pin rule for this
  continuously reconciled DuckDB Projection.
- **No “source error must fail every query” finding.** CA-M-396 requires actual
  failure to remain observable without disabling healthy work (CA-M-396:20-35).
  The Draft's stderr channel plus valid committed rows follows that policy and
  preserves the intended distinction between source diagnostics and SQL errors.
- **No missing SQL view/renderer finding.** CA-R-2727 and CA-D-674 explicitly
  require ordinary rows through the shared connector and defer TABLE/DOC/TREE
  modes (CA-R-2727:28-38; CA-D-674:31-37).

## Uncertainty and not checked

The exact Current carrier that names the Project's governed Atom inventory was
not identified in the packet, so this review cannot choose its selection,
Projection ID, or generator/configuration on the Operator's behalf. It also
does not establish DuckDB security/concurrency behaviour, parser fidelity,
runtime integration, test results, or delivery status. Those are the assigned
implementation/evaluation surfaces. No Current source was changed and no Draft
was promoted.

## Next action

At runtime instantiation, bind the concrete Projection identity and selection.
At adoption, resolve the Journal/exact-revision applicability question and
record the settled new-Atom filename supersession. Then let the other assigned
reviews decide Draft-internal and implementation surfaces. Do not add a custom
query language, renderer, source-writing path, or new model entity as part of
this alignment.
