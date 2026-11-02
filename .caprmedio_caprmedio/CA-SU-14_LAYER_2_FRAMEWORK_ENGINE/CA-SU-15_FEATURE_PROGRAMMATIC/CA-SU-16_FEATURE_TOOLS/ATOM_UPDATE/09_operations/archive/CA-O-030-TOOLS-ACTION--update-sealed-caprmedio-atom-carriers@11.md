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
version: 11
updated_at: "2026-10-12 05:39:01 +0400"
relations: {}
---
# Summary

Update sealed CAPRMEDIO Atom carriers

## Operation

Update Sealed Atom Carriers **means** the reusable Action that applies the admitted same-identity changes **to** **every** Atom **in** an exact selected set as **`=1`** all-or-nothing transaction. Subject-only preview selects one ordinary Profile for both source and result syntax and seals its grammar evidence. Default local preview remains mutation-free; opt-in staging writes only derived temporary candidates without changing authoritative sources. the modeled boundary is the approved change set: partial application does **not** fulfill its operational contribution.

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
5. on explicitly authorized apply, recheck **every** frozen source **and** destination precondition. persist the exact prior semantic Revisions **where** the admitted class creates a new Revision **and** publish **all** selected current Carriers within the same all-or-nothing boundary. an archive collision **or** changed source blocks apply **without** overwriting evidence.
6. verify the published set's admitted class-specific Version/time results **and** its exact prior history. **if** publication **or** post-write validation fails, restore **every** mutable Carrier **to** its before-state, including **any** newly created archive destinations; preserve pre-existing historical Carriers, unrelated targets, **and** accepted Journal Records.

### Outcome

successful apply requires **every** selected admitted change's class-specific result with identity, Summary, placement, **and** required history preserved; **not** every generic edit advances Version. A non-no-op Subject-only change is instead always the stated `semantic_revision` and advances Version by one. a mutation-free preview is prepared, a no-op is not an invented Revision, **and** deferred/not-applied **or** rejected is not applied. stop before effects on an invalid target **or** failed precondition. report actual applied, failed/partial/unknown-effect **and** recovery outcomes with their evidence; incomplete **or** unverified restoration is **not** a successful update **or** rollback. shared Run receipt failure preserves the performed result **and** visible recording blocker, **not** authority to repeat the update.

### Subject-only preview

Subject-only preview **must** select a complete original Atom Carrier with a stable Atom ID, excluding Draft and archived carriers by both carried Status and placement. Both the pinned source and proposed result **must** pass existing complete-carrier validation, including the applicable Content Role/Type Status model and correct Carrier placement. Preserve the carried Status byte-for-byte; do not activate the source or perform a lifecycle transition. Missing, ambiguous, unsupported, or stale validation authority **must** fail closed.

1. accept only the closed root envelope `{atoms, subject_profile?}` for this mode. `subject_profile` omitted selects `legacy`; `approved` is explicit; unknown or malformed supplied Profiles fail. `atoms` is non-empty and has no repeated selected file. Every Atom item has one safe repository-relative `selector`, one `expected` object with exactly `atom_id`, `version`, and `sha256`, and an ordered `subject_patches` list. The list may be empty only for a truthful no-op, which still validates the selected pinned source and complete Carrier. Every patch has exactly `field`, `old`, and `new`; it has a zero-based `index` exactly when `field` is `depends_on`. `field` is `governs` or `depends_on`. Reject every other root or item key.
2. resolve every selector only as a safe repository-relative regular file. reject an absolute or escaping path, symlink, missing Carrier, invalid or ineligible original Carrier, duplicate identity, stale expected Atom ID/Version/SHA-256, malformed or nested `subjects`, a repeated patch occurrence, mismatched `old` value, invalid value, or duplicate resulting `depends_on` value. Validate each source and resulting Subject under the one selected Profile. `legacy` rejects every `atom(...)` selector; `approved` accepts only the exact initial lowercase selector forms registered by CA-R-1321, preserving `Atom`/`atom` case distinction and rejecting every other selector construction, escaping, conjunction, wildcard, evaluation, alias, nesting, later-position selector, and `@`. These syntax checks do not enumerate Atom rows or create a carrier or display operator; D governs `@<version>` archive filenames as carrier storage, not as an Entity token. `legacy` keeps `/` bearer qualification, `:` allowed values, and literal dots, while `approved` uses `/` broader-to-narrower, `.` bearer-to-dependent, and `:` Property-to-allowed-value. Do not infer a relation, semantic conformance, or cross-Profile conversion.
3. reject an Atom item that also carries complete frontmatter or body replacement. apply the explicit patches only to the named flat Subject scalar spans; preserve every other frontmatter byte, all body bytes, line endings, filename, path, identity, Summary, Status, Relations, and unrelated metadata byte-for-byte.
4. validate the complete resulting Carrier. produce a mutation-free preview with exact before and proposed source pins, ordered patch findings, a byte-preservation result, selected `subject_profile`, and `subject_profile_evidence` with exactly the `grammar_pins` for `legacy`'s five exact historical definitions adopted before CA-P-2059 or `approved`'s five current definitions, plus `native_admission: "not_performed"`; seal all of those fields in the preview digest. The grammar evidence is neither a native endpoint registry nor an attestation about source semantic conformance. Retain the required actual-effect rule: a non-no-op Subject change is a `semantic_revision` with Version `N+1` and Updated At set at the real effect time. The default preview materializes that illustrative Updated At only in its in-memory proposed Carrier; it neither archives a prior Carrier nor writes a Carrier or Journal Record, and it does not claim an executed effect. Opt-in staging may export those same derived bytes only under CA-D-425.
5. do not infer ontology, relation meaning, replacement mapping, grammar cutover, migration batch, Profile migration, native endpoint admission, or approval. This Subject-only local mode is preview-only. An actual effect remains subject to the existing sealed Project-local MCP delegation, exact authorized preview, source recheck, history, and Journal guards; unsupported MCP is not used.

