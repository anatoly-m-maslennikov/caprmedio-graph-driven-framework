# CA-P-1958 — independent candidate-presentation acceptance

Outcome: **PASS** for the saved CA-P-1908 candidate presentation produced by CA-P-1957. This accepts presentation fidelity, pins, reproduction and bounded persistence guards. It is not Operator approval, semantic/native admission, ontology adoption, deletion, Subject migration or an execution Run.

Verified on 2026-10-10. Required start prerequisite CA-P-1957 was independently located by exact Atom ID, confirmed Done, and its current bytes match the Done Carrier at commit `4b0468fab5b46e293ed4a9698b76fe47ad223c9b`. All three saved presentation artifacts also match that commit byte-for-byte.

## Frozen package

| Artifact | SHA-256 |
| --- | --- |
| `candidate.entities.indented.txt` | `f32588f6f9bc97e2180578c051bfbc73f39a7e80b7273bdf6702f9309778ed56` |
| `candidate.review.md` | `8b0d9c9ff3f940f3bfb4456aabda7b808060424a9910a194ff85a50073bcf975` |
| `candidate.manifest.json` | `fb9deec859a5f828e648d94da9d7888c50175872a70b9711e6a9f6a734ec81ce` |
| Renderer, `support/render_candidate.py` | `3b18039bbfe8292d012b1944d3567d055ae9874dfb64e457fbad15716ede4260` |
| Independent verifier, `support/verify_candidate_presentation.py` | `56e3805fe95cfb2af911362e2f3d3808bf5fb40d53d3eab49995adfb577c9767` |

The candidate JSON file remains the accepted `../nodes/candidate.structure.marked.json`, file SHA-256 `04f2b8d3606ac30b74850ab9ff53ebebfcbcffd1cda1e5ad2d948662c085e34b`. Its independently recomputed UTF-8 sorted compact JSON hash, without a trailing newline, is separately recorded as `0b26e7571ab4897f85e2b521255feb9f83e33c4f48ce86f02fd0a8f80c9303b1`. A canonical-value hash is not mislabeled as a file-byte hash.

## Coverage and readable candidate meaning

- Independently parsed the primary display inventory, including its two-space parent stack, labels, original-identity annotations and marks. All **706 original identities appear exactly once**, with the exact accepted display path; every extra prefix is explicitly presentation support. No new model identity is minted.
- Bucket membership—not just totals—matches the accepted design exactly: **17 Continuant, three Occurrent, four non-temporal broad anchors and 682 explicitly unclassified identities**. No additional temporal member or default parent is inferred. The 359 rendered top-level labels are a display calculation, not an ontology-root count; the original 346 literal syntactic roots and 293 standalone roots remain distinct accounting.
- The **584 retain, three consolidate, two generalize and 117 question** marks match the accepted review. Every question still has its specific question and null semantic proposal in the linked disposition ledger. Both unresolved potential-drop annotations remain visible as questions and preserve their identities.
- All **123 blocked legacy chains** carry the exact `LEGACY RELATION UNRESOLVED` label. The legend limits operator interpretation to separately evidenced display decisions and explicitly states that retaining an identity does not approve its relation. Legacy syntax is not silently promoted to taxonomy or bearer qualification.
- All five reviewer proposals show their actual target, original basis and complete preserved risk: Applicable Methodology → Projection; Artifact/Revision, Atom/Revision and Journal/Revision → the proposed Revision display family; Claim → Substance. These are candidate targets, not applied replacements. Exact distinctions, effects, source evidence and questions remain available through the pinned ledgers.
- All **seven inherited constraint bullets** reproduce their exact `applies_when` condition and rule. Conditional context such as a Carrier Format or File Extension change is therefore visible before “That change alone”. No concrete Carrier inheritance, actual binding, default-copy rule or universal IS_BORNE_BY fact is inferred.
- All **ten Term proposals** retain separate Terms ownership and nonadmission. Human `/` order is broader parent then narrower child; the explicit canonical label is `NARROWER_THAN`, child → parent. No inverse or Entity-graph edge is created by the presentation.

