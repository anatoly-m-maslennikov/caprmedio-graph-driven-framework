"""Fresh, source-pinned disposable Project for lifecycle caller checks.

The fixture owns no repository Atom state.  It materializes only the checked-in
source bytes and route shape under ``fixtures/container_lifecycle`` (captured
from the reviewed originals at authoring time), then exposes the public
preview/freeze boundary used by caller tests.
"""
from __future__ import annotations

from contextlib import contextmanager
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile
from typing import Any, Iterator, Mapping

from frozen_selected_workflows import (
    frozen_manifest,
    frozen_selected_root_paths,
    frozen_source_bytes,
    frozen_source_paths,
)


APP = Path(__file__).resolve().parents[1]
PROGRAMMATIC = APP.parents[1]
CONTROL = Path(".caprmedio_caprmedio")
MANIFEST_REF = ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json"
# Runtime reads this corpus only; it never resolves a source from the host Project.
FIXTURE_ROOT = Path(__file__).with_name("fixtures") / "container_lifecycle"
ROUTE_SHAPE = FIXTURE_ROOT / "route_shape.json"
TOOLS = PROGRAMMATIC / "FEATURE_TOOLS"
MCP = PROGRAMMATIC / "FEATURE_MCP"
for _path in (APP, TOOLS, MCP):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))
from scope_declaration_test_support import write_scope_unit_declarations


class ContainerLifecycleFixtureError(RuntimeError):
    """The source-pinned disposable lifecycle fixture is not admissible."""


def _digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _canonical_digest(value: object) -> str:
    raw = json.dumps(value, ensure_ascii=False, allow_nan=False,
                     sort_keys=True, separators=(",", ":")).encode("utf-8")
    return _digest(raw)


def _metadata_bytes(raw: bytes, label: str) -> dict[str, Any]:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ContainerLifecycleFixtureError(f"source is not UTF-8: {label}") from error
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        raise ContainerLifecycleFixtureError(f"source has no YAML frontmatter: {label}")
    values: dict[str, str] = {}
    for field in ("atom_id", "content_role", "type", "version"):
        found = re.search(rf"(?m)^{field}:\s*(?:\"([^\"]+)\"|'([^']+)'|([^\n#]+))", match.group(1))
        if found is not None:
            values[field] = next(value for value in found.groups() if value is not None).strip()
    if not values.get("atom_id") or not values.get("version", "").isdigit():
        raise ContainerLifecycleFixtureError(f"source identity is incomplete: {label}")
    values["version"] = int(values["version"])
    return values


