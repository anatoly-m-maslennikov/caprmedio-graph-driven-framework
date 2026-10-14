#!/usr/bin/env python3
"""Read-only, root-bound direct Subject lookup and the existing Atom search CLI."""
from __future__ import annotations

import hashlib
from pathlib import Path
from types import SimpleNamespace
import sys
from typing import Annotated, Any, Literal

from pydantic import BaseModel, ConfigDict, Field, JsonValue, ValidationError, field_validator

SCRIPT = Path(__file__).resolve()
TOOLS = SCRIPT.parents[1]
for parent in SCRIPT.parents:
    if parent.name in {".caprmedio_install", ".caprmedio_runtime"}:
        sys.pycache_prefix = str(parent.parent / ".caprmedio_tmp/cache/python")
        break
sys.path.insert(0, str(TOOLS))

from atom_operations import ToolError, cli
from atom_subject_lookup import run_subject_search
from project_selection import ProjectSelectionError, active_selection, bind_selection
from tool_description import binding_matches, make_tool_description
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier
from VALIDATE_ATOMS.validate_atoms_workers.read_io import LimitReached, ReadContext
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS

TOOL_NAME = "ATOM_SEARCH"
MCP_NAME = "atom_search"
ACTION_ID = "CA-O-046"
DELIVERY_ID = "CA-D-424"
ENTRYPOINT = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/atom_search.py"
SOURCE_PINS = tuple([
    {
        "atom_id": "CA-R-1936",
        "version": 2,
        "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/305_FEATURE_CONNECTOR_TOOLS/04_requirement/CA-R-1936-CONNECTOR_TOOLS-CORE-REQUIREMENT--use-one-coherent-connector-interface.md",
        "sha256": "dbb7471c477adf1474db73624e066d3fff202a61d975729d8d4ea4cbf95b040a"
    },
    {
        "atom_id": "CA-R-863",
        "version": 20,
        "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/305_FEATURE_CONNECTOR_TOOLS/04_requirement/CA-R-863-CONNECTOR_TOOLS-STANDARD-REQUIREMENT--search-caprmedio-markdown-atoms.md",
        "sha256": "83955ee92f170f9a97d9edc4e01c933f34fd9485f3d177f91e7ac2b77c7e39f6"
    },
    {
        "atom_id": "CA-O-046",
        "version": 9,
        "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/305_FEATURE_CONNECTOR_TOOLS/09_operations/CA-O-046-CONNECTOR_TOOLS-STANDARD-ACTION--search-caprmedio-atom-carriers.md",
        "sha256": "6b0b3fdc81d0089861e7cea5e4a2eaa7570ac712293a573104c602853311340b"
    },
    {
        "atom_id": "CA-M-370",
        "version": 6,
        "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/305_FEATURE_CONNECTOR_TOOLS/05_method/CA-M-370-CONNECTOR_TOOLS-STANDARD-METHOD--match-direct-subject-fields.md",
        "sha256": "253899527362c6bf17fad6bbe5b33f7cd2b0fa909c8a66669002cf17b4c1e08d"
    },
    {
        "atom_id": "CA-M-376",
        "version": 2,
        "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/305_FEATURE_CONNECTOR_TOOLS/05_method/CA-M-376-CONNECTOR_TOOLS-CORE-METHOD--execute-one-explicit-connector-operation.md",
        "sha256": "5ccecc40357c7819b2dbed8855748a1ef1ac06f05bfd1581792806206ea6810a"
    },
    {
        "atom_id": "CA-E-301",
        "version": 19,
        "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/305_FEATURE_CONNECTOR_TOOLS/06_evaluation/CA-E-301-CONNECTOR_TOOLS-STANDARD-QA_CASE--verify-search-caprmedio-atom-carriers.md",
        "sha256": "3f2f31abd50ff2d1330b73d11d7c424a76d55f9988854e939e1146b1908d943e"
    },
    {
        "atom_id": "CA-D-625",
        "version": 3,
        "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/305_FEATURE_CONNECTOR_TOOLS/07_delivery/CA-D-625-CONNECTOR_TOOLS-CORE-DELIVERY--deliver-coherent-connector-interface.md",
        "sha256": "708d39bbb841ece46a30d330c3768fbede6373ae00d30aacb5cdde3c18c24fcc"
    },
    {
        "atom_id": "CA-D-424",
        "version": 14,
        "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/305_FEATURE_CONNECTOR_TOOLS/07_delivery/CA-D-424-CONNECTOR_TOOLS-STANDARD-DELIVERY--deliver-atom-search-tool.md",
        "sha256": "1c956aecac1b3cfb55b90cf32aa03ea44ca029289e0e1ab49ecf6d946237564a"
    }
])

