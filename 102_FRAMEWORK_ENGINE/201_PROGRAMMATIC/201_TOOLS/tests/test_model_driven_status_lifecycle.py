"""Real-source golden native effects; not MCP, queue or immutable-image proof."""
from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
REPOSITORY = TOOLS.parents[2]
APP_TESTS = TOOLS.parent / "203_APPS/WORKFLOW_ORCHESTRATOR/tests"
CONTROL = Path(".caprmedio_caprmedio")
SOURCE = CONTROL / "101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES"
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(APP_TESTS))
sys.path.insert(0, str(TOOLS / "VALIDATE_ATOMS/tests"))

from atom_operations import atom_from_path, frontmatter_scalar, ToolError  # noqa: E402
from authoritative_status_models import resolve_status_model, StatusModelError  # noqa: E402
import lifecycle_intents  # noqa: E402
from golden_authority import frozen_authority_fixture_bytes  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.check_sections import ROLE_SECTIONS  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.support_authority import support_sources  # noqa: E402
from frozen_selected_workflows import (  # noqa: E402
    frozen_complete_carrier_authority,
    frozen_graph_authority,
    frozen_source_root,
)
from lifecycle_intents import (  # noqa: E402
    carrier_descriptor,
    change_status_atom_action,
    create_atom_action,
    LifecycleError,
    preflight_atom_lifecycle,
)


DOMAINS = (
    ("Requirement", "R", "04_requirement", "CA-R-1309", ("Draft", "Active", "Archived")),
    ("Method", "M", "05_method", "CA-R-1397", ("Draft", "Active", "Archived")),
    ("Evaluation", "E", "06_evaluation", "CA-R-1398", ("Draft", "Active", "Archived")),
    ("Delivery", "D", "07_delivery", "CA-R-1399", ("Draft", "Active", "Archived")),
    ("Plan", "P", "03_plan", "CA-R-1539", ("Active", "Backlog", "Done", "Canceled", "Archived")),
    ("Concern", "C", "01_concern", "CA-R-1608", ("draft", "active", "resolved", "canceled")),
    ("Operations", "O", "09_operations", "CA-R-1874", ("Draft", "Active", "Archived")),
    ("Analysis", "A", "02_analysis", "CA-R-1875", ("Draft", "Done", "Archived")),
)
AUTHORITY_IDS = tuple(row[3] for row in DOMAINS) + (
    "CA-R-1308", "CA-R-1521", "CA-R-1312", "CA-R-1311", "CA-R-1419",
    "CA-D-461", "CA-D-466", "CA-D-565", "CA-D-289", "CA-D-434",
    "CA-D-446", "CA-D-288", "CA-D-483", "CA-D-324",
)
FRONTIER_IDS = ("CA-D-434", "CA-D-467", "CA-D-460", "CA-D-481")


