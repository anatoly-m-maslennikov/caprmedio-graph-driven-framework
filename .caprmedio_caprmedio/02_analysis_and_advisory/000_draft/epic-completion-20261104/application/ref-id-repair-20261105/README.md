# Identity and Status repair — 2026-11-06

All 206 original identity/Status holds now have formula-valid Ref IDs. No missing Status, missing ID or Draft-lineage identity hold remains in this set.

- Assigned numeric identities to 40 existing v1 Drafts and recovered Workflow Mermaid Draft CA-R-2962@1. Their bodies, Versions and Draft state were preserved. Five proposals retain their historical/withdrawn purpose.
- Restored Status Active on 159 records directly in ordinary Role folders, following the Operator's folder mapping. Added 151 Ref IDs from established base IDs, including recovered CA-D-409.
- Assigned fresh IDs to six existing Drafts while preserving five Version 2 heads and one Version 3 head. The five known archived predecessors remain byte-identical. The Operator explicitly approved preserving Versions.
- Restored the final eight IDs from filenames after a carried-ID collision check, as approved by the Operator: CA-C-268 through CA-C-272, CA-D-019, CA-D-021 and CA-D-022. Added matching Current Ref IDs.
- Repaired exact renamed-file references and their Markdown destinations. Frozen archives and historical evidence remain unchanged.

This closes the original 206-record repair set. It does not close the full Epic or establish full schema conformance. No Draft was promoted. This source lane changed no production code, runtime, tests or Journal.

Evidence: progress-readback.json; each application directory's plan and receipt; identity/final-eight-collision-check-20261106.json; verification/verification.json; verification/folder-status-20261106.json; verification/versioned-draft-application.json; verification/final-206-readback-20261106.json.
