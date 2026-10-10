"""Retained, source-pinned controls for the disposable Unit driver Project.

The canonical live selector may lag an accepted Release graph.  This fixture
copies actual current or archived carriers by digest and constructs its private
selector from those copied sources; it never repairs the live selector.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import tomllib

from release_suite_reference_context import (
    ReleaseSuiteReferenceContextError,
    _forbid_non_control_path,
    _project_structure_ref,
    _prompt_binding_rows,
    _selected_source_refresh_frontier,
)
from release_source_admission import (
    AUTHORITY_PIN,
    derive_release_graph_admission,
    derive_release_source_admission,
)
from selected_routes import PROJECT_SETTINGS_REF, canonical_digest, canonical_json, selected_manifest_ref


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
    """Build a synthetic selector while retaining real source-admission guards."""

    manifest_ref = selected_manifest_ref(repository)
    manifest = json.loads((repository / manifest_ref).read_bytes())
    # Replace only the private fixture's Release route.  An obsolete live
    # Release graph must not select retired bytes for the new admission.
    manifest["routes"] = [route for route in manifest["routes"] if route["route"] != "release_version"]
    manifest.pop("release_source_admissions", None)
    admission = derive_release_source_admission(repository)
    pins = _pins(manifest)
    for path, digest in _pins(admission).items():
        prior = pins.setdefault(path, digest)
        if prior != digest:
            raise RuntimeError(f"golden control pin disagrees for {path}")
    pins[AUTHORITY_PIN["source_path"]] = AUTHORITY_PIN["digest"]
    freshness = manifest["source_freshness"]
    pins[freshness["selected_source_registry_ref"]] = freshness["selected_source_registry_digest"]
    settings_relative = PROJECT_SETTINGS_REF.as_posix()
    settings_source = _retained_source(repository, settings_relative, pins.get(settings_relative))
    project_structure_relative = _project_structure_ref(settings_source.read_bytes())
    required = set(pins) | {
        ".caprmedio_caprmedio/operators_registry.toml",
        settings_relative,
        project_structure_relative,
        *_UNIT_DEADLINE_SETTINGS,
    }
    for relative in sorted(required):
        source = _retained_source(repository, relative, pins.get(relative))
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
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

    # D580 declares a closed Prompt binding frontier.  Copy only its two
    # binding carriers and their exact pinned active Atom files; no directory
    # discovery or legacy Plan material is admitted into the retained fixture.
    d580_relative = next(path for path in pins if "/CA-D-580-" in path)
    for binding_relative, binding_digest in _prompt_binding_rows((root / d580_relative).read_bytes()):
        binding_source = _retained_source(repository, binding_relative, binding_digest)
        binding_target = root / binding_relative
        binding_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(binding_source, binding_target)
        binding_target.chmod(binding_source.stat().st_mode & 0o777)
        binding = json.loads(binding_target.read_bytes())
        for pin in binding["sources"]:
            atom_source = _retained_source(repository, pin["path"], pin["sha256"])
            atom_target = root / pin["path"]
            atom_target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(atom_source, atom_target)
            atom_target.chmod(atom_source.stat().st_mode & 0o777)

    # D580 separately declares five exact selected-source refresh authority
    # leaves.  They are not Prompt bindings, so copy and revalidate them as
    # their own closed frontier rather than discovering an MCP directory.
    refresh_paths = _selected_source_refresh_frontier((root / d580_relative).read_bytes(), {})
    for relative in refresh_paths:
        source = _retained_source(repository, relative, None)
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        target.chmod(source.stat().st_mode & 0o777)
    refresh_captured = {
        relative: ((root / relative).read_bytes(), (root / relative).stat().st_mode & 0o777)
        for relative in refresh_paths
    }
    _selected_source_refresh_frontier((root / d580_relative).read_bytes(), refresh_captured)

    # Current D572 is ID membership, not an implementation-code or resolver
    # proof block. Preserve only its actual authority bytes in this fixture.
    authority = root / AUTHORITY_PIN["source_path"]
    if hashlib.sha256(authority.read_bytes()).hexdigest() != AUTHORITY_PIN["digest"]:
        raise RuntimeError("golden current authority carrier changed")

    route, copied_admission = derive_release_graph_admission(root)
    manifest["routes"].append(route)
    manifest["release_source_admissions"] = [copied_admission]
    freshness["selected_binding_digest"] = canonical_digest(manifest["routes"])
    manifest["canonical_manifest_sha256"] = canonical_digest({
        key: value for key, value in manifest.items() if key != "canonical_manifest_sha256"
    })
    target = root / manifest_ref
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(canonical_json(manifest), encoding="utf-8", newline="\n")
    target.chmod((repository / manifest_ref).stat().st_mode & 0o777)
