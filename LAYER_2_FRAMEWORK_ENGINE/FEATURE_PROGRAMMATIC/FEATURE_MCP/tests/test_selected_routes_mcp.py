"""Golden contracts for the selected, source-bound MCP route adapter."""

from __future__ import annotations

import copy
import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

MCP = Path(__file__).resolve().parents[1]
ROOT = MCP.parents[2]
ORCHESTRATOR = MCP.parent / "FEATURE_APPS" / "APP_WORKFLOW_ORCHESTRATOR"
TOOLS_TESTS = MCP.parent / "FEATURE_TOOLS" / "tests"
WORKFLOW_TESTS = ORCHESTRATOR / "tests"
TEST_TEMP_ROOT = ROOT / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(MCP))
sys.path.insert(0, str(TOOLS_TESTS))
sys.path.insert(0, str(ORCHESTRATOR))
sys.path.insert(0, str(WORKFLOW_TESTS))

from selected_routes import (  # noqa: E402
    ADMITTED_SELECTED_ROUTE_NAMES,
    ORIGINAL_SELECTED_ROUTE_NAMES,
    QUERY_ROUTE_NAMES,
    SELECTED_ROUTE_NAMES,
    SelectedRouteError,
    SelectedRouteAdapter,
    canonical_digest,
    load_selected_manifest,
    selected_manifest_contract,
    selected_manifest_ref,
)
import test_model_driven_status_lifecycle as status_goldens  # noqa: E402
import selected_routes  # noqa: E402
from frozen_selected_workflows import (  # noqa: E402
    frozen_manifest,
    frozen_source_bytes,
    frozen_selected_root_paths,
    frozen_source_paths,
    frozen_source_root,
)
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from scope_unit_declarations import (  # noqa: E402
    ScopeDeclarationError,
    read_scope_unit_declarations,
)


_FIXTURE_SCOPE_ROWS = (
    {
        "scope_unit_name": "METHODOLOGY_SOURCES",
        "parent": "PROJECT",
        "scope_unit_type": "Unordered",
        "scope_unit_label": "METHODOLOGY",
    },
    {
        "scope_unit_name": "CORE_META_MODEL",
        "parent": "METHODOLOGY_SOURCES",
        "scope_unit_type": "Unordered",
        "scope_unit_label": "METHODOLOGY",
    },
    {
        "scope_unit_name": "INSTALLED_EXTENSIONS",
        "parent": "METHODOLOGY_SOURCES",
        "scope_unit_type": "Unordered",
        "scope_unit_label": "METHODOLOGY",
    },
    {
        "scope_unit_name": "PROJECT_CONFIGURATION",
        "parent": "METHODOLOGY_SOURCES",
        "scope_unit_type": "Unordered",
        "scope_unit_label": "METHODOLOGY",
    },
    {
        "scope_unit_name": "PARENT",
        "parent": "PROJECT",
        "scope_unit_type": "Ordered",
        "scope_unit_label": "LAYER",
        "local_order": 1,
    },
    {
        "scope_unit_name": "CHILD",
        "parent": "PARENT",
        "scope_unit_type": "Unordered",
        "scope_unit_label": "FEATURE",
    },
    {
        "scope_unit_name": "DEST",
        "parent": "PROJECT",
        "scope_unit_type": "Unordered",
        "scope_unit_label": "LAYER",
    },
    {
        "scope_unit_name": "TOOL_WORKFLOWS",
        "parent": "PROJECT",
        "scope_unit_type": "Unordered",
        "scope_unit_label": "FEATURE",
    },
)
_QUERY_CORE_SOURCES = (
    "09_operations/CA-O-158-CORE_META_MODEL-WORKFLOW--find-and-fetch-artifacts.md",
    "09_operations/CA-O-159-CORE_META_MODEL-ACTION--query-and-fetch-artifacts.md",
    "09_operations/CA-O-160-CORE_META_MODEL-STEP--run-the-artifact-query-and-fetch.md",
    "09_operations/CA-O-161-CORE_META_MODEL-WORKFLOW--find-and-fetch-journal-events.md",
    "09_operations/CA-O-162-CORE_META_MODEL-ACTION--query-journal-events.md",
    "09_operations/CA-O-161-CORE_META_MODEL-WORKFLOW--find-and-fetch-journal-events/"
    "CA-O-163-CORE_META_MODEL-STEP--query-the-stable-journal-event-snapshot.md",
)


def _query_definition_pins(entry: dict) -> list[dict]:
    return [
        entry["workflow"],
        *entry["ordered_actions"],
        *[pin for item in entry["ordered_steps"] for pin in item.values()],
        *entry.get("native_action_calls", []),
    ]


def _query_source_locator_hints() -> dict[str, str]:
    """Return the reviewed query consumers' path hints keyed by Atom ID."""
    hints: dict[str, str] = {}
    for entry in selected_routes._QUERY_SOURCE_ADMISSION_SPECS:
        for pin in _query_definition_pins(entry):
            hints[pin["atom_id"]] = pin["source_path"]
    return hints


def _rewrite_query_definition_locators(entry: dict, hints: dict[str, str]) -> None:
    for pin in _query_definition_pins(entry):
        pin["source_path"] = hints[pin["atom_id"]]


