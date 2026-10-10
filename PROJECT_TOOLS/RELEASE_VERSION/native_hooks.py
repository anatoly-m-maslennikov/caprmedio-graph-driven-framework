"""Project-owned local-release bindings for one already-admitted O164 Session.

The release Action owns the phase order and the selected Session owns durable
Run evidence.  These bindings only reopen the sealed private frontier before
the product and installed-tree transitions; they neither admit a candidate nor
create a second Run, Journal, or callback surface.
"""

from __future__ import annotations

import hashlib
import json
import os
import stat
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from types import ModuleType
from typing import Any, Mapping


_PROJECT_ROOT = Path(globals().get("__caprmedio_project_root__", Path(__file__).resolve().parents[2]))
_ENGINE_RELEASE = _PROJECT_ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION"
_ENGINE_TOOLS = _ENGINE_RELEASE.parent
for _path in (_ENGINE_RELEASE, _ENGINE_TOOLS):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from release_contract import ReleaseContractError, SHA256, ValidatedCandidate  # noqa: E402
from release_handoff import SealedMethodologyExport, revalidate_sealed_methodology_export  # noqa: E402
from release_promotion import retained_native_promotion_packet  # noqa: E402
from retained_full_gate_packet import RetainedNativeFullGatePacket  # noqa: E402
from methodology_layout import MethodologyLayout, resolve_methodology_layout  # noqa: E402


_SOURCE_TOP_LEVEL = frozenset({"001_CORE_META_MODEL", "002_INSTALLED_EXTENSIONS", "003_PROJECT_CONFIGURATION"})


_BOUND_LOCAL_RELEASE_CORE: ModuleType | None = None


def bind_local_release_core(module: ModuleType) -> None:
    """Accept the sibling module that the selected Run already byte-bound."""

    global _BOUND_LOCAL_RELEASE_CORE
    if not isinstance(module, ModuleType):
        raise ReleaseContractError("local-release-helper-unavailable", "frozen local-release core is not a module")
    if _BOUND_LOCAL_RELEASE_CORE is not None and _BOUND_LOCAL_RELEASE_CORE is not module:
        raise ReleaseContractError("local-release-helper-unavailable", "local-release hook cannot replace its frozen sibling")
    _BOUND_LOCAL_RELEASE_CORE = module


def _local_release_module() -> ModuleType:
    """Return only the sibling module injected by the frozen Release Run."""

    if _BOUND_LOCAL_RELEASE_CORE is None:
        raise ReleaseContractError("local-release-helper-unbound", "local-release core was not frozen with this selected Run")
    return _BOUND_LOCAL_RELEASE_CORE


def _safe_relative(value: object, *, label: str) -> PurePosixPath:
    if not isinstance(value, str) or not value:
        raise ReleaseContractError("local-release-export-invalid", f"sealed export {label} is absent")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise ReleaseContractError("local-release-export-invalid", f"sealed export {label} is unsafe")
    return path


@dataclass(frozen=True)
class _ExportedAtom:
    relative: PurePosixPath
    digest: str
    atom_id: str
    version: int


