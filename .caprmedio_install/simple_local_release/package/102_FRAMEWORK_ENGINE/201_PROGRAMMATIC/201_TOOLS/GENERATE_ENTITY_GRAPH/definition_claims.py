"""Read definition claims without creating Terms or authority.

The entity-graph projection needs a deliberately small semantic read of an
Atom Carrier.  This module recognizes the current Core definition idiom; it
does not interpret a Subject Path's components as separately defined Terms.
"""

from __future__ import annotations

import hashlib
import re
from collections.abc import Mapping, Sequence
from pathlib import Path


_RMED_ROLES = frozenset({"requirement", "method", "evaluation", "delivery"})
_ROLE_PRIMARY_SECTION = {
    **{role: "Claim" for role in _RMED_ROLES},
    "operations": "Operation",
}
_FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
_BOLD_MEANS = re.compile(r"\*\*means\*\*")
_PLAIN_MEANS = re.compile(r"(?<!\*)\bmeans\b(?!\*)", re.IGNORECASE)
_LEGACY_TYPE_DEFINITION = re.compile(r"\btypeDefinition\b", re.IGNORECASE)
_ATOM_ID_FROM_FILENAME = re.compile(r"(?:[0-9]+-)?(CA-[CAPRMEDIO]-[0-9]+)(?:-|\.|@|$)")


def _diagnostic(code: str, message: str, **details: object) -> dict[str, object]:
    record: dict[str, object] = {"code": code, "message": message}
    if details:
        record["details"] = details
    return record


def _carrier_evidence(carrier: object) -> dict[str, object]:
    evidence_method = getattr(carrier, "evidence", None)
    if not callable(evidence_method):
        return {}
    try:
        value = evidence_method()
    except Exception:  # pragma: no cover - defensive boundary for duck types
        return {}
    return dict(value) if isinstance(value, Mapping) else {}


def _carrier_trace(carrier: object, evidence: Mapping[str, object]) -> dict[str, object]:
    """Retain the usual revision/hash identity even for lightweight fixtures."""

    aliases = {
        "atom_id": ("atom_id",),
        "revision": ("atom_revision", "revision", "version"),
        "carrier_path": ("carrier_path", "path"),
        "carrier_sha256": ("carrier_sha256", "sha256", "digest"),
    }
    trace: dict[str, object] = {}
    for output_key, keys in aliases.items():
        for key in keys:
            if evidence.get(key) not in (None, ""):
                trace[output_key] = evidence[key]
                break
            value = getattr(carrier, key, None)
            if value not in (None, ""):
                trace[output_key] = value
                break
    return trace


def _source(carrier: object, text: str, location: Mapping[str, object] | None) -> dict[str, object]:
    evidence = _carrier_evidence(carrier)
    return {
        "evidence": evidence,
        "location": dict(location) if location is not None else None,
        "digest": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "carrier": _carrier_trace(carrier, evidence),
    }


def _role_primary_section(content_role: object) -> str | None:
    if not isinstance(content_role, str):
        return None
    return _ROLE_PRIMARY_SECTION.get(content_role.strip().casefold())


def _visible_headers_and_lines(body: str) -> tuple[list[tuple[int, int, str]], list[bool]]:
    """Return non-fenced Markdown headings and the visibility of every line."""

    lines = body.splitlines()
    visible = [True] * len(lines)
    headers: list[tuple[int, int, str]] = []
    fence: str | None = None
    for index, line in enumerate(lines):
        fence_match = _FENCE.match(line)
        if fence is not None:
            visible[index] = False
            if fence_match and fence_match.group(1)[0] == fence:
                fence = None
            continue
        if fence_match:
            visible[index] = False
            fence = fence_match.group(1)[0]
            continue
        heading = _HEADING.match(line)
        if heading:
            headers.append((index, len(heading.group(1)), heading.group(2).strip()))
    return headers, visible


