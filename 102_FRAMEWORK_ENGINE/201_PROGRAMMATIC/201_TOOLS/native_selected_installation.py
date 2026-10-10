"""Read-only reopening of one final D598/D599/D604 native installation."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import tomllib

from framework_package import FrameworkPackageError, VerifiedFrameworkPackage, verify_current_package_selector
from installed_mcp_binding import InstalledMcpBinding, InstalledMcpBindingError, admit_installed_mcp_binding
from portable_runtime_materialization import PortableRuntimeMaterializationError, reopen_final_runtime_command_fragment
from retained_full_gate_packet import RetainedNativeFullGatePacket


_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_PROOF_KEYS = frozenset({
    "schema_version", "package_manifest_sha256", "framework_version", "version_toml_sha256",
    "source_catalog_sha256", "full_gate_receipt_sha256", "image_digest", "target_project_context_sha256",
    "state_generation", "installation_lock_generation", "installation_command_sha256", "command_sha256",
    "command_stage_manifest_sha256", "methodology_delivery_manifest_ref", "methodology_delivery_manifest_sha256",
    "selector_sha256",
})


class NativeSelectedInstallationError(RuntimeError):
    """Stable refusal from the final selected-native reader."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


@dataclass(frozen=True)
class NativeSelectedInstallation:
    package_manifest_sha256: str
    framework_version: str
    version_toml_sha256: str
    source_catalog_sha256: str
    full_gate_receipt_sha256: str
    image_digest: str
    target_project_context_sha256: str
    state_generation: int
    installation_lock_generation: str
    selector_sha256: str
    release_proof_sha256: str
    binding: InstalledMcpBinding


def _refuse(code: str, message: str) -> None:
    raise NativeSelectedInstallationError(code, message)


def _read(path: Path, *, code: str, mode: int = 0o600) -> bytes:
    try:
        for ancestor in (path, *path.parents):
            observed = os.lstat(ancestor)
            if stat.S_ISLNK(observed.st_mode):
                _refuse(code, "carrier has a symlink ancestor")
        observed = os.lstat(path)
        if not stat.S_ISREG(observed.st_mode) or (mode is not None and observed.st_mode & 0o777 != mode):
            _refuse(code, "carrier is missing or unsafe")
        payload = path.read_bytes()
        after = os.lstat(path)
        if (observed.st_dev, observed.st_ino, observed.st_size, observed.st_mtime_ns) != (
            after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns,
        ):
            _refuse(code, "carrier changed while being read")
        return payload
    except OSError as error:
        raise NativeSelectedInstallationError(code, "carrier cannot be reopened") from error


def _reopen_installation_command(
    root: Path,
    payload: bytes,
    digest: str,
    *,
    action_package: VerifiedFrameworkPackage,
    operators_registry_ref: Path,
):
    """Dispatch the two closed D604 command variants and reopen their authority."""

    try:
        operation = json.loads(payload.decode("utf-8")).get("operation")
    except (UnicodeDecodeError, json.JSONDecodeError, AttributeError) as error:
        raise NativeSelectedInstallationError("native-selected-installation-command-invalid", "installation command is not closed JSON") from error
    try:
        if operation == "install_framework_runtime":
            from framework_installation_command import (
                read_framework_installation_command_receipt,
                reopen_framework_installation_command_start,
            )
            receipt = read_framework_installation_command_receipt(payload, expected_sha256=digest)
            reopen_framework_installation_command_start(
                root,
                receipt,
                action_package=action_package,
                operators_registry_ref=operators_registry_ref,
            )
            return receipt
        if operation == "promote_selected_runtime":
            from selected_installation_command import (
                read_selected_installation_command_receipt,
                reopen_selected_installation_command_start,
            )
            receipt = read_selected_installation_command_receipt(payload, expected_sha256=digest)
            reopen_selected_installation_command_start(root, receipt)
            return receipt
    except Exception as error:
        raise NativeSelectedInstallationError("native-selected-installation-command-invalid", str(error)) from error
    _refuse("native-selected-installation-command-invalid", "installation command operation is not designated")


