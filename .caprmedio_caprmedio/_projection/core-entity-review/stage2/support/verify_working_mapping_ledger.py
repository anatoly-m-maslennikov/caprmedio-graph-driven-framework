"""Independent verifier for the derived CA-P-2086 working Subject ledger.

This module deliberately does not import the consolidator.  It re-enumerates
the active Core RMEDO frontier through the strict carrier parser, then checks
that the derived files preserve that frontier and make every current Subject
occurrence accountable.  It is a read-only acceptance gate, not a mapping
producer or a source writer.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tomllib
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[5]
STAGE2_REL = Path(".caprmedio_caprmedio/_projection/core-entity-review/stage2")
WORKING_REL = STAGE2_REL / "working-ledger"
LEDGER_REL = WORKING_REL / "working-mapping-ledger.json"
FRONTIER_REL = WORKING_REL / "source-frontier.json"
DIAGNOSTICS_REL = WORKING_REL / "diagnostics.json"
BASELINE_REL = STAGE2_REL / "current-subjects.mapping-ledger.json"
GRAMMAR_DRIFT_REL = STAGE2_REL / "current-grammar-source-drift.json"
ACTOR_SUBSET_REL = STAGE2_REL / "semantic-reviews/task-2058.accepted-subset.json"
GRAMMAR_REPORT_REL = STAGE2_REL / "semantic-reviews/current-grammar-subjects.review.json"
GRAMMAR_RECEIPT_REL = STAGE2_REL / "task-2087.receipt.json"
FOLLOWUP_MANIFEST_REL = STAGE2_REL / "semantic-reviews/followups-2094-2099.inputs.json"
FOLLOWUP_MANIFEST_SHA256 = "5e9ed02cadeccf6b46dcea33593db65c8540c7cf77ce984a3d2502d8f00c3a3d"
SECOND_FOLLOWUP_MANIFEST_REL = STAGE2_REL / "semantic-reviews/followups-2103-2108.inputs.json"
SECOND_FOLLOWUP_MANIFEST_SHA256 = "7babc00405598a0af98c21bc2de69d4db04e9d59672d9746aa048f2f17a44ef3"
THIRD_FOLLOWUP_MANIFEST_REL = STAGE2_REL / "semantic-reviews/followups-2112-2117.inputs.json"
THIRD_FOLLOWUP_MANIFEST_SHA256 = "397b371532dc4f1fb684649ffe3ef6728e955c3825939ab9ee35e76047381bd5"
FOURTH_FOLLOWUP_MANIFEST_REL = STAGE2_REL / "semantic-reviews/followups-2121-2128.inputs.json"
FOURTH_FOLLOWUP_MANIFEST_SHA256 = "311058fd59732975cbe9c3662c6eb93dc2231d192a66c33bc416a4ee83084c5f"
FIFTH_FOLLOWUP_MANIFEST_REL = STAGE2_REL / "semantic-reviews/followups-2132-2139.inputs.json"
FIFTH_FOLLOWUP_MANIFEST_SHA256 = "a115ac2b55f88698a057bec8f13c9bbfba72105cb56bc2a7d606ff6360214cfd"
OPERATOR_DECISION_REL = STAGE2_REL / "operator.subject-decisions.2026-10-11.json"
OPERATOR_DECISION_SHA256 = "743fd63f5c8c8ea19b0f1ffae1fa1d89d81504308c7f5345e2809fe7cef15ffc"
STRUCTURE_REL = Path(".caprmedio_caprmedio/project_structure.toml")
VALIDATOR_ROOT = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS"
if str(VALIDATOR_ROOT) not in sys.path:
    sys.path.insert(0, str(VALIDATOR_ROOT))

from validate_atoms_workers.parsing import CarrierError, parse_carrier  # noqa: E402


ROLES = {"Requirement", "Method", "Evaluation", "Delivery", "Operations"}
ROLE_DIRS = {
    "04_requirement": "Requirement",
    "05_method": "Method",
    "06_evaluation": "Evaluation",
    "07_delivery": "Delivery",
    "09_operations": "Operations",
    "09_ops": "Operations",
}
ROLE_BY_ID_KIND = {"R": "Requirement", "M": "Method", "E": "Evaluation", "D": "Delivery", "O": "Operations"}
ATOM_ID_RE = re.compile(r"^CA-([RMEDO])-([0-9]+)$")
FILENAME_ID_RE = re.compile(r"^(CA-([RMEDO])-[0-9]+)(?:-|$)")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
FORBIDDEN_TARGET_RE = re.compile(r"[@\[\]{}()=]")
LAYER_SPECS = (
    ("CA-P-2048", "substance"),
    ("CA-P-2072", "semantic"), ("CA-P-2073", "semantic"),
    ("CA-P-2074", "semantic"), ("CA-P-2075", "semantic"),
    ("CA-P-2076", "semantic"),
    ("CA-P-2078", "research"), ("CA-P-2079", "research"),
    ("CA-P-2080", "research"), ("CA-P-2082", "research"),
    ("CA-P-2083", "research"), ("CA-P-2084", "research"),
    ("CA-P-2085", "research"),
)
FOLLOWUP_LAYER_SPECS = (
    ("CA-P-2094", "research", 27, 21, 6, "265356c22829b6416f1d27c57969f509fec260f1e46dce99d8a7f3cc0219e3b5"),
    ("CA-P-2095", "research", 28, 8, 20, "42a578818395cbe4e2f5fe5d997745058af39ff38ab02a3f84d8096cb674690d"),
    ("CA-P-2096", "research", 41, 21, 20, "fa53f20f59f5bb9b75223fa407e8233a00d74ae2a962002657d30713da7fd1e7"),
    ("CA-P-2097", "research", 25, 14, 11, "7a24becd960411a50eeb6ef344df0599c817820376453cdfbc6511c15495ae04"),
    ("CA-P-2098", "research", 32, 1, 31, "ab4acfbfdf3ea8addfdfee7fc4502b5e84a4808ec91499da82dfd9bebc3784b2"),
    ("CA-P-2099", "research", 27, 15, 12, "0e50e15645a4d56385a240ca47179b1c708ec839aecd4a81c4acfcdc13f4e69b"),
)
SECOND_FOLLOWUP_LAYER_SPECS = (
    ("CA-P-2103", "research", 26, 23, 3, "22db7aa281823d7e01c58454bcc52ee7060d5ffe24a12396e62e6e952f28071c"),
    ("CA-P-2104", "research", 31, 17, 14, "d19ad7f585610a10910c4b0355aaca1743a670adb3b56c96114a0cfd5d35a5f4"),
    ("CA-P-2105", "research", 41, 22, 19, "40a2d1c26cc6b617b49ac109172c99996de6727401e99326d17bf89f2adf492e"),
    ("CA-P-2106", "research", 25, 9, 16, "109edfd87f6f788658a210e561e034275dff6b49df34357b5d386340ba3e8204"),
    ("CA-P-2107", "research", 26, 4, 22, "149a9a3c35f2c4c3a08733e9dac790093d4c592da428f5bbfd262fbb396c458a"),
    ("CA-P-2108", "research", 34, 25, 9, "eb40f1fc810edb418f3acdeec8ce798837109264e45a966d348c86b810945da5"),
)
THIRD_FOLLOWUP_LAYER_SPECS = (
    ("CA-P-2112", "research", 17, 8, 9, "e65fe0ec394ca5655ee23052d869467aab0a632abede70d3311b86425f58b3d7"),
    ("CA-P-2113", "research", 27, 24, 3, "97dae252cfe7cdfce21864bb38bf3bb12fc0c2a2ef489edd668387faa4415a6c"),
    ("CA-P-2114", "research", 28, 9, 19, "c4a3db04a629185cddf1b56b2f52860b14262eb3d42a92aa68d43a5af4e3ade7"),
    ("CA-P-2115", "research", 24, 9, 15, "cbad7db5ae4f00f397f67eb240d593596402fcb8bc02a247bdfd2b78abcf75b3"),
    ("CA-P-2116", "research", 15, 13, 2, "90d3027a973bd4ff6ecfbe8c6d2288744513df48cf99d6be1c38a3fccf9ce50d"),
    ("CA-P-2117", "research", 26, 24, 2, "d49221d9c8468f92b0f8144f879163538cc438699b5145fe2f36ed18bd8ffb8f"),
)
FOURTH_FOLLOWUP_LAYER_SPECS = (
    ("CA-P-2121", "research", 22, 21, 1, "96d906b7769f52f32bfc4b8d1ccfb638ba5eee6c525bcc2e25851827fb4f693b"),
    ("CA-P-2122", "research", 20, 8, 12, "3577856baf8a35c61c479c9d2feaa7e54f0252ec2f33f5ec9bb94def9eb928f8"),
    ("CA-P-2123", "research", 28, 7, 21, "64c5e84639b39c37d7a175c11e967b407dfabbd840b76a80bc91352dd29e8728"),
    ("CA-P-2124", "research", 33, 7, 26, "94b9b57e83a2b23bd493355ece510907ed31277edab45dc56e9ee5eefacfe9e3"),
    ("CA-P-2125", "research", 29, 7, 22, "43bca8f0776c3d7ff25321e4e9c6b3da10b3bd5c3333c0cb0a8dbb9d1af7aeb3"),
    ("CA-P-2126", "research", 21, 11, 10, "3fa0af8d302898a399cb1406cd9bcfcdd7ee22d3e3bc28f907f322e935dd8c52"),
    ("CA-P-2127", "research", 23, 7, 16, "db250a76d1b6f5b4a8226a44656a81eb16e57965faa174c3b7f5a1337f638896"),
    ("CA-P-2128", "research", 29, 3, 26, "12aff3f78128cb401ec7f070840d0958a9edcd0e20266f9a0acb231fa8220f56"),
)
FIFTH_FOLLOWUP_LAYER_SPECS = (
    ("CA-P-2132", "research", 22, 2, 20, "2c79d4e3114f6db167acda343fecd0762eab6a78988e43f534f575661ffc35d2"),
    ("CA-P-2133", "research", 20, 9, 11, "90b13cf54d48ec1f60c21bf778e27ff9f0a794599a37e769612d9ef3cff46445"),
    ("CA-P-2134", "research", 25, 11, 14, "12805a8750a8b3840870416c0a742ceaf74e312c1bd71444f076a6b558b50303"),
    ("CA-P-2135", "research", 19, 16, 3, "e4ca2241b187c266061078a216d2128e7d5b8350903b9fbc298f7aa72e30ba9f"),
    ("CA-P-2136", "research", 37, 2, 35, "30ad47d268d8927561d78fe36860eafafaacc888d0408be1f79457f062aa7975"),
    ("CA-P-2137", "research", 29, 7, 22, "d89d428d4262410bdb1bf1a833dd28b9bb6186bb153eaa6abf58c9157e39b113"),
    ("CA-P-2138", "research", 23, 6, 17, "709b2e24e1e2c6961ef804c0a44460f1d1e1105fcdd49ae47096164b9c888c83"),
    ("CA-P-2139", "research", 20, 10, 10, "1c07b8e41e299861b4a507e5f977bbff9e7b4adde19c9f9df4a3fd59a544fb83"),
)
# CA-P-2143 withdraws the foreign-evidence CA-P-2133 report.  The successor
# path and independently accepted final hash are intentionally closed.  This
# is not an alias: the old report remains immutable historical evidence and
# must not be read as the fifth-group CA-P-2133 layer again.
FIFTH_SUCCESSOR_BINDINGS = {
    "CA-P-2133": {
        "report": STAGE2_REL / "semantic-reviews/task-2133.core-only.research.json",
        "receipt": STAGE2_REL / "task-2133.core-only.receipt.json",
        "supersedes": {
            "path": (STAGE2_REL / "semantic-reviews/task-2133.research.json").as_posix(),
            "sha256": "90b13cf54d48ec1f60c21bf778e27ff9f0a794599a37e769612d9ef3cff46445",
        },
        "predecessor_receipt": {
            "path": (STAGE2_REL / "task-2133.receipt.json").as_posix(),
            "sha256": "ce54fe83aae0618a624f044c54ac4b1c8e1557edf5bbd4ee0255f697c05b6a71",
        },
        "successor_task": "CA-P-2143",
        "report_revision": 2,
        "registration_commit": "5814a20c8d7b27b45b383409b35e4f0dfda5cefc",
        "successor_registration_commit": "74f96a6901765d5a854db87f8180655e3fb922ea",
        "successor_contract": {
            "path": (STAGE2_REL / "working-ledger.core-only-successor-2143.contract.md").as_posix(),
            "sha256": "9019dada59adeb3f23dd2cc114600bc7fd5e9d72daa49034dd9390d46214d7a0",
        },
        "final_report_sha256": "4d87d8cfe5376d23d37580b09019b9169b6bd75c976d749f67f10b8840926893",
    },
}
FOLLOWUP_TASKS = {task for task, _kind, _rows, _proposed, _unresolved, _sha256 in FOLLOWUP_LAYER_SPECS}
SECOND_FOLLOWUP_TASKS = {task for task, _kind, _rows, _proposed, _unresolved, _sha256 in SECOND_FOLLOWUP_LAYER_SPECS}
THIRD_FOLLOWUP_TASKS = {task for task, _kind, _rows, _proposed, _unresolved, _sha256 in THIRD_FOLLOWUP_LAYER_SPECS}
FOURTH_FOLLOWUP_TASKS = {task for task, _kind, _rows, _proposed, _unresolved, _sha256 in FOURTH_FOLLOWUP_LAYER_SPECS}
FIFTH_FOLLOWUP_TASKS = {task for task, _kind, _rows, _proposed, _unresolved, _sha256 in FIFTH_FOLLOWUP_LAYER_SPECS}
ALL_FOLLOWUP_TASKS = FOLLOWUP_TASKS | SECOND_FOLLOWUP_TASKS | THIRD_FOLLOWUP_TASKS | FOURTH_FOLLOWUP_TASKS | FIFTH_FOLLOWUP_TASKS
LATER_FOLLOWUP_TASKS = SECOND_FOLLOWUP_TASKS | THIRD_FOLLOWUP_TASKS | FOURTH_FOLLOWUP_TASKS | FIFTH_FOLLOWUP_TASKS
LATER_FOLLOWUP_PROOF_FIELDS = ("evidence", "candidate_basis", "preserved_distinctions")
LAYER_PRIORITY = [task for task, _kind in LAYER_SPECS] + ["CA-P-2058 coverage_only", "CA-P-2087 recheck_gate"]
GRAMMAR_ACCEPTED_PRIORITY = "CA-P-2087 accepted_current_grammar"
ORDINARY_LAYER_PRIORITY = {
    **{task: index for index, (task, _kind) in enumerate(LAYER_SPECS, start=1)},
    **{task: len(LAYER_SPECS) + index for index, (task, _kind, _rows, _proposed, _unresolved, _sha256) in enumerate(FOLLOWUP_LAYER_SPECS, start=1)},
    **{task: len(LAYER_SPECS) + len(FOLLOWUP_LAYER_SPECS) + index for index, (task, _kind, _rows, _proposed, _unresolved, _sha256) in enumerate(SECOND_FOLLOWUP_LAYER_SPECS, start=1)},
    **{task: len(LAYER_SPECS) + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS) + index for index, (task, _kind, _rows, _proposed, _unresolved, _sha256) in enumerate(THIRD_FOLLOWUP_LAYER_SPECS, start=1)},
    **{task: len(LAYER_SPECS) + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS) + len(THIRD_FOLLOWUP_LAYER_SPECS) + index for index, (task, _kind, _rows, _proposed, _unresolved, _sha256) in enumerate(FOURTH_FOLLOWUP_LAYER_SPECS, start=1)},
    **{task: len(LAYER_SPECS) + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS) + len(THIRD_FOLLOWUP_LAYER_SPECS) + len(FOURTH_FOLLOWUP_LAYER_SPECS) + index for index, (task, _kind, _rows, _proposed, _unresolved, _sha256) in enumerate(FIFTH_FOLLOWUP_LAYER_SPECS, start=1)},
}


class VerificationError(AssertionError):
    """A deterministic, concise acceptance-gate failure."""


def require(condition: bool, label: str) -> None:
    if not condition:
        raise VerificationError(label)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _is_sha(value: Any) -> bool:
    return isinstance(value, str) and SHA_RE.fullmatch(value) is not None


def _layer_layout(ledger: dict[str, Any]) -> tuple[tuple[tuple[str, str, int, int], ...], int, int | None]:
    """Describe the accepted-layer manifest without accepting arbitrary additions.

    The historical working draft remains a valid input until CA-P-2102 performs
    its controlled replacement. A replacement appends only complete fixed
    report groups after the thirteen ordinary layers, then preserves the
    Actor coverage check and final grammar recheck. A partial extension is
    deliberately invalid.
    """

    pins = ledger.get("input_pins")
    accepted = pins.get("accepted_layers") if isinstance(pins, dict) else None
    require(isinstance(accepted, list), "accepted layer manifest list")
    base_count = len(LAYER_SPECS)
    old_without_grammar = base_count + 1
    old_with_grammar = base_count + 2
    first_followup_with_grammar = base_count + 1 + len(FOLLOWUP_LAYER_SPECS) + 1
    second_followup_with_grammar = first_followup_with_grammar + len(SECOND_FOLLOWUP_LAYER_SPECS)
    third_followup_with_grammar = second_followup_with_grammar + len(THIRD_FOLLOWUP_LAYER_SPECS)
    fourth_followup_with_grammar = third_followup_with_grammar + len(FOURTH_FOLLOWUP_LAYER_SPECS)
    fifth_followup_with_grammar = fourth_followup_with_grammar + len(FIFTH_FOLLOWUP_LAYER_SPECS)
    base = tuple((task, kind, position, position + 1) for position, (task, kind) in enumerate(LAYER_SPECS))
    if len(accepted) == old_without_grammar:
        return base, base_count, None
    if len(accepted) == old_with_grammar:
        return base, base_count, base_count + 1
    followup = tuple(
        (task, kind, base_count + index, base_count + index + 1)
        for index, (task, kind, _rows, _proposed, _unresolved, _sha256) in enumerate(FOLLOWUP_LAYER_SPECS)
    )
    if len(accepted) == first_followup_with_grammar:
        return base + followup, base_count + len(FOLLOWUP_LAYER_SPECS), first_followup_with_grammar - 1
    second_followup = tuple(
        (task, kind, base_count + len(FOLLOWUP_LAYER_SPECS) + index, base_count + len(FOLLOWUP_LAYER_SPECS) + index + 1)
        for index, (task, kind, _rows, _proposed, _unresolved, _sha256) in enumerate(SECOND_FOLLOWUP_LAYER_SPECS)
    )
    if len(accepted) == second_followup_with_grammar:
        return base + followup + second_followup, base_count + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS), second_followup_with_grammar - 1
    third_followup = tuple(
        (task, kind, base_count + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS) + index, base_count + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS) + index + 1)
        for index, (task, kind, _rows, _proposed, _unresolved, _sha256) in enumerate(THIRD_FOLLOWUP_LAYER_SPECS)
    )
    if len(accepted) == third_followup_with_grammar:
        return base + followup + second_followup + third_followup, base_count + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS) + len(THIRD_FOLLOWUP_LAYER_SPECS), third_followup_with_grammar - 1
    fourth_followup = tuple(
        (task, kind, base_count + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS) + len(THIRD_FOLLOWUP_LAYER_SPECS) + index, base_count + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS) + len(THIRD_FOLLOWUP_LAYER_SPECS) + index + 1)
        for index, (task, kind, _rows, _proposed, _unresolved, _sha256) in enumerate(FOURTH_FOLLOWUP_LAYER_SPECS)
    )
    if len(accepted) == fourth_followup_with_grammar:
        return base + followup + second_followup + third_followup + fourth_followup, base_count + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS) + len(THIRD_FOLLOWUP_LAYER_SPECS) + len(FOURTH_FOLLOWUP_LAYER_SPECS), fourth_followup_with_grammar - 1
    fifth_followup = tuple(
        (task, kind, base_count + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS) + len(THIRD_FOLLOWUP_LAYER_SPECS) + len(FOURTH_FOLLOWUP_LAYER_SPECS) + index, base_count + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS) + len(THIRD_FOLLOWUP_LAYER_SPECS) + len(FOURTH_FOLLOWUP_LAYER_SPECS) + index + 1)
        for index, (task, kind, _rows, _proposed, _unresolved, _sha256) in enumerate(FIFTH_FOLLOWUP_LAYER_SPECS)
    )
    require(len(accepted) == fifth_followup_with_grammar, "complete accepted-layer manifest")
    return base + followup + second_followup + third_followup + fourth_followup + fifth_followup, base_count + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS) + len(THIRD_FOLLOWUP_LAYER_SPECS) + len(FOURTH_FOLLOWUP_LAYER_SPECS) + len(FIFTH_FOLLOWUP_LAYER_SPECS), fifth_followup_with_grammar - 1


def _require_followup_extension_when_receipts_exist(root: Path, ledger: dict[str, Any]) -> None:
    """Do not let a live accepted receipt silently fall back to the old draft."""

    first_receipts_exist = any((root / STAGE2_REL / f"task-{task.removeprefix('CA-P-')}.receipt.json").is_file() for task in FOLLOWUP_TASKS)
    second_receipts_exist = any((root / STAGE2_REL / f"task-{task.removeprefix('CA-P-')}.receipt.json").is_file() for task in SECOND_FOLLOWUP_TASKS)
    third_receipts_exist = any((root / STAGE2_REL / f"task-{task.removeprefix('CA-P-')}.receipt.json").is_file() for task in THIRD_FOLLOWUP_TASKS)
    fourth_receipts_exist = any((root / STAGE2_REL / f"task-{task.removeprefix('CA-P-')}.receipt.json").is_file() for task in FOURTH_FOLLOWUP_TASKS)
    fifth_receipts_exist = any((root / STAGE2_REL / f"task-{task.removeprefix('CA-P-')}.receipt.json").is_file() for task in FIFTH_FOLLOWUP_TASKS)
    specs, _actor_position, _grammar_position = _layer_layout(ledger)
    admitted = {task for task, _kind, _position, _priority in specs}
    if first_receipts_exist:
        require(FOLLOWUP_TASKS <= admitted, "accepted first follow-up extension required")
    if second_receipts_exist:
        require(FOLLOWUP_TASKS <= admitted and SECOND_FOLLOWUP_TASKS <= admitted, "accepted second follow-up extension required")
    if third_receipts_exist:
        require(FOLLOWUP_TASKS <= admitted and SECOND_FOLLOWUP_TASKS <= admitted and THIRD_FOLLOWUP_TASKS <= admitted, "accepted third follow-up extension required")
    if fourth_receipts_exist:
        require(FOLLOWUP_TASKS <= admitted and SECOND_FOLLOWUP_TASKS <= admitted and THIRD_FOLLOWUP_TASKS <= admitted and FOURTH_FOLLOWUP_TASKS <= admitted, "accepted fourth follow-up extension required")
    if fifth_receipts_exist:
        require(FOLLOWUP_TASKS <= admitted and SECOND_FOLLOWUP_TASKS <= admitted and THIRD_FOLLOWUP_TASKS <= admitted and FOURTH_FOLLOWUP_TASKS <= admitted and FIFTH_FOLLOWUP_TASKS <= admitted, "accepted fifth follow-up extension required")


def relative_path(root: Path, value: Any, label: str) -> Path:
    require(isinstance(value, str) and value and not Path(value).is_absolute(), f"{label} relative path")
    relative = Path(value)
    require(".." not in relative.parts, f"{label} path traversal")
    candidate = root / relative
    try:
        candidate.resolve(strict=False).relative_to(root.resolve())
        relative = candidate.relative_to(root)
    except ValueError as error:
        raise VerificationError(f"{label} escapes repository root") from error
    probe = root
    for part in relative.parts:
        probe /= part
        require(not probe.is_symlink(), f"{label} symlink")
    return candidate


def read_json(path: Path, label: str) -> dict[str, Any]:
    require(path.is_file() and not path.is_symlink(), f"{label} exists as regular file")
    try:
        value = json.loads(path.read_bytes())
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise VerificationError(f"{label} valid JSON") from error
    require(isinstance(value, dict), f"{label} JSON object")
    return value


def _updated_at(frontmatter: str) -> tuple[str | None, str]:
    match = re.search(r"(?m)^updated_at:\s*(.*?)\s*$", frontmatter)
    if match is None:
        return None, "missing"
    text = match.group(1).strip()
    return text.strip("\"'"), "quoted" if text[:1] in "\"'" else "plain"


def _directory_role(source_root: Path, path: Path) -> str | None:
    for component in path.relative_to(source_root).parts[:-1]:
        if component in ROLE_DIRS:
            return ROLE_DIRS[component]
    return None


def current_authority_path(root: Path) -> tuple[Path, Path]:
    structure = relative_path(root, STRUCTURE_REL.as_posix(), "authoritative Structure")
    require(structure.is_file(), "authoritative Structure exists")
    try:
        document = tomllib.loads(structure.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, tomllib.TOMLDecodeError) as error:
        raise VerificationError("authoritative Structure parses as TOML") from error
    rows = document.get("scope_units") if isinstance(document, dict) else None
    require(isinstance(rows, list), "Structure scope_units list")
    matches = [row for row in rows if isinstance(row, dict) and row.get("scope_unit_name") == "CORE_META_MODEL"]
    require(len(matches) == 1, "one CORE_META_MODEL Structure row")
    source_root = relative_path(root, matches[0].get("authority_path"), "CORE_META_MODEL authority")
    require(source_root.is_dir(), "CORE_META_MODEL authority directory")
    return structure, source_root


def enumerate_current_frontier(root: Path) -> dict[str, Any]:  # noqa: C901 - mirrors the strict frontier partition deliberately.
    """Strictly reconstruct active Core RMEDO sources and Subject occurrences."""

    structure, source_root = current_authority_path(root)
    selected: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []
    diagnostics: list[dict[str, Any]] = []
    occurrences: list[dict[str, Any]] = []
    for path in sorted(source_root.rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        if "archive" in path.parts:
            excluded.append({"relative_path": rel, "reason": "archived_lifecycle_copy"})
            continue
        raw = path.read_bytes()
        try:
            parsed = parse_carrier(raw, path)
            metadata = parsed.metadata
        except CarrierError as error:
            filename_match = FILENAME_ID_RE.match(path.stem)
            if filename_match is None:
                excluded.append({"relative_path": rel, "reason": "strict_parse_error", "code": error.code, "detail": str(error)})
            else:
                selected.append({
                    "relative_path": rel, "full_file_sha256": sha(raw), "atom_id": None,
                    "filename_atom_id": filename_match.group(1), "version": None,
                    "role": ROLE_BY_ID_KIND[filename_match.group(2)], "owner": None,
                    "author": None, "status": None, "updated_at": None,
                    "updated_at_type": "unavailable", "quarantined": True,
                    "findings": [f"strict_parse_error:{error.code}"],
                })
            continue
        role = metadata.get("content_role")
        scope = metadata.get("current_scope_unit")
        status = metadata.get("status")
        if scope != "CORE_META_MODEL":
            excluded.append({"relative_path": rel, "reason": "owner_mismatch", "content_role": role, "current_scope_unit": scope, "status": status})
            diagnostics.append({"relative_path": rel, "code": "owner_mismatch", "expected": "CORE_META_MODEL", "actual": scope})
            continue
        if status != "Active":
            excluded.append({"relative_path": rel, "reason": "not_active_lifecycle", "content_role": role, "current_scope_unit": scope, "status": status})
            continue
        if role not in ROLES:
            excluded.append({"relative_path": rel, "reason": "not_rmedo_role", "content_role": role, "current_scope_unit": scope, "status": status})
            continue
        updated_at, _ = _updated_at(parsed.frontmatter)
        findings: list[str] = []
        atom_id = metadata.get("atom_id")
        atom_match = ATOM_ID_RE.fullmatch(atom_id) if isinstance(atom_id, str) else None
        if atom_match is None or int(atom_match.group(2)) < 1:
            findings.append("missing_or_invalid_atom_id")
        else:
            if ROLE_BY_ID_KIND[atom_match.group(1)] != role:
                findings.append("atom_id_role_mismatch")
            if not (path.stem == atom_id or path.stem.startswith(f"{atom_id}-")):
                findings.append("filename_atom_id_mismatch")
        if _directory_role(source_root, path) != role:
            findings.append("directory_role_mismatch")
        if not isinstance(metadata.get("version"), int) or isinstance(metadata.get("version"), bool) or metadata["version"] <= 0:
            findings.append("missing_or_invalid_version")
        if updated_at is None:
            findings.append("missing_updated_at")
        if not isinstance(metadata.get("updated_at"), str) or not re.search(r"(?:[+-]\d{2}:?\d{2}|Z)$", updated_at or ""):
            findings.append("updated_at_invalid_or_naive")
        subjects = metadata.get("subjects")
        valid_subjects: list[tuple[str, int | None, str]] = []
        if not isinstance(subjects, dict):
            findings.append("subjects_not_mapping")
            subjects = {}
        governs = subjects.get("governs")
        if isinstance(governs, str) and governs.strip():
            valid_subjects.append(("governs", None, governs))
        else:
            findings.append("governs_missing_or_invalid")
        depends_on = subjects.get("depends_on")
        if depends_on is not None:
            if isinstance(depends_on, list) and all(isinstance(value, str) and value.strip() for value in depends_on) and len(set(depends_on)) == len(depends_on):
                valid_subjects.extend(("depends_on", index, value) for index, value in enumerate(depends_on))
            else:
                findings.append("depends_on_missing_or_invalid_unique_string_list")
        full_sha = sha(raw)
        selected.append({
            "relative_path": rel, "full_file_sha256": full_sha, "atom_id": atom_id,
            "version": metadata.get("version"), "role": role, "owner": scope,
            "author": metadata.get("author"), "status": status, "updated_at": updated_at,
            "updated_at_type": type(metadata.get("updated_at")).__name__,
            "quarantined": bool(findings), "findings": findings,
        })
        for field, index, old_value in valid_subjects:
            suffix = f"subjects.{field}" + (f"[{index}]" if index is not None else "")
            occurrences.append({
                "occurrence_id": f"{rel}#{suffix}", "source_path": rel,
                "source_atom_id": atom_id, "source_version": metadata.get("version"),
                "source_sha256": full_sha, "field": field, "index": index,
                "old_value": old_value, "quarantined": bool(findings),
            })
    counts: dict[str, int] = {}
    for source in selected:
        if isinstance(source["atom_id"], str) and ATOM_ID_RE.fullmatch(source["atom_id"]):
            counts[source["atom_id"]] = counts.get(source["atom_id"], 0) + 1
    duplicate_paths: set[str] = set()
    for atom_id in sorted(atom_id for atom_id, count in counts.items() if count > 1):
        copies = [source for source in selected if source["atom_id"] == atom_id]
        for source in copies:
            source["findings"].append("duplicate_atom_id")
            source["quarantined"] = True
            duplicate_paths.add(source["relative_path"])
        diagnostics.append({"code": "duplicate_atom_id", "atom_id": atom_id, "relative_paths": [source["relative_path"] for source in copies]})
    quarantined_paths = {source["relative_path"] for source in selected if source["quarantined"]} | duplicate_paths
    for occurrence in occurrences:
        occurrence["quarantined"] = occurrence["source_path"] in quarantined_paths
    selected.sort(key=lambda value: value["relative_path"])
    excluded.sort(key=lambda value: value["relative_path"])
    diagnostics.sort(key=lambda value: (value.get("relative_path", ""), value["code"]))
    occurrences.sort(key=lambda value: value["occurrence_id"])
    return {
        "structure_path": structure.relative_to(root).as_posix(),
        "structure_sha256": sha(structure.read_bytes()),
        "selected_sources": selected, "excluded_sources": excluded,
        "diagnostics": diagnostics, "occurrences": occurrences,
    }


def _source_view(source: dict[str, Any]) -> dict[str, Any]:
    """The compact derived frontier must preserve every source truth it exposes."""

    return {key: source.get(key) for key in (
        "relative_path", "full_file_sha256", "atom_id", "version", "role", "owner",
        "status", "quarantined", "findings",
    )}


def _verify_frontier(root: Path, frontier: dict[str, Any], expected: dict[str, Any]) -> None:
    require(frontier.get("schema_version") == 1, "frontier schema version")
    require(frontier.get("non_authoritative") is True, "frontier non-authoritative")
    require(frontier.get("source_migration") == "not_performed", "frontier source migration")
    require(frontier.get("native_admission") == "not_performed", "frontier native admission")
    pins = frontier.get("input_pins")
    require(isinstance(pins, dict) and pins.get("structure") == {
        "path": expected["structure_path"], "sha256": expected["structure_sha256"],
    }, "frontier live Structure pin")
    require(frontier.get("selected_sources") == [_source_view(source) for source in expected["selected_sources"]], "exact current frontier source pins")
    excluded = frontier.get("excluded_sources")
    require(isinstance(excluded, list), "frontier excluded source list")
    require({item.get("relative_path") for item in excluded if isinstance(item, dict)} == {item["relative_path"] for item in expected["excluded_sources"]}, "exact current excluded source coverage")
    require(frontier.get("occurrence_count") == len(expected["occurrences"]), "frontier occurrence count")


def _span_matches(root: Path, evidence: dict[str, Any], expected: dict[str, Any], label: str) -> bool:
    if not isinstance(evidence, dict) or evidence.get("path") != expected["source_path"] or evidence.get("sha256") != expected["source_sha256"]:
        return False
    start, end = evidence.get("start_line"), evidence.get("end_line")
    if not isinstance(start, int) or isinstance(start, bool) or not isinstance(end, int) or isinstance(end, bool) or start < 1 or end < start or not _is_sha(evidence.get("span_sha256")):
        return False
    path = relative_path(root, evidence["path"], label)
    if not path.is_file() or sha(path.read_bytes()) != evidence["sha256"]:
        return False
    lines = path.read_bytes().splitlines(keepends=True)
    return end <= len(lines) and sha(b"".join(lines[start - 1 : end])) == evidence["span_sha256"]


def _later_followup_evidence_is_current(
    root: Path,
    evidence: dict[str, Any],
    current_source_pins: dict[str, str],
    label: str,
) -> bool:
    """Accept only a current Core source or the exact Operator decision record.

    This deliberately applies only to CA-P-2103--2117. Earlier accepted
    layers retain their historical verifier boundary, while these two later
    groups must prove every supporting span that their accepted reports rely on.
    """

    if not isinstance(evidence, dict):
        return False
    evidence_path = evidence.get("path")
    if not isinstance(evidence_path, str):
        return False
    expected_sha = current_source_pins.get(evidence_path)
    if expected_sha is None:
        expected_sha = OPERATOR_DECISION_SHA256 if evidence_path == OPERATOR_DECISION_REL.as_posix() else None
    if expected_sha is None:
        return False
    return _span_matches(root, evidence, {"source_path": evidence_path, "source_sha256": expected_sha}, label)


def _verify_lineage(
    row: dict[str, Any],
    expected: dict[str, Any],
    baseline_rows: dict[str, dict[str, Any]],
    grammar_effects: dict[str, dict[str, Any]],
    label: str,
) -> dict[str, Any]:
    historic = row.get("historical_origin")
    require(isinstance(historic, dict), f"{label} historical origin")
    historic_id = historic.get("occurrence_id")
    require(isinstance(historic_id, str) and historic_id in baseline_rows, f"{label} baseline historic occurrence")
    baseline = baseline_rows[historic_id]
    for field in ("occurrence_id", "source_path", "source_atom_id", "source_version", "source_sha256", "field", "index", "old_value", "quarantined", "decision", "proposed_value", "confidence"):
        require(historic.get(field) == baseline.get(field), f"{label} exact frozen baseline {field}")
    require(historic["field"] == expected["field"] and historic["index"] == expected["index"] and historic["old_value"] == expected["old_value"], f"{label} exact counterpart field/index/text")
    changed = historic["occurrence_id"] != expected["occurrence_id"] or historic["source_sha256"] != expected["source_sha256"]
    same_source_identity = historic["source_atom_id"] == expected["source_atom_id"] and historic["source_path"] == expected["source_path"]
    if not changed:
        require(same_source_identity and historic["source_version"] == expected["source_version"], f"{label} unchanged exact source counterpart")
    if changed:
        effect = grammar_effects.get(expected["source_atom_id"])
        require(isinstance(effect, dict), f"{label} declared grammar source change")
        before, after = effect.get("before"), effect.get("after")
        require(isinstance(before, dict) and isinstance(after, dict), f"{label} declared grammar before/after")
        require(after.get("path") == expected["source_path"] and after.get("version") == expected["source_version"] and after.get("sha256") == expected["source_sha256"], f"{label} declared grammar current source")
        require(before.get("path") == historic["source_path"] and before.get("version") == historic["source_version"] and before.get("sha256") == historic["source_sha256"], f"{label} declared grammar historic source")
        if same_source_identity:
            require(effect.get("operation") == "revise_active_atom", f"{label} same-ID grammar revision")
        else:
            require(effect.get("operation") == "replace_with_new_id" and effect.get("atom_id") == historic["source_atom_id"] and after.get("atom_id") == expected["source_atom_id"], f"{label} sole declared replacement counterpart")
        lineage = row.get("replacement_lineage")
        require(isinstance(lineage, dict), f"{label} replacement lineage")
        require(lineage.get("historic_occurrence_id") == historic["occurrence_id"], f"{label} lineage historic occurrence")
        require(lineage.get("current_occurrence_id") == expected["occurrence_id"], f"{label} lineage current occurrence")
        require(lineage.get("historic_source_sha256") == historic["source_sha256"], f"{label} lineage historic pin")
        require(lineage.get("current_source_sha256") == expected["source_sha256"], f"{label} lineage current pin")
        require(lineage.get("field") == expected["field"] and lineage.get("index") == expected["index"] and lineage.get("old_value") == expected["old_value"], f"{label} lineage field/index/text")
    return baseline


def _normalized_layer_row(kind: str, row: dict[str, Any], label: str) -> tuple[str, str | None, float]:
    if kind == "semantic":
        disposition = row.get("disposition")
        if disposition == "accepted":
            target, confidence = row.get("proposed_value"), row.get("confidence")
            require(isinstance(target, str) and target and isinstance(confidence, (int, float)) and not isinstance(confidence, bool) and confidence >= .9, f"{label} accepted semantic value")
            return "proposed", target, float(confidence)
        require(disposition in {"rejected", "unresolved", "stale"}, f"{label} semantic disposition")
        return "unresolved", None, 0.0
    decision = row.get("decision")
    if decision == "proposed":
        target, confidence = row.get("proposed_value"), row.get("confidence")
        require(isinstance(target, str) and target and isinstance(confidence, (int, float)) and not isinstance(confidence, bool) and confidence >= .9, f"{label} proposed value")
        return "proposed", target, float(confidence)
    require(decision in {"unresolved", "rejected", "stale"}, f"{label} layer decision")
    confidence = row.get("confidence")
    return "unresolved", None, float(confidence) if isinstance(confidence, (int, float)) and not isinstance(confidence, bool) else 0.0


def _verify_later_followup_final_proof(row: dict[str, Any], references: dict[str, Any], label: str) -> None:
    """Ensure a later-group decision retains its accepted report proof fields."""

    proofs = references.get("proofs")
    require(isinstance(proofs, dict) and row["occurrence_id"] in proofs, f"{label} later follow-up proof provenance")
    proof = proofs[row["occurrence_id"]]
    require(isinstance(proof, dict), f"{label} later follow-up proof mapping")
    for field in LATER_FOLLOWUP_PROOF_FIELDS:
        require(row.get(field) == proof.get(field), f"{label} later follow-up preserved {field}")


def _verify_layers(
    row: dict[str, Any],
    label: str,
    layer_rows: dict[str, dict[str, tuple[str, str | None, float]]],
    baseline: dict[str, Any] | None,
    grammar_effects: dict[str, dict[str, Any]],
    accepted_grammar_rows: dict[str, tuple[str, str | None, float]] | None,
    layer_refs: dict[str, dict[str, dict[str, str]]],
) -> None:
    layers = row.get("applied_layers")
    require(isinstance(layers, list), f"{label} applied layers")
    required = (["baseline"] if baseline is not None else []) + [
        task for task in ORDINARY_LAYER_PRIORITY if row["occurrence_id"] in layer_rows.get(task, {})
    ]
    if row["source_atom_id"] in grammar_effects:
        required.append("CA-P-2087")
    require([layer.get("layer") if isinstance(layer, dict) else None for layer in layers] == required, f"{label} complete selected-layer sequence")
    final_decision, final_target, final_confidence = ("unresolved", None, 0.0)
    if baseline is not None:
        final_decision = baseline["decision"]
        final_target = baseline["proposed_value"]
        final_confidence = float(baseline["confidence"])
    for index, layer in enumerate(layers):
        require(isinstance(layer, dict), f"{label} layer mapping")
        task = layer.get("layer")
        if task == "baseline":
            require(index == 0 and layer.get("accepted") is False, f"{label} baseline lineage only")
            require(layer.get("decision") == final_decision and layer.get("proposed_value") == final_target, f"{label} baseline decision/target")
        elif task == "CA-P-2087":
            require(index == len(layers) - 1, f"{label} grammar recheck final layer")
            if accepted_grammar_rows is None:
                require(layer.get("status") == "not_independently_accepted", f"{label} grammar recheck gate")
                require(layer.get("decision") == "unresolved" and layer.get("proposed_value") is None, f"{label} grammar recheck null")
                final_decision, final_target, final_confidence = "unresolved", None, 0.0
            else:
                expected = accepted_grammar_rows.get(row["occurrence_id"])
                require(expected is not None and layer.get("priority") == "current_grammar", f"{label} accepted grammar layer")
                decision, target, confidence = expected
                references = layer_refs.get("CA-P-2087")
                require(isinstance(references, dict), f"{label} accepted grammar manifest provenance")
                require(layer.get("status") == "independently_accepted_current_grammar" and layer.get("report") == references.get("report") and layer.get("receipt") == references.get("receipt"), f"{label} accepted grammar provenance")
                require(layer.get("decision") == decision and layer.get("proposed_value") == target and layer.get("confidence") == confidence, f"{label} accepted grammar target/confidence")
                final_decision, final_target, final_confidence = decision, target, confidence
        else:
            require(isinstance(task, str) and task in layer_rows, f"{label} known accepted layer")
            rank = layer.get("priority")
            require(rank == ORDINARY_LAYER_PRIORITY[task], f"{label} accepted layer priority")
            expected = layer_rows[task].get(row["occurrence_id"])
            require(expected is not None, f"{label} selected layer occurrence")
            decision, target, confidence = expected
            references = layer_refs.get(task)
            require(isinstance(references, dict), f"{label} layer manifest provenance")
            require(layer.get("report") == references.get("report") and layer.get("receipt") == references.get("receipt"), f"{label} layer provenance")
            if "independent_review_sha256" in references:
                require(layer.get("independent_review_sha256") == references["independent_review_sha256"], f"{label} layer independent-review provenance")
            if task in LATER_FOLLOWUP_TASKS:
                _verify_later_followup_final_proof(row, references, label)
            require(layer.get("decision") == decision and layer.get("proposed_value") == target, f"{label} layer target")
            if task in ALL_FOLLOWUP_TASKS:
                require(layer.get("confidence") == confidence, f"{label} layer confidence")
            final_decision, final_target, final_confidence = decision, target, confidence
    require(row.get("decision") == final_decision, f"{label} final selected-layer decision")
    require(row.get("proposed_value") == final_target, f"{label} final selected-layer target")
    require(row.get("confidence") == final_confidence, f"{label} final selected-layer confidence")


def _verify_rows(
    root: Path,
    rows: Any,
    expected: list[dict[str, Any]],
    baseline_rows: dict[str, dict[str, Any]],
    layer_rows: dict[str, dict[str, tuple[str, str | None, float]]],
    actor_targets: dict[str, str],
    grammar_effects: dict[str, dict[str, Any]],
    accepted_grammar_rows: dict[str, tuple[str, str | None, float]] | None,
    layer_refs: dict[str, dict[str, dict[str, str]]],
) -> dict[str, int]:
    require(isinstance(rows, list), "ledger rows list")
    expected_by_id = {row["occurrence_id"]: row for row in expected}
    actual_by_id: dict[str, dict[str, Any]] = {}
    for number, row in enumerate(rows):
        label = f"ledger row {number}"
        require(isinstance(row, dict), f"{label} mapping")
        occurrence_id = row.get("occurrence_id")
        require(isinstance(occurrence_id, str) and occurrence_id in expected_by_id, f"{label} expected occurrence")
        require(occurrence_id not in actual_by_id, f"{label} duplicate occurrence")
        actual_by_id[occurrence_id] = row
    require(set(actual_by_id) == set(expected_by_id), "exact current occurrence coverage")
    counts = {"proposed": 0, "unchanged": 0, "unresolved": 0}
    for occurrence_id, expected_row in expected_by_id.items():
        row = actual_by_id[occurrence_id]
        label = f"ledger occurrence {occurrence_id}"
        require({key: row.get(key) for key in expected_row} == expected_row, f"{label} exact current origin/pin")
        decision = row.get("decision")
        require(decision in counts, f"{label} explicit decision")
        target = row.get("proposed_value")
        if decision == "proposed":
            require(isinstance(target, str) and target.strip(), f"{label} proposal target")
            require(FORBIDDEN_TARGET_RE.search(target) is None and "selector" not in target.lower(), f"{label} inferred selector or at target")
            require(isinstance(row.get("confidence"), (int, float)) and not isinstance(row.get("confidence"), bool) and .9 <= row["confidence"] <= 1, f"{label} proposal confidence")
        elif decision == "unchanged":
            require(isinstance(target, str) and target.strip(), f"{label} unchanged target")
            require(isinstance(row.get("confidence"), (int, float)) and not isinstance(row.get("confidence"), bool) and .9 <= row["confidence"] <= 1, f"{label} unchanged confidence")
        else:
            require(target is None, f"{label} explicit null target")
            require(isinstance(row.get("confidence"), (int, float)) and not isinstance(row.get("confidence"), bool) and 0 <= row["confidence"] < .9, f"{label} non-proposal confidence")
        require(row.get("executable") is False, f"{label} non-executable")
        require(isinstance(row.get("reason"), str) and row["reason"].strip(), f"{label} reason")
        baseline = _verify_lineage(row, expected_row, baseline_rows, grammar_effects, label)
        _verify_layers(row, label, layer_rows, baseline, grammar_effects, accepted_grammar_rows, layer_refs)
        if occurrence_id in actor_targets:
            require(decision == "proposed" and target == actor_targets[occurrence_id], f"{label} Actor canonical target")
        if decision != "unresolved":
            evidence = row.get("evidence")
            require(isinstance(evidence, list) and any(_span_matches(root, item, expected_row, label) for item in evidence), f"{label} live current source span")
        counts[decision] += 1
    return counts


def _layer_path(task: str) -> Path:
    if task == "CA-P-2048":
        return STAGE2_REL / "supplements/substance.review.json"
    suffix = ".review.json" if task in {"CA-P-2072", "CA-P-2073", "CA-P-2074", "CA-P-2075", "CA-P-2076"} else ".research.json"
    return STAGE2_REL / "semantic-reviews" / f"task-{task.removeprefix('CA-P-')}{suffix}"


def _followup_artifact_paths(task: str) -> tuple[Path, Path]:
    """Return the only report/receipt paths accepted for a follow-up task."""

    binding = FIFTH_SUCCESSOR_BINDINGS.get(task)
    if binding is not None:
        return binding["report"], binding["receipt"]
    return _layer_path(task), STAGE2_REL / f"task-{task.removeprefix('CA-P-')}.receipt.json"


def _followup_expected_report_sha256(task: str, default: str) -> str:
    """Refuse a successor until its separately accepted final hash is bound."""

    binding = FIFTH_SUCCESSOR_BINDINGS.get(task)
    if binding is None:
        return default
    value = binding.get("final_report_sha256")
    require(_is_sha(value), f"successor final report hash bound {task}")
    return value


def _verify_followup_successor_binding(
    root: Path,
    task: str,
    report: dict[str, Any],
    receipt: dict[str, Any],
    report_pin: dict[str, str],
) -> None:
    """Ensure a withdrawn report cannot return through a generic task path."""

    binding = FIFTH_SUCCESSOR_BINDINGS.get(task)
    if binding is None:
        return
    predecessor = binding["supersedes"]
    predecessor_relative = Path(predecessor["path"])
    predecessor_path = relative_path(root, predecessor_relative.as_posix(), f"successor predecessor report {task}")
    require(predecessor_path.is_file() and not predecessor_path.is_symlink(), f"successor predecessor report exists {task}")
    require(_descriptor(predecessor_path, predecessor_relative) == predecessor, f"successor predecessor report pin {task}")
    predecessor_receipt = binding["predecessor_receipt"]
    predecessor_receipt_relative = Path(predecessor_receipt["path"])
    predecessor_receipt_path = relative_path(root, predecessor_receipt_relative.as_posix(), f"successor predecessor receipt {task}")
    require(predecessor_receipt_path.is_file() and not predecessor_receipt_path.is_symlink(), f"successor predecessor receipt exists {task}")
    require(_descriptor(predecessor_receipt_path, predecessor_receipt_relative) == predecessor_receipt, f"successor predecessor receipt pin {task}")
    contract = binding["successor_contract"]
    contract_relative = Path(contract["path"])
    contract_path = relative_path(root, contract_relative.as_posix(), f"successor contract {task}")
    require(contract_path.is_file() and not contract_path.is_symlink(), f"successor contract exists {task}")
    require(_descriptor(contract_path, contract_relative) == contract, f"successor contract pin {task}")
    report_path = binding["report"].as_posix()
    receipt_path = binding["receipt"].as_posix()
    require(report_pin.get("path") == report_path, f"successor report path {task}")
    require(
        report.get("successor_task") == binding["successor_task"]
        and report.get("report_revision") == binding["report_revision"]
        and report.get("supersedes") == binding["supersedes"],
        f"successor report lineage {task}",
    )
    verification = receipt.get("verification")
    require(
        receipt.get("successor_task") == binding["successor_task"]
        and receipt.get("registration_commit") == binding["registration_commit"]
        and receipt.get("successor_registration_commit") == binding["successor_registration_commit"]
        and receipt.get("successor_contract") == binding["successor_contract"]
        and receipt.get("supersedes") == binding["supersedes"]
        and isinstance(verification, dict)
        and verification.get("task") == task
        and verification.get("successor_task") == binding["successor_task"]
        and verification.get("registration_commit") == binding["registration_commit"]
        and verification.get("successor_registration_commit") == binding["successor_registration_commit"]
        and verification.get("supersedes") == binding["supersedes"]
        and verification.get("output") == report_pin,
        f"successor receipt lineage {task}",
    )
    require(receipt_path.endswith("task-2133.core-only.receipt.json"), f"successor receipt path {task}")


def _descriptor(path: Path, relative: Path) -> dict[str, str]:
    return {"path": relative.as_posix(), "sha256": sha(path.read_bytes())}


def _read_baseline_rows(root: Path, ledger: dict[str, Any]) -> dict[str, dict[str, Any]]:
    path = relative_path(root, BASELINE_REL.as_posix(), "frozen baseline")
    baseline = read_json(path, "frozen baseline")
    pins = ledger.get("input_pins")
    require(isinstance(pins, dict) and pins.get("baseline") == _descriptor(path, BASELINE_REL), "frozen baseline pin")
    rows = baseline.get("occurrences")
    require(isinstance(rows, list), "frozen baseline occurrences")
    mapped: dict[str, dict[str, Any]] = {}
    for number, row in enumerate(rows):
        require(isinstance(row, dict) and isinstance(row.get("occurrence_id"), str), f"frozen baseline row {number}")
        occurrence_id = row["occurrence_id"]
        require(occurrence_id not in mapped, "frozen baseline duplicate occurrence")
        require(row.get("decision") in {"unchanged", "proposed", "unresolved"}, f"frozen baseline decision {occurrence_id}")
        mapped[occurrence_id] = row
    return mapped


def _grammar_effects(root: Path, ledger: dict[str, Any]) -> dict[str, dict[str, Any]]:
    path = relative_path(root, GRAMMAR_DRIFT_REL.as_posix(), "grammar drift")
    drift = read_json(path, "grammar drift")
    pins = ledger.get("input_pins")
    require(isinstance(pins, dict) and pins.get("grammar_drift") == _descriptor(path, GRAMMAR_DRIFT_REL), "grammar drift pin")
    records = drift.get("changed_or_missing")
    require(isinstance(records, list) and len(records) == 5, "five grammar effects")
    effects: dict[str, dict[str, Any]] = {}
    for number, record in enumerate(records):
        require(isinstance(record, dict) and record.get("classified") == "approved_grammar_effect", f"grammar effect {number}")
        atom_id = record.get("atom_id")
        effect = record.get("declared_effect")
        require(isinstance(atom_id, str) and isinstance(effect, dict), f"grammar effect {number} shape")
        if effect.get("operation") == "replace_with_new_id":
            after = effect.get("after")
            require(isinstance(after, dict) and isinstance(after.get("atom_id"), str), f"grammar replacement {number}")
            effects[after["atom_id"]] = effect
        else:
            require(effect.get("operation") == "revise_active_atom", f"grammar revision {number}")
            effects[atom_id] = effect
    require(len(effects) == 5, "five current grammar source identities")
    return effects


def _read_accepted_grammar_rows(
    root: Path,
    ledger: dict[str, Any],
    expected_occurrences: list[dict[str, Any]],
    grammar_effects: dict[str, dict[str, Any]],
) -> dict[str, tuple[str, str | None, float]] | None:
    pins = ledger.get("input_pins")
    accepted = pins.get("accepted_layers") if isinstance(pins, dict) else None
    specs, _actor_position, grammar_position = _layer_layout(ledger)
    require(isinstance(accepted, list), "accepted layer manifest")
    if grammar_position is None:
        receipt_path = relative_path(root, GRAMMAR_RECEIPT_REL.as_posix(), "accepted grammar receipt")
        require(not receipt_path.exists(), "accepted grammar manifest required when receipt exists")
        return None
    require(len(specs) in {
        len(LAYER_SPECS),
        len(LAYER_SPECS) + len(FOLLOWUP_LAYER_SPECS),
        len(LAYER_SPECS) + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS),
        len(LAYER_SPECS) + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS) + len(THIRD_FOLLOWUP_LAYER_SPECS),
        len(LAYER_SPECS) + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS) + len(THIRD_FOLLOWUP_LAYER_SPECS) + len(FOURTH_FOLLOWUP_LAYER_SPECS),
        len(LAYER_SPECS) + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS) + len(THIRD_FOLLOWUP_LAYER_SPECS) + len(FOURTH_FOLLOWUP_LAYER_SPECS) + len(FIFTH_FOLLOWUP_LAYER_SPECS),
    }, "accepted grammar ordinary layers")
    item = accepted[grammar_position]
    require(isinstance(item, dict) and item.get("task") == "CA-P-2087" and item.get("priority") == "current_grammar" and item.get("kind") == "current_grammar_subject_recheck" and item.get("rows") == 33, "accepted grammar manifest")
    report_path = relative_path(root, GRAMMAR_REPORT_REL.as_posix(), "accepted grammar report")
    receipt_path = relative_path(root, GRAMMAR_RECEIPT_REL.as_posix(), "accepted grammar receipt")
    report = read_json(report_path, "accepted grammar report")
    receipt = read_json(receipt_path, "accepted grammar receipt")
    report_pin = _descriptor(report_path, GRAMMAR_REPORT_REL)
    receipt_pin = _descriptor(receipt_path, GRAMMAR_RECEIPT_REL)
    require(item.get("report") == report_pin and item.get("receipt") == receipt_pin, "accepted grammar report/receipt pins")
    verification = receipt.get("verification")
    independent = receipt.get("independent_review")
    require(receipt.get("task") == "CA-P-2087" and isinstance(receipt.get("result"), str) and receipt["result"].startswith("PASS") and receipt.get("non_authoritative") is True, "accepted grammar receipt identity")
    require(isinstance(verification, dict) and verification.get("task") == "CA-P-2087" and verification.get("output") == report_pin and verification.get("rows") == 33 and verification.get("current_sources") == 5 and verification.get("counts") == {"proposed": 15, "unresolved": 18} and str(verification.get("root_mechanical_checks", "")).startswith("PASS"), "accepted grammar receipt verification")
    require(isinstance(independent, dict) and independent.get("reviewed_output_sha256") == report_pin["sha256"] and independent.get("accepted_proposals") == 15 and independent.get("correct_unresolved") == 18 and isinstance(independent.get("result"), str) and independent["result"].startswith("PASS"), "accepted grammar independent receipt")
    require(report.get("schema_version") == 1 and report.get("task_id") == "CA-P-2087" and report.get("non_authoritative") is True and report.get("source_migration") == "not_performed" and report.get("native_admission") == "not_performed", "accepted grammar report boundary")
    rows = report.get("occurrences")
    expected_by_id = {row["occurrence_id"]: row for row in expected_occurrences if row["source_atom_id"] in grammar_effects}
    require(isinstance(rows, list) and len(rows) == 33 and len(expected_by_id) == 33 and report.get("counts", {}).get("occurrences") == 33 and report.get("counts", {}).get("proposed") == 15 and report.get("counts", {}).get("unresolved") == 18, "accepted grammar exact coverage/counts")
    mapped: dict[str, tuple[str, str | None, float]] = {}
    for number, row in enumerate(rows):
        require(isinstance(row, dict), f"accepted grammar row {number}")
        occurrence_id = row.get("occurrence_id")
        require(isinstance(occurrence_id, str) and occurrence_id in expected_by_id and occurrence_id not in mapped, f"accepted grammar occurrence {number}")
        expected = expected_by_id[occurrence_id]
        require({key: row.get(key) for key in expected} == expected, f"accepted grammar current origin {occurrence_id}")
        decision, target, confidence = _normalized_layer_row("research", row, f"accepted grammar row {number}")
        require(row.get("executable") is False and any(_span_matches(root, evidence, expected, f"accepted grammar row {number}") for evidence in row.get("evidence", []) if isinstance(evidence, dict)), f"accepted grammar current evidence {occurrence_id}")
        mapped[occurrence_id] = (decision, target, confidence)
    require(set(mapped) == set(expected_by_id), "accepted grammar exact occurrence identities")
    return mapped


def _verify_receipt(task: str, kind: str, receipt: dict[str, Any], report_pin: dict[str, str]) -> None:
    require(receipt.get("task") == task and isinstance(receipt.get("result"), str) and receipt["result"].startswith("PASS"), f"accepted receipt identity {task}")
    if task == "CA-P-2048":
        checks = receipt.get("checks")
        require(receipt.get("output") == report_pin and isinstance(checks, dict), "CA-P-2048 output receipt")
        require(str(checks.get("independent_semantic_review", "")).startswith("PASS") and str(checks.get("independent_supplement_checker", "")).startswith("PASS"), "CA-P-2048 independent acceptance")
        return
    verification = receipt.get("verification")
    require(receipt.get("non_authoritative") is True and isinstance(verification, dict) and verification.get("task") == task, f"accepted receipt boundary {task}")
    if kind == "semantic":
        require(verification.get("review") == report_pin, f"semantic receipt output {task}")
        require(isinstance(receipt.get("review_method"), str) and "Independent" in receipt["review_method"], f"semantic receipt review method {task}")
        return
    require(verification.get("output") == report_pin and isinstance(verification.get("result"), str) and verification["result"].startswith("PASS"), f"research receipt output {task}")
    independent = receipt.get("independent_review")
    require(isinstance(independent, dict) and isinstance(independent.get("result"), str) and independent["result"].startswith("PASS"), f"research receipt independent review {task}")
    reviewed_sha = independent.get("reviewed_output_sha256")
    if reviewed_sha != report_pin["sha256"]:
        normalized = receipt.get("formatting_normalization")
        normalized_reviewed = normalized.get("reviewed_output_sha256") if isinstance(normalized, dict) else None
        if normalized_reviewed is None and isinstance(normalized, dict):
            normalized_reviewed = normalized.get("independently_reviewed_output_sha256")
        require(isinstance(normalized, dict) and normalized_reviewed == reviewed_sha and normalized.get("final_output_sha256") == report_pin["sha256"] and normalized.get("exact_reverse_hash_and_json_value_equality") == "PASS", f"research receipt normalization {task}")


def _read_followup_manifest(
    root: Path,
    expected_by_id: dict[str, dict[str, Any]],
    baseline_rows: dict[str, dict[str, Any]],
    specs: tuple[tuple[str, str, int, int, int, str], ...] = FOLLOWUP_LAYER_SPECS,
    manifest_relative: Path = FOLLOWUP_MANIFEST_REL,
    manifest_sha256: str = FOLLOWUP_MANIFEST_SHA256,
    label: str = "first follow-up",
    historical_working_ledger_sha256: str = "9c16ba32e74cb51cbd4c63cf3b938a57f614f55ca2650d54af2d6ed15b92088d",
) -> dict[str, list[dict[str, Any]]]:
    """Read the fixed selection independently of a derived working-ledger draft."""

    path = relative_path(root, manifest_relative.as_posix(), f"{label} selection manifest")
    raw = path.read_bytes()
    require(sha(raw) == manifest_sha256, f"{label} selection manifest pin")
    manifest = read_json(path, f"{label} selection manifest")
    require(manifest.get("schema_version") == 1 and manifest.get("non_authoritative") is True, f"{label} selection envelope")
    require(manifest.get("source_migration") == "not_performed" and manifest.get("native_admission") == "not_performed", f"{label} selection boundary")
    require(manifest.get("working_ledger") == {"path": LEDGER_REL.as_posix(), "sha256": historical_working_ledger_sha256}, f"{label} historical working-ledger context")
    tasks = manifest.get("tasks")
    require(isinstance(tasks, list) and len(tasks) == len(specs), f"{label} task coverage")
    selected: dict[str, list[dict[str, Any]]] = {}
    all_ids: set[str] = set()
    for position, (task, _kind, row_count, _proposed, _unresolved, _report_sha) in enumerate(specs):
        item = tasks[position]
        require(isinstance(item, dict) and item.get("task_id") == task and item.get("occurrences") == row_count, f"{label} manifest task {task}")
        rows = item.get("input_rows")
        require(isinstance(rows, list) and len(rows) == row_count, f"{label} manifest rows {task}")
        mapped: list[dict[str, Any]] = []
        for number, row in enumerate(rows):
            require(isinstance(row, dict), f"{label} manifest {task} row {number}")
            occurrence_id = row.get("occurrence_id")
            require(isinstance(occurrence_id, str) and occurrence_id in expected_by_id and occurrence_id not in all_ids, f"{label} manifest current occurrence {task} row {number}")
            expected = expected_by_id[occurrence_id]
            require({key: row.get(key) for key in expected} == expected, f"{label} manifest current origin {occurrence_id}")
            baseline = baseline_rows.get(occurrence_id)
            require(isinstance(baseline, dict) and baseline.get("decision") == "unresolved" and baseline.get("proposed_value") is None, f"{label} manifest baseline-only unresolved {occurrence_id}")
            all_ids.add(occurrence_id)
            mapped.append(expected)
        selected[task] = mapped
    require(len(all_ids) == sum(spec[2] for spec in specs), f"{label} exact selected occurrence count")
    return selected


def _read_followup_layer_rows(
    root: Path,
    ledger: dict[str, Any],
    expected_occurrences: list[dict[str, Any]],
    baseline_rows: dict[str, dict[str, Any]],
    specs: tuple[tuple[str, str, int, int, int, str], ...] = FOLLOWUP_LAYER_SPECS,
    manifest_relative: Path = FOLLOWUP_MANIFEST_REL,
    manifest_sha256: str = FOLLOWUP_MANIFEST_SHA256,
    offset: int = len(LAYER_SPECS),
    label: str = "first follow-up",
    historical_working_ledger_sha256: str = "9c16ba32e74cb51cbd4c63cf3b938a57f614f55ca2650d54af2d6ed15b92088d",
    verify_supporting_evidence: bool = False,
) -> tuple[dict[str, dict[str, tuple[str, str | None, float]]], dict[str, dict[str, Any]]]:
    """Verify all six accepted reports, receipts, live evidence, and selection ownership."""

    expected_by_id = {row["occurrence_id"]: row for row in expected_occurrences}
    current_source_pins = {row["source_path"]: row["source_sha256"] for row in expected_occurrences}
    selected = _read_followup_manifest(root, expected_by_id, baseline_rows, specs, manifest_relative, manifest_sha256, label, historical_working_ledger_sha256)
    _specs, _actor_position, _grammar_position = _layer_layout(ledger)
    pins = ledger.get("input_pins")
    accepted = pins.get("accepted_layers") if isinstance(pins, dict) else None
    require(isinstance(accepted, list), "follow-up accepted manifest")
    output: dict[str, dict[str, tuple[str, str | None, float]]] = {}
    references: dict[str, dict[str, Any]] = {}
    for index, (task, kind, row_count, proposed_count, unresolved_count, report_sha) in enumerate(specs):
        priority = ORDINARY_LAYER_PRIORITY[task]
        item = accepted[offset + index]
        require(isinstance(item, dict) and item.get("task") == task and item.get("kind") == kind and item.get("priority") == priority and item.get("rows") == row_count, f"{label} accepted manifest {task}")
        report_relative, receipt_relative = _followup_artifact_paths(task)
        report_path = relative_path(root, report_relative.as_posix(), f"{label} {task} report")
        receipt_path = relative_path(root, receipt_relative.as_posix(), f"{label} {task} receipt")
        report_pin, receipt_pin = _descriptor(report_path, report_relative), _descriptor(receipt_path, receipt_relative)
        expected_report_sha = _followup_expected_report_sha256(task, report_sha)
        require(report_pin["sha256"] == expected_report_sha and item.get("report") == report_pin and item.get("receipt") == receipt_pin, f"{label} accepted pins {task}")
        report, receipt = read_json(report_path, f"{label} {task} report"), read_json(receipt_path, f"{label} {task} receipt")
        _verify_followup_successor_binding(root, task, report, receipt, report_pin)
        verification, independent = receipt.get("verification"), receipt.get("independent_review")
        require(receipt.get("task") == task and receipt.get("non_authoritative") is True and receipt.get("source_migration") == "not_performed" and receipt.get("native_admission") == "not_performed" and isinstance(receipt.get("result"), str) and receipt["result"].startswith("PASS"), f"{label} accepted receipt {task}")
        require(isinstance(verification, dict) and verification.get("task") == task and verification.get("output") == report_pin and verification.get("rows") == row_count and verification.get("counts") == {"proposed": proposed_count, "unresolved": unresolved_count} and verification.get("input_manifest") == {"path": manifest_relative.as_posix(), "sha256": manifest_sha256}, f"{label} receipt verification {task}")
        require(isinstance(independent, dict) and independent.get("final_report_sha256") == expected_report_sha and isinstance(independent.get("result"), str) and independent["result"].startswith("PASS"), f"{label} receipt independent review {task}")
        require(item.get("independent_review_sha256") == expected_report_sha, f"{label} manifest independent-review hash {task}")
        require(report.get("schema_version") == 1 and report.get("task_id") == task and report.get("non_authoritative") is True and report.get("source_migration") == "not_performed" and report.get("native_admission") == "not_performed", f"{label} report boundary {task}")
        report_pins = report.get("input_pins")
        require(isinstance(report_pins, dict), f"{label} report input pins {task}")
        selection_pin = report_pins.get("selection_manifest")
        manifest_pin = report_pins.get("manifest")
        expected_selection_pin = {"path": manifest_relative.as_posix(), "sha256": manifest_sha256}
        require((selection_pin == expected_selection_pin and manifest_pin is None) or (selection_pin is None and manifest_pin == expected_selection_pin), f"{label} report selection pin {task}")
        if verify_supporting_evidence:
            require(
                report_pins.get("operator_decision_record") == {
                    "path": OPERATOR_DECISION_REL.as_posix(), "sha256": OPERATOR_DECISION_SHA256,
                },
                f"{label} report exact Operator decision pin {task}",
            )
        rows = report.get("rows")
        require(isinstance(rows, list) and len(rows) == row_count, f"{label} report rows {task}")
        mapped: dict[str, tuple[str, str | None, float]] = {}
        expected_ids = {row["occurrence_id"] for row in selected[task]}
        for number, row in enumerate(rows):
            require(isinstance(row, dict), f"{label} report {task} row {number}")
            occurrence_id = row.get("occurrence_id")
            require(isinstance(occurrence_id, str) and occurrence_id in expected_ids and occurrence_id not in mapped, f"{label} report selected occurrence {task} row {number}")
            expected = expected_by_id[occurrence_id]
            require({key: row.get(key) for key in expected} == expected and row.get("prior_decision") == "unresolved", f"{label} report current origin {occurrence_id}")
            decision, target, confidence = _normalized_layer_row(kind, row, f"{label} report {task} row {number}")
            require(row.get("executable") is False and isinstance(row.get("evidence"), list) and any(_span_matches(root, evidence, expected, f"{label} report {task} row {number}") for evidence in row["evidence"] if isinstance(evidence, dict)), f"{label} report current evidence {occurrence_id}")
            if verify_supporting_evidence:
                require(
                    all(
                        _later_followup_evidence_is_current(
                            root, evidence, current_source_pins, f"{label} report {task} row {number} supporting evidence"
                        )
                        for evidence in row["evidence"]
                    ),
                    f"{label} report all supporting evidence current {occurrence_id}",
                )
            if decision == "proposed":
                require(target is not None and FORBIDDEN_TARGET_RE.search(target) is None and "selector" not in target.lower(), f"{label} report target syntax {occurrence_id}")
            else:
                require(row.get("proposed_value") is None and 0 <= confidence < .9, f"{label} report explicit null {occurrence_id}")
            mapped[occurrence_id] = (decision, target, confidence)
        require(set(mapped) == expected_ids, f"{label} report exact occurrence coverage {task}")
        require(sum(decision == "proposed" for decision, _target, _confidence in mapped.values()) == proposed_count and sum(decision == "unresolved" for decision, _target, _confidence in mapped.values()) == unresolved_count, f"{label} report exact decisions {task}")
        output[task] = mapped
        reference: dict[str, Any] = {"report": report_pin, "receipt": receipt_pin, "independent_review_sha256": expected_report_sha}
        if verify_supporting_evidence:
            reference["proofs"] = {
                row["occurrence_id"]: {field: row.get(field) for field in LATER_FOLLOWUP_PROOF_FIELDS}
                for row in rows
            }
        references[task] = reference
    return output, references


def _read_actor_targets(root: Path, ledger: dict[str, Any]) -> dict[str, str]:
    pins = ledger.get("input_pins")
    accepted = pins.get("accepted_layers") if isinstance(pins, dict) else None
    _specs, actor_position, _grammar_position = _layer_layout(ledger)
    require(isinstance(accepted, list), "Actor accepted manifest")
    item = accepted[actor_position]
    require(isinstance(item, dict) and item.get("task") == "CA-P-2058" and item.get("priority") == "coverage_only" and item.get("kind") == "canonical_target_check" and item.get("rows") == 43, "Actor subset manifest")
    report_path = relative_path(root, ACTOR_SUBSET_REL.as_posix(), "Actor subset")
    report = read_json(report_path, "Actor subset")
    report_pin = _descriptor(report_path, ACTOR_SUBSET_REL)
    require(item.get("report") == report_pin and report.get("task_id") == "CA-P-2058", "Actor subset report pin")
    receipt_rel = STAGE2_REL / "task-2058.receipt.json"
    receipt_path = relative_path(root, receipt_rel.as_posix(), "Actor subset receipt")
    receipt = read_json(receipt_path, "Actor subset receipt")
    require(item.get("receipt") == _descriptor(receipt_path, receipt_rel), "Actor subset receipt pin")
    checks = receipt.get("checks")
    require(receipt.get("task") == "CA-P-2058" and isinstance(receipt.get("result"), str) and receipt["result"].startswith("PASS") and receipt.get("non_authoritative") is True and receipt.get("output") == report_pin and isinstance(checks, dict) and str(checks.get("independent_baseline_selection", "")).startswith("PASS"), "Actor subset accepted receipt")
    rows = report.get("rows")
    require(isinstance(rows, list) and len(rows) == 43, "Actor subset exact coverage")
    targets: dict[str, str] = {}
    for number, row in enumerate(rows):
        require(isinstance(row, dict) and isinstance(row.get("occurrence_id"), str) and isinstance(row.get("proposed_value"), str) and row.get("executable") is False, f"Actor subset row {number}")
        occurrence_id = row["occurrence_id"]
        require(occurrence_id not in targets, "Actor subset duplicate occurrence")
        targets[occurrence_id] = row["proposed_value"]
    require({target: list(targets.values()).count(target) for target in set(targets.values())} == {"Actor.Type: Operator": 33, "Actor.Type: AI Agent": 10}, "Actor subset canonical targets")
    return targets


def _layer_refs(ledger: dict[str, Any], followup_refs: dict[str, dict[str, Any]] | None = None) -> dict[str, dict[str, Any]]:
    """Return the manifest descriptors each admitted per-row layer must repeat."""

    pins = ledger.get("input_pins")
    accepted = pins.get("accepted_layers") if isinstance(pins, dict) else None
    specs, _actor_position, grammar_position = _layer_layout(ledger)
    require(isinstance(accepted, list), "layer provenance manifest coverage")
    references: dict[str, dict[str, Any]] = {}
    for task, _kind, position, _priority in specs:
        item = accepted[position]
        require(isinstance(item, dict) and item.get("task") == task, f"layer provenance manifest {task}")
        report, receipt = item.get("report"), item.get("receipt")
        require(isinstance(report, dict) and isinstance(receipt, dict), f"layer provenance descriptors {task}")
        references[task] = {"report": report, "receipt": receipt}
    if followup_refs is not None:
        for task, _kind, _position, _priority in specs:
            if task not in ALL_FOLLOWUP_TASKS:
                continue
            require(references.get(task) == {"report": followup_refs[task]["report"], "receipt": followup_refs[task]["receipt"]}, f"follow-up per-row manifest references {task}")
            references[task]["independent_review_sha256"] = followup_refs[task]["independent_review_sha256"]
            if task in LATER_FOLLOWUP_TASKS:
                proofs = followup_refs[task].get("proofs")
                require(isinstance(proofs, dict), f"later follow-up proof references {task}")
                references[task]["proofs"] = proofs
    if grammar_position is not None:
        item = accepted[grammar_position]
        require(isinstance(item, dict) and item.get("task") == "CA-P-2087", "accepted grammar provenance manifest")
        report, receipt = item.get("report"), item.get("receipt")
        require(isinstance(report, dict) and isinstance(receipt, dict), "accepted grammar provenance descriptors")
        references["CA-P-2087"] = {"report": report, "receipt": receipt}
    return references


def _read_layer_rows(
    root: Path,
    ledger: dict[str, Any],
    expected_occurrences: list[dict[str, Any]],
    baseline_rows: dict[str, dict[str, Any]],
) -> tuple[dict[str, dict[str, tuple[str, str | None, float]]], dict[str, dict[str, Any]]]:
    pins = ledger.get("input_pins")
    require(isinstance(pins, dict), "ledger input pins")
    accepted = pins.get("accepted_layers")
    specs, _actor_position, _grammar_position = _layer_layout(ledger)
    require(isinstance(accepted, list), "accepted layer manifest coverage")
    output: dict[str, dict[str, tuple[str, str | None, float]]] = {}
    followup_refs: dict[str, dict[str, Any]] = {}
    followup_rows: dict[str, dict[str, tuple[str, str | None, float]]] = {}
    admitted_tasks = {task for task, _kind, _position, _priority in specs}
    if FOLLOWUP_TASKS <= admitted_tasks:
        first_rows, first_refs = _read_followup_layer_rows(root, ledger, expected_occurrences, baseline_rows)
        followup_rows.update(first_rows)
        followup_refs.update(first_refs)
    if SECOND_FOLLOWUP_TASKS <= admitted_tasks:
        second_rows, second_refs = _read_followup_layer_rows(
            root,
            ledger,
            expected_occurrences,
            baseline_rows,
            SECOND_FOLLOWUP_LAYER_SPECS,
            SECOND_FOLLOWUP_MANIFEST_REL,
            SECOND_FOLLOWUP_MANIFEST_SHA256,
            len(LAYER_SPECS) + len(FOLLOWUP_LAYER_SPECS),
            "second follow-up",
            "50ab0114669787dba6331b58f8054cd8fb33b5abbed33df6fbf5b52df53923fa",
            True,
        )
        followup_rows.update(second_rows)
        followup_refs.update(second_refs)
    if THIRD_FOLLOWUP_TASKS <= admitted_tasks:
        third_rows, third_refs = _read_followup_layer_rows(
            root,
            ledger,
            expected_occurrences,
            baseline_rows,
            THIRD_FOLLOWUP_LAYER_SPECS,
            THIRD_FOLLOWUP_MANIFEST_REL,
            THIRD_FOLLOWUP_MANIFEST_SHA256,
            len(LAYER_SPECS) + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS),
            "third follow-up",
            "c52b26478acac8d5cfa9687b0925a1a9165a3647bd510e9877d69b06cbf214d4",
            True,
        )
        followup_rows.update(third_rows)
        followup_refs.update(third_refs)
    if FOURTH_FOLLOWUP_TASKS <= admitted_tasks:
        fourth_rows, fourth_refs = _read_followup_layer_rows(
            root,
            ledger,
            expected_occurrences,
            baseline_rows,
            FOURTH_FOLLOWUP_LAYER_SPECS,
            FOURTH_FOLLOWUP_MANIFEST_REL,
            FOURTH_FOLLOWUP_MANIFEST_SHA256,
            len(LAYER_SPECS) + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS) + len(THIRD_FOLLOWUP_LAYER_SPECS),
            "fourth follow-up",
            "4f2ec9d285283a76386dd176f6d4a6bf6a101db32219349462a91bc6c666ecf2",
            True,
        )
        followup_rows.update(fourth_rows)
        followup_refs.update(fourth_refs)
    if FIFTH_FOLLOWUP_TASKS <= admitted_tasks:
        fifth_rows, fifth_refs = _read_followup_layer_rows(
            root,
            ledger,
            expected_occurrences,
            baseline_rows,
            FIFTH_FOLLOWUP_LAYER_SPECS,
            FIFTH_FOLLOWUP_MANIFEST_REL,
            FIFTH_FOLLOWUP_MANIFEST_SHA256,
            len(LAYER_SPECS) + len(FOLLOWUP_LAYER_SPECS) + len(SECOND_FOLLOWUP_LAYER_SPECS) + len(THIRD_FOLLOWUP_LAYER_SPECS) + len(FOURTH_FOLLOWUP_LAYER_SPECS),
            "fifth follow-up",
            "19d55f08f9bd809d5a7cf7c937992b597e1a17d4b641e186ebc144b1e26c1186",
            True,
        )
        followup_rows.update(fifth_rows)
        followup_refs.update(fifth_refs)
    for task, kind, position, priority in specs:
        if task in ALL_FOLLOWUP_TASKS:
            output[task] = followup_rows[task]
            continue
        item = accepted[position]
        require(isinstance(item, dict) and item.get("task") == task and item.get("priority") == priority and item.get("kind") == kind, f"accepted layer manifest {task}")
        relative = _layer_path(task)
        report_path = relative_path(root, relative.as_posix(), f"layer {task} report")
        report = read_json(report_path, f"layer {task} report")
        report_pin = {"path": relative.as_posix(), "sha256": sha(report_path.read_bytes())}
        require(item.get("report") == report_pin, f"accepted layer report pin {task}")
        receipt_relative = STAGE2_REL / f"task-{task.removeprefix('CA-P-')}.receipt.json"
        receipt_path = relative_path(root, receipt_relative.as_posix(), f"layer {task} receipt")
        receipt_pin = _descriptor(receipt_path, receipt_relative)
        require(item.get("receipt") == receipt_pin, f"accepted layer receipt pin {task}")
        _verify_receipt(task, kind, read_json(receipt_path, f"layer {task} receipt"), report_pin)
        rows = report.get("occurrences") if kind == "substance" else report.get("rows")
        require(isinstance(rows, list) and item.get("rows") == len(rows), f"accepted layer row count {task}")
        mapped: dict[str, tuple[str, str | None, float]] = {}
        for row_number, row in enumerate(rows):
            require(isinstance(row, dict) and isinstance(row.get("occurrence_id"), str), f"layer {task} row {row_number}")
            occurrence_id = row["occurrence_id"]
            require(occurrence_id not in mapped, f"layer {task} duplicate ownership")
            mapped[occurrence_id] = _normalized_layer_row(kind, row, f"layer {task} row {row_number}")
        output[task] = mapped
    return output, followup_refs


def verify_working_ledger(root: Path = ROOT) -> dict[str, Any]:
    """Verify the persisted derived ledger without importing its producer."""

    expected = enumerate_current_frontier(root)
    ledger_path = relative_path(root, LEDGER_REL.as_posix(), "working ledger")
    frontier_path = relative_path(root, FRONTIER_REL.as_posix(), "current frontier")
    diagnostics_path = relative_path(root, DIAGNOSTICS_REL.as_posix(), "working diagnostics")
    ledger = read_json(ledger_path, "working ledger")
    frontier = read_json(frontier_path, "current frontier")
    diagnostics = read_json(diagnostics_path, "working diagnostics")
    _require_followup_extension_when_receipts_exist(root, ledger)
    _verify_frontier(root, frontier, expected)
    require(ledger.get("schema_version") == 1, "ledger schema version")
    require(ledger.get("non_authoritative") is True, "ledger non-authoritative")
    require(ledger.get("source_migration") == "not_performed", "ledger source migration")
    require(ledger.get("native_admission") == "not_performed", "ledger native admission")
    require(ledger.get("source_reviews") == [_source_view(source) for source in expected["selected_sources"]], "ledger exact current source pins")
    require(ledger.get("remaining_gaps", {}).get("diagnostics_path") == DIAGNOSTICS_REL.as_posix(), "ledger diagnostics reference")
    require(diagnostics.get("schema_version") == 1 and diagnostics.get("non_authoritative") is True, "diagnostics envelope")
    require(diagnostics.get("excluded_sources") == frontier.get("excluded_sources"), "diagnostics exclusions")
    require(diagnostics.get("counts", {}).get("quarantined_sources") == sum(source["quarantined"] for source in expected["selected_sources"]), "diagnostics quarantines")
    baseline_rows = _read_baseline_rows(root, ledger)
    grammar_effects = _grammar_effects(root, ledger)
    accepted_grammar_rows = _read_accepted_grammar_rows(root, ledger, expected["occurrences"], grammar_effects)
    specs, _actor_position, _grammar_position = _layer_layout(ledger)
    expected_priority = [task for task, _kind, _position, _priority in specs]
    expected_priority.append("CA-P-2058 coverage_only")
    expected_priority.append(GRAMMAR_ACCEPTED_PRIORITY if accepted_grammar_rows is not None else "CA-P-2087 recheck_gate")
    require(ledger.get("layer_priority") == expected_priority, "ledger accepted layer priority")
    layer_rows, followup_refs = _read_layer_rows(root, ledger, expected["occurrences"], baseline_rows)
    actor_targets = _read_actor_targets(root, ledger)
    layer_refs = _layer_refs(ledger, followup_refs if followup_refs else None)
    counts = _verify_rows(root, ledger.get("occurrences"), expected["occurrences"], baseline_rows, layer_rows, actor_targets, grammar_effects, accepted_grammar_rows, layer_refs)
    actual_counts = ledger.get("counts")
    require(isinstance(actual_counts, dict), "ledger counts")
    require(actual_counts.get("sources") == len(expected["selected_sources"]) and actual_counts.get("occurrences") == len(expected["occurrences"]), "ledger exact coverage counts")
    require(actual_counts.get("decisions") == dict(sorted(counts.items())) and actual_counts.get("unresolved") == counts["unresolved"], "ledger exact decision counts")
    require(actual_counts.get("quarantined_sources") == sum(source["quarantined"] for source in expected["selected_sources"]), "ledger quarantine count")
    return {"outcome": "PASS", "sources": len(expected["selected_sources"]), "occurrences": len(expected["occurrences"]), **counts, "quarantined_sources": actual_counts["quarantined_sources"], "excluded_sources": len(frontier["excluded_sources"])}


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify the one-off working Subject ledger.")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    print(json.dumps(verify_working_ledger(args.root.resolve()), sort_keys=True))


if __name__ == "__main__":
    main()
