# CA-P-1922 — independent design acceptance

Outcome: PASS for the source-pinned, non-authoritative CA-P-1921 ledger and candidate design. This accepts the integration and preservation checks, not adoption, native semantic admission, source migration, a complete ontology, or an execution Run.

## Frozen outputs and prerequisite

| Checked input | SHA-256 |
| --- | --- |
| `relations.ledger.json` | `6ec53f14e64280815e5f57f8d00598913bc26b342102ca3acce5a7f4221d10bd` |
| `candidate.structure.json` | `eda055c887706454cfd2d52bee7196a818e8eb0b8e1710d587fcfc4ffa8d9071` |
| `support/build_relation_ledger_ca_p_1921.py` | `e61da9e7889a19fc384ceb7af411ed35784127c86a92a5648b89bc41f9273b0c` |
| Baseline inventory file | `bc5d99e91fb7dd4dcb42e59ff33cc24cff1d0901c5904764394c769aaa0a9430` |
| Baseline canonical inventory | `23394abaf6e9c18a585cf3146aedd0a80df166c9dd82be6e86ed7c3c56780bdc` |
| Current Core frontier | `7792e842cfe6c66320745660e69cd0df5525ec18bb22b5c060a6ddfff5fc97f7` |

Required start prerequisite CA-P-1921 was located independently by exact Atom ID, not a frozen path: current unarchived Carrier is under `done/09-CA-P-1921-TASK--integrate-the-source-pinned-core-relation-ledger.md`, Version 2, Status Done, SHA-256 `157e0d0454c35086d1ce59c61c9dcf9f817d8a10cc39641fdce0c5e9d12844d9`.

All nine frozen prerequisite IDs were also located by exact ID and their current bytes, Version and Done status matched the ledger: CA-P-1905, CA-P-1913, CA-P-1914, CA-P-1915, CA-P-1916, CA-P-1917, CA-P-1918, CA-P-1919 and CA-P-1920. Batch 6 child completion pins CA-P-1923 through CA-P-1926 remain current. Carrier movement is not treated as an identity change.

## Independent checks

- All 294 case rows are an exact join of the six reviewed batches, including all endpoints, fields, evidence, reasons and questions. Batch 6 is exactly its 16 checkpoint cases plus four children containing 13, 12, 12 and 12 cases. There are 247 not-native and 47 unresolved dispositions; sub-90 confidence stays unresolved and its question is retained.
- All 706 original node records, 4,534 original occurrences and 3,093 original segment records are preserved exactly. The segments comprise 2,275 slash and 818 colon occurrences. Every slash pair has exactly one case review. Original source roles, qualified paths, list positions, line coordinates, contribution hashes and segment IDs remain intact.
- All 951 source pins (908 selected and 43 excluded), Project Structure and the baseline producer profile's five component hashes are current. The integration producer freshly reconstructs the registered Core frontier, exact owned-Active selection and source collection. Original Subjects contributions were rechecked using their original-EOL raw spans. There were 317 exact current Main Content evidence checks across case reviews and the structure catalogue.
- Independently recomputed every complete qualification chain. All 236 display-only rebases require evidence, confidence at least 90 and a non-unresolved display decision for every slash segment in that exact chain. All 123 blocked chains retain the original identity; 347 identities are unchanged. All 706 display paths remain distinct; no collisions, alias merges or canonical identity rewrites occur.
- Zero native slash proposals and zero native edges from display rewrites. Source Atom provenance is separate from model identity. No derived inverse is promoted to another native fact. Colon segments retain syntax only: neither assignment nor native allowed-value admission is inferred.
- The ten additional NARROWER_THAN proposals remain separate Terms Graph, narrower-to-broader proposals with new Main Content synthesis provenance, not fabricated old Subject occurrences or Entity edges. The seven common constraints retain their conditions and explicitly prohibit concrete Carrier inheritance.
- Structure fields are copied without alteration: 17 Continuant and three Occurrent display memberships; 24 assessed and 682 unreviewed identities, with 326 unreviewed syntactic roots. The six confirmed memberships distinguish the Operator's display decision from Core proof; only three specifically evidenced subtype derivations follow the three direct confirmations. No blanket subtype or native temporal rule is introduced. Session remains an unassessed example; no ephemeral-to-Occurrent or Journal-only storage rule is adopted. No reduced native ontology-root count is claimed.

## Both RMED views

Independent reconstruction from the baseline Subjects matches both role-centered and Entity-centered pointer views exactly: 805 GOVERNS and 2,844 DEPENDS_ON pointers, 580 literal targets and 805 shared source records. The excluded Operations pointers (102 GOVERNS and 782 DEPENDS_ON) and Concern pointer (one GOVERNS) complete the original 4,534 occurrences. Operations is not M; DEPENDS_ON is not a governing Claim. Nonempty M/E/D links remain associated pointers, not established applicability. Prefix indentation is presentation, not model hierarchy or native relation admission.

All four saved RMED renderings—`rmed.views.json`, `rmed.views.md`, `rmed.roles.indented.txt` and `rmed.entities.indented.txt`—reproduce byte-for-byte in memory. Every filesystem write from the original producer was intercepted; no output was rewritten.

Portability caveat: older files in `support/` are archived producer-source copies, not declared installed portable Tools. The RMED helper's legacy location-relative `main()` is reproduced from its original source location, `.caprmedio_tmp/planning/core-entity-review/design/build_rmed_views_ca_p_1920.py`, with writes intercepted. Its exact archived copy is `support/build_rmed_views_ca_p_1920.py`; both have SHA-256 `8d3f12653075ccfe6710d983dd206c8ff6ddf22920f3dcb0fdd2e4af33fbc75f`. This acceptance does not claim that every archived helper is directly executable after relocation.

## Reproduction and boundary

Both checks passed from the repository root, without `--persist` or YAML tooling:

```text
UV_CACHE_DIR=.caprmedio_tmp/cache/uv uv run --offline --no-project --no-env-file --python 3.14 python -B .caprmedio_caprmedio/_projection/core-entity-review/design/support/build_relation_ledger_ca_p_1921.py --verify-output
UV_CACHE_DIR=.caprmedio_tmp/cache/uv uv run --offline --no-project --no-env-file --python 3.14 python -B .caprmedio_tmp/planning/core-entity-review/design/verify_1922_acceptance.py
```

The first check freshly reproduces all four durable/temporary ledger and candidate copies at the frozen hashes. The second is an independent verifier; SHA-256 `777887295922f11c6784c180031f36a521d6f1b2006fc28b742b1ce44ce0c301`.

The newer Operator direction to use Substance for generic primary content and SubstanceScope for applicability postdates these pinned inputs. It is not retrofitted into Core quotes, identities or approval evidence here; that candidate direction remains separate work. The 47 unresolved relation cases and 682 unreviewed whole-node dispositions remain visible and are not silently decided by this PASS.

Reviewed source, baseline, design and prerequisite bytes were unchanged during verification. Only this acceptance record and the independent temporary verifier were created. No Core Atoms, Subjects, Plans, history, Git, MCP, FPF or runtime state were changed. This record is derived review evidence, not source authority or a lifecycle receipt.