def _raw_visible_headers(lines: Sequence[str]) -> tuple[list[tuple[int, int, str]], list[bool]]:
    """Find headings in raw lines without treating fenced or quoted text as one.

    This is intentionally separate from the body-only reader above.  The raw
    source-evidence API must preserve source bytes and line positions, whereas
    ``primary_contribution`` retains its established body-relative behavior.
    """

    visible = [True] * len(lines)
    headers: list[tuple[int, int, str]] = []
    fence: tuple[str, int] | None = None
    for index, raw_line in enumerate(lines):
        line = raw_line.rstrip("\r\n")
        if line.lstrip().startswith(">"):
            visible[index] = False
            continue
        fence_match = _FENCE.match(line)
        if fence is not None:
            visible[index] = False
            if (
                fence_match
                and fence_match.group(1)[0] == fence[0]
                and len(fence_match.group(1)) >= fence[1]
                and not line[fence_match.end() :].strip()
            ):
                fence = None
            continue
        if fence_match:
            visible[index] = False
            fence = (fence_match.group(1)[0], len(fence_match.group(1)))
            continue
        heading = _HEADING.match(line)
        if heading:
            headers.append((index, len(heading.group(1)), heading.group(2).strip()))
    return headers, visible


def _frontmatter_scalar(frontmatter: str, key: str) -> tuple[str | None, str | None]:
    """Read one top-level YAML scalar without accepting duplicate identity data."""

    matches = re.findall(rf"(?m)^{re.escape(key)}:\s*([^\r\n]+?)\s*$", frontmatter)
    if len(matches) > 1:
        return None, "raw-carrier-frontmatter-duplicate"
    if not matches:
        return None, None
    value = matches[0].strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value, None


def _raw_carrier_parts(data: bytes) -> tuple[bytes, bytes] | None:
    """Split one Markdown Atom Carrier while retaining its original bytes.

    Both LF and CRLF are supported, but the opening and closing delimiters
    must use the same EOL style.  No parsed body/frontmatter is ever used to
    reconstruct ``data``.
    """

    if data.startswith(b"---\r\n"):
        eol = b"\r\n"
    elif data.startswith(b"---\n"):
        eol = b"\n"
    else:
        return None
    opening_size = len(b"---") + len(eol)
    closing = eol + b"---" + eol
    boundary = data.find(closing, opening_size)
    if boundary < 0:
        return None
    return data[opening_size:boundary], data[boundary + len(closing) :]


def _atom_identifier_from_raw_path(path: Path, explicit: str | None) -> str:
    if explicit:
        return explicit.strip().strip("\"'")
    match = _ATOM_ID_FROM_FILENAME.match(path.name)
    if match:
        return match.group(1)
    return path.name.removesuffix(".md").split("--", 1)[0]


def _raw_evidence_result(
    evidence: Mapping[str, object] | None,
    diagnostics: list[dict[str, object]],
) -> dict[str, object]:
    return {"evidence": dict(evidence) if evidence is not None else None, "diagnostics": diagnostics}