## Pins, prerequisites and shared views

All nine accepted inputs match both their fixed SHA-256 values and immutable blobs at receipt commit `94776a14a368827a758534eb9c5c0109d649f309`: node dispositions, marked relation ledger, marked candidate structure, structure design, RMED JSON, snapshot context, Substance direction, Scope-omission direction and CA-P-1938 acceptance. The renderer rejects a changed digest for each of those nine inputs. Both linked RMED text views match their manifest descriptors and the accepted receipt-commit bytes.

The manifest's Plan pins were independently resolved to actual Git blobs and compared with current Done Carrier bytes, Version and identity:

| Plan | Version | Actual Plan Carrier SHA-256 |
| --- | ---: | --- |
| CA-P-1907 | 14 | `9ac74a857d8356db6e4a0f68890ca8e19babb6b3644a5f831fb681515046eedf` |
| CA-P-1938 | 3 | `b2bb487194a14212560e109a4c763d4f107611f033c7c7151335c534d50fa022` |

CA-P-1938's derived acceptance-record SHA-256 is separately `c2576865efcd2cfcc10a7075ad546b1c2d288cdae9f285eeaeb61f858bbf2e9b`; it is not used as the Plan Carrier hash. Current locations may move normally; the manifest's receipt commit remains its stable locator basis.

Both RMED tree links and the machine-readable shared view resolve. GOVERNS and DEPENDS_ON remain separate. M/E/D links remain pointer-derived associations, not proven applicability; no empty slot is invented. The 805 GOVERNS and 2,844 DEPENDS_ON counts are unchanged. The presentation links these views rather than duplicating their Claim authority as new Entity nodes.

The latest separately pinned Substance Scope direction requires the full governed Subject **AND** full owning Scope Unit for omission; otherwise Scope stays explicit. Applicability is not ownership. Substance, role labels and optional general Details are candidate presentation direction, not retroactive Core evidence or schema/authoring migration. Existing role/type requirements remain in the unchanged accepted source model.

## Reproduction and isolated guards

The final verifier passed from the repository root:

```text
UV_CACHE_DIR=.caprmedio_tmp/cache/uv uv run --offline --no-project --no-env-file --python 3.14 python -B .caprmedio_caprmedio/_projection/core-entity-review/presentation/support/verify_candidate_presentation.py
```

It freshly reproduces all three output byte strings and verifies their saved bytes. Both the renderer's default dry-run and `--verify-output` paths passed with output-writing methods forbidden. Manifest output hashes and byte lengths independently match the actual inventory and review.

Sixteen isolated scratch guard cases passed: late mismatch before any creation; exclusive creation of absent files; identical existing files without rewrite; missing verification output; dangling and existing output symlinks; directory output; output-name escape; exclusive-creation race with prior-created-file rollback and competitor bytes preserved; default dry-run without creation; mutually exclusive modes; symlinks at all four lexical ancestors inside the repository route; and a symlinked repository root. The temporary fixtures were automatically cleaned. Production persistence was never invoked.

All 18 protected accepted input, output, producer and prerequisite files watched by verification were unchanged. Only this acceptance record and the assigned independent verifier were created in the presentation scope.

## Explicit limits and handoff

This is exhaustive QA of the saved presentation against the accepted inputs, not a fresh semantic review of 706 identities, an ontology-equivalence proof or another 951-source audit. CA-P-1938's historical source/meaning acceptance remains a pinned input. The captured context remains commit `a971d0e00c33c779f485fc8cad63194894d440fb`; no live Core bytes were read or rebound. The guard tests do not establish crash/power-loss transactionality or comprehensive hostile concurrent-filesystem security.

No candidate artifacts, accepted sources, Core, Subjects, baseline, history, native graph, Plans, Git, MCP, FPF or runtime state were edited by this verification. Candidate review is now ready for the separate CA-P-1909 Operator decision gate. This PASS does not answer the 117 questions, apply the five proposals or authorize a later migration.
