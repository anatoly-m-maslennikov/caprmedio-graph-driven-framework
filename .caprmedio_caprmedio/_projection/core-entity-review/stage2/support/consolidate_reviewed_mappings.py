#!/usr/bin/env python3
"""Create-only CA-P-2086 current-frontier working Subject mapping drafts."""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
import sys
import tomllib
from typing import Any, Iterable

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from inventory_current_subjects import (  # strict Core parser and frontier rules
    ATOM_ID,
    FILENAME_ATOM_ID,
    ROLE_DIRS,
    ROLES,
    SUBJECT_FIELDS,
    UPDATED_AT,
    CarrierError,
    ROOT,
    checked_relative_path,
    directory_role,
    parse_carrier,
    source_files,
    updated_at,
)

STAGE = Path(".caprmedio_caprmedio/_projection/core-entity-review/stage2")
BASELINE = STAGE / "current-subjects.mapping-ledger.json"
DRIFT = STAGE / "current-grammar-source-drift.json"
CANDIDATE = Path(".caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.entity-graph.candidate.json")
DECISION_RECORD = STAGE / "operator.subject-decisions.2026-10-11.json"
CONTRACTS = (
    STAGE / "current-subjects.contract.md",
    STAGE / "current-subjects.review.contract.md",
    STAGE / "current-subjects.supplements.contract.md",
    STAGE / "working-ledger.contract.md",
    STAGE / "working-ledger.followups-2094-2099.contract.md",
    STAGE / "working-ledger.followups-2103-2108.contract.md",
    STAGE / "working-ledger.followups-2112-2117.contract.md",
    STAGE / "working-ledger.followups-2121-2128.contract.md",
    STAGE / "working-ledger.followups-2132-2139.contract.md",
    STAGE / "working-ledger.core-only-successor-2143.contract.md",
)
WORKING = STAGE / "working-ledger"
LEDGER = WORKING / "working-mapping-ledger.json"
FRONTIER = WORKING / "source-frontier.json"
DIAGNOSTICS = WORKING / "diagnostics.json"
STRUCTURE = Path(".caprmedio_caprmedio/project_structure.toml")

# Each record is consumed only when the recorded independently accepted output
# pin equals the actual current file.  CA-P-2058 is validation-only.
LAYER_SPECS = (
    ("CA-P-2048", STAGE / "supplements/substance.review.json", "substance"),
    ("CA-P-2072", STAGE / "semantic-reviews/task-2072.review.json", "semantic"),
    ("CA-P-2073", STAGE / "semantic-reviews/task-2073.review.json", "semantic"),
    ("CA-P-2074", STAGE / "semantic-reviews/task-2074.review.json", "semantic"),
    ("CA-P-2075", STAGE / "semantic-reviews/task-2075.review.json", "semantic"),
    ("CA-P-2076", STAGE / "semantic-reviews/task-2076.review.json", "semantic"),
    ("CA-P-2078", STAGE / "semantic-reviews/task-2078.research.json", "research"),
    ("CA-P-2079", STAGE / "semantic-reviews/task-2079.research.json", "research"),
    ("CA-P-2080", STAGE / "semantic-reviews/task-2080.research.json", "research"),
    ("CA-P-2082", STAGE / "semantic-reviews/task-2082.research.json", "research"),
    ("CA-P-2083", STAGE / "semantic-reviews/task-2083.research.json", "research"),
    ("CA-P-2084", STAGE / "semantic-reviews/task-2084.research.json", "research"),
    ("CA-P-2085", STAGE / "semantic-reviews/task-2085.research.json", "research"),
)
ACTOR_SUBSET = STAGE / "semantic-reviews/task-2058.accepted-subset.json"
CURRENT_GRAMMAR_TASK = "CA-P-2087"
CURRENT_GRAMMAR_REPORT = STAGE / "semantic-reviews/current-grammar-subjects.review.json"
@dataclass(frozen=True)
class ResearchLayerGroup:
    """One fixed accepted research group, not a discovery mechanism."""

    label: str
    manifest: Path
    manifest_sha256: str
    registration_commit: str
    historical_working_pin: dict[str, str]
    specifications: tuple[tuple[str, Path, str, int, int, int], ...]
    expected_rows: int


