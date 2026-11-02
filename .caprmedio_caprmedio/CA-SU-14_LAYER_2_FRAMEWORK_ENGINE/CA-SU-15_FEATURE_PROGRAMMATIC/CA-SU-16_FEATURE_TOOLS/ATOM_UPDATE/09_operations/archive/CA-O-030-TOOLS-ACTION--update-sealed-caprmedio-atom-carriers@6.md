---
atom_id: CA-O-030
content_role: Operations
type: Action
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Update Sealed Atom Carriers"
  depends_on:
    - "Action"
    - "Tool/ATOM_UPDATE"
    - "Atom"
    - "Atom/Revision"
    - "Atom/Summary"
    - "Atom/Revision/Updated At"
    - "Artifact/Carrier"
    - "Journal/Record"
version: 6
updated_at: "2026-10-10 23:57:31 +0400"
relations: {}
---
# Summary

Update sealed CAPRMEDIO Atom carriers

## Operation

Update Sealed Atom Carriers **means** the reusable Action that applies the admitted same-identity changes **to** **every** Atom **in** an exact selected set as **`=1`** all-or-nothing transaction. the modeled boundary is the approved change set: partial application does **not** fulfill its operational contribution.

## Details

### Applicable conditions

- select **`=1`** Atom **or** a frozen bulk set of **`>=2`** Atoms by exact Carrier evidence. an unassigned Draft has no invented Atom ID; retain its exact locator **and** Version evidence.
- preserve identity, Summary, path, **and** filename. under CA-R-1464, a requested Summary change needs a new Atom **and** new Atom ID; this same-identity Action **must not** perform it as an update.
- apply **only** through authorized Project-local MCP delegation with a sealed Initiative action envelope. default **to** mutation-free preview.

### Steps

1. resolve **every** target uniquely. reject repeated, missing, ambiguous, **or** stale selections; seal path, filename, assigned ID **when** present, Version, Updated At, **and** digest as preconditions.
2. prepare the requested frontmatter, body, **or** combined change **in** memory. preserve the immutable Summary **and** identity **and** reject an attempt **to** change them through this Action.
3. validate **every** complete resulting Carrier, including required metadata **and** direct Relations. reuse CA-O-067's assessment against the exact proposal/target **and** admit **`=1`** class under CA-R-1432: `carrier_only` **and** equivalent `refinement` retain ID **and** Version; `semantic_revision` retains ID **and** uses the next Version under CA-R-1415 with the exact previous semantic Revision preserved under CA-R-1371. `replacement`, including **any** Summary-value change, leaves this Action for the caller's separately authorized replacement route; uncertain classification blocks apply. refresh Updated At **to** the actual edit instant for **every** accepted Carrier edit under CA-R-1788, including formatting; no edit/no-op creates no fictitious Version, timestamp edit, **or** mutation.
4. freeze the complete target map, required historical Carriers, expected Revisions, **and** digests. expose the exact mutation-free dry-run diff **before** apply.
5. on explicit authorized `--apply`, recheck **every** frozen source **and** destination precondition. persist the exact prior semantic Revisions **where** the admitted class creates a new Revision **and** publish **all** selected current Carriers within the same all-or-nothing boundary. an archive collision **or** changed source blocks apply **without** overwriting evidence.
6. verify the published set's admitted class-specific Version/time results **and** its exact prior history. **if** publication **or** post-write validation fails, restore **every** mutable Carrier **to** its before-state, including **any** newly created archive destinations; preserve pre-existing historical Carriers, unrelated targets, **and** accepted Journal Records.

### Outcome

successful apply requires **every** selected admitted change's class-specific result with identity, Summary, placement, **and** required history preserved; **not** every generic edit advances Version. A non-no-op Subject-only change is instead always the stated `semantic_revision` and advances Version by one. a mutation-free preview is prepared, a no-op is not an invented Revision, **and** deferred/not-applied **or** rejected is not applied. stop before effects on an invalid target **or** failed precondition. report actual applied, failed/partial/unknown-effect **and** recovery outcomes with their evidence; incomplete **or** unverified restoration is **not** a successful update **or** rollback. shared Run receipt failure preserves the performed result **and** visible recording blocker, **not** authority to repeat the update.

### Subject-only preview

1. accept only `{atoms: [{selector, expected: {atom_id, version, sha256}, subject_patches}]}` for this mode. `atoms` is non-empty and has no repeated selected file. Every Atom item has one safe repository-relative `selector`, one `expected` object with exactly `atom_id`, `version`, and `sha256`, and a non-empty ordered `subject_patches` list. Every patch has exactly `field`, `old`, and `new`; it has a zero-based `index` exactly when `field` is `depends_on`. `field` is `governs` or `depends_on`.
2. resolve every selector only as a safe repository-relative regular file. reject an absolute or escaping path, symlink, missing Carrier, invalid active Carrier, duplicate identity, stale expected Atom ID/Version/SHA-256, malformed or nested `subjects`, a repeated patch occurrence, mismatched `old` value, invalid value, or duplicate resulting `depends_on` value.
3. reject an Atom item that also carries complete frontmatter or body replacement. apply the explicit patches only to the named flat Subject scalar spans; preserve every other frontmatter byte, all body bytes, line endings, filename, path, identity, Summary, Status, Relations, and unrelated metadata byte-for-byte.
4. validate the complete resulting Carrier. produce a mutation-free preview with exact before and proposed source pins, ordered patch findings, a byte-preservation result, and the required actual-effect rule: a non-no-op Subject change is a `semantic_revision` with Version `N+1` and Updated At set at the real effect time. Preview does not materialize an illustrative timestamp, archive a prior Carrier, write a Journal Record, or claim an executed effect.
5. do not infer ontology, relation meaning, replacement mapping, grammar cutover, migration batch, or approval. This Subject-only local mode is preview-only. An actual effect remains subject to the existing sealed Project-local MCP delegation, exact authorized preview, source recheck, history, and Journal guards; unsupported MCP is not used.

### Run recording

Bind each actual standalone **or** nested Action Run **to** the shared every-Run contract in CA-P-1117 v3, Done CA-P-1443 J01–J08, independently reviewed by CA-P-1451: exact admitted definition Revision, actual Run identity/lineage, safe input/result/effect references, start, truthful terminal **or** still-pending interruption, **and** durable canonical Journal receipts under CA-R-1720. Workflow-contained bindings also follow CA-R-1525; standalone coverage is the selected Epic obligation, **not** a broadened applicability claim for that Requirement. Reuse the shared recording capability **without** owning another Journal implementation. Preserve accepted events **and** pending evidence; retry failed recording with the same Event identity/payload, **not** the performed Action. No receipt, intake acknowledgment, **or** Git Commit alone proves successful effects **or** complete Run recording.
