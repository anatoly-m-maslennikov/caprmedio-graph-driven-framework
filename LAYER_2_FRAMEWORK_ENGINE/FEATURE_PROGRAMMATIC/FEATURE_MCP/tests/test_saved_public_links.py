# CA-M-1008@2
"""Saved query links across HTTP and stdio transports."""
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from urllib.parse import urlencode

MCP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(MCP), str(MCP.parent / "FEATURE_TOOLS")]
from registry_workbench_provider import WorkbenchProvider
from workbench_links import public_saved


class SavedPublicLinksTests(unittest.TestCase):
    def test_stdio_config_and_unknown_for_save_and_list(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            selection = SimpleNamespace(root=root, settings={"project": {"name": "alpha"}})
            provider = WorkbenchProvider(SimpleNamespace(selection=selection))
            context = SimpleNamespace(request=None, params={"arguments": {"project_root": str(root)}})
            saved = {"saved_query_id": "q_1"}
            unknown = provider.present_result("query_run", saved, context)
            self.assertEqual({**saved, "saved_query_url": None, "saved_query_url_reason": "workbench_url_unknown"}, unknown)
            settings = root / ".caprmedio_runtime" / "caprmedio_runtime_settings.toml"
            settings.parent.mkdir()
            settings.write_text('[workbench]\npublic_url = "https://example.test/custom/page"\n')
            linked = provider.present_result("query_saved_list", {"items": [saved]}, context)["items"][0]
            self.assertEqual("https://example.test/custom/page?" + urlencode({"query": "q_1", "project_root": str(root)}), linked["saved_query_url"])
            settings.write_text('[workbench]\npublic_url = "javascript:alert(1)"\n')
            self.assertIsNone(provider.present_result("query_run", saved, context)["saved_query_url"])
            settings.write_text('invalid toml =')
            self.assertIsNone(provider.present_result("query_run", saved, context)["saved_query_url"])
            request = SimpleNamespace(base_url="http://localhost/")
            self.assertEqual("http://localhost/caprmedio/workbench/alpha?query=q_1", public_saved(saved, request, selection)["saved_query_url"])


if __name__ == "__main__":
    unittest.main()
