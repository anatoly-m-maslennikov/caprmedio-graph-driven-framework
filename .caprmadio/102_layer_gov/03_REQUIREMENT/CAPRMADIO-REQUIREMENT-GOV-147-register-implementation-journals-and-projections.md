---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-147
scope_path: layer:gov
subject_scopes:
  - provenance
tier: standard
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-113
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-116
      - CAPRMADIO-REQUIREMENT-GOV-133
      - CAPRMADIO-REQUIREMENT-GOV-144
      - CAPRMADIO-REQUIREMENT-GOV-145
      - CAPRMADIO-REQUIREMENT-GOV-146
---

# Requirement — Register Implementation Journals and derived Projections

GOV registers `implementation_journal` as an internal Journal Type with the semantic coordinate `journal × implementation × internal` and the four-character identity prefix `IJRN`.

Every structural scope that realizes Requirement, Method, Assurance, or Delivery Atoms owns one logical Implementation Journal under its `07_IMPLEMENTATION/` role folder. The Journal uses append-only NDJSON and may rotate into ordered carrier segments without changing its logical identity or rewriting admitted records.

Each record identifies:

- its stable record identity, sequence position, and recording time;
- whether it establishes, replaces or corrects, or removes an implementation binding;
- every source Atom by `artifact_id` and exact carrier-content digest;
- every native implementation target by target kind, stable repository-relative locator, and content digest;
- the earlier record it replaces, corrects, or removes when applicable; and
- available Git commit, pull request, author, signer, and LLM-session provenance without requiring those values to remain the binding's semantic identity.

A record may bind Requirement, Method, Assurance, and Delivery sources together when one bounded implementation change realizes them in one structural scope. It must not claim that the targets pass their Assurance criteria, were successfully delivered, or produced an observed result.

The effective implementation frontier is derived by replaying the complete ordered Journal. A deterministic CAPRMADIO tool regenerates Implementation-role Catalog, Map, Hub, coverage, and dashboard Projections from that frontier plus the declared current Atom and native-target frontier. Each generated Projection records the exact Journal frontier it consumed and is replaced by regeneration rather than direct semantic editing.

The Projections may show implemented, missing, removed, and potentially stale relationships, scope summaries, coverage counts, and navigation to native targets. They do not replace the Journal, normative Atoms, native implementation, Ops evidence, or Verification.

## Primary claim

Each implementing scope records exact normative-Atom-to-native-target bindings in one append-only Implementation Journal and regenerates non-authoritative implementation coverage and navigation Projections from its effective Journal frontier.

## Rationale

One scoped Journal preserves implementation lineage across squash merges and other Git graph transformations, while deterministic Projections provide fast current views without becoming another writable traceability authority.
