"""Retained-state carriers for the bounded legacy installation migration.

This module deliberately contains no process control.  It can inventory, copy,
verify, switch selector bytes, and retain evidence only while the caller owns
the per-Project installation publication lock.  A process acknowledgement is
input evidence; this library never signals, kills, starts, or replaces a
process.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import tempfile
import tomllib
from collections.abc import Mapping, Sequence
from typing import Any


SCHEMA_VERSION = 1
INSTALLATION_ROOT = Path(".caprmedio_runtime/installation")
LEGACY_INSTALLATION_ROOT = Path(".caprmedio_install")
LEGACY_SELECTOR = LEGACY_INSTALLATION_ROOT / "current.toml"
RUNTIME_SELECTOR = INSTALLATION_ROOT / "current.toml"
OWNED_LEGACY_ROOTS = (
    ("project_mcp", Path("runtime/project_mcp")),
    ("mcp_hot_reload", Path("runtime/mcp_hot_reload")),
    ("workflow_orchestrator", Path("runtime/workflow_orchestrator")),
)
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
MIGRATION_ID = re.compile(r"[a-zA-Z0-9][a-zA-Z0-9._-]{0,127}\Z")


class InstallationStateError(RuntimeError):
    """A retained migration state carrier is absent, unsafe, or changed."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(f"{code}: {message}")


def canonical_json(value: object) -> str:
    """Render stable evidence bytes without depending on an ambient serializer."""

    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _digest(value: object) -> str:
    return sha256_bytes(canonical_json(value).encode("utf-8"))


def _is_sha256(value: object) -> bool:
    return isinstance(value, str) and SHA256.fullmatch(value) is not None


def _project_root(project_root: Path | str) -> Path:
    try:
        root = Path(project_root).absolute()
    except (TypeError, ValueError, OSError) as error:
        raise InstallationStateError("installation-project-invalid", "Project root is invalid") from error
    try:
        observed = root.lstat()
    except FileNotFoundError as error:
        raise InstallationStateError("installation-project-invalid", "Project root is missing") from error
    if root.is_symlink() or not stat.S_ISDIR(observed.st_mode):
        raise InstallationStateError("installation-project-unsafe", "Project root must be a real directory")
    return root


def _migration_id(value: str) -> str:
    if not isinstance(value, str) or not MIGRATION_ID.fullmatch(value):
        raise InstallationStateError("migration-id-invalid", "migration ID must be a safe component")
    return value


def migration_directory(project_root: Path | str, migration_id: str) -> Path:
    return _project_root(project_root) / INSTALLATION_ROOT / "migrations" / _migration_id(migration_id)


def _regular(path: Path, code: str) -> os.stat_result:
    try:
        observed = path.lstat()
    except FileNotFoundError as error:
        raise InstallationStateError(code, f"missing carrier: {path}") from error
    if path.is_symlink() or not stat.S_ISREG(observed.st_mode) or observed.st_nlink != 1:
        raise InstallationStateError(code, f"unsafe regular carrier: {path}")
    return observed


def _directory(path: Path, code: str) -> os.stat_result:
    try:
        observed = path.lstat()
    except FileNotFoundError as error:
        raise InstallationStateError(code, f"missing directory: {path}") from error
    if path.is_symlink() or not stat.S_ISDIR(observed.st_mode):
        raise InstallationStateError(code, f"unsafe directory: {path}")
    return observed


def _mkdirs(path: Path) -> None:
    """Make a private carrier chain while refusing pre-existing symlink hops."""

    # Every mutable carrier in this module is below this exact Project-local
    # root.  Walking from it (rather than from the nearest existing ancestor)
    # prevents an already-populated ``migrations`` symlink from escaping the
    # Project before a later child is checked.
    project_root: Path | None = None
    for ancestor in (path, *path.parents):
        if ancestor.name == INSTALLATION_ROOT.name and ancestor.parent.name == INSTALLATION_ROOT.parts[0]:
            project_root = ancestor.parent.parent
            break
    if project_root is None:
        raise InstallationStateError("installation-carrier-unsafe", f"carrier is outside installation state: {path}")
    try:
        components = path.relative_to(project_root).parts
    except ValueError as error:
        raise InstallationStateError("installation-carrier-unsafe", f"carrier escapes Project: {path}") from error
    _directory(project_root, "installation-carrier-unsafe")
    current = project_root
    for part in components:
        current /= part
        try:
            current.mkdir(mode=0o700)
        except FileExistsError:
            pass
        _directory(current, "installation-carrier-unsafe")


def _atomic_write(path: Path, content: str | bytes, *, mode: int = 0o600) -> None:
    _mkdirs(path.parent)
    existing = None
    try:
        existing = path.lstat()
    except FileNotFoundError:
        pass
    if existing is not None and (path.is_symlink() or not stat.S_ISREG(existing.st_mode) or existing.st_nlink != 1):
        raise InstallationStateError("installation-carrier-unsafe", f"cannot replace unsafe carrier: {path}")
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            payload = content.encode("utf-8") if isinstance(content, str) else content
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        temporary.chmod(mode)
        os.replace(temporary, path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def _toml_scalar(value: object) -> str:
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, list) and all(isinstance(item, str) for item in value):
        return "[" + ", ".join(json.dumps(item, ensure_ascii=False) for item in value) + "]"
    raise InstallationStateError("installation-toml-invalid", f"unsupported TOML value: {value!r}")


