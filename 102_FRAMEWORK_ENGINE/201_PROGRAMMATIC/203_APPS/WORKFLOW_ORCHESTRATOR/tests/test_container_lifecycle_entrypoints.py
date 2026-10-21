"""Container coordination is rooted in sealed MCP preview, not member Runs."""
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch


APP = Path(__file__).resolve().parents[1]
for location in (APP, APP.parents[1] / "204_MCP", APP.parents[1] / "201_TOOLS"):
    sys.path.insert(0, str(location))

from selected_native_providers import SelectedNativeProviders  # noqa: E402
from selected_routes import _QueueBackedSelectedSupport  # noqa: E402


class ContainerLifecycleEntrypointTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)

    def test_preview_seals_scope_separately_from_one_atom_admission(self):
        own = {"requested_status": "Done"}
        scope = {"parent": own, "descendants": [{"status": "Canceled"}]}
        manifest = {"routes": [{"route": "change_atom_status"}], "manifest_ref": "fixture.json",
                    "canonical_manifest_sha256": "a" * 64, "source_freshness": {"state": "current"}}
        request = {"operation_route": "change_atom_status", "parameters": {},
                   "definition_manifest": {"manifest_ref": "fixture.json", "manifest_digest": "a" * 64},
                   "source_freshness": {"state": "current"}}
        with patch("selected_routes.load_selected_manifest", return_value=manifest), \
                patch("selected_execution.preflight_selected_lifecycle", return_value=own), \
                patch("container_lifecycle_admission.seal_contained_status_changes", return_value=scope):
            observation = _QueueBackedSelectedSupport(self.root, None)._tracker()._observe(request)
        self.assertTrue(observation["current"])
        self.assertEqual(own, observation["observed"]["lifecycle_admission"])
        self.assertEqual(scope, observation["observed"]["container_lifecycle"])
        self.assertEqual([], list(self.root.iterdir()))

    def test_worker_routes_sealed_root_to_technical_coordinator_only(self):
        frozen = {"request": {"execution": {"proposal_receipt": {"source_freshness": {
            "observed": {"container_lifecycle": {"descendants": [1]}}}}}}}
        selected = MagicMock()
        providers = SelectedNativeProviders(self.root, implementation_agent=lambda *_: {})
        with patch("selected_native_providers.SelectedExecution") as loader, \
                patch.object(providers, "execution", return_value=selected), \
                patch("container_lifecycle_composition.coordinate_container_lifecycle", return_value={"coordinator_id": "root"}) as coordinate:
            loader.return_value.load.return_value = frozen
            self.assertEqual({"coordinator_id": "root"}, providers.dispatch("root"))
        coordinate.assert_called_once_with(selected, frozen)
        selected.dispatch.assert_not_called()

    def test_ordinary_member_dispatch_does_not_reenter_coordinator(self):
        frozen = {"request": {"execution": {"proposal_receipt": {"source_freshness": {
            "observed": {"lifecycle_admission": {"requested_status": "Canceled"}}}}}}}
        selected = MagicMock()
        providers = SelectedNativeProviders(self.root, implementation_agent=lambda *_: {})
        with patch("selected_native_providers.SelectedExecution") as loader, \
                patch.object(providers, "execution", return_value=selected):
            loader.return_value.load.return_value = frozen
            self.assertIs(selected.dispatch.return_value, providers.dispatch("member"))
        selected.dispatch.assert_called_once_with(frozen)


if __name__ == "__main__":
    unittest.main()
