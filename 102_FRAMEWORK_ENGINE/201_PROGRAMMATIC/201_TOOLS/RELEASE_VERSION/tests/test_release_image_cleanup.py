"""Bounded fake-Docker cleanup coverage; no actual promotion or image proof."""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

import release_image as images  # noqa: E402
from release_contract import canonical_json  # noqa: E402
from release_promotion import NativePromotionEvidence  # noqa: E402


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class CleanupDocker:
    """Only immutable inventory/inspection/removal; never a real Docker call."""

    def __init__(self, root: Path, listed: list[str], bindings: dict[str, tuple[str, str]]):
        self.root = root
        self.listed = list(listed)
        self.bindings = bindings
        self.calls = []
        self.removed = set()
        self.containers = {}
        self.timeout_removal = set()

    def run(self, argv, *, cwd, timeout_seconds):
        argv = tuple(argv)
        if cwd != self.root or timeout_seconds != 30:
            raise AssertionError("cleanup changed its fixed root or bounded timeout")
        self.calls.append(argv)
        result = images.DockerCommandResult
        if argv == ("docker", "image", "ls", "--all", "--quiet", "--no-trunc"):
            return result(0, ("\n".join(image for image in self.listed if image not in self.removed) + "\n").encode(), b"")
        if argv[:3] == ("docker", "image", "inspect"):
            image = argv[3]
            if image in self.removed:
                return result(1, b"[]", f"Error: No such image: {image}".encode())
            candidate, context = self.bindings[image]
            return result(0, json.dumps([{"Id": image, "Config": {"Labels": {
                images.CANDIDATE_LABEL: candidate, images.CONTEXT_LABEL: context,
            }}}]).encode(), b"")
        if argv == ("docker", "container", "ls", "--all", "--quiet", "--no-trunc"):
            return result(0, "\n".join(self.containers).encode(), b"")
        if argv[:3] == ("docker", "container", "inspect"):
            return result(0, json.dumps([{"Id": identity, "Image": self.containers[identity],
                                          "State": {"Status": "exited"}} for identity in argv[3:]]).encode(), b"")
        if argv[:3] == ("docker", "image", "rm") and len(argv) == 4:
            image = argv[3]
            if image in self.timeout_removal:
                return result(None, b"", b"CLI timeout; daemon effect unknown", True)
            self.removed.add(image)
            return result(0, f"Deleted: {image}\n".encode(), b"")
        raise AssertionError(f"unexpected cleanup command {argv!r}")


class ReleaseImageCleanupTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.candidate_sha = "a" * 64
        self.prior_sha = "b" * 64
        self.context_sha = "c" * 64
        self.current_image = "sha256:" + "1" * 64
        self.prior_image = "sha256:" + "2" * 64
        self.unrelated_image = "sha256:" + "3" * 64
        settings = b'[release_version.rollback_retention]\ncondition = "until_verified_promotion"\nrequired_image_digests = []\n'
        self.settings_path = self.root / images.FRAMEWORK_SETTINGS_RELATIVE
        self.settings_path.parent.mkdir(parents=True)
        self.settings_path.write_bytes(settings)
        self.candidate = SimpleNamespace(manifest=SimpleNamespace(
            sha256=self.candidate_sha, framework_settings_digest=digest(settings),
        ))
        self.compilation, self.suite, self.build, self.verification = (object() for _ in range(4))
        self.e2e, self.full_gate, self.prepared_package = (object() for _ in range(3))
        # Typed branch-selection input only. The native verifier below is
        # mocked; this fixture is explicitly not an admitted promotion proof.
        self.promotion = NativePromotionEvidence(
            candidate_snapshot_manifest_sha256=self.candidate_sha, outcome="promoted", reason="fixture",
            candidate_image_digest=self.current_image, prior_image_digest=self.prior_image, prior_release="N",
            package_manifest_sha256="d" * 64, full_gate_receipt_sha256="e" * 64,
            framework_version="N+1", version_toml_sha256="f" * 64,
            action_run_id="fixture-action", action_start_event_id="fixture-start",
            installation_command_sha256="4" * 64, target_project_context_sha256="5" * 64,
            state_generation=1, evidence_root="fixture", retained_prior_selector_ref="fixture-selector",
            receipt_sha256="6" * 64,
        )
        self.bindings = {self.current_image: (self.candidate_sha, self.context_sha),
                         self.prior_image: (self.prior_sha, self.context_sha)}
        # Deliberately omit the candidate's historical build receipt: the
        # selected candidate remains protected even without cleanup ownership.
        attempt = images._attempt(self.root, self.prior_sha, "build")
        # Use exactly the production writer's shape (stored checksum is null;
        # the returned evidence carries the hash of those stored bytes).
        # This synthetic receipt tests ownership parsing, not live build proof.
        build_evidence = images.ImageBuildEvidence(
            candidate_snapshot_manifest_sha256=self.prior_sha, outcome="built", reason="fixture build receipt",
            candidate_image_digest=self.prior_image, context_root="fixture-context", context_sha256=self.context_sha,
            package_manifest_sha256="d" * 64, suite_receipt_sha256="e" * 64,
            evidence_root=attempt.relative_to(self.root).as_posix(), commands_sha256=digest(canonical_json([])),
            execution_kind="docker-subprocess",
        )
        recorded = images._record(attempt, build_evidence)
        self.build_receipt_path = attempt / "receipt.json"
        self.assertEqual(recorded.receipt_sha256, digest(self.build_receipt_path.read_bytes()))
        self.assertIsNone(json.loads(self.build_receipt_path.read_bytes())["receipt_sha256"])

    def cleanup(self, docker: CleanupDocker):
        with patch("release_promotion.verify_native_promotion_evidence", return_value=self.root) as native_verify, \
             patch("release_promotion.verify_bound_promotion_evidence", side_effect=AssertionError("legacy promotion verifier used")):
            evidence = images.cleanup_superseded_release_images(
                self.candidate, self.compilation, self.suite, self.build, self.verification, self.promotion,
                e2e=self.e2e, full_gate=self.full_gate, executor=docker, timeout_seconds=30,
                prepared_package=self.prepared_package,
            )
        self.assertEqual(native_verify.call_count, 2)
        for call in native_verify.call_args_list:
            self.assertEqual(call.args, (self.candidate, self.compilation, self.suite, self.build,
                                         self.verification, self.promotion))
            self.assertEqual(call.kwargs, {"e2e": self.e2e, "full_gate": self.full_gate,
                                           "prepared_package": self.prepared_package})
        report_path = self.root / evidence.report_ref
        report = json.loads(report_path.read_bytes())
        receipt_bytes = (report_path.parent / "receipt.json").read_bytes()
        receipt = json.loads(receipt_bytes)
        self.assertEqual(evidence.receipt_sha256, digest(receipt_bytes))
        self.assertEqual(receipt["outcome"], evidence.outcome)
        self.assertEqual(receipt["report_ref"], evidence.report_ref)
        self.assertEqual(report["candidate_snapshot_manifest_sha256"], self.candidate_sha)
        self.assertEqual(len(report["commands"]), len(docker.calls))
        return evidence, report, report_path.parent

    def test_native_cleanup_deduplicates_ids_protects_candidate_and_records_exact_nonforce_removal(self) -> None:
        docker = CleanupDocker(self.root, [self.current_image, self.prior_image, self.prior_image, self.unrelated_image], self.bindings)
        evidence, report, attempt = self.cleanup(docker)
        self.assertEqual(evidence.outcome, "cleaned")
        self.assertEqual(report["items"], [{"image": self.current_image, "outcome": "candidate_protected"},
                                          {"image": self.prior_image, "outcome": "removed"},
                                          {"image": self.unrelated_image, "outcome": "excluded_unproven"}])
        self.assertEqual([call for call in docker.calls if call[:3] == ("docker", "image", "rm")],
                         [("docker", "image", "rm", self.prior_image)])
        self.assertEqual(docker.removed, {self.prior_image})
        self.assertNotIn(("docker", "image", "inspect", self.current_image), docker.calls)
        self.assertNotIn(("docker", "image", "inspect", self.unrelated_image), docker.calls)
        intent = json.loads((attempt / f"removal-{self.prior_image.removeprefix('sha256:')}.json").read_bytes())
        self.assertEqual(intent, {"schema": "caprmedio.release_version.image_cleanup_intent.v1",
                                  "image": self.prior_image, "candidate": self.candidate_sha,
                                  "promotion": self.promotion.receipt_sha256})
        self.assertEqual(docker.calls[-2:], [("docker", "image", "inspect", self.prior_image),
                                           ("docker", "image", "ls", "--all", "--quiet", "--no-trunc")])

    def test_unrelated_or_mismatched_proof_is_retained_without_removal_intent(self) -> None:
        bindings = {**self.bindings, self.prior_image: ("0" * 64, self.context_sha)}
        docker = CleanupDocker(self.root, [self.current_image, self.prior_image, self.unrelated_image], bindings)
        evidence, report, attempt = self.cleanup(docker)
        self.assertEqual(evidence.outcome, "incomplete")
        self.assertEqual({row["image"]: row["outcome"] for row in report["items"]}, {
            self.current_image: "candidate_protected", self.prior_image: "unproven", self.unrelated_image: "excluded_unproven",
        })
        self.assertFalse(docker.removed)
        self.assertFalse(list(attempt.glob("removal-*.json")))
        self.assertNotIn(("docker", "image", "inspect", self.unrelated_image), docker.calls)

    def test_stopped_container_retains_receipt_proven_image(self) -> None:
        docker = CleanupDocker(self.root, [self.current_image, self.prior_image], self.bindings)
        container = "7" * 64
        docker.containers[container] = self.prior_image
        evidence, report, attempt = self.cleanup(docker)
        self.assertEqual(evidence.outcome, "incomplete")
        self.assertEqual(report["items"][1], {"image": self.prior_image, "outcome": "in_use", "containers": [container]})
        self.assertFalse(docker.removed)
        self.assertFalse(list(attempt.glob("removal-*.json")))

    def test_removal_timeout_is_unknown_not_a_successful_cleanup(self) -> None:
        docker = CleanupDocker(self.root, [self.current_image, self.prior_image], self.bindings)
        docker.timeout_removal.add(self.prior_image)
        evidence, report, attempt = self.cleanup(docker)
        self.assertEqual(evidence.outcome, "effect_uncertain")
        self.assertEqual(report["items"][1], {"image": self.prior_image, "outcome": "uncertain"})
        removal = [row for row in report["commands"] if row["argv"][:3] == ["docker", "image", "rm"]]
        self.assertEqual(len(removal), 1)
        self.assertIsNone(removal[0]["exit_code"])
        self.assertTrue(removal[0]["timed_out"])
        self.assertFalse(docker.removed)
        self.assertTrue(list(attempt.glob("removal-*.json")))

    def test_real_build_receipt_writer_shape_proves_ownership_but_changed_binding_does_not(self) -> None:
        self.assertEqual(images._retained_owned_images(self.root), {
            self.prior_image: (self.prior_sha, self.context_sha),
        })
        original = json.loads(self.build_receipt_path.read_bytes())
        for changed in ({"candidate_snapshot_manifest_sha256": "0" * 64},
                        {"unexpected": "not a producer field"}, {"receipt_sha256": "9" * 64}):
            with self.subTest(changed=changed):
                self.build_receipt_path.write_bytes(canonical_json({**original, **changed}))
                self.assertEqual(images._retained_owned_images(self.root), {})

    def test_required_image_or_explicit_prior_retention_never_creates_removal_intent(self) -> None:
        for condition, required in (("until_verified_promotion", [self.prior_image]), ("retain_prior", [])):
            with self.subTest(condition=condition):
                settings = (f'[release_version.rollback_retention]\ncondition = "{condition}"\n'
                            f'required_image_digests = {json.dumps(required)}\n').encode()
                self.settings_path.write_bytes(settings)
                self.candidate.manifest.framework_settings_digest = digest(settings)
                docker = CleanupDocker(self.root, [self.current_image, self.prior_image], self.bindings)
                evidence, report, attempt = self.cleanup(docker)
                self.assertEqual(evidence.outcome, "incomplete")
                self.assertEqual(report["items"][1]["outcome"], "protected")
                self.assertTrue(report["items"][1]["references"])
                self.assertFalse(docker.removed)
                self.assertFalse(list(attempt.glob("removal-*.json")))


if __name__ == "__main__":
    unittest.main()