### Opt-in local staged preview

The local wrapper may accept `run --stage-preview` only with the unchanged closed Subject-only payload, rejecting generic input and `--apply` before staging. Reuse the existing illustrative preview and pure planner; create only a fresh generated temporary batch under CA-D-425's numbered-filename layout, preserving each source filename. No authoritative source, history, Journal, promotion or MCP effect is authorized.

Read back exact candidate bytes and hashes, validate each complete Carrier using its ORIGINAL logical source path and applicable Status/placement, and finally recheck source pins/current identity uniqueness/grammar with the same illustrative time and original preview/intent hashes. Source drift refuses success rather than refresh. Only complete success produces CA-D-425's separate closed manifest and explicit staging-only/illustrative/sources-unchanged result evidence. Failure reports retained partial artifacts without a success seal or unsafe cleanup. Candidate Version/time are illustrative and no-op metadata are unchanged; this point-in-time evidence grants no apply permission.

### Admitted one-target Subject application

CA-D-531's closed Subject parameter variant extends the existing `update_atom` MCP route only. It does not execute the local preview envelope, add a transport or bypass CA-D-527's exact preview/Operator authorization. Select exactly one complete eligible non-archived original, preserving its intended Status and current Delivery placement. Reuse CA-M-371's pure planner and require the caller's `subject_intent_sha256` to match freshly derived CA-D-425 intent. Reject a delivered/projection copy, owner/path mismatch, duplicate non-archived original, malformed or unsafe competing identity claim, archive collision, changed snapshot or pin, mixed generic fields, or unsupported validation authority before effects.

Derive the complete assessment proposal from the exact source by replacing only Subjects, leaving old Version/time. For a value change, obtain the existing current Done Analysis Report evidence and completed CA-O-145/CA-O-067 result; verify unchanged Summary/primary-Claim identity, declared delta and completed lineage review under CA-R-1892 and CA-D-585. Consume that exact result again at CA-O-129. An uncertain, replacement-required, different-class or stale result stops this update; no new classifier or caller Boolean substitutes for it.

Before native publication, require the actual selected execution session, the exact admitted CA-D-527 execute envelope and its current permission/definition bindings, the actual canonically recorded CA-O-030 Action start, and durable admission of the exact prior Carrier observation. Reopen source, grammar, report, validation authority, assessment and destination evidence. An unsupported or retained/recovered invocation cannot start another effect.

For a non-no-op, preserve the exact `N` predecessor at the existing history path as `predecessorArchive`, classified archived by placement, with identical bytes and no second Version, Status or Updated At edit. In the same bounded transaction publish the current Carrier from the byte-span plan with exactly `N+1` and one actual Project-time Updated At. Only declared Subject, Version and Updated At spans may change; preserve file modes and every unrelated byte. Validate and independently read back both current/history outputs, then bind the actual Version/time/hash and exact effect descriptors to `subject_intent_sha256` in the native result.

On publication or postcondition failure, restore exact current before-bytes/mode and remove only verified attempt-owned history; preserve pre-existing history, unrelated files and accepted Journal events. Report verified restoration as a failed attempt, and incomplete or unverifiable restoration as partial/unknown with retained evidence. Shared current-state/change and Run recording must confirm the actual effects and Atom identity through safe result/effect references, without copying Atom contents into Journal or inventing events. A recording blocker preserves performed effects and retries only recording; it never replays publication. A no-op validates the exact source/intent, creates no Carrier/history/change effect and retains only its truthful Run evidence.

### Run recording

Bind each actual standalone **or** nested Action Run **to** the shared every-Run contract in CA-P-1117 v3, Done CA-P-1443 J01–J08, independently reviewed by CA-P-1451: exact admitted definition Revision, actual Run identity/lineage, safe input/result/effect references, start, truthful terminal **or** still-pending interruption, **and** durable canonical Journal receipts under CA-R-1720. Workflow-contained bindings also follow CA-R-1525; standalone coverage is the selected Epic obligation, **not** a broadened applicability claim for that Requirement. Reuse the shared recording capability **without** owning another Journal implementation. Preserve accepted events **and** pending evidence; retry failed recording with the same Event identity/payload, **not** the performed Action. No receipt, intake acknowledgment, **or** Git Commit alone proves successful effects **or** complete Run recording.