FOLLOWUP_HISTORICAL_WORKING_PIN = {
    "path": (WORKING / "working-mapping-ledger.json").as_posix(),
    "sha256": "9c16ba32e74cb51cbd4c63cf3b938a57f614f55ca2650d54af2d6ed15b92088d",
}
FOLLOWUP_LAYER_SPECS = (
    ("CA-P-2094", STAGE / "semantic-reviews/task-2094.research.json", "265356c22829b6416f1d27c57969f509fec260f1e46dce99d8a7f3cc0219e3b5", 27, 21, 6),
    ("CA-P-2095", STAGE / "semantic-reviews/task-2095.research.json", "42a578818395cbe4e2f5fe5d997745058af39ff38ab02a3f84d8096cb674690d", 28, 8, 20),
    ("CA-P-2096", STAGE / "semantic-reviews/task-2096.research.json", "fa53f20f59f5bb9b75223fa407e8233a00d74ae2a962002657d30713da7fd1e7", 41, 21, 20),
    ("CA-P-2097", STAGE / "semantic-reviews/task-2097.research.json", "7a24becd960411a50eeb6ef344df0599c817820376453cdfbc6511c15495ae04", 25, 14, 11),
    ("CA-P-2098", STAGE / "semantic-reviews/task-2098.research.json", "ab4acfbfdf3ea8addfdfee7fc4502b5e84a4808ec91499da82dfd9bebc3784b2", 32, 1, 31),
    ("CA-P-2099", STAGE / "semantic-reviews/task-2099.research.json", "0e50e15645a4d56385a240ca47179b1c708ec839aecd4a81c4acfcdc13f4e69b", 27, 15, 12),
)
FOLLOWUP_GROUP = ResearchLayerGroup(
    label="CA-P-2094–2099",
    manifest=STAGE / "semantic-reviews/followups-2094-2099.inputs.json",
    manifest_sha256="5e9ed02cadeccf6b46dcea33593db65c8540c7cf77ce984a3d2502d8f00c3a3d",
    registration_commit="da5074e2d2ac47d44f001526f0e88c947f963ef2",
    historical_working_pin=FOLLOWUP_HISTORICAL_WORKING_PIN,
    specifications=FOLLOWUP_LAYER_SPECS,
    expected_rows=180,
)
SUBJECT_FAMILY_HISTORICAL_WORKING_PIN = {
    "path": (WORKING / "working-mapping-ledger.json").as_posix(),
    "sha256": "50ab0114669787dba6331b58f8054cd8fb33b5abbed33df6fbf5b52df53923fa",
}
SUBJECT_FAMILY_LAYER_SPECS = (
    ("CA-P-2103", STAGE / "semantic-reviews/task-2103.research.json", "22db7aa281823d7e01c58454bcc52ee7060d5ffe24a12396e62e6e952f28071c", 26, 23, 3),
    ("CA-P-2104", STAGE / "semantic-reviews/task-2104.research.json", "d19ad7f585610a10910c4b0355aaca1743a670adb3b56c96114a0cfd5d35a5f4", 31, 17, 14),
    ("CA-P-2105", STAGE / "semantic-reviews/task-2105.research.json", "40a2d1c26cc6b617b49ac109172c99996de6727401e99326d17bf89f2adf492e", 41, 22, 19),
    ("CA-P-2106", STAGE / "semantic-reviews/task-2106.research.json", "109edfd87f6f788658a210e561e034275dff6b49df34357b5d386340ba3e8204", 25, 9, 16),
    ("CA-P-2107", STAGE / "semantic-reviews/task-2107.research.json", "149a9a3c35f2c4c3a08733e9dac790093d4c592da428f5bbfd262fbb396c458a", 26, 4, 22),
    ("CA-P-2108", STAGE / "semantic-reviews/task-2108.research.json", "eb40f1fc810edb418f3acdeec8ce798837109264e45a966d348c86b810945da5", 34, 25, 9),
)
SUBJECT_FAMILY_GROUP = ResearchLayerGroup(
    label="CA-P-2103–2108",
    manifest=STAGE / "semantic-reviews/followups-2103-2108.inputs.json",
    manifest_sha256="7babc00405598a0af98c21bc2de69d4db04e9d59672d9746aa048f2f17a44ef3",
    registration_commit="9edbdb2156d7a2949ca4d11c6d86e511c8bf9cfb",
    historical_working_pin=SUBJECT_FAMILY_HISTORICAL_WORKING_PIN,
    specifications=SUBJECT_FAMILY_LAYER_SPECS,
    expected_rows=183,
)
FINAL_SUBJECT_FAMILY_HISTORICAL_WORKING_PIN = {
    "path": (WORKING / "working-mapping-ledger.json").as_posix(),
    "sha256": "c52b26478acac8d5cfa9687b0925a1a9165a3647bd510e9877d69b06cbf214d4",
}
FINAL_SUBJECT_FAMILY_LAYER_SPECS = (
    ("CA-P-2112", STAGE / "semantic-reviews/task-2112.research.json", "e65fe0ec394ca5655ee23052d869467aab0a632abede70d3311b86425f58b3d7", 17, 8, 9),
    ("CA-P-2113", STAGE / "semantic-reviews/task-2113.research.json", "97dae252cfe7cdfce21864bb38bf3bb12fc0c2a2ef489edd668387faa4415a6c", 27, 24, 3),
    ("CA-P-2114", STAGE / "semantic-reviews/task-2114.research.json", "c4a3db04a629185cddf1b56b2f52860b14262eb3d42a92aa68d43a5af4e3ade7", 28, 9, 19),
    ("CA-P-2115", STAGE / "semantic-reviews/task-2115.research.json", "cbad7db5ae4f00f397f67eb240d593596402fcb8bc02a247bdfd2b78abcf75b3", 24, 9, 15),
    ("CA-P-2116", STAGE / "semantic-reviews/task-2116.research.json", "90d3027a973bd4ff6ecfbe8c6d2288744513df48cf99d6be1c38a3fccf9ce50d", 15, 13, 2),
    ("CA-P-2117", STAGE / "semantic-reviews/task-2117.research.json", "d49221d9c8468f92b0f8144f879163538cc438699b5145fe2f36ed18bd8ffb8f", 26, 24, 2),
)
FINAL_SUBJECT_FAMILY_GROUP = ResearchLayerGroup(
    label="CA-P-2112–2117",
    manifest=STAGE / "semantic-reviews/followups-2112-2117.inputs.json",
    manifest_sha256="397b371532dc4f1fb684649ffe3ef6728e955c3825939ab9ee35e76047381bd5",
    registration_commit="9a584ff18f338aef87ac8c1d45116e430abf41b5",
    historical_working_pin=FINAL_SUBJECT_FAMILY_HISTORICAL_WORKING_PIN,
    specifications=FINAL_SUBJECT_FAMILY_LAYER_SPECS,
    expected_rows=137,
)
REMAINING_SUBJECT_DOMAINS_HISTORICAL_WORKING_PIN = {
    "path": (WORKING / "working-mapping-ledger.json").as_posix(),
    "sha256": "4f2ec9d285283a76386dd176f6d4a6bf6a101db32219349462a91bc6c666ecf2",
}
CORE_ONLY_SUCCESSOR_TASK = "CA-P-2133"
CORE_ONLY_SUCCESSOR_REPORT = STAGE / "semantic-reviews/task-2133.core-only.research.json"
CORE_ONLY_SUCCESSOR_RECEIPT = STAGE / "task-2133.core-only.receipt.json"
CORE_ONLY_SUCCESSOR_REPORT_SHA256 = "4d87d8cfe5376d23d37580b09019b9169b6bd75c976d749f67f10b8840926893"
CORE_ONLY_SUCCESSOR_TASK_ID = "CA-P-2143"
CORE_ONLY_SUCCESSOR_REGISTRATION_COMMIT = "74f96a6901765d5a854db87f8180655e3fb922ea"
CORE_ONLY_SUCCESSOR_PREDECESSOR = {
    "path": (STAGE / "semantic-reviews/task-2133.research.json").as_posix(),
    "sha256": "90b13cf54d48ec1f60c21bf778e27ff9f0a794599a37e769612d9ef3cff46445",
}
CORE_ONLY_SUCCESSOR_PREDECESSOR_RECEIPT = {
    "path": (STAGE / "task-2133.receipt.json").as_posix(),
    "sha256": "ce54fe83aae0618a624f044c54ac4b1c8e1557edf5bbd4ee0255f697c05b6a71",
}
CORE_ONLY_SUCCESSOR_CONTRACT = STAGE / "working-ledger.core-only-successor-2143.contract.md"
CORE_ONLY_SUCCESSOR_CONTRACT_SHA256 = "9019dada59adeb3f23dd2cc114600bc7fd5e9d72daa49034dd9390d46214d7a0"
REMAINING_SUBJECT_DOMAINS_LAYER_SPECS = (
    ("CA-P-2121", STAGE / "semantic-reviews/task-2121.research.json", "96d906b7769f52f32bfc4b8d1ccfb638ba5eee6c525bcc2e25851827fb4f693b", 22, 21, 1),
    ("CA-P-2122", STAGE / "semantic-reviews/task-2122.research.json", "3577856baf8a35c61c479c9d2feaa7e54f0252ec2f33f5ec9bb94def9eb928f8", 20, 8, 12),
    ("CA-P-2123", STAGE / "semantic-reviews/task-2123.research.json", "64c5e84639b39c37d7a175c11e967b407dfabbd840b76a80bc91352dd29e8728", 28, 7, 21),
    ("CA-P-2124", STAGE / "semantic-reviews/task-2124.research.json", "94b9b57e83a2b23bd493355ece510907ed31277edab45dc56e9ee5eefacfe9e3", 33, 7, 26),
    ("CA-P-2125", STAGE / "semantic-reviews/task-2125.research.json", "43bca8f0776c3d7ff25321e4e9c6b3da10b3bd5c3333c0cb0a8dbb9d1af7aeb3", 29, 7, 22),
    ("CA-P-2126", STAGE / "semantic-reviews/task-2126.research.json", "3fa0af8d302898a399cb1406cd9bcfcdd7ee22d3e3bc28f907f322e935dd8c52", 21, 11, 10),
    ("CA-P-2127", STAGE / "semantic-reviews/task-2127.research.json", "db250a76d1b6f5b4a8226a44656a81eb16e57965faa174c3b7f5a1337f638896", 23, 7, 16),
    ("CA-P-2128", STAGE / "semantic-reviews/task-2128.research.json", "12aff3f78128cb401ec7f070840d0958a9edcd0e20266f9a0acb231fa8220f56", 29, 3, 26),
)
REMAINING_SUBJECT_DOMAINS_GROUP = ResearchLayerGroup(
    label="CA-P-2121–2128",
    manifest=STAGE / "semantic-reviews/followups-2121-2128.inputs.json",
    manifest_sha256="311058fd59732975cbe9c3662c6eb93dc2231d192a66c33bc416a4ee83084c5f",
    registration_commit="56bb0d1b4da85c34ffc5dfe0edd5296d868011bd",
    historical_working_pin=REMAINING_SUBJECT_DOMAINS_HISTORICAL_WORKING_PIN,
    specifications=REMAINING_SUBJECT_DOMAINS_LAYER_SPECS,
    expected_rows=205,
)
RESIDUAL_SUBJECT_DOMAINS_HISTORICAL_WORKING_PIN = {
    "path": (WORKING / "working-mapping-ledger.json").as_posix(),
    "sha256": "19d55f08f9bd809d5a7cf7c937992b597e1a17d4b641e186ebc144b1e26c1186",
}
RESIDUAL_SUBJECT_DOMAINS_LAYER_SPECS = (
    ("CA-P-2132", STAGE / "semantic-reviews/task-2132.research.json", "2c79d4e3114f6db167acda343fecd0762eab6a78988e43f534f575661ffc35d2", 22, 2, 20),
    ("CA-P-2133", CORE_ONLY_SUCCESSOR_REPORT, CORE_ONLY_SUCCESSOR_REPORT_SHA256, 20, 9, 11),
    ("CA-P-2134", STAGE / "semantic-reviews/task-2134.research.json", "12805a8750a8b3840870416c0a742ceaf74e312c1bd71444f076a6b558b50303", 25, 11, 14),
    ("CA-P-2135", STAGE / "semantic-reviews/task-2135.research.json", "e4ca2241b187c266061078a216d2128e7d5b8350903b9fbc298f7aa72e30ba9f", 19, 16, 3),
    ("CA-P-2136", STAGE / "semantic-reviews/task-2136.research.json", "30ad47d268d8927561d78fe36860eafafaacc888d0408be1f79457f062aa7975", 37, 2, 35),
    ("CA-P-2137", STAGE / "semantic-reviews/task-2137.research.json", "d89d428d4262410bdb1bf1a833dd28b9bb6186bb153eaa6abf58c9157e39b113", 29, 7, 22),
    ("CA-P-2138", STAGE / "semantic-reviews/task-2138.research.json", "709b2e24e1e2c6961ef804c0a44460f1d1e1105fcdd49ae47096164b9c888c83", 23, 6, 17),
    ("CA-P-2139", STAGE / "semantic-reviews/task-2139.research.json", "1c07b8e41e299861b4a507e5f977bbff9e7b4adde19c9f9df4a3fd59a544fb83", 20, 10, 10),
)
RESIDUAL_SUBJECT_DOMAINS_GROUP = ResearchLayerGroup(
    label="CA-P-2132–2139",
    manifest=STAGE / "semantic-reviews/followups-2132-2139.inputs.json",
    manifest_sha256="a115ac2b55f88698a057bec8f13c9bbfba72105cb56bc2a7d606ff6360214cfd",
    registration_commit="5814a20c8d7b27b45b383409b35e4f0dfda5cefc",
    historical_working_pin=RESIDUAL_SUBJECT_DOMAINS_HISTORICAL_WORKING_PIN,
    specifications=RESIDUAL_SUBJECT_DOMAINS_LAYER_SPECS,
    expected_rows=195,
)
RESEARCH_LAYER_GROUPS = (
    FOLLOWUP_GROUP,
    SUBJECT_FAMILY_GROUP,
    FINAL_SUBJECT_FAMILY_GROUP,
    REMAINING_SUBJECT_DOMAINS_GROUP,
    RESIDUAL_SUBJECT_DOMAINS_GROUP,
)
ORIGIN_FIELDS = (
    "occurrence_id", "source_path", "source_atom_id", "source_version", "source_sha256",
    "field", "index", "old_value", "quarantined",
)


def validate_research_group_configuration(groups: tuple[ResearchLayerGroup, ...]) -> None:
    """Keep this closed one-off integration from turning into layer discovery."""
    if groups != (
        FOLLOWUP_GROUP,
        SUBJECT_FAMILY_GROUP,
        FINAL_SUBJECT_FAMILY_GROUP,
        REMAINING_SUBJECT_DOMAINS_GROUP,
        RESIDUAL_SUBJECT_DOMAINS_GROUP,
    ):
        fail("research layer group order or membership changed")
    expected_tasks = (
        "CA-P-2094", "CA-P-2095", "CA-P-2096", "CA-P-2097", "CA-P-2098", "CA-P-2099",
        "CA-P-2103", "CA-P-2104", "CA-P-2105", "CA-P-2106", "CA-P-2107", "CA-P-2108",
        "CA-P-2112", "CA-P-2113", "CA-P-2114", "CA-P-2115", "CA-P-2116", "CA-P-2117",
        "CA-P-2121", "CA-P-2122", "CA-P-2123", "CA-P-2124",
        "CA-P-2125", "CA-P-2126", "CA-P-2127", "CA-P-2128",
        "CA-P-2132", "CA-P-2133", "CA-P-2134", "CA-P-2135",
        "CA-P-2136", "CA-P-2137", "CA-P-2138", "CA-P-2139",
    )
    tasks = tuple(specification[0] for group in groups for specification in group.specifications)
    if tasks != expected_tasks:
        fail("research layer task order or membership changed")


