# Code Synopsis content contract review

This content contribution merges into the one generic Code Synopsis Form owner. That owner targets `.Header.Form := Code Synopsis` and binds its instances to Role Implementation; it is not a second role-qualified Declaration.

The proposed shape reuses the required Summary and existing Claim container with one or both existing children: Formal Claim and Prose Claim. Each child is optional individually; Formal Claim remains CFEL-fenced and Prose Claim is Markdown. This allows formal statements of actual facts, prose explanation, or both, without inventing subproperties or headings. Role Implementation makes the contribution descriptive of actual implementation, not normative intent.

Partial descriptions need no specification; rationale is optional, inferences are distinguished from observations, and specification differences remain neutral unless assessed as matters needing resolution. R1873 continues to govern implementation production. M307's existing CCE role profiles do not cover Implementation; none is borrowed or created. Code references and lifecycle remain separately owned. All direct Current pins in `ready-bodies.json` match. No native files were changed.
