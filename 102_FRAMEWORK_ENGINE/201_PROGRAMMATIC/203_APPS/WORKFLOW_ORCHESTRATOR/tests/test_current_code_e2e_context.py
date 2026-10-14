"""Plain Docker inputs and the retained sealed adapter, without Docker effects."""

import asyncio
from dataclasses import fields
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock


TESTS = Path(__file__).resolve().parent
RELEASE = TESTS.parents[4] / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION"
sys.path.insert(0, str(RELEASE))
sys.path.insert(0, str(RELEASE / "tests"))

from current_code_e2e_context import load_test_context, narrow_context  # noqa: E402
from release_e2e_context import ReleaseE2EContextError  # noqa: E402
import test_release_e2e_context as sealed_fixture  # noqa: E402
import test_selected_query_mcp_e2e as query_harness  # noqa: E402


class CurrentCodeE2EContextTests(unittest.TestCase):
    def setUp(self):
        self.tmp = TESTS.parents[4] / ".caprmedio_tmp"
        self.tmp.mkdir(exist_ok=True)
        directory = tempfile.TemporaryDirectory(prefix="plain-e2e-context-", dir=self.tmp)
        self.addCleanup(directory.cleanup)
        self.scratch = Path(directory.name)
        self.image = "sha256:" + "a" * 64
        self.environment = {
            "CAPRMEDIO_FIRST_CUT_HTTP_IMAGE": self.image,
            "CAPRMEDIO_FIRST_CUT_HTTP_SCRATCH": str(self.scratch),
        }

    def test_disabled_and_unconfigured_has_no_context(self):
        self.assertIsNone(load_test_context({}, self.tmp))
        self.assertIsNone(load_test_context({"CAPRMEDIO_DOCKER_E2E": "0"}, self.tmp))

    def test_enabled_or_partial_configuration_refuses_instead_of_skip(self):
        cases = [{flag: "1"} for flag in ("CAPRMEDIO_DOCKER_E2E", "CAPRMEDIO_DOCKER_QUERY_E2E")]
        cases += [{key: value} for key, value in self.environment.items()]
        for environment in cases:
            with (
                self.subTest(environment=environment),
                self.assertRaisesRegex(ValueError, "both required"),
            ):
                load_test_context(environment, self.tmp)

    def test_plain_context_contains_only_actual_supplied_test_inputs(self):
        context = load_test_context(self.environment, self.tmp)
        self.assertEqual(self.image, context.candidate_image_digest)
        self.assertEqual(self.scratch.resolve(), context.scratch_root)
        self.assertEqual(
            ["scratch_root", "candidate_image_digest"], [field.name for field in fields(context)]
        )
        self.assertFalse(hasattr(context, "candidate_snapshot_manifest_sha256"))
        self.assertFalse(hasattr(context, "grammar_sha256"))

    def test_mutable_malformed_or_whitespace_images_refuse(self):
        for image in ("latest", "sha256:" + "A" * 64, self.image + "\n"):
            with self.subTest(image=image), self.assertRaisesRegex(ValueError, "immutable digest"):
                narrow_context(
                    dict(self.environment, CAPRMEDIO_FIRST_CUT_HTTP_IMAGE=image), self.tmp
                )

    def test_scratch_must_be_existing_private_child(self):
        file = self.scratch / "file"
        file.write_bytes(b"not a directory")
        for scratch in (self.tmp, self.tmp.parent, file, self.scratch / "absent", Path("relative")):
            with self.subTest(scratch=scratch), self.assertRaises(ValueError):
                narrow_context(
                    dict(self.environment, CAPRMEDIO_FIRST_CUT_HTTP_SCRATCH=str(scratch)), self.tmp
                )

    def test_scratch_symlinks_and_symlink_ancestors_refuse(self):
        child = self.scratch / "child"
        child.mkdir()
        alias = self.scratch / "alias"
        alias.symlink_to(child, target_is_directory=True)
        nested = child / "nested"
        nested.mkdir()
        for scratch in (alias, alias / "nested"):
            with self.subTest(scratch=scratch), self.assertRaisesRegex(ValueError, "non-symlink"):
                narrow_context(
                    dict(self.environment, CAPRMEDIO_FIRST_CUT_HTTP_SCRATCH=str(scratch)), self.tmp
                )

    def test_explicit_sealed_context_keeps_real_loader_and_all_its_fields(self):
        fixture = sealed_fixture.ReleaseE2EContextContractTests()
        fixture.setUp()
        path = fixture.write_context(fixture.golden())
        environment = dict(self.environment, **fixture.environment(path))
        context = load_test_context(environment, self.tmp)
        self.assertEqual(sealed_fixture.MANIFEST, context.candidate_snapshot_manifest_sha256)
        self.assertEqual(
            sealed_fixture.HARNESS_SOURCES, tuple(row.source_path for row in context.harnesses)
        )
        self.assertEqual(str(fixture.scratch_root), context.scratch_root)

    def test_invalid_explicit_sealed_context_cannot_fall_back_to_plain(self):
        environment = dict(
            self.environment, CAPRMEDIO_RELEASE_E2E_CONTEXT=str(self.scratch / "missing.json")
        )
        environment["CAPRMEDIO_CANDIDATE_IMAGE_DIGEST"] = self.image
        with self.assertRaises(ReleaseE2EContextError):
            load_test_context(environment, self.tmp)

    def test_query_image_mismatch_refuses_before_any_docker_call(self):
        context = narrow_context(self.environment, self.tmp)
        case = query_harness.SelectedQueryMcpEndToEnd("runTest")
        with (
            mock.patch.object(query_harness.strict, "E2E_CONTEXT", context),
            mock.patch.dict(os.environ, {"CAPRMEDIO_DOCKER_QUERY_IMAGE": "sha256:" + "b" * 64}),
            mock.patch.object(
                query_harness.subprocess, "run", side_effect=AssertionError("Docker called")
            ),
        ):
            with self.assertRaisesRegex(AssertionError, "query image must equal"):
                asyncio.run(case.asyncSetUp())


if __name__ == "__main__":
    unittest.main()