def fail(message: str) -> None:
    raise ValueError(message)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def pin(relative: Path) -> dict[str, str]:
    path = checked_relative_path(relative, "input")
    if not path.is_file() or path.is_symlink():
        fail(f"required regular input missing: {relative}")
    return {"path": relative.as_posix(), "sha256": sha(path.read_bytes())}


def canonical_decision_record_pin(input_pins: dict[str, Any]) -> dict[str, str]:
    """Permit the one recorded operator decision file, never an arbitrary support file."""
    canonical = pin(DECISION_RECORD)
    if input_pins.get("operator_decision_record") != canonical:
        fail("research report operator decision-record pin")
    return canonical


def core_only_successor_predecessor_pins() -> tuple[dict[str, str], dict[str, str]]:
    """Keep the withdrawn CA-P-2133 evidence immutable and live-pinned."""
    report_pin = pin(Path(CORE_ONLY_SUCCESSOR_PREDECESSOR["path"]))
    receipt_pin_value = pin(Path(CORE_ONLY_SUCCESSOR_PREDECESSOR_RECEIPT["path"]))
    if report_pin != CORE_ONLY_SUCCESSOR_PREDECESSOR or receipt_pin_value != CORE_ONLY_SUCCESSOR_PREDECESSOR_RECEIPT:
        fail("Core-only successor predecessor lineage pin")
    return report_pin, receipt_pin_value


def read_json(relative: Path) -> dict[str, Any]:
    path = checked_relative_path(relative, "JSON input")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError(f"invalid JSON input: {relative}") from error
    if not isinstance(value, dict):
        fail(f"JSON object required: {relative}")
    return value


def json_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True).encode("utf-8") + b"\n"


def body_evidence(path: Path, raw: bytes) -> list[dict[str, Any]]:
    lines = raw.splitlines(keepends=True)
    separators = [index for index, line in enumerate(lines) if line.rstrip(b"\r\n") == b"---"]
    if len(separators) < 2:
        fail(f"missing frontmatter boundary: {rel(path)}")
    start = separators[1] + 2
    body = b"".join(lines[separators[1] + 1 :])
    return [{
        "path": rel(path), "sha256": sha(raw), "start_line": start,
        "end_line": len(lines), "span_sha256": sha(body),
        "reason": "Current full Main Content pin for required semantic recheck.",
    }]


def current_frontier() -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], dict[str, str]]:
    structure_path = checked_relative_path(STRUCTURE, "authoritative Structure")
    try:
        structure = tomllib.loads(structure_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, tomllib.TOMLDecodeError) as error:
        raise ValueError("authoritative Structure is unreadable") from error
    units = structure.get("scope_units") if isinstance(structure, dict) else None
    matches = [unit for unit in units or [] if isinstance(unit, dict) and unit.get("scope_unit_name") == "CORE_META_MODEL"]
    if len(matches) != 1 or not isinstance(matches[0].get("authority_path"), str):
        fail("CORE_META_MODEL authority path missing or ambiguous")
    source_root = checked_relative_path(Path(matches[0]["authority_path"]), "CORE_META_MODEL authority")
    if not source_root.is_dir() or source_root.is_symlink():
        fail("CORE_META_MODEL authority root is unsafe")

    sources: list[dict[str, Any]] = []
    occurrences: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []
    for path in source_files(source_root):
        relative = rel(path)
        if "archive" in path.relative_to(source_root).parts:
            excluded.append({"relative_path": relative, "reason": "archived_lifecycle_copy"})
            continue
        raw = path.read_bytes()
        try:
            parsed = parse_carrier(raw, path)
            metadata = parsed.metadata
        except CarrierError as error:
            filename = FILENAME_ATOM_ID.match(path.stem)
            if filename is None:
                excluded.append({"relative_path": relative, "reason": "strict_parse_error", "code": error.code})
                continue
            role = next((name for name, code in ROLES.items() if code == filename.group(2)), None)
            if role is None:
                excluded.append({"relative_path": relative, "reason": "strict_parse_error", "code": error.code})
                continue
            sources.append({"relative_path": relative, "full_file_sha256": sha(raw), "atom_id": None,
                            "version": None, "role": role, "owner": None, "status": None,
                            "quarantined": True, "findings": [f"strict_parse_error:{error.code}"]})
            continue
        role = metadata.get("content_role")
        owner = metadata.get("current_scope_unit")
        status = metadata.get("status")
        if owner != "CORE_META_MODEL" or status != "Active" or role not in ROLES:
            excluded.append({"relative_path": relative, "reason": "outside_original_active_rmedo_frontier",
                             "content_role": role, "current_scope_unit": owner, "status": status})
            continue
        findings: list[str] = []
        atom_id = metadata.get("atom_id")
        atom_match = ATOM_ID.fullmatch(atom_id) if isinstance(atom_id, str) else None
        if atom_match is None:
            findings.append("missing_or_invalid_atom_id")
        else:
            if ROLES[role] != atom_match.group(1):
                findings.append("atom_id_role_mismatch")
            if not (path.stem == atom_id or path.stem.startswith(f"{atom_id}-")):
                findings.append("filename_atom_id_mismatch")
        if directory_role(source_root, path) != role:
            findings.append("directory_role_mismatch")
        version = metadata.get("version")
        if not isinstance(version, int) or isinstance(version, bool) or version <= 0:
            findings.append("missing_or_invalid_version")
        raw_updated, _ = updated_at(parsed.frontmatter)
        if raw_updated is None or not isinstance(metadata.get("updated_at"), str) or not UPDATED_AT.fullmatch(raw_updated):
            findings.append("updated_at_invalid_or_naive")
        subjects = metadata.get("subjects")
        valid: list[tuple[str, int | None, str]] = []
        if not isinstance(subjects, dict):
            findings.append("subjects_not_mapping")
            subjects = {}
        else:
            for field in sorted(set(subjects).difference(SUBJECT_FIELDS)):
                findings.append(f"unknown_subjects_field:{field}")
        governs = subjects.get("governs")
        if isinstance(governs, str) and governs.strip():
            valid.append(("governs", None, governs))
        else:
            findings.append("governs_missing_or_invalid")
        depends = subjects.get("depends_on")
        if depends is not None:
            if isinstance(depends, list) and all(isinstance(item, str) and item.strip() for item in depends) and len(set(depends)) == len(depends):
                valid.extend(("depends_on", index, value) for index, value in enumerate(depends))
            else:
                findings.append("depends_on_missing_or_invalid_unique_string_list")
        source = {"relative_path": relative, "full_file_sha256": sha(raw), "atom_id": atom_id,
                  "version": version, "role": role, "owner": owner, "status": status,
                  "quarantined": bool(findings), "findings": findings, "body_evidence": body_evidence(path, raw)}
        sources.append(source)
        for field, index, old_value in valid:
            suffix = f"subjects.{field}" + (f"[{index}]" if index is not None else "")
            occurrences.append({"occurrence_id": f"{relative}#{suffix}", "source_path": relative,
                                "source_atom_id": atom_id, "source_version": version,
                                "source_sha256": source["full_file_sha256"], "field": field,
                                "index": index, "old_value": old_value, "quarantined": source["quarantined"]})
    sources.sort(key=lambda item: item["relative_path"])
    occurrences.sort(key=lambda item: item["occurrence_id"])
    excluded.sort(key=lambda item: item["relative_path"])
    return sources, occurrences, excluded, {"path": STRUCTURE.as_posix(), "sha256": sha(structure_path.read_bytes())}


def receipt_pin(task_id: str, report_pin: dict[str, str]) -> dict[str, str]:
    relative = STAGE / f"task-{task_id.removeprefix('CA-P-')}.receipt.json"
    receipt = read_json(relative)
    if receipt.get("task") != task_id:
        fail(f"invalid receipt identity: {task_id}")
    if task_id != "CA-P-2048" and receipt.get("non_authoritative") is not True:
        fail(f"invalid non-authoritative receipt boundary: {task_id}")
    if not str(receipt.get("result", "")).startswith("PASS"):
        fail(f"receipt is not an accepted result: {task_id}")
    if task_id == "CA-P-2048":
        if receipt.get("output") != report_pin:
            fail(f"receipt output pin mismatch: {task_id}")
        checks = receipt.get("checks")
        if not isinstance(checks, dict) or not str(checks.get("independent_semantic_review", "")).startswith("PASS"):
            fail(f"independent semantic acceptance missing: {task_id}")
        return pin(relative)
    if task_id == "CA-P-2058":
        if receipt.get("output") != report_pin:
            fail(f"receipt output pin mismatch: {task_id}")
        accepted = receipt.get("independent_acceptance")
        if not isinstance(accepted, list) or not accepted:
            fail(f"independent accepted coverage missing: {task_id}")
        return pin(relative)
    verification = receipt.get("verification")
    if not isinstance(verification, dict):
        fail(f"missing receipt verification: {task_id}")
    output = verification.get("review") or verification.get("output")
    if output != report_pin:
        fail(f"receipt output pin mismatch: {task_id}")
    independent = receipt.get("independent_review")
    if independent is not None and (not isinstance(independent, dict) or not str(independent.get("result", "")).startswith("PASS")):
        fail(f"independent semantic acceptance missing: {task_id}")
    return pin(relative)