def _materialize_query_declaration_authority(root: Path, rows: dict[str, dict]) -> dict[str, str]:
    """Copy selected definition bytes beneath declaration-derived authorities.

    The checked-in selected-route manifest carries consumer path hints from the
    query admission contract.  The files themselves live at the returned
    declaration-derived authority path; the reader resolves each hint to that
    current carrier without changing its frozen bytes or digest.
    """
    legacy_root = Path(
        ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/"
        "CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL"
    )
    core_authority = Path(rows["CORE_META_MODEL"]["authority_path"])
    project_configuration_authority = Path(rows["PROJECT_CONFIGURATION"]["authority_path"])
    query_hints = _query_source_locator_hints()
    manifest = frozen_manifest()
    definitions = [pin for route in manifest["routes"] for pin in _query_definition_pins(route)]
    definitions.extend(
        pin
        for admission in manifest["query_source_admissions"]
        for pin in _query_definition_pins(admission)
    )
    seen: set[str] = set()
    destination_refs: dict[str, str] = {}
    for pin in definitions:
        if pin["atom_id"] in seen:
            continue
        seen.add(pin["atom_id"])
        source_path = Path(pin["source_path"])
        try:
            source_relative = source_path.relative_to(legacy_root)
        except ValueError:
            candidates = [
                Path(path)
                for path in frozen_source_paths()
                if Path(path).name.startswith(f"{pin['atom_id']}-")
            ]
            if len(candidates) != 1:
                raise AssertionError(
                    f"frozen source for {pin['atom_id']} is unavailable or ambiguous"
                )
            source_path = candidates[0]
            source_relative = Path("09_operations") / source_path.name
            destination = Path(rows["TOOL_WORKFLOWS"]["authority_path"]) / source_relative
        else:
            destination = core_authority / source_relative
        if pin["atom_id"] in query_hints:
            try:
                query_relative = Path(query_hints[pin["atom_id"]]).relative_to(legacy_root.parent)
            except ValueError as error:
                raise AssertionError(
                    f"query source for {pin['atom_id']} is outside the declared methodology root"
                ) from error
            destination = project_configuration_authority / Path(*query_relative.parts[1:])
        destination.parent.mkdir(parents=True, exist_ok=True)
        source = root / source_path
        source_bytes = frozen_source_bytes(source_path, pin.get("digest"))
        destination.write_bytes(source_bytes)
        destination_refs[pin["atom_id"]] = destination.relative_to(root).as_posix()
        if source != destination and source.exists():
            source.unlink()
    return destination_refs


def _normalized_existing_scope_rows(root: Path) -> dict[str, dict] | None:  # noqa: C901
    """Return existing derived declaration rows, or None for a fresh Project."""
    control_root = root / ".caprmedio_caprmedio"
    try:
        aggregate = read_scope_unit_declarations(root, control_root)
    except ScopeDeclarationError as error:
        if str(error) != "no current Scope Unit Declarations found":
            raise
        return None
    else:
        rows = {}
        for row in aggregate.as_structure()["scope_units"]:
            name = row.get("scope_unit_name")
            if not isinstance(name, str) or not name:
                raise ScopeDeclarationError("existing Scope Unit Declaration has no name")
            normalized = dict(row)
            for field in ("authority_path", "delivery_path"):
                value = normalized.get(field)
                if not isinstance(value, str) or not value:
                    raise ScopeDeclarationError(
                        f"existing Scope Unit Declaration {name} has no {field}"
                    )
                normalized[field] = root / value
            rows[name] = normalized
    for required in ("CORE_META_MODEL", "PROJECT_CONFIGURATION"):
        if required not in rows:
            raise ScopeDeclarationError(
                f"fixture declarations do not define required Scope Unit: {required}"
            )
    if "TOOL_WORKFLOWS" not in rows and "TOOLS" in rows:
        rows["TOOL_WORKFLOWS"] = dict(rows["TOOLS"])
    return rows


def _fixture_scope_rows(root: Path) -> dict[str, dict]:
    """Use an existing valid declaration aggregate before creating fresh rows."""
    existing = _normalized_existing_scope_rows(root)
    return (
        existing
        if existing is not None
        else write_scope_unit_declarations(root, _FIXTURE_SCOPE_ROWS)
    )


def _materialize_existing_manifest_support(root: Path) -> None:
    """Copy the frozen support closure without reviving superseded D276."""
    for relative in frozen_selected_root_paths():
        path = Path(relative)
        if path.name.startswith("CA-D-276-"):
            continue
        raw = frozen_source_bytes(path)
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)


def frozen_project(root: Path) -> Path:
    """Materialize the checked-in selected-route authority, never live Atoms."""
    root = root.resolve()
    settings = root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
    if not settings.exists():
        settings.parent.mkdir(parents=True, exist_ok=True)
        settings.write_text(
            '[project]\nkey = "golden-fixture"\nname = "caprmedio"\nrepository_slug = "golden-fixture"\n'
            '[artifacts.identity]\nproject_prefix = "CA"\n\n[paths]\n'
            'control_root = ".caprmedio_caprmedio"\njournal_root = ".caprmedio_caprmedio/_journal"\n',
            encoding="utf-8",
        )
    existing_rows = _normalized_existing_scope_rows(root)
    if existing_rows is None:
        frozen_source_root(root)
        rows = write_scope_unit_declarations(root, _FIXTURE_SCOPE_ROWS)
    else:
        rows = existing_rows
        _materialize_existing_manifest_support(root)
    query_hints = _query_source_locator_hints()
    definition_refs = _materialize_query_declaration_authority(root, rows)
    manifest = frozen_manifest()
    for admission in manifest["query_source_admissions"]:
        _rewrite_query_definition_locators(admission, query_hints)
    for route in manifest["routes"]:
        if route["route"] in QUERY_ROUTE_NAMES:
            _rewrite_query_definition_locators(route, query_hints)
        else:
            _rewrite_query_definition_locators(route, definition_refs)
    manifest["source_freshness"]["selected_binding_digest"] = canonical_digest(manifest["routes"])
    manifest["canonical_manifest_sha256"] = canonical_digest(
        {key: value for key, value in manifest.items() if key != "canonical_manifest_sha256"}
    )
    manifest_path = root / selected_manifest_ref(root)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    return root