def raw_primary_content_evidence(repository: Path, carrier: object) -> dict[str, object]:
    """Read and verify D539 primary-content source evidence for one Carrier.

    The returned ``evidence`` is a D539-shaped source reference with an
    inclusive, absolute raw-carrier line span.  Its text digest is calculated
    from the exact reread UTF-8 bytes in that span, including original line
    endings.  It intentionally does not classify or admit any graph fact.

    Existing callers should continue to use ``primary_contribution`` for the
    established body-relative view.  This companion API requires a real
    repository path and never reconstructs source bytes from parsed fields.
    """

    diagnostics: list[dict[str, object]] = []
    trace = _carrier_trace(carrier, _carrier_evidence(carrier))
    raw_path = trace.get("carrier_path")
    expected_id = trace.get("atom_id")
    expected_revision = trace.get("revision")
    expected_sha256 = trace.get("carrier_sha256")
    if not isinstance(raw_path, str) or not raw_path:
        return _raw_evidence_result(None, [
            _diagnostic("raw-carrier-path-missing", "Carrier evidence lacks a repository-relative path.")
        ])
    if "\\" in raw_path or "\x00" in raw_path:
        return _raw_evidence_result(None, [
            _diagnostic(
                "raw-carrier-path-invalid",
                "Carrier evidence must use a NUL-free POSIX repository-relative path.",
                carrier_path=raw_path.replace("\x00", "<NUL>"),
            )
        ])
    if (
        not isinstance(expected_id, str)
        or not expected_id
        or type(expected_revision) is not int
        or expected_revision < 1
        or not isinstance(expected_sha256, str)
        or not re.fullmatch(r"[0-9a-f]{64}", expected_sha256)
    ):
        return _raw_evidence_result(None, [
            _diagnostic(
                "raw-carrier-evidence-incomplete",
                "Carrier evidence must provide atom identity, positive revision, and lowercase SHA-256.",
            )
        ])

    try:
        root = Path(repository).resolve(strict=True)
    except OSError:
        return _raw_evidence_result(None, [
            _diagnostic("raw-carrier-repository-invalid", "The repository root cannot be resolved.")
        ])
    if not root.is_dir():
        return _raw_evidence_result(None, [
            _diagnostic("raw-carrier-repository-invalid", "The repository root is not a directory.")
        ])

    relative = Path(raw_path)
    if (
        relative.is_absolute()
        or ".." in relative.parts
        or relative.as_posix() != raw_path
        or raw_path.startswith("./")
    ):
        return _raw_evidence_result(None, [
            _diagnostic(
                "raw-carrier-path-invalid",
                "Carrier evidence must name one normalized repository-relative path.",
                carrier_path=raw_path,
            )
        ])
    candidate = root / relative
    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            return _raw_evidence_result(None, [
                _diagnostic(
                    "raw-carrier-symlink-rejected",
                    "Carrier source evidence cannot pass through a symbolic link.",
                    carrier_path=raw_path,
                )
            ])
    try:
        resolved = candidate.resolve(strict=True)
        if not resolved.is_relative_to(root) or not resolved.is_file():
            raise OSError("outside repository or not a file")
        data = resolved.read_bytes()
    except OSError:
        return _raw_evidence_result(None, [
            _diagnostic(
                "raw-carrier-unreadable",
                "Carrier source bytes cannot be read from the repository-relative path.",
                carrier_path=raw_path,
            )
        ])

    actual_sha256 = hashlib.sha256(data).hexdigest()
    if actual_sha256 != expected_sha256:
        return _raw_evidence_result(None, [
            _diagnostic(
                "raw-carrier-hash-mismatch",
                "Reread carrier bytes do not match the Carrier SHA-256 evidence.",
                carrier_path=raw_path,
            )
        ])
    parts = _raw_carrier_parts(data)
    if parts is None:
        return _raw_evidence_result(None, [
            _diagnostic(
                "raw-carrier-frontmatter-invalid",
                "Carrier bytes do not contain one supported, consistently delimited YAML frontmatter block.",
                carrier_path=raw_path,
            )
        ])
    frontmatter_bytes, body_bytes = parts
    try:
        frontmatter = frontmatter_bytes.decode("utf-8")
        body = body_bytes.decode("utf-8")
    except UnicodeDecodeError:
        return _raw_evidence_result(None, [
            _diagnostic("raw-carrier-not-utf8", "Carrier source bytes are not UTF-8.", carrier_path=raw_path)
        ])

    for key in ("atom_id", "version", "content_role", "status"):
        _, duplicate = _frontmatter_scalar(frontmatter, key)
        if duplicate is not None:
            return _raw_evidence_result(None, [
                _diagnostic(duplicate, "Carrier frontmatter repeats an identity-relevant scalar.", field=key)
            ])
    raw_atom_id, _ = _frontmatter_scalar(frontmatter, "atom_id")
    actual_id = _atom_identifier_from_raw_path(relative, raw_atom_id)
    raw_version, _ = _frontmatter_scalar(frontmatter, "version")
    if raw_version is None or not raw_version.isdigit() or int(raw_version) < 1:
        return _raw_evidence_result(None, [
            _diagnostic("raw-carrier-revision-invalid", "Carrier frontmatter lacks a positive integer version.")
        ])
    if actual_id != expected_id or int(raw_version) != expected_revision:
        return _raw_evidence_result(None, [
            _diagnostic(
                "raw-carrier-identity-mismatch",
                "Reread carrier identity or revision differs from Carrier evidence.",
                carrier_path=raw_path,
            )
        ])

    raw_role, _ = _frontmatter_scalar(frontmatter, "content_role")
    expected_role = getattr(carrier, "content_role", None)
    if not isinstance(raw_role, str) or raw_role != expected_role:
        return _raw_evidence_result(None, [
            _diagnostic(
                "raw-carrier-content-role-mismatch",
                "Reread carrier Content Role differs from the parsed Carrier.",
                carrier_path=raw_path,
            )
        ])
    raw_status, _ = _frontmatter_scalar(frontmatter, "status")
    expected_status = getattr(carrier, "status", None)
    if isinstance(expected_status, str) and raw_status != expected_status:
        return _raw_evidence_result(None, [
            _diagnostic(
                "raw-carrier-status-mismatch",
                "Reread carrier status differs from the parsed Carrier.",
                carrier_path=raw_path,
            )
        ])
    if getattr(carrier, "frontmatter", frontmatter) != frontmatter:
        return _raw_evidence_result(None, [
            _diagnostic(
                "raw-carrier-frontmatter-drift",
                "Parsed Carrier frontmatter differs from reread source bytes.",
                carrier_path=raw_path,
            )
        ])
    if getattr(carrier, "body", body) != body:
        return _raw_evidence_result(None, [
            _diagnostic(
                "raw-carrier-body-drift",
                "Parsed Carrier body differs from reread source bytes, including line endings.",
                carrier_path=raw_path,
            )
        ])

    section = _role_primary_section(raw_role)
    if section is None:
        return _raw_evidence_result(None, [
            _diagnostic(
                "raw-primary-section-unsupported-role",
                "The reread Content Role has no D539 role-primary section.",
                content_role=raw_role,
            )
        ])
    body_lines_bytes = body_bytes.splitlines(keepends=True)
    body_lines = [line.decode("utf-8") for line in body_lines_bytes]
    headers, _ = _raw_visible_headers(body_lines)
    matches = [header for header in headers if header[2].casefold() == section.casefold()]
    if not matches:
        return _raw_evidence_result(None, [
            _diagnostic(
                "raw-primary-section-missing",
                "The reread Carrier has no role-primary source section.",
                section=section,
            )
        ])
    primary_level = min(match[1] for match in matches)
    primary_matches = [match for match in matches if match[1] == primary_level]
    if len(primary_matches) != 1:
        return _raw_evidence_result(None, [
            _diagnostic(
                "raw-primary-section-cardinality",
                "The reread Carrier has more than one role-primary source section.",
                section=section,
                count=len(primary_matches),
            )
        ])
    heading_index, level, _ = primary_matches[0]
    end_index = len(body_lines)
    for candidate_index, candidate_level, _ in headers:
        if candidate_index > heading_index and candidate_level <= level:
            end_index = candidate_index
            break
    content_start_index = heading_index + 1
    if content_start_index >= end_index:
        return _raw_evidence_result(None, [
            _diagnostic(
                "raw-primary-section-empty",
                "The role-primary source section has no line span after its heading.",
                section=section,
            )
        ])

    # The byte stream before ``body_bytes`` contains every raw frontmatter and
    # delimiter line, so this is an absolute Carrier line number rather than a
    # body-relative location.  The contribution span is inclusive at both ends.
    body_offset = len(data) - len(body_bytes)
    first_body_line = data[:body_offset].count(b"\n") + 1
    span_bytes = b"".join(body_lines_bytes[content_start_index:end_index])
    source_evidence = {
        "atom_id": expected_id,
        "atom_revision": expected_revision,
        "carrier_path": raw_path,
        "carrier_sha256": actual_sha256,
        "contribution": {
            "kind": "primary_content",
            "section": section,
            "start_line": first_body_line + content_start_index,
            "end_line": first_body_line + end_index - 1,
            "text_sha256": hashlib.sha256(span_bytes).hexdigest(),
        },
    }
    return _raw_evidence_result(source_evidence, diagnostics)