def layer_rows(kind: str, report: dict[str, Any]) -> Iterable[dict[str, Any]]:
    rows = report.get("occurrences") if kind == "substance" else report.get("rows")
    if not isinstance(rows, list):
        fail(f"missing rows for {report.get('task_id')}")
    return rows


def normalized_decision(kind: str, row: dict[str, Any]) -> tuple[str, str | None, float]:
    if kind == "semantic":
        disposition = row.get("disposition")
        if disposition == "accepted":
            value = row.get("proposed_value")
            confidence = row.get("confidence")
            if not isinstance(value, str) or not value or not isinstance(confidence, (int, float)) or confidence < 0.90:
                fail("invalid accepted semantic row")
            return "proposed", value, float(confidence)
        if disposition in {"rejected", "unresolved", "stale"}:
            return "unresolved", None, 0.0
        fail("unknown semantic disposition")
    decision = row.get("decision")
    value = row.get("proposed_value")
    confidence = row.get("confidence")
    if decision == "proposed":
        if not isinstance(value, str) or not value or not isinstance(confidence, (int, float)) or confidence < 0.90:
            fail("invalid proposed layer row")
        return "proposed", value, float(confidence)
    if decision in {"unresolved", "rejected", "stale"}:
        return "unresolved", None, float(confidence) if isinstance(confidence, (int, float)) else 0.0
    fail("unknown layer decision")


def no_inferred_syntax(value: str | None) -> None:
    if value is not None and any(token in value for token in ("@", "(", ")", "&", "|", "=")):
        fail(f"inferred selector or unsupported syntax: {value}")


def historical_origin(row: dict[str, Any]) -> dict[str, Any]:
    return {key: row.get(key) for key in (
        "occurrence_id", "source_path", "source_atom_id", "source_version", "source_sha256",
        "field", "index", "old_value", "quarantined", "decision", "proposed_value",
        "confidence", "originating_review_path", "originating_review_sha256", "task_id", "batch_id",
    )}