class FakeRunSupport:
    """Records adapter calls without executing a Workflow, Action, or effect."""

    def __init__(self) -> None:
        self.calls: list[dict] = []

    def run_selected_operation(self, request: dict) -> dict:
        self.calls.append(copy.deepcopy(request))
        if request["mode"] == "preview":
            receipt = {
                "request_id": request["request_id"],
                "definition_manifest": request["definition_manifest"],
            }
            return {
                "request_id": request["request_id"],
                "disposition": "preview",
                "outcome": "prepared",
                "proposal_receipt": receipt,
                "proposal_receipt_digest": canonical_digest(receipt),
                "source_freshness": copy.deepcopy(request["source_freshness"]),
            }
        return {
            "request_id": request["request_id"],
            "disposition": "started",
            "outcome": "started",
            "workflow_run_id": "run:fixture",
            "action_run_ids": ["action:fixture"],
            "event_refs": ["event:fixture"],
            "report_ref": "report:fixture",
            "source_freshness": copy.deepcopy(request["source_freshness"]),
        }

    def get_selected_workflow_run(self, request: dict) -> dict:
        return {
            "run_id": request["run_id"],
            "status": "recording_pending",
            "event_refs": ["event:pending"],
        }

    def get_selected_action_run(self, request: dict) -> dict:
        return {
            "action_run_id": request["action_run_id"],
            "status": "completed",
            "lineage": {"workflow_run_id": "run:fixture"},
        }


class SelectedManifestRefResolverTest(unittest.TestCase):
    def test_manifest_ref_uses_the_configured_control_root_projection(self) -> None:
        with tempfile.TemporaryDirectory(
            dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True
        ) as temporary:
            project = Path(temporary)
            self.assertEqual(
                ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
                selected_manifest_ref(project),
            )

            settings = project / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
            settings.parent.mkdir()
            settings.write_text(
                '[paths]\ncontrol_root = ".caprmedio_fixture"\njournal_root = ".caprmedio_fixture/_journal"\n',
                encoding="utf-8",
            )
            self.assertEqual(
                ".caprmedio_fixture/_projection/selected_workflow_bindings.json",
                selected_manifest_ref(project),
            )


class QueryAdmissionPhysicalProofTest(unittest.TestCase):
    """Reopen the two proofs without depending on the unrepaired portfolio."""

    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(temporary.cleanup)
        self.root = frozen_project(Path(temporary.name))
        self.admissions = list(selected_routes._query_admission_specs(self.root))
        manifest = frozen_manifest()
        self.routes = [
            copy.deepcopy(route)
            for route in manifest["routes"]
            if route["route"] in QUERY_ROUTE_NAMES
        ]
        for admission, route in zip(self.admissions, self.routes, strict=True):
            for field in ("workflow", "ordered_steps", "ordered_actions"):
                route[field] = copy.deepcopy(admission[field])

    def test_query_source_admissions_and_read_only_routes_validate(self) -> None:
        self.assertEqual(
            self.admissions,
            selected_routes._validate_query_source_admissions(
                self.root, self.admissions, self.routes
            ),
        )
        for route in self.routes:
            self.assertFalse(route["mutation_capable"])
            selected_routes._validate_route(self.root, route)

    def test_missing_third_reordered_or_shadow_proofs_reject(self) -> None:
        for mutation in (
            "missing",
            "third",
            "reordered",
            "shadow",
            "route-mismatch",
            "invalid-digest",
        ):
            with self.subTest(mutation=mutation):
                admissions, routes = copy.deepcopy(self.admissions), copy.deepcopy(self.routes)
                if mutation == "missing":
                    admissions.pop()
                elif mutation == "third":
                    admissions.append(copy.deepcopy(admissions[0]))
                elif mutation == "reordered":
                    admissions.reverse()
                elif mutation == "shadow":
                    admissions[1]["structural_successor_bridge"] = {"accepted": True}
                elif mutation == "route-mismatch":
                    routes[1]["workflow"] = copy.deepcopy(routes[0]["workflow"])
                else:
                    admissions[0]["workflow"]["digest"] = "invalid"
                with self.assertRaises(SelectedRouteError):
                    selected_routes._validate_query_source_admissions(self.root, admissions, routes)

    def test_current_revisions_resolve_but_substituted_proof_identity_rejects(self) -> None:
        for mutation in (
            "old-proof",
            "predecessor",
            "superseded-step",
            "newer-step",
            "changed-body",
        ):
            with self.subTest(mutation=mutation):
                admissions = copy.deepcopy(self.admissions)
                pin = (
                    admissions[0]["acceptance_frontier"]
                    if mutation == "old-proof"
                    else admissions[1]["ordered_steps"][0]["step"]
                )
                path = self.root / pin["source_path"]
                original_contents = path.read_bytes()
                if mutation in {"predecessor", "superseded-step"}:
                    version = 2 if mutation == "predecessor" else 3
                    contents = original_contents.replace(
                        f"version: {pin['version']}".encode(), f"version: {version}".encode(), 1
                    )
                    pin["version"] = version
                else:
                    contents = original_contents
                    if mutation == "old-proof":
                        contents = contents.replace(b"CA-P-1618", b"CA-P-1532").replace(
                            b"version: 1", b"version: 2"
                        )
                        pin.update(atom_id="CA-P-1532", version=2)
                    elif mutation == "newer-step":
                        prior_version = pin["version"]
                        contents = contents.replace(
                            f"version: {prior_version}".encode(),
                            f"version: {prior_version + 1}".encode(),
                            1,
                        )
                        pin["version"] = prior_version + 1
                    else:
                        contents += b"\nUnadmitted changed query body.\n"
                pin["digest"] = hashlib.sha256(contents).hexdigest()
                path.write_bytes(contents)
                try:
                    self.assertEqual(pin, selected_routes._validate_pin(self.root, pin))
                    if mutation == "old-proof":
                        with self.assertRaises(SelectedRouteError):
                            selected_routes._validate_query_source_admissions(
                                self.root, admissions, self.routes
                            )
                    else:
                        routes = copy.deepcopy(self.routes)
                        for route in routes:
                            for item in route["ordered_steps"]:
                                if item["step"]["atom_id"] == pin["atom_id"]:
                                    item["step"] = pin
                        selected_routes._validate_query_source_admissions(
                            self.root, admissions, routes
                        )
                finally:
                    path.write_bytes(original_contents)

    def test_query_only_manifest_still_rejects_before_shared_support(self) -> None:
        manifest = frozen_manifest()
        registry_ref = manifest["source_freshness"]["selected_source_registry_ref"]
        self.assertTrue((self.root / registry_ref).is_file())
        manifest["routes"], manifest["query_source_admissions"] = self.routes, self.admissions
        manifest["source_freshness"]["selected_binding_digest"] = canonical_digest(self.routes)
        manifest["canonical_manifest_sha256"] = canonical_digest(
            {key: value for key, value in manifest.items() if key != "canonical_manifest_sha256"}
        )
        path = self.root / selected_manifest_ref(self.root)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(manifest))
        support = FakeRunSupport()
        adapter = SelectedRouteAdapter(self.root, service=support, strict_manifest=False)
        result = adapter.invoke(QUERY_ROUTE_NAMES[0], {"request_id": "query-only"})
        self.assertEqual("rejected", result["disposition"])
        self.assertIn(
            "must contain eleven routes or twelve with move_atom", result["diagnostics"][0]
        )
        self.assertEqual([], support.calls)