def _export_atoms(export: SealedMethodologyExport) -> tuple[_ExportedAtom, ...]:
    """Open only the exact atom rows from the exporter-sealed inventory."""

    root = Path(export.candidate.project_root)
    inventory = root / export.source_export_root / "inventory.json"
    try:
        import json

        if inventory.is_symlink() or not inventory.is_file():
            raise ValueError("inventory unavailable")
        payload = json.loads(inventory.read_text(encoding="utf-8"))
        rows = payload["atoms"]
    except (KeyError, OSError, UnicodeDecodeError, ValueError, TypeError) as error:
        raise ReleaseContractError("local-release-export-invalid", "sealed Methodology inventory is unavailable") from error
    if not isinstance(rows, list) or not rows:
        raise ReleaseContractError("local-release-export-invalid", "sealed Methodology inventory has no atom rows")
    result: list[_ExportedAtom] = []
    seen: set[PurePosixPath] = set()
    for row in rows:
        if not isinstance(row, Mapping) or set(row) != {
            "atom_id", "destination_path", "digest", "sha256", "source_path", "version",
        }:
            raise ReleaseContractError("local-release-export-invalid", "sealed Methodology atom row is malformed")
        path = _safe_relative(row.get("source_path"), label="atom path")
        digest = row.get("sha256")
        atom_id = row.get("atom_id")
        version = row.get("version")
        if (row.get("destination_path") != path.as_posix() or row.get("digest") != digest
                or not isinstance(digest, str) or SHA256.fullmatch(digest) is None
                or not isinstance(atom_id, str) or not atom_id or type(version) is not int or version < 1
                or path.parts[0] not in _SOURCE_TOP_LEVEL or path in seen):
            raise ReleaseContractError("local-release-export-invalid", "sealed Methodology atom row is inconsistent")
        source = root / export.source_export_root / path
        try:
            mode = source.lstat().st_mode
            data = source.read_bytes()
        except OSError as error:
            raise ReleaseContractError("local-release-export-invalid", "sealed Methodology atom is unavailable") from error
        if stat.S_ISLNK(mode) or not stat.S_ISREG(mode) or hashlib.sha256(data).hexdigest() != digest:
            raise ReleaseContractError("local-release-export-invalid", "sealed Methodology atom differs from its inventory")
        seen.add(path)
        result.append(_ExportedAtom(path, digest, atom_id, version))
    return tuple(result)


def _export_supports(export: SealedMethodologyExport, atoms: tuple[_ExportedAtom, ...]) -> tuple[tuple[PurePosixPath, str], ...]:
    root = Path(export.candidate.project_root)
    inventory = root / export.source_export_root / "inventory.json"
    try:
        import json

        payload = json.loads(inventory.read_text(encoding="utf-8"))
        rows = payload["support"]
    except (KeyError, OSError, UnicodeDecodeError, ValueError, TypeError) as error:
        raise ReleaseContractError("local-release-export-invalid", "sealed Methodology support inventory is unavailable") from error
    if not isinstance(rows, list):
        raise ReleaseContractError("local-release-export-invalid", "sealed Methodology support inventory is malformed")
    known = {atom.relative for atom in atoms}
    result: list[tuple[PurePosixPath, str]] = []
    for row in rows:
        if not isinstance(row, Mapping) or set(row) != {"path", "sha256"}:
            raise ReleaseContractError("local-release-export-invalid", "sealed Methodology support row is malformed")
        path = _safe_relative(row.get("path"), label="support path")
        digest = row.get("sha256")
        if (path.parts[0] not in _SOURCE_TOP_LEVEL or path in known
                or not isinstance(digest, str) or SHA256.fullmatch(digest) is None):
            raise ReleaseContractError("local-release-export-invalid", "sealed Methodology support row is inconsistent")
        source = root / export.source_export_root / path
        try:
            mode = source.lstat().st_mode
            data = source.read_bytes()
        except OSError as error:
            raise ReleaseContractError("local-release-export-invalid", "sealed Methodology support is unavailable") from error
        if stat.S_ISLNK(mode) or not stat.S_ISREG(mode) or hashlib.sha256(data).hexdigest() != digest:
            raise ReleaseContractError("local-release-export-invalid", "sealed Methodology support differs from its inventory")
        known.add(path)
        result.append((path, digest))
    return tuple(result)


def _same_exported_files(root: Path, source_copy: Path, files: tuple[tuple[PurePosixPath, str], ...]) -> None:
    for relative, digest in files:
        target = source_copy.joinpath(*relative.parts)
        try:
            mode = target.lstat().st_mode
            data = target.read_bytes()
        except OSError as error:
            raise ReleaseContractError("local-release-product-stale", "product Methodology source copy is incomplete") from error
        if stat.S_ISLNK(mode) or not stat.S_ISREG(mode) or hashlib.sha256(data).hexdigest() != digest:
            raise ReleaseContractError("local-release-product-stale", "product Methodology source copy differs from the sealed export")