def declared_grammar_effects(drift: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    """Return only the five audited current-source effects, fail closed otherwise."""
    current_effects: dict[str, dict[str, Any]] = {}
    replacement: dict[str, str] = {}
    records = drift.get("changed_or_missing")
    if not isinstance(records, list) or len(records) != 5:
        fail("expected exactly five audited grammar effects")
    for record in records:
        if record.get("classified") != "approved_grammar_effect" or not isinstance(record.get("atom_id"), str):
            fail("unapproved grammar drift")
        atom_id = record["atom_id"]
        effect = record.get("declared_effect")
        if not isinstance(effect, dict):
            fail("grammar effect missing declaration")
        before = effect.get("before")
        if not isinstance(before, dict) or any(not isinstance(before.get(field), expected) for field, expected in (("path", str), ("version", int), ("sha256", str))):
            fail("grammar effect missing complete before pin")
        if (record.get("path"), record.get("baseline_version"), record.get("baseline_sha256")) != (before["path"], before["version"], before["sha256"]):
            fail("grammar effect record/before pin disagreement")
        if effect.get("operation") == "replace_with_new_id":
            after = effect.get("after")
            if not isinstance(after, dict) or any(not isinstance(after.get(field), expected) for field, expected in (("atom_id", str), ("path", str), ("version", int), ("sha256", str))):
                fail("replacement grammar effect missing new Atom ID")
            current_atom_id = after["atom_id"]
            if current_atom_id in replacement:
                fail("duplicate replacement current Atom ID")
            replacement[current_atom_id] = atom_id
        elif effect.get("operation") == "revise_active_atom":
            after = effect.get("after")
            if not isinstance(after, dict) or any(not isinstance(after.get(field), expected) for field, expected in (("path", str), ("version", int), ("sha256", str))):
                fail("revision grammar effect missing complete after pin")
            current_atom_id = atom_id
        else:
            fail("unsupported grammar effect")
        if current_atom_id in current_effects:
            fail("duplicate grammar current Atom ID")
        current_effects[current_atom_id] = {"historic_atom_id": atom_id, "operation": effect["operation"], "before": before, "after": after}
    return current_effects, replacement


def source_index(sources: list[dict[str, Any]], label: str) -> dict[str, dict[str, Any]]:
    indexed = {source.get("relative_path"): source for source in sources if isinstance(source.get("relative_path"), str)}
    if len(indexed) != len(sources):
        fail(f"duplicate or invalid {label} source path")
    return indexed


def source_matches_pin(source: dict[str, Any], atom_id: str, pin_value: dict[str, Any]) -> bool:
    return (source.get("atom_id") == atom_id and source.get("relative_path") == pin_value.get("path")
            and source.get("version") == pin_value.get("version") and source.get("full_file_sha256") == pin_value.get("sha256"))


def validate_declared_drift(
    baseline_sources: list[dict[str, Any]], current_sources: list[dict[str, Any]], current_effects: dict[str, dict[str, Any]],
) -> None:
    """Require exact audited pins for every drift and reject all other source movement."""
    historic = source_index(baseline_sources, "baseline")
    current = source_index(current_sources, "current")
    effect_by_historic = {effect["historic_atom_id"]: (current_atom_id, effect) for current_atom_id, effect in current_effects.items()}
    for current_atom_id, effect in current_effects.items():
        before, after = effect["before"], effect["after"]
        historic_source = historic.get(before["path"])
        if historic_source is None or not source_matches_pin(historic_source, effect["historic_atom_id"], before):
            fail(f"declared grammar before pin does not match frozen baseline: {effect['historic_atom_id']}")
        active_source = current.get(after["path"])
        if active_source is None or not source_matches_pin(active_source, current_atom_id, after):
            fail(f"declared grammar current-after pin does not match live Core: {current_atom_id}")
    for path, historic_source in historic.items():
        active_source = current.get(path)
        if active_source is not None:
            if active_source.get("full_file_sha256") == historic_source.get("full_file_sha256"):
                continue
            current_atom_id = active_source.get("atom_id")
            effect = current_effects.get(current_atom_id) if isinstance(current_atom_id, str) else None
            if effect is None or effect["operation"] != "revise_active_atom" or not source_matches_pin(active_source, current_atom_id, effect["after"]):
                fail(f"unexpected current source hash drift: {path}")
            continue
        historic_atom_id = historic_source.get("atom_id")
        declared = effect_by_historic.get(historic_atom_id) if isinstance(historic_atom_id, str) else None
        if declared is None or declared[1]["operation"] != "replace_with_new_id" or not source_matches_pin(historic_source, historic_atom_id, declared[1]["before"]):
            fail(f"missing current source without declared replacement: {path}")
    for path, active_source in current.items():
        if path in historic:
            continue
        active_atom_id = active_source.get("atom_id")
        effect = current_effects.get(active_atom_id) if isinstance(active_atom_id, str) else None
        if effect is None or effect["operation"] != "replace_with_new_id" or not source_matches_pin(active_source, active_atom_id, effect["after"]):
            fail(f"unexpected current source path without declared replacement: {path}")


def matched_origin(
    current: dict[str, Any], baseline_by_id: dict[str, dict[str, Any]], baseline_by_atom_field: dict[tuple[Any, Any, Any, Any], list[dict[str, Any]]],
    replacement: dict[str, str],
) -> dict[str, Any]:
    origin = baseline_by_id.get(current["occurrence_id"])
    if origin is not None:
        if (origin.get("field"), origin.get("index"), origin.get("old_value")) != (current["field"], current["index"], current["old_value"]):
            fail(f"existing occurrence ID does not preserve field/index/text: {current['occurrence_id']}")
        return origin
    historic_atom_id = replacement.get(current.get("source_atom_id"))
    if historic_atom_id is None:
        fail(f"missing exact frozen baseline occurrence: {current['occurrence_id']}")
    candidates = baseline_by_atom_field.get((historic_atom_id, current["field"], current["index"], current["old_value"]), [])
    if len(candidates) != 1:
        fail(f"declared replacement lacks one exact field/index/text baseline counterpart: {current['occurrence_id']}")
    return candidates[0]


def current_span_matches(evidence: dict[str, Any], current: dict[str, Any]) -> bool:
    if evidence.get("path") != current.get("source_path") or evidence.get("sha256") != current.get("source_sha256"):
        return False
    start, end = evidence.get("start_line"), evidence.get("end_line")
    span_sha = evidence.get("span_sha256")
    if not isinstance(start, int) or isinstance(start, bool) or not isinstance(end, int) or isinstance(end, bool) or start < 1 or end < start or not isinstance(span_sha, str):
        return False
    path = checked_relative_path(Path(evidence["path"]), "current grammar evidence")
    if not path.is_file() or path.is_symlink():
        return False
    raw = path.read_bytes()
    if sha(raw) != evidence["sha256"]:
        return False
    lines = raw.splitlines(keepends=True)
    return end <= len(lines) and sha(b"".join(lines[start - 1 : end])) == span_sha


def exact_span_matches_file(evidence: dict[str, Any], label: str) -> bool:
    """Check a pinned evidence span without granting it Core-source status."""
    path_value, digest = evidence.get("path"), evidence.get("sha256")
    start, end, span_sha = evidence.get("start_line"), evidence.get("end_line"), evidence.get("span_sha256")
    if (not isinstance(path_value, str) or not isinstance(digest, str) or not isinstance(start, int)
            or isinstance(start, bool) or not isinstance(end, int) or isinstance(end, bool)
            or start < 1 or end < start or not isinstance(span_sha, str)):
        return False
    try:
        path = checked_relative_path(Path(path_value), label)
    except CarrierError:
        return False
    if not path.is_file() or path.is_symlink():
        return False
    raw = path.read_bytes()
    if sha(raw) != digest:
        return False
    lines = raw.splitlines(keepends=True)
    return end <= len(lines) and sha(b"".join(lines[start - 1 : end])) == span_sha


def json_pointer(document: Any, pointer: Any, label: str) -> Any:
    if not isinstance(pointer, str):
        fail(f"invalid JSON pointer: {label}")
    pointer = pointer.removeprefix("#")
    if not pointer.startswith("/") or pointer == "/":
        fail(f"invalid JSON pointer: {label}")
    value = document
    for part in pointer[1:].split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(value, list):
            if not part.isdigit() or int(part) >= len(value):
                fail(f"missing JSON list pointer: {label}")
            value = value[int(part)]
        elif isinstance(value, dict) and part in value:
            value = value[part]
        else:
            fail(f"missing JSON object pointer: {label}")
    return value


def research_group_tasks(
    group: ResearchLayerGroup, manifest: dict[str, Any], manifest_pin: dict[str, str],
) -> dict[str, dict[str, Any]]:
    """Fail closed over one registered, fixed research group."""
    if manifest_pin["sha256"] != group.manifest_sha256:
        fail(f"research manifest SHA-256 changed: {group.label}")
    tasks = manifest.get("tasks")
    expected_order = [item[0] for item in group.specifications]
    if (not isinstance(tasks, list) or len(tasks) != len(expected_order) or not all(isinstance(item, dict) for item in tasks)
            or [item.get("task_id") for item in tasks] != expected_order):
        fail(f"research manifest task order or ownership changed: {group.label}")
    result: dict[str, dict[str, Any]] = {}
    all_ids: set[str] = set()
    for task, _, _, expected_rows, _, _ in group.specifications:
        entry = next((item for item in tasks if isinstance(item, dict) and item.get("task_id") == task), None)
        if entry is None:
            fail(f"research manifest task missing: {task}")
        rows = entry.get("input_rows")
        if not isinstance(rows, list) or len(rows) != expected_rows or entry.get("occurrences") != expected_rows:
            fail(f"research manifest occurrence count: {task}")
        if not all(isinstance(row, dict) for row in rows):
            fail(f"research manifest origin rows: {task}")
        ids = [row.get("occurrence_id") for row in rows]
        if not all(isinstance(item, str) for item in ids) or len(set(ids)) != len(ids):
            fail(f"research manifest duplicate occurrence: {task}")
        digest = sha("".join(f"{occurrence_id}\n" for occurrence_id in sorted(ids)).encode("utf-8"))
        if entry.get("occurrence_id_set_sha256") != digest:
            fail(f"research manifest occurrence digest: {task}")
        if len({row.get("source_path") for row in rows}) != entry.get("sources"):
            fail(f"research manifest source coverage: {task}")
        if all_ids.intersection(ids):
            fail(f"research manifest cross-task duplicate: {task}")
        all_ids.update(ids)
        result[task] = entry
    if len(all_ids) != group.expected_rows:
        fail(f"research manifest total occurrence coverage: {group.label}")
    return result


def accepted_research_layer(
    group: ResearchLayerGroup, specification: tuple[str, Path, str, int, int, int],
    manifest_pin: dict[str, str], manifest_task: dict[str, Any],
    baseline_by_id: dict[str, dict[str, Any]], current_by_id: dict[str, dict[str, Any]],
    current_sources_by_path: dict[str, dict[str, Any]], candidate: dict[str, Any], candidate_pin: dict[str, str],
) -> tuple[dict[str, Any], dict[str, str], dict[str, Any]]:
    """Load one final accepted fixed research layer with live proof only."""
    task_id, report_rel, expected_sha, expected_rows, expected_proposed, expected_unresolved = specification
    is_core_only_successor = task_id == CORE_ONLY_SUCCESSOR_TASK
    if is_core_only_successor and (report_rel != CORE_ONLY_SUCCESSOR_REPORT or expected_sha != CORE_ONLY_SUCCESSOR_REPORT_SHA256):
        fail("Core-only successor report binding")
    report = read_json(report_rel)
    report_pin = pin(report_rel)
    if report_pin["sha256"] != expected_sha:
        fail(f"research report SHA-256 changed: {task_id}")
    if any(report.get(field) != value for field, value in (
        ("schema_version", 1), ("task_id", task_id), ("non_authoritative", True),
        ("source_migration", "not_performed"), ("native_admission", "not_performed"),
    )):
        fail(f"research report boundary: {task_id}")
    predecessor_report_pin: dict[str, str] | None = None
    predecessor_receipt_pin: dict[str, str] | None = None
    if is_core_only_successor:
        predecessor_report_pin, predecessor_receipt_pin = core_only_successor_predecessor_pins()
    input_pins = report.get("input_pins")
    if not isinstance(input_pins, dict) or input_pins.get("candidate") != candidate_pin:
        fail(f"research report candidate pin: {task_id}")
    successor_contract_pin = pin(CORE_ONLY_SUCCESSOR_CONTRACT)
    if successor_contract_pin["sha256"] != CORE_ONLY_SUCCESSOR_CONTRACT_SHA256:
        fail("Core-only successor contract SHA-256 changed")
    if is_core_only_successor:
        if (report.get("report_revision") != 2 or report.get("successor_task") != CORE_ONLY_SUCCESSOR_TASK_ID
                or report.get("supersedes") != predecessor_report_pin):
            fail("Core-only successor report metadata")
        report_contracts = input_pins.get("contracts")
        if not isinstance(report_contracts, list) or successor_contract_pin not in report_contracts:
            fail("Core-only successor report contract pin")
    decision_record_pin = canonical_decision_record_pin(input_pins)
    manifest_descriptors = [input_pins[key] for key in ("selection_manifest", "manifest") if key in input_pins]
    if manifest_descriptors != [manifest_pin]:
        fail(f"research report manifest pin: {task_id}")
    if input_pins.get("working_ledger") != group.historical_working_pin:
        fail(f"research report historical working-ledger pin: {task_id}")
    baseline_descriptors = [input_pins[key] for key in ("base_ledger", "baseline_ledger", "frozen_baseline_ledger") if key in input_pins]
    if baseline_descriptors != [pin(BASELINE)]:
        fail(f"research report baseline-ledger pin: {task_id}")

    receipt_rel = CORE_ONLY_SUCCESSOR_RECEIPT if is_core_only_successor else STAGE / f"task-{task_id.removeprefix('CA-P-')}.receipt.json"
    receipt = read_json(receipt_rel)
    receipt_pin_value = pin(receipt_rel)
    verification = receipt.get("verification")
    if (receipt.get("task") != task_id or receipt.get("non_authoritative") is not True
            or receipt.get("source_migration") != "not_performed" or receipt.get("native_admission") != "not_performed"
            or not str(receipt.get("result", "")).startswith("PASS") or not isinstance(verification, dict)):
        fail(f"research receipt boundary: {task_id}")
    if (verification.get("task") != task_id or verification.get("output") != report_pin
            or verification.get("rows") != expected_rows
            or verification.get("counts") != {"proposed": expected_proposed, "unresolved": expected_unresolved}
            or verification.get("input_manifest") != manifest_pin
            or verification.get("registration_commit") != group.registration_commit
            or receipt.get("registration_commit") != group.registration_commit):
        fail(f"research receipt descriptors: {task_id}")
    if is_core_only_successor:
        if (receipt.get("successor_task") != CORE_ONLY_SUCCESSOR_TASK_ID
                or receipt.get("successor_registration_commit") != CORE_ONLY_SUCCESSOR_REGISTRATION_COMMIT
                or receipt.get("supersedes") != predecessor_report_pin
                or receipt.get("successor_contract") != successor_contract_pin
                or verification.get("successor_task") != CORE_ONLY_SUCCESSOR_TASK_ID
                or verification.get("successor_registration_commit") != CORE_ONLY_SUCCESSOR_REGISTRATION_COMMIT
                or verification.get("supersedes") != predecessor_report_pin):
            fail("Core-only successor receipt metadata")
    for review in (receipt.get("independent_review"), verification.get("independent_review")):
        if (not isinstance(review, dict) or review.get("final_report_sha256") != report_pin["sha256"]
                or not str(review.get("result", "")).startswith("PASS")):
            fail(f"research independent semantic acceptance: {task_id}")

    rows = report.get("rows")
    expected_origins = manifest_task.get("input_rows")
    if (not isinstance(rows, list) or not isinstance(expected_origins, list)
            or len(rows) != expected_rows or len(expected_origins) != expected_rows):
        fail(f"research row coverage: {task_id}")
    expected_by_id = {row.get("occurrence_id"): row for row in expected_origins if isinstance(row, dict)}
    if len(expected_by_id) != expected_rows:
        fail(f"research manifest origin uniqueness: {task_id}")
    reported_ids = [row.get("occurrence_id") for row in rows if isinstance(row, dict)]
    if len(reported_ids) != expected_rows or len(set(reported_ids)) != expected_rows or set(reported_ids) != set(expected_by_id):
        fail(f"research report exact ownership: {task_id}")

    decisions = Counter()
    for row in rows:
        if not isinstance(row, dict):
            fail(f"research row object: {task_id}")
        occurrence_id = row["occurrence_id"]
        expected = expected_by_id[occurrence_id]
        if {field: row.get(field) for field in ORIGIN_FIELDS} != {field: expected.get(field) for field in ORIGIN_FIELDS}:
            fail(f"research report origin mismatch: {task_id} {occurrence_id}")
        current = current_by_id.get(occurrence_id)
        if current is None or {field: row.get(field) for field in ORIGIN_FIELDS} != {field: current.get(field) for field in ORIGIN_FIELDS}:
            fail(f"research current origin drift: {task_id} {occurrence_id}")
        baseline = baseline_by_id.get(occurrence_id)
        if baseline is None or baseline.get("decision") != "unresolved" or row.get("prior_decision") != "unresolved":
            fail(f"research baseline-only unresolved boundary: {task_id} {occurrence_id}")
        if row.get("executable") is not False or not isinstance(row.get("reason"), str) or not row["reason"].strip():
            fail(f"research row safety/reason: {task_id} {occurrence_id}")
        evidence = row.get("evidence")
        if not isinstance(evidence, list) or not evidence or not any(isinstance(item, dict) and current_span_matches(item, current) for item in evidence):
            fail(f"research owning current evidence: {task_id} {occurrence_id}")
        for item in evidence:
            if not isinstance(item, dict):
                fail(f"research evidence object: {task_id} {occurrence_id}")
            supporting_source = current_sources_by_path.get(item.get("path"))
            if supporting_source is not None:
                if not current_span_matches(item, {
                    "source_path": supporting_source["relative_path"], "source_sha256": supporting_source["full_file_sha256"],
                }):
                    fail(f"research stale Core supporting evidence: {task_id} {occurrence_id}")
                continue
            if (item.get("path") != decision_record_pin["path"] or item.get("sha256") != decision_record_pin["sha256"]
                    or not exact_span_matches_file(item, "research decision evidence")):
                fail(f"research unsupported non-Core evidence: {task_id} {occurrence_id}")
        if row.get("decision") not in {"proposed", "unresolved"}:
            fail(f"research decision: {task_id} {occurrence_id}")
        decision, value, confidence = normalized_decision("research", row)
        no_inferred_syntax(value)
        if decision == "proposed":
            basis = row.get("candidate_basis")
            if not isinstance(basis, list) or not basis:
                fail(f"research proposal basis: {task_id} {occurrence_id}")
            for item in basis:
                if not isinstance(item, dict) or not isinstance(item.get("reason"), str) or not item["reason"].strip():
                    fail(f"research proposal basis reason: {task_id} {occurrence_id}")
                json_pointer(candidate, item.get("pointer"), f"{task_id} {occurrence_id}")
        else:
            if value is not None or confidence >= .90:
                fail(f"research null decision shape: {task_id} {occurrence_id}")
        decisions[decision] += 1
    if decisions != Counter({"proposed": expected_proposed, "unresolved": expected_unresolved}):
        fail(f"research final decision coverage: {task_id}")
    report_counts = report.get("counts")
    if isinstance(report_counts, dict) and (report_counts.get("proposed") != expected_proposed or report_counts.get("unresolved") != expected_unresolved):
        fail(f"research report counts: {task_id}")
    descriptor = {
        "task": task_id, "report": report_pin, "receipt": receipt_pin_value, "manifest": manifest_pin,
        "independent_review_sha256": report_pin["sha256"], "rows": expected_rows,
        "kind": "research",
    }
    if is_core_only_successor:
        descriptor.update({"successor_task": CORE_ONLY_SUCCESSOR_TASK_ID, "report_revision": 2,
                           "supersedes": predecessor_report_pin, "predecessor_receipt": predecessor_receipt_pin,
                           "successor_contract": successor_contract_pin})
    return report, receipt_pin_value, descriptor


def accepted_current_grammar_review(
    current_by_id: dict[str, dict[str, Any]], current_effects: dict[str, dict[str, Any]],
) -> dict[str, Any] | None:
    """Load CA-P-2087 only when its accepted receipt and live current proof agree."""
    receipt_rel = STAGE / "task-2087.receipt.json"
    receipt_path = checked_relative_path(receipt_rel, "current grammar receipt")
    if not receipt_path.exists():
        return None
    if receipt_path.is_symlink():
        fail("unsafe current grammar receipt")
    report = read_json(CURRENT_GRAMMAR_REPORT)
    report_pin = pin(CURRENT_GRAMMAR_REPORT)
    receipt = receipt_pin(CURRENT_GRAMMAR_TASK, report_pin)
    if (report.get("schema_version") != 1 or report.get("task_id") != CURRENT_GRAMMAR_TASK
            or report.get("non_authoritative") is not True or report.get("source_migration") != "not_performed"
            or report.get("native_admission") != "not_performed"):
        fail("current grammar report boundary")
    verification = read_json(receipt_rel).get("verification")
    if not isinstance(verification, dict) or verification.get("output") != report_pin or verification.get("rows") != 33 or verification.get("current_sources") != 5:
        fail("current grammar receipt coverage/pin")
    expected_ids = {occurrence_id for occurrence_id, current in current_by_id.items() if current.get("source_atom_id") in current_effects}
    if len(expected_ids) != 33:
        fail("audited grammar occurrence coverage changed")
    rows = report.get("occurrences")
    if not isinstance(rows, list) or len(rows) != 33:
        fail("current grammar report rows")
    rows_by_id: dict[str, dict[str, Any]] = {}
    decisions = Counter()
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("occurrence_id"), str) or row["occurrence_id"] in rows_by_id:
            fail("current grammar duplicate or invalid occurrence")
        occurrence_id = row["occurrence_id"]
        current = current_by_id.get(occurrence_id)
        if current is None or {key: row.get(key) for key in current} != current:
            fail(f"current grammar row has stale or conflicting origin: {occurrence_id}")
        if row.get("executable") is not False or not isinstance(row.get("reason"), str) or not row["reason"].strip():
            fail(f"current grammar row safety/reason: {occurrence_id}")
        evidence = row.get("evidence")
        if not isinstance(evidence, list) or not any(isinstance(item, dict) and current_span_matches(item, current) for item in evidence):
            fail(f"current grammar row stale evidence: {occurrence_id}")
        decision, value, confidence = row.get("decision"), row.get("proposed_value"), row.get("confidence")
        if decision == "proposed":
            if not isinstance(value, str) or not value or not isinstance(confidence, (int, float)) or isinstance(confidence, bool) or confidence < .90:
                fail(f"current grammar proposal shape: {occurrence_id}")
            no_inferred_syntax(value)
            basis = row.get("candidate_basis")
            if not isinstance(basis, list) or not basis or any(not isinstance(item, dict) or not isinstance(item.get("pointer"), str) or not isinstance(item.get("reason"), str) for item in basis):
                fail(f"current grammar proposal basis: {occurrence_id}")
        elif decision == "unresolved":
            if value is not None or not isinstance(confidence, (int, float)) or isinstance(confidence, bool) or not 0 <= confidence < .90:
                fail(f"current grammar null shape: {occurrence_id}")
        else:
            fail(f"current grammar decision: {occurrence_id}")
        decisions[decision] += 1
        rows_by_id[occurrence_id] = row
    if set(rows_by_id) != expected_ids or decisions != Counter({"proposed": 15, "unresolved": 18}):
        fail("current grammar exact decision coverage")
    counts = report.get("counts")
    if not isinstance(counts, dict) or any(counts.get(key) != value for key, value in {"sources": 5, "occurrences": 33, "proposed": 15, "unresolved": 18, "unchanged": 0}.items()):
        fail("current grammar report counts")
    sources = report.get("sources")
    if not isinstance(sources, list) or len(sources) != 5:
        fail("current grammar source coverage")
    report_atoms = {source.get("atom_id") for source in sources if isinstance(source, dict)}
    if report_atoms != set(current_effects):
        fail("current grammar source identities")
    for source in sources:
        effect = current_effects[source["atom_id"]]
        after = effect["after"]
        if (source.get("path"), source.get("version"), source.get("sha256")) != (after["path"], after["version"], after["sha256"]):
            fail(f"current grammar source pin: {source['atom_id']}")
    return {"task": CURRENT_GRAMMAR_TASK, "report": report_pin, "receipt": receipt, "rows": rows_by_id,
            "counts": dict(sorted(decisions.items())), "sources": sorted(report_atoms)}