def copy_complete_selected_guard_fixture(project: Path) -> dict:
    """Frozen eleven-route fixture; not a route-count repair receipt."""
    tools = MCP.parent / "FEATURE_TOOLS"
    sys.path.insert(0, str(tools / "VALIDATE_ATOMS"))
    from validate_atoms_workers.parsing import parse_carrier

    project = frozen_project(project)
    manifest = load_selected_manifest(project)
    assert tuple(row["route"] for row in manifest["routes"]) == SELECTED_ROUTE_NAMES
    query_hints = _query_source_locator_hints()
    for admission in manifest["query_source_admissions"]:
        _rewrite_query_definition_locators(admission, query_hints)
    query = {row["route"]: row for row in manifest["query_source_admissions"]}

    def current_pin(pin):
        # Fixture inputs are the exact selected paths, not a whole Project catalog.
        path = selected_routes._safe_path(project, pin["source_path"])
        raw = path.read_bytes()
        metadata = parse_carrier(raw, path).metadata
        assert metadata.get("atom_id") == pin["atom_id"], "fixture source identity differs"
        assert str(metadata.get("status", "")).lower() == "active", "fixture source is not Active"
        version = metadata.get("version")
        assert type(version) is int and version > 0, "fixture source version is invalid"
        return {
            "atom_id": pin["atom_id"],
            "version": version,
            "source_path": pin["source_path"],
            "digest": hashlib.sha256(raw).hexdigest(),
        }

    for route in manifest["routes"]:
        if route["route"] in query:
            for field in ("workflow", "ordered_steps", "ordered_actions"):
                route[field] = copy.deepcopy(query[route["route"]][field])
            _rewrite_query_definition_locators(route, query_hints)
        else:
            route["workflow"] = current_pin(route["workflow"])
            route["ordered_steps"] = [
                {key: current_pin(pin) for key, pin in row.items()}
                for row in route["ordered_steps"]
            ]
            route["ordered_actions"] = [current_pin(pin) for pin in route["ordered_actions"]]
        route["native_action_calls"] = [current_pin(pin) for pin in route["native_action_calls"]]
    freshness = manifest["source_freshness"]
    registry = current_pin(
        {"atom_id": "CA-A-1142", "source_path": freshness["selected_source_registry_ref"]}
    )
    freshness["selected_source_registry_ref"] = registry["source_path"]
    freshness["selected_source_registry_digest"] = registry["digest"]
    freshness["selected_binding_digest"] = canonical_digest(manifest["routes"])
    manifest.pop("manifest_ref", None)
    manifest["canonical_manifest_sha256"] = canonical_digest(
        {key: value for key, value in manifest.items() if key != "canonical_manifest_sha256"}
    )
    path = project / selected_manifest_ref(project)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest))
    return load_selected_manifest(project)


class _GuardServer:
    def __init__(self):
        self.tools = {}

    def tool(self, *, name, **metadata):
        def register(function):
            self.tools[name] = function
            return function

        return register


class WholeRegistryGuardTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.manifest = copy_complete_selected_guard_fixture(self.root)
        self.support = FakeRunSupport()

    def snapshot(self):
        return {
            path.relative_to(self.root).as_posix(): path.read_bytes()
            for path in self.root.rglob("*")
            if path.is_file()
        }

    def request(self, route):
        parameters, frontier, effects = {}, ["target:fixture"], []
        return {
            "operation_route": route,
            "request_id": "guard-request",
            "parameters": parameters,
            "parameters_digest": canonical_digest(parameters),
            "target_frontier": frontier,
            "target_frontier_digest": canonical_digest(frontier),
            "effects": effects,
            "effects_digest": canonical_digest(effects),
            "source_freshness": self.manifest["source_freshness"],
            "definition_manifest": {
                "manifest_ref": self.manifest["manifest_ref"],
                "manifest_digest": self.manifest["canonical_manifest_sha256"],
            },
            "initiative": {"initiative_id": "fixture", "instruction_summary": "guard"},
        }

    def corrupt_unselected_route(self, *, malformed=False):
        path = self.root / self.manifest["manifest_ref"]
        document = json.loads(path.read_text())
        self.assertNotEqual("create_atom", document["routes"][1]["route"])
        if malformed:
            document["routes"][1]["unknown_route_field"] = True
        else:
            pin = document["routes"][1]["workflow"]
            source = self.root / pin["source_path"]
            source.write_bytes(source.read_bytes().replace(pin["atom_id"].encode(), b"CA-O-999999"))
        document["source_freshness"]["selected_binding_digest"] = canonical_digest(
            document["routes"]
        )
        document["canonical_manifest_sha256"] = canonical_digest(
            {key: value for key, value in document.items() if key != "canonical_manifest_sha256"}
        )
        path.write_text(json.dumps(document))

    def test_complete_physical_fixture_registers_code_selected_routes_and_previews(self):
        before = self.snapshot()
        server = _GuardServer()
        adapter = selected_routes.register_selected_routes(server, self.root)
        self.assertEqual(
            frozenset((*ADMITTED_SELECTED_ROUTE_NAMES, "release_version", "public.release")),
            adapter.public_route_names,
        )
        self.assertEqual(
            set(ADMITTED_SELECTED_ROUTE_NAMES)
            | {
                "release_version",
                "public.release",
                "get_selected_workflow_run",
                "get_selected_action_run",
            },
            set(server.tools),
        )
        self.assertNotIn("recover_selected_run_recording", server.tools)
        self.assertFalse(hasattr(adapter, "recover_recording"))
        self.assertFalse(
            hasattr(selected_routes._QueueBackedSelectedSupport, "recover_selected_run_recording")
        )
        self.assertIn("release_version", server.tools)
        self.assertIn("public.release", server.tools)
        adapter.service = self.support
        result = server.tools["create_atom"](self.request("create_atom"))
        self.assertEqual("preview", result["disposition"])
        self.assertEqual(1, len(self.support.calls))
        self.assertEqual(
            "run:fixture",
            server.tools["get_selected_workflow_run"]({"run_id": "run:fixture"})["run_id"],
        )
        self.assertEqual(
            "action:fixture",
            server.tools["get_selected_action_run"]({"action_run_id": "action:fixture"})[
                "action_run_id"
            ],
        )
        self.assertEqual(1, len(self.support.calls))
        self.assertEqual(before, self.snapshot())

    def test_unselected_source_drift_keeps_code_selected_routes_exposed(self):
        self.corrupt_unselected_route()
        server = _GuardServer()
        sentinel = object()
        server.tools["existing_helper"] = sentinel
        before = self.snapshot()
        selected_routes.register_selected_routes(server, self.root)
        self.assertEqual(
            {
                "existing_helper",
                *ADMITTED_SELECTED_ROUTE_NAMES,
                "release_version",
                "public.release",
                "get_selected_workflow_run",
                "get_selected_action_run",
            },
            set(server.tools),
        )
        self.assertIs(sentinel, server.tools["existing_helper"])
        self.assertEqual(before, self.snapshot())

    def test_empty_generated_route_inventory_registers_only_control_tools(self):
        server = _GuardServer()
        adapter = selected_routes.register_selected_routes(server, self.root, route_names=())

        self.assertEqual(
            frozenset({"release_version", "public.release"}), adapter.public_route_names
        )
        self.assertEqual(
            {
                "release_version",
                "public.release",
                "get_selected_workflow_run",
                "get_selected_action_run",
            },
            set(server.tools),
        )

    def test_unselected_route_drift_blocks_invocation_before_shared_support(self):
        adapter = SelectedRouteAdapter(self.root, service=self.support)
        self.corrupt_unselected_route()
        before = self.snapshot()
        result = adapter.invoke("create_atom", self.request("create_atom"))
        self.assertEqual("rejected", result["disposition"])
        self.assertIn("current definition is unavailable or invalid", result["diagnostics"][0])
        self.assertEqual([], self.support.calls)
        self.assertEqual(before, self.snapshot())

    def test_direct_release_refuses_selected_envelope_without_virtual_manifest(self):
        adapter = SelectedRouteAdapter(self.root, service=self.support)
        self.corrupt_unselected_route()
        before = self.snapshot()
        self.assertFalse(hasattr(selected_routes, "load_release_execution_manifest"))
        result = adapter.invoke("release_version", self.request("release_version"))
        self.assertEqual("failed", result["outcome"])
        self.assertIn("only project_root and run_id", result["diagnostics"][0])
        self.assertEqual([], self.support.calls)
        self.assertEqual(before, self.snapshot())

    def test_malformed_unselected_route_keeps_registration_and_blocks_invocation(self):
        adapter = SelectedRouteAdapter(self.root, service=self.support)
        self.corrupt_unselected_route(malformed=True)
        server = _GuardServer()
        before = self.snapshot()
        selected_routes.register_selected_routes(server, self.root)
        result = adapter.invoke("create_atom", self.request("create_atom"))
        self.assertEqual("rejected", result["disposition"])
        self.assertIn("incomplete or unknown schema", result["diagnostics"][0])
        self.assertEqual(
            set(ADMITTED_SELECTED_ROUTE_NAMES)
            | {
                "release_version",
                "public.release",
                "get_selected_workflow_run",
                "get_selected_action_run",
            },
            set(server.tools),
        )
        self.assertEqual([], self.support.calls)
        self.assertEqual(before, self.snapshot())