def _validate_selected_session(project_root: Path, run: Any, context: Any) -> None:
    from release_actions import ReleaseActionRun, SelectedReleaseActionContext, _fingerprint
    from workflow_run_support import RunExecutionSession, SelectedRunError

    if type(run) is not ReleaseActionRun or type(context) is not SelectedReleaseActionContext:
        raise ReleaseContractError("local-release-context-untrusted", "local bindings require the retained selected Release Run")
    session = run.selected_action_session
    if type(session) is not RunExecutionSession:
        raise ReleaseContractError("local-release-session-unavailable", "local bindings require the actual selected Session")
    if (Path(session.tracker.root).resolve(strict=True) != project_root
            or context.project_root != str(project_root) or context.workflow_run_id != run.workflow_run_id
            or context.parent_workflow_run_id != run.workflow_run_id
            or context.parent_step_run_id != context.step_run_id
            or context.frozen_parameters_sha256 != run.frozen_parameters_sha256
            or _fingerprint(run.request) != run.frozen_parameters_sha256
            or session.request.get("mode") != "execute" or session.request.get("operation_route") != "release_version"):
        raise ReleaseContractError("local-release-session-mismatch", "local bindings differ from the selected Release Session")
    try:
        selected_request = type(run.request).model_validate(session.request.get("parameters"))
    except (TypeError, ValueError) as error:
        raise ReleaseContractError("local-release-session-mismatch", "selected Session has no exact Release input") from error
    if _fingerprint(selected_request) != run.frozen_parameters_sha256:
        raise ReleaseContractError("local-release-session-mismatch", "selected Session input differs from the frozen Release Run")
    records = {record.get("run_id"): record for record in session.actual.values()}
    action = records.get(context.action_run_id)
    step = records.get(context.step_run_id)
    workflow = records.get(context.workflow_run_id)
    if (not all(isinstance(item, Mapping) for item in (action, step, workflow))
            or action.get("kind") != "action" or step.get("kind") != "step" or workflow.get("kind") != "workflow"
            or action.get("parent_run_id") != context.step_run_id
            or step.get("parent_run_id") != context.workflow_run_id
            or action.get("definition", {}).get("atom_id") != context.action_atom_id
            or step.get("definition", {}).get("atom_id") != context.step_atom_id
            or workflow.get("definition", {}).get("atom_id") != "CA-O-164"
            or workflow.get("definition", {}).get("version") != 11
            or context.action_run_id in session.terminal or context.action_run_id in session.interrupted):
        raise ReleaseContractError("local-release-session-mismatch", "selected Session has no exact running local Release occurrence")
    try:
        provenance = session.read_recorded_action_start(context.action_run_id)
    except (KeyError, TypeError, ValueError, SelectedRunError) as error:
        raise ReleaseContractError("local-release-session-untrusted", "selected local Action start cannot be reopened") from error
    if provenance.parent_lineage != (context.step_run_id, context.workflow_run_id):
        raise ReleaseContractError("local-release-session-mismatch", "selected local Action has another parent lineage")


