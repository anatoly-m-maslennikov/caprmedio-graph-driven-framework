# Latest Operator decisions (ordered; later wins)

1. Default: one Atom, one coherent Claim; optional Semantics/Details. Summary faithfully condenses the whole Atom; RMED Summary normally a statement. Forms (formerly Types) may explicitly override defaults.
2. R / Form: Declaration can contain multiple statements, in prose, GFEL formal expressions, or both, about one coherent topic. Its template may allow a topic Summary such as Define Run. No invented GFEL syntax/functions.
3. From Operator input, keep wording as close as possible; correct grammar/spelling and organize coherent statements with simplest syntax. Keep exact terms/key concepts, not polished synonyms.
4. Scope Unit Declarations may replace project_structure.toml AS GOVERNING SOURCE. Any necessary compatibility TOML is derived, no independently maintained second authority. Adoption/cutover not yet authorized in this Draft task.
5. A Declaration can cover declared Scope Unit ID, Name, ordered/unordered, Label, even Navigation Number, and connections. No new mandatory per-field cardinality/format/derivation rules were decided here.
6. Rejected extra per-unit Definition Atom: Declaration plus Contracts sufficient. Generic shared structure belongs in reusable Declaration model/template; do not duplicate generic semantics per unit or silently retire active sources.
7. Scope Constraint is outside the governed Scope Unit; MAY be part of its Declaration. External here relative to governed unit; ordinary parent ownership is existing convention, not permission to invent scopes. Inside: Scope Contract ATOMS, plural, tier 0, RMEDO as applicable; not exactly one and not forced all five roles.
8. Earlier proposal: Goal inside Declaration. SUPERSEDED by latest explicit correction: exactly ONE Declaration and ONE OR MORE separate Goals outside the declared Scope Unit. Do not put Goals into Declaration operative Claim. Can link separate Goals without duplicating their content.
9. Existing ordinary Goals have parent owner/child Target Scope Unit. Project Goal is Operator-owned, targets Project, Tier -1. Operator Actor is not a Scope Unit. Latest answer: “Outside the project, as project goal”. Keep the Project Declaration outside the Project, like the Project Goal, with the same external Operator ownership. No filesystem path was chosen; the proposed project-root carrier location is not adopted.
10. Unrelated source revert completed:47 Active root project Principle/Core contents restored from Oct27, metadata kept. E002 retired. Do not undo or rewrite them in this task.

Task: update DRAFTS and Spec Proposal only, then review against latest human input and for coherence/gaps. No Current methodology, Project Structure TOML, code/runtime, projections or promotion. Historical A1313 Done proposal records older adoption, not a fresh permission to publish this amendment. Existing generic structural GFEL Scope Unit Declaration is a KIND model, not one external declaration per actual unit.

Do not add functions, new relation names, new control/status machinery, mandatory 70/100 char limits, blanket Principle/Form adoption, or automatically synthesize all project instance declarations.

Latest answer to local Contract minimum: “I’m not sure, so no.” No mandatory minimum is introduced; zero local Scope Contract Atoms is allowed. This does not alter the separate 1+ external Goals requirement.

Latest Navigation Number answer: “Explicit”. Navigation Number, when present, is explicitly declared. Filenames and views that use it derive their displayed number from that declared value; do not maintain a separate authoritative value for the same position. No mandatory presence, new numeric format or default is introduced.

Latest Declaration binding answer: “One atom with role scope unit declaration and active subject = the Scope Unit”. Bind via Governs to the specific declared Scope Unit. Count one Active Scope Unit Declaration Atom for that unit; do not introduce a duplicate Claim/Target binding. Existing Requirement role and Declaration Form are retained.

Latest correction: “.Role = Requirement & .Form = Scope Unit Declaration”. This supersedes putting Scope Unit Declaration in Role and the earlier generic Declaration Form discriminator for this specific template. Exact expression: `(Atom//.Role = Requirement & .Form = Scope Unit Declaration & .subjects.active = Scope Unit//){:1}`.

Latest correction supersedes the earlier explicit Scope Unit Navigation Number: “we can drop navigational number for scope units”; “keep only for steps and P”. Scope Units retain Local Order. Navigation Number remains only for Steps and P Atoms. No Current configuration or filename changes are performed by this Draft update.

Latest Applicable Methodology answer: “yes, it's a special projection”. Retain the special Projection, withdraw the separate hosting Scope Unit Declaration Draft and plan retirement of that Scope Unit at adoption. Do not invent a Scope Unit Goal or delete delivered Projection content.

Latest folder decisions: “Delivery folder is derived it's $parent/<label>_<order>_<name>”; for Unordered units “Omit the order segment and separator”; “Authority Folder name = Delivery Folder”, “let's keep it simple”. Use one shared D naming Policy. No separately authored Authority/Delivery path values in per-unit Declarations.

Latest formal decisions: non-root IDs are CA-SU-<number>. Authority Folder uses the ID prefix; Delivery Folder omits it. Ordered names include ordered.number; Unordered names omit that segment and separator. Project inherits ordered=false and no ordered.number from its model; its Authority Folder remains .caprmedio_<project name>. Project has no Scope Unit ID because it is not moved or renamed through Scope Unit operations. Earlier same-folder-name and root-ID proposals are superseded.

Latest ordering property declarations: Scope Unit.ordered: [bool]{:1}; Scope Unit.ordered.number: IF ordered = true THEN [int, 1+]{:1} ELSE []{:0}. The condition uses ordered on that same unit. The numeric minimum and value cardinality are separate.

Latest grouping decision: order is a no-direct-value group; ordered and number are its sibling Properties. Use Scope Unit.order.ordered and Scope Unit.order.number. The Project rules are Project//.order.ordered == false and Project//.order.number: []{:0}. Null is not substituted for zero values.

Latest adoption instruction: remove authority_mode: strict overrides; do steps 1 and 3 (remove obsolete overrides and promote Declarations/shared model). Retire project_structure.toml entirely, including its governing Atoms, file and implementation consumers. Update the Epic first, then continue. This supersedes retained-TOML compatibility proposals.
