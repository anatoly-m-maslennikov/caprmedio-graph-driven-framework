---
cce_version: cce_1
cce_form: rationale
subjects:
  declared:
    continuant:
      - methodology
subject_scope: artifact-model
version: 4
updated_at: 2026-08-23 15:00:38
---
# LLM Wiki and graph-driven development

## Source

- [LLM Wiki — Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

## Question

What does Karpathy's LLM Wiki establish about persistent LLM-maintained knowledge, what is relevant to CAPRMEDIO, and where does CAPRMEDIO require stronger governance?

## Source model

The LLM Wiki contrasts ordinary retrieval-augmented generation with a persistent, compounding intermediate artifact. Instead of rediscovering and resynthesizing raw fragments for every question, an LLM incrementally maintains an interlinked Markdown wiki. New sources update entity pages, topic summaries, cross-references, contradictions, and the evolving synthesis.

Karpathy summarizes the operating relationship as:

> “Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.”

The proposed architecture has three layers:

| LLM Wiki layer | Responsibility |
|---|---|
| Raw sources | Immutable source material read but never modified by the LLM |
| Wiki | LLM-generated summaries, entity pages, concepts, comparisons, and synthesis |
| Schema | Instructions defining structure, conventions, and ingest, query, and maintenance workflows |

It also defines three recurring operations:

- **Ingest** integrates a source into the existing knowledge structure instead of merely indexing it.
- **Query** produces cited synthesis and MAY preserve valuable answers as new wiki pages.
- **Lint** looks for contradictions, stale claims, orphan pages, missing concepts, missing cross-references, and research gaps.

A content-oriented index supports navigation, while an append-only chronological log records ingests, queries, and lint passes. Search infrastructure is introduced only when the simpler index stops being sufficient.

## What is graph-like

The LLM Wiki is graph-like because it maintains interlinked pages, cross-references, hubs, and orphans, and because new material changes several connected pages rather than creating an isolated document. Its main architectural contribution, however, is not a formal typed graph. It is the persistent compiled knowledge layer that accumulates structure and synthesis between raw sources and later LLM executions.

Obsidian's graph view visualizes the links, but visualization is not the mechanism that makes the wiki compound. Compounding comes from repeated source integration, cross-reference maintenance, contradiction handling, preservation of useful query results, and periodic health checks.

## CAPRMEDIO mapping

| LLM Wiki mechanism | CAPRMEDIO equivalent |
|---|---|
| Immutable raw source | Pinned external source and its governed provenance |
| Wiki page | Analysis, generated Projection, or proposed Atom |
| Interlinked wiki | Governed semantic graph |
| Schema file | META and GOV rules plus agent-operating instructions |
| Ingest | Source admission followed by Analysis and proposed graph changes |
| Query | Task-specific graph traversal and generated Projection |
| Lint | Graph validation and Evaluation over consistency and currentness |
| `index.md` | Programmatic Catalog or Hub Projection |
| `log.md` | Append-only Journal or factual Ops history |
| Git-backed wiki | Revision history and recoverable lineage |

The strongest common idea is that durable project knowledge should live outside an individual prompt or model context. An LLM invocation consumes and changes a persistent structure; the invocation itself is temporary.

## Authority boundary

Karpathy's model says that raw sources are the source of truth while the LLM owns the entire derived wiki. That is suitable for a personal synthesis system, but it is too permissive for governed development authority. A generated summary can misstate its source, a synthesis can conceal disagreement, and a page filed from an answer can cause the wiki to cite or reinforce its own derivative claims.

CAPRMEDIO therefore needs a stricter boundary:

```text
Raw source
  → generated Analysis or Projection
  → proposed graph change
  → Plan and review
  → admitted Atom
```

The LLM MAY maintain non-authoritative views automatically. It MUST NOT silently convert its synthesis into an authoritative Requirement, Method, Evaluation rule, Delivery rule, or accepted external obligation. Every generated claim needs recoverable source provenance, and every authoritative change needs explicit admission.

## Ideas worth adopting

1. Make `ingest`, `query`, and `lint` first-class graph operations rather than informal prompt patterns.
2. Preserve immutable source inputs and compile their reusable meaning once instead of reconstructing it for every task.
3. Add graph-health checks for contradictions, stale claims, orphans, missing concepts, missing typed connections, and unresolved source gaps.
4. Maintain a programmatic content index and an append-only activity log with different responsibilities.
5. Preserve useful analyses and comparisons outside chat history as governed Analysis or generated Projections.
6. Start with deterministic repository navigation and introduce heavier search only when measured scale requires it.
7. Keep a human involved in source selection, emphasis, contradiction disposition, and authority admission.

## Gaps in the LLM Wiki model

- Links are not given precise relation semantics or endpoint constraints.
- Generated pages do not have explicit authority, lifecycle, or currentness states.
- The source frontier of each derived claim is not required to be revision-bound.
- Lint is an LLM activity rather than a combination of deterministic validation and governed judgment.
- The model does not separate Requirement, Method, Evaluation, Delivery, Implementation, and Ops meanings.
- Filing query answers back into the wiki can create derivative self-reference unless provenance and authority remain explicit.

## CAPRMEDIO gaps exposed

CAPRMEDIO already defines the stronger semantic and authority model, but it does not yet implement the LLM Wiki's operating convenience. It still needs a source-ingest workflow, a graph query and context compiler, generated Catalog and Hub Projections, an append-only operation log, graph-health linting, and a safe path from LLM-generated synthesis to reviewed graph change.

## Conclusion

The LLM Wiki provides a compelling operating pattern for persistent, compounding LLM-maintained knowledge. CAPRMEDIO should adopt its ingest, query, lint, index, and log mechanics while preserving a stricter distinction between immutable evidence, generated synthesis, proposed authority, and admitted authority.

The CAPRMEDIO logline captures that relationship: prompts execute the work; the graph preserves what the work means.
