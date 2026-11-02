# Regenerate an Atom Summary

Write one short, meaningful Summary from the supplied Atom content. The original Summary is hidden.

A Summary states what the whole Atom means. It is a title, not an abstract or a compressed copy of every sentence. It can be a short instruction, a statement or a familiar principle name. Do not force one sentence form.

1. Read the Claim and its context. Identify the main assertion or purpose of the whole Atom.
2. Keep the central subject, action and scope. Preserve whether the Atom specifies a result, explains a method, checks something or describes a representation.
3. Keep the source's clear words. Preserve important restrictions such as "all and only", optional versus required, and read-only. Do not move a qualifier: "all required X" does not mean "all X".
4. Name the main capabilities or responsibilities. Leave examples, test cases, parameter bindings, return conditions and lists of exclusions in the body unless they are the main point.
5. Use a group name instead of listing all its members when that keeps the meaning. If several clauses define one thing, cover their shared meaning rather than selecting just one clause.
6. Remove supporting detail from the title. Do not remove a main assertion or replace several concrete outcomes with a vague label. A concise Claim sentence can stay intact when it already works as a title.

Before returning, check both questions:

- Does this retain the main meaning without adding, narrowing or broadening it?
- Does this read as a clear title rather than a list of details?

There is no fixed word count. Use simple English and retain needed technical names.

Return one JSON object per input: `key`, `generated_summary`, `ambiguity` (`null` if none).

Use only the supplied content and writing guide. Do not look up old Summaries, expected answers, identities or earlier attempts. Do not edit source Atoms.
