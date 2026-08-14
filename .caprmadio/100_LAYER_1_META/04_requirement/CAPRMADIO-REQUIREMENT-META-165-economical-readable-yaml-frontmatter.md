---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-165
scope_path: layer:meta
subject_scopes:
  - principles
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-115-prioritize-human-comprehension-and-decisive-structure
    - CAPRMADIO-REQUIREMENT-META-139-use-canonical-carrier-address-as-authority
    - CAPRMADIO-REQUIREMENT-META-140-apply-dry-across-caprmadio
    - CAPRMADIO-REQUIREMENT-META-163-semantic-irreducibility
---

# Economical, readable YAML frontmatter

Every CAPRMADIO YAML frontmatter schema must use the least syntax and nesting
that preserves unambiguous meaning, deterministic parsing and validation,
required extensibility, and immediate human readability.

A key, wrapper, discriminator, or repeated value is forbidden when its meaning
is already determined by the canonical carrier address, parent key, registered
Type, or value shape. Syntax economy must not depend on positional conventions,
ambiguous shorthand, or hidden inference that makes a carrier harder to read,
validate, extend, or diagnose.
