# Subject file operations — CA-P-1960 compiled contract

Derived from the accepted twelve-carrier tool-rmedo.packet.json (SHA-256 928074c3b7bb67d60a3c302681c7fbd687e88a7df48babcf5046f9be949769d7) and tool-rmedo.acceptance.md. This compiles their current source-pinned contract; it is not another authority. Recorded 2026-10-11 00:12:22 +0400.

## Boundary

Use existing ATOM_SEARCH/ATOM_UPDATE wrappers, configured Project root, safe path/selector handling, YAML parser, complete-carrier validation and apply guard. Reusable Tools operate correct files only. Repairs, migration decisions/application, actual effect-time materialization, Git history and Journal effects belong to separately approved ad-hoc scripts. No MCP adapter, repair engine, grammar adoption or source write is introduced. Invalid files are diagnosed/rejected, never repaired.

## Lookup

One --subject VALUE selects Subject mode. Add --subject-field governs|depends_on|both (default both), --subject-match exact|prefix (default exact), repeatable --content-role ROLE (OR within roles) and --scope-unit OWNER. Subject mode defaults to Active originals; generic search retains its existing default. Existing --under, --atom, --query, --limit and explicit lifecycle filters remain conjunctive with the Subject criterion. Reject unsupported requests, unknown owner/role and escaping/symlink paths before traversal.

The Step-1 caller selects the declared Core authoring subtree, owner CORE_META_MODEL and exactly Requirement/Method/Evaluation/Delivery/Operations. This is caller selection, not a hardcoded Tool Core root. Exclude Projections and non-Atoms. Diagnose invalid selected files, owner/path disagreement and conflicting original identities, not silent omissions.

Read flat structured governs (one scalar) and optional depends_on (unique scalar list; absent means empty). Exact is literal equality; prefix is equality or query followed by current / or : boundary. Artifact/Atomology is not an Artifact/Atom match. No ontology meaning or dot grammar is inferred.

Return source_root, count, occurrences and diagnostics. Each occurrence has atom_id, version, status, owner/current_scope_unit, relative_path, sha256, updated_at, field, index and value. Index is null for governs and zero-based for dependencies. Order by relative path/field/index. Count means occurrences. Mark limited or diagnostic-restricted coverage truthfully.

## Subject-only preview

Use existing update input with an exclusive new mode:

    {"atoms":[{"selector":".caprmedio_caprmedio/.../CA-R-123-...md",
      "expected":{"atom_id":"CA-R-123","version":1,"sha256":"<exact hash>"},
      "subject_patches":[{"field":"governs","old":"Atom/Status","new":"Atom/State"}]}]}

Selector is the exact repository-relative source file, not an ID/filename alias. Expected contains exactly atom_id/version/sha256. Patches contain field, exact old and explicit new; depends_on additionally requires a zero-based integer index, governs has no index. Reject duplicate file/occurrence targets and mixing Subjects with full frontmatter/body replacement. No mapping or field move is inferred. Empty/unchanged proposals are no-ops, not revisions.

Reject stale ID/Version/hash/old values, malformed/nested Subjects, invalid fields/indexes, ambiguous/overlapping spans, resulting duplicate dependencies, path escapes and symlinks. Patch exact scalar spans. Preserve every unrelated UTF-8 byte and line ending. Validate the complete resulting file through the existing finite complete-carrier boundary; unavailable authority is an explicit refusal, not a bypass.

A non-no-op proposal changes Version N→N+1 and clearly illustrative updated_at only. Return exact Subject/revision-metadata patches, before/after hashes and Versions, complete proposed Carrier, no-op state and canonical preview_sha256 over the full materialized preview. Preview time/hash are not execution evidence. A later approved ad-hoc execution rechecks pins and binds actual updated_at under its approved metadata rule, recording actual final hash; it cannot substitute Subjects/body.

No local Carrier/history/Journal writes. Reject Subject-only apply even via raw internals. Existing generic sealed update and standalone CLI guard remain unchanged. Unsupported MCP is unused. No preview grants live approval/admission.

## Acceptance

CA-E-301/304 own independent checks: valid complete fixtures and separately authored expected occurrence ledger; no producer graph builder. Cover field direction, exact/prefix, Active default, filters, body false positives, ordered pins and invalid-source diagnostics. Cover pinned replacements, all stale preconditions, full-result validation, no-op, duplicate paths/occurrences/dependencies, escapes/symlinks, CRLF/Unicode/unknown-field/body preservation, no-write preview and retained generic guards. Deliberately wrong output must fail comparison.

Existing baseline tests do not prove these features. Recheck accepted source pins at handoff. The bounded RMEDO acceptance is not whole-repository validation. Native Entity/Term relation admission is outside these mechanical file operations.