def _render_toml(scalars: Mapping[str, object], tables: Mapping[str, Sequence[Mapping[str, object]]] = {}) -> str:
    lines = [f"{key} = {_toml_scalar(value)}" for key, value in scalars.items()]
    for name, rows in tables.items():
        for row in rows:
            lines.extend(("", f"[[{name}]]"))
            lines.extend(f"{key} = {_toml_scalar(value)}" for key, value in row.items())
    return "\n".join(lines) + "\n"


def _read_toml(path: Path, code: str) -> dict[str, Any]:
    _regular(path, code)
    try:
        document = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise InstallationStateError(code, f"cannot parse carrier: {path}") from error
    if not isinstance(document, dict):
        raise InstallationStateError(code, f"carrier root must be a table: {path}")
    return document


def _lock_for(project_root: Path, lock: object) -> None:
    if lock is None or Path(getattr(lock, "project_root", "")).absolute() != project_root:
        raise InstallationStateError("installation-lock-required", "a matching per-Project installation lock is required")
    revalidate = getattr(lock, "revalidate", None)
    if not callable(revalidate):
        raise InstallationStateError("installation-lock-required", "lock cannot revalidate publication ownership")
    revalidate()


def _scan_root(root: Path, name: str) -> list[dict[str, object]]:
    """Read a deterministic, no-symlink inventory for one explicitly owned root."""

    _directory(root, "legacy-root-missing")
    rows: list[dict[str, object]] = []

    def visit(path: Path, relative: Path) -> None:
        # Refuse sensitive names from directory-entry metadata before lstat or
        # payload access.  This keeps inventorying from becoming a read path
        # for dotenv or similarly protected carriers.
        if relative.parts and _protected_legacy_name(path.name):
            raise InstallationStateError("legacy-protected-name", f"legacy inventory refuses protected name: {path.name}")
        observed = path.lstat()
        if path.is_symlink():
            raise InstallationStateError("legacy-symlink", f"legacy inventory refuses symlink: {path}")
        mode = observed.st_mode & 0o777
        if stat.S_ISDIR(observed.st_mode):
            rows.append(
                {
                    "root": name,
                    "relative_path": relative.as_posix() if relative.parts else ".",
                    "type": "directory",
                    "sha256": sha256_bytes(b""),
                    "mode": mode,
                }
            )
            for child in sorted(path.iterdir(), key=lambda item: item.name):
                visit(child, relative / child.name)
            return
        if stat.S_ISREG(observed.st_mode) and observed.st_nlink == 1:
            rows.append(
                {
                    "root": name,
                    "relative_path": relative.as_posix(),
                    "type": "file",
                    "sha256": sha256_bytes(path.read_bytes()),
                    "mode": mode,
                }
            )
            return
        raise InstallationStateError("legacy-special-file", f"legacy inventory refuses special carrier: {path}")

    visit(root, Path())
    return rows


def _protected_legacy_name(name: str) -> bool:
    """Reject protected dotenv-shaped carriers by name without opening them."""

    return name.startswith(".env") or name.endswith(".env")


def _process_binding(observation: Mapping[str, object]) -> dict[str, object]:
    """The full immutable identity tuple; PID is intentionally excluded."""

    command = observation.get("command")
    release = observation.get("release")
    command_map = command if isinstance(command, Mapping) else {}
    release_map = release if isinstance(release, Mapping) else {}
    argv = command_map.get("argv")
    return {
        "owned_subtree": observation.get("owned_subtree"),
        "state_generation": observation.get("state_generation"),
        "observed_start_token": observation.get("observed_start_token"),
        "command_sha256": command_map.get("sha256"),
        "argv": list(argv) if isinstance(argv, list) else argv,
        "environment_sha256": command_map.get("environment_sha256"),
        "wrapper_sha256": command_map.get("wrapper_sha256"),
        "invocation_nonce": command_map.get("invocation_nonce"),
        "package_manifest_sha256": release_map.get("package_manifest_sha256"),
        "framework_version": release_map.get("framework_version"),
        "version_carrier_sha256": release_map.get("version_carrier_sha256"),
        "source_catalog_sha256": release_map.get("source_catalog_sha256"),
        "full_gate_receipt_sha256": release_map.get("full_gate_receipt_sha256"),
        "image_digest": release_map.get("image_digest"),
        "target_context_sha256": release_map.get("target_context_sha256"),
        "selector_sha256": release_map.get("selector_sha256"),
    }


def _process_identity(observation: Mapping[str, object]) -> str:
    return _digest(_process_binding(observation))


