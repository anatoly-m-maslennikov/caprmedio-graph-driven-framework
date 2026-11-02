"""Release metadata comes from the owning repository and canonical selection."""

from pathlib import Path
import subprocess
from types import SimpleNamespace
import unittest
from unittest.mock import Mock

import test_simple_local_release as fixtures
from local_release import run_local_release
from release_image_provenance import release_image_provenance


class ReleaseImageProvenanceTests(unittest.TestCase):
    def test_owner_name_and_full_head_are_observed_from_owning_root(self) -> None:
        root = Path("/owning-repository")
        selection = SimpleNamespace(
            instance_id="c" * 64,
            control_relative=Path(".caprmedio_caprmedio"),
            settings={"project": {"name": "Named Project"}},
        )
        runner = Mock(return_value=subprocess.CompletedProcess([], 0, "d" * 40 + "\n", ""))
        metadata = release_image_provenance(root, selection, runner)
        runner.assert_called_once_with(("git", "rev-parse", "--verify", "HEAD"), root)
        self.assertEqual(
            metadata,
            {
                "project_id": "c" * 64,
                "project_root": str(root),
                "control_root": ".caprmedio_caprmedio",
                "project_name": "Named Project",
                "head_commit": "d" * 40,
            },
        )

    def test_missing_name_bad_head_and_failed_git_refuse(self) -> None:
        selection = SimpleNamespace(
            instance_id="c" * 64,
            control_relative=Path(".caprmedio_caprmedio"),
            settings={"project": {"name": "Named Project"}},
        )
        for status, output in ((0, "short-sha"), (1, "d" * 40), (0, "")):
            with self.subTest(status=status, output=output), self.assertRaises(ValueError):
                release_image_provenance(
                    Path("/owner"),
                    selection,
                    Mock(return_value=subprocess.CompletedProcess([], status, output, "")),
                )
        selection.settings = {"project": {"name": ""}}
        runner = Mock()
        with self.assertRaises(ValueError):
            release_image_provenance(Path("/owner"), selection, runner)
        runner.assert_not_called()

    def test_native_runner_passes_owning_provenance_only_to_candidate_build(self) -> None:
        fixture = fixtures.SimpleLocalReleaseTests("runTest")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)

        def runner(argv: tuple[str, ...], root: Path) -> subprocess.CompletedProcess[str]:
            return subprocess.CompletedProcess(argv, 0, "", "")

        with fixture._compiler():
            result = run_local_release(fixture.root, run_id="provenance", runner=runner)
        self.assertEqual(result["outcome"], "completed")
        fixture.provenance.assert_called_once()
        self.assertEqual(fixture.provenance.call_args.args[0], fixture.root)
        self.assertEqual(
            fixture.image_factory.call_args_list[0].kwargs["build_provenance"],
            fixture.provenance.return_value,
        )
        self.assertNotIn("build_provenance", fixture.image_factory.call_args_list[1].kwargs)

    def test_unavailable_head_stops_before_candidate_build(self) -> None:
        fixture = fixtures.SimpleLocalReleaseTests("runTest")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        fixture.provenance.side_effect = ValueError("HEAD unavailable")

        def runner(argv: tuple[str, ...], root: Path) -> subprocess.CompletedProcess[str]:
            return subprocess.CompletedProcess(argv, 0, "", "")

        with fixture._compiler():
            result = run_local_release(fixture.root, run_id="no-head", runner=runner)
        self.assertEqual(result["failed_step"], "prepare_candidate_image")
        fixture.image_factory.assert_not_called()

    def test_build_head_observation_follows_initial_commit_in_owning_repository(self) -> None:
        fixture = fixtures.SimpleLocalReleaseTests("runTest")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        fixture.provenance.side_effect = release_image_provenance
        calls: list[tuple[str, ...]] = []
        dirty = True
        head = "d" * 40

        def runner(argv: tuple[str, ...], root: Path) -> subprocess.CompletedProcess[str]:
            nonlocal dirty, head
            self.assertEqual(root, fixture.root)
            calls.append(argv)
            if argv == ("git", "diff", "--cached", "--quiet"):
                return subprocess.CompletedProcess(argv, int(dirty), "", "")
            if argv[:2] == ("git", "commit"):
                dirty, head = False, "e" * 40
            return subprocess.CompletedProcess(
                argv, 0, head if argv[:3] == ("git", "rev-parse", "--verify") else "", ""
            )

        with fixture._compiler():
            result = run_local_release(fixture.root, run_id="post-commit-head", runner=runner)
        self.assertEqual(result["outcome"], "completed")
        commit = next(index for index, argv in enumerate(calls) if argv[:2] == ("git", "commit"))
        observe = calls.index(("git", "rev-parse", "--verify", "HEAD"))
        self.assertLess(commit, observe)
        metadata = fixture.image_factory.call_args_list[0].kwargs["build_provenance"]
        self.assertEqual(metadata["head_commit"], "e" * 40)
        self.assertEqual(metadata["project_root"], str(fixture.root))


if __name__ == "__main__":
    unittest.main()