def _safe_relative(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or not value:
        raise ContainerLifecycleFixtureError(f"unsafe fixture source path: {value!r}")
    return path


class ContainerLifecycleFixture:
    """Disposable Project with nested Plan carriers and a current selected route."""

    def __init__(self, root: str | Path | None = None) -> None:
        self._temporary: tempfile.TemporaryDirectory[str] | None = None
        if root is None:
            parent = APP.parents[3] / ".caprmedio_tmp" / "tests" / "container-lifecycle"
            parent.mkdir(parents=True, exist_ok=True)
            self._temporary = tempfile.TemporaryDirectory(
                prefix="native-", dir=parent, ignore_cleanup_errors=True,
            )
            self.root = Path(self._temporary.name).resolve()
        else:
            self.root = Path(root).resolve()
            self.root.mkdir(parents=True, exist_ok=True)
        self.manifest: dict[str, Any] | None = None
        self._current_pin_cache: dict[str, dict[str, Any]] | None = None
        self.scope_rows: dict[str, dict[str, Any]] | None = None
        self.parent_plan: Path | None = None
        self.child_plan: Path | None = None

    @property
    def manifest_path(self) -> Path:
        return self.root / MANIFEST_REF

    @property
    def current_route(self) -> dict[str, Any]:
        if self.manifest is None:
            raise ContainerLifecycleFixtureError("prepare the fixture before reading its route")
        matches = [route for route in self.manifest["routes"]
                   if route.get("route") == "change_atom_status"]
        if len(matches) != 1:
            raise ContainerLifecycleFixtureError("current lifecycle route is missing or duplicated")
        return matches[0]

    def prepare(self) -> "ContainerLifecycleFixture":
        (self.root / ".git").mkdir(parents=True, exist_ok=True)
        self._write_settings()
        self._write_structure()
        (self.root / CONTROL / "_journal").mkdir(parents=True, exist_ok=True)
        self._materialize_current_methodology_sources()
        self._materialize_pinned_closure()
        self._write_nested_plans()
        self._write_manifest()
        from selected_routes import load_selected_manifest

        self.manifest = load_selected_manifest(self.root)
        return self

    def close(self) -> None:
        if self._temporary is not None:
            self._temporary.cleanup()
            self._temporary = None

    def __enter__(self) -> "ContainerLifecycleFixture":
        return self.prepare()

    def __exit__(self, *_: object) -> None:
        self.close()

    def _write_settings(self) -> None:
        path = self.root / CONTROL / "caprmedio_project_settings.toml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            '[project]\nkey = "container-lifecycle-fixture"\nname = "caprmedio"\n'
            'repository_slug = "container-lifecycle-fixture"\n'
            '[artifacts.identity]\nproject_prefix = "CA"\n'
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
            'journal_root = ".caprmedio_caprmedio/_journal"\n'
            'runtime_root = ".caprmedio_runtime"\n',
            encoding="utf-8",
        )
        (self.root / CONTROL / "operators_registry.toml").write_text(
            '[[operators]]\nname = "Container Fixture"\nrole = "project owner"\n',
            encoding="utf-8",
        )

    def _write_structure(self) -> None:
        self.scope_rows = write_scope_unit_declarations(self.root, (
            {"scope_unit_name": "METHODOLOGY_SOURCES", "parent": "PROJECT",
             "scope_unit_type": "Unordered", "scope_unit_label": "METHODOLOGY"},
            {"scope_unit_name": "CORE_META_MODEL", "parent": "METHODOLOGY_SOURCES",
             "scope_unit_type": "Unordered", "scope_unit_label": "METHODOLOGY"},
            {"scope_unit_name": "PROJECT_CONFIGURATION", "parent": "METHODOLOGY_SOURCES",
             "scope_unit_type": "Ordered", "scope_unit_label": "LAYER", "local_order": 3},
            {"scope_unit_name": "STATUS_FIXTURE", "parent": "PROJECT",
             "scope_unit_type": "Unordered", "scope_unit_label": "FIXTURE"},
        ))

    def _materialize_current_methodology_sources(self) -> None:
        if self.scope_rows is None:
            raise ContainerLifecycleFixtureError("scope declarations were not materialized")
        core_authority = Path(self.scope_rows["CORE_META_MODEL"]["authority_path"])
        project_configuration_authority = Path(
            self.scope_rows["PROJECT_CONFIGURATION"]["authority_path"]
        )
        current_roots = (
            (
                Path(
                    ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/"
                    "CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL"
                ),
                core_authority,
            ),
            (
                Path(
                    ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/"
                    "CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION"
                ),
                project_configuration_authority,
            ),
        )
        for current_root, authority in current_roots:
            for source_path in frozen_source_paths():
                source = Path(source_path)
                try:
                    relative = source.relative_to(current_root)
                except ValueError:
                    continue
                destination = authority / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(frozen_source_bytes(source_path))
        support_source = FIXTURE_ROOT / "sources" / "CA-R-793.md"
        raw = support_source.read_bytes()
        if _digest(raw) != "64390748e2831226ce86ecff6aad4391bd5d5264c79dd715b9ed6f99a5996bfa":
            raise ContainerLifecycleFixtureError("frozen support source is stale: CA-R-793")
        destination = core_authority / "04_requirement" / (
            "CA-R-793-CORE_META_MODEL--define-evaluation-approach-as-a-type-value-for-evaluation-atoms.md"
        )
        self._copy_source(raw, "CA-R-793", destination.relative_to(self.root).as_posix())

    def _current_pins(self) -> dict[str, dict[str, Any]]:
        if self._current_pin_cache is not None:
            return self._current_pin_cache
        result: dict[str, dict[str, Any]] = {}

        def collect(value: object) -> None:
            if isinstance(value, Mapping):
                if all(key in value for key in ("atom_id", "source_path", "version", "digest")):
                    atom_id = value["atom_id"]
                    pin = {
                        "atom_id": atom_id,
                        "source_path": value["source_path"],
                        "version": value["version"],
                        "digest": value["digest"],
                    }
                    if not all(isinstance(pin[key], str) for key in ("atom_id", "source_path", "digest")):
                        raise ContainerLifecycleFixtureError("current frozen source pin is malformed")
                    if type(pin["version"]) is not int:
                        raise ContainerLifecycleFixtureError("current frozen source pin has invalid version")
                    previous = result.setdefault(atom_id, pin)
                    if previous != pin:
                        raise ContainerLifecycleFixtureError(
                            f"current frozen source pins disagree for Atom: {atom_id}"
                        )
                for child in value.values():
                    collect(child)
            elif isinstance(value, list):
                for child in value:
                    collect(child)

        collect(frozen_manifest())
        self._current_pin_cache = result
        return result

    def _copy_source(self, raw: bytes, atom_id: str, destination: str) -> dict[str, Any]:
        target = self.root / _safe_relative(destination)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
        observed = _metadata_bytes(raw, destination)
        if _digest(raw) != _digest(target.read_bytes()):
            raise ContainerLifecycleFixtureError(f"fixture source copy changed bytes: {destination}")
        if observed["atom_id"] != atom_id:
            raise ContainerLifecycleFixtureError(f"fixture source identity differs for {atom_id}")
        return {"atom_id": observed["atom_id"], "version": observed["version"],
                "source_path": destination, "digest": _digest(raw)}

    def _pin_from_source(self, atom_id: str, preferred: str | None,
                         forced_destination: str | None = None) -> dict[str, Any]:
        current = self._current_pins().get(atom_id)
        expected_digest: str | None = None
        if current is not None:
            source_path = current["source_path"]
            expected_digest = current["digest"]
        elif isinstance(preferred, str) and preferred:
            source_path = preferred
            try:
                frozen_source_bytes(source_path)
            except (AssertionError, OSError):
                candidates = [
                    path for path in frozen_source_paths()
                    if Path(path).name.startswith(f"{atom_id}-")
                ]
                if len(candidates) != 1:
                    raise ContainerLifecycleFixtureError(
                        f"current frozen source for {atom_id} is unavailable or ambiguous"
                    )
                source_path = candidates[0]
        else:
            raise ContainerLifecycleFixtureError(f"frozen route pin has no source path: {atom_id}")
        destination = self._query_source_hints().get(atom_id, source_path)
        try:
            raw = frozen_source_bytes(source_path, expected_digest)
        except (AssertionError, OSError) as error:
            raise ContainerLifecycleFixtureError(f"selected frozen source is unavailable: {source_path}") from error
        observed = _metadata_bytes(raw, destination)
        actual_digest = _digest(raw)
        if observed["atom_id"] != atom_id:
            raise ContainerLifecycleFixtureError(f"source identity differs for {atom_id}")
        self._copy_source(raw, atom_id, destination)
        return {"atom_id": atom_id, "version": observed["version"],
                "source_path": destination, "digest": actual_digest}

    def _materialize_pinned_closure(self) -> None:
        for relative in frozen_selected_root_paths():
            raw = frozen_source_bytes(relative)
            target = self.root / _safe_relative(relative)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)

    def _fresh_definition(self, raw: Mapping[str, Any], forced_destination: str | None = None) -> dict[str, Any]:
        atom_id = raw.get("atom_id")
        if not isinstance(atom_id, str) or not atom_id:
            raise ContainerLifecycleFixtureError("selected definition has no Atom identity")
        return self._pin_from_source(atom_id, raw.get("source_path"), forced_destination)

    @staticmethod
    def _query_paths(document: Mapping[str, Any]) -> dict[tuple[str, str], str]:
        result: dict[tuple[str, str], str] = {}
        for admission in document.get("query_source_admissions", []):
            if not isinstance(admission, Mapping):
                continue
            route = admission.get("route")
            if not isinstance(route, str):
                continue
            values: list[Mapping[str, Any]] = []
            for key in ("acceptance_frontier", "workflow"):
                value = admission.get(key)
                if isinstance(value, Mapping):
                    values.append(value)
            for item in admission.get("ordered_steps", []):
                if isinstance(item, Mapping):
                    values.extend(value for value in (item.get("step"), item.get("action"))
                             if isinstance(value, Mapping))
            values.extend(value for value in admission.get("ordered_actions", []) if isinstance(value, Mapping))
            for value in values:
                if isinstance(value.get("atom_id"), str) and isinstance(value.get("source_path"), str):
                    result[(route, value["atom_id"])] = value["source_path"]
        return result

    @staticmethod
    def _query_source_hints() -> dict[str, str]:
        from selected_routes import _QUERY_SOURCE_ADMISSION_SPECS

        paths = ContainerLifecycleFixture._query_paths(
            {"query_source_admissions": _QUERY_SOURCE_ADMISSION_SPECS}
        )
        return {atom_id: path for (_route, atom_id), path in paths.items()}

    def _fresh_route(self, raw: Mapping[str, Any], query_paths: Mapping[tuple[str, str], str]) -> dict[str, Any]:
        route = deepcopy(dict(raw))
        name = route.get("route")

        def forced(pin: Mapping[str, Any]) -> str | None:
            return query_paths.get((name, pin.get("atom_id"))) if isinstance(name, str) else None

        route["workflow"] = self._fresh_definition(route["workflow"], forced(route["workflow"]))
        route["ordered_steps"] = [
            {"step": self._fresh_definition(item["step"], forced(item["step"])),
             "action": self._fresh_definition(item["action"], forced(item["action"]))}
            for item in route["ordered_steps"]
        ]
        route["ordered_actions"] = [self._fresh_definition(item, forced(item))
                                     for item in route["ordered_actions"]]
        route["native_action_calls"] = [self._fresh_definition(item, forced(item))
                                         for item in route["native_action_calls"]]
        return route

    def _fresh_admission(self, raw: Mapping[str, Any]) -> dict[str, Any]:
        admission = deepcopy(dict(raw))
        admission["acceptance_frontier"] = self._fresh_definition(
            admission["acceptance_frontier"], admission["acceptance_frontier"]["source_path"])
        admission["workflow"] = self._fresh_definition(
            admission["workflow"], admission["workflow"]["source_path"])
        admission["ordered_steps"] = [
            {"step": self._fresh_definition(item["step"], item["step"]["source_path"]),
             "action": self._fresh_definition(item["action"], item["action"]["source_path"])}
            for item in admission["ordered_steps"]
        ]
        admission["ordered_actions"] = [self._fresh_definition(item, item["source_path"])
                                         for item in admission["ordered_actions"]]
        return admission

    def _write_manifest(self) -> None:
        try:
            document = json.loads(ROUTE_SHAPE.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ContainerLifecycleFixtureError("selected route projection is unavailable") from error
        if not isinstance(document, dict) or not isinstance(document.get("routes"), list):
            raise ContainerLifecycleFixtureError("selected route projection has no route list")
        query_paths = self._query_paths(document)
        routes = [self._fresh_route(route, query_paths) for route in document["routes"]]
        admissions = [self._fresh_admission(admission)
                      for admission in document.get("query_source_admissions", [])]
        freshness_source = document.get("source_freshness", {})
        registry_path = freshness_source.get("selected_source_registry_ref")
        if not isinstance(registry_path, str):
            raise ContainerLifecycleFixtureError("selected source registry reference is missing")
        registry = self._pin_from_source("CA-A-1142", registry_path, registry_path)
        freshness = {
            "selected_source_registry_ref": registry["source_path"],
            "selected_source_registry_version": registry["version"],
            "selected_source_registry_digest": registry["digest"],
            "selected_binding_ref": f"{MANIFEST_REF}#/routes",
            "selected_binding_digest": _canonical_digest(routes),
        }
        output: dict[str, Any] = {
            "schema_version": 1,
            "source_freshness": freshness,
            "query_source_admissions": admissions,
            "routes": routes,
        }
        output["canonical_manifest_sha256"] = _canonical_digest(output)
        path = self.manifest_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(output, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n",
                        encoding="utf-8")

    @staticmethod
    def plan_carrier_bytes(atom_id: str, *, status: str = "Active", parent: str | None = None) -> bytes:
        relation = "{}" if parent is None else f"{{is_decomposition_of: [{parent}]}}"
        return (
            "---\n"
            f"atom_id: {atom_id}\ncontent_role: Plan\ntype: Plan\n"
            "current_scope_unit: STATUS_FIXTURE\nclaim_target_scope_unit: STATUS_FIXTURE\n"
            "local_tier: Standard\nglobal_tier: 11\nauthor: Container Fixture\n"
            f"status: {status}\nversion: 1\nupdated_at: 2026-01-01 00:00:00 +0000\n"
            "subjects:\n  governs: Atom/Test\n  depends_on: []\n"
            f"relations: {relation}\n---\n"
            f"# Summary\n\n{atom_id} container fixture.\n\n"
            "## Objective\n\nRetain exact source bindings in the nested lifecycle fixture.\n\n"
            "## Details\n\nNested lifecycle carrier.\n\n"
            "### Definition of Done\n\nThe selected route can preview and freeze one status change.\n"
        ).encode("utf-8")

    def _write_nested_plans(self) -> None:
        if self.scope_rows is None:
            raise ContainerLifecycleFixtureError("scope declarations were not materialized")
        base = Path(self.scope_rows["STATUS_FIXTURE"]["authority_path"]) / "03_plan"
        self.parent_plan = base / "01-CA-P-701-EPIC--parent.md"
        self.child_plan = base / "01-CA-P-701-EPIC--parent/02-CA-P-702-TASK--child.md"
        self.child_plan.parent.mkdir(parents=True, exist_ok=True)
        self.parent_plan.write_bytes(self.plan_carrier_bytes("CA-P-701"))
        self.child_plan.write_bytes(self.plan_carrier_bytes("CA-P-702", parent="CA-P-701"))

    def status_parameters(self, target: Path | None = None) -> dict[str, Any]:
        if self.manifest is None or self.parent_plan is None:
            raise ContainerLifecycleFixtureError("prepare the fixture before making a lifecycle request")
        from lifecycle_intents import carrier_descriptor

        path = self.parent_plan if target is None else target
        return {"target": carrier_descriptor(self.root, str(path)), "status": "Archived"}

    def preview_status(self) -> dict[str, Any]:
        from lifecycle_intents import change_status_atom_action

        return change_status_atom_action(self.root, self.status_parameters(), execute=False, authorized=False)

    def freeze_status(self, run_id: str = "container-lifecycle") -> dict[str, Any]:
        if self.manifest is None:
            raise ContainerLifecycleFixtureError("prepare the fixture before freezing a request")
        from selected_execution import SelectedExecution, build_requested_runs, preflight_selected_lifecycle

        parameters = self.status_parameters()
        execution: dict[str, Any] = {
            "mode": "execute",
            "operation_route": "change_atom_status",
            "request_id": f"{run_id}-request",
            "parameters": parameters,
            "definition_manifest": {"manifest_ref": MANIFEST_REF,
                                    "manifest_digest": self.manifest["canonical_manifest_sha256"]},
            "source_freshness": self.manifest["source_freshness"],
        }
        selected = SelectedExecution(self.root)
        graph = selected._validate_graph(execution)
        execution["requested_runs"] = build_requested_runs(graph, run_id)
        admission = preflight_selected_lifecycle(self.root, "change_atom_status", parameters)
        execution["proposal_receipt"] = {"source_freshness": {"observed": {
            "lifecycle_admission": admission,
        }}}
        return selected.freeze({"operation": "enqueue_selected", "run_id": run_id,
                               "execution": execution})

    def self_check(self) -> dict[str, Any]:
        preview = self.preview_status()
        if preview.get("outcome") != "preview":
            raise ContainerLifecycleFixtureError("lifecycle preview did not remain side-effect free")
        frozen = self.freeze_status()
        if frozen.get("graph", {}).get("route") != "change_atom_status":
            raise ContainerLifecycleFixtureError("frozen graph is not the current lifecycle route")
        if frozen.get("lifecycle_admission", {}).get("requested_status") != "Archived":
            raise ContainerLifecycleFixtureError("frozen lifecycle admission is incomplete")
        return {"root": str(self.root), "route": self.current_route,
                "preview": preview, "frozen": frozen}


@contextmanager
def disposable_container_lifecycle_project() -> Iterator[ContainerLifecycleFixture]:
    """Yield one prepared disposable Project and clean it up on exit."""
    fixture = ContainerLifecycleFixture()
    try:
        yield fixture.prepare()
    finally:
        fixture.close()
