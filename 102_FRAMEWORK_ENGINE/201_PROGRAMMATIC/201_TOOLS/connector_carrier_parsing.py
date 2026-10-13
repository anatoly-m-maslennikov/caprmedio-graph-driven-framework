"""Pure defensive cleanup classification; it never proves non-Atom eligibility."""

def removal_guard(prefix: bytes) -> str:
    # shortcut: refuse YAML-frontmatter cleanup, extend only with accepted positive classification proof.
    if prefix.startswith((b"---\n", b"---\r\n")):
        return "uncertain"
    return "requires_positive_eligibility"