def _observation_rows(observations: Sequence[Mapping[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for observation in observations:
        if not isinstance(observation, Mapping):
            raise InstallationStateError("process-observation-invalid", "process observation must be a table")
        materialized = dict(observation)
        try:
            canonical_json(materialized)
        except (TypeError, ValueError) as error:
            raise InstallationStateError("process-observation-invalid", "process observation is not serializable") from error
        rows.append({"identity": _process_identity(materialized), "observation_json": canonical_json(materialized)})
    if len({str(row["identity"]) for row in rows}) != len(rows):
        raise InstallationStateError("process-observation-invalid", "process observations must have unique identities")
    return sorted(rows, key=lambda row: str(row["identity"]))


def _inventory_body(inventory: Mapping[str, object]) -> dict[str, object]:
    return {
        "schema_version": inventory.get("schema_version"),
        "migration_id": inventory.get("migration_id"),
        "target_context_sha256": inventory.get("target_context_sha256"),
        "source_roots": inventory.get("source_roots"),
        "rows": inventory.get("rows"),
        "owned_process_observations": inventory.get("owned_process_observations"),
        "legacy_selector_path": inventory.get("legacy_selector_path"),
        "legacy_selector_sha256": inventory.get("legacy_selector_sha256"),
        "legacy_selector_mode": inventory.get("legacy_selector_mode"),
        "prior_runtime_selector_sha256": inventory.get("prior_runtime_selector_sha256"),
    }


def build_legacy_inventory(
    project_root: Path | str,
    *,
    migration_id: str,
    target_context_sha256: str,
    process_observations: Sequence[Mapping[str, object]] = (),
) -> dict[str, object]:
    """Inventory exactly the three named legacy subtrees without changing them."""

    root = _project_root(project_root)
    migration = _migration_id(migration_id)
    if not _is_sha256(target_context_sha256):
        raise InstallationStateError("target-context-invalid", "target context must be a SHA-256 digest")
    legacy = root / LEGACY_INSTALLATION_ROOT
    _directory(legacy, "legacy-installation-missing")
    selector = root / LEGACY_SELECTOR
    selector_stat = _regular(selector, "legacy-selector-missing")
    prior_runtime_selector = root / RUNTIME_SELECTOR
    if prior_runtime_selector.exists():
        _regular(prior_runtime_selector, "runtime-selector-unsafe")
        prior_runtime_selector_sha256 = sha256_bytes(prior_runtime_selector.read_bytes())
    else:
        prior_runtime_selector_sha256 = ""
    source_roots: list[dict[str, object]] = []
    rows: list[dict[str, object]] = []
    for name, target in OWNED_LEGACY_ROOTS:
        source = legacy / name
        root_rows = _scan_root(source, name)
        source_roots.append(
            {
                "name": name,
                "source": (LEGACY_INSTALLATION_ROOT / name).as_posix(),
                "target": target.as_posix(),
                "row_count": len(root_rows),
            }
        )
        rows.extend(root_rows)
    observations = _observation_rows(process_observations)
    inventory: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "migration_id": migration,
        "target_context_sha256": target_context_sha256,
        "source_roots": source_roots,
        "rows": rows,
        "owned_process_observations": observations,
        "legacy_selector_path": LEGACY_SELECTOR.as_posix(),
        "legacy_selector_sha256": sha256_bytes(selector.read_bytes()),
        "legacy_selector_mode": selector_stat.st_mode & 0o777,
        # This reference preserves prior selected-state provenance without
        # claiming adjacent legacy state is installation-owned.
        "prior_runtime_selector_sha256": prior_runtime_selector_sha256,
    }
    inventory["inventory_sha256"] = _digest(_inventory_body(inventory))
    return inventory


def _validated_inventory(inventory: Mapping[str, object]) -> dict[str, object]:
    materialized = dict(inventory)
    if materialized.get("schema_version") != SCHEMA_VERSION:
        raise InstallationStateError("inventory-invalid", "inventory schema is unsupported")
    if not isinstance(materialized.get("migration_id"), str):
        raise InstallationStateError("inventory-invalid", "inventory migration ID is missing")
    _migration_id(str(materialized["migration_id"]))
    if not _is_sha256(materialized.get("target_context_sha256")):
        raise InstallationStateError("inventory-invalid", "inventory target context is invalid")
    if not isinstance(materialized.get("source_roots"), list) or not isinstance(materialized.get("rows"), list):
        raise InstallationStateError("inventory-invalid", "inventory rows are missing")
    if not isinstance(materialized.get("owned_process_observations"), list):
        raise InstallationStateError("inventory-invalid", "inventory process observations are missing")
    if (
        materialized.get("legacy_selector_path") != LEGACY_SELECTOR.as_posix()
        or not _is_sha256(materialized.get("legacy_selector_sha256"))
        or not isinstance(materialized.get("legacy_selector_mode"), int)
        or not isinstance(materialized.get("prior_runtime_selector_sha256"), str)
        or (materialized["prior_runtime_selector_sha256"] and not _is_sha256(materialized["prior_runtime_selector_sha256"]))
    ):
        raise InstallationStateError("inventory-invalid", "selector provenance is invalid")
    actual = _digest(_inventory_body(materialized))
    if materialized.get("inventory_sha256") != actual:
        raise InstallationStateError("inventory-tampered", "inventory digest differs")
    names = [row.get("name") for row in materialized["source_roots"] if isinstance(row, Mapping)]
    if names != [name for name, _ in OWNED_LEGACY_ROOTS]:
        raise InstallationStateError("inventory-invalid", "inventory roots are not the exact owned set")
    return materialized


def verify_inventory(project_root: Path | str, inventory: Mapping[str, object]) -> None:
    """Reopen all source rows and reject every changed byte, mode, or path."""

    checked = _validated_inventory(inventory)
    observations: list[Mapping[str, object]] = []
    for row in checked["owned_process_observations"]:  # type: ignore[index]
        if not isinstance(row, Mapping) or not isinstance(row.get("observation_json"), str):
            raise InstallationStateError("inventory-invalid", "inventory process observation is invalid")
        decoded = json.loads(str(row["observation_json"]))
        if not isinstance(decoded, dict):
            raise InstallationStateError("inventory-invalid", "inventory process observation must decode to a table")
        observations.append(decoded)
    rebuilt = build_legacy_inventory(
        project_root,
        migration_id=str(checked["migration_id"]),
        target_context_sha256=str(checked["target_context_sha256"]),
        process_observations=observations,
    )
    if rebuilt["inventory_sha256"] != checked["inventory_sha256"]:
        raise InstallationStateError("inventory-changed", "legacy bytes, modes, paths, or observations changed")


def _inventory_toml(inventory: Mapping[str, object]) -> str:
    checked = _validated_inventory(inventory)
    roots = [dict(row) for row in checked["source_roots"] if isinstance(row, Mapping)]  # type: ignore[index]
    rows = [dict(row) for row in checked["rows"] if isinstance(row, Mapping)]  # type: ignore[index]
    observations = [dict(row) for row in checked["owned_process_observations"] if isinstance(row, Mapping)]  # type: ignore[index]
    return _render_toml(
        {
            "schema_version": SCHEMA_VERSION,
            "migration_id": str(checked["migration_id"]),
            "target_context_sha256": str(checked["target_context_sha256"]),
            "inventory_sha256": str(checked["inventory_sha256"]),
            "legacy_selector_path": str(checked["legacy_selector_path"]),
            "legacy_selector_sha256": str(checked["legacy_selector_sha256"]),
            "legacy_selector_mode": int(checked["legacy_selector_mode"]),
            "prior_runtime_selector_sha256": str(checked["prior_runtime_selector_sha256"]),
        },
        {"source_roots": roots, "rows": rows, "owned_process_observations": observations},
    )


def write_inventory(project_root: Path | str, inventory: Mapping[str, object], *, lock: object) -> Path:
    root = _project_root(project_root)
    _lock_for(root, lock)
    checked = _validated_inventory(inventory)
    path = migration_directory(root, str(checked["migration_id"])) / "inventory.toml"
    _atomic_write(path, _inventory_toml(checked), mode=0o600)
    _lock_for(root, lock)
    return path


def read_inventory(project_root: Path | str, migration_id: str) -> dict[str, object]:
    document = _read_toml(migration_directory(project_root, migration_id) / "inventory.toml", "inventory-unavailable")
    inventory = {
        "schema_version": document.get("schema_version"),
        "migration_id": document.get("migration_id"),
        "target_context_sha256": document.get("target_context_sha256"),
        "source_roots": document.get("source_roots", []),
        "rows": document.get("rows", []),
        "owned_process_observations": document.get("owned_process_observations", []),
        "legacy_selector_path": document.get("legacy_selector_path"),
        "legacy_selector_sha256": document.get("legacy_selector_sha256"),
        "legacy_selector_mode": document.get("legacy_selector_mode"),
        "prior_runtime_selector_sha256": document.get("prior_runtime_selector_sha256"),
        "inventory_sha256": document.get("inventory_sha256"),
    }
    return _validated_inventory(inventory)


def _proof_status(
    proof: Mapping[str, object],
    target_context_sha256: str,
    *,
    selector_sha256: str | None = None,
    state_generation: str | None = None,
) -> tuple[str, str]:
    subtree = proof.get("owned_subtree")
    if subtree not in {name for name, _ in OWNED_LEGACY_ROOTS}:
        return "unowned-subtree", "process is not bound to an exact owned legacy subtree"
    command = proof.get("command")
    release = proof.get("release")
    shutdown = proof.get("shutdown")
    if not isinstance(command, Mapping) or not isinstance(release, Mapping) or not isinstance(shutdown, Mapping):
        return "pid-proof-insufficient", "PID lacks command, release, and shutdown evidence"
    required_command = ("sha256", "environment_sha256", "wrapper_sha256")
    if not all(_is_sha256(command.get(key)) for key in required_command):
        return "command-proof-invalid", "command digest bindings are incomplete"
    argv = command.get("argv")
    if not isinstance(argv, list) or not argv or any(
        not isinstance(value, str) or Path(value).is_absolute() or ".." in Path(value).parts for value in argv
    ):
        return "command-proof-invalid", "command argv must be exact package-relative arguments"
    if not isinstance(command.get("invocation_nonce"), str) or not command.get("invocation_nonce"):
        return "command-proof-invalid", "command invocation nonce is missing"
    if not isinstance(proof.get("state_generation"), str) or not proof.get("state_generation"):
        return "generation-proof-invalid", "state generation is missing"
    if state_generation is not None and proof.get("state_generation") != state_generation:
        return "generation-proof-stale", "process state generation changed"
    if not isinstance(proof.get("observed_start_token"), str) or not proof.get("observed_start_token"):
        return "generation-proof-invalid", "observed start token is missing"
    required_release = (
        "package_manifest_sha256",
        "version_carrier_sha256",
        "source_catalog_sha256",
        "full_gate_receipt_sha256",
        "target_context_sha256",
        "selector_sha256",
    )
    if not all(_is_sha256(release.get(key)) for key in required_release):
        return "release-proof-invalid", "release digest bindings are incomplete"
    image = release.get("image_digest")
    if not isinstance(image, str) or not image.startswith("sha256:") or not _is_sha256(image[7:]):
        return "release-proof-invalid", "image digest is missing or mutable"
    if not isinstance(release.get("framework_version"), str) or not release.get("framework_version"):
        return "release-proof-invalid", "framework version is missing"
    if release.get("target_context_sha256") != target_context_sha256:
        return "release-proof-stale", "release target context changed"
    if selector_sha256 is not None and release.get("selector_sha256") != selector_sha256:
        return "release-proof-stale", "release selector binding changed"
    if shutdown.get("requested") is not True or shutdown.get("response") != "acknowledged":
        return "quiescence-unacknowledged", "no safe shutdown acknowledgement was supplied"
    if shutdown.get("deadline_status") != "within-deadline":
        return "quiescence-timeout", "shutdown was not confirmed before its deadline"
    return "proven-quiescent", "process proof and injected shutdown acknowledgement match"


def _inventory_observations(inventory: Mapping[str, object]) -> list[dict[str, object]]:
    """Reopen the immutable observation snapshot retained in inventory.toml."""

    observations: list[dict[str, object]] = []
    for row in inventory["owned_process_observations"]:  # type: ignore[index]
        if not isinstance(row, Mapping) or not isinstance(row.get("identity"), str) or not isinstance(row.get("observation_json"), str):
            raise InstallationStateError("inventory-invalid", "inventory process observation is invalid")
        try:
            decoded = json.loads(str(row["observation_json"]))
        except json.JSONDecodeError as error:
            raise InstallationStateError("inventory-invalid", "inventory process observation is not JSON") from error
        if not isinstance(decoded, dict) or _process_identity(decoded) != row["identity"]:
            raise InstallationStateError("inventory-tampered", "inventory process binding differs")
        observations.append(decoded)
    return observations


def prove_quiescence(inventory: Mapping[str, object], process_observations: Sequence[Mapping[str, object]]) -> dict[str, object]:
    """Generate a proof from supplied evidence; it performs no process action."""

    checked = _validated_inventory(inventory)
    expected: dict[str, Mapping[str, object]] = {}
    for row in checked["owned_process_observations"]:  # type: ignore[index]
        if not isinstance(row, Mapping) or not isinstance(row.get("identity"), str):
            raise InstallationStateError("inventory-invalid", "inventory process observation is invalid")
        expected[str(row["identity"])] = row
    actual: dict[str, Mapping[str, object]] = {}
    for observation in process_observations:
        if not isinstance(observation, Mapping):
            raise InstallationStateError("process-observation-invalid", "process observation must be a table")
        identity = _process_identity(observation)
        if identity in actual:
            raise InstallationStateError("process-observation-invalid", "duplicate process observation")
        actual[identity] = observation
    processes: list[dict[str, object]] = []
    for identity in sorted(set(expected) | set(actual)):
        if identity not in expected:
            status, reason = "unobserved-process", "process was not frozen into the legacy inventory"
        elif identity not in actual:
            status, reason = "missing-process-proof", "an inventoried process lacks refreshed proof"
        else:
            status, reason = _proof_status(
                actual[identity],
                str(checked["target_context_sha256"]),
                selector_sha256=str(checked["legacy_selector_sha256"]),
            )
        processes.append({"identity": identity, "status": status, "reason": reason})
    proof: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "migration_id": checked["migration_id"],
        "target_context_sha256": checked["target_context_sha256"],
        "inventory_sha256": checked["inventory_sha256"],
        "safe": all(row["status"] == "proven-quiescent" for row in processes),
        "processes": processes,
    }
    proof["quiescence_sha256"] = _digest({key: value for key, value in proof.items() if key != "quiescence_sha256"})
    return proof


def _validated_quiescence(inventory: Mapping[str, object], quiescence: Mapping[str, object]) -> dict[str, object]:
    checked_inventory = _validated_inventory(inventory)
    checked = dict(quiescence)
    if (
        checked.get("schema_version") != SCHEMA_VERSION
        or checked.get("migration_id") != checked_inventory["migration_id"]
        or checked.get("target_context_sha256") != checked_inventory["target_context_sha256"]
        or checked.get("inventory_sha256") != checked_inventory["inventory_sha256"]
        or not isinstance(checked.get("safe"), bool)
        or not isinstance(checked.get("processes"), list)
    ):
        raise InstallationStateError("quiescence-invalid", "quiescence proof is not bound to this inventory")
    # A caller may recompute a digest over forged ``safe`` / ``processes``.
    # Reconstruct the only admissible proof from the frozen full evidence
    # tuple, including its injected shutdown acknowledgement, instead.
    expected = prove_quiescence(checked_inventory, _inventory_observations(checked_inventory))
    if checked != expected:
        raise InstallationStateError("quiescence-invalid", "quiescence must exactly match retained full process evidence")
    return expected


def write_quiescence(
    project_root: Path | str,
    inventory: Mapping[str, object],
    quiescence: Mapping[str, object],
    *,
    lock: object,
) -> Path:
    root = _project_root(project_root)
    _lock_for(root, lock)
    checked = _validated_quiescence(inventory, quiescence)
    rows = [dict(row) for row in checked["processes"] if isinstance(row, Mapping)]  # type: ignore[index]
    path = migration_directory(root, str(checked["migration_id"])) / "quiescence.toml"
    _atomic_write(
        path,
        _render_toml(
            {key: checked[key] for key in ("schema_version", "migration_id", "target_context_sha256", "inventory_sha256", "safe", "quiescence_sha256")},
            {"processes": rows},
        ),
        mode=0o600,
    )
    _lock_for(root, lock)
    return path


def read_quiescence(project_root: Path | str, inventory: Mapping[str, object]) -> dict[str, object]:
    """Reopen and recompute the retained quiescence proof before publication."""

    checked = _validated_inventory(inventory)
    document = _read_toml(
        migration_directory(project_root, str(checked["migration_id"])) / "quiescence.toml", "quiescence-unavailable"
    )
    proof = {
        "schema_version": document.get("schema_version"),
        "migration_id": document.get("migration_id"),
        "target_context_sha256": document.get("target_context_sha256"),
        "inventory_sha256": document.get("inventory_sha256"),
        "safe": document.get("safe"),
        "processes": document.get("processes", []),
        "quiescence_sha256": document.get("quiescence_sha256"),
    }
    return _validated_quiescence(checked, proof)


def _write_immutable(path: Path, content: str, *, mode: int = 0o600) -> None:
    """Create one evidence carrier once; a differing rewrite is never a retry."""

    if path.exists():
        _regular(path, "generation-proof-unsafe")
        if path.read_text(encoding="utf-8") != content:
            raise InstallationStateError("generation-proof-conflict", f"generation evidence already differs: {path}")
        return
    _atomic_write(path, content, mode=mode)


def write_generation_process_proof(
    project_root: Path | str,
    process_observation: Mapping[str, object],
    *,
    state_generation: str,
    target_context_sha256: str,
    lock: object,
) -> Path:
    """Retain command/release evidence for one proved runtime observation.

    The function records supplied evidence only.  In particular, ``pid`` and
    ``observed_start_token`` are supplemental and cannot make an incomplete
    release or command proof acceptable.
    """

    root = _project_root(project_root)
    _lock_for(root, lock)
    if not isinstance(state_generation, str) or not state_generation or "/" in state_generation or ".." in state_generation:
        raise InstallationStateError("state-generation-invalid", "state generation must be a safe non-empty component")
    if not _is_sha256(target_context_sha256):
        raise InstallationStateError("target-context-invalid", "target context must be a SHA-256 digest")
    status, reason = _proof_status(
        process_observation,
        target_context_sha256,
        selector_sha256=sha256_bytes(_selector_bytes(root)),
        state_generation=state_generation,
    )
    if status != "proven-quiescent":
        raise InstallationStateError(status, reason)
    if process_observation.get("state_generation") != state_generation:
        raise InstallationStateError("generation-proof-stale", "process state generation differs")
    command = process_observation["command"]
    release = process_observation["release"]
    shutdown = process_observation["shutdown"]
    if not isinstance(command, Mapping) or not isinstance(release, Mapping) or not isinstance(shutdown, Mapping):
        raise InstallationStateError("generation-proof-invalid", "proved process evidence changed shape")
    directory = root / INSTALLATION_ROOT / "generations" / state_generation
    release_fields = {
        "schema_version": SCHEMA_VERSION,
        "package_manifest_sha256": str(release["package_manifest_sha256"]),
        "framework_version": str(release["framework_version"]),
        "version_carrier_sha256": str(release["version_carrier_sha256"]),
        "source_catalog_sha256": str(release["source_catalog_sha256"]),
        "full_gate_receipt_sha256": str(release["full_gate_receipt_sha256"]),
        "image_digest": str(release["image_digest"]),
        "target_context_sha256": str(release["target_context_sha256"]),
        "selector_sha256": str(release["selector_sha256"]),
    }
    command_fields = {
        "schema_version": SCHEMA_VERSION,
        "command_sha256": str(command["sha256"]),
        "argv": list(command["argv"]),
        "environment_sha256": str(command["environment_sha256"]),
        "wrapper_sha256": str(command["wrapper_sha256"]),
        "state_generation": state_generation,
        "invocation_nonce": str(command["invocation_nonce"]),
    }
    process_fields = {
        "schema_version": SCHEMA_VERSION,
        "state_generation": state_generation,
        "command_sha256": str(command["sha256"]),
        "release_proof_sha256": _digest(release_fields),
        "pid": int(process_observation["pid"]) if isinstance(process_observation.get("pid"), int) else -1,
        "observed_start_token": str(process_observation["observed_start_token"]),
        "shutdown_response": str(shutdown["response"]),
        "shutdown_deadline_status": str(shutdown["deadline_status"]),
    }
    _write_immutable(directory / "release-proof.toml", _render_toml(release_fields))
    _write_immutable(directory / "command.toml", _render_toml(command_fields))
    _write_immutable(directory / "process.toml", _render_toml(process_fields))
    _lock_for(root, lock)
    return directory


def _selector_bytes(root: Path) -> bytes:
    selector = root / LEGACY_SELECTOR
    _regular(selector, "legacy-selector-missing")
    return selector.read_bytes()


def _staged_rows(stage_runtime: Path, inventory: Mapping[str, object]) -> dict[str, dict[str, object]]:
    rows: dict[str, dict[str, object]] = {}
    for name, _target in OWNED_LEGACY_ROOTS:
        for row in _scan_root(stage_runtime / name, name):
            relative = str(row["relative_path"])
            rows[f"{name}/{relative}" if relative != "." else name] = row
    return rows


def _mapping_toml(inventory: Mapping[str, object]) -> str:
    rows = [
        {"source": (LEGACY_INSTALLATION_ROOT / name).as_posix(), "target": target.as_posix()}
        for name, target in OWNED_LEGACY_ROOTS
    ]
    return _render_toml(
        {
            "schema_version": SCHEMA_VERSION,
            "migration_id": str(inventory["migration_id"]),
            "inventory_sha256": str(inventory["inventory_sha256"]),
        },
        {"mappings": rows},
    )


def _validate_mapping(project_root: Path | str, inventory: Mapping[str, object]) -> None:
    checked = _validated_inventory(inventory)
    document = _read_toml(
        migration_directory(project_root, str(checked["migration_id"])) / "mapping.toml", "mapping-unavailable"
    )
    expected = [
        {"source": (LEGACY_INSTALLATION_ROOT / name).as_posix(), "target": target.as_posix()}
        for name, target in OWNED_LEGACY_ROOTS
    ]
    if (
        document.get("schema_version") != SCHEMA_VERSION
        or document.get("migration_id") != checked["migration_id"]
        or document.get("inventory_sha256") != checked["inventory_sha256"]
        or document.get("mappings") != expected
    ):
        raise InstallationStateError("mapping-invalid", "migration mapping is not the exact retained three-root mapping")


def _copy_inventory_rows(root: Path, inventory: Mapping[str, object], stage_runtime: Path) -> None:
    for row in inventory["rows"]:  # type: ignore[index]
        if not isinstance(row, Mapping):
            raise InstallationStateError("inventory-invalid", "inventory row is invalid")
        name = row.get("root")
        relative = row.get("relative_path")
        kind = row.get("type")
        if not isinstance(name, str) or not isinstance(relative, str) or kind not in {"directory", "file"}:
            raise InstallationStateError("inventory-invalid", "inventory row is unsafe")
        source = root / LEGACY_INSTALLATION_ROOT / name
        destination = stage_runtime / name
        if relative != ".":
            candidate = Path(relative)
            if candidate.is_absolute() or ".." in candidate.parts:
                raise InstallationStateError("inventory-invalid", "inventory path is unsafe")
            source /= candidate
            destination /= candidate
        if kind == "directory":
            destination.mkdir(parents=True, exist_ok=False)
            destination.chmod(int(row["mode"]))
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination, follow_symlinks=False)
            destination.chmod(int(row["mode"]))


