---
identity:
  atom_id: CA-M-1016
  ref_id: CA-M-1016
context:
  role: method
  form: Eng Standard
  container:
    scope_unit: CA-SU-15
  tier: 2
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
      <+ Traceability
state:
  version: 1
  status: active
  updated_at: '2026-11-13T12:17:19.900198+00:00'
destination:
  file:
    name: CA-M-1016-PROGRAMMATIC-ENG_STANDARD--store-rmedo-pins-in-markdown-spec-references.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
---
## Summary

Store RMEDO pins in Markdown spec references

## Claim scope

Authoring implementation trace and package policy records in PROGRAMMATIC.

## Claim

### Prose Claim

Store Module pins in `<full module filename with extension>.spec_trace.md` beside the Module, including the Module’s original extension. Store Package pins in `<folder name>.p.spec_trace.md` at the Package root. Keep the full Module filename and use the `.p` marker for Packages. This distinguishes Modules that share a stem and a Module and Package that share a name. Standalone CI/CD workflow files that implement Delivery behavior count as Modules for tracing. Assets and individual golden corpus files are outside the trace scope. If a golden corpus itself realizes an Evaluation Claim, record the pin once in the owning evaluation Package’s spec trace.

Record what the Module or Package implements or follows today. Use Markdown bullet lists under optional `## Implements` and `## Applies` headings. Each bullet contains one exact Atom ID and Version.

- Put Solutions in the owning Package’s Implements section when the Package directly implements them.
- Put Engineering Standards that the Package follows in its current implementation in its Applies section. Applies is available only in Package spec references.
- Put Decisions, individual Requirements, and Test or Evaluation Cases in the Implements section of the Module that directly implements them. Apply the same ownership rule to other Claims.

Keep pins for all cited versions, including non-Current versions. Archiving an Atom or publishing a newer version leaves the sidecar unchanged. Update the pin explicitly when the implemented or applied Claim changes.

Omit empty lists and empty sidecars. Record a package entry once. Build descendant rollups from the sidecars.

## Details

For example, `query.py` and a sibling `query/` Package use `query.py.spec_trace.md` and `query/query.p.spec_trace.md`. A CI/CD workflow at `.github/workflows/publish-release.yml` uses `.github/workflows/publish-release.yml.spec_trace.md` for the Delivery Claims it implements. The Package reference can contain:

```markdown
## Implements

- CA-M-123@4

## Applies

- CA-M-456@2
```