class SelectedRoutesMCPTest(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(temporary.cleanup)
        self.frozen_root = frozen_project(Path(temporary.name))
        self.manifest = load_selected_manifest(self.frozen_root)
        self.status_fixture = status_goldens.ModelDrivenStatusLifecycleTest()
        self.status_fixture.setUp()
        self.addCleanup(self.status_fixture.tearDown)
        status_model = self.status_fixture.sources["CA-R-1309"]
        declared_status_model = (
            self.status_fixture.source / status_model.parent.name / status_model.name
        )
        declared_status_model.parent.mkdir(parents=True, exist_ok=True)
        declared_status_model.write_bytes(status_model.read_bytes())
        self.status_fixture.sources["CA-R-1309"] = declared_status_model
        self.status_target = self.status_fixture.atom("Requirement", "Active")
        self.support = FakeRunSupport()
        self.loader = patch("selected_routes.load_selected_manifest", return_value=self.manifest)
        self.loader.start()
        self.addCleanup(self.loader.stop)
        # Status preflight must inspect a real disposable Atom and its copied
        # source-bound model/Structure authority.  Other selected routes still
        # use the same manifest snapshot and fake shared support.
        self.adapter = SelectedRouteAdapter(self.status_fixture.root, service=self.support)

    def request(self, route: str, *, mode: str = "preview") -> dict:
        if route == "change_atom_status":
            parameters = self.status_fixture.request(self.status_target, "Archived")
            refs = [parameters["target"]["path"]]
        else:
            parameters = {"route_input": route}
            refs = ["target:fixture"]
        effects = []
        request = {
            "operation_route": route,
            "mode": mode,
            "request_id": f"request-{route}",
            "parameters": parameters,
            "parameters_digest": canonical_digest(parameters),
            "target_frontier": refs,
            "target_frontier_digest": canonical_digest(refs),
            "effects": effects,
            "effects_digest": canonical_digest(effects),
            "definition_manifest": {
                "manifest_ref": self.manifest["manifest_ref"],
                "manifest_digest": self.manifest["canonical_manifest_sha256"],
            },
            "source_freshness": copy.deepcopy(self.manifest["source_freshness"]),
            "initiative": {
                "initiative_id": "initiative:fixture",
                "instruction_summary": "fixture",
                "initiative_ref": "initiative:fixture",
            },
        }
        if mode == "execute":
            receipt = {
                "request_id": request["request_id"],
                "definition_manifest": request["definition_manifest"],
            }
            receipt_digest = canonical_digest(receipt)
            request.update(
                {
                    "proposal_receipt": receipt,
                    "proposal_receipt_digest": receipt_digest,
                    "assigned_action_id": "operator:fixture",
                    "requested_runs": [
                        {
                            "requested_run_id": "requested:workflow",
                            "kind": "workflow",
                            "definition": self._definition(route, "workflow"),
                        },
                        {
                            "requested_run_id": "requested:action",
                            "kind": "action",
                            "definition": self._definition(route, "action"),
                            "parent_requested_run_id": "requested:workflow",
                        },
                    ],
                    "operator_authorization": {
                        "authorization_ref": "authorization:fixture",
                        "authorization_freshness": {"state": "current", "digest": "b" * 64},
                        "request_id": request["request_id"],
                        "operation_route": route,
                        "proposal_receipt_digest": receipt_digest,
                        "parameters_digest": request["parameters_digest"],
                        "target_frontier_digest": request["target_frontier_digest"],
                        "effects_digest": request["effects_digest"],
                        "definition_manifest": copy.deepcopy(request["definition_manifest"]),
                        "source_freshness": copy.deepcopy(request["source_freshness"]),
                    },
                }
            )
        return request

    def _definition(self, route: str, kind: str) -> dict:
        entry = next(item for item in self.manifest["routes"] if item["route"] == route)
        pin = entry["workflow"] if kind == "workflow" else entry["ordered_actions"][0]
        return {
            "atom_id": pin["atom_id"],
            "version": pin["version"],
            "path": pin["source_path"],
            "digest": pin["digest"],
        }

    @staticmethod
    def _queue_requested_runs(graph: dict, run_id: str) -> list[dict]:
        sys.path.insert(0, str(ORCHESTRATOR))
        from selected_execution import SelectedExecution

        return SelectedExecution.build_requested_runs(graph, run_id)

    def _copy_status_bindings(self, project: Path) -> dict:
        """Copy the real disposable Atom, model sources, and Project Structure."""
        for source in self.status_fixture.sources.values():
            relative = source.relative_to(self.status_fixture.root)
            destination = project / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
        target = self.status_target.relative_to(self.status_fixture.root)
        target_destination = project / target
        target_destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(self.status_target, target_destination)
        return self.status_fixture.request(self.status_target, "Archived")

    def test_current_physical_manifest_freezes_the_generic_routes_through_queue_consumer(
        self,
    ) -> None:
        """The MCP source fixture must be sufficient for the independent queue.

        This copies only the immutable manifest and its pinned sources into a
        disposable Project, then uses the queue consumer's real ``freeze``
        boundary. No Action handler or DBOS worker is invoked.
        """
        sys.path.insert(0, str(ORCHESTRATOR))
        from selected_execution import SelectedExecution  # noqa: PLC0415

        with tempfile.TemporaryDirectory(
            dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True
        ) as temporary:
            project = Path(temporary)
            (project / ".git").mkdir()
            control = project / ".caprmedio_caprmedio"
            control.mkdir()
            (control / "caprmedio_project_settings.toml").write_text(
                '[project]\nname = "caprmedio"\n\n'
                '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
                'journal_root = ".caprmedio_caprmedio/_journal"\n',
                encoding="utf-8",
            )
            status_parameters = self._copy_status_bindings(project)
            frozen_project(project)

            queue = SelectedExecution(project, handlers={})
            generic_routes = [
                route
                for route in self.manifest["routes"]
                if route["route"] in ORIGINAL_SELECTED_ROUTE_NAMES
                and route["route"] != "run_implementation_workflow"
            ]
            self.assertEqual(8, len(generic_routes))
            for ordinal, route in enumerate(generic_routes, start=1):
                run_id = f"freeze{ordinal:02d}"
                parameters = (
                    copy.deepcopy(status_parameters)
                    if route["route"] == "change_atom_status"
                    else {}
                )
                target_frontier = (
                    [parameters["target"]["path"]]
                    if route["route"] == "change_atom_status"
                    else ["fixture/input"]
                )
                execution = {
                    "mode": "execute",
                    "request_id": f"request-{run_id}",
                    "operation_route": route["route"],
                    "parameters": parameters,
                    "target_frontier": target_frontier,
                    "effects": [],
                    "definition_manifest": {
                        "manifest_ref": self.manifest["manifest_ref"],
                        "manifest_digest": self.manifest["canonical_manifest_sha256"],
                    },
                    "source_freshness": copy.deepcopy(self.manifest["source_freshness"]),
                    "initiative": {"initiative_id": "fixture", "instruction_summary": "freeze"},
                }
                if route["route"] == "change_atom_status":
                    preview = SelectedRouteAdapter(project).invoke(
                        route["route"],
                        self.request(route["route"]),
                    )
                    self.assertEqual("preview", preview["disposition"], preview)
                    execution["proposal_receipt"] = preview["proposal_receipt"]
                    execution["proposal_receipt_digest"] = preview["proposal_receipt_digest"]
                graph = queue._validate_graph(execution)
                execution["requested_runs"] = self._queue_requested_runs(graph, run_id)
                frozen = queue.freeze(
                    {"operation": "enqueue_selected", "run_id": run_id, "execution": execution}
                )
                self.assertEqual(route["route"], frozen["graph"]["route"])
                self.assertEqual(graph["entry_step"], frozen["graph"]["entry_step"])

    def test_manifest_is_closed_eleven_ordinary_routes(self) -> None:
        contract = selected_manifest_contract(self.frozen_root)
        self.assertEqual(self.manifest["manifest_ref"], contract["manifest_ref"])
        self.assertEqual(list(SELECTED_ROUTE_NAMES), contract["route_names"])
        self.assertTrue(contract["canonical_digest"]["self_field_omitted_from_digest"])
        self.assertEqual(
            ["route", "acceptance_frontier", "workflow", "ordered_steps", "ordered_actions"],
            contract["query_source_admission_fields"],
        )
        self.assertEqual(["from", "condition", "to"], contract["on_result_fields"])
        self.assertEqual("complete", contract["on_result_terminal_target"])
        route_names = [entry["route"] for entry in self.manifest["routes"]]
        self.assertEqual(list(SELECTED_ROUTE_NAMES), route_names)
        self.assertEqual(
            self.manifest["canonical_manifest_sha256"],
            canonical_digest(
                {
                    key: value
                    for key, value in self.manifest.items()
                    if key not in {"canonical_manifest_sha256", "manifest_ref"}
                }
            ),
        )
        for entry in self.manifest["routes"]:
            self.assertTrue(entry["entry_step"])
            self.assertTrue(entry["ordered_steps"])
            self.assertEqual(
                [item["action"]["atom_id"] for item in entry["ordered_steps"]],
                [item["atom_id"] for item in entry["ordered_actions"]],
            )
            steps = {item["step"]["atom_id"] for item in entry["ordered_steps"]}
            self.assertIn(entry["entry_step"], steps)
            for edge in entry["on_result"]:
                self.assertIn(edge["from"], steps)
                self.assertTrue(edge["to"] == "complete" or edge["to"] in steps)
            for pin in [
                entry["workflow"],
                *[item["step"] for item in entry["ordered_steps"]],
                *entry["ordered_actions"],
                *entry["native_action_calls"],
            ]:
                self.assertEqual(64, len(pin["digest"]))

        routes = {entry["route"]: entry for entry in self.manifest["routes"]}
        self.assertNotIn("release_version", routes)
        self.assertNotIn("public.release", routes)
        self.assertNotIn("release_source_admissions", self.manifest)
        self.assertNotIn("public_release_source_admissions", self.manifest)
        admissions = self.manifest["query_source_admissions"]
        self.assertEqual(list(QUERY_ROUTE_NAMES), [entry["route"] for entry in admissions])
        for admission in admissions:
            route = routes[admission["route"]]
            self.assertFalse(route["mutation_capable"])
            for field in ("workflow", "ordered_steps", "ordered_actions"):
                self.assertEqual(admission[field], route[field])
        for route in ("create_atom", "replace_atom", "change_atom_status"):
            self.assertEqual([], routes[route]["on_result"])

    def test_manifest_rejects_missing_or_third_query_source_admission(self) -> None:
        """The two accepted frontier records are closed manifest evidence."""
        with tempfile.TemporaryDirectory(
            dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True
        ) as temporary:
            project = Path(temporary)
            (project / ".git").mkdir()
            frozen_project(project)

            old_frontier = {
                "atom_id": "CA-P-1532",
                "version": 2,
                "source_path": ".caprmedio_caprmedio/fixtures/malformed-artifact-frontier.md",
                "digest": "",
            }
            old_receipt = project / old_frontier["source_path"]
            old_receipt.parent.mkdir(parents=True, exist_ok=True)
            malformed_frontier = (
                b"---\n"
                b"atom_id: CA-P-1532\n"
                b"version: 2\n"
                b"---\n"
                b"malformed disposable query-frontier fixture\n"
            )
            old_receipt.write_bytes(malformed_frontier)
            old_frontier["digest"] = hashlib.sha256(malformed_frontier).hexdigest()

            for mutation in ("missing", "third", "old-artifact-frontier"):
                with self.subTest(mutation=mutation):
                    candidate = {
                        key: copy.deepcopy(value)
                        for key, value in self.manifest.items()
                        if key not in {"manifest_ref", "canonical_manifest_sha256"}
                    }
                    if mutation == "missing":
                        candidate["query_source_admissions"] = candidate["query_source_admissions"][
                            :1
                        ]
                    elif mutation == "third":
                        candidate["query_source_admissions"].append(
                            copy.deepcopy(candidate["query_source_admissions"][0])
                        )
                    else:
                        admission = candidate["query_source_admissions"][0]
                        admission["acceptance_frontier"] = old_frontier
                        self.assertEqual("CA-O-158", admission["workflow"]["atom_id"])
                        self.assertEqual(candidate["routes"][9]["workflow"], admission["workflow"])
                    query_hints = _query_source_locator_hints()
                    for route in candidate["routes"]:
                        if route["route"] in QUERY_ROUTE_NAMES:
                            _rewrite_query_definition_locators(route, query_hints)
                    for admission in candidate["query_source_admissions"]:
                        _rewrite_query_definition_locators(admission, query_hints)
                    candidate["source_freshness"]["selected_binding_digest"] = canonical_digest(
                        candidate["routes"]
                    )
                    candidate["canonical_manifest_sha256"] = canonical_digest(candidate)
                    (project / self.manifest["manifest_ref"]).write_text(
                        __import__("json").dumps(candidate),
                        encoding="utf-8",
                    )
                    expected = (
                        "current definition is unavailable or invalid"
                        if mutation == "old-artifact-frontier"
                        else "exactly two routes"
                    )
                    with self.assertRaisesRegex(SelectedRouteError, expected):
                        load_selected_manifest(project)

    def test_every_selected_route_forwards_one_mutation_free_preview(self) -> None:
        for route in SELECTED_ROUTE_NAMES:
            result = self.adapter.invoke(route, self.request(route))
            if route == "run_implementation_workflow":
                self.assertEqual("retired", result["outcome"])
                continue
            self.assertEqual("prepared", result["outcome"])
            self.assertEqual(route, self.support.calls[-1]["operation_route"])
            self.assertEqual("preview", self.support.calls[-1]["mode"])
        self.assertEqual(10, len(self.support.calls))

    def test_default_adapter_uses_shared_preview_support_without_an_executor(self) -> None:
        result = SelectedRouteAdapter(self.frozen_root).invoke(
            "create_atom", self.request("create_atom")
        )
        self.assertEqual("preview", result["disposition"])
        self.assertIn("proposal_receipt", result)
        self.assertNotIn("run_ids", result)

    def test_execute_forwards_exact_request_once_and_observations_do_not_dispatch(self) -> None:
        route = "create_atom"
        request = self.request(route, mode="execute")
        result = self.adapter.invoke(route, request)
        self.assertEqual("started", result["outcome"])
        self.assertEqual(request, self.support.calls[-1])
        before = len(self.support.calls)
        self.assertEqual(
            "recording_pending", self.adapter.get_workflow_run({"run_id": "run:fixture"})["status"]
        )
        self.assertEqual(
            "completed", self.adapter.get_action_run({"action_run_id": "action:fixture"})["status"]
        )
        self.assertEqual(before, len(self.support.calls))

    def test_execute_accepts_manifest_in_the_shared_supports_real_preview_receipt(self) -> None:
        route = "create_atom"
        preview = SelectedRouteAdapter(self.frozen_root).invoke(route, self.request(route))
        self.assertEqual("preview", preview["disposition"])
        request = self.request(route, mode="execute")
        request["proposal_receipt"] = preview["proposal_receipt"]
        request["proposal_receipt_digest"] = preview["proposal_receipt_digest"]
        request["operator_authorization"]["proposal_receipt_digest"] = preview[
            "proposal_receipt_digest"
        ]

        result = self.adapter.invoke(route, request)

        self.assertEqual("started", result["outcome"], result)
        self.assertEqual([request], self.support.calls)

    def test_receipt_exception_does_not_allow_nested_shadow_manifest_wrappers(self) -> None:
        cases = []
        for wrapper in ("proposal_receipt", "operator_authorization"):
            request = self.request("create_atom", mode="execute")
            request["parameters"] = {
                wrapper: {"definition_manifest": request["definition_manifest"]}
            }
            request["parameters_digest"] = canonical_digest(request["parameters"])
            request["operator_authorization"]["parameters_digest"] = request["parameters_digest"]
            cases.append(request)
        request = self.request("create_atom", mode="execute")
        request["proposal_receipt"] = {
            "unexpected": {"definition_manifest": request["definition_manifest"]}
        }
        cases.append(request)

        for request in cases:
            with self.subTest(request=request):
                self.assertEqual(
                    "rejected", self.adapter.invoke("create_atom", request)["disposition"]
                )
        self.assertEqual([], self.support.calls)

    def test_execute_rejects_non_object_empty_or_digest_mismatched_receipts(self) -> None:
        for receipt in ("proposal:fixture", {}, {"request_id": "changed"}):
            with self.subTest(receipt=receipt):
                request = self.request("create_atom", mode="execute")
                request["proposal_receipt"] = receipt
                result = self.adapter.invoke("create_atom", request)
                self.assertEqual("blocked", result["disposition"])
        self.assertEqual([], self.support.calls)

    def test_stale_manifest_and_matching_or_different_shadow_manifest_fields_reject_before_support(
        self,
    ) -> None:
        cases = []
        altered = self.request("create_atom")
        altered["definition_manifest"]["manifest_digest"] = "b" * 64
        cases.append(altered)
        stale_ref = self.request("create_atom")
        stale_ref["definition_manifest"]["manifest_ref"] = (
            "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/selected_workflow_bindings.json"
        )
        cases.append(stale_ref)
        for value in (self.manifest["canonical_manifest_sha256"], "c" * 64):
            shadow = self.request("create_atom")
            shadow["source_freshness"]["definition_manifest_digest"] = value
            cases.append(shadow)
        stale = self.request("create_atom")
        stale["source_freshness"]["selected_binding_digest"] = "d" * 64
        cases.append(stale)
        for request in cases:
            result = self.adapter.invoke("create_atom", request)
            self.assertEqual("rejected", result["disposition"])
        self.assertEqual([], self.support.calls)

    def test_apply_unknown_route_and_bad_lineage_are_strict(self) -> None:
        apply = self.request("create_atom", mode="apply")
        self.assertEqual("rejected", self.adapter.invoke("create_atom", apply)["disposition"])
        malformed = self.request("create_atom")
        malformed["lineage"] = {"parent_workflow_run_id": "not-a-real-lineage", "unexpected": True}
        self.assertEqual("rejected", self.adapter.invoke("create_atom", malformed)["disposition"])


if __name__ == "__main__":
    unittest.main()
