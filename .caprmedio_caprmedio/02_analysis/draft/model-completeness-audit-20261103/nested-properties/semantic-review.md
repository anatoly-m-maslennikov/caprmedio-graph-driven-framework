# Bounded semantic review of nested Property cardinalities

Scope: 21 parent paths in the inventory, with `Atom.Content.Claim` split into RMED and non-RMED contexts, giving 22 review rows. The latter is a context split, not a 22nd distinct Property. This is not a proof that those are all MODEL Property groups. MODEL supplier frontier is `../model-supplier-frontier.json` (1,167 records; SHA-256 `8deca481ee12c09ac65df272e20c4d15aaffafbafcd344187003011bfe9db71e`), including CA-R-2632 and 12 other Current legacy `subjects.governs` sources absent from the older 1,154-source pin. Legacy Subject spelling is migration debt, not by itself a missing nested contract; carrier_read_view handles it. Rules CA-R-2243:42–50 distinguish occurrence, direct values, immediate and recursive counts; CA-R-2470:25–33 and CA-R-2471:27 establish inherited applicable Property declarations and constraints. Wildcards constrain names; they do not declare arbitrary named Properties. CA-R-2722:34 confirms Markdown headings alone are not child Properties. Per-child omissions are a separate precision issue from the user's parent nested-count question.

| Parent/context | Classification | Immediate nested count and name restriction; provenance and precision |
|---|---|---|
| Atom.Content | Supported | R2498:29 `0+`, string; R2498:30 recursively `0+`, string. These constrain, not declare, names. Summary R2499:28; Claim R2500:28 conditional; Semantics R2502:28; Details R2503:28 conditional. |
| Atom.Content.Claim / RMED | Supported | R2500:28–31 `1..2`, string and Formal Claim/Prose Claim allowlist; each `0..1`. R2721 and R2722 define children. |
| Atom.Content.Claim / other Roles | Unknown | R2500:28–31 explicitly limits its contract to RMED. Generic Content recursion R2498:30 does not establish the immediate Claim count; no general Claim child contract established for other Roles in this bounded review. Do not presume such a Claim exists there. |
| Atom.Header | Supported | R2719:33 `0+`, string and explicit allowlist; child declarations specify occurrences. Role-specific names are admitted but their actual applicability is qualified. |
| Atom.Header / Concern | Inherited | R2719:33 generic Header `0+` and allowlist; R2710:28–29 declares Priority for Concern. R2470 inheritance. |
| Atom.Header / Plan | Inherited | R2719:33 generic Header `0+` and allowlist; R2711:28–29 and R2712:28–29 declare Plan children. R2470 inheritance. |
| Atom.Header.Relations | Supported | R2709:29 `0+`, Relation// names; R2698:28 `IS_CONTAINED_BY` is `0..1`. Name format is not an exhaustive list and does not itself declare relation-name Properties. |
| Atom.Header.Relations.IS_CONTAINED_BY | Supported | R2698:29 exactly 1, atom/scope_unit allowlist; R2699:28 and R2700:28 each `0..1`. |
| Atom.Header.Subjects | Supported | R2713:29 `0..2`, Active/Passive allowlist; R2714:28 and R2708:32 each `0..1`. |
| Atom.Header.Tier | Supported | R2706:33 `0..1`, Label allowlist; R2707:28 Label `0..1`. |
| Atom.Header.Carrier Destination | Supported | R2715:29 exactly 1, File allowlist; R2716:28 File exactly 1. |
| Atom.Header.Carrier Destination.File | Supported | R2716:29 exactly 2, Name/Path allowlist; R2717:28 and R2718:28 each exactly 1. |
| Event Record.Relations | Supported | R2581:25 `0+`, Relation// names; R2582:24 HAS_EVENT_AUTHOR exactly 1. Format does not itself declare arbitrary children. |
| Event Record.object_input | Supported | R2572:25 `2..3`, id/version/updated_at allowlist; R2573:24 `1`, R2574:24 `0..1`, R2575:24 `1`. |
| Event Record.object_output | Supported | R2576:25 `2..3`, id/version/updated_at allowlist; R2577:24 `1`, R2578:24 `0..1`, R2579:24 `1`. |
| Project.Settings | Supported | R2532:25 `3..11`, explicit 11-name allowlist including Authority Modes; child declarations supply occurrences. No conflict with R2632's Authority Modes name. |
| Project.Settings.Authority Modes | Supported | R2632:22–23 `2`, two-name allowlist; R2633:25 and R2634:25 each `1`. R2632's legacy Subject is a source-normalization issue, not absent contract. |
| Project.Settings.Confidence | Supported | R1979:27 `0..2`, two-name allowlist; R2624:25 and R2625:25 each `0..1`. |
| Project.Settings.Interaction | Supported | R1982:27 `1`, Reporting Mode allowlist; R2626:25 exactly `1`. |
| Project.Settings.RMED Review | Supported | R2631:26 `0..2`, two-name allowlist; R2629:25 and R2630:25 each `0..1`. |
| Projection.Source | Supported | R2586:25 `1..2`, Named Selection/Atoms allowlist; R2541:24 `1`, R2540:24 `0..1`. |
| Scope Unit.order | Supported | R2687:25 `1..2`, ordered/number allowlist. R2685:25 and R2686:26 omit separate occurrence slots; their value conditions do not substitute for occurrence. This is secondary precision, not a missing parent count. |

Result for the bounded rows: 19 explicitly supported, 2 inherited, 1 unknown (non-RMED Claim context); no confirmed parent nested-count contradiction or missing parent count. The non-RMED row is not an assertion that a Claim group is required outside RMED. A Property with no declared children is not granted new children by a wildcard: explicit leaf `.*[]{:0}` remains direct evidence of zero; inherited declarations and allowed names must be resolved before classifying an omitted leaf statement. R2243:50 explains explicit zero, and R2470:25–33 resolves inherited declarations; this review does not establish a universal explicit-zero requirement.

## Definition-only Property parents: separate authority gap

The entity-lane map identifies 22 Definition-only Property targets. Four are literal parents of another such target. None has a matching `Requirement / Declaration` immediate nested-cardinality expression in the 1,167-source supplier frontier; Definitions and Delivery sources are not counted as Declaration contracts. These four are outside the 22 rows above and are **not nested-contract passes**. This literal comparison does not prove that broader inherited declarations cannot constrain them; such an effective contract requires separate evidence.

| Definition-only parent | Child target | Definition source evidence | Result |
|---|---|---|---|
| Carrier.Canonical Address | Segment | CA-R-1949:7, CA-R-1948:7 | No matching parent Declaration authority found |
| Carrier/File.Filename | Scope Unit Token | CA-R-1975:7, CA-R-2345:7 | No matching parent Declaration authority found |
| Carrier/File.Main Content | CCE Operator, Paragraph | CA-R-2347:7, CA-R-2348:7, CA-R-2349:7 | No matching parent Declaration authority found |
| Carrier/File.YAML Frontmatter | Scalar | CA-R-2350:7, CA-R-2351:7 | No matching parent Declaration authority found |

The other 18 Definition-only targets have no literal child within that 22-target map. This does not establish leaf closure or exclude children declared through another target, qualification, inheritance, or source outside this map. No Engine instance records are used.
