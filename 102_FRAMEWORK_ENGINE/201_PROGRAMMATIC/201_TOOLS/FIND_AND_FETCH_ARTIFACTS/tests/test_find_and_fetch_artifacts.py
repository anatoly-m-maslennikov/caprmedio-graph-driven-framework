import os
from contextlib import contextmanager
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import find_and_fetch_artifacts as artifact_query
from find_and_fetch_artifacts import ArtifactQueryError, query_artifacts
from query_filter import QueryFilterError, evaluate_filter, parse_filter
from project_selection import bind_selection, resolve_project

DEFAULT_BYTES = (HERE.parents[3] / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
                 "METHODOLOGY_SOURCES/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml").read_bytes()


class ArtifactQueryGoldenTest(unittest.TestCase):
    @contextmanager
    def project(self, name="fixture"):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw).resolve()
            control = root / f".caprmedio_{name}"
            core = control / "core"
            core.mkdir(parents=True)
            (control / "caprmedio_project_settings.toml").write_text(
                f'[project]\nname = "{name}"\n[paths]\ncontrol_root = ".caprmedio_{name}"\n', encoding="utf-8")
            (control / "project_structure.toml").write_text(
                f'schema_version = 1\n[[scope_units]]\nscope_unit_name = "CORE_META_MODEL"\nauthority_path = ".caprmedio_{name}/core"\ndelivery_path = ".caprmedio_{name}/output"\n', encoding="utf-8")
            (core / "caprmedio_framework_default_settings.toml").write_bytes(DEFAULT_BYTES)
            yield root

    def fixture(self, root, name, frontmatter, body=""):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("---\n" + frontmatter + "\n---\n" + body, encoding="utf-8")
        return path

    def assert_rejected(self, root, request, **kwargs):
        with self.assertRaises((ArtifactQueryError, artifact_query.QueryFilterError)):
            query_artifacts(root, request, **kwargs)

    def test_default_ids_selected_values_and_canonical_section_bodies(self):
        with self.project() as raw:
            root = Path(raw)
            self.fixture(root, "a.md", "atom_id: A\nstatus: Draft\nflag: true\nnullable: null\nwhen: 2026-10-05\nvalues: [zero, one]", "## same/name~x\nalpha\n### child\nchild\n## sibling\nbeta\n```markdown\n## pseudo\n```\n")
            self.fixture(root, "b.md", "artifact_id: B\nstatus: Archived\nflag: 1\nmap: {kind: x, number: 1}", "## same/name~x\nbravo\n")
            self.fixture(root, "c.md", "artifact_id: C\nstatus: Active")
            source_before = {path.name: path.read_bytes() for path in root.glob("*.md")}
            request = {
                "filter": '"fm:/flag" = true OR "fm:/status" IN ("Archived")',
                "select": ["fm:/nullable", "fm:/when", "section:/2:same~1name~0x"], "limit": 2,
            }
            result = query_artifacts(root, request)
            self.assertEqual([row["artifact_id"] for row in result["results"]], ["A", "B"])
            self.assertEqual(result["results"][0]["fm:/nullable"], None)
            self.assertEqual(result["results"][0]["fm:/when"], "2026-10-05")
            self.assertEqual(result["results"][0]["section:/2:same~1name~0x"], "alpha\n### child\nchild\n")
            self.assertEqual(result["results"][1]["fm:/nullable"], "missing")
            self.assertEqual([row["artifact_id"] for row in query_artifacts(root, {})["results"]], ["A", "B", "C"])
            self.assertEqual(query_artifacts(root, {"filter": '"fm:/map" = {"kind":"x","number":1}'})["results"], [{"artifact_id": "B"}])
            self.assertEqual(query_artifacts(root, {"filter": '"fm:/values" IN (["zero","one"])'})["results"], [{"artifact_id": "A"}])
            self.assertEqual(query_artifacts(root, {"filter": '"fm:/status" != "Draft"'})["results"], [{"artifact_id": "B"}, {"artifact_id": "C"}])
            self.assertEqual(source_before, {path.name: path.read_bytes() for path in root.glob("*.md")})
            self.assertTrue(result["coverage"]["complete"])
            self.assertFalse(result["coverage"]["incomplete"])
            self.assertEqual(result["diagnostics"], {"complete": True, "incomplete": False, "findings": []})

    def test_continuation_uses_exact_retained_members_without_enumeration(self):
        with self.project() as raw:
            root = Path(raw)
            self.fixture(root, "a.md", "artifact_id: A")
            self.fixture(root, "b.md", "artifact_id: B")
            first = query_artifacts(root, {"limit": 1})
            continuation = {"limit": 1, "snapshot": first["snapshot"], "cursor": first["next_cursor"]}
            with patch.object(artifact_query.os, "walk", side_effect=AssertionError("must not enumerate")):
                second = query_artifacts(root, continuation)
            self.assertEqual(second["results"], [{"artifact_id": "B"}])
            self.assertEqual(second["examined_count"], 2)
            self.assertFalse(second["has_more"])

    def test_same_spelling_frontmatter_and_section_selectors_do_not_collide(self):
        with self.project() as raw:
            root = Path(raw)
            self.fixture(root, "collision.md", "artifact_id: Collision\nsummary: frontmatter value", "## summary\nsection value\n")
            self.fixture(root, "frontmatter-only.md", "artifact_id: FrontmatterOnly\nsummary: section value", "## unrelated\nother\n")

            self.assertEqual(
                query_artifacts(root, {})["results"],
                [{"artifact_id": "Collision"}, {"artifact_id": "FrontmatterOnly"}],
            )
            self.assertEqual(
                query_artifacts(root, {"filter": '"fm:/summary" = "frontmatter value"'})["results"],
                [{"artifact_id": "Collision"}],
            )
            self.assertEqual(
                query_artifacts(root, {"filter": '"section:/2:summary" = "section value\\n"'})["results"],
                [{"artifact_id": "Collision"}],
            )
            fetched = query_artifacts(root, {
                "filter": '"section:/2:summary" = "section value\\n"',
                "select": ["fm:/summary", "section:/2:summary"],
            })
            self.assertEqual(fetched["results"], [{
                "artifact_id": "Collision", "fm:/summary": "frontmatter value",
                "section:/2:summary": "section value\n",
            }])

    def test_continuation_rejects_changed_root_members_and_tamper(self):
        with self.project() as raw, self.project("other") as other:
            root = Path(raw)
            item = self.fixture(root, "a.md", "artifact_id: A")
            first = query_artifacts(root, {"limit": 1})
            tampered = dict(first["snapshot"])
            tampered["digest"] = "0" * 64
            self.assert_rejected(root, {"snapshot": tampered, "cursor": first["next_cursor"]})
            self.assert_rejected(Path(other), {"snapshot": first["snapshot"], "cursor": first["next_cursor"]})
            item.write_text("---\nartifact_id: Changed\n---\n", encoding="utf-8")
            self.assert_rejected(root, {"snapshot": first["snapshot"], "cursor": first["next_cursor"]})

    def test_cursor_is_bound_to_filter_selection_settings_and_bytes(self):
        with self.project() as raw:
            root = Path(raw)
            self.fixture(root, "a.md", "artifact_id: A\nkind: keep")
            self.fixture(root, "b.md", "artifact_id: B\nkind: keep")
            request = {"filter": '"fm:/kind" = "keep"', "select": ["fm:/kind"], "limit": 1}
            first = query_artifacts(root, request)
            self.assert_rejected(root, {"filter": '"fm:/kind" = "other"', "select": ["fm:/kind"], "snapshot": first["snapshot"], "cursor": first["next_cursor"]})
            self.assert_rejected(root, {"filter": request["filter"], "select": [], "snapshot": first["snapshot"], "cursor": first["next_cursor"]})
            self.assert_rejected(root, {"filter": request["filter"], "select": request["select"], "settings": {"max_page_size": 1}, "snapshot": first["snapshot"], "cursor": first["next_cursor"]})
            self.assert_rejected(root, {"filter": request["filter"], "select": request["select"], "snapshot": first["snapshot"], "cursor": first["next_cursor"] + "x"})

    def test_selector_escaping_section_namespace_and_leading_array_zero(self):
        with self.project() as raw:
            root = Path(raw)
            self.fixture(root, "x.md", "artifact_id: X\nitems: [zero, one]", "## a/b~c\nok\n")
            self.assertEqual(query_artifacts(root, {"select": ["section:/2:a~1b~0c"]})["results"][0]["section:/2:a~1b~0c"], "ok\n")
            for selector in ("section:2:a", "section:/2:a~2b", "fm:/items/01", "fm:/bad~2key"):
                self.assert_rejected(root, {"select": [selector]})
            self.assert_rejected(root, {"filter": '"fm:/missing" = 1 AND "fm:/items/01" = 1'})

    def test_yaml_safe_duplicate_and_identity_failures_are_not_partial_results(self):
        with self.project() as raw:
            root = Path(raw)
            self.fixture(root, "duplicate-key.md", "artifact_id: One\nartifact_id: Two")
            self.assert_rejected(root, {})
        with self.project() as raw:
            root = Path(raw)
            self.fixture(root, "missing.md", "status: Draft")
            self.assert_rejected(root, {})
            (root / "missing.md").unlink()
            self.fixture(root, "conflict.md", "atom_id: A\nartifact_id: B")
            self.assert_rejected(root, {})
            (root / "conflict.md").unlink()
            self.fixture(root, "a.md", "artifact_id: Duplicate")
            self.fixture(root, "b.md", "atom_id: Duplicate")
            self.assert_rejected(root, {})
            (root / "a.md").unlink()
            (root / "b.md").unlink()
            self.fixture(root, "headings.md", "artifact_id: Heading", "## duplicate\none\n## duplicate\ntwo\n")
            self.assert_rejected(root, {})

    def test_secret_values_and_forbidden_carriers_are_never_selected_or_read(self):
        with self.project() as raw:
            root = Path(raw)
            self.fixture(root, "safe.md", "artifact_id: Safe\nconfig: {nested: {token: not-for-output}}")
            (root / "secret.env").write_bytes(b"this must not be read")
            self.assert_rejected(root, {"select": ["fm:/config"]})
            self.assert_rejected(root, {"select": ["fm:/token"]})
            self.assert_rejected(root, {"mutation": {"write": "forbidden"}})
            self.assert_rejected(root, {"filter": '"fm:/config" = __import__("os")'})
            (root / "secret.md").write_text("unreadable secret carrier", encoding="utf-8")
            self.assert_rejected(root, {})

    def test_root_and_symlink_escape_are_rejected(self):
        with self.project() as raw, tempfile.TemporaryDirectory() as outside:
            root = Path(raw)
            self.fixture(root, "safe.md", "artifact_id: Safe")
            self.fixture(Path(outside), "outside.md", "artifact_id: Outside")
            link = root / "escape"
            try:
                os.symlink(outside, link)
            except (NotImplementedError, OSError):
                self.skipTest("symlinks are unavailable")
            self.assert_rejected(root, {})
            self.assert_rejected(root / "absent", {})

    def test_every_resolved_budget_rejects_actual_overage(self):
        with self.project() as raw:
            root = Path(raw)
            first = self.fixture(root, "a.md", "artifact_id: A\nvalue: 1")
            second = self.fixture(root, "b.md", "artifact_id: B\nvalue: 2")
            self.assert_rejected(root, {}, settings={"max_request_bytes": 1})
            self.assert_rejected(root, {"filter": 'NOT (NOT ("fm:/value" = 1))'}, settings={"max_grammar_depth": 1})
            self.assert_rejected(root, {"filter": '"fm:/value" = 1 OR "fm:/value" = 2'}, settings={"max_filter_tokens": 1})
            self.assert_rejected(root, {"filter": '"fm:/value" IN (1, 2)'}, settings={"max_in_members": 1})
            self.assert_rejected(root, {"select": ["fm:/value", "fm:/missing"]}, settings={"max_selected_fields": 1})
            self.assert_rejected(root, {"limit": 2}, settings={"max_page_size": 1})
            self.assert_rejected(root, {}, settings={"max_snapshot_members": 1})
            self.assert_rejected(root, {}, settings={"max_file_bytes": 1})
            total_limit = first.stat().st_size + second.stat().st_size - 1
            self.assert_rejected(root, {}, settings={"max_file_bytes": 10000, "max_total_read_bytes": total_limit})
            read_member = artifact_query._read_member
            def expired_member(*args, **kwargs):
                with patch.object(artifact_query.time, "monotonic", return_value=kwargs["started"] + 2):
                    return read_member(*args, **kwargs)
            with patch.object(artifact_query, "_read_member", side_effect=expired_member):
                self.assert_rejected(root, {}, settings={"timeout_seconds": 1})
        with self.project() as raw:
            root = Path(raw)
            (root / "bad-a.md").write_text("not markdown", encoding="utf-8")
            (root / "bad-b.md").write_text("not markdown", encoding="utf-8")
            self.assert_rejected(root, {}, settings={"max_findings": 1})

    def test_parser_contract_remains_shared_and_typed(self):
        tree = parse_filter('NOT ("x" = 1) AND "y" != null')
        self.assertTrue(evaluate_filter(tree, lambda key: {"x": True, "y": "ok"}[key]))
        with self.assertRaises(QueryFilterError):
            parse_filter('"x" = __import__("os")')

    def test_selected_project_defaults_and_override_precedence(self):
        with self.project() as root:
            defaults = tomllib.loads(DEFAULT_BYTES.decode())["query"]
            self.assertEqual(defaults, artifact_query._load_budgets(root, None, None))
            instance = root / ".caprmedio_fixture/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"
            instance.parent.mkdir()
            instance.write_text("[query]\nmax_page_size = 2\n", encoding="utf-8")
            self.assertEqual(2, artifact_query._load_budgets(root, None, None)["max_page_size"])
            self.assertEqual(3, artifact_query._load_budgets(root, {"max_page_size": 3}, None)["max_page_size"])
            self.assertEqual(4, artifact_query._load_budgets(root, {"max_page_size": 3}, {"max_page_size": 4})["max_page_size"])
            self.fixture(root, "a.md", "artifact_id: A")
            self.fixture(root, "b.md", "artifact_id: B")
            self.assertEqual([{"artifact_id": "A"}, {"artifact_id": "B"}], query_artifacts(root, {})["results"])
            self.assertEqual([{"artifact_id": "A"}], query_artifacts(root, {"settings": {"max_page_size": 1}})["results"])
            self.assertEqual("[query]\nmax_page_size = 2\n", instance.read_text())

    def test_projects_are_isolated_and_foreign_bound_root_is_refused(self):
        with self.project("alpha") as alpha, self.project("beta") as beta:
            for root, name, size in ((alpha, "alpha", 1), (beta, "beta", 2)):
                default = root / f".caprmedio_{name}/core/caprmedio_framework_default_settings.toml"
                default.write_bytes(DEFAULT_BYTES.replace(b"max_page_size = 100", f"max_page_size = {size}".encode()))
                self.fixture(root, "a.md", "artifact_id: A")
                self.fixture(root, "b.md", "artifact_id: B")
            self.assertEqual(1, query_artifacts(alpha, {})["returned_count"])
            self.assertEqual(2, query_artifacts(beta, {})["returned_count"])
            with bind_selection(resolve_project(alpha)):
                self.assertEqual(1, query_artifacts(alpha, {})["returned_count"])
                self.assert_rejected(beta, {})

    def test_invalid_budget_sources_and_explicit_values_refuse(self):
        for case in ("missing-default", "malformed-default", "missing-field", "unknown-field", "symlink-default",
                     "missing-core", "duplicate-core", "escaping-core", "malformed-instance", "symlink-instance", "instance-parent-file"):
            with self.subTest(case=case), self.project() as root:
                control = root / ".caprmedio_fixture"
                default = control / "core/caprmedio_framework_default_settings.toml"
                structure = control / "project_structure.toml"
                if case == "missing-default":
                    default.unlink()
                elif case == "malformed-default":
                    default.write_text("[query", encoding="utf-8")
                elif case == "missing-field":
                    default.write_bytes(DEFAULT_BYTES.replace(b"max_page_size = 100\n", b""))
                elif case == "unknown-field":
                    default.write_bytes(DEFAULT_BYTES.replace(b"[query]\n", b"[query]\nunknown = 1\n"))
                elif case == "symlink-default":
                    target = root / "default.toml"
                    target.write_bytes(DEFAULT_BYTES)
                    default.unlink()
                    default.symlink_to(target)
                elif case == "missing-core":
                    structure.write_text("schema_version = 1\n", encoding="utf-8")
                elif case == "duplicate-core":
                    structure.write_text(structure.read_text() + '[[scope_units]]\nscope_unit_name = "CORE_META_MODEL"\nauthority_path = ".caprmedio_fixture/core"\n', encoding="utf-8")
                elif case == "escaping-core":
                    structure.write_text(structure.read_text().replace(".caprmedio_fixture/core", "../outside"), encoding="utf-8")
                else:
                    instance = control / "000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"
                    if case == "instance-parent-file":
                        instance.parent.write_text("not a directory", encoding="utf-8")
                    else:
                        instance.parent.mkdir()
                    if case == "malformed-instance":
                        instance.write_text("[query", encoding="utf-8")
                    elif case == "symlink-instance":
                        instance.symlink_to(default)
                with self.assertRaises(ArtifactQueryError):
                    artifact_query._load_budgets(root, None, None)
        with self.project() as root:
            for value in (True, 0, -1, "1"):
                with self.subTest(value=value), self.assertRaises(ArtifactQueryError):
                    artifact_query._load_budgets(root, None, {"max_page_size": value})
            with self.assertRaises(ArtifactQueryError):
                artifact_query._load_budgets(root, {"unknown": 1}, None)

    def test_bound_selection_drift_and_changed_continuation_budgets_refuse(self):
        with self.project() as root:
            self.fixture(root, "a.md", "artifact_id: A")
            self.fixture(root, "b.md", "artifact_id: B")
            first = query_artifacts(root, {"limit": 1})
            self.assert_rejected(root, {"limit": 1, "snapshot": first["snapshot"], "cursor": first["next_cursor"],
                                        "settings": {"max_page_size": 2}})
            selection = resolve_project(root)
            selection.structure_path.write_text(selection.structure_path.read_text() + "\n# drift\n", encoding="utf-8")
            with bind_selection(selection):
                self.assert_rejected(root, {})

    def test_instance_creation_or_removal_during_resolution_refuses(self):
        for present in (False, True):
            with self.subTest(present=present), self.project() as root:
                instance = root / ".caprmedio_fixture/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"
                instance.parent.mkdir()
                if present:
                    instance.write_text("[query]\nmax_page_size = 1\n", encoding="utf-8")
                selection = resolve_project(root)
                currentness = artifact_query.ReadContext.currentness
                def change_instance(reader):
                    result = currentness(reader)
                    if present:
                        instance.unlink()
                    else:
                        instance.write_text("[query]\nmax_page_size = 1\n", encoding="utf-8")
                    return result
                with bind_selection(selection), patch.object(artifact_query.ReadContext, "currentness", change_instance):
                    self.assert_rejected(root, {})


if __name__ == "__main__":
    unittest.main()
