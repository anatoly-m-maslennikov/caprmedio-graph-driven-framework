---
artifact_type: requirement
artifact_id: DSET-REQUIREMENT-GOV-123
scope_path: layer:gov
subject_scopes:
  - carrier-format
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - DSET-REQUIREMENT-GOV-116
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-038
      - DSET-REQUIREMENT-GOV-122
      - DSET-CONSTRAINT-GOV-002
---

# Requirement — Keep frontmatter values ready for plain scalars

DSET-controlled frontmatter keys and string values are designed for
unambiguous YAML plain-scalar storage. DSET-authored Markdown therefore emits
those values without quotation marks.

Controlled property keys use `snake_case`. Controlled vocabulary values use
lowercase `kebab-case` unless the property's registered grammar requires
another stable form, such as an artifact ID, `scope_path`, relation kind, URL,
or LLM session reference.

Every registered string grammar must:

- contain no whitespace or control characters;
- use only letters, digits, `.`, `_`, `-`, `/`, or `:` unless an external
  standard requires another YAML-safe character;
- avoid YAML booleans, nulls, numbers, dates, timestamps, directives, tags,
  anchors, aliases, collection syntax, and comment syntax; and
- preserve the same string meaning when parsed as YAML 1.2.

Lists use block sequence syntax with one plain scalar per item. Structured
properties use block mappings. Human prose belongs in the Markdown body.
Uncontrolled external literals that cannot satisfy a registered safe grammar
are represented in the body or through a governed reference rather than
forcing quoted free-form strings into frontmatter.

## Primary claim

Every DSET-controlled Markdown frontmatter value is valid and unambiguous
without quotes, and DSET-authored carriers emit it in that plain form.

## Rationale

A constrained plain-scalar vocabulary makes frontmatter easier to read in
GitHub and avoids inconsistent quoting while preserving deterministic parsing.
Keeping prose and unsafe external literals out of properties also prevents
frontmatter from becoming a second narrative document.
