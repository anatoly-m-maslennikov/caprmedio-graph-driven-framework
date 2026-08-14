---
artifact_type: implementation_decision
artifact_id: CAPRMADIO-DECISION-GOV-018
scope_path: layer:gov
subject_scopes:
  - carrier-format
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: resolution_of
    targets:
      - CAPRMADIO-CONFLICT-GOV-001
  - type: replacement_of
    targets:
      - CAPRMADIO-DECISION-GOV-003
      - CAPRMADIO-DECISION-GOV-016
      - CAPRMADIO-DECISION-GOV-017
---

# Decision — Preserve immutable semantics through TOML carrier migration

An emitted atomic artifact keeps an immutable semantic identity and record:
its stable IDs, Type and subtype, claim or QA definition, authority, acceptance
state, scope, provenance, rationale, relations, and Markdown body content do not
change. Carrier bytes and filename extensions are representation, not semantic
identity.

An explicit operator-authorized representation migration may change those
bytes only when one deterministic transaction:

- parses the old carrier and the proposed TOML carrier into the same normalized
  semantic value, including explicit reconstruction of YAML nulls;
- records old and new paths, whole-file digests, normalized-semantic digests,
  carrier IDs, governing Decision, timestamp, source Git blob return address,
  declared loss, and LLM session IDs in
  `dset/scopes/gov/migrations/carrier-transitions.toml`;
- updates atom seals, legacy selector seals, artifact classification, retained
  links, generated views, and the bootstrap bundle in the same validated
  transaction;
- rejects missing inputs, collisions, unsupported values, semantic drift,
  partial resealing, stale evidence, or rollback mismatch; and
- becomes a no-op after the committed cutover.

Markdown artifacts keep their paths and bodies while YAML frontmatter becomes
TOML frontmatter. A historical standalone YAML file moves to an adjacent
`<stem>.legacy.toml` envelope because its sibling `<stem>.toml` already owns
current truth. The envelope records the original path and digest and stores a
lossless TOML payload plus explicit null paths. Readers never treat the
historical envelope as current authority.

After cutover, `dset/` contains no `.yaml` or `.yml` artifact carriers and no
Markdown YAML frontmatter. Standards-compliant JSON Schema, GitHub Actions,
host skill metadata, ecosystem manifests, wire formats, and runtime journals
retain externally prescribed formats because they are not CAPRMADIO-owned artifact
encodings.

This Decision fully replaces `CAPRMADIO-DECISION-GOV-003`,
`CAPRMADIO-DECISION-GOV-016`, and `CAPRMADIO-DECISION-GOV-017`. It carries forward the
still-applicable semantic immutability, append-only lifecycle, explicit and
acyclic replacement/absorption, role-before-priority conflict classification,
universal-priority, retirement, and stable-lookup consequences. Their current
independent owners—especially `CAPRMADIO-DECISION-GOV-010` and
`CAPRMADIO-REQUIREMENT-GOV-020..026`—remain active. Only permanent byte identity and
retained YAML are withdrawn; historical package and structured data remain
preserved through TOML envelopes and the transition ledger.

This emitted Decision atom is immutable. Later correction requires a successor
Decision and append-only lifecycle event.

## Primary claim

Atomic semantics and identity are immutable, but an explicitly authorized lossless carrier migration may convert every CAPRMADIO-owned YAML artifact carrier to TOML under one transactional old-to-new digest ledger.

## Rationale

Carrier encoding is not the project claim itself; preserving semantic values, stable IDs, provenance, relations, body content, and a verifiable transition map retains history without keeping YAML in the current repository.