def _contribution_result(
    *,
    text: str,
    section: str | None,
    diagnostics: list[dict[str, object]],
    carrier: object,
    location: Mapping[str, object] | None,
) -> dict[str, object]:
    source = _source(carrier, text, location)
    # The flat aliases keep this provenance easy to consume in a projection
    # while ``source`` remains the canonical grouped representation.
    return {
        "text": text,
        "section": section,
        "diagnostics": diagnostics,
        "source": source,
        "source_evidence": source["evidence"],
        "source_location": source["location"],
        "source_digest": source["digest"],
    }


def primary_contribution(carrier: object) -> dict[str, object]:
    """Read exactly one role-primary Markdown section from ``carrier``.

    RMED carriers use ``Claim`` and Operations carriers use ``Operation``.
    Fenced examples are deliberately invisible: an example must not admit an
    Entity definition into the graph.
    """

    section = _role_primary_section(getattr(carrier, "content_role", None))
    if section is None:
        return _contribution_result(
            text="",
            section=None,
            diagnostics=[
                _diagnostic(
                    "definition-content-role-unsupported",
                    "The carrier Content Role has no definition-bearing primary section.",
                    content_role=getattr(carrier, "content_role", None),
                )
            ],
            carrier=carrier,
            location=None,
        )

    body = getattr(carrier, "body", "")
    if not isinstance(body, str):
        return _contribution_result(
            text="",
            section=section,
            diagnostics=[
                _diagnostic("definition-body-invalid", "The carrier body is not text.")
            ],
            carrier=carrier,
            location=None,
        )

    headers, visible = _visible_headers_and_lines(body)
    matches = [header for header in headers if header[2].casefold() == section.casefold()]
    if not matches:
        return _contribution_result(
            text="",
            section=section,
            diagnostics=[
                _diagnostic(
                    "definition-primary-section-missing",
                    "The carrier has no role-primary section.",
                    section=section,
                )
            ],
            carrier=carrier,
            location=None,
        )

    primary_level = min(match[1] for match in matches)
    primary_matches = [match for match in matches if match[1] == primary_level]
    if len(primary_matches) != 1:
        return _contribution_result(
            text="",
            section=section,
            diagnostics=[
                _diagnostic(
                    "definition-primary-section-cardinality",
                    "A carrier must have exactly one role-primary section.",
                    section=section,
                    count=len(primary_matches),
                )
            ],
            carrier=carrier,
            location=None,
        )

    start, level, _ = primary_matches[0]
    body_lines = body.splitlines()
    end = len(body_lines)
    for heading_start, heading_level, _ in headers:
        if heading_start > start and heading_level <= level:
            end = heading_start
            break
    text = "\n".join(
        line for index, line in enumerate(body_lines[start + 1 : end], start + 1) if visible[index]
    ).strip()
    diagnostics: list[dict[str, object]] = []
    if not text:
        diagnostics.append(
            _diagnostic(
                "definition-primary-section-empty",
                "The role-primary section is empty.",
                section=section,
            )
        )
    return _contribution_result(
        text=text,
        section=section,
        diagnostics=diagnostics,
        carrier=carrier,
        location={
            "section": section,
            "heading_line": start + 1,
            "start_line": start + 2,
            "end_line": end,
        },
    )