class ModelDrivenStatusLifecycleTest(unittest.TestCase):
    """Only fresh disposable Projects are writable by these native invocations."""

    def setUp(self) -> None:
        temporary_root = REPOSITORY / ".caprmedio_tmp/tests/model-driven-status-lifecycle"
        temporary_root.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temporary_root, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        self.input_root = frozen_source_root(self.root / "_frozen_authority")
        frozen_by_id: dict[str, Path] = {}
        for path in self.input_root.rglob("*.md"):
            match = re.search(r"(?m)^atom_id:\s*[\"']?([^\s\"']+)", path.read_text(encoding="utf-8"))
            if match:
                existing = frozen_by_id.setdefault(match[1], path)
                self.assertEqual(
                    hashlib.sha256(existing.read_bytes()).hexdigest(),
                    hashlib.sha256(path.read_bytes()).hexdigest(),
                    f"frozen authority aliases diverge: {match[1]}",
                )
        missing = set((*AUTHORITY_IDS, *FRONTIER_IDS)) - set(frozen_by_id)
        if missing:
            raise AssertionError(f"frozen authority is incomplete: {missing}")
        control = self.root / CONTROL
        control.mkdir()
        for entry in {**frozen_complete_carrier_authority(), **frozen_graph_authority()}.values():
            source = self.input_root / entry["source_path"]
            destination = self.root / entry["source_path"]
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
            self.assertEqual(entry["sha256"], hashlib.sha256(destination.read_bytes()).hexdigest())
        r793_entry = support_sources()["CA-R-793"]
        r793_path = self.root / r793_entry["source_path"]
        r793_path.parent.mkdir(parents=True, exist_ok=True)
        r793_path.write_bytes(frozen_authority_fixture_bytes("CA-R-793"))
        self.assertEqual(r793_entry["sha256"], hashlib.sha256(r793_path.read_bytes()).hexdigest())
        (control / "caprmedio_project_settings.toml").write_text(
            '[project]\nkey = "status-fixture"\nname = "caprmedio"\nrepository_slug = "status-fixture"\n'
            '[artifacts.identity]\nproject_prefix = "CA"\n'
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
            'journal_root = ".caprmedio_caprmedio/_journal"\n', encoding="utf-8",
        )
        (control / "operators_registry.toml").write_text(
            '[[operators]]\nname = "Anatoly Maslennikov"\n'
            'role = "project owner"\njournal_author = "anatoly-m-maslennikov"\n',
            encoding="utf-8",
        )
        (control / "project_structure.toml").write_text(
            'schema_version = 1\n\n'
            '[[scope_units]]\nscope_unit_name = "METHODOLOGY_SOURCES"\n'
            'parent = "PROJECT"\nscope_unit_type = "Unordered"\n'
            'scope_unit_label = "METHODOLOGY"\nstructural_level = 1\n'
            'navigational_order_number = 0\n'
            f'authority_path = "{SOURCE.as_posix()}"\n'
            'delivery_path = "101_FRAMEWORK_METHODOLOGY/sources"\n\n'
            '[[scope_units]]\nscope_unit_name = "CORE_META_MODEL"\n'
            'parent = "METHODOLOGY_SOURCES"\nscope_unit_type = "Unordered"\n'
            'scope_unit_label = "METHODOLOGY"\nstructural_level = 2\n'
            'navigational_order_number = 0\n'
            f'authority_path = "{(SOURCE / "001_CORE_META_MODEL").as_posix()}"\n'
            'delivery_path = "101_FRAMEWORK_METHODOLOGY/sources/001_CORE_META_MODEL"\n\n'
            '[[scope_units]]\nscope_unit_name = "PROJECT_CONFIGURATION"\n'
            'parent = "METHODOLOGY_SOURCES"\nscope_unit_type = "Ordered"\n'
            'scope_unit_label = "LAYER"\nstructural_level = 2\nlocal_order = 3\n'
            'navigational_order_number = 3\n'
            f'authority_path = "{(SOURCE / "003_PROJECT_CONFIGURATION").as_posix()}"\n'
            'delivery_path = "101_FRAMEWORK_METHODOLOGY/sources/003_PROJECT_CONFIGURATION"\n'
            'authority_mode = "strict"\n\n'
            '[[scope_units]]\nscope_unit_name = "STATUS_FIXTURE"\n'
            'parent = "PROJECT"\nscope_unit_type = "Unordered"\n'
            'scope_unit_label = "FIXTURE"\nstructural_level = 1\n'
            'navigational_order_number = 1\n'
            'authority_path = ".caprmedio_caprmedio/fixture"\n'
            'delivery_path = ".caprmedio_caprmedio/fixture"\n', encoding="utf-8",
        )
        self.sources: dict[str, Path] = {}
        for atom_id in (*AUTHORITY_IDS, *FRONTIER_IDS):
            source = frozen_by_id[atom_id]
            relative = source.relative_to(self.input_root)
            legacy_source = CONTROL / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources"
            if relative.is_relative_to(legacy_source):
                relative = SOURCE / relative.relative_to(legacy_source)
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
            self.assertEqual(source.read_bytes(), destination.read_bytes())
            self.sources[atom_id] = destination

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def snapshot(self) -> dict[str, str | None]:
        return {path.relative_to(self.root).as_posix():
                hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
                for path in self.root.rglob("*")}

    def atom(self, role: str, status: str, *, number: int = 8000,
             atom_type: str | None = None, container: str | None = None,
             relations: str = "relations: {}", draft: bool = False) -> Path:
        row = next(row for row in DOMAINS if row[0] == role)
        _, letter, directory, _, _ = row
        folder = self.root / CONTROL / "fixture" / directory
        if container:
            folder /= container
        if status in {"Draft", "draft"}:
            folder /= "draft"
        elif role == "Plan" and status == "Backlog":
            folder /= "001_backlog"
        elif status.casefold() != "active":
            folder /= status.lower()
        folder.mkdir(parents=True, exist_ok=True)
        name = f"CA-{letter}--golden.md" if draft else f"CA-{letter}-{number}--golden.md"
        path = folder / name
        identity = "" if draft else f"atom_id: CA-{letter}-{number}\n"
        atom_type = atom_type or {"Concern": "Problem", "Analysis": "Analysis Report", "Plan": "Plan",
                                  "Evaluation": "QA Case", "Operations": "Action"}.get(role)
        type_value = f"type: {atom_type}\n" if atom_type else ""
        sections = (*ROLE_SECTIONS[role],) if "Details" in ROLE_SECTIONS[role] else (*ROLE_SECTIONS[role], "Details")
        body = "# Summary\n\nGolden immutable meaning\n\n" + "".join(
            f"## {section}\n\n" + ("The whole body must survive the status transition." if section == "Details"
                                     else "Golden immutable meaning") + "\n\n" for section in sections)
        if role == "Plan":
            body += "### Definition of Done\n\nEach admitted Status transition preserves this Plan's Summary and supporting Details.\n"
        path.write_text(
            f"---\n{identity}content_role: {role}\n{type_value}status: {status}\n"
            "current_scope_unit: STATUS_FIXTURE\nclaim_target_scope_unit: STATUS_FIXTURE\n"
            "local_tier: Standard\nglobal_tier: 11\nauthor: Anatoly Maslennikov\n"
            "version: 3\nupdated_at: 2026-01-01 00:00:00 +0000\n"
            "subjects:\n  governs: Atom/Test\n  depends_on: []\n"
            f"{relations}\n---\n{body}",
            encoding="utf-8",
        )
        return path

    def create_carrier(self, role: str, status: str, *, number: int) -> dict[str, str]:
        """Build one complete, source-model-qualified carrier for native Create."""
        _role, letter, directory, _source_id, statuses = next(row for row in DOMAINS if row[0] == role)
        if status not in statuses:
            raise AssertionError(f"fixture status is not admitted: {role}/{status}")
        draft = status.casefold() == "draft"
        folder = self.root / CONTROL / "fixture" / directory
        if draft:
            folder /= "draft"
        elif role == "Plan" and status == "Backlog":
            folder /= "001_backlog"
        elif status.casefold() != "active":
            folder /= status.casefold()
        atom_id = None if draft else f"CA-{letter}-{number}"
        filename = f"CA-{letter}--created-{number}.md" if draft else f"{atom_id}--created-{number}.md"
        if status == "Archived":
            filename = filename.removesuffix(".md") + "@1.md"
        atom_type = {"Concern": "Problem", "Analysis": "Analysis Report", "Plan": "Plan",
                     "Evaluation": "QA Case", "Operations": "Action"}.get(role)
        type_value = f"type: {atom_type}\n" if atom_type else ""
        sections = (*ROLE_SECTIONS[role],) if "Details" in ROLE_SECTIONS[role] else (*ROLE_SECTIONS[role], "Details")
        body = "# Summary\n\nCreated fixture carrier\n\n" + "".join(
            f"## {section}\n\nCreated fixture value.\n\n" for section in sections
        )
        if role == "Plan":
            body += "### Definition of Done\n\nFixture completion condition.\n"
        identity = f"atom_id: {atom_id}\n" if atom_id is not None else ""
        return {
            "path": (folder / filename).relative_to(self.root).as_posix(),
            "frontmatter": (
                f"{identity}content_role: {role}\n{type_value}status: {status}\n"
                "current_scope_unit: STATUS_FIXTURE\nclaim_target_scope_unit: STATUS_FIXTURE\n"
                "local_tier: Standard\nglobal_tier: 11\nauthor: Anatoly Maslennikov\n"
                "subjects:\n  governs: Atom/Test\n  depends_on: []\nrelations: {}"
            ),
            "content": body,
        }

    def set_journal_state(self, state: str) -> Path:
        """Place only the requested pre-existing Journal condition in this disposable Project."""
        journal = self.root / CONTROL / "_journal"
        if state == "missing":
            if journal.exists():
                shutil.rmtree(journal)
            return journal
        if state == "empty":
            if journal.exists() and any(journal.iterdir()):
                shutil.rmtree(journal)
            journal.mkdir(parents=True, exist_ok=True)
            return journal
        if state == "incomplete":
            if journal.exists() and any(path.name != "preexisting.ndjson" for path in journal.iterdir()):
                shutil.rmtree(journal)
            journal.mkdir(parents=True, exist_ok=True)
            (journal / "preexisting.ndjson").write_text(
                '{"schema_version":5,"kind":"workflow_execution","event":"started"}\n',
                encoding="utf-8",
            )
            return journal
        raise AssertionError(f"unknown Journal fixture state: {state}")

    def request(self, path: Path, status: str) -> dict[str, object]:
        actual = atom_from_path(self.root, path)
        return {"target": carrier_descriptor(self.root, actual), "status": status}

    def execute(self, request: dict[str, object]) -> dict[str, object]:
        return change_status_atom_action(self.root, request, execute=True, authorized=True)

    def assert_model(self, result: dict[str, object], request: dict[str, object]) -> None:
        expected = resolve_status_model(self.root, request["target"], request["status"])
        self.assertEqual(expected, result["status_model"])
        for pin in expected["model_sources"]:
            actual = self.root / pin["path"]
            self.assertEqual(pin["sha256"], hashlib.sha256(actual.read_bytes()).hexdigest())
            self.assertEqual(str(pin["revision"]), frontmatter_scalar(actual.read_text().split("\n---\n", 1)[0][4:], "version"))

    def assert_no_effect(self, result: dict[str, object]) -> None:
        self.assertFalse(any(effect["state"] != "unchanged" for effect in result["effects"]))
        if "effect_refs" in result:
            self.assertEqual([], result["effect_refs"])

    def test_actual_eight_role_domains_and_exact_source_pins(self) -> None:
        for role, _, _, source_id, statuses in DOMAINS:
            with self.subTest(role=role):
                atom_type = {"Operations": "Action", "Analysis": "Analysis Report", "Plan": "Task"}.get(role)
                path = self.atom(role, "active" if role == "Concern" else "Done" if role == "Analysis" else "Active",
                                 atom_type=atom_type)
                actual = atom_from_path(self.root, path)
                for status in statuses:
                    model = resolve_status_model(self.root, actual, status)
                    self.assertEqual(list(statuses), model["statuses"])
                    self.assertEqual(source_id, model["model_sources"][0]["atom_id"])
                    self.assertEqual(hashlib.sha256(self.sources[source_id].read_bytes()).hexdigest(),
                                     model["model_sources"][0]["sha256"])
                with self.assertRaises(StatusModelError):
                    resolve_status_model(self.root, actual, statuses[0].swapcase())

    def test_create_accepts_every_role_admitted_status_without_journal_or_draft_history(self) -> None:
        """Creation follows the current role model; absent recording state is not admission evidence."""
        journal = self.set_journal_state("missing")
        history = self.root / CONTROL / "archive" / "_draft_history"
        for offset, (role, letter, _directory, _source_id, statuses) in enumerate(DOMAINS, start=1):
            for status_offset, status in enumerate(statuses, start=1):
                with self.subTest(role=role, status=status):
                    number = 8100 + offset * 10 + status_offset
                    carrier = self.create_carrier(role, status, number=number)
                    result = create_atom_action(self.root, {"carrier": carrier}, execute=True, authorized=True)
                    self.assertEqual("applied", result["outcome"])
                    observed = result["observed"]
                    path = self.root / observed["path"]
                    self.assertTrue(path.is_file(), observed)
                    atom = atom_from_path(self.root, path)
                    self.assertEqual(role, frontmatter_scalar(atom.frontmatter, "content_role"))
                    self.assertEqual(status, frontmatter_scalar(atom.frontmatter, "status"))
                    self.assertIn(status, resolve_status_model(self.root, atom, status)["statuses"])
                    if status.casefold() == "draft":
                        self.assertIsNone(atom.atom_id)
                    else:
                        self.assertEqual(f"CA-{letter}-{number}", atom.atom_id)
        self.assertFalse(journal.exists(), "Create must not admit itself through a Journal directory")
        self.assertFalse(history.exists(), "Draft creation must not fabricate retained Draft history")

    def test_archived_create_requires_its_initial_revision_suffix(self) -> None:
        carrier = self.create_carrier("Requirement", "Archived", number=9050)
        self.assertTrue(carrier["path"].endswith("@1.md"))
        for invalid_path in (carrier["path"].replace("@1.md", ".md"),
                             carrier["path"].replace("@1.md", "@2.md"),
                             carrier["path"].replace("@1.md", "@1@1.md")):
            with self.subTest(path=invalid_path):
                before = self.snapshot()
                with self.assertRaisesRegex(LifecycleError, "filename-invalid"):
                    create_atom_action(self.root, {"carrier": {**carrier, "path": invalid_path}},
                                       execute=True, authorized=True)
                self.assertEqual(before, self.snapshot())
        before = self.snapshot()
        self.assertEqual("preview", create_atom_action(self.root, {"carrier": carrier})["outcome"])
        self.assertEqual(before, self.snapshot())
        created = create_atom_action(self.root, {"carrier": carrier}, execute=True, authorized=True)
        self.assertEqual("applied", created["outcome"])
        self.assertEqual("CA-R-9050", created["observed"]["atom_id"])
        self.assertEqual(1, created["observed"]["version"])
        self.assertEqual(carrier["path"], created["observed"]["path"])
        archived = self.root / created["observed"]["path"]
        active = self.execute(self.request(archived, "Active"))
        rearchived = self.execute(self.request(self.root / active["observed"]["path"], "Archived"))
        self.assertEqual(3, rearchived["observed"]["version"])
        self.assertTrue(rearchived["observed"]["path"].endswith("@3.md"))

    def test_manual_draft_promotes_without_retained_history_or_journal(self) -> None:
        """An operator-written Draft is a valid current carrier without retrospective provenance."""
        journal = self.set_journal_state("missing")
        history = self.root / CONTROL / "archive" / "_draft_history"
        path = self.atom("Requirement", "Draft", draft=True)
        self.assertFalse(history.exists())
        self.assertIsNone(atom_from_path(self.root, path).atom_id)
        result = self.execute(self.request(path, "Active"))
        self.assertEqual("applied", result["outcome"])
        observed = self.root / result["observed"]["path"]
        self.assertTrue(observed.is_file(), result)
        promoted = atom_from_path(self.root, observed)
        self.assertEqual("Active", frontmatter_scalar(promoted.frontmatter, "status"))
        self.assertRegex(promoted.atom_id or "", r"^CA-R-[0-9]+$")
        self.assertFalse(history.exists(), "Promotion must not manufacture Draft-history evidence")
        self.assertFalse(journal.exists(), "Promotion must not require a Journal directory")

    def test_manual_draft_to_archived_allocates_fresh_identity_and_next_version(self) -> None:
        """Leaving Draft allocates once even when the selected admitted Status is Archived."""
        journal = self.set_journal_state("missing")
        path = self.atom("Requirement", "Draft", draft=True)
        result = self.execute(self.request(path, "Archived"))
        self.assertEqual("applied", result["outcome"])
        observed = self.root / result["observed"]["path"]
        archived = atom_from_path(self.root, observed)
        self.assertEqual("Archived", frontmatter_scalar(archived.frontmatter, "status"))
        self.assertRegex(archived.atom_id or "", r"^CA-R-[0-9]+$")
        self.assertEqual(4, result["observed"]["version"])
        self.assertTrue(observed.name.endswith("@4.md"), result["observed"])
        self.assertFalse(journal.exists(), "Journal recording is not an admission precondition")

    def test_operations_workflow_draft_active_draft_uses_status_directories_and_fresh_identity(self) -> None:
        """Workflow carriers follow the Operations model without restoring an old Draft identity."""
        draft = self.atom("Operations", "Draft", atom_type="Workflow", draft=True)
        activated = self.execute(self.request(draft, "Active"))
        active_path = self.root / activated["observed"]["path"]
        active = atom_from_path(self.root, active_path)
        self.assertEqual("Active", frontmatter_scalar(active.frontmatter, "status"))
        self.assertRegex(active.atom_id or "", r"^CA-O-[0-9]+$")
        self.assertEqual(4, activated["observed"]["version"])
        self.assertEqual(self.root / CONTROL / "fixture/09_operations" / f"{active.atom_id}--golden.md", active_path)

        demoted = self.execute(self.request(active_path, "Draft"))
        draft_path = self.root / demoted["observed"]["path"]
        after = atom_from_path(self.root, draft_path)
        self.assertEqual("Draft", frontmatter_scalar(after.frontmatter, "status"))
        self.assertIsNone(after.atom_id)
        self.assertEqual(5, demoted["observed"]["version"])
        self.assertEqual(self.root / CONTROL / "fixture/09_operations/draft/CA-O--golden.md", draft_path)

    def test_supported_status_change_ignores_missing_empty_or_incomplete_journal(self) -> None:
        """Journal state is post-effect observation, not a Status-change admission gate."""
        for offset, state in enumerate(("missing", "empty", "incomplete"), start=1):
            with self.subTest(journal=state):
                journal = self.set_journal_state(state)
                before = (journal / "preexisting.ndjson").read_bytes() if (
                    journal / "preexisting.ndjson"
                ).is_file() else None
                path = self.atom("Requirement", "Active", number=8200 + offset)
                result = self.execute(self.request(path, "Archived"))
                self.assertEqual("applied", result["outcome"])
                self.assertEqual("Archived", result["observed"]["status"])
                if state == "missing":
                    self.assertFalse(journal.exists())
                elif state == "empty":
                    self.assertTrue(journal.is_dir())
                    self.assertEqual([], list(journal.iterdir()))
                elif before is not None:
                    self.assertEqual(before, (journal / "preexisting.ndjson").read_bytes())

    def test_actual_typed_atoms_use_role_fallback(self) -> None:
        for role, atom_type, status, source_id in (
            ("Operations", "Action", "Active", "CA-R-1874"),
            ("Operations", "Workflow", "Active", "CA-R-1874"),
            ("Analysis", "Rationale", "Done", "CA-R-1875"),
            ("Plan", "Task", "Active", "CA-R-1539"),
            ("Plan", "EPIC", "Active", "CA-R-1539"),
        ):
            with self.subTest(role=role, atom_type=atom_type):
                path = self.atom(role, status, atom_type=atom_type)
                model = resolve_status_model(self.root, atom_from_path(self.root, path), status)
                self.assertEqual(atom_type, model["type"])
                self.assertEqual(source_id, model["model_sources"][0]["atom_id"])

    def test_declared_fixture_type_extension_overrides_without_invented_status_values(self) -> None:
        """A labelled disposable Project extension, not a production source pin."""
        source = self.sources["CA-R-1874"]
        extension = source.with_name("CA-R-9900--fixture-action-domain.md")
        text = source.read_text(encoding="utf-8").replace('"CA-R-1874"', '"CA-R-9900"').replace(
            "atom_id: CA-R-1874", "atom_id: CA-R-9900"
        )
        text = re.sub(r'(?m)^(\s*governs:)\s*.*$',
                      r'\1 "Atom/Content Role: Operations/Type: `Action`/Status"', text, count=1)
        extension.write_text(text, encoding="utf-8")
        action = self.atom("Operations", "Active", atom_type="Action")
        selected = resolve_status_model(self.root, atom_from_path(self.root, action), "Active")
        self.assertEqual("CA-R-9900", selected["model_sources"][0]["atom_id"])
        self.assertEqual(["Draft", "Active", "Archived"], selected["statuses"])
        workflow = self.atom("Operations", "Active", number=8001, atom_type="Workflow")
        fallback = resolve_status_model(self.root, atom_from_path(self.root, workflow), "Active")
        self.assertEqual("CA-R-1874", fallback["model_sources"][0]["atom_id"])

    def test_every_role_same_status_is_noop_before_all_writes(self) -> None:
        for role, status in ((row[0], "active" if row[0] == "Concern" else "Done"
                             if row[0] in {"Analysis", "Plan"} else "Active") for row in DOMAINS):
            with self.subTest(role=role):
                path = self.atom(role, status)
                request = self.request(path, status)
                before = self.snapshot()
                result = self.execute(request)
                self.assertEqual("no-op", result["outcome"])
                self.assert_no_effect(result)
                self.assertEqual(before, self.snapshot())
                self.assertEqual(request["target"]["version"], result["observed"]["version"])
                self.assertEqual(request["target"]["updated_at"], result["observed"]["updated_at"])
                self.assert_model(result, request)

    def test_all_archival_roles_apply_current_d565_destination_and_preserve_whole_body(self) -> None:
        for role, _, directory, _, statuses in DOMAINS:
            if "Archived" not in statuses:
                continue
            with self.subTest(role=role):
                path = self.atom(role, "Done" if role == "Analysis" else "Active")
                request = self.request(path, "Archived")
                before_atom = atom_from_path(self.root, path)
                before_bytes = path.read_bytes()
                canonical_current = self.root / CONTROL / "fixture" / directory
                destination = canonical_current / "archived" / f"{path.stem}@4.md"
                self.assertFalse(destination.parent.exists())
                result = self.execute(request)
                self.assertEqual("applied", result["outcome"])
                self.assertFalse(path.exists())
                self.assertEqual(destination.relative_to(self.root).as_posix(), result["observed"]["path"])
                self.assertEqual("Archived", result["observed"]["status"])
                self.assertEqual(4, result["observed"]["version"])
                self.assertEqual(before_bytes, (self.root / result["history"]["prior_revision"]["path"]).read_bytes())
                after_atom = atom_from_path(self.root, destination)
                self.assertEqual(before_atom.content, after_atom.content)
                self.assertEqual(before_atom.atom_id, after_atom.atom_id)
                self.assert_model(result, request)

    def test_plan_local_container_backlog_done_canceled_and_reactivation(self) -> None:
        parent = self.atom("Plan", "Active", number=7999)
        canonical_parent = parent.with_name("CA-P-7999--golden-immutable-meaning.md")
        parent.rename(canonical_parent)
        path = self.atom("Plan", "Active", atom_type="Plan", container=canonical_parent.stem,
                         relations="relations:\n  is_decomposition_of: [CA-P-7999]")
        local = path.parent
        for status, folder in (("Backlog", "001_backlog"), ("Done", "done"),
                               ("Canceled", "canceled"), ("Active", None)):
            request = self.request(path, status)
            result = self.execute(request)
            self.assertEqual("applied", result["outcome"])
            expected = local / folder / "CA-P-8000--golden.md" if folder else local / "CA-P-8000--golden.md"
            self.assertEqual(expected.relative_to(self.root).as_posix(), result["observed"]["path"])
            path = expected
            self.assert_model(result, request)

    def test_concern_lowercase_nonactive_transitions_never_borrow_archive(self) -> None:
        path = self.atom("Concern", "active", atom_type="Problem")
        local = self.root / CONTROL / "fixture/01_concern"
        for status in ("resolved", "canceled", "active"):
            request = self.request(path, status)
            result = self.execute(request)
            expected = local / path.name if status == "active" else local / status / path.name
            self.assertEqual(expected.relative_to(self.root).as_posix(), result["observed"]["path"])
            path = expected
            self.assert_model(result, request)
        before = self.snapshot()
        with self.assertRaises(StatusModelError):
            resolve_status_model(self.root, atom_from_path(self.root, path), "Archived")
        self.assertEqual(before, self.snapshot())

    def test_preview_denied_execution_and_destination_collision_are_unchanged(self) -> None:
        path = self.atom("Requirement", "Active")
        request = self.request(path, "Archived")
        before = self.snapshot()
        preview = change_status_atom_action(self.root, request)
        self.assertEqual("preview", preview["outcome"])
        self.assert_no_effect(preview)
        self.assertEqual(before, self.snapshot())
        with self.assertRaises((LifecycleError, StatusModelError, ToolError)):
            change_status_atom_action(self.root, request, execute=True, authorized=False)
        self.assertEqual(before, self.snapshot())
        destination = path.parent / "archived" / f"{path.stem}@4.md"
        destination.parent.mkdir()
        destination.write_bytes(b"reserved destination; must survive")
        collided = self.snapshot()
        with self.assertRaises((LifecycleError, StatusModelError, ToolError)):
            self.execute(request)
        self.assertEqual(collided, self.snapshot())

    def test_caller_models_and_revoked_authority_refuse_before_effects(self) -> None:
        path = self.atom("Requirement", "Active")
        request = self.request(path, "Archived")
        for field, value in (("content_role", "Plan"), ("statuses", ["Active", "Reviewed", "Archived"])):
            forged = copy.deepcopy(request)
            forged["status_model"] = resolve_status_model(self.root, forged["target"], "Archived")
            forged["status_model"][field] = value
            before = self.snapshot()
            with self.assertRaises((LifecycleError, StatusModelError, ToolError)):
                self.execute(forged)
            self.assertEqual(before, self.snapshot())
        source = self.sources["CA-R-1309"]
        original = source.read_bytes()
        for changed in (original.replace(b'status: "Active"', b'status: "Archived"').replace(
                            b"status: Active", b"status: Archived"),):
            source.write_bytes(changed)
            before = self.snapshot()
            with self.assertRaises((LifecycleError, StatusModelError, ToolError)):
                self.execute(request)
            self.assertEqual(before, self.snapshot())
            source.write_bytes(original)

    def test_native_exact_status_refusals_leave_all_project_bytes_unchanged(self) -> None:
        for role, current, denied in (("Requirement", "Active", "Reviewed"),
                                      ("Requirement", "Active", "active"),
                                      ("Plan", "Done", "done"),
                                      ("Concern", "resolved", "Active"),
                                      ("Analysis", "Done", "Active")):
            with self.subTest(role=role, denied=denied):
                path = self.atom(role, current)
                request = self.request(path, denied)
                before = self.snapshot()
                with self.assertRaises((LifecycleError, StatusModelError, ToolError)):
                    self.execute(request)
                self.assertEqual(before, self.snapshot())

    def test_source_change_after_pure_preflight_is_reobserved_before_effect(self) -> None:
        source = self.sources["CA-R-1309"]
        original = source.read_bytes()
        allowed = lifecycle_intents._execute_allowed
        changes = (original + b"\nChanged after admission.\n",
                   original.replace(b'status: "Active"', b'status: "Archived"').replace(
                       b"status: Active", b"status: Archived"))
        for offset, changed in enumerate(changes):
            with self.subTest(revocation=b"Changed after" not in changed):
                path = self.atom("Requirement", "Active", number=8000 + offset,
                                 container=f"race-{offset}")
                request = self.request(path, "Archived")
                before_target = path.read_bytes()
                preflight = preflight_atom_lifecycle(self.root, "change_status", request)
                self.assertEqual(hashlib.sha256(original).hexdigest(),
                                 preflight["status_model"]["model_sources"][0]["sha256"])
                changed_snapshot = []

                def change_authority(*, execute: bool, authorized: bool) -> bool:
                    source.write_bytes(changed)
                    changed_snapshot.append(self.snapshot())
                    return allowed(execute=execute, authorized=authorized)

                try:
                    with patch.object(lifecycle_intents, "_execute_allowed", side_effect=change_authority):
                        with self.assertRaises((LifecycleError, StatusModelError, ToolError)):
                            self.execute(request)
                    self.assertEqual(before_target, path.read_bytes())
                    self.assertEqual(1, len(changed_snapshot))
                    self.assertEqual(changed_snapshot[0], self.snapshot())
                    self.assertFalse((path.parent / "archived").exists())
                    self.assertFalse((path.parent / "archive").exists())
                finally:
                    source.write_bytes(original)

    def test_archive_retains_legacy_history_and_reports_refs_without_repair(self) -> None:
        path = self.atom("Requirement", "Active", relations="relations:\n  depends_on: [CA-R-8001]")
        successor = self.atom("Requirement", "Active", number=8001)
        referrer = self.atom("Requirement", "Active", number=8002,
                             relations="relations:\n  depends_on: [CA-R-8000]")
        unchanged = {candidate: candidate.read_bytes() for candidate in (successor, referrer)}
        legacy = path.parent / "archive" / f"{path.stem}@2.md"
        legacy.parent.mkdir()
        legacy.write_bytes(b"immutable legacy revision evidence")
        unchanged[legacy] = legacy.read_bytes()
        result = self.execute(self.request(path, "Archived"))
        self.assertEqual("applied", result["outcome"])
        self.assertEqual(
            [
                {"direction": "outgoing", "relation_owner": "CA-R-8000",
                 "referenced_atom_id": "CA-R-8001", "reason": "target-status-becomes-inactive",
                 "active_referrer": True},
                {"direction": "inbound", "relation_owner": "CA-R-8002",
                 "referenced_atom_id": "CA-R-8000", "reason": "target-status-becomes-inactive",
                 "active_referrer": True},
            ],
            result["broken_references"],
        )
        self.assertFalse(result["repair_handoff"]["automatic_repair"])
        for candidate, raw in unchanged.items():
            self.assertEqual(raw, candidate.read_bytes())

    def test_actual_unassigned_draft_same_status_is_noop(self) -> None:
        path = self.atom("Requirement", "Draft", draft=True)
        request = self.request(path, "Draft")
        self.assertIsNone(request["target"]["atom_id"])
        before = self.snapshot()
        result = self.execute(request)
        self.assertEqual("no-op", result["outcome"])
        self.assert_no_effect(result)
        self.assertEqual(before, self.snapshot())
        self.assertIsNone(result["observed"]["atom_id"])

    def test_identified_to_draft_removes_assignment_but_retains_same_meaning(self) -> None:
        path = self.atom("Requirement", "Active")
        before = atom_from_path(self.root, path)
        history = path.parent / "archive" / f"{path.stem}@2.md"
        history.parent.mkdir()
        history.write_bytes(b"old identified revision evidence")
        before_history = history.read_bytes()
        result = self.execute(self.request(path, "Draft"))
        self.assertEqual("applied", result["outcome"])
        destination = self.root / result["observed"]["path"]
        self.assertFalse(path.exists())
        self.assertEqual("CA-R--golden.md", destination.name)
        self.assertIsNone(result["observed"]["atom_id"])
        after = atom_from_path(self.root, destination)
        self.assertIsNone(frontmatter_scalar(after.frontmatter, "atom_id"))
        self.assertEqual(before.content, after.content)
        self.assertEqual(4, result["observed"]["version"])
        self.assertEqual(before_history, history.read_bytes())


if __name__ == "__main__":
    unittest.main()
