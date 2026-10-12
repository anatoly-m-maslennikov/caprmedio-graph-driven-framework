"""Prepare, but never apply, the approved five-definition grammar patch.

This ad-hoc preview is intentionally create-only.  Its source bytes are
current-pinned inputs; applying its proposed bytes is reserved for Root after a
fresh pin check and independent review.
"""
from __future__ import annotations

import argparse
import datetime as dt
from functools import lru_cache
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[5]
STAGE2 = ".caprmedio_caprmedio/_projection/core-entity-review/stage2"
SOURCE_ROOT = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL"
PACKET_JSON = f"{STAGE2}/grammar-decision.packet.json"
PACKET_MD = f"{STAGE2}/grammar-decision.packet.md"
APPROVAL = f"{STAGE2}/grammar-decision.operator-answer.json"
SETTINGS = ".caprmedio_caprmedio/caprmedio_project_settings.toml"
OUTPUT = f"{STAGE2}/grammar-adoption.preview.json"

PACKET_SHA256 = "4e3636cc01e40801c8f6b8beec9632e80fee3187524bf052656cec9a4e6035ab"
APPROVAL_SHA256 = "396dd826016ff7f021960f74345298bdb583124374249ce07c5cdb3edf1fc0eb"
SUCCESSOR_ID = "CA-R-1931"
SUCCESSOR_FILENAME = "CA-R-1931-CORE_META_MODEL--use-subject-path-separators-for-broader-to-narrower-and-bearer-to-dependent.md"

REVISED_CLAIMS = {
    "CA-R-1321": """a Subject Expression **means** a reference **to** **`=1`** Entity formed from Term references **and** registered relation syntax. **every** named component, including the initial target name, Property names, **and** named allowed values, references a Term; `/`, `.`, **and** `:` are syntax, **not** Terms. `@` is outside Subject syntax. the expression identifies the target, **not** the Atom's Subject Relation **to** it.""",
    "CA-R-1324": """a Term name **must not** contain `/`, `.`, **or** `:`. `@` is outside Subject syntax **and** is **not** a Subject Expression separator.""",
    "CA-M-228": """**to** write a Subject Expression, start with a canonical Entity reference **and** apply `/` in broader-to-narrower order, `.` in bearer-to-dependent order, **and** `:` in Property-to-allowed-value order. resolve **every** named component, including names **before** **and** **after** the separators, as a Term reference under CA-R-1321. `.` retains the mechanical native fact Dependent IS_BORNE_BY Bearer, **and** `:` retains AllowedValue IS_ALLOWED_VALUE_OF Property; `/` admits no native Subject or Entity relation. the resulting qualified path identifies its existing canonical target **without** copying it; connecting the Atom **to** that target through GOVERNS **or** DEPENDS_ON creates the Subject Relation, **not** another target Entity.""",
    "CA-E-383": """the Evaluation **must** reject a Subject Expression **if**

- `/` does **not** express the approved broader-to-narrower Subject Path profile,
- `.` does **not** encode **`=1`** valid bearer edge from the following Dependent Entity occurrence **to** the immediately preceding bearer occurrence,
- `:` does **not** express **`=1`** admitted IS_ALLOWED_VALUE_OF qualification under CA-R-1436-CORE_META_MODEL-CORE-REQUIREMENT--define-is-allowed-value-of,
- allowed-value admission is treated as assignment **to** a particular Property occurrence **or** as determining its cardinality,
- a Dependent Entity occurrence lacks **`=1`** immediate bearer,
- a reusable Term is rejected **only** for changing ordinal position,
- a Governed Term begins with a lowercase letter,
- a named component fails **to** resolve **to** a Term under CA-R-1321-CORE_META_MODEL-CORE--define-subject-expression,
- an ordinary General Term is substituted for a required Term reference,
- a Term name **contains** `/`, `.`, **or** `:`,
- `@` is used as a Subject token,
- a complete composite Subject Expression is classified as one Term,
- **or** a registered CCE Operator is redefined as a Governed Term **or** Scope Unit Name.""",
}