def stage_legacy_copy(
    project_root: Path | str,
    inventory: Mapping[str, object],
    quiescence: Mapping[str, object],
    *,
    lock: object,
) -> dict[str, object]:
    """Copy exact frozen rows to private staging after only proven quiescence."""

    root = _project_root(project_root)
    _lock_for(root, lock)
    checked = _validated_inventory(inventory)
    proof = _validated_quiescence(checked, quiescence)
    if not proof["safe"]:
        raise InstallationStateError("migration-quiescence-blocked", "unsafe process proof blocks copy without process action")
    verify_inventory(root, checked)
    migration_root = migration_directory(root, str(checked["migration_id"]))
    stage = migration_root / "staging"
    if stage.exists():
        raise InstallationStateError("migration-stage-exists", "existing staged bytes require recovery, not replay")
    _mkdirs(migration_root)
    stage_runtime = stage / "runtime"
    try:
        _copy_inventory_rows(root, checked, stage_runtime)
        selector = _selector_bytes(root)
        stage_selector = stage / "selector" / "current.toml"
        _atomic_write(stage_selector, selector, mode=0o600)
        rows = _staged_rows(stage_runtime, checked)
        staged: dict[str, object] = {
            "schema_version": SCHEMA_VERSION,
            "migration_id": checked["migration_id"],
            "inventory_sha256": checked["inventory_sha256"],
            "source_selector_sha256": sha256_bytes(selector),
            "staged_selector_sha256": sha256_bytes(stage_selector.read_bytes()),
            "rows": rows,
        }
        staged["destination_inventory_sha256"] = _digest(rows)
        _atomic_write(
            migration_root / "mapping.toml", _mapping_toml(checked), mode=0o600
        )
        _atomic_write(
            migration_root / "copy-proof.toml",
            _render_toml(
                {
                    "schema_version": SCHEMA_VERSION,
                    "migration_id": str(checked["migration_id"]),
                    "source_inventory_sha256": str(checked["inventory_sha256"]),
                    "destination_inventory_sha256": str(staged["destination_inventory_sha256"]),
                    "source_selector_sha256": str(staged["source_selector_sha256"]),
                    "staged_selector_sha256": str(staged["staged_selector_sha256"]),
                }
            ),
            mode=0o600,
        )
    except BaseException:
        # Staging is retained for inspection/recovery.  It is deliberately not deleted.
        raise
    _lock_for(root, lock)
    return staged


