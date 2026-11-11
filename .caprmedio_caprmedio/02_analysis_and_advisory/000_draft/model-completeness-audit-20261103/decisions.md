# Operator decisions during MODEL audit resolution

## 1. Object, Artifact and Carrier boundary

- Object: an instance of any model entity.
- Artifact: a file or folder.
- Delivery: `Object >> Carrier//`.
- Operations work with Objects.
- Adapters handle the file/folder representation, including reading, creation, updates and moves.
- Main Content Paragraph is not needed as a modeled Property. Its missing Declaration is a retirement candidate.

## 2. Atom destination Properties

Retain the MODEL declarations and stored values for:

- `Atom.Header.Carrier Destination.File.Name`: calculated full filename, including extension.
- `Atom.Header.Carrier Destination.File.Path`: calculated containing directory, relative to repository root.

The adapter sets the selected Carrier instance from the selected Atom instance:

```CFEL
Atom//$atom >> Carrier//$carrier;
$carrier.filename == $atom.Header.Carrier Destination.File.Name;
$carrier.location == $atom.Header.Carrier Destination.File.Path
```

The explicit variables keep the source Object and destination Carrier paired. Operator notation above refines the accepted generic example; it does not add another stored Property.

The Header/Content serialization mappings remain:

```CFEL
atom.header.** >> markdown.frontmatter;
atom.content.** >> markdown.markdown
```

The latest Object definition supersedes the earlier Node-only wording. Carrier remains the delivery target; `Object >> Artifact` was rejected. The proposal to remove stored destination Properties was rejected. Current governing sources and runtime have not been changed by this decision record.

## 3. Declaration lookup Relation

Rename `IS_DEFINED_BY` to `IS_DECLARED_BY`. Select Declarations instead of the former Entity Definition qualification. Preserve the qualified derivation; a general inverse is not inferred.

## 4. Instance variables and expression groups

Use `$` for variables and explicit typed bindings such as `Atom//$atom` and `Carrier//$carrier`. Reuse `$atom` and `$carrier` for those same bound instances within a Claim. Keep the current binding and endpoint-count semantics; binding itself does not create an instance.

Group expressions in one CFEL block, with model expressions first and instance expressions after them. The labels are comments. They do not introduce Markdown Properties. Explicit named model descriptors such as Relation//NAME remain named references; the groups distinguish purpose rather than mechanically classify every // address as runtime data.

```CFEL
# model
Atom.Header.Carrier Destination.File.Name: [string]{:1};
Atom.Header.Carrier Destination.File.Path: [string]{:1};

# instances
Atom//$atom >> Carrier//$carrier;
$carrier.filename == $atom.Header.Carrier Destination.File.Name;
$carrier.location == $atom.Header.Carrier Destination.File.Path
```

This is a notation example, not a newly admitted governing Atom. Formal population cardinalities and all comment-reading consumers need review before a mechanical migration. Current source carriers and runtime remain unchanged.

The Operator corrected these two model clauses: the value format and allowed value count follow `:`; their names carry no additional `{:1}`. Other optional-Property occurrence rules are not changed by this example.

Use the same `$x` notation for model bindings where needed. This scope is now tracked in P2694@50 as Planned; governing notation and consumer migration remain pending.

## 5. Carrier kinds

Retire Carrier/Git Index. Retain Database, Docker Image, Git Branch, Git Commit, Git Repository and Pull Request. The Operator answered the seven-kind scope question; other detailed Carrier Properties are not changed implicitly.

## 6. Model variable binding

Use `IF $x in (...) THEN ( ... )` with a parenthesized multi-line conclusion. Reuse each matching binding throughout that conclusion. An already bound variable keeps membership-test semantics. No FOR primitive is needed; it is syntactic sugar.

## 7. Carrier layout

Use the Delivery template `--- / <yaml> / --- / <markdown>`. Retire the separate Carrier.Format Property; its inherited File.Format view is also removed. Object Property value formats remain. The adapter applies the selected Delivery template.
