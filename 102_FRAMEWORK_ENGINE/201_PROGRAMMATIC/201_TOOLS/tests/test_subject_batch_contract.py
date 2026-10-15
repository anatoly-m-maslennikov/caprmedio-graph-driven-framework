"""Exact batch packet, recovery checkpoint and repeated lifecycle planning."""

import copy
import unittest

from subject_batch_fixture import SubjectBatchProject
from subject_batch import (
    build_subject_batch_requested_runs,
    load_subject_batch,
    require_git_checkpoint,
)
from lifecycle_intents import LifecycleError, carrier_descriptor


class SubjectBatchContractTests(unittest.TestCase):
    def setUp(self):
        self.project = SubjectBatchProject(self)

    def test_closed_packet_uses_committed_prestate_without_journal_baseline(self):
        project = self.project
        packet = load_subject_batch(project.root, project.parameters)
        require_git_checkpoint(project.root, packet)
        self.assertEqual(project.packet, packet)
        self.assertEqual([], list((project.root / ".caprmedio_caprmedio/_journal").glob("*")))
        self.assertTrue(all("semantic_assessment_report" not in item for item in packet["atoms"]))

    def test_packet_digest_and_each_target_original_are_exact(self):
        project = self.project
        original = project.packet_path.read_bytes()
        project.packet_path.write_bytes(original + b"\n")
        with self.assertRaises(ValueError):
            load_subject_batch(project.root, project.parameters)
        project.packet_path.write_bytes(original)
        path = project.paths[1]
        path.write_bytes(project.before[path] + b"\nconcurrent edit\n")
        with self.assertRaises(ValueError):
            load_subject_batch(project.root, project.parameters)
        with self.assertRaises(ValueError):
            require_git_checkpoint(project.root, project.packet)

    def test_duplicate_and_non_subject_payloads_are_rejected(self):
        project = self.project
        original = copy.deepcopy(project.packet)
        for mutation in ("duplicate", "body", "confirmed", "profile", "target", "patch"):
            with self.subTest(mutation=mutation):
                project.packet = copy.deepcopy(original)
                if mutation == "duplicate":
                    project.packet["atoms"].append(copy.deepcopy(project.packet["atoms"][0]))
                elif mutation == "body":
                    project.packet["atoms"][0]["content"] = "unauthorized body replacement"
                elif mutation == "confirmed":
                    project.packet["confirmed"] = True
                elif mutation == "profile":
                    project.packet["subject_profile"] = "legacy"
                elif mutation == "patch":
                    project.packet["atoms"][0]["subject_patches"][0]["field"] = "content"
                else:
                    project.packet["atoms"][0]["target"]["untrusted"] = True
                project.save_packet()
                with self.assertRaises((ValueError, LifecycleError)):
                    load_subject_batch(project.root, project.parameters)

    def test_checkpoint_cannot_omit_an_untracked_target(self):
        project = self.project
        path = project.golden.status_atom("Requirement", "Active", number=8105)
        project.packet["atoms"][0]["target"] = carrier_descriptor(
            project.root, path.relative_to(project.root).as_posix()
        )
        project.save_packet()
        packet = load_subject_batch(project.root, project.parameters)
        with self.assertRaises(ValueError):
            require_git_checkpoint(project.root, packet)

    def test_one_workflow_declares_real_repeated_mutation_children_only(self):
        _, frozen = self.project.execution()
        self.assertFalse(
            any(
                "subject_intent_sha256" in effect
                for effect in frozen["request"]["execution"]["effects"]
            )
        )
        runs = frozen["request"]["execution"]["requested_runs"]
        self.assertEqual(
            ["CA-O-127", "CA-O-129", "CA-O-128", "CA-O-030", "CA-O-129", "CA-O-128", "CA-O-030"],
            [row["definition"]["atom_id"] for row in runs],
        )
        self.assertEqual(len(runs), len({row["requested_run_id"] for row in runs}))
        self.assertEqual(1, sum(row["kind"] == "workflow" for row in runs))

        large = build_subject_batch_requested_runs(frozen["graph"], "large-subject-batch", 611)
        self.assertEqual(1 + 3 * 611, len(large))
        self.assertEqual(611, sum(row["definition"]["atom_id"] == "CA-O-030" for row in large))


if __name__ == "__main__":
    unittest.main()