def _definition_candidate(text: str) -> tuple[str | None, str | None, list[dict[str, object]]]:
    """Return the defined terminal Term and text after the one bold marker."""

    markers = list(_BOLD_MEANS.finditer(text))
    if not markers:
        diagnostics: list[dict[str, object]] = []
        if _LEGACY_TYPE_DEFINITION.search(text):
            diagnostics.append(
                _diagnostic(
                    "definition-legacy-type-definition-unsupported",
                    "Legacy typeDefinition notation is not a current Core definition claim.",
                )
            )
        elif _PLAIN_MEANS.search(text):
            diagnostics.append(
                _diagnostic(
                    "definition-means-not-bold",
                    "A definition candidate must use the current bold **means** marker.",
                )
            )
        return None, None, diagnostics
    if len(markers) != 1:
        return None, None, [
            _diagnostic(
                "definition-means-cardinality",
                "A definition claim must contain exactly one bold **means** marker.",
                count=len(markers),
            )
        ]

    marker = markers[0]
    left = text[: marker.start()].strip()
    # Current Core definitions introduce their subject directly.  A preceding
    # blank paragraph cannot be part of that subject phrase.
    if "\n\n" in left:
        left = left.rsplit("\n\n", 1)[-1].strip()
    left = re.sub(r"^(?:the\s+Term\s+|the\s+|an?\s+)", "", left, flags=re.IGNORECASE)
    left = left.strip().strip("`*_ ")
    definition = text[marker.end() :].strip()
    diagnostics = []
    if not left:
        diagnostics.append(
            _diagnostic("definition-term-missing", "The **means** marker has no defined Term before it.")
        )
    if not re.search(r"\w", definition, flags=re.UNICODE):
        diagnostics.append(
            _diagnostic("definition-text-empty", "The **means** marker has no definition text after it.")
        )
    return (left or None), definition, diagnostics


def _governs_rows(governs: Sequence[object]) -> list[object]:
    rows: list[object] = []
    for row in governs:
        kind = getattr(row, "kind", None)
        if isinstance(kind, str) and kind.strip().upper() == "GOVERNS":
            rows.append(row)
    return rows


