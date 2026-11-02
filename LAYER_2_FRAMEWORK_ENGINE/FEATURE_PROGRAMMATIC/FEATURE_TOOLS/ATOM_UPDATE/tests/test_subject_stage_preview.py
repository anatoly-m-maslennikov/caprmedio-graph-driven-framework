"""Independent exact-byte and failure checks for temporary Subject staging."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import stat
import subprocess
import sys
import unittest
import uuid
from pathlib import Path
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOOLS))

import atom_operations as operations  # noqa: E402
import atom_subject_patch as subject_patch  # noqa: E402
import atom_subject_stage as staging  # noqa: E402
import test_nonarchived_subject_preview as preview_fixture  # noqa: E402
from subject_notation import get_profile  # noqa: E402


ILLUSTRATIVE_TIME = "2026-10-12 10:20:30 +0400"
STAGE_PREFIX = Path(".caprmedio_tmp/subject-preview")


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


class SubjectStagePreviewTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = preview_fixture.NonarchivedSubjectPreviewTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.path = self.fixture._plan("Done", number=7801)
        self.original = self.path.read_bytes()
        self.items = self.fixture._payload(self.path)
        history = self.path.parent.parent / "archive" / "CA-P-7799--prior@2.md"
        history.parent.mkdir(parents=True, exist_ok=True)
        history.write_bytes(self.original.replace(b"CA-P-7801", b"CA-P-7799").replace(b"version: 7", b"version: 2"))
        journal = self.root / ".caprmedio_caprmedio/_journal/existing-record.bin"
        journal.parent.mkdir(parents=True)
        journal.write_bytes(b"existing Journal evidence\n")

    def _ledger(self) -> dict[str, tuple[bytes, int]]:
        return {path.relative_to(self.root).as_posix(): (path.read_bytes(), stat.S_IMODE(path.stat().st_mode))
                for path in (self.root / ".caprmedio_caprmedio").rglob("*") if path.is_file()}

    def _stage(self, items=None, *, profile="legacy", timestamp=ILLUSTRATIVE_TIME):
        return staging.stage_subject_preview(self.root, self.items if items is None else items,
                                             timestamp=timestamp, subject_profile=profile)

    def _expected(self, original: bytes, *, new: str = "Atom/State", noop: bool = False) -> bytes:
        if noop:
            return original
        # Independent literal ledger: never use the producer's spans/proposal.
        old_subject = b'  governs: "Atom/Status"'
        old_time = b'updated_at: "2026-01-01 00:00:00 +0000"'
        self.assertEqual(1, original.count(old_subject))
        self.assertEqual(1, original.count(old_time))
        newline = b"\r\n" if b"\r\n" in original else b"\n"
        return (original.replace(old_subject, f'  governs: "{new}"'.encode())
                .replace(b"version: 7" + newline, b"version: 8" + newline)
                .replace(old_time, f'updated_at: "{ILLUSTRATIVE_TIME}"'.encode()))

    def _assert_success(self, result: dict, items: list, expected: list[bytes]) -> dict:
        self.assertEqual({"preview", "staging_only", "illustrative", "sources_unchanged", "stage_root",
                          "manifest_path", "manifest_sha256"}, set(result))
        for flag in ("staging_only", "illustrative", "sources_unchanged"):
            self.assertIs(True, result[flag])
        relative = Path(result["stage_root"])
        self.assertFalse(relative.is_absolute())
        self.assertEqual(STAGE_PREFIX, relative.parent)
        self.assertNotIn("..", relative.parts)
        self.assertEqual(relative / "manifest.json", Path(result["manifest_path"]))
        preview = result["preview"]
        unsigned = {key: value for key, value in preview.items() if key != "preview_sha256"}
        canonical = json.dumps(unsigned, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
        self.assertEqual(sha256(canonical.encode()), preview["preview_sha256"])
        manifest_raw = (self.root / result["manifest_path"]).read_bytes()
        self.assertEqual(sha256(manifest_raw), result["manifest_sha256"])
        manifest = json.loads(manifest_raw)
        self.assertEqual({"schema_version", "preview_sha256", "atoms"}, set(manifest))
        self.assertEqual(1, manifest["schema_version"])
        self.assertEqual(preview["preview_sha256"], manifest["preview_sha256"])
        self.assertEqual(len(items), len(manifest["atoms"]))
        for ordinal, (item, raw, entry, atom) in enumerate(zip(items, expected, manifest["atoms"], preview["atoms"], strict=True), 1):
            candidate = relative / f"{ordinal:04d}" / Path(item["selector"]).name
            self.assertEqual({"source", "subject_intent_sha256", "candidate", "validation"}, set(entry))
            self.assertEqual({"path": item["selector"], **item["expected"]}, entry["source"])
            self.assertEqual(atom["subject_intent_sha256"], entry["subject_intent_sha256"])
            self.assertEqual({"path": candidate.as_posix(), "sha256": sha256(raw)}, entry["candidate"])
            self.assertEqual({"state": "passed", "logical_source_path": item["selector"]}, entry["validation"])
            self.assertEqual(raw, (self.root / candidate).read_bytes())
            self.assertEqual(raw, atom["proposed_carrier"].encode())
            self.assertEqual(sha256(raw), atom["after_sha256"])
            source_raw = (self.root / item["selector"]).read_bytes()
            separator = b"\r\n---\r\n" if b"\r\n" in source_raw else b"\n---\n"
            self.assertEqual(source_raw.split(separator, 1)[1], raw.split(separator, 1)[1])
        return manifest

    def _assert_failure(self, function, *, code=None, staged=True):
        with self.assertRaises(operations.ToolError) as raised:
            function()
        error = raised.exception
        if code is not None:
            self.assertEqual(code, error.code)
        if staged:
            self.assertIs(True, error.details["staging_only"])
            if error.details["stage_root"] is None:
                self.assertEqual([], error.details["retained_artifacts"])
                return error
            stage_root = Path(error.details["stage_root"])
            self.assertEqual(STAGE_PREFIX, stage_root.parent)
            self.assertNotIn("manifest_sha256", error.details)
            for artifact in error.details["retained_artifacts"]:
                relative = Path(artifact["path"])
                self.assertTrue(relative.is_relative_to(stage_root))
                path = self.root / relative
                self.assertTrue(path.exists() or path.is_symlink())
                if "sha256" in artifact:
                    self.assertTrue(stat.S_ISREG(path.lstat().st_mode))
                    self.assertEqual(sha256(path.read_bytes()), artifact["sha256"])
        return error

    def test_exact_multi_target_exports_profiles_line_endings_statuses_and_noop(self) -> None:
        lf = self.fixture._plan("Backlog", number=7802)
        lf.write_bytes(lf.read_bytes().replace(b"\r\n", b"\n"))
        noop = self.fixture._plan("Active", number=7803)
        paths = [self.path, lf, noop]
        items = [self.fixture._payload(path, patches=index != 2)[0] for index, path in enumerate(paths)]
        before = self._ledger()
        expected = [self._expected(path.read_bytes(), noop=index == 2) for index, path in enumerate(paths)]
        roots = []
        real_validator = operations._validate_complete_carrier
        for profile in ("legacy", "approved"):
            original_preview = subject_patch.preview_subject_patches(self.root, items, timestamp=ILLUSTRATIVE_TIME,
                                                                      subject_profile=profile)
            with self.subTest(profile=profile), patch.object(operations, "_validate_complete_carrier", wraps=real_validator) as validator:
                with patch.object(staging, "preview_subject_patches", wraps=subject_patch.preview_subject_patches) as planner:
                    result = self._stage(items, profile=profile)
                self.assertGreaterEqual(planner.call_count, 2)
                self.assertTrue(all(call.kwargs["timestamp"] == ILLUSTRATIVE_TIME for call in planner.call_args_list))
                self._assert_success(result, items, expected)
                self.assertEqual(original_preview, result["preview"])
                self.assertEqual(profile, result["preview"]["subject_profile"])
                for call in validator.call_args_list:
                    self.assertIn(Path(call.args[1]), paths)
                roots.append(result["stage_root"])
        self.assertEqual(2, len(set(roots)))
        self.assertEqual(before, self._ledger())

    def test_default_preview_and_wrapper_remain_write_free_and_identical(self) -> None:
        input_path = self.root / "input.json"
        input_path.write_text(json.dumps({"atoms": self.items}), encoding="utf-8")
        before = self.fixture._snapshot()
        preview = subject_patch.preview_subject_patches(self.root, self.items, timestamp=ILLUSTRATIVE_TIME)
        with patch.object(subject_patch, "_preview_timestamp", return_value=ILLUSTRATIVE_TIME):
            result = operations.run_update(self.root, argparse.Namespace(input=str(input_path), apply=False))
        self.assertEqual(preview, result)
        self.assertEqual(before, self.fixture._snapshot())
        self.assertFalse((self.root / STAGE_PREFIX).exists())

    def test_all_noop_exports_exact_original_without_new_time_or_history(self) -> None:
        items = self.fixture._payload(self.path, patches=False)
        before = self._ledger()
        result = self._stage(items, timestamp=None)
        self._assert_success(result, items, [self.original])
        self.assertTrue(result["preview"]["noop"])
        self.assertIsNone(result["preview"]["illustrative_updated_at"])
        self.assertIsNone(result["preview"]["atoms"][0]["subject_intent"]["predecessorArchive"])
        manifest = json.loads((self.root / result["manifest_path"]).read_bytes())
        candidate = manifest["atoms"][0]["candidate"]
        (self.root / candidate["path"]).write_bytes(self.original + b"\nlater illustrative edit\n")
        self.assertNotEqual(candidate["sha256"], sha256((self.root / candidate["path"]).read_bytes()))
        self.assertEqual(before, self._ledger())

    def test_invalid_pins_and_competing_same_basename_reject_before_staging(self) -> None:
        wrong = copy.deepcopy(self.items)
        wrong[0]["expected"]["sha256"] = "0" * 64
        before = self._ledger()
        self._assert_failure(lambda: self._stage(wrong), code="subject-pin-stale", staged=False)
        self.assertEqual(before, self._ledger())
        duplicate = self.path.parent.parent / "001_backlog" / self.path.name
        duplicate.parent.mkdir()
        duplicate.write_bytes(self.original.replace(b"status: Done", b"status: Backlog"))
        self._assert_failure(self._stage, code="subject-identity-duplicate", staged=False)
        self.assertEqual(self.original, self.path.read_bytes())
        self.assertFalse((self.root / STAGE_PREFIX).exists())

    def test_post_export_source_grammar_identity_and_validation_authority_drift_refuse(self) -> None:
        authority_sources = json.loads((TOOLS / "VALIDATE_ATOMS/validate_atoms_workers/registry.json").read_text())["sources"]
        authority = self.root / authority_sources["CA-D-276"]["source_path"]
        grammar = self.root / get_profile("legacy").grammar_pins[0].path
        duplicate = self.path.parent.parent / "001_backlog" / self.path.name
        for kind, path, code in (("source", self.path, "subject-pin-stale"),
                                 ("grammar", grammar, "subject-grammar-pin-stale"),
                                 ("identity", duplicate, "subject-identity-duplicate"),
                                 ("authority", authority, None)):
            with self.subTest(kind=kind):
                before = self._ledger()
                original = path.read_bytes() if path.exists() else None
                real_write = staging._write_candidate
                injected = False
                injected_bytes = None

                def drift(root, destination, raw):
                    nonlocal injected, injected_bytes
                    result = real_write(root, destination, raw)
                    if destination.name != "manifest.json" and not injected:
                        injected = True
                        path.parent.mkdir(parents=True, exist_ok=True)
                        injected_bytes = (self.original.replace(b"status: Done", b"status: Backlog") if kind == "identity"
                                          else original + b"\nfixture drift\n")
                        path.write_bytes(injected_bytes)
                    return result

                try:
                    with patch.object(staging, "_write_candidate", side_effect=drift):
                        error = self._assert_failure(self._stage, code=code)
                    self.assertTrue(injected)
                    self.assertEqual(injected_bytes, path.read_bytes(), "staging must not roll back an external fixture edit")
                    self.assertFalse((self.root / error.details["stage_root"] / "manifest.json").exists())
                    if kind == "authority":
                        self.assertIn(error.code, {"complete-carrier-invalid", "complete-carrier-authority-unavailable"})
                finally:
                    if original is None:
                        path.unlink(missing_ok=True)
                    else:
                        path.write_bytes(original)
                self.assertEqual(before, self._ledger())

    def test_tampered_or_substituted_candidate_never_returns_a_success_seal(self) -> None:
        before = self._ledger()
        for kind in ("bytes", "inode", "directory", "symlink-readback"):
            with self.subTest(kind=kind):
                real_write = staging._write_candidate

                def replace_candidate(root, destination, raw):
                    result = real_write(root, destination, raw)
                    if destination.name != "manifest.json":
                        if kind == "bytes":
                            destination.write_bytes(raw + b"\nfixture tamper\n")
                        elif kind == "inode":
                            replacement = destination.with_suffix(".replacement")
                            replacement.write_bytes(raw)
                            os.replace(replacement, destination)
                        elif kind == "symlink-readback":
                            destination.unlink()
                            destination.symlink_to(self.path)
                        else:
                            destination.parent.rename(destination.parent.with_name(destination.parent.name + "-retained"))
                            destination.parent.mkdir()
                            destination.write_bytes(raw)
                    return result

                with patch.object(staging, "_write_candidate", side_effect=replace_candidate):
                    self._assert_failure(self._stage, code="subject-stage-write-failed" if kind == "symlink-readback"
                                         else "subject-stage-destination-changed")
                self.assertEqual(before, self._ledger())

    def test_staging_ancestor_symlinks_and_non_directory_paths_do_not_escape(self) -> None:
        outside = self.root / "unapproved-output"
        outside.mkdir()
        sentinel = outside / "sentinel.bin"
        sentinel.write_bytes(b"do not overwrite\n")
        before = self._ledger()
        temporary = self.root / ".caprmedio_tmp"
        for kind in ("ancestor-symlink", "nested-symlink", "ancestor-file"):
            with self.subTest(kind=kind):
                if kind == "nested-symlink":
                    temporary.mkdir()
                    alias = temporary / "subject-preview"
                    alias.symlink_to(outside, target_is_directory=True)
                elif kind == "ancestor-symlink":
                    alias = temporary
                    alias.symlink_to(outside, target_is_directory=True)
                else:
                    alias = temporary
                    alias.write_bytes(b"occupied ancestor\n")
                try:
                    self._assert_failure(self._stage, staged=False)
                    self.assertEqual([sentinel], list(outside.iterdir()))
                    self.assertEqual(b"do not overwrite\n", sentinel.read_bytes())
                    self.assertEqual(before, self._ledger())
                finally:
                    alias.unlink()
                    if kind == "nested-symlink":
                        temporary.rmdir()

    def test_occupied_generated_batch_is_never_reused_or_overwritten(self) -> None:
        batch_id = uuid.UUID(int=1)
        occupied = self.root / STAGE_PREFIX / batch_id.hex
        occupied.mkdir(parents=True)
        sentinel = occupied / "existing.bin"
        sentinel.write_bytes(b"existing generated destination\n")
        before = self._ledger()
        with patch.object(staging.uuid, "uuid4", return_value=batch_id):
            self._assert_failure(self._stage, code="subject-stage-destination-occupied")
        self.assertEqual([sentinel], list(occupied.iterdir()))
        self.assertEqual(b"existing generated destination\n", sentinel.read_bytes())
        self.assertEqual(before, self._ledger())

    def test_candidate_symlink_file_and_manifest_collisions_preserve_existing_bytes(self) -> None:
        before = self._ledger()
        for kind in ("symlink", "file", "manifest"):
            with self.subTest(kind=kind):
                real_write = staging._write_candidate
                occupied = []

                def collide(root, destination, raw):
                    if (destination.name == "manifest.json") == (kind == "manifest"):
                        occupied.append(destination)
                        if kind == "symlink":
                            destination.symlink_to(self.path)
                        else:
                            destination.write_bytes(b"preexisting collision bytes\n")
                    return real_write(root, destination, raw)

                with patch.object(staging, "_write_candidate", side_effect=collide):
                    self._assert_failure(self._stage, code="subject-stage-destination-occupied")
                self.assertEqual(1, len(occupied))
                if kind == "symlink":
                    self.assertTrue(occupied[0].is_symlink())
                else:
                    self.assertEqual(b"preexisting collision bytes\n", occupied[0].read_bytes())
                self.assertEqual(before, self._ledger())

    def test_partial_candidate_write_and_candidate_or_manifest_read_failure_retain_evidence(self) -> None:
        second = self.fixture._plan("Backlog", number=7802)
        items = self.items + self.fixture._payload(second)
        before = self._ledger()
        real_write = os.write
        writes = 0
        shortened = False

        def short_write(descriptor, raw):
            nonlocal shortened
            if not shortened:
                shortened = True
                return real_write(descriptor, raw[:19])
            return real_write(descriptor, raw)

        with patch.object(staging.os, "write", side_effect=short_write):
            self._assert_success(self._stage(items), items, [self._expected(self.original), self._expected(second.read_bytes())])

        def partial(descriptor, raw):
            nonlocal writes
            writes += 1
            if writes == 2:
                real_write(descriptor, raw[:19])
                raise OSError("fixture partial staged write")
            return real_write(descriptor, raw)

        with patch.object(staging.os, "write", side_effect=partial):
            error = self._assert_failure(lambda: self._stage(items), code="subject-stage-write-failed")
        self.assertFalse((self.root / error.details["stage_root"] / "manifest.json").exists())
        self.assertTrue(any(entry.get("sha256") == sha256(self._expected(second.read_bytes())[:19])
                            for entry in error.details["retained_artifacts"]))
        real_read = operations.read_raw_atom_revision
        for kind in ("candidate", "manifest", "candidate-bytes", "manifest-bytes", "late-candidate"):
            with self.subTest(kind=kind):
                corrupted = False

                def unreadable(root, path):
                    nonlocal corrupted
                    is_manifest_case = kind.startswith("manifest") or kind == "late-candidate"
                    if path.is_relative_to(root / STAGE_PREFIX) and (path.name == "manifest.json") == is_manifest_case:
                        if kind in {"candidate", "manifest"}:
                            raise OSError("fixture staged readback unavailable")
                        if not corrupted:
                            corrupted = True
                            raw, fingerprint = real_read(root, path)
                            if kind == "late-candidate":
                                candidate = path.parent / "0001" / self.path.name
                                candidate.write_bytes(candidate.read_bytes() + b"\nlate candidate tamper\n")
                                return raw, fingerprint
                            return raw + b"fixture readback mismatch", fingerprint
                    return real_read(root, path)

                with patch.object(operations, "read_raw_atom_revision", side_effect=unreadable):
                    code = ("subject-stage-destination-changed" if kind == "late-candidate" else
                            "subject-stage-readback-mismatch" if kind.endswith("-bytes") else "subject-stage-write-failed")
                    self._assert_failure(self._stage, code=code)
        self.assertEqual(before, self._ledger())

    def test_unexpected_real_validation_failure_after_export_reports_owned_partial_candidate(self) -> None:
        before = self._ledger()
        real_write = staging._write_candidate
        real_validator = operations._validate_complete_carrier
        exported = failed = False

        def mark_export(root, path, raw):
            nonlocal exported
            result = real_write(root, path, raw)
            exported = True
            return result

        def bounded_authority_failure(*args, **kwargs):
            nonlocal failed
            real_validator(*args, **kwargs)
            if exported and not failed:
                failed = True
                raise RuntimeError("fixture authority resource failure after real validation")

        with patch.object(staging, "_write_candidate", side_effect=mark_export), patch.object(
            operations, "_validate_complete_carrier", side_effect=bounded_authority_failure,
        ):
            error = self._assert_failure(self._stage, code="complete-carrier-authority-unavailable")
        self.assertTrue(failed)
        self.assertTrue(any(entry.get("sha256") == sha256(self._expected(self.original))
                            for entry in error.details["retained_artifacts"]))
        self.assertFalse((self.root / error.details["stage_root"] / "manifest.json").exists())
        self.assertEqual(before, self._ledger())

    def test_post_mkdir_verification_and_uncaptured_identity_report_actual_partial_paths(self) -> None:
        before = self._ledger()
        real_identity = staging._directory_identity
        for depth in (1, 2):
            with self.subTest(created_depth=depth):
                created_path = None

                def failed_verification(root, path):
                    nonlocal created_path
                    identity = real_identity(root, path)
                    if created_path is None and path.is_relative_to(root / STAGE_PREFIX) and len(path.relative_to(root / STAGE_PREFIX).parts) == depth:
                        created_path = path
                        raise RuntimeError("fixture verification failed after real mkdir and identity read")
                    return identity

                with patch.object(staging, "_directory_identity", side_effect=failed_verification):
                    error = self._assert_failure(self._stage, code="subject-stage-write-failed")
                self.assertIsNotNone(created_path)
                self.assertTrue(created_path.is_dir())
                self.assertIn({"path": created_path.relative_to(self.root).as_posix()}, error.details["retained_artifacts"])
                self.assertEqual(before, self._ledger())
        batch_id = uuid.UUID(int=2)
        batch = self.root / STAGE_PREFIX / batch_id.hex
        real_stat = os.stat
        failed = False

        def uncaptured(path, *args, **kwargs):
            nonlocal failed
            if path == batch_id.hex and kwargs.get("dir_fd") is not None and not failed:
                failed = True
                raise OSError("fixture identity capture unavailable after mkdir")
            return real_stat(path, *args, **kwargs)

        with patch.object(staging.uuid, "uuid4", return_value=batch_id), patch.object(staging.os, "stat", side_effect=uncaptured):
            error = self._assert_failure(self._stage, code="subject-stage-write-failed")
        self.assertTrue(failed)
        self.assertTrue(batch.is_dir())
        self.assertEqual([], error.details["retained_artifacts"])
        self.assertEqual([{"path": batch.relative_to(self.root).as_posix(), "state": "unverified"}], error.details["unverified_artifacts"])
        self.assertEqual(before, self._ledger())

    def test_cli_stage_preview_success_is_explicit_and_local_only(self) -> None:
        input_path = self.root / "subject-stage.json"
        input_path.write_text(json.dumps({"atoms": self.items}), encoding="utf-8")
        before = self._ledger()
        completed = subprocess.run([sys.executable, str(TOOLS / "ATOM_UPDATE/atom_update.py"), "--repository", str(self.root),
                                    "run", "--input", str(input_path), "--stage-preview"], capture_output=True, text=True, check=False)
        self.assertEqual(0, completed.returncode, completed.stderr + completed.stdout)
        envelope = json.loads(completed.stdout)
        self.assertTrue(envelope["ok"])
        self.assertEqual("staged-preview", envelope["mode"])
        result = envelope["result"]
        illustrative = result["preview"]["illustrative_updated_at"]
        expected = self._expected(self.original).replace(ILLUSTRATIVE_TIME.encode(), illustrative.encode())
        self._assert_success(result, self.items, [expected])
        self.assertEqual(before, self._ledger())

    def test_cli_and_wrapper_refuse_apply_generic_mixed_and_unknown_payload_before_artifacts(self) -> None:
        generic = {"selector": self.path.relative_to(self.root).as_posix(), "content": "# unrelated replacement\n"}
        cases = (({"atoms": self.items}, ["--apply"]), ({"atoms": [generic]}, []),
                 ({"atoms": [self.items[0], generic]}, []), ({"atoms": self.items, "destination": "caller-chosen"}, []))
        input_path = self.root / "rejected-stage.json"
        before = self._ledger()
        for payload, extra in cases:
            with self.subTest(payload=payload, extra=extra):
                input_path.write_text(json.dumps(payload), encoding="utf-8")
                completed = subprocess.run([sys.executable, str(TOOLS / "ATOM_UPDATE/atom_update.py"), "--repository", str(self.root),
                                            "run", "--input", str(input_path), "--stage-preview", *extra], capture_output=True, text=True, check=False)
                self.assertEqual(2, completed.returncode, completed.stderr + completed.stdout)
                self.assertFalse(json.loads(completed.stdout)["ok"])
                self.assertFalse((self.root / STAGE_PREFIX).exists())
                self.assertEqual(before, self._ledger())
                self._assert_failure(lambda: operations.run_update(self.root, argparse.Namespace(input=str(input_path), apply=bool(extra),
                                                                                                 stage_preview=True)), staged=False)


if __name__ == "__main__":
    unittest.main()