def verify_staged_copy(project_root: Path | str, inventory: Mapping[str, object], staged: Mapping[str, object]) -> None:
    root = _project_root(project_root)
    checked = _validated_inventory(inventory)
    if staged.get("migration_id") != checked["migration_id"] or staged.get("inventory_sha256") != checked["inventory_sha256"]:
        raise InstallationStateError("staged-copy-invalid", "staged copy does not bind this inventory")
    _validate_mapping(root, checked)
    stage_runtime = migration_directory(root, str(checked["migration_id"])) / "staging" / "runtime"
    actual = _staged_rows(stage_runtime, checked)
    copy_proof = _read_toml(
        migration_directory(root, str(checked["migration_id"])) / "copy-proof.toml", "copy-proof-unavailable"
    )
    if (
        copy_proof.get("schema_version") != SCHEMA_VERSION
        or copy_proof.get("migration_id") != checked["migration_id"]
        or copy_proof.get("source_inventory_sha256") != checked["inventory_sha256"]
        or copy_proof.get("destination_inventory_sha256") != _digest(actual)
        or copy_proof.get("source_selector_sha256") != checked["legacy_selector_sha256"]
        or copy_proof.get("staged_selector_sha256") != checked["legacy_selector_sha256"]
    ):
        raise InstallationStateError("staged-copy-tampered", "retained copy proof differs from exact staged state")
    source_rows = {
        f"{row['root']}/{row['relative_path']}" if row["relative_path"] != "." else str(row["root"]): row
        for row in checked["rows"]  # type: ignore[index]
        if isinstance(row, Mapping)
    }
    for path, row in source_rows.items():
        staged_row = actual.get(path)
        if staged_row is None or any(staged_row.get(key) != row.get(key) for key in ("type", "sha256", "mode")):
            raise InstallationStateError("staged-copy-mismatch", f"copied row differs: {path}")
    selector = migration_directory(root, str(checked["migration_id"])) / "staging" / "selector" / "current.toml"
    _regular(selector, "staged-selector-missing")
    if sha256_bytes(selector.read_bytes()) != checked["legacy_selector_sha256"]:
        raise InstallationStateError("staged-selector-tampered", "staged selector differs")