def run_negative_probes() -> None:
    """In-memory fail-closed probes; they never write project inputs or outputs."""
    baseline_source = {"relative_path": "core/CA-R-1.md", "atom_id": "CA-R-1", "version": 1, "full_file_sha256": "a" * 64}

    def require_rejection(label: str, callback: Any) -> None:
        try:
            callback()
        except ValueError:
            return
        fail(f"negative probe unexpectedly accepted: {label}")

    require_rejection(
        "unexpected_same_id_hash",
        lambda: validate_declared_drift([baseline_source], [{**baseline_source, "full_file_sha256": "b" * 64}], {}),
    )
    require_rejection(
        "unexpected_path_move",
        lambda: validate_declared_drift([baseline_source], [{**baseline_source, "relative_path": "core/moved-CA-R-1.md"}], {}),
    )
    require_rejection(
        "missing_current_source",
        lambda: validate_declared_drift([baseline_source], [], {}),
    )
    historic_occurrence = {"occurrence_id": "core/CA-R-1.md#subjects.governs", "source_atom_id": "CA-R-1", "field": "governs", "index": None, "old_value": "Atom"}
    current_occurrence = {"occurrence_id": "core/CA-R-2.md#subjects.governs", "source_atom_id": "CA-R-2", "field": "governs", "index": None, "old_value": "Atom"}
    require_rejection(
        "unapproved_occurrence_rebind",
        lambda: matched_origin(current_occurrence, {historic_occurrence["occurrence_id"]: historic_occurrence}, {("CA-R-1", "governs", None, "Atom"): [historic_occurrence]}, {}),
    )
    require_rejection(
        "changed_text_at_existing_occurrence_id",
        lambda: matched_origin({**historic_occurrence, "old_value": "Claim"}, {historic_occurrence["occurrence_id"]: historic_occurrence}, {}, {}),
    )
    validate_research_group_configuration(RESEARCH_LAYER_GROUPS)
    require_rejection(
        "research_group_omission",
        lambda: validate_research_group_configuration(RESEARCH_LAYER_GROUPS[:3]),
    )
    canonical_decision_record_pin({"operator_decision_record": pin(DECISION_RECORD)})
    unrelated_plan = Path(
        ".caprmedio_caprmedio/03_plan/18-CA-P-1959-EPIC--improve-entity-model-stage-2/"
        "08-CA-P-1966-EPIC--map-current-core-subject-origins/53-CA-P-2043-TASK--integrate-current-subject-mapping-ledger/"
        "02-CA-P-2045-TASK--integrate-reviewed-current-subject-mappings/"
        "010-CA-P-2109-TASK--integrate-accepted-subject-family-research.md"
    )
    require_rejection(
        "plan_descriptor_is_not_operator_decision_record",
        lambda: canonical_decision_record_pin({"operator_decision_record": pin(unrelated_plan)}),
    )
    for group in RESEARCH_LAYER_GROUPS:
        manifest = read_json(group.manifest)
        manifest_pin = pin(group.manifest)
        research_group_tasks(group, manifest, manifest_pin)  # valid control before adversarial copies
        missing_row_manifest = json.loads(json.dumps(manifest))
        missing_row_manifest["tasks"][0]["input_rows"].pop()
        require_rejection(
            f"{group.label}_manifest_missing_row",
            lambda group=group, manifest=missing_row_manifest, manifest_pin=manifest_pin:
                research_group_tasks(group, manifest, manifest_pin),
        )
        require_rejection(
            f"{group.label}_manifest_wrong_pin",
            lambda group=group, manifest=manifest, manifest_pin=manifest_pin:
                research_group_tasks(group, manifest, {"path": manifest_pin["path"], "sha256": "0" * 64}),
        )
    require_rejection(
        "missing_research_candidate_pointer",
        lambda: json_pointer({}, "/missing", "negative research pointer"),
    )


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    validate_research_group_configuration(RESEARCH_LAYER_GROUPS)
    baseline = read_json(BASELINE)
    if baseline.get("non_authoritative") is not True or baseline.get("source_migration") != "not_performed":
        fail("baseline ledger boundary")
    baseline_rows = baseline.get("occurrences")
    if not isinstance(baseline_rows, list) or len({row.get("occurrence_id") for row in baseline_rows}) != len(baseline_rows):
        fail("baseline occurrence coverage invalid")
    baseline_sources = baseline.get("source_reviews")
    if not isinstance(baseline_sources, list):
        fail("baseline source coverage invalid")
    baseline_by_id = {row["occurrence_id"]: row for row in baseline_rows}
    baseline_by_atom_field: dict[tuple[Any, Any, Any, Any], list[dict[str, Any]]] = {}
    for row in baseline_rows:
        key = (row.get("source_atom_id"), row.get("field"), row.get("index"), row.get("old_value"))
        baseline_by_atom_field.setdefault(key, []).append(row)
    drift = read_json(DRIFT)
    current_effects, replacement = declared_grammar_effects(drift)
    sources, current_rows, excluded, structure_pin = current_frontier()
    validate_declared_drift(baseline_sources, sources, current_effects)
    current_by_id = {row["occurrence_id"]: row for row in current_rows}
    if len(current_by_id) != len(current_rows):
        fail("duplicate current occurrence ID")
    current_body_evidence = {source["relative_path"]: source["body_evidence"] for source in sources}

    states: dict[str, dict[str, Any]] = {}
    matched_baseline_ids: set[str] = set()
    for current in current_rows:
        origin = matched_origin(current, baseline_by_id, baseline_by_atom_field, replacement)
        matched_baseline_ids.add(origin["occurrence_id"])
        source_unchanged = origin.get("source_sha256") == current.get("source_sha256")
        if not source_unchanged and current.get("source_atom_id") not in current_effects:
            fail(f"unexpected occurrence source hash drift: {current['occurrence_id']}")
        needs_recheck = current.get("source_atom_id") in current_effects
        state = {"decision": origin.get("decision"), "proposed_value": origin.get("proposed_value"),
                 "confidence": origin.get("confidence"), "reason": origin.get("reason"),
                 "evidence": origin.get("evidence", []), "candidate_basis": origin.get("candidate_basis", []),
                 "preserved_distinctions": origin.get("preserved_distinctions", []), "question": origin.get("question"),
                 "applied_layers": [{"layer": "baseline", "decision": origin.get("decision"),
                                     "proposed_value": origin.get("proposed_value"), "accepted": False,
                                     "reason": "Captured baseline retained as historical provenance, not independent follow-up acceptance."}],
                 "historical_origin": historical_origin(origin), "source_unchanged_from_baseline": source_unchanged}
        states[current["occurrence_id"]] = {"current": current, "state": state, "needs_recheck": needs_recheck}

    missing_current_counterparts = sorted(set(baseline_by_id).difference(matched_baseline_ids))
    if missing_current_counterparts:
        fail(f"frozen baseline occurrences missing current counterpart: {missing_current_counterparts[0]}")

    accepted_layers: list[dict[str, Any]] = []
    for priority, (task_id, report_rel, kind) in enumerate(LAYER_SPECS, start=1):
        report = read_json(report_rel)
        report_pin = pin(report_rel)
        if report.get("task_id") != task_id or report.get("non_authoritative") is not True:
            fail(f"layer report boundary: {task_id}")
        receipt = receipt_pin(task_id, report_pin)
        rows = list(layer_rows(kind, report))
        ids = [row.get("occurrence_id") for row in rows]
        if not all(isinstance(item, str) for item in ids) or len(set(ids)) != len(ids):
            fail(f"duplicate layer ownership: {task_id}")
        for row in rows:
            occurrence_id = row["occurrence_id"]
            if occurrence_id not in states:
                fail(f"layer occurrence missing current counterpart: {task_id} {occurrence_id}")
            decision, value, confidence = normalized_decision(kind, row)
            no_inferred_syntax(value)
            target = states[occurrence_id]["state"]
            target["applied_layers"].append({"layer": task_id, "priority": priority, "report": report_pin,
                                             "receipt": receipt, "decision": decision, "proposed_value": value,
                                             "accepted": decision == "proposed"})
            target.update({"decision": decision, "proposed_value": value, "confidence": confidence,
                           "reason": row.get("reason"), "evidence": row.get("evidence", []),
                           "candidate_basis": row.get("candidate_basis", []),
                           "preserved_distinctions": row.get("preserved_distinctions", []),
                           "question": row.get("question"), "selected_layer_row": {"task": task_id, "kind": kind}})
        accepted_layers.append({"task": task_id, "priority": priority, "report": report_pin, "receipt": receipt,
                                "rows": len(rows), "kind": kind})

    candidate = read_json(CANDIDATE)
    candidate_pin = pin(CANDIDATE)
    current_sources_by_path = source_index(sources, "current evidence")
    research_owned: set[str] = set()
    priority = len(LAYER_SPECS) + 1
    for group in RESEARCH_LAYER_GROUPS:
        manifest = read_json(group.manifest)
        manifest_pin = pin(group.manifest)
        group_tasks = research_group_tasks(group, manifest, manifest_pin)
        group_owned: set[str] = set()
        for specification in group.specifications:
            task_id = specification[0]
            report, receipt, descriptor = accepted_research_layer(
                group, specification, manifest_pin, group_tasks[task_id], baseline_by_id, current_by_id,
                current_sources_by_path, candidate, candidate_pin,
            )
            rows = list(layer_rows("research", report))
            ids = {row["occurrence_id"] for row in rows}
            if group_owned.intersection(ids) or research_owned.intersection(ids):
                fail(f"duplicate research layer ownership: {task_id}")
            group_owned.update(ids)
            research_owned.update(ids)
            for row in rows:
                occurrence_id = row["occurrence_id"]
                decision, value, confidence = normalized_decision("research", row)
                target = states[occurrence_id]["state"]
                target["applied_layers"].append({
                    "layer": task_id, "priority": priority, "report": descriptor["report"],
                    "receipt": receipt, "manifest": manifest_pin,
                    "independent_review_sha256": descriptor["independent_review_sha256"],
                    "decision": decision, "proposed_value": value, "confidence": confidence,
                    "accepted": decision == "proposed",
                })
                target.update({"decision": decision, "proposed_value": value, "confidence": confidence,
                               "reason": row["reason"], "evidence": row["evidence"],
                               "candidate_basis": row.get("candidate_basis", []),
                               "preserved_distinctions": row.get("preserved_distinctions", []),
                               "question": row.get("question"),
                               "selected_layer_row": {"task": task_id, "kind": "research"}})
            accepted_layers.append({**descriptor, "priority": priority})
            priority += 1
        if len(group_owned) != group.expected_rows:
            fail(f"research group total ownership: {group.label}")
    if len(research_owned) != sum(group.expected_rows for group in RESEARCH_LAYER_GROUPS):
        fail("research layer total ownership")

    actor_report = read_json(ACTOR_SUBSET)
    actor_pin = pin(ACTOR_SUBSET)
    actor_receipt = receipt_pin("CA-P-2058", actor_pin)
    actor_rows = actor_report.get("rows")
    if not isinstance(actor_rows, list) or len(actor_rows) != 43:
        fail("Actor subset coverage")
    for row in actor_rows:
        state = states.get(row.get("occurrence_id"))
        if state is None or state["state"].get("proposed_value") != row.get("proposed_value"):
            fail("Actor subset canonical target disagreement")
    accepted_layers.append({"task": "CA-P-2058", "priority": "coverage_only", "report": actor_pin,
                            "receipt": actor_receipt, "rows": 43, "kind": "canonical_target_check"})

    current_grammar = accepted_current_grammar_review(current_by_id, current_effects)
    grammar_rechecks: list[dict[str, Any]] = []
    grammar_review_rows: list[dict[str, Any]] = []
    for occurrence_id, record in states.items():
        if not record["needs_recheck"]:
            continue
        state = record["state"]
        if current_grammar is None:
            state["applied_layers"].append({"layer": CURRENT_GRAMMAR_TASK, "status": "not_independently_accepted",
                                            "decision": "unresolved", "proposed_value": None})
            state.update({"decision": "unresolved", "proposed_value": None, "confidence": 0.0,
                          "reason": "Current source is one of the five audited grammar changed/replaced sources; without independently accepted CA-P-2087 current-grammar Subject evidence its mapping is reset to null.",
                          "evidence": next(source["body_evidence"] for source in sources if source["relative_path"] == record["current"]["source_path"]),
                          "candidate_basis": [], "preserved_distinctions": ["Historical baseline and selected-layer hypotheses remain provenance only.", "No old source hash is treated as current semantic evidence.", "No selector or grammar rebind is inferred."], "question": None,
                          "current_source_semantic_recheck_required": True})
            grammar_rechecks.append({"occurrence_id": occurrence_id, "source_atom_id": record["current"].get("source_atom_id"),
                                     "source_path": record["current"]["source_path"]})
            continue
        review_row = current_grammar["rows"].get(occurrence_id)
        if review_row is None:
            fail(f"accepted current grammar row missing: {occurrence_id}")
        decision, value, confidence = review_row["decision"], review_row["proposed_value"], review_row["confidence"]
        state["applied_layers"].append({"layer": CURRENT_GRAMMAR_TASK, "status": "independently_accepted_current_grammar",
                                        "report": current_grammar["report"], "receipt": current_grammar["receipt"],
                                        "priority": "current_grammar",
                                        "decision": decision, "proposed_value": value, "confidence": confidence,
                                        "accepted": decision == "proposed"})
        state.update({"decision": decision, "proposed_value": value, "confidence": confidence,
                      "reason": review_row["reason"], "evidence": review_row["evidence"],
                      "candidate_basis": review_row.get("candidate_basis", []),
                      "preserved_distinctions": review_row.get("preserved_distinctions", []), "question": review_row.get("question"),
                      "selected_layer_row": {"task": CURRENT_GRAMMAR_TASK, "kind": "current_grammar"},
                      "current_source_semantic_recheck_required": False})
        grammar_review_rows.append({"occurrence_id": occurrence_id, "source_atom_id": record["current"].get("source_atom_id"),
                                    "source_path": record["current"]["source_path"], "decision": decision})

    if current_grammar is not None:
        accepted_layers.append({"task": CURRENT_GRAMMAR_TASK, "priority": "current_grammar",
                                "report": current_grammar["report"], "receipt": current_grammar["receipt"],
                                "rows": len(current_grammar["rows"]), "kind": "current_grammar_subject_recheck"})

    rows: list[dict[str, Any]] = []
    for occurrence_id in sorted(states):
        record = states[occurrence_id]
        current = record["current"]
        state = record["state"]
        decision = state.get("decision")
        value = state.get("proposed_value")
        confidence = state.get("confidence")
        if decision not in {"unchanged", "proposed", "unresolved"} or not isinstance(confidence, (int, float)):
            fail("final decision shape")
        if decision == "unresolved" and value is not None:
            fail("unresolved target must be null")
        if decision in {"unchanged", "proposed"} and (not isinstance(value, str) or confidence < 0.90):
            fail("decided target invalid")
        no_inferred_syntax(value)
        evidence = list(state.get("evidence", []))
        selected_layer = state.get("selected_layer_row")
        if isinstance(selected_layer, dict) and selected_layer.get("kind") == "research":
            if not any(isinstance(item, dict) and current_span_matches(item, current) for item in evidence):
                fail("accepted research owning evidence unavailable at emission")
        elif decision != "unresolved":
            live = current_body_evidence.get(current["source_path"])
            if not live:
                fail("current source evidence unavailable")
            if not any(item.get("path") == live[0]["path"] and item.get("sha256") == live[0]["sha256"]
                       and item.get("span_sha256") == live[0]["span_sha256"] for item in evidence if isinstance(item, dict)):
                evidence.extend(live)
        row = {**current, **state, "evidence": evidence, "executable": False}
        historic = row.get("historical_origin")
        if isinstance(historic, dict) and (historic.get("occurrence_id") != current["occurrence_id"] or historic.get("source_sha256") != current["source_sha256"]):
            row["replacement_lineage"] = {
                "historic_occurrence_id": historic.get("occurrence_id"),
                "current_occurrence_id": current["occurrence_id"],
                "historic_source_sha256": historic.get("source_sha256"),
                "current_source_sha256": current["source_sha256"],
                "field": current["field"], "index": current["index"], "old_value": current["old_value"],
            }
        rows.append(row)
    decisions = Counter(row["decision"] for row in rows)
    source_by_path = {source["relative_path"]: source for source in sources}
    source_rows = []
    for path, source in sorted(source_by_path.items()):
        source_rows.append({key: value for key, value in source.items() if key != "body_evidence"})

    input_pins = {"baseline": pin(BASELINE), "grammar_drift": pin(DRIFT), "structure": structure_pin,
                  "contracts": [pin(item) for item in CONTRACTS], "accepted_layers": accepted_layers}
    diagnostic = {
        "schema_version": 1, "task_id": "CA-P-2086", "non_authoritative": True,
        "source_migration": "not_performed", "native_admission": "not_performed",
        "counts": {"current_sources": len(sources), "current_occurrences": len(rows),
                   "quarantined_sources": sum(source["quarantined"] for source in sources),
                   "quarantined_occurrences": sum(row["quarantined"] for row in rows),
                   "grammar_recheck_occurrences": len(grammar_rechecks),
                   "accepted_current_grammar_occurrences": len(grammar_review_rows),
                   "missing_baseline_counterparts": 0,
                   "missing_current_counterparts": len(missing_current_counterparts),
                   "decisions": dict(sorted(decisions.items()))},
        "grammar_recheck_required": grammar_rechecks, "accepted_current_grammar_rows": grammar_review_rows,
        "missing_baseline_counterparts": [],
        "missing_current_counterparts": missing_current_counterparts,
        "excluded_sources": excluded,
        "limits": ["CA-P-2087 current-grammar conclusions apply only when its independently accepted receipt/report pins validate; otherwise all five grammar changed/replaced source occurrences are explicit nulls.", "This derived draft is not migration approval or native admission."],
    }
    frontier = {"schema_version": 1, "task_id": "CA-P-2086", "non_authoritative": True,
                "source_migration": "not_performed", "native_admission": "not_performed",
                "input_pins": {"structure": structure_pin, "grammar_drift": pin(DRIFT)},
                "authority_path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL",
                "selected_sources": source_rows, "excluded_sources": excluded,
                "occurrence_count": len(rows)}
    ledger = {"schema_version": 1, "task_id": "CA-P-2086", "non_authoritative": True,
              "source_migration": "not_performed", "native_admission": "not_performed",
              "scope": "Create-only current-frontier working mapping ledger; not semantic final acceptance or source migration.",
              "input_pins": input_pins,
              "layer_priority": [item[0] for item in LAYER_SPECS]
              + [item[0] for group in RESEARCH_LAYER_GROUPS for item in group.specifications]
              + ["CA-P-2058 coverage_only", "CA-P-2087 accepted_current_grammar" if current_grammar is not None else "CA-P-2087 recheck_gate"],
              "counts": {"sources": len(source_rows), "occurrences": len(rows), "quarantined_sources": sum(source["quarantined"] for source in source_rows),
                         "quarantined_occurrences": sum(row["quarantined"] for row in rows), "decisions": dict(sorted(decisions.items())),
                         "unresolved": decisions["unresolved"], "grammar_recheck_required": len(grammar_rechecks),
                         "accepted_current_grammar_occurrences": len(grammar_review_rows)},
              "source_reviews": source_rows, "occurrences": rows,
              "remaining_gaps": {"diagnostics_path": (WORKING / "diagnostics.json").as_posix(), "grammar_recheck_occurrences": len(grammar_rechecks),
                                 "unresolved_occurrences": decisions["unresolved"]}}
    return ledger, frontier, diagnostic