@dataclass(frozen=True)
class SelectedLocalReleaseBindings:
    """Retained-gate capabilities for the last three selected O164 phases."""

    root: Path
    layout: MethodologyLayout
    export: SealedMethodologyExport
    packet: RetainedNativeFullGatePacket
    atoms: tuple[_ExportedAtom, ...]
    supports: tuple[tuple[PurePosixPath, str], ...]
    workflow_run_id: str = ""
    action_run_id: str = ""
    checkpoint_refs: list[str] = field(default_factory=list)

    def _git(self, *arguments: str) -> bytes:
        result = subprocess.run(["git", "-C", str(self.root), *arguments],
                                capture_output=True, timeout=30, check=False)
        if result.returncode:
            raise ReleaseContractError("local-release-git-failed", "scoped Local release Git step failed; manual handling required")
        return result.stdout

    def _commit_changes(self, before: Mapping[str, object], after: Mapping[str, object], phase: str) -> None:
        paths = sorted(path for path in set(before) | set(after) if before.get(path) != after.get(path))
        if not paths:
            return
        run = _safe_relative(self.workflow_run_id, label="Workflow Run")
        if len(run.parts) != 1:
            raise ReleaseContractError("local-release-run-invalid", "Git checkpoint requires one actual Workflow Run")
        if self._git("diff", "--cached", "--name-only", "-z"):
            raise ReleaseContractError("local-release-git-index-not-empty", "preserve the existing index before Local release checkpoints")
        self._git("add", "-A", "--", *paths)
        staged = sorted(path.decode("utf-8") for path in self._git("diff", "--cached", "--name-only", "-z").split(b"\0") if path)
        if staged != paths:
            raise ReleaseContractError("local-release-git-scope-mismatch", "Local release staged paths differ from this step's observed changes")
        self._git("commit", "-m", f"chore(release): {phase.replace('_', ' ')}")
        commit = self._git("rev-parse", "HEAD").decode().strip()
        receipt = self.root / ".caprmedio_tmp/local_release" / run.as_posix() / f"{phase}.json"
        receipt.parent.mkdir(parents=True, exist_ok=True)
        with receipt.open("x", encoding="utf-8") as handle:
            json.dump({"workflow_run_id": self.workflow_run_id, "action_run_id": self.action_run_id,
                       "phase": phase, "commit": commit, "paths": paths}, handle, sort_keys=True)
        self.checkpoint_refs.append(receipt.relative_to(self.root).as_posix())

    @property
    def _files(self) -> tuple[tuple[PurePosixPath, str], ...]:
        return tuple((atom.relative, atom.digest) for atom in self.atoms) + self.supports

    def _reopen(self) -> None:
        observed = revalidate_sealed_methodology_export(self.export)
        if observed != self.export:
            raise ReleaseContractError("local-release-export-stale", "sealed Methodology export changed after full gate")
        # The packet was freshly verified by retained_native_promotion_packet;
        # re-open it for every destructive boundary rather than trusting this
        # in-memory wrapper as a grant.
        from release_full_gate import verify_detached_native_full_gate_evidence

        verify_detached_native_full_gate_evidence(
            self.packet.artifact_root,
            self.packet.retained_candidate,
            self.packet.suite,
            self.packet.build,
            self.packet.verification,
            self.packet.e2e,
            self.packet.evidence,
        )

    def deliver_sources(self) -> tuple[str, int]:
        """Replace only product-owned content with exact sealed active atoms."""

        self._reopen()
        core = _local_release_module()
        product = self.root / self.layout.product_root
        source_copy = self.root / self.layout.source_copy_root
        before = core._snapshot(product, root=self.root, preserve=core._PRESERVED_NAMES)
        core._clear_target(product, root=self.root, preserve=core._PRESERVED_NAMES, label="product")
        cleared = core._snapshot(product, root=self.root, preserve=core._PRESERVED_NAMES)
        self._commit_changes(before, cleared, "clear_product")
        source_copy.mkdir(parents=True, exist_ok=True)
        for relative, digest in self._files:
            source = self.root / self.export.source_export_root / relative
            target = source_copy.joinpath(*relative.parts)
            data = source.read_bytes()
            if hashlib.sha256(data).hexdigest() != digest:
                raise ReleaseContractError("local-release-export-stale", "sealed Methodology atom changed before product delivery")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        _same_exported_files(self.root, source_copy, self._files)
        self._commit_changes(cleared, core._snapshot(product, root=self.root, preserve=core._PRESERVED_NAMES), "copy_active_sources")
        return self.layout.source_copy_root, len(self.atoms)

    def compile_product(self) -> str:
        """Compile the delivered product root with the existing compiler."""

        self._reopen()
        source_copy = self.root / self.layout.source_copy_root
        _same_exported_files(self.root, source_copy, self._files)
        from COMPILE_APPLICABLE_METHODOLOGY.compile_applicable_methodology import (
            CompileError,
            MethodologyPaths,
            compile_report,
            generated_tree_digest,
            replace_outputs_atomically,
            stage_outputs,
        )

        places = MethodologyPaths(
            source=Path(self.layout.source_copy_root),
            output=Path(self.layout.applicable_root),
            structure_sha256=self.layout.structure_sha256,
            control_root=Path(self.layout.control_root),
        )
        report, candidates, snapshot = compile_report(self.root, places)
        if report.get("can_apply") is not True:
            raise ReleaseContractError("local-release-product-compile-blocked", "product Methodology has unresolved compiler diagnostics")
        expected = {(atom.relative.as_posix(), atom.atom_id, atom.version, atom.digest) for atom in self.atoms}
        observed = set()
        for candidate in candidates:
            path = Path(candidate.source_path)
            try:
                relative = path.relative_to(Path(self.layout.source_copy_root)).as_posix()
            except ValueError as error:
                raise ReleaseContractError("local-release-product-compile-mismatch", "product compiler selected a source outside the delivered Methodology") from error
            observed.add((relative, candidate.atom_id, candidate.version, candidate.source_sha256))
        if observed != expected:
            raise ReleaseContractError("local-release-product-compile-mismatch", "product compiler selection differs from the tested sealed Methodology compilation")
        try:
            core = _local_release_module()
            output = self.root / self.layout.applicable_root
            before = core._snapshot(output, root=self.root, preserve=frozenset())
            staging = stage_outputs(self.root, candidates, snapshot, places)
            replace_outputs_atomically(self.root, staging, places)
            self._commit_changes(before, core._snapshot(output, root=self.root, preserve=frozenset()), "compile_product")
            return generated_tree_digest(self.root, places)
        except CompileError as error:
            raise ReleaseContractError("local-release-product-compile-blocked", "product Methodology compiler did not complete") from error

    def snapshot_product(self) -> dict[str, object]:
        core = _local_release_module()
        return core._snapshot(self.root / self.layout.product_root, root=self.root, preserve=core._PRESERVED_NAMES)

    def install_product(self, *, product_before_publication: Mapping[str, object] | None = None) -> str:
        """Copy the gated product tree into installed Methodology, preserving settings."""

        self._reopen()
        _same_exported_files(self.root, self.root / self.layout.source_copy_root, self._files)
        core = _local_release_module()
        product = self.root / self.layout.product_root
        installed = self.root / self.layout.installed_root
        if not product.is_dir() or product.is_symlink():
            raise ReleaseContractError("local-release-product-missing", "gated product Methodology is unavailable for install")
        before = core._snapshot(installed, root=self.root, preserve=core._PRESERVED_NAMES)
        core._clear_target(installed, root=self.root, preserve=core._PRESERVED_NAMES, label="installed")
        cleared = core._snapshot(installed, root=self.root, preserve=core._PRESERVED_NAMES)
        self._commit_changes(before, cleared, "clear_installed_framework")
        core._copy_tree(product, installed, preserve=core._PRESERVED_NAMES)
        copied = core._snapshot(installed, root=self.root, preserve=core._PRESERVED_NAMES)
        # Any final tested-projection materialization belongs to this same
        # O169 checkpoint, not an additional release command or workflow.
        if product_before_publication is not None:
            cleared = {**cleared, **product_before_publication}
            copied = {**copied, **self.snapshot_product()}
        self._commit_changes(cleared, copied, "copy_product_to_installed_framework")
        return self.layout.installed_root

    def start_and_check_mcp(self, promotion: Any) -> tuple[Mapping[str, Any], str]:
        """Reopen the installed package and use its existing bounded HTTP launcher."""
        self._reopen()
        core = _local_release_module()
        def owned(relative: str) -> dict[str, object]:
            observed = core._snapshot(self.root / relative, root=self.root, preserve=core._PRESERVED_NAMES)
            return {Path(path).relative_to(relative).as_posix(): value for path, value in observed.items()}
        if owned(self.layout.installed_root) != owned(self.layout.product_root):
            raise ReleaseContractError("local-release-installed-product-mismatch", "native publication changed the installed Methodology away from the release product")
        from framework_package import verify_framework_package
        from installed_mcp_runtime import launch_installed_mcp_http
        launcher_root = _PROJECT_ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker"
        if str(launcher_root) not in sys.path:
            sys.path.insert(0, str(launcher_root))
        from project_mcp_launcher import Launcher
        package = verify_framework_package(self.root / ".caprmedio_install/releases" / promotion.package_manifest_sha256)
        result = launch_installed_mcp_http(
            self.root, self.layout.control_root, package,
            target_context_sha256=promotion.target_project_context_sha256,
            package_selector_sha256=promotion.package_selector_sha256,
            runtime_selector_sha256=promotion.runtime_selector_sha256,
            launcher=Launcher(),
        )
        receipt = self.root / ".caprmedio_tmp/local_release" / self.workflow_run_id / "mcp_start.json"
        receipt.parent.mkdir(parents=True, exist_ok=True)
        with receipt.open("x", encoding="utf-8") as handle:
            json.dump(result, handle, sort_keys=True)
        return result, receipt.relative_to(self.root).as_posix()