def switch_runtime_selector(
    project_root: Path | str,
    inventory: Mapping[str, object],
    staged: Mapping[str, object],
    *,
    state_generation: str,
    lock: object,
) -> dict[str, object]:
    """Atomically publish only verified selector bytes; legacy carriers remain untouched."""

    root = _project_root(project_root)
    _lock_for(root, lock)
    if not isinstance(state_generation, str) or not state_generation:
        raise InstallationStateError("state-generation-invalid", "state generation is required")
    supplied = _validated_inventory(inventory)
    # Do not publish from a caller-constructed inventory or quiescence map.
    # The retained carriers are reopened under the still-held publication lock.
    checked = read_inventory(root, str(supplied["migration_id"]))
    if checked != supplied:
        raise InstallationStateError("inventory-tampered", "caller inventory differs from retained inventory")
    verify_inventory(root, checked)
    proof = read_quiescence(root, checked)
    if not proof["safe"]:
        raise InstallationStateError("migration-quiescence-blocked", "retained quiescence proof is unsafe")
    for observation in _inventory_observations(checked):
        status, reason = _proof_status(
            observation,
            str(checked["target_context_sha256"]),
            selector_sha256=str(checked["legacy_selector_sha256"]),
            state_generation=state_generation,
        )
        if status != "proven-quiescent":
            raise InstallationStateError("migration-quiescence-blocked", reason)
    verify_staged_copy(root, checked, staged)
    source_selector = _selector_bytes(root)
    if sha256_bytes(source_selector) != checked["legacy_selector_sha256"]:
        raise InstallationStateError("legacy-selector-changed", "legacy selector changed after staging")
    selector = migration_directory(root, str(checked["migration_id"])) / "staging" / "selector" / "current.toml"
    new_bytes = selector.read_bytes()
    runtime_selector = root / RUNTIME_SELECTOR
    previous: bytes | None = runtime_selector.read_bytes() if runtime_selector.exists() else None
    if runtime_selector.exists():
        _regular(runtime_selector, "runtime-selector-unsafe")
        _atomic_write(migration_directory(root, str(checked["migration_id"])) / "prior-selector.toml", previous or b"", mode=0o600)
    _atomic_write(runtime_selector, new_bytes, mode=0o600)
    switched = {
        "schema_version": SCHEMA_VERSION,
        "migration_id": checked["migration_id"],
        "state_generation": state_generation,
        "previous_selector_sha256": sha256_bytes(previous) if previous is not None else "",
        "replacement_selector_sha256": sha256_bytes(new_bytes),
        "source_inventory_sha256": checked["inventory_sha256"],
        "prior_history_reference": "prior-selector.toml" if previous is not None else "",
    }
    try:
        _atomic_write(
            migration_directory(root, str(checked["migration_id"])) / "switch.toml", _render_toml(switched), mode=0o600
        )
    except OSError as error:
        # The selector write has returned successfully, so recovery must report
        # its actual selected state and record only the missing receipt.
        raise InstallationStateError(
            "switch-recording-pending", "selector was published but switch receipt recording is pending"
        ) from error
    _lock_for(root, lock)
    return switched