def write_create_only(values: dict[Path, dict[str, Any]]) -> None:
    for relative in values:
        target = checked_relative_path(relative, "derived output")
        if target.exists() or target.is_symlink():
            fail(f"create-only output already exists: {relative}")
        if target.parent.exists() and target.parent.is_symlink():
            fail(f"unsafe output parent: {target.parent}")
    for relative, value in values.items():
        target = checked_relative_path(relative, "derived output")
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            with target.open("xb") as handle:
                handle.write(json_bytes(value))
        except FileExistsError as error:
            raise ValueError(f"create-only output already exists: {relative}") from error


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--persist", action="store_true", help="create three working-ledger drafts once")
    parser.add_argument("--negative-probes", action="store_true", help="run isolated fail-closed drift probes without project I/O")
    args = parser.parse_args(argv)
    try:
        if args.negative_probes:
            if args.persist:
                fail("negative probes cannot persist outputs")
            run_negative_probes()
            print(json.dumps({"outcome": "NEGATIVE_PROBES_PASS"}, sort_keys=True))
            return 0
        ledger, frontier, diagnostic = build()
        if args.persist:
            write_create_only({LEDGER: ledger, FRONTIER: frontier, DIAGNOSTICS: diagnostic})
        print(json.dumps({"outcome": "CREATED" if args.persist else "PREVIEW", "counts": ledger["counts"],
                          "would_create": [path.as_posix() for path in (LEDGER, FRONTIER, DIAGNOSTICS)]}, sort_keys=True))
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(json.dumps({"outcome": "FAIL", "reason": str(error)}, sort_keys=True), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