def create_selected_local_bindings(project_root: Path | str, *, run: Any, context: Any) -> SelectedLocalReleaseBindings:
    """Create the sole local-release factory from an admitted selected Session."""

    root = Path(project_root).resolve(strict=True)
    _validate_selected_session(root, run, context)
    if context.action_atom_id not in {"CA-O-166", "CA-O-169"}:
        raise ReleaseContractError("local-release-phase-unselected", "only O166 and O169 own local product transitions")
    candidate = run.candidate
    if not isinstance(candidate, ValidatedCandidate) or candidate.project_root != str(root):
        raise ReleaseContractError("local-release-candidate-missing", "local bindings require the frozen selected candidate")
    export = run.methodology_export
    if not isinstance(export, SealedMethodologyExport) or export.candidate != candidate:
        raise ReleaseContractError("local-release-export-missing", "local bindings require the sealed Methodology export")
    from release_compilation import SealedPrivateMethodologyCompilation, read_sealed_private_methodology_compilation

    compilation = run.portable_compilation
    suite = run.portable_suite
    package = run.prepared_portable_package
    if any(value is None for value in (compilation, suite, run.build, run.verification, run.e2e, run.full_gate, package)):
        raise ReleaseContractError("local-release-full-gate-missing", "local product transitions require complete retained full-gate evidence")
    private = read_sealed_private_methodology_compilation(export)
    if not isinstance(run.private_compilation, SealedPrivateMethodologyCompilation) or private != run.private_compilation:
        raise ReleaseContractError("local-release-private-compile-stale", "tested private Methodology compilation changed after the full gate")
    packet = retained_native_promotion_packet(
        candidate, compilation, suite, run.build, run.verification, run.e2e, run.full_gate, package,
    )
    layout = resolve_methodology_layout(root)
    observed = revalidate_sealed_methodology_export(export)
    if observed != export:
        raise ReleaseContractError("local-release-export-stale", "sealed Methodology export changed after the full gate")
    atoms = _export_atoms(export)
    return SelectedLocalReleaseBindings(root, layout, export, packet, atoms, _export_supports(export, atoms),
                                       context.workflow_run_id, context.action_run_id)


__all__ = ["SelectedLocalReleaseBindings", "create_selected_local_bindings"]
