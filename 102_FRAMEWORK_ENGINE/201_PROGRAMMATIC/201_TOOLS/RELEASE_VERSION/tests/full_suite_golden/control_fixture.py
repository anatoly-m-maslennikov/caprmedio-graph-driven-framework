"""Retained, source-pinned controls for the disposable Unit driver Project.

The canonical live selector may lag an accepted Release graph.  This fixture
copies actual current or archived carriers by digest and constructs its private
selector from those copied sources; it never repairs the live selector.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import tomllib

from release_suite_reference_context import (
    ReleaseSuiteReferenceContextError,
    _forbid_non_control_path,
    _project_structure_ref,
    _read_regular,
    validate_copied_reference_rows,
)
from release_source_admission import derive_release_execution_source_snapshot
from selected_routes import PROJECT_SETTINGS_REF


_UNIT_DEADLINE_SETTINGS = (
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/"
    "caprmedio_framework_default_settings.toml",
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml",
)


# These two archived Prompt pins are unavailable from the live source tree or
# its Atom archives.  They are deliberately test-only copies from one sealed
# historical package; this fixture is neither a Project control source nor an
# installed-package fallback at test runtime.
_RETAINED_CONTROL_SOURCES_ROOT = Path(__file__).resolve().parent / "retained_control_sources"
_RETAINED_CONTROL_SOURCES_MANIFEST = _RETAINED_CONTROL_SOURCES_ROOT / "manifest.json"
_RETAINED_PACKAGE_MANIFEST_REF = (
    ".caprmedio_runtime/framework/releases/"
    "6f2e3a615a4f4d6da0f16831800f9e4b7ff84f89b89faeefc359f51711d28c57/manifest.toml"
)
_RETAINED_PACKAGE_MANIFEST_SHA256 = "6f2e3a615a4f4d6da0f16831800f9e4b7ff84f89b89faeefc359f51711d28c57"


def _pins(value: object) -> dict[str, str]:
    result: dict[str, str] = {}
    if isinstance(value, dict):
        path, digest = value.get("source_path"), value.get("digest")
        if isinstance(path, str) and isinstance(digest, str):
            result[path] = digest
        children = value.values()
    elif isinstance(value, list):
        children = value
    else:
        return result
    for child in children:
        for path, digest in _pins(child).items():
            prior = result.setdefault(path, digest)
            if prior != digest:
                raise RuntimeError(f"golden control pin disagrees for {path}")
    return result


def _retained_fixture_source(relative: str, digest: str | None) -> Path | None:
    """Return one closed, manifest-proven historic Prompt carrier for tests.

    A fixture entry is eligible only for the exact original source path and
    pin.  Its byte digest and mode are independently rechecked before copy;
    no package directory is consulted at test runtime.
    """

    relative = _forbid_non_control_path(relative).as_posix()
    if digest is None:
        return None
    try:
        fixture_root = _RETAINED_CONTROL_SOURCES_ROOT
        manifest_path = _RETAINED_CONTROL_SOURCES_MANIFEST
        if fixture_root.is_symlink() or manifest_path.is_symlink() or not manifest_path.is_file():
            raise ValueError("retained fixture root or manifest is unsafe")
        root = fixture_root.resolve(strict=True)
        if manifest_path.resolve(strict=True).parent != root:
            raise ValueError("retained fixture manifest escapes its fixture root")
        document = json.loads(manifest_path.read_bytes())
        if not isinstance(document, dict) or set(document) != {"schema_version", "provenance", "sources"}:
            raise ValueError("retained fixture manifest has an invalid schema")
        if document["schema_version"] != 1 or document["provenance"] != {
            "package_manifest_ref": _RETAINED_PACKAGE_MANIFEST_REF,
            "package_manifest_sha256": _RETAINED_PACKAGE_MANIFEST_SHA256,
        }:
            raise ValueError("retained fixture provenance is invalid")
        sources = document["sources"]
        if not isinstance(sources, list):
            raise ValueError("retained fixture sources are invalid")
        matches: list[dict[str, object]] = []
        source_paths: set[str] = set()
        for item in sources:
            if not isinstance(item, dict) or set(item) != {"source_path", "fixture_path", "sha256", "mode"}:
                raise ValueError("retained fixture source row is invalid")
            source_path = item["source_path"]
            fixture_path = item["fixture_path"]
            expected_digest = item["sha256"]
            mode = item["mode"]
            if (
                not isinstance(source_path, str)
                or not isinstance(fixture_path, str)
                or not isinstance(expected_digest, str)
                or len(expected_digest) != 64
                or any(character not in "0123456789abcdef" for character in expected_digest)
                or type(mode) is not int
                or mode < 0
                or mode > 0o777
            ):
                raise ValueError("retained fixture source row is malformed")
            try:
                source_path = _forbid_non_control_path(source_path).as_posix()
            except ReleaseSuiteReferenceContextError as error:
                raise ValueError("retained fixture source row is outside the control allowlist") from error
            fixture_relative = PurePosixPath(fixture_path)
            if (
                fixture_relative.is_absolute()
                or len(fixture_relative.parts) != 1
                or fixture_relative.name != fixture_path
                or fixture_relative.suffix != ".md"
                or source_path in source_paths
            ):
                raise ValueError("retained fixture source row is unsafe or duplicated")
            source_paths.add(source_path)
            if source_path == relative and expected_digest == digest:
                matches.append(item)
        if len(matches) > 1:
            raise ValueError("retained fixture has duplicate eligible source rows")
        if not matches:
            return None
        fixture = root / str(matches[0]["fixture_path"])
        if fixture.is_symlink() or not fixture.is_file() or fixture.resolve(strict=True).parent != root:
            raise ValueError("retained fixture carrier is unsafe")
        payload = fixture.read_bytes()
        if (
            hashlib.sha256(payload).hexdigest() != digest
            or (fixture.stat().st_mode & 0o777) != matches[0]["mode"]
        ):
            raise ValueError("retained fixture carrier differs from its sealed row")
        return fixture
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as error:
        raise RuntimeError("golden retained fixture is unavailable or invalid") from error


def _retained_source(repository: Path, relative: str, digest: str | None) -> Path:
    relative = _forbid_non_control_path(relative).as_posix()
    source = repository / relative
    if source.is_file() and not source.is_symlink():
        if digest is None or hashlib.sha256(source.read_bytes()).hexdigest() == digest:
            return source
    archive = source.parent / "archive"
    if archive.is_dir() and not archive.is_symlink():
        for carrier in sorted(archive.rglob("*.md")):
            if carrier.is_file() and not carrier.is_symlink():
                if hashlib.sha256(carrier.read_bytes()).hexdigest() == digest:
                    return carrier
    fixture = _retained_fixture_source(relative, digest)
    if fixture is not None:
        return fixture
    raise RuntimeError(f"golden control has no retained byte carrier: {relative}")


def copy_control_closure(repository: Path, root: Path) -> None:
    """Copy current Release controls without selecting historic portfolio pins.

    These files remain disposable fixture inputs. The real reader derives its
    virtual execution snapshot from them; this helper creates no manifest file.
    """

    repository = repository.resolve(strict=True)
    detached_binding = os.environ.get("CAPRMEDIO_RELEASE_SOURCE_BINDINGS")
    if repository == Path("/workspace") or detached_binding is not None:
        # Child test processes intentionally receive no suite environment.
        # /workspace is the driver's fixed read-only mount, not a live Project.
        # A supplied fixture frame is an equally explicit context selection;
        # neither branch may fall back to host source discovery.
        binding_path = repository / ".caprmedio_release/source_bindings.json"
        if (root.resolve() == repository
                or detached_binding is not None and Path(detached_binding) != binding_path
                or binding_path.parent.is_symlink() or binding_path.is_symlink()
                or not binding_path.is_file()):
            raise RuntimeError("detached golden fixture has no exact sealed source bindings")
        envelope = json.loads(binding_path.read_bytes())
        if not isinstance(envelope, dict) or envelope.get("schema_version") != 2:
            raise RuntimeError("detached golden fixture source bindings are invalid")
        rows = validate_copied_reference_rows(repository, envelope.get("reference_rows"))
        snapshot_row = next(row for row in rows if row.source_path.endswith("/_projection/release_execution_snapshot.json"))
        snapshot_payload, snapshot_mode = _read_regular(repository, snapshot_row.source_path)
        if hashlib.sha256(snapshot_payload).hexdigest() != snapshot_row.sha256 or snapshot_mode != snapshot_row.mode:
            raise RuntimeError("detached golden fixture snapshot changed before copy")
        snapshot = json.loads(snapshot_payload)
        for row in rows:
            # The disposable Project owns a narrower native Engine inventory.
            # Re-derive its virtual projection; retain only authoring bytes.
            if row == snapshot_row:
                continue
            payload, mode = _read_regular(repository, row.source_path)
            if hashlib.sha256(payload).hexdigest() != row.sha256 or mode != row.mode:
                raise RuntimeError("detached golden fixture reference changed before copy")
            target = root / row.source_path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)
            target.chmod(row.mode)
        settings = (root / PROJECT_SETTINGS_REF).read_bytes()
        structure_ref = _project_structure_ref(settings)
        structure = tomllib.loads((root / structure_ref).read_text(encoding="utf-8"))
        for unit in structure["scope_units"]:
            if unit.get("scope_unit_name") in {"TOOLS", "PROJECT_TOOLS"}:
                for role in ("04_requirement", "05_method", "06_evaluation", "07_delivery"):
                    relative = _forbid_non_control_path(str(Path(unit["authority_path"]) / role))
                    (root / relative).mkdir(parents=True, exist_ok=True)
        tool_relative = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/release_version.py"
        tool_payload, tool_mode = _read_regular(repository, tool_relative)
        target = root / tool_relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(tool_payload)
        target.chmod(tool_mode)
        route, admission, authority = derive_release_execution_source_snapshot(root)
        if (snapshot.get("routes") != [route] or snapshot.get("release_source_admissions") != [admission]
                or snapshot.get("release_execution_snapshot", {}).get("authority") != authority):
            raise RuntimeError("detached golden fixture differs from its captured Release definitions")
        return

    _route, admission, authority = derive_release_execution_source_snapshot(repository)
    pins = _pins(admission)
    pins[authority["source_path"]] = authority["digest"]
    settings_relative = PROJECT_SETTINGS_REF.as_posix()
    settings_source = repository / settings_relative
    project_structure_relative = _project_structure_ref(settings_source.read_bytes())
    required = set(pins) | {
        ".caprmedio_caprmedio/operators_registry.toml",
        settings_relative,
        project_structure_relative,
        *_UNIT_DEADLINE_SETTINGS,
    }
    for relative in sorted(required):
        relative = _forbid_non_control_path(relative).as_posix()
        source = repository / relative
        if source.is_symlink() or not source.is_file():
            raise RuntimeError(f"current golden control source is unavailable: {relative}")
        payload = source.read_bytes()
        if relative in pins and hashlib.sha256(payload).hexdigest() != pins[relative]:
            raise RuntimeError(f"current golden control source changed: {relative}")
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
        target.chmod(source.stat().st_mode & 0o777)

    # The current resolver checks both registered RMED namespaces. Mirror
    # their existing role directories, including an empty namespace when no
    # member in this fixture selects a carrier from it; invent no source pin.
    structure = tomllib.loads((root / project_structure_relative).read_text(encoding="utf-8"))
    for unit in structure["scope_units"]:
        if unit.get("scope_unit_name") not in {"TOOLS", "PROJECT_TOOLS"}:
            continue
        for role in ("04_requirement", "05_method", "06_evaluation", "07_delivery"):
            relative = Path(unit["authority_path"]) / role
            existing = repository / relative
            if existing.is_symlink() or not existing.is_dir():
                raise RuntimeError(f"current registered RMED directory unavailable: {relative}")
            (root / relative).mkdir(parents=True, exist_ok=True)

    # A control-only test Project still supplies the actual mapped Tool bytes
    # required by the implementation snapshot. Existing synthetic Engine
    # members remain the fixture's own native inventory, never replaced here.
    tool_relative = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/release_version.py"
    source = repository / tool_relative
    if source.is_symlink() or not source.is_file():
        raise RuntimeError("current release Tool fixture source is unavailable")
    target = root / tool_relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    target.chmod(source.stat().st_mode & 0o777)
    _copied_route, copied_admission, copied_authority = derive_release_execution_source_snapshot(root)
    if copied_admission != admission or copied_authority != authority:
        raise RuntimeError("current Release control fixture differs from its source snapshot")