AtomID = Annotated[str, Field(pattern=r"^CA-[CAPRMEDO]-[0-9]+$")]
Digest = Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]
Role = Literal["Concern", "Analysis", "Plan", "Requirement", "Method", "Evaluation", "Delivery", "Operations"]
Lifecycle = Literal["active", "draft", "archived", "done", "resolved", "canceled", "all"]
Profile = Literal["legacy", "approved"]


class _Closed(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


class LookupSourceView(_Closed):
    scope_unit: str = Field(min_length=1)
    content_roles: list[Role] = Field(min_length=1)
    lifecycle: Lifecycle

    @field_validator("content_roles")
    @classmethod
    def unique_roles(cls, values):
        if len(values) != len(set(values)):
            raise ValueError("content_roles must be unique")
        return values


class SubjectLookupRequest(LookupSourceView):
    subject: str = Field(min_length=1)
    subject_field: Literal["governs", "depends_on", "both"]
    subject_match: Literal["exact", "prefix", "suffix", "contains"]
    subject_profile: Profile
    atom_ids: list[AtomID] = Field(default_factory=list)

    @field_validator("atom_ids")
    @classmethod
    def unique_ids(cls, values):
        if len(values) != len(set(values)):
            raise ValueError("atom_ids must be unique")
        return values


class LookupMatch(_Closed):
    atom_id: AtomID
    version: int = Field(ge=1)
    status: str = Field(min_length=1)
    current_scope_unit: str = Field(min_length=1)
    updated_at: str = Field(min_length=1)
    field: Literal["governs", "depends_on"]
    value: str = Field(min_length=1)


class GrammarEvidence(_Closed):
    atom_id: AtomID
    version: int = Field(ge=1)
    sha256: Digest


class ProfileEvidence(_Closed):
    grammar_pins: list[GrammarEvidence] = Field(min_length=5, max_length=5)
    native_admission: Literal["not_performed"]


class LookupData(_Closed):
    matches: list[LookupMatch]
    complete: Literal[True]
    subject_profile: Profile
    subject_profile_evidence: ProfileEvidence


class LookupCurrentState(_Closed):
    identity: AtomID
    version: int = Field(ge=1)
    source_token: Digest
    source_view: LookupSourceView


class LookupError(_Closed):
    code: Literal["input_invalid", "unsupported_operation", "target_not_found", "target_ambiguous",
                  "stale_state", "permission_denied", "schema_invalid", "backend_failure", "effect_uncertain"]
    message: str
    field: str | None


class SubjectLookupResult(_Closed):
    data: LookupData | None
    current_state: list[LookupCurrentState] | None
    effects: list[JsonValue] = Field(max_length=0)
    errors: list[LookupError]


def _refusal(code: str, message: str, field: str | None = None) -> SubjectLookupResult:
    return SubjectLookupResult(data=None, current_state=None, effects=[],
                               errors=[LookupError(code=code, message=message, field=field)])


def _contract_reader(root: Path) -> ReadContext:
    reader = ReadContext(roots=[str(root)], limits=dict(CEILINGS))
    for pin in SOURCE_PINS:
        raw = reader.read(root / pin["path"])
        if hashlib.sha256(raw).hexdigest() != pin["sha256"]:
            raise ToolError("subject-contract-stale", "Direct lookup contract differs from its accepted source pin")
        metadata = parse_carrier(raw, root / pin["path"]).metadata
        if metadata.get("atom_id") != pin["atom_id"] or metadata.get("version") != pin["version"]:
            raise ToolError("subject-contract-stale", "Direct lookup contract identity or Version differs")
    return reader


def _error_code(code: str) -> str:
    if code in {"subject-identity-duplicate", "subject-identity-inventory-unavailable", "duplicate-original-id"}:
        return "target_ambiguous"
    if "stale" in code or "changed" in code:
        return "stale_state"
    if code in {"subject-source-verification-unavailable", "subject-source-unavailable"}:
        return "backend_failure"
    return "input_invalid"


class _DescriptorAdapter:
    def __init__(self, root: str | Path):
        self._root = Path(root).absolute()
        if not self._root.is_dir() or self._root.resolve() != self._root:
            raise ValueError("Direct lookup requires one canonical server-bound Project root")

    def invoke(self, request: SubjectLookupRequest | dict[str, Any]) -> SubjectLookupResult:
        try:
            parsed = request if isinstance(request, SubjectLookupRequest) else SubjectLookupRequest.model_validate(request)
        except ValidationError:
            return _refusal("input_invalid", "Request does not match the closed direct Subject lookup schema")
        try:
            contracts = _contract_reader(self._root)
            selection = active_selection(self._root)
            for path in (selection.settings_path, selection.structure_path):
                raw = contracts.read(path)
                pin = selection.provenance.get(path.relative_to(self._root).as_posix(), {})
                if hashlib.sha256(raw).hexdigest() != pin.get("sha256"):
                    raise ToolError("subject-project-selection-stale", "Selected Project carriers differ from their retained provenance")
            selection._revalidate_boundary(reader=contracts)
            args = SimpleNamespace(subject=parsed.subject, subject_field=parsed.subject_field,
                                   subject_match=parsed.subject_match, subject_profile=parsed.subject_profile,
                                   scope_unit=parsed.scope_unit, content_role=parsed.content_roles,
                                   lifecycle=parsed.lifecycle, atom=parsed.atom_ids, under=None, query=[], limit=None)
            with bind_selection(selection):
                result = run_subject_search(self._root, args, direct_subject_only=True)
            selection._revalidate_boundary(reader=contracts)
            if contracts.currentness()["state"] != "unchanged":
                return _refusal("stale_state", "Direct lookup contract sources changed during lookup")
            diagnostics = result["diagnostics"]
            if diagnostics:
                errors = [LookupError(code="target_ambiguous" if diagnostic["code"] == "duplicate-original-id" else "schema_invalid",
                                      message="A selected Subject source failed lookup validation", field=None)
                          for diagnostic in diagnostics]
                return SubjectLookupResult(data=None, current_state=None, effects=[], errors=errors)
            if result["coverage"] != "full":
                return _refusal("backend_failure", "Complete Subject lookup coverage could not be verified")
            occurrences = sorted(result["occurrences"],
                                 key=lambda row: (row["atom_id"], row["version"], row["field"], row["value"]))
            matches = [{key: row[key] for key in LookupMatch.model_fields} for row in occurrences]
            view = LookupSourceView(scope_unit=parsed.scope_unit, content_roles=parsed.content_roles,
                                    lifecycle=parsed.lifecycle)
            states = {(row["atom_id"], row["version"], row["sha256"]): LookupCurrentState(
                identity=row["atom_id"], version=row["version"], source_token=row["sha256"], source_view=view)
                      for row in occurrences}
            evidence = result["subject_profile_evidence"]
            public_evidence = {"grammar_pins": [{key: pin[key] for key in GrammarEvidence.model_fields}
                                                for pin in evidence["grammar_pins"]],
                               "native_admission": evidence["native_admission"]}
            return SubjectLookupResult(data=LookupData(matches=matches, complete=True,
                subject_profile=result["subject_profile"], subject_profile_evidence=public_evidence),
                current_state=[states[key] for key in sorted(states)], effects=[], errors=[])
        except ToolError as error:
            return _refusal(_error_code(error.code), "Direct Subject lookup refused the selected request or source frontier")
        except ProjectSelectionError:
            return _refusal("stale_state", "Direct Subject lookup could not verify the selected Project declaration boundary")
        except (OSError, LimitReached):
            return _refusal("backend_failure", "Direct Subject lookup could not verify its bounded source frontier")
        except (ValueError, KeyError, TypeError):
            return _refusal("schema_invalid", "Direct Subject lookup evidence does not match its closed result schema")


def create_adapter(root: str | Path) -> _DescriptorAdapter:
    return _DescriptorAdapter(root)


def describe_tool() -> dict[str, Any]:
    return make_tool_description(entrypoint=ENTRYPOINT, name=TOOL_NAME,
        delivery_atom_id=DELIVERY_ID, action_ids=[ACTION_ID],
        input_symbol="SubjectLookupRequest", output_symbol="SubjectLookupResult",
        title="Look up Atom Subjects",
        description="Read direct Atom Subject fields without creating a Session, Run, Journal or staging artifact.",
        purpose="Return source-verified logical Subject matches for explicit owning Scope, roles and lifecycle.",
        read_only=True, idempotent=True)


def binding_is_admitted(binding: Any) -> bool:
    return (binding_matches(binding, entrypoint=ENTRYPOINT, name=TOOL_NAME,
                            delivery_atom_id=DELIVERY_ID, action_ids=[ACTION_ID])
            and binding.get("mcp_name") == MCP_NAME)


if __name__ == "__main__":
    raise SystemExit(cli("ATOM_SEARCH"))
