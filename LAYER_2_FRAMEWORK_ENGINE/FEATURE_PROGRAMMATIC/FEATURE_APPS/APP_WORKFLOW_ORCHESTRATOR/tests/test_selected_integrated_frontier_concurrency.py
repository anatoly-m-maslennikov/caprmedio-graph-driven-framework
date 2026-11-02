"""Focused concurrency and crash-resume checks for Integrated frontier state."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import sys
import tempfile
import unittest


APP = Path(__file__).resolve().parents[1]
PROJECT_ROOT = APP.parents[3]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

from selected_integrated_frontier import (  # noqa: E402
    IntegratedFrontierError,
    admit_submission,
    complete_receipt,
    load_pending,
    save_pending,
)
from selected_integrated_frontier_records import digest  # noqa: E402


class IntegratedFrontierConcurrencyTests(unittest.TestCase):
    def setUp(self) -> None:
        parent = PROJECT_ROOT / ".caprmedio_tmp" / "integrated-frontier-concurrency"
        parent.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=parent)
        self.project = Path(self.temporary.name) / "project"
        (self.project / ".git").mkdir(parents=True)
        (self.project / ".caprmedio_tmp").mkdir()
        self.run_id = "integrated-run-concurrent"

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def frontier(self, continuation_id: str) -> dict[str, object]:
        project_root = self.project.resolve().as_posix()
        return {
            "continuation_id": continuation_id,
            "project": {"root": project_root, "digest": digest(project_root)},
            "run": {"id": self.run_id, "digest": "b" * 64},
            "step": {"id": "CA-O-231", "digest": "c" * 64},
            "action": {"id": "CA-O-017", "digest": "d" * 64},
            "request_digest": "e" * 64,
            "source_digest": "f" * 64,
            "packet_digest": "0" * 64,
            "candidate_digest": f"candidate-{continuation_id}",
            "authorization_digest": "1" * 64,
        }

    @staticmethod
    def submission(continuation_id: str, result: str = "completed") -> dict[str, object]:
        result_digest = digest(result)
        return {
            "continuation_id": continuation_id,
            "result": result,
            "result_digest": result_digest,
        }

    def test_concurrent_exact_submission_is_one_use_and_idempotent(self) -> None:
        save_pending(self.project, self.run_id, self.frontier("frontier-a"))
        submission = self.submission("frontier-a")
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(
                pool.map(
                    lambda _item: admit_submission(self.project, self.run_id, submission),
                    range(2),
                )
            )
        self.assertEqual(results[0], results[1])
        self.assertEqual(results[0]["submission"], submission)

    def test_concurrent_next_publication_has_one_cas_winner(self) -> None:
        save_pending(self.project, self.run_id, self.frontier("frontier-a"))
        admit_submission(self.project, self.run_id, self.submission("frontier-a"))

        def publish(continuation_id: str) -> object:
            try:
                save_pending(self.project, self.run_id, self.frontier(continuation_id))
                return continuation_id
            except IntegratedFrontierError as error:
                return error

        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(publish, ("frontier-b", "frontier-c")))
        self.assertEqual(1, sum(isinstance(result, str) for result in results))
        self.assertEqual(1, sum(isinstance(result, IntegratedFrontierError) for result in results))
        self.assertIn(
            load_pending(self.project, self.run_id)["frontier"]["continuation_id"], results
        )

    def test_response_receipt_survives_admit_crash_before_graph_resume(self) -> None:
        save_pending(self.project, self.run_id, self.frontier("frontier-a"))
        submission = self.submission("frontier-a")
        first = admit_submission(self.project, self.run_id, submission)
        retry = admit_submission(self.project, self.run_id, submission)
        self.assertEqual(first, retry)
        self.assertNotIn("response", retry)

        response = {"next_prompt": "continue with the next Step"}
        complete_receipt(self.project, self.run_id, "frontier-a", response)
        resumed = admit_submission(self.project, self.run_id, submission)
        self.assertEqual(response, resumed["response"])
        with self.assertRaises(IntegratedFrontierError):
            complete_receipt(self.project, self.run_id, "frontier-a", {"next_prompt": "tampered"})

    def test_arbitrary_directory_is_not_accepted_as_a_project(self) -> None:
        arbitrary = self.project.parent / "arbitrary"
        arbitrary.mkdir()
        with self.assertRaises(IntegratedFrontierError):
            save_pending(arbitrary, self.run_id, self.frontier("frontier-a"))

    def test_nested_directory_is_not_accepted_as_a_project_root(self) -> None:
        nested = self.project / "nested"
        nested.mkdir()
        with self.assertRaises(IntegratedFrontierError):
            save_pending(nested, self.run_id, self.frontier("frontier-a"))


if __name__ == "__main__":
    unittest.main()
