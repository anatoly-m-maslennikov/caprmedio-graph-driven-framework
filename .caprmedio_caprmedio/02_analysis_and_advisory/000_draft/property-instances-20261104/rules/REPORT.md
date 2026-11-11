# Property instance rule previews

The complete `.txt` candidates and pinned sources in `manifest.json` are proposals, not adopted Atoms. CA-R-2619 is reproduced unchanged. The earlier universal mandatory-occurrence proposal is superseded.

A Property instance has at most one occurrence per applicable schema and corresponding bearer, with distinct data-bearer and model-Property links. Its schema retains its original model bearer. Present Properties have a value; nonempty child structure can be the value of a structural parent whose direct-value count is zero. A leaf with a positive minimum direct-value count is required; zero by itself does not require presence. Explicit occurrence and other applicable constraints still apply.

CA-R-2498 declares the common Markdown format for Content descendants. Content child declarations use inherited format and their own value bounds. CA-R-2500 retains the parent and child-name constraints and delegates child value counts to CA-R-2721 and CA-R-2722. The Formal Claim fence requirement applies only when Formal Claim is present. Named leaf declarations that formerly allowed an absent occurrence and exactly one direct value have been changed to allow zero or one direct value, preserving the previous possibility of absence. Existing additional constraints still apply.

The candidate set covers Current requirement declarations under CORE_META_MODEL found by the exact optional occurrence and single direct-value pattern. Other syntax, conditional contexts, containers and separately governed requirements require review; this scan is not evidence of project-wide completeness. Format inheritance, count-only syntax, presence-conditioned fence evaluation, parser/runtime, data migration and adoption remain to be verified.
