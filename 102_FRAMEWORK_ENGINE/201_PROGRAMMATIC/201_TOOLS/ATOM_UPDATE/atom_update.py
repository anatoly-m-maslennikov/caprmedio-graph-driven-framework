#!/usr/bin/env python3
"""Root-bound Subject preparation and the existing Atom update CLI."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path
import sys
from typing import Annotated, Any, Literal

from pydantic import BaseModel, ConfigDict, Field, RootModel, ValidationError, field_validator
SCRIPT = Path(__file__).resolve()
TOOLS = SCRIPT.parents[1]
for parent in SCRIPT.parents:
    if parent.name in {".caprmedio_install", ".caprmedio_runtime"}:
        sys.pycache_prefix = str(parent.parent / ".caprmedio_tmp/cache/python")
        break
sys.path.insert(0, str(TOOLS))

import atom_operations as operations
import atom_subject_patch as subjects
import atom_subject_stage as staging
from project_selection import ProjectSelectionError, active_selection, bind_selection
from tool_description import binding_matches, make_tool_description
from VALIDATE_ATOMS.validate_atoms_workers.read_io import LimitReached, ReadContext
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS

TOOL_NAME = "ATOM_UPDATE"
MCP_NAME = "atom_update"
ACTION_ID = "CA-O-030"
DELIVERY_ID = "CA-D-425"
ENTRYPOINT = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_UPDATE/atom_update.py"
SOURCE_PINS = tuple([
    {
        "atom_id": "CA-R-866",
        "version": 26,
        "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/306_FEATURE_TOOL_WORKFLOWS/04_requirement/CA-R-866-TOOL_WORKFLOWS-STANDARD-REQUIREMENT--update-caprmedio-markdown-atoms.md",
        "sha256": "ef34d271cdf1fac68cec3ee5df48937396f3485cadf107ca46b9b1c32e883146"
    },
    {
        "atom_id": "CA-R-1093",
        "version": 12,
        "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/306_FEATURE_TOOL_WORKFLOWS/04_requirement/CA-R-1093-TOOL_WORKFLOWS-CORE-REQUIREMENT--separate-generic-and-atom-specific-tool-authority.md",
        "sha256": "089aef0c7af39cd3135b411b5629ee32e350f35beae53a5dbd85754cb50f53e4"
    },
    {
        "atom_id": "CA-O-030",
        "version": 19,
        "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/306_FEATURE_TOOL_WORKFLOWS/09_operations/CA-O-030-TOOL_WORKFLOWS-STANDARD-ACTION--update-sealed-caprmedio-atom-carriers.md",
        "sha256": "14b8423f542af6d12a2f40a7ca4cdf3a343c7ea14ebc6bdecc16c01a69a28453"
    },
    {
        "atom_id": "CA-M-371",
        "version": 12,
        "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/306_FEATURE_TOOL_WORKFLOWS/05_method/CA-M-371-TOOL_WORKFLOWS-STANDARD-METHOD--preview-exact-subject-patches.md",
        "sha256": "f0f4a2aa25de2d6b04061a65b7606101410cd9f56ccfe81567f323c6dc99b04d"
    },
    {
        "atom_id": "CA-D-425",
        "version": 16,
        "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/306_FEATURE_TOOL_WORKFLOWS/07_delivery/CA-D-425-TOOL_WORKFLOWS-STANDARD-DELIVERY--deliver-atom-update-tool.md",
        "sha256": "208431f44e901ed023f45c80536a92ab63e7c046ff45f56dede0f091c8bc7023"
    },
    {
        "atom_id": "CA-E-304",
        "version": 25,
        "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/306_FEATURE_TOOL_WORKFLOWS/06_evaluation/CA-E-304-TOOL_WORKFLOWS-STANDARD-QA_CASE--verify-update-sealed-caprmedio-atom-carriers.md",
        "sha256": "79f5eb5b9e73fe1907a8b923c1ea9443a11def5f1d21eaea0e0393644bd0b2c3"
    }
])

AtomID = Annotated[str, Field(pattern=r"^CA-[CAPRMEDO]-[0-9]+$")]
Digest = Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]
Version = Annotated[int, Field(ge=1)]
Text = Annotated[str, Field(min_length=1)]
Timestamp = Annotated[str, Field(pattern=r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [+-]\d{4}$")]
Profile = Literal["legacy", "approved"]
Operation = Literal["preview_subjects", "stage_subjects"]


class _Closed(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


class ReplacementPatch(_Closed):
    field: Literal["governs", "depends_on"]
    old: Text
    new: Text


class DependencySetPatch(_Closed):
    field: Literal["depends_on"]
    operation: Literal["replace_set"]
    old: list[Text]
    new: list[Text]


Patch = ReplacementPatch | DependencySetPatch


class LogicalAtomPatch(_Closed):
    atom_id: AtomID
    version: Version
    sha256: Digest
    subject_patches: list[Patch]


class _Preparation(_Closed):
    subject_profile: Profile
    atoms: list[LogicalAtomPatch] = Field(min_length=1)

    @field_validator("atoms")
    @classmethod
    def unique_atoms(cls, atoms):
        if len({atom.atom_id for atom in atoms}) != len(atoms):
            raise ValueError("atoms must contain unique logical Atom IDs")
        return atoms


class PreviewSubjectsRequest(_Preparation):
    operation: Literal["preview_subjects"]


class StageSubjectsRequest(_Preparation):
    operation: Literal["stage_subjects"]
    preview_sha256: Digest
    illustrative_updated_at: Timestamp | None


class SubjectPreparationRequest(RootModel[Annotated[PreviewSubjectsRequest | StageSubjectsRequest, Field(discriminator="operation")]]):
    pass


class Span(_Closed):
    start: int = Field(ge=0)
    end: int = Field(ge=0)


class ReplacementRecord(ReplacementPatch):
    index: int | None
    changed: bool
    span: Span


class DependencySetRecord(DependencySetPatch):
    changed: bool
    span: Span


class VersionPatch(_Closed):
    field: Literal["version"]
    old: Version
    new: Version


class TimePatch(_Closed):
    field: Literal["updated_at"]
    old: Timestamp
    new: Timestamp


class GrammarPin(_Closed):
    atom_id: AtomID
    version: Version
    path: Text
    sha256: Digest


class ProfileEvidence(_Closed):
    grammar_pins: list[GrammarPin] = Field(min_length=5, max_length=5)
    native_admission: Literal["not_performed"]


class TargetDescriptor(_Closed):
    atom_id: AtomID
    path: Text
    filename: Text
    version: Version
    digest: Digest
    lifecycle: Text
    status: Text
    updated_at: Timestamp
    content_role: Text
    type: str | None


class Proposal(_Closed):
    frontmatter_digest: Digest
    content_digest: Digest
    sha256: Digest


class ExecutionMetadata(_Closed):
    version: Version
    updated_at: Literal["actual_effect_time", "preserve"]


class PredecessorArchive(_Closed):
    atom_id: AtomID
    version: Version
    path: Text
    sha256: Digest
    lifecycle: Literal["archived"]


class SubjectIntent(_Closed):
    schema_version: Literal[1]
    target: TargetDescriptor
    subject_profile: Profile
    subject_profile_evidence: ProfileEvidence
    subject_patches: list[Patch]
    proposal: Proposal
    execution_metadata: ExecutionMetadata
    predecessorArchive: PredecessorArchive | None
    noop: bool


class BytePreservation(_Closed):
    preserved: Literal[True]
    permitted_fields: list[Literal["subjects", "version", "updated_at"]]


class PreviewAtom(_Closed):
    selector: Text
    relative_path: Text
    atom_id: AtomID
    before_sha256: Digest
    after_sha256: Digest
    before_version: Version
    after_version: Version
    proposed_version: Version
    patches: list[ReplacementRecord | DependencySetRecord]
    revision_metadata_patches: list[VersionPatch | TimePatch]
    proposed_carrier: str
    noop: bool
    illustrative_updated_at: Timestamp | None
    byte_preservation: BytePreservation
    subject_intent: SubjectIntent
    subject_intent_sha256: Digest


class SubjectPreview(_Closed):
    count: int = Field(ge=1)
    atoms: list[PreviewAtom]
    noop: bool
    illustrative_updated_at: Timestamp | None
    subject_profile: Profile
    subject_profile_evidence: ProfileEvidence
    preview_sha256: Digest


class ScratchStage(_Closed):
    staging_only: Literal[True]
    illustrative: Literal[True]
    sources_unchanged: Literal[True]
    stage_root: Text
    manifest_path: Text
    manifest_sha256: Digest


class ArtifactReference(_Closed):
    path: Text


class HashedArtifactReference(ArtifactReference):
    sha256: Digest


class UnverifiedArtifact(_Closed):
    path: Text
    state: Literal["unverified"]


class PreparationError(_Closed):
    code: Text
    message: str
    stage_root: str | None
    retained_artifacts: list[HashedArtifactReference | ArtifactReference]
    unverified_artifacts: list[UnverifiedArtifact]


class SubjectPreparationResult(_Closed):
    operation: Operation
    preview: SubjectPreview | None
    staging: ScratchStage | None
    errors: list[PreparationError]


def _contract_reader(root):
    reader = ReadContext(roots=[str(root)], limits=dict(CEILINGS))
    for pin in SOURCE_PINS:
        raw = reader.read(root / pin["path"])
        metadata = operations.parse_carrier(raw, root / pin["path"]).metadata
        if (hashlib.sha256(raw).hexdigest() != pin["sha256"]
                or metadata.get("atom_id") != pin["atom_id"] or metadata.get("version") != pin["version"]):
            raise operations.ToolError("subject-preparation-contract-stale", "Preparation definition differs from its accepted source pin")
    return reader


def _resolve_items(root, request, reader):
    control = operations.control_root(root)
    layout = subjects._capture_identity_layout(operations, root)
    ids = {item.atom_id for item in request.atoms}
    pool = []
    for path in reader.inventory(control):
        role = operations._role_directory(path, control)
        if (role is None or "_projection" in path.relative_to(control).parts
                or operations._lifecycle(path, control) in {"draft", "archived"}
                or (layout is not None and path.is_relative_to(layout[0]))):
            continue
        identity = operations.ATOM_ID.search(path.name)
        if identity is None or identity.group(1) not in ids:
            continue
        raw = reader.read(path)
        parsed = operations.parse_carrier(raw, path)
        if "projection" in parsed.metadata:
            continue
        if parsed.metadata.get("atom_id") != identity.group(1):
            raise operations.ToolError("atom-frontmatter-id-mismatch", "Selected filename and declared Atom identity disagree")
        frontmatter, content = subjects._raw_frontmatter(operations, raw.decode("utf-8"))
        pool.append(operations.Atom(path, path.relative_to(root).as_posix(), path.name, identity.group(1),
                                   operations._lifecycle(path, control), role, frontmatter, content))
    items = []
    for item in request.atoms:
        atom = operations.resolve_selector(root, item.atom_id, pool)
        items.append({"selector": atom.relative, "expected": {"atom_id": item.atom_id, "version": item.version, "sha256": item.sha256},
                      "subject_patches": [patch.model_dump(mode="json") for patch in item.subject_patches]})
    subjects._assert_identity_layout_current(operations, root, layout)
    return items


def _stage_failure_evidence(root, result):
    stage_root = Path(result["stage_root"])
    paths = [stage_root, Path(result["manifest_path"])]
    for ordinal, atom in enumerate(result["preview"]["atoms"], 1):
        directory = stage_root / f"{ordinal:04d}"
        paths.extend((directory, directory / Path(atom["selector"]).name))
    identities, unverified = {}, []
    for relative in paths:
        try:
            parent = operations._raw_revision_parent(root, root / relative)
            try:
                observed = os.stat(relative.name, dir_fd=parent, follow_symlinks=False)
            finally:
                os.close(parent)
            identities[root / relative] = (observed.st_dev, observed.st_ino)
        except (operations.ToolError, OSError):
            unverified.append({"path": relative.as_posix(), "state": "unverified"})
    return {"stage_root": stage_root.as_posix(), "retained_artifacts": staging._retained_artifacts(root, identities),
            "unverified_artifacts": unverified}


def _failure(operation, error, details):
    return SubjectPreparationResult(operation=operation, preview=None, staging=None, errors=[PreparationError(
        code=getattr(error, "code", "subject-preparation-unavailable"), message=getattr(error, "message", "Subject preparation could not verify its source boundary"),
        stage_root=details.get("stage_root"), retained_artifacts=details.get("retained_artifacts", []),
        unverified_artifacts=details.get("unverified_artifacts", []))])


class _DescriptorAdapter:
    def __init__(self, root: str | Path):
        self._root = Path(root).absolute()
        if not self._root.is_dir() or self._root.resolve() != self._root:
            raise ValueError("Preparation requires one canonical server-bound Project root")

    def invoke(self, request: SubjectPreparationRequest | dict[str, Any]) -> SubjectPreparationResult:
        try:
            parsed = request.root if isinstance(request, SubjectPreparationRequest) else SubjectPreparationRequest.model_validate(request).root
        except ValidationError as error:
            raise operations.ToolError("subject-preparation-request-invalid", "Request does not match the closed preparation schema") from error
        stage_result = None
        try:
            reader = _contract_reader(self._root)
            selection = active_selection(self._root)
            for path in (selection.settings_path, selection.structure_path):
                raw = reader.read(path)
                pin = selection.provenance.get(path.relative_to(self._root).as_posix(), {})
                if hashlib.sha256(raw).hexdigest() != pin.get("sha256"):
                    raise operations.ToolError("subject-project-selection-stale", "Project carriers differ from retained provenance")
            selection._revalidate_boundary(reader=reader)
            with bind_selection(selection):
                items = _resolve_items(self._root, parsed, reader)
                if parsed.operation == "preview_subjects":
                    preview = subjects.preview_subject_patches(self._root, items, subject_profile=parsed.subject_profile)
                else:
                    stage_result = staging.stage_subject_preview(self._root, items, subject_profile=parsed.subject_profile,
                        timestamp=parsed.illustrative_updated_at, expected_preview_sha256=parsed.preview_sha256)
                    preview = stage_result["preview"]
            selection._revalidate_boundary(reader=reader)
            if reader.currentness()["state"] != "unchanged":
                raise operations.ToolError("subject-source-changed", "Preparation source frontier changed")
            return SubjectPreparationResult(operation=parsed.operation, preview=preview,
                staging=None if stage_result is None else {key: value for key, value in stage_result.items() if key != "preview"}, errors=[])
        except (operations.ToolError, ProjectSelectionError, OSError, LimitReached, ValueError) as error:
            details = dict(getattr(error, "details", None) or {})
            if stage_result is not None:
                details.update(_stage_failure_evidence(self._root, stage_result))
            return _failure(parsed.operation, error, details)


def create_adapter(root: str | Path):
    return _DescriptorAdapter(root)


def describe_tool():
    return make_tool_description(entrypoint=ENTRYPOINT, name=TOOL_NAME, delivery_atom_id=DELIVERY_ID,
        action_ids=[ACTION_ID], input_symbol="SubjectPreparationRequest", output_symbol="SubjectPreparationResult",
        title="Prepare Atom Subjects", description="Preview exact Subject changes or explicitly export derived scratch candidates.",
        purpose="Prepare reviewed Subject evidence without invoking Atom publication or creating a Session, Run or Journal.",
        read_only=False, destructive=False, idempotent=False, open_world=False)


def binding_is_admitted(binding: Any):
    return (binding_matches(binding, entrypoint=ENTRYPOINT, name=TOOL_NAME, delivery_atom_id=DELIVERY_ID, action_ids=[ACTION_ID])
            and binding.get("mcp_name") == MCP_NAME and not binding.get("workflow_ids"))


if __name__ == "__main__":
    raise SystemExit(operations.cli("ATOM_UPDATE"))
