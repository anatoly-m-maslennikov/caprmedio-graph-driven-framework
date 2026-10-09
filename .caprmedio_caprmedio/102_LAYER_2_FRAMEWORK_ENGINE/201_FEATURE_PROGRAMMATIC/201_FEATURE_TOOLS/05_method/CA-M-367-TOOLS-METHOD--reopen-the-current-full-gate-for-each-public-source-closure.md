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
version: 2
updated_at: "2026-10-10 02:48:57 +0400"
relations:
  method_for: [CA-R-1924]
---
# Summary

Reopen the current Full Gate for each public source closure

## Scope

one gated public-source closure.

## Claim

the PUBLIC_RELEASE Tool **must** reopen and validate original typed Full Gate evidence for the exact selected Source Proof before **every** commanded public push, including a newly sealed Source Proof after Version History linking changes the snapshot.

## Details

1. Consume the existing full-gate interface and its original retained receipt. Legacy `FullGateEvidence` uses its bound reader; native `NativeFullGateEvidence` uses the detached retained-packet reader. Both branches validate the candidate snapshot, framework version and version-carrier identity against the selected Source Proof.
2. The native reader reopens the original descriptor, package and complete constituent receipts under the explicit artifact root. It validates recorded test evidence; it neither executes a new gate nor reconstructs live candidate authority. A boolean, copied test summary or unverified digest is not gate evidence.
3. A changed Source Proof requires evidence for that newly sealed closure. The earlier packet cannot authorize a later push after Version History changes the snapshot.
4. These checks run within the public-release capability only on the Operator's command. Retaining evidence does not invoke installation, private package promotion or public release.