E383_DETAILS = """### Term-component cases

`Artifact/Atom.Status: Active` **must** pass the component check **only when** its four named Terms **and** exact qualified target are admitted. `/`, `.`, **and** `:` contribute no Term nodes. an unresolved named component **must** fail the source-reference check; the diagnostic **must** preserve the unresolved reference **without** supplying an invented definition. a complete composite path **must not** be admitted as **`=1`** Term merely because it resolves **to** **`=1`** Entity.

`Atom/Content Role: Requirement/Type: Demand` is retained only as a legacy five-component fixture; it does **not** define an approved all-dot role conjunction or selector grammar."""

SUCCESSOR_CLAIM = """**in** a Subject Path, `/` **must** separate a broader component from its following narrower component; `.` **must** separate a bearer component from its following dependent component; `:` **must** separate a Property component from its following allowed-value component; **and** `@` is **not** Subject syntax. a Subject Path still resolves **`=1`** canonical target **and** does **not** create target identities. the mechanical native fact for `.` is Dependent IS_BORNE_BY Bearer; for `:` it is AllowedValue IS_ALLOWED_VALUE_OF Property. `/` admits **no** native Subject **or** Entity relation; any later Terms-Graph binding to NARROWER_THAN remains separately governed."""
SUCCESSOR_SUMMARY = "Use Subject Path Separators for Broader-to-Narrower and Bearer-to-Dependent"


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def relative_path(root: Path, value: str) -> Path:
    path = (root / value).resolve()
    require(path.is_relative_to(root.resolve()), f"path escapes project: {value}")
    return path


def raw_file(root: Path, relative: str) -> bytes:
    path = relative_path(root, relative)
    require(path.is_file(), f"missing input: {relative}")
    return path.read_bytes()


def pinned_json(root: Path, relative: str, expected: str) -> dict[str, Any]:
    raw = raw_file(root, relative)
    require(digest(raw) == expected, f"stale pinned input: {relative}")
    value = json.loads(raw)
    require(isinstance(value, dict), f"object required: {relative}")
    return value


def split_atom(raw: bytes) -> tuple[str, str]:
    text = raw.decode("utf-8")
    require(text.startswith("---\n"), "YAML frontmatter start required")
    closing = text.find("\n---\n", 4)
    require(closing >= 0, "YAML frontmatter end required")
    return text[4:closing], text[closing + 5:]


def front_value(frontmatter: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+)$", frontmatter)
    require(match is not None, f"missing frontmatter key: {key}")
    return match.group(1).strip().strip('"')


def replace_front_value(frontmatter: str, key: str, value: str, *, quoted: bool = True) -> str:
    pattern = re.compile(rf"(?m)^({re.escape(key)}:\s*).+$")
    replacement = f'"{value}"' if quoted else value
    result, count = pattern.subn(rf"\g<1>{replacement}", frontmatter, count=1)
    require(count == 1, f"frontmatter key not unique: {key}")
    return result


def replace_section(body: str, heading: str, replacement: str) -> str:
    start = body.find(heading + "\n")
    require(start >= 0, f"missing section: {heading}")
    next_heading = body.find("\n## ", start + len(heading) + 1)
    require(next_heading >= 0, f"section must have following heading: {heading}")
    return body[:start] + heading + "\n\n" + replacement + "\n" + body[next_heading:]


def replace_final_section(body: str, heading: str, replacement: str) -> str:
    start = body.find(heading + "\n")
    require(start >= 0, f"missing final section: {heading}")
    require(body.find("\n## ", start + len(heading) + 1) < 0, f"final section is not final: {heading}")
    return body[:start] + heading + "\n\n" + replacement + "\n"


def section_value(body: str, heading: str) -> str:
    start = body.find(heading + "\n")
    require(start >= 0, f"missing section: {heading}")
    next_heading = body.find("\n## ", start + len(heading) + 1)
    require(next_heading >= 0, f"section must have following heading: {heading}")
    return body[start:next_heading]


def atom_bytes(frontmatter: str, body: str) -> bytes:
    return f"---\n{frontmatter}\n---\n{body}".encode("utf-8")


def archive_target(relative: str, old_version: int) -> str:
    path = Path(relative)
    return (path.parent / "archive" / f"{path.stem}@{old_version}{path.suffix}").as_posix()


