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
version: 5
updated_at: "2026-10-10 18:14:20 +0400"
relations:
  method_for: [CA-R-1924]
---
# Summary

Reuse the stable local Full Gate for public release

## Scope

one stable local-release candidate and its public metadata.

## Claim

the PUBLIC_RELEASE Tool **must** reopen and validate typed Full Gate evidence for the stable selected local-release candidate before public effects. A Version History link or other mechanical public metadata update does not invoke another producer, suite, gate, review, package installation, or authorization when that candidate and its Version identity remain unchanged.

## Details

1. Before public effects, reopen the original retained native package proof. Legacy `FullGateEvidence` uses its bound reader; native `NativeFullGateEvidence` uses the detached retained-packet reader. Both branches establish the immutable D566 candidate snapshot, framework version, version-carrier identity, selected N+1 package provenance, and recorded complete suite evidence.
2. The detached native reader remains read-only: it reopens the original descriptor, package and complete constituent receipts under the explicit artifact root. A boolean, copied test summary, or unverified digest is not gate evidence.
3. The Tool derives every public-material closure locally and reopens its carriers before the corresponding public effect. Actual PR URL and concise Version History metadata bind that public closure but do not change the tested candidate or require a closure-specific gate bridge.
4. A changed executable candidate, Methodology, package, Version, or `version.toml` requires a new local candidate, complete suite, same-bytes promotion and live verification. Earlier evidence never authorizes that changed candidate.
5. These checks run only within the exact Operator-commanded public-release workflow. Retaining or reopening evidence alone does not invoke public release.
