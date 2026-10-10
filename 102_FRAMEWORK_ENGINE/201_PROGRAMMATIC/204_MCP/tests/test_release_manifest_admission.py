"""Preparatory canonical loader proof, not Release registration or execution."""
from __future__ import annotations

import copy
from contextlib import contextmanager
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch


MCP = Path(__file__).resolve().parents[1]
REPOSITORY = MCP.parents[2]
APP_TESTS = MCP.parent / "203_APPS/WORKFLOW_ORCHESTRATOR/tests"
PUBLIC_RELEASE = MCP.parent / "201_TOOLS/PUBLIC_RELEASE"
for location in (PUBLIC_RELEASE, MCP, MCP / "tests", APP_TESTS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import test_release_source_admission as source_goldens  # noqa: E402
import selected_admission as public_admission  # noqa: E402
import selected_routes as routes_module  # noqa: E402
from selected_routes import (  # noqa: E402
    SELECTED_ROUTE_NAMES, SelectedRouteAdapter, SelectedRouteError, canonical_digest,
    load_selected_manifest, selected_manifest_contract,
)


class _NeverSupport:
    def __init__(self) -> None:
        self.calls = 0

    def run_selected_operation(self, request: dict) -> dict:
        self.calls += 1
        raise AssertionError("refused input reached shared support")


class ReleaseManifestAdmissionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        source_goldens.ReleaseSourceAdmissionTest.setUpClass()

    def setUp(self) -> None:
        # The checkout's D572 private-carrier rows may lag simultaneous
        # RELEASE_VERSION edits.  Freeze their copied bytes under a test-local
        # D572 pin; production D572 and its production pin are never changed.
        self.fixture = self._resealed_d572_fixture()
        self.root = self.fixture.root
        self.base, self.path = self._resealed_fifteen_route_manifest()
        self.record = copy.deepcopy(self.fixture.record)
        self.release = copy.deepcopy(self.fixture.route)

    def _rewrite_fixture_d572_authority(self, text: str, root: Path) -> str:
        """Rebind every closed D572 pin to the copied fixture byte surface."""
        def source_bytes(relative: str) -> bytes:
            path = root / relative
            self.assertTrue(path.is_file() and not path.is_symlink(), relative)
            return path.read_bytes()

        def digest(relative: str) -> str:
            return hashlib.sha256(source_bytes(relative)).hexdigest()

        def identity(relative: str) -> tuple[str, int]:
            contents = source_bytes(relative).decode("utf-8")
            atom_id = routes_module._frontmatter_value(contents, "atom_id")
            version = routes_module._frontmatter_value(contents, "version")
            self.assertIsNotNone(atom_id, relative)
            self.assertIsNotNone(version, relative)
            assert atom_id is not None and version is not None
            return atom_id, int(version)

        def rewrite_json_block(value: str, heading: str, digest_key: str) -> str:
            pattern = re.compile(
                rf"^(## {re.escape(heading)}\n+```json\n)(.*?)(\n```)$", re.MULTILINE | re.DOTALL,
            )
            matches = list(pattern.finditer(value))
            self.assertEqual(1, len(matches), f"fixture D572 {heading} block is unavailable")
            match = matches[0]
            rows = json.loads(match[2])
            self.assertIsInstance(rows, list)
            assert isinstance(rows, list)
            for row in rows:
                self.assertIsInstance(row, dict)
                assert isinstance(row, dict)
                relative = row.get("source_path")
                self.assertIsInstance(relative, str)
                assert isinstance(relative, str)
                row[digest_key] = digest(relative)
                if "atom_id" in row or "version" in row:
                    row["atom_id"], row["version"] = identity(relative)
            return value[:match.start()] + match[1] + json.dumps(rows, indent=2) + match[3] + value[match.end():]

        text = rewrite_json_block(text, "Private implementation carriers", "sha256")
        text = rewrite_json_block(text, "Unknown-effect resolver authority", "digest")

        def frontier(match: re.Match[str]) -> str:
            atom_id, version = identity(match.group("path"))
            return f"{atom_id}@{version} at `{match.group('path')}`, SHA-256 `{digest(match.group('path'))}`"

        def table(match: re.Match[str]) -> str:
            atom_id, version = identity(match.group("path"))
            return f"| {atom_id} | {version} | `{match.group('path')}` | `{digest(match.group('path'))}` |"

        def occurrence(match: re.Match[str]) -> str:
            atom_id, version = identity(match.group("path"))
            return f"{atom_id}@{version} `{match.group('path')}` `{digest(match.group('path'))}`"

        text = re.sub(
            r"CA-P-[0-9]+@[1-9][0-9]* at `(?P<path>[^`\n]+)`, SHA-256 `[0-9a-f]{64}`",
            frontier, text,
        )
        text = re.sub(
            r"^\| CA-[A-Z]+-[0-9]+ \| [1-9][0-9]* \| `(?P<path>[^`\n]+)` \| `[0-9a-f]{64}` \|$",
            table, text, flags=re.MULTILINE,
        )
        return re.sub(
            r"CA-O-[0-9]+@[1-9][0-9]* `(?P<path>[^`\n]+)` `[0-9a-f]{64}`",
            occurrence, text,
        )

    def _resealed_d572_fixture(self):
        fixture = source_goldens.ReleaseSourceAdmissionTest()
        temporary_root = REPOSITORY / ".caprmedio_tmp/tests/release-manifest-admission"
        temporary_root.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=temporary_root, ignore_cleanup_errors=True)
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        record = copy.deepcopy(source_goldens.ReleaseSourceAdmissionTest.expected)
        private_carriers = copy.deepcopy(source_goldens.ReleaseSourceAdmissionTest.private_carriers)
        authority_source = REPOSITORY / source_goldens.AUTHORITY_REF
        authority_text = authority_source.read_text(encoding="utf-8")
        resolver_match = re.search(
            r"^## Unknown-effect resolver authority\n+```json\n(.*?)\n```$", authority_text,
            re.MULTILINE | re.DOTALL,
        )
        self.assertIsNotNone(resolver_match, "fixture D572 resolver block is unavailable")
        assert resolver_match is not None
        resolver_rows = json.loads(resolver_match[1])
        self.assertIsInstance(resolver_rows, list)
        assert isinstance(resolver_rows, list)
        for relative in {source_goldens.AUTHORITY_REF, *[pin["source_path"] for pin in source_goldens.all_pins(record)],
                         *[row["source_path"] for row in private_carriers],
                         *[row["source_path"] for row in resolver_rows]}:
            source = REPOSITORY / relative
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)

        authority = root / source_goldens.AUTHORITY_REF
        original = authority.read_text(encoding="utf-8")
        rewritten = self._rewrite_fixture_d572_authority(original, root)
        authority.write_text(rewritten, encoding="utf-8", newline="")
        local_pin = {
            **source_goldens.admission_module.AUTHORITY_PIN,
            "digest": hashlib.sha256(rewritten.encode("utf-8")).hexdigest(),
        }
        authority_patch = patch.object(source_goldens.admission_module, "AUTHORITY_PIN", local_pin)
        authority_patch.start()
        self.addCleanup(authority_patch.stop)
        fixture.root = root
        fixture.record = source_goldens.derive_release_source_admission(root)
        fixture.private_carriers = source_goldens.admission_module._private_carriers(rewritten)
        fixture.graph = source_goldens.derive_release_route_graph(root)
        fixture.route = {"route": "release_version", **copy.deepcopy(fixture.graph)}
        return fixture

    def _resealed_fifteen_route_manifest(self) -> tuple[dict, Path]:
        """Copy the fixed fifteen-route baseline with current fixture-only pins."""
        manifest_ref = routes_module.selected_manifest_ref(self.root)
        production = json.loads((REPOSITORY / manifest_ref).read_text(encoding="utf-8"))
        routes = production.get("routes")
        self.assertIsInstance(routes, list)
        assert isinstance(routes, list)
        self.assertEqual(list(SELECTED_ROUTE_NAMES), [row.get("route") for row in routes[:len(SELECTED_ROUTE_NAMES)]])
        manifest = copy.deepcopy(production)
        manifest["routes"] = manifest["routes"][:len(SELECTED_ROUTE_NAMES)]
        manifest.pop("release_source_admissions", None)
        manifest.pop("public_release_source_admissions", None)

        def copy_and_reseal(value) -> None:
            if isinstance(value, dict):
                relative = value.get("source_path")
                digest = value.get("digest")
                if isinstance(relative, str) and isinstance(digest, str):
                    source = REPOSITORY / relative
                    target = self.root / relative
                    self.assertTrue(source.is_file() and not source.is_symlink(), relative)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(source, target)
                    contents = target.read_bytes()
                    value["digest"] = hashlib.sha256(contents).hexdigest()
                    if "atom_id" in value or "version" in value:
                        text = contents.decode("utf-8")
                        atom_id = routes_module._frontmatter_value(text, "atom_id")
                        version = routes_module._frontmatter_value(text, "version")
                        self.assertIsNotNone(atom_id, relative)
                        self.assertIsNotNone(version, relative)
                        assert atom_id is not None and version is not None
                        value["atom_id"] = atom_id
                        value["version"] = int(version)
                for child in value.values():
                    copy_and_reseal(child)
            elif isinstance(value, list):
                for child in value:
                    copy_and_reseal(child)

        copy_and_reseal(manifest["routes"])
        copy_and_reseal(manifest["query_source_admissions"])
        freshness = manifest["source_freshness"]
        self.assertIsInstance(freshness, dict)
        assert isinstance(freshness, dict)
        registry = freshness.get("selected_source_registry_ref")
        self.assertIsInstance(registry, str)
        assert isinstance(registry, str)
        registry_source = REPOSITORY / registry
        registry_target = self.root / registry
        registry_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(registry_source, registry_target)
        freshness["selected_source_registry_digest"] = hashlib.sha256(registry_target.read_bytes()).hexdigest()
        freshness["selected_binding_digest"] = canonical_digest(manifest["routes"])
        unsigned = {key: value for key, value in manifest.items() if key != "canonical_manifest_sha256"}
        manifest["canonical_manifest_sha256"] = canonical_digest(unsigned)
        path = self.root / manifest_ref
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(manifest, separators=(",", ":")), encoding="utf-8")
        return manifest, path

    def successor(self) -> dict:
        return {**copy.deepcopy(self.base), "routes": [*copy.deepcopy(self.base["routes"]), copy.deepcopy(self.release)],
                "release_source_admissions": [copy.deepcopy(self.record)]}

    def _copy_public_release_sources(self) -> None:
        """Copy D613 and its exact source rows into the isolated Project."""
        authority = REPOSITORY / public_admission.AUTHORITY_REF
        authority_target = self.root / public_admission.AUTHORITY_REF
        authority_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(authority, authority_target)
        tables = public_admission._tables(authority.read_text(encoding="utf-8"))
        acceptance, _ = public_admission._single_pin(tables[0], acceptance=True)
        workflow, _ = public_admission._single_pin(tables[1])
        steps, actions = public_admission._paired_pins(tables[2])
        rmed = public_admission._rmed_pins(tables[3])
        pins = [acceptance, workflow, *steps, *actions,
                *(pin for collection in ("requirements", "methods", "evaluations", "deliveries")
                  for pin in rmed[collection])]
        for relative in {pin["source_path"] for pin in pins}:
            source = REPOSITORY / relative
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)

    @contextmanager
    def _locally_completed_d613(self):
        """Trust only a copied D613/CA-P-1869 pair for the positive fixture."""
        authority = self.root / public_admission.AUTHORITY_REF
        tables = public_admission._tables(authority.read_text(encoding="utf-8"))
        acceptance, _ = public_admission._single_pin(tables[0], acceptance=True)
        plan = self.root / acceptance["source_path"]
        original_authority, original_plan = authority.read_bytes(), plan.read_bytes()
        try:
            completed_plan, count = re.subn(
                rb"(?m)^status:\s*Active\s*$", b"status: Done", original_plan,
            )
            self.assertEqual(1, count, "the fixture must begin with D613's actually Active CA-P-1869")
            plan.write_bytes(completed_plan)
            completed_digest = hashlib.sha256(completed_plan).hexdigest().encode("ascii")
            updated_authority = original_authority.replace(
                acceptance["digest"].encode("ascii"), completed_digest, 1,
            )
            self.assertNotEqual(original_authority, updated_authority)
            authority.write_bytes(updated_authority)
            local_authority_pin = {
                **public_admission.AUTHORITY_PIN,
                "digest": hashlib.sha256(updated_authority).hexdigest(),
            }
            with patch.object(public_admission, "AUTHORITY_PIN", local_authority_pin):
                yield
        finally:
            plan.write_bytes(original_plan)
            authority.write_bytes(original_authority)

    @staticmethod
    def _public_route(record: dict) -> dict:
        steps = copy.deepcopy(record["ordered_steps"])
        actions = copy.deepcopy(record["ordered_actions"])
        conditions = (
            "a unique existing matching PR or no matching PR is evidenced",
            "material source proof is complete and any existing link is actual",
            "full gate is typed, current, passed, and sealed for that source proof",
            "immutable push proof and one actual open PR URL are evidenced",
            "unchanged history closure, or a changed history closure with renewed gate, follow-up push, and refreshed same PR",
        )
        return {
            "route": "public.release", "workflow": copy.deepcopy(record["workflow"]),
            "ordered_steps": [
                {"step": step, "action": action}
                for step, action in zip(steps, actions, strict=True)
            ],
            "ordered_actions": actions, "native_action_calls": [],
            "entry_step": steps[0]["atom_id"],
            "on_result": [
                {"from": step["atom_id"], "condition": conditions[index],
                 "to": steps[index + 1]["atom_id"] if index + 1 < len(steps) else "complete"}
                for index, step in enumerate(steps)
            ],
            "mutation_capable": True,
        }

    def public_successor(self, record: dict) -> dict:
        manifest = self.successor()
        manifest["routes"].append(self._public_route(record))
        manifest["public_release_source_admissions"] = [copy.deepcopy(record)]
        return manifest

    def save(self, manifest: dict, *, rehash: bool = True) -> None:
        if rehash:
            manifest["source_freshness"]["selected_binding_digest"] = canonical_digest(manifest["routes"])
            unsigned = {key: value for key, value in manifest.items() if key != "canonical_manifest_sha256"}
            manifest["canonical_manifest_sha256"] = canonical_digest(unsigned)
        self.path.write_text(json.dumps(manifest, separators=(",", ":")), encoding="utf-8")

    def refusal(self, manifest: dict) -> None:
        self.save(manifest)
        before = self.fixture.snapshot()
        support = _NeverSupport()
        with self.assertRaises(SelectedRouteError):
            SelectedRouteAdapter(self.root, service=support)
        self.assertEqual(0, support.calls)
        self.assertEqual(before, self.fixture.snapshot())

    def test_actual_fifteen_route_compatibility_is_byte_preserving_and_not_advertised_as_sixteen(self) -> None:
        before = self.fixture.snapshot()
        loaded = load_selected_manifest(self.root)
        self.assertEqual(list(SELECTED_ROUTE_NAMES), [row["route"] for row in loaded["routes"]])
        self.assertEqual(15, len(SELECTED_ROUTE_NAMES))
        self.assertEqual(list(SELECTED_ROUTE_NAMES), selected_manifest_contract(self.root)["route_names"])
        self.assertNotIn("release_source_admissions", loaded)
        self.assertEqual(self.base["source_freshness"], loaded["source_freshness"])
        self.assertEqual(self.base["query_source_admissions"], loaded["query_source_admissions"])
        self.assertEqual(self.base, json.loads(self.path.read_text(encoding="utf-8")))
        self.assertEqual(before, self.fixture.snapshot())

    def test_actual_source_bound_successor_sixteen_loads_without_changing_first_fifteen_or_registration(self) -> None:
        manifest = self.successor()
        self.save(manifest)
        before = self.fixture.snapshot()
        loaded = load_selected_manifest(self.root)
        self.assertEqual([*SELECTED_ROUTE_NAMES, "release_version"], [row["route"] for row in loaded["routes"]])
        self.assertEqual(self.base["routes"], loaded["routes"][:-1])
        self.assertEqual([self.record], loaded["release_source_admissions"])
        self.assertEqual(self.base["query_source_admissions"], loaded["query_source_admissions"])
        self.assertEqual(15, len(SELECTED_ROUTE_NAMES), "a preparatory loader must not advertise/register Release")
        self.assertEqual(before, self.fixture.snapshot())

    def test_locally_completed_d613_admits_the_ordered_seventeenth_public_route(self) -> None:
        self._copy_public_release_sources()
        with self._locally_completed_d613():
            record = public_admission.derive_public_release_source_admission(self.root)
            manifest = self.public_successor(record)
            self.save(manifest)
            before = self.fixture.snapshot()
            loaded = load_selected_manifest(self.root)
            adapter = SelectedRouteAdapter(self.root, service=_NeverSupport())
            self.assertEqual(before, self.fixture.snapshot())
        self.assertEqual(
            [*SELECTED_ROUTE_NAMES, "release_version", "public.release"],
            [row["route"] for row in loaded["routes"]],
        )
        self.assertEqual(self.base["routes"], loaded["routes"][:len(SELECTED_ROUTE_NAMES)])
        self.assertEqual([record], loaded["public_release_source_admissions"])
        self.assertIn("public.release", adapter.routes)

    def test_active_d613_acceptance_refuses_the_seventeenth_public_route_before_support(self) -> None:
        self._copy_public_release_sources()
        with self._locally_completed_d613():
            record = public_admission.derive_public_release_source_admission(self.root)
        self.refusal(self.public_successor(record))

    def test_rehashed_public_transition_graph_alteration_refuses_before_support(self) -> None:
        self._copy_public_release_sources()
        with self._locally_completed_d613():
            record = public_admission.derive_public_release_source_admission(self.root)
            manifest = self.public_successor(record)
            manifest["routes"][-1]["on_result"][0]["condition"] = "complete"
            self.refusal(manifest)

    def test_public_release_source_admission_is_present_only_for_the_seventeenth_route(self) -> None:
        self._copy_public_release_sources()
        with self._locally_completed_d613():
            record = public_admission.derive_public_release_source_admission(self.root)
            absent = self.public_successor(record)
            absent.pop("public_release_source_admissions")
            self.refusal(absent)
        unexpected = self.successor()
        unexpected["public_release_source_admissions"] = [record]
        self.refusal(unexpected)

    def test_missing_extra_unknown_or_out_of_order_release_evidence_refuses_before_support(self) -> None:
        manifest = self.successor()
        manifest.pop("release_source_admissions")
        self.refusal(manifest)
        for value in ([], None, [self.record, self.record], [{**self.record, "caller_approval": True}]):
            self.refusal({**self.successor(), "release_source_admissions": value})
        self.refusal({**copy.deepcopy(self.base), "release_source_admissions": []})
        for field in ("ordered_steps", "ordered_actions", "rmed_frontier"):
            manifest = self.successor()
            manifest["release_source_admissions"][0][field].reverse()
            self.refusal(manifest)
        manifest = self.successor()
        manifest["release_source_admissions"][0]["rmed_frontier"].pop()
        self.refusal(manifest)
        for field in ("mutation_capable", "native_action_calls"):
            manifest = self.successor()
            manifest["release_source_admissions"][0].pop(field)
            self.refusal(manifest)
        for field, values in (("mutation_capable", (None, 0, False)),
                              ("native_action_calls", (None, 0, False, ["CA-O-165"]))):
            for value in values:
                manifest = self.successor()
                manifest["release_source_admissions"][0][field] = value
                self.refusal(manifest)

    def test_registry_order_unknown_route_and_existing_query_guards_remain_closed(self) -> None:
        manifest = self.successor()
        manifest["routes"][0], manifest["routes"][1] = manifest["routes"][1], manifest["routes"][0]
        self.refusal(manifest)
        manifest = self.successor()
        manifest["routes"][-1]["route"] = "release_unlisted"
        self.refusal(manifest)
        manifest = self.successor()
        manifest["routes"].append(copy.deepcopy(self.release))
        self.refusal(manifest)
        manifest = self.successor()
        manifest["query_source_admissions"].pop()
        self.refusal(manifest)
        manifest = self.successor()
        manifest["source_freshness"]["selected_source_registry_version"] = 3
        self.refusal(manifest)

    def test_rehashed_structurally_valid_release_graph_alterations_refuse_before_support(self) -> None:
        mutations = (
            ("entry_step", lambda route: route.__setitem__("entry_step", "CA-O-171")),
            ("transition", lambda route: route["on_result"][0].__setitem__("to", "CA-O-172")),
            ("native-call", lambda route: route.__setitem__(
                "native_action_calls", [copy.deepcopy(route["ordered_actions"][0])])),
            ("capability", lambda route: route.__setitem__("mutation_capable", False)),
        )
        for name, mutate in mutations:
            with self.subTest(name=name):
                manifest = self.successor()
                mutate(manifest["routes"][-1])
                self.refusal(manifest)

    def test_self_digest_binding_digest_and_stale_actual_rmed_are_rejected(self) -> None:
        manifest = self.successor()
        self.save(manifest)
        manifest["canonical_manifest_sha256"] = "f" * 64
        self.save(manifest, rehash=False)
        with self.assertRaisesRegex(SelectedRouteError, "canonical digest differs"):
            load_selected_manifest(self.root)
        manifest = self.successor()
        self.save(manifest)
        manifest["source_freshness"]["selected_binding_digest"] = "f" * 64
        unsigned = {key: value for key, value in manifest.items() if key != "canonical_manifest_sha256"}
        manifest["canonical_manifest_sha256"] = canonical_digest(unsigned)
        self.save(manifest, rehash=False)
        with self.assertRaisesRegex(SelectedRouteError, "binding digest differs"):
            load_selected_manifest(self.root)
        pin = self.record["rmed_frontier"][-1]
        source = self.root / pin["source_path"]
        source.write_bytes(source.read_bytes() + b"\nDeliberately stale D574.\n")
        self.refusal(self.successor())

    def test_raw_duplicate_members_reject_before_json_collapse_at_every_depth(self) -> None:
        self.save(self.successor())
        text = self.path.read_text()
        mutations = (text.replace('"schema_version":1', '"schema_version":1,"schema_version":1', 1),
                     text.replace('"route":"release_version"', '"route":"release_version","route":"release_version"', 1),
                     text.replace('"atom_id":"CA-O-164"', '"atom_id":"CA-O-164","atom_id":"CA-O-164"', 1))
        for raw in mutations:
            self.assertNotEqual(text, raw)
            self.path.write_text(raw)
            before = self.fixture.snapshot()
            with self.assertRaisesRegex(SelectedRouteError, "duplicate JSON"):
                load_selected_manifest(self.root)
            self.assertEqual(before, self.fixture.snapshot())

    def test_release_evidence_cannot_enter_d527_request_or_its_two_field_manifest(self) -> None:
        support = _NeverSupport()
        adapter = SelectedRouteAdapter(self.root, service=support)
        parameters, refs, effects = {}, ["fixture/target"], []
        request = {"operation_route": "create_scope_unit", "mode": "preview", "request_id": "release-field-refusal",
                   "parameters": parameters, "parameters_digest": canonical_digest(parameters),
                   "target_frontier": refs, "target_frontier_digest": canonical_digest(refs),
                   "effects": effects, "effects_digest": canonical_digest(effects),
                   "definition_manifest": {"manifest_ref": self.path.relative_to(self.root).as_posix(),
                                           "manifest_digest": self.base["canonical_manifest_sha256"]},
                   "source_freshness": copy.deepcopy(self.base["source_freshness"]),
                   "initiative": {"initiative_id": "fixture", "instruction_summary": "refusal fixture"}}
        for location in ("outer", "definition_manifest"):
            forged = copy.deepcopy(request)
            target = forged if location == "outer" else forged["definition_manifest"]
            target["release_source_admissions"] = [self.record]
            result = adapter.invoke("create_scope_unit", forged)
            self.assertEqual("rejected", result["disposition"], result)
            self.assertEqual(0, support.calls)


if __name__ == "__main__":
    unittest.main()
