# Atom carrier Delivery alignment

`previews/CA-D-657.txt` is a complete prospective replacement for Current CA-D-657@3, pinned in `manifest.json`; it is not applied. It changes three operative passages and preserves Summary, IDs, source metadata, scope-field migration disposition, legacy alias handling, conflicting/equal-pair safeguards, projection restrictions, and the Subjects-only draft exception.

- For ordinary RMED, the `## Claim` container has zero direct values and one or both named children. Each child has zero or one direct Markdown value; when a Formal Claim value exists, its CFEL fence applies. Other headings inside a Prose value do not create Properties without an applicable Declaration. This aligns with CA-R-2500@5, CA-R-2721@2, CA-R-2722@2 and inherited Markdown from CA-R-2498@5.
- The Plan Header Property is AI Agent Confidence Threshold, with zero or one integer values (CA-R-2711@2); inherited values are not copied as explicit selections. Plan Header Implementation Retry Limit is removed from this rule in accordance with the latest Workflow-only decision. The preview uses the selected canonical `ai_agent_confidence_threshold` key. The new-ID successor preview and migration boundary are in `RETIREMENT-AND-ADOPTION.md`.
- A Delivery rule alone does not establish a new MODEL Property. The preview drops the unconditional `assignee` admission from this general rule and retains the requirement for a separate applicable Property Declaration and encoding. This does not decide the future identity or encoding of Assignee.

## Other directly affected Current Delivery sources

- **CA-D-472@29:** Still prescribes `autonomous_confidence_threshold` and the old Plan Autonomous Confidence Threshold name for the Property now declared as Header AI Agent Confidence Threshold. The proposed new-ID successor uses `ai_agent_confidence_threshold` and a bounded migration disposition; adoption and ID allocation remain pending.
- **CA-D-447@30:** Still admits Plan frontmatter `implementation_retry_limit` and Plan inheritance. Reconcile with the Workflow-only retry decision while preserving separately governed settings/default behavior; this needs its own bounded source review.
- **CA-D-669@1:** States an optional R-only nested Formal Claim. The ordinary RMED Claim model permits the child across RMED, subject to its model constraints; retain its independent configuration-boundary provisions when repairing it.
- **CA-D-479@30:** Its child-heading arrangement already matches Claim containment but describes a Formal Claim as containing a fence without expressing CA-R-2721@2's zero-or-one value and conditional fence rule. Review the direct-value statement against that current Declaration.
- **CA-D-473@25:** Still carries the old Plan Assignee Subject and encoding. Verify a current Plan Assignee Property Declaration before retaining that admission; an existing Delivery Atom or occurrence of `assignee` alone does not declare it.
- **CA-D-663@2:** Describes generic heading ancestry as Properties, whereas CA-D-479@30 and CA-R-2722@2 limit Atom Property recognition to declared children and preserve other Prose headings as value. Clarify the generic outline versus declared-Property boundary without destroying generic Markdown retrieval behavior.

This is a bounded scan for this Header/Content/Claim feature, not an audit of the entire Delivery registry. It does not establish implementation, validation, application or migration. The confidence key is selected in this prospective packet; it is not yet applied. No value or fallback has been invented.
