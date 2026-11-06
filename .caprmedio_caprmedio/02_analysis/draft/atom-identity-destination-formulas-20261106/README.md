# Atom identity and destination formulas

Draft work. Current authority, live filenames and runtime behavior are unchanged.

## Accepted decisions

- ID has two hyphens: `CA-R-001`. Its components are Project Prefix, first Role letter, and a number with at least three decimal digits. The number is unique within its Project and Role; versions retain the same logical ID.
- The serialized key becomes `identity.id`; the reference key remains `identity.ref_id`.
- Ref ID is the base ID for Current, `ID@Version` for Archived, and `ID@Version-draft` for Draft.
- The common filename uses Ref ID, Label with Role fallback, the immediate Container's Scope Unit name or Atom ID, and the Summary slug. Label/Role and Container tokens are uppercase. The Summary is lowercase with hyphens. The extension is `.md`.
- Plans retain the Work Sequence Number prefix.
- `$a` introduces a binding. `a.property` and `$a.property` read that binding within the same scope. Existing no-shadowing rules remain.
- A simple filter can be written `FOR EACH $a[<Atom>, .context.role = Plan]: (...)`.
- `<Atom>.destination.file.name(a)` calls the expression authored in the Atom Declaration for the same receiver `a`.
- A narrower Declaration replaces only the inherited calculation for that Property. Other inherited constraints still apply. Ambiguous calculation selection is a conflict.

## Drafts

- CA-R-2995@1: Declaration Expression Call.
- CA-R-2996@1: Property Calculation specialization.
- Updated CA-R-2552@5 and CA-R-2778@1: scoped bare binding references and simple filters.
- Updated CA-R-2957@1 and CA-R-2487@15: qualified calls and language overview.
- Updated CA-A-1321@1: proposal and rationale.

The new Draft paths are listed in [drafts.json](drafts.json).

## Open calculation details

- Label currently defaults to Form. The pending question is whether Role replaces that default everywhere or only in filename calculation.
- String concatenation, case conversion, Summary slug conversion, decimal formatting and complete filename/path formulas still need their declarations and review.
- The selected Declaration supplies the called expression. This does not introduce `BASE_FILENAME` or a new stored Property.

## Migration boundary

The prior `8ffaff048` Header packet writes `identity.atom_id`. The approved `identity.id` change requires rebasing that packet and checking its readers before live application. Its earlier rehearsal does not verify this newer contract. The obsolete additional simulation was interrupted before producing a plan or readback result.

Workbench reported its narrow code checks ready for the previous contract; the installed old runtime remains a cutover blocker. Production code, deployment and Workflow implementation stay with their owners.