def metadata_helper(root: Path) -> Any:
    helper_path = root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/artifact_metadata.py"
    helper_directory = str(helper_path.parent)
    if helper_directory not in sys.path:
        sys.path.insert(0, helper_directory)
    spec = importlib.util.spec_from_file_location("caprmedio_artifact_metadata", helper_path)
    require(spec is not None and spec.loader is not None, "project timestamp helper unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def configured_timestamp(root: Path) -> str:
    helper = metadata_helper(root)
    timezone = helper.configured_timezone(root)
    moment = dt.datetime.now().astimezone() if timezone is None else dt.datetime.now(timezone)
    return moment.strftime("%Y-%m-%d %H:%M:%S %z")


def source_specs(packet: dict[str, Any]) -> list[dict[str, Any]]:
    replacement = packet.get("replacement_candidate")
    changes = packet.get("minimum_five_changes")
    require(isinstance(replacement, dict) and isinstance(changes, list) and len(changes) == 5, "five-change packet shape")
    replacement_path = "04_requirement/CA-R-1204-CORE_META_MODEL--use-subject-path-slash-only-for-bearer-qualification.md"
    specs = [{
        "atom_id": replacement["predecessor_atom_id"],
        "version": replacement["predecessor_version"],
        "path": f"{SOURCE_ROOT}/{replacement_path}",
        "sha256": replacement["predecessor_sha256"],
        "operation": "replacement",
    }]
    for item in changes[1:]:
        specs.append({
            "atom_id": item["atom_id"],
            "version": item["current_version"],
            "path": f"{SOURCE_ROOT}/{item['path']}",
            "sha256": item["sha256"],
            "operation": "revision",
        })
    require([item["atom_id"] for item in specs] == ["CA-R-1204", "CA-R-1321", "CA-R-1324", "CA-M-228", "CA-E-383"], "approved source identity set")
    return specs


@lru_cache(maxsize=4)
def discovered_atom_ids(root: Path) -> frozenset[str]:
    result = subprocess.run(
        ["rg", "-o", r'^atom_id:\s*["\']?CA-R-[0-9]+["\']?\s*$', ".caprmedio_caprmedio", "--glob", "*.md"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    require(result.returncode in {0, 1}, "global Atom-ID uniqueness check failed")
    return frozenset(re.findall(r"CA-R-[0-9]+", result.stdout))


def ensure_successor_id_unoccupied(atom_ids: set[str] | frozenset[str]) -> None:
    require(SUCCESSOR_ID not in atom_ids, f"successor ID collision: {SUCCESSOR_ID}")


def revision_bytes(old: bytes, atom_id: str, next_version: int, timestamp: str) -> bytes:
    frontmatter, body = split_atom(old)
    require(front_value(frontmatter, "atom_id") == atom_id, f"atom identity mismatch: {atom_id}")
    require(int(front_value(frontmatter, "version")) + 1 == next_version, f"version sequence mismatch: {atom_id}")
    frontmatter = replace_front_value(frontmatter, "version", str(next_version), quoted=False)
    frontmatter = replace_front_value(frontmatter, "updated_at", timestamp)
    if atom_id == "CA-E-383":
        require(frontmatter.count("- CA-R-1204") == 1, "CA-E-383 predecessor binding missing or duplicated")
        frontmatter = frontmatter.replace("- CA-R-1204", f"- {SUCCESSOR_ID}")
    body = replace_section(body, "## Claim", REVISED_CLAIMS[atom_id])
    if atom_id == "CA-E-383":
        body = replace_final_section(body, "## Details", E383_DETAILS)
    return atom_bytes(frontmatter, body)


def successor_bytes(old: bytes, timestamp: str) -> bytes:
    frontmatter, body = split_atom(old)
    require(front_value(frontmatter, "atom_id") == "CA-R-1204", "replacement predecessor identity")
    frontmatter = replace_front_value(frontmatter, "atom_id", SUCCESSOR_ID)
    frontmatter = replace_front_value(frontmatter, "version", "1", quoted=False)
    frontmatter = replace_front_value(frontmatter, "updated_at", timestamp)
    body = replace_section(body, "# Summary", SUCCESSOR_SUMMARY)
    body = replace_section(body, "## Claim", SUCCESSOR_CLAIM)
    return atom_bytes(frontmatter, body)


def source_pin(root: Path, spec: dict[str, Any]) -> tuple[dict[str, Any], bytes]:
    raw = raw_file(root, spec["path"])
    require(digest(raw) == spec["sha256"], f"stale approved source: {spec['atom_id']}")
    frontmatter, _ = split_atom(raw)
    require(front_value(frontmatter, "atom_id") == spec["atom_id"], f"source ID mismatch: {spec['atom_id']}")
    require(int(front_value(frontmatter, "version")) == spec["version"], f"source version mismatch: {spec['atom_id']}")
    return {key: spec[key] for key in ("atom_id", "version", "path", "sha256")}, raw


def replacement_effect(spec: dict[str, Any], old: bytes, timestamp: str) -> dict[str, Any]:
    successor_path = (Path(spec["path"]).parent / SUCCESSOR_FILENAME).as_posix()
    successor = successor_bytes(old, timestamp)
    return {
        "atom_id": "CA-R-1204",
        "operation": "replace_with_new_id",
        "approved_predecessor": {"path": spec["path"], "sha256": digest(old), "version": 14, "content_utf8": old.decode("utf-8")},
        "history": {"operation": "move_exact_bytes", "from": spec["path"], "to": archive_target(spec["path"], 14), "sha256": digest(old), "content_utf8": old.decode("utf-8")},
        "successor": {"atom_id": SUCCESSOR_ID, "version": 1, "path": successor_path, "sha256": digest(successor), "content_utf8": successor.decode("utf-8")},
        "allowed_changes": ["new ID", "Summary", "Claim", "Version", "Updated At"],
    }


def revision_effect(spec: dict[str, Any], old: bytes, timestamp: str) -> dict[str, Any]:
    updated = revision_bytes(old, spec["atom_id"], spec["version"] + 1, timestamp)
    return {
        "atom_id": spec["atom_id"],
        "operation": "revise_active_atom",
        "active": {
            "path": spec["path"],
            "old_version": spec["version"],
            "new_version": spec["version"] + 1,
            "old_sha256": digest(old),
            "new_sha256": digest(updated),
            "old_content_utf8": old.decode("utf-8"),
            "new_content_utf8": updated.decode("utf-8"),
        },
        "history": {"operation": "create_exact_prior_revision", "path": archive_target(spec["path"], spec["version"]), "sha256": digest(old), "content_utf8": old.decode("utf-8")},
        "allowed_changes": (["Claim", "Details", "Version", "Updated At", "relations.evaluation_for CA-R-1204 -> CA-R-1931"] if spec["atom_id"] == "CA-E-383" else ["Claim", "Version", "Updated At"]),
    }


def assemble_preview(root: Path, timestamp: str) -> dict[str, Any]:
    require(re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [+-]\d{4}", timestamp) is not None, "timezone-qualified timestamp required")
    approval = pinned_json(root, APPROVAL, APPROVAL_SHA256)
    packet = pinned_json(root, PACKET_JSON, PACKET_SHA256)
    require(approval.get("decision") == "approved_five_definition_grammar_exception_in_step_1", "five-change approval absent")
    require(approval.get("packet", {}).get("json", {}).get("sha256") == PACKET_SHA256, "approval packet binding stale")
    require(approval.get("notation") == {"/": "broader_to_narrower", ".": "bearer_to_dependent", ":": "property_to_allowed_value", "@": "display_or_carrier_only_not_subject_syntax"}, "approved notation changed")
    specs = source_specs(packet)
    requirement_ids = discovered_atom_ids(root)
    ensure_successor_id_unoccupied(requirement_ids)
    requirement_numbers = [int(value.removeprefix("CA-R-")) for value in requirement_ids]
    require(requirement_numbers and max(requirement_numbers) == 1930, "CA-R-1931 is not the next globally unused Requirement ID")
    source_pins: list[dict[str, Any]] = []
    effects: list[dict[str, Any]] = []
    for spec in specs:
        pin, old = source_pin(root, spec)
        source_pins.append(pin)
        if spec["operation"] == "replacement":
            effects.append(replacement_effect(spec, old, timestamp))
        else:
            effects.append(revision_effect(spec, old, timestamp))
    return {
        "schema_version": 1,
        "task_id": "CA-P-2059",
        "non_authoritative": True,
        "preview_only": True,
        "source_writes": "not_performed",
        "native_admission": "not_performed",
        "subject_migration": "not_performed",
        "timestamp": {"value": timestamp, "timezone_source": f"{SETTINGS} [artifact_timestamps].timezone via artifact_metadata.configured_timezone", "status": "dry_run_illustrative; Root must obtain a fresh timestamp and recompute effect hashes immediately before applying."},
        "evidence_pins": [
            {"path": APPROVAL, "sha256": APPROVAL_SHA256},
            {"path": PACKET_JSON, "sha256": PACKET_SHA256},
            {"path": PACKET_MD, "sha256": digest(raw_file(root, PACKET_MD))},
            {"path": SETTINGS, "sha256": digest(raw_file(root, SETTINGS))},
        ],
        "source_pins": source_pins,
        "successor_id_check": {"successor_id": SUCCESSOR_ID, "existing_atom_id_matches": 0, "prior_global_requirement_max": max(requirement_numbers)},
        "planned_effects": effects,
        "limits": [
            "Only the five approved grammar definitions are represented.",
            "All active Subjects, existing summaries/scopes except the approved new-ID successor summary, and other metadata remain unchanged.",
            "Archive entries preserve exact prior revision bytes; predecessor/successor history is not an active Atom relation.",
            "No Journal entry, native slash relation, Core write, parser change, source migration, MCP, FPF, or Git action is performed by this preview.",
        ],
    }


def validate_preview(document: dict[str, Any], root: Path = ROOT) -> None:
    require(document.get("schema_version") == 1 and document.get("task_id") == "CA-P-2059", "preview identity")
    require(document.get("non_authoritative") is True and document.get("preview_only") is True, "preview-only boundary")
    require(document.get("source_writes") == document.get("native_admission") == document.get("subject_migration") == "not_performed", "no authoritative effects")
    timestamp = document.get("timestamp", {}).get("value")
    require(isinstance(timestamp, str), "preview timestamp")
    expected = assemble_preview(root, timestamp)
    for key in ("evidence_pins", "source_pins", "successor_id_check", "planned_effects", "limits"):
        require(document.get(key) == expected.get(key), f"preview differs from pinned effect set: {key}")
    effects = document["planned_effects"]
    require(len(effects) == 5 and [item["atom_id"] for item in effects] == ["CA-R-1204", "CA-R-1321", "CA-R-1324", "CA-M-228", "CA-E-383"], "five approved changes only")
    require(effects[0]["successor"]["atom_id"] == SUCCESSOR_ID and effects[0]["successor"]["version"] == 1, "successor identity/version")
    for item in effects[1:]:
        active = item["active"]
        require(active["new_version"] == active["old_version"] + 1, "one revision increment")
        require(item["history"]["content_utf8"] == active["old_content_utf8"], "exact prior bytes preserved")
    require("relations.evaluation_for CA-R-1204 -> CA-R-1931" in effects[-1]["allowed_changes"], "evaluation successor binding")


def serialise(document: dict[str, Any]) -> bytes:
    return (json.dumps(document, indent=2, sort_keys=True) + "\n").encode("utf-8")


def output_path(root: Path, supplied: str) -> Path:
    candidate = Path(supplied)
    if not candidate.is_absolute():
        candidate = root / candidate
    candidate = candidate.resolve()
    require(candidate.is_relative_to(root.resolve()), "output must remain in project")
    return candidate


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timestamp", help="Timezone-qualified illustrative timestamp; default uses current project-local configuration.")
    parser.add_argument("--write", action="store_true", help="Create the preview once; never overwrite it.")
    parser.add_argument("--output", default=OUTPUT, help="Repository-relative preview output path.")
    args = parser.parse_args()
    try:
        timestamp = args.timestamp or configured_timestamp(ROOT)
        document = assemble_preview(ROOT, timestamp)
        validate_preview(document)
        raw = serialise(document)
        target = output_path(ROOT, args.output)
        result = {"mode": "write" if args.write else "preview", "output": str(target.relative_to(ROOT)), "sha256": digest(raw), "timestamp": timestamp, "effects": 5, "revisions": 4, "replacement": SUCCESSOR_ID}
        if args.write:
            require(not target.exists(), f"create-only output already exists: {target.relative_to(ROOT)}")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
        print(json.dumps(result, sort_keys=True))
    except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"outcome": "FAIL", "reason": str(error)}, sort_keys=True))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
