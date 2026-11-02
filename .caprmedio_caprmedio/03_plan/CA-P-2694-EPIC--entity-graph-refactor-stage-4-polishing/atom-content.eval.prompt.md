# Review Atom content

Review the complete supplied Markdown, including its Summary, against the supplied facts, instructions and Atom content-writing prompt. Use that writing prompt as the contract; do not add your own style rules.

Check syntax, vocabulary, structure, formatting and meaning:

- When the source is Operator input, check that its wording stays as close as possible. Allow spelling, grammar, punctuation and structural corrections needed for coherent statements with simple syntax. Flag unnecessary synonyms, formal vocabulary, invented paraphrases or changed meaning. Do not penalize retaining clear Operator wording.
- Compare the body with the source. Keep actors, scope, required outcomes, conditions, limits, references and formal expressions intact. Distinguish necessary from useful, must from may, all from any, and AND from OR.
- By default, check that Summary is a faithful short version of the whole Atom; for RMED it is normally a statement. Follow explicit Form-template overrides: R / Form: Declaration may use a topic such as “Define Run” and may contain multiple prose or GFEL statements. Do not demand a condensed Claim from a Form that explicitly permits topic Summaries. Reject contradictory Summaries or invented meaning; do not require every supporting detail in the title.
- Check that source terms, names and key concepts are preserved, including DRY and MECE when present. Flag replacement with synonyms or invented paraphrases; simplify surrounding prose instead of terminology. Keep clear source wording. Do not demand fixed openings, exact matches to an older Summary or an invented word limit.
- Follow the supplied section template. Check shared-opening lists and number only sequences.
- Review writing and fidelity, not whether the underlying business rules should be redesigned.

Report only real problems. Quote the source and draft where needed to make a meaning change clear. Suggest the smallest correction. Do not rewrite the Atom or turn a preference into a requirement.

Return `Pass` if there are no issues. Otherwise return `Needs changes` or `Needs context`, followed by a short list containing:

- Location and exact quote
- Problem and relevant source evidence
- Smallest correction

If information needed to judge a point is missing, name it rather than guessing. Do not claim a body-fidelity pass when the source was not supplied.