def write_transaction_status(
    project_root: Path | str,
    inventory: Mapping[str, object],
    *,
    phase: str,
    status: str,
    lock: object,
) -> Path:
    root = _project_root(project_root)
    _lock_for(root, lock)
    checked = _validated_inventory(inventory)
    path = migration_directory(root, str(checked["migration_id"])) / "transaction.toml"
    _atomic_write(
        path,
        _render_toml(
            {
                "schema_version": SCHEMA_VERSION,
                "migration_id": str(checked["migration_id"]),
                "inventory_sha256": str(checked["inventory_sha256"]),
                "phase": phase,
                "status": status,
            }
        ),
        mode=0o600,
    )
    _lock_for(root, lock)
    return path


def append_history(
    project_root: Path | str,
    inventory: Mapping[str, object],
    *,
    phase: str,
    status: str,
    selector_changed: bool,
    lock: object,
) -> Path:
    """Append actual migration outcome without granting cleanup authority."""

    root = _project_root(project_root)
    _lock_for(root, lock)
    checked = _validated_inventory(inventory)
    path = migration_directory(root, str(checked["migration_id"])) / "history.toml"
    attempts: list[dict[str, object]] = []
    if path.exists():
        document = _read_toml(path, "history-invalid")
        old = document.get("attempts", [])
        if not isinstance(old, list) or any(not isinstance(row, Mapping) for row in old):
            raise InstallationStateError("history-invalid", "migration history is not append-only rows")
        attempts.extend(dict(row) for row in old)
    attempts.append(
        {
            "migration_id": str(checked["migration_id"]),
            "inventory_sha256": str(checked["inventory_sha256"]),
            "phase": phase,
            "status": status,
            "selector_changed": selector_changed,
        }
    )
    _atomic_write(path, _render_toml({"schema_version": SCHEMA_VERSION}, {"attempts": attempts}), mode=0o600)
    _lock_for(root, lock)
    return path


def cleanup_legacy_state(*_args: object, **_kwargs: object) -> None:
    """Refuse all cleanup here; later exact approval is a separate operation."""

    raise InstallationStateError("legacy-cleanup-deferred", "this retained-state migration library never deletes legacy carriers")


__all__ = [
    "INSTALLATION_ROOT",
    "LEGACY_INSTALLATION_ROOT",
    "LEGACY_SELECTOR",
    "OWNED_LEGACY_ROOTS",
    "RUNTIME_SELECTOR",
    "SCHEMA_VERSION",
    "InstallationStateError",
    "append_history",
    "build_legacy_inventory",
    "canonical_json",
    "cleanup_legacy_state",
    "migration_directory",
    "prove_quiescence",
    "read_inventory",
    "sha256_bytes",
    "stage_legacy_copy",
    "switch_runtime_selector",
    "verify_inventory",
    "verify_staged_copy",
    "write_inventory",
    "write_generation_process_proof",
    "write_quiescence",
    "write_transaction_status",
]
