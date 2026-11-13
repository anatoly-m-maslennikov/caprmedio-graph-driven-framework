# CA-E-681@6
from __future__ import annotations

import asyncio
import duckdb
from pathlib import Path
import sys
import tempfile
import unittest


REPOSITORY = Path(__file__).resolve().parents[5]
PROGRAMMATIC = REPOSITORY / "LAYER_2_FRAMEWORK_ENGINE" / "FEATURE_PROGRAMMATIC"
APP_ROOT = PROGRAMMATIC / "FEATURE_APPS" / "APP_WORKBENCH"
for location in (PROGRAMMATIC / "FEATURE_MCP", APP_ROOT.parent, APP_ROOT / "tests"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from smalltest_support import built_assets, extension_directory, write_atom, write_settings  # noqa: E402
from workbench_tools import WorkbenchTools  # noqa: E402


class _ConfiguredWorkbenchTools(WorkbenchTools):
    def __init__(self, root):
        super().__init__(root)
        self.assets = built_assets(root)

    def _owner(self):
        if self._service is None:
            self._service = WorkbenchService(
                self.root, extension_directory=extension_directory(REPOSITORY), **self.assets,
            )
        return self._service


class WorkbenchRereadTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        control = write_settings(self.root)
        declarations = write_scope_unit_declarations(
            self.root,
            ({"scope_unit_name": "ENGINE", "scope_unit_type": "Ordered", "scope_unit_label": "LAYER", "local_order": 1},),
            control_root=control,
        )
        self.source = Path(declarations["ENGINE"]["authority_path"]) / "04_requirement" / "CA-R-501.md"
        write_atom(self.source, "CA-R-501")
        self.source_bytes = self.source.read_bytes()
        database = self.root / ".caprmedio_runtime" / "workbench" / "projection.duckdb"
        database.parent.mkdir(parents=True)
        connection = duckdb.connect(str(database))
        try:
            connection.execute("CREATE SCHEMA obsolete")
            connection.execute("CREATE TABLE obsolete.stale (value INTEGER)")
            connection.execute("INSERT INTO obsolete.stale VALUES (1)")
        finally:
            connection.close()
        self.tools = _ConfiguredWorkbenchTools(self.root)
        self.addCleanup(lambda: asyncio.run(self.tools.close()))

    def test_reread_rebuilds_only_derived_database_and_preserves_sources_and_saved_queries(self) -> None:
        before = asyncio.run(self.tools.call("query_run", {"sql": "SELECT 1", "save": True}))
        database = self.root / ".caprmedio_runtime" / "workbench" / "projection.duckdb"
        temporary = database.parent / "duckdb-temp"
        self.assertTrue(database.is_file())
        self.assertTrue(temporary.is_dir())
        self.assertEqual(
            [[1]],
            asyncio.run(self.tools.call("query_run", {"sql": "SELECT count(*) FROM obsolete.stale", "result_delivery": "inline"}))["rows"],
        )
        write_atom(self.source.with_name("CA-R-502.md"), "CA-R-502")

        reread = asyncio.run(self.tools.call("workbench_reread", {}))

        self.assertEqual({"service": "workbench", "status": "ready"}, reread)
        self.assertTrue(database.is_file())
        self.assertTrue(temporary.is_dir())
        self.assertEqual(self.source_bytes, self.source.read_bytes())
        self.assertEqual(
            [[0]],
            asyncio.run(self.tools.call("query_run", {
                "sql": "SELECT count(*) FROM information_schema.tables WHERE table_schema = 'obsolete'", "result_delivery": "inline",
            }))["rows"],
        )
        self.assertEqual(
            [["CA-R-502"]],
            asyncio.run(self.tools.call("query_run", {
                "sql": 'SELECT "header.atom_id" FROM atoms WHERE "header.atom_id" = \'CA-R-502\'', "result_delivery": "inline",
            }))["rows"],
        )
        with self.assertRaisesRegex(Exception, "unknown query_id"):
            asyncio.run(self.tools.call("query_page", {"query_id": before["query_id"], "offset": 0}))
        saved = asyncio.run(self.tools.call("query_load", {"reference": before["saved_query_id"]}))
        self.assertEqual("SELECT 1", saved["sql"])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