def _terminal_term(subject_path: object) -> tuple[str | None, list[dict[str, object]]]:
    if not isinstance(subject_path, str) or not subject_path.strip():
        return None, [
            _diagnostic("definition-governed-target-invalid", "The GOVERNS Subject Path is empty or invalid.")
        ]
    parts = [part.strip() for part in subject_path.strip().split("/")]
    if any(not part for part in parts):
        return None, [
            _diagnostic(
                "definition-governed-target-invalid",
                "The GOVERNS Subject Path has an empty component.",
                subject_path=subject_path,
            )
        ]
    terminal = parts[-1]
    if ":" in terminal:
        qualifier, value = (item.strip() for item in terminal.rsplit(":", 1))
        if not qualifier or not value:
            return None, [
                _diagnostic(
                    "definition-governed-target-invalid",
                    "The terminal qualified Subject Path component is invalid.",
                    subject_path=subject_path,
                )
            ]
        terminal = value
    return terminal, []


def _relation_evidence(row: object) -> dict[str, object]:
    evidence_method = getattr(row, "evidence", None)
    if not callable(evidence_method):
        return {}
    try:
        value = evidence_method()
    except Exception:  # pragma: no cover - defensive boundary for duck types
        return {}
    return dict(value) if isinstance(value, Mapping) else {}


def assess_definition(carrier: object, governs: Sequence[object]) -> dict[str, object]:
    """Assess whether an Active carrier currently defines its GOVERNS target.

    This function is intentionally an assessor, not an admission mechanism:
    it reports only the terminal Term already named by the one existing GOVERNS
    relation and never derives additional Terms from path components.
    """

    contribution = primary_contribution(carrier)
    diagnostics = list(contribution["diagnostics"])
    text = contribution["text"]
    term, definition_text, candidate_diagnostics = _definition_candidate(text)
    diagnostics.extend(candidate_diagnostics)
    # Multiple primary sections are themselves an ambiguous candidate: their
    # hidden text must not downgrade that malformed definition to a silent
    # non-definition.
    candidate_signalled = (
        bool(_BOLD_MEANS.search(text))
        or bool(candidate_diagnostics)
        or any(diagnostic["code"] == "definition-primary-section-cardinality" for diagnostic in diagnostics)
    )

    rows = _governs_rows(governs)
    subject_path: str | None = None
    governed_term: str | None = None
    relation_evidence: dict[str, object] | None = None
    if candidate_signalled:
        if len(rows) != 1:
            diagnostics.append(
                _diagnostic(
                    "definition-governs-cardinality",
                    "A definition candidate must have exactly one GOVERNS relation.",
                    count=len(rows),
                )
            )
        else:
            subject = getattr(rows[0], "subject_path", None)
            if isinstance(subject, str):
                subject_path = subject
            governed_term, target_diagnostics = _terminal_term(subject)
            diagnostics.extend(target_diagnostics)
            relation_evidence = _relation_evidence(rows[0])

    active = isinstance(getattr(carrier, "status", None), str) and getattr(carrier, "status").strip().casefold() == "active"
    if candidate_signalled and not active:
        diagnostics.append(
            _diagnostic(
                "definition-authority-inactive",
                "Only an Active carrier can supply a recognized definition.",
                status=getattr(carrier, "status", None),
            )
        )

    if not candidate_signalled:
        state = "not_definition"
    elif any(
        diagnostic["code"]
        in {
            "definition-primary-section-missing",
            "definition-primary-section-cardinality",
            "definition-primary-section-empty",
            "definition-body-invalid",
            "definition-content-role-unsupported",
            "definition-legacy-type-definition-unsupported",
            "definition-means-not-bold",
            "definition-means-cardinality",
            "definition-term-missing",
            "definition-text-empty",
            "definition-governs-cardinality",
            "definition-governed-target-invalid",
            "definition-authority-inactive",
        }
        for diagnostic in diagnostics
    ):
        state = "unsupported_candidate"
    elif term != governed_term:
        diagnostics.append(
            _diagnostic(
                "definition-terminal-term-mismatch",
                "The defined Term does not exactly match the terminal GOVERNS Term.",
                defined_term=term,
                governed_term=governed_term,
                subject_path=subject_path,
            )
        )
        state = "target_mismatch"
    else:
        state = "recognized"

    evidence = {
        "contribution": contribution["source"],
        "governs": relation_evidence,
    }
    return {
        "state": state,
        "term": term,
        "subject_path": subject_path,
        "contribution": contribution,
        "definition_text": definition_text,
        "evidence": evidence,
        "diagnostics": diagnostics,
    }