def reopen_current_native_installation(
    project_root: str | Path,
    verified_package: VerifiedFrameworkPackage,
    packet: RetainedNativeFullGatePacket,
    *,
    target_context_sha256: str,
) -> NativeSelectedInstallation:
    """Reopen final selected carriers and the original retained Full Gate packet."""

    if not isinstance(packet, RetainedNativeFullGatePacket):
        _refuse("native-selected-packet-invalid", "selected native installation requires a retained Full Gate packet")
    try:
        root = Path(project_root).resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise NativeSelectedInstallationError("native-selected-project-invalid", "Project root is unavailable") from error
    if root.is_symlink() or not root.is_dir():
        _refuse("native-selected-project-invalid", "Project root is unsafe")
    try:
        from release_full_gate import verify_detached_native_full_gate_evidence

        retained = verify_detached_native_full_gate_evidence(
            packet.artifact_root, packet.retained_candidate, packet.suite, packet.build,
            packet.verification, packet.e2e, packet.evidence,
        )
        binding = admit_installed_mcp_binding(root, verified_package, target_context_sha256=target_context_sha256)
    except (InstalledMcpBindingError, RuntimeError) as error:
        raise NativeSelectedInstallationError("native-selected-admission-invalid", str(error)) from error
    package_selector = _read(root / ".caprmedio_install/current.toml", code="native-selected-package-selector-invalid", mode=None)
    try:
        selected_package = verify_current_package_selector(package_selector, verified_package)
    except FrameworkPackageError as error:
        raise NativeSelectedInstallationError("native-selected-package-selector-invalid", str(error)) from error
    if selected_package.full_gate_receipt_sha256 != packet.evidence.receipt_sha256:
        _refuse("native-selected-packet-mismatch", "retained Full Gate receipt differs from selected package")
    selector = _read(root / ".caprmedio_runtime/installation/current.toml", code="native-selected-selector-invalid", mode=None)
    try:
        selected = tomllib.loads(selector.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise NativeSelectedInstallationError("native-selected-selector-invalid", "native selector is not TOML") from error
    generation = selected.get("state_generation") if isinstance(selected, dict) else None
    if isinstance(generation, bool) or not isinstance(generation, int) or generation < 1:
        _refuse("native-selected-selector-invalid", "native selector generation is invalid")
    proof = _read(root / ".caprmedio_runtime/installation/generations" / str(generation) / "release-proof.toml", code="native-selected-proof-invalid", mode=None)
    try:
        document = tomllib.loads(proof.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise NativeSelectedInstallationError("native-selected-proof-invalid", "release proof is not TOML") from error
    if not isinstance(document, dict) or set(document) != _PROOF_KEYS or type(document.get("schema_version")) is not int or document.get("schema_version") != 2:
        _refuse("native-selected-proof-invalid", "release proof schema is not closed")
    expected = {
        "package_manifest_sha256": binding.package_manifest_sha256,
        "framework_version": verified_package.framework_version,
        "version_toml_sha256": verified_package.version_toml_sha256,
        "source_catalog_sha256": binding.source_catalog_sha256,
        "full_gate_receipt_sha256": packet.evidence.receipt_sha256,
        "image_digest": binding.image_digest,
        "target_project_context_sha256": target_context_sha256,
        "state_generation": generation,
        "installation_lock_generation": selected.get("installation_lock_generation"),
        "selector_sha256": hashlib.sha256(selector).hexdigest(),
    }
    view = retained.view
    if (
        view.actual_package_manifest_sha256 != binding.package_manifest_sha256
        or view.source_catalog_sha256 != binding.source_catalog_sha256
        or view.framework_version != verified_package.framework_version
        or view.version_toml_sha256 != verified_package.version_toml_sha256
    ):
        _refuse("native-selected-packet-mismatch", "retained Full Gate packet does not attest the selected package")
    if packet.evidence.candidate_image_digest != "sha256:" + binding.image_digest:
        _refuse("native-selected-packet-mismatch", "retained Full Gate image differs from selected immutable image")
    if hashlib.sha256(selector).hexdigest() != binding.runtime_selector_sha256:
        _refuse("native-selected-selector-raced", "runtime selector changed after installed binding admission")
    if any(document.get(key) != value for key, value in expected.items()):
        _refuse("native-selected-proof-mismatch", "release proof differs from selected native carriers")
    if not all(_SHA256.fullmatch(str(document[key])) for key in (
        "installation_command_sha256", "command_sha256", "command_stage_manifest_sha256", "methodology_delivery_manifest_sha256",
    )):
        _refuse("native-selected-proof-invalid", "release proof command digests are invalid")
    try:
        from native_installation_proof import NativeInstallationProofError, read_native_methodology_delivery

        delivery = read_native_methodology_delivery(
            root,
            verified_package,
            target_context_sha256=target_context_sha256,
            manifest_ref=document["methodology_delivery_manifest_ref"],
            expected_manifest_sha256=document["methodology_delivery_manifest_sha256"],
            full_gate_packet=packet,
        )
    except NativeInstallationProofError as error:
        raise NativeSelectedInstallationError("native-selected-methodology-delivery-invalid", str(error)) from error
    if (
        delivery.manifest_ref != document["methodology_delivery_manifest_ref"]
        or delivery.manifest_sha256 != document["methodology_delivery_manifest_sha256"]
    ):
        _refuse("native-selected-methodology-delivery-mismatch", "final Methodology delivery differs from D604 proof")
    installation_digest = str(document["installation_command_sha256"])
    receipt_bytes = _read(
        root / ".caprmedio_runtime/installation/commands" / f"{installation_digest}.json",
        code="native-selected-installation-command-invalid",
        mode=None,
    )
    receipt = _reopen_installation_command(
        root,
        receipt_bytes,
        installation_digest,
        action_package=verified_package,
        operators_registry_ref=Path(binding.target_context.control_child_relpath) / "operators_registry.toml",
    )
    if (
        receipt.target_project_context_sha256 != target_context_sha256
        or receipt.package_manifest_sha256 != binding.package_manifest_sha256
        or receipt.full_gate_receipt_sha256 != packet.evidence.receipt_sha256
    ):
        _refuse("native-selected-installation-command-mismatch", "installation command differs from selected native evidence")
    try:
        reopen_final_runtime_command_fragment(
            root,
            verified_package,
            target_context_sha256=target_context_sha256,
            state_generation=generation,
            installation_lock_generation=document["installation_lock_generation"],
            command_sha256=document["command_sha256"],
            stage_manifest_sha256=document["command_stage_manifest_sha256"],
            release_proof_sha256=hashlib.sha256(proof).hexdigest(),
        )
    except PortableRuntimeMaterializationError as error:
        raise NativeSelectedInstallationError("native-selected-command-invalid", str(error)) from error
    return NativeSelectedInstallation(
        **{key: expected[key] for key in (
            "package_manifest_sha256", "framework_version", "version_toml_sha256", "source_catalog_sha256",
            "full_gate_receipt_sha256", "image_digest", "target_project_context_sha256", "state_generation",
            "installation_lock_generation", "selector_sha256",
        )},
        release_proof_sha256=hashlib.sha256(proof).hexdigest(), binding=binding,
    )


__all__ = ["NativeSelectedInstallation", "NativeSelectedInstallationError", "reopen_current_native_installation"]
