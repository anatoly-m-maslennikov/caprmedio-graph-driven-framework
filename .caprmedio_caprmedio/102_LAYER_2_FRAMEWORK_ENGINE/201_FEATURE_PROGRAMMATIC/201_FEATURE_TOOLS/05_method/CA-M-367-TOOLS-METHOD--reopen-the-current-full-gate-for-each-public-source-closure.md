---
atom_id: "CA-M-367"
content_role: "Method"
current_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release Full Gate reuse"
  depends_on: [Full Gate, Source Proof, Test, Tool, Operator, Version History]
version: 4
updated_at: "2026-10-10 12:56:30 +0400"
relations:
  method_for: [CA-R-1924]
---
# Summary

Reopen the current Full Gate for each public source closure

## Scope

one gated public-source closure.

## Claim

the PUBLIC_RELEASE Tool **must** reopen and validate typed Full Gate evidence for the exact selected Source Proof before **every** commanded public push. After an actual Version History link changes `public_document_closure_sha256` while canonical Version, `version.toml`, and D566 candidate snapshot remain unchanged, it invokes the existing selected native `RELEASE_VERSION` Full Gate producer for that current selected N+1 same-Version package proof and retains a fresh non-promoting bridge to the new public-document closure before the follow-up push.

## Details

1. Before a public push, reopen the original retained native package proof. Legacy `FullGateEvidence` uses its bound reader; native `NativeFullGateEvidence` uses the detached retained-packet reader. Both branches establish only the immutable D566 candidate snapshot, framework version, version-carrier identity, and selected N+1 package provenance. The original receipt does not attest a newly prepared public-document closure.
2. The detached native reader remains read-only: it reopens the original descriptor, package and complete constituent receipts under the explicit artifact root. It validates recorded test evidence and never executes the renewed producer or supplies either public-document-closure bridge. A boolean, copied test summary, or unverified digest is not gate evidence.
3. For **each** O194 initial public-document closure and O198 post-history-link closure, the already sealed public request admits one fresh non-promoting invocation of the existing selected native `RELEASE_VERSION` Full Gate producer against the current selected N+1 same-Version package proof. The Tool derives the current closure locally, receives the current typed producer result, and retains CA-D-615's exact bridge before that phase's push. An actual Version History link therefore changes the closure and requires a distinct fresh bridge even while canonical Version, `version.toml` digest, D566 candidate snapshot, and package identity remain unchanged. The Tool reopens the typed result and bridge before the corresponding push. It must not install a runtime, promote a package or Skill, retire an image, create a second Operator authorization, accept a caller pass flag, or fall back to another checkout.
4. A changed canonical Version still requires the renewed local cycle governed by CA-R-1922. The earlier package proof, gate receipt, or document-closure bridge never authorizes a later candidate, Version, or closure.
5. These checks run only within the exact Operator-sealed public-release request. Retaining or reopening evidence alone does not invoke public release.
