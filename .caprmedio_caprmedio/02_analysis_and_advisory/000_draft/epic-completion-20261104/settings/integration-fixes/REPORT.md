# Settings integration fixes

The proposed CA-R-1981 same-ID preview is withdrawn. See `RETIRE-R1981.md` and the pinned reference inventory for the duplicate-rule retirement plan. The separate CA-R-1404 non-Atom successor remains unchanged.

CA-D-387 is a separate unresolved model issue. CA-R-1630@41 governs atomic admission strictness values `medium` and `high`, and CA-D-387@27 serializes an explicit selection as `[artifacts].creation_strictness` in the existing Framework Settings TOML carrier. The current `Project.Settings.Authority Modes` Declaration specifies `strict` or `casual` for Project and default Scope Unit authority modes. These are different domains and cannot be assumed equivalent. No applicable Requirement/Form Declaration for an Atomic Admission Strictness Property was established, nor did this scan establish an independent adapter-profile authority for retaining the field outside the MODEL. The existing Default Settings TOML contains `creation_strictness = "medium"`; that observation does not supply MODEL authority.

**Decision needed:** Should atomic admission strictness become a declared Project.Settings Property, remain an explicitly governed non-MODEL execution setting, or be retired with its dependent rule and encoding? This affects the CA-R-1630 admission/promotion gates, CA-D-387 serialization and default/override resolution. Do not map it to Authority Modes or invent a Property while that choice is unresolved.

No Current files, runtime or Git state were changed.
