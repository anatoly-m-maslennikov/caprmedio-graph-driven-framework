"""Source-bound direct preparation over the real registered MCP protocol."""

from __future__ import annotations

from contextlib import asynccontextmanager
import copy
import hashlib
import json
from pathlib import Path
import shutil
import stat
import sys
import unittest
from unittest.mock import patch

from mcp.client._memory import InMemoryTransport
from mcp.client.session import ClientSession


MCP_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = MCP_ROOT.parent / "201_TOOLS"
REPOSITORY = MCP_ROOT.parents[2]
NATIVE_TESTS = TOOLS_ROOT / "ATOM_UPDATE/tests"
for directory in (MCP_ROOT, TOOLS_ROOT, NATIVE_TESTS, TOOLS_ROOT / "VALIDATE_ATOMS"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import implementation_server  # noqa: E402
import atom_operations as operations  # noqa: E402
import atom_subject_patch as subject_patch  # noqa: E402
import atom_subject_stage as staging  # noqa: E402
import test_nonarchived_subject_preview as native_fixture  # noqa: E402
from subject_notation import get_profile  # noqa: E402


STAGE_PREFIX = Path(".caprmedio_tmp/subject-preview")
TOOL_WORKFLOWS = (
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/306_FEATURE_TOOL_WORKFLOWS/"
)
# Current preparation sources retain plain logging and the host-owned Subject dispatch contract.
PREPARATION_PINS = tuple({"atom_id": atom_id, "version": version,
                          "path": TOOL_WORKFLOWS + relative, "sha256": digest}
                         for atom_id, version, relative, digest in (
    ("CA-R-866", 26,
     "04_requirement/CA-R-866-TOOL_WORKFLOWS-STANDARD-REQUIREMENT--update-caprmedio-markdown-atoms.md",
     "ef34d271cdf1fac68cec3ee5df48937396f3485cadf107ca46b9b1c32e883146"),
    ("CA-R-1093", 12,
     "04_requirement/CA-R-1093-TOOL_WORKFLOWS-CORE-REQUIREMENT--separate-generic-and-atom-specific-tool-authority.md",
     "089aef0c7af39cd3135b411b5629ee32e350f35beae53a5dbd85754cb50f53e4"),
    ("CA-O-030", 19,
     "09_operations/CA-O-030-TOOL_WORKFLOWS-STANDARD-ACTION--update-sealed-caprmedio-atom-carriers.md",
     "14b8423f542af6d12a2f40a7ca4cdf3a343c7ea14ebc6bdecc16c01a69a28453"),
    ("CA-M-371", 12,
     "05_method/CA-M-371-TOOL_WORKFLOWS-STANDARD-METHOD--preview-exact-subject-patches.md",
     "f0f4a2aa25de2d6b04061a65b7606101410cd9f56ccfe81567f323c6dc99b04d"),
    ("CA-D-425", 16,
     "07_delivery/CA-D-425-TOOL_WORKFLOWS-STANDARD-DELIVERY--deliver-atom-update-tool.md",
     "208431f44e901ed023f45c80536a92ab63e7c046ff45f56dede0f091c8bc7023"),
    ("CA-E-304", 25,
     "06_evaluation/CA-E-304-TOOL_WORKFLOWS-STANDARD-QA_CASE--verify-update-sealed-caprmedio-atom-carriers.md",
     "79f5eb5b9e73fe1907a8b923c1ea9443a11def5f1d21eaea0e0393644bd0b2c3"),
))


def _digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _sealed(value: dict) -> str:
    return _digest(json.dumps(value, sort_keys=True, separators=(",", ":"),
                              ensure_ascii=False, allow_nan=False).encode("utf-8"))


def _snapshot(root: Path) -> dict[str, tuple]:
    result = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix()
        mode = stat.S_IMODE(path.lstat().st_mode)
        if path.is_symlink():
            result[relative] = ("symlink", str(path.readlink()), mode)
        elif path.is_dir():
            result[relative] = ("directory", mode)
        else:
            result[relative] = ("file", path.read_bytes(), mode)
    return result


class DirectSubjectPreparationProtocolTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.assertEqual(6, len(PREPARATION_PINS), "accepted preparation source pins are not ready")
        self.fixture = native_fixture.NonarchivedSubjectPreviewTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.assertTrue(self.root.is_relative_to(REPOSITORY / ".caprmedio_tmp"))
        for pin in PREPARATION_PINS:
            source = REPOSITORY / pin["path"]
            raw = source.read_bytes()
            self.assertEqual(pin["sha256"], _digest(raw), f"accepted pin is stale: {pin['atom_id']}")
            metadata = operations.parse_carrier(raw, source).metadata
            self.assertEqual((pin["atom_id"], pin["version"]), (metadata["atom_id"], metadata["version"]))
            destination = self.root / pin["path"]
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
        self.path = self.fixture._plan("Done", number=9500)
        self.second = self.fixture._plan("Backlog", number=9501)
        self.second.write_bytes(self.second.read_bytes().replace(b"\r\n", b"\n"))
        self.settings = self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        self.request = {
            "operation": "preview_subjects", "subject_profile": "approved",
            "atoms": [self._item(self.path), self._item(self.second)],
        }
        self.originals = {path: path.read_bytes() for path in (self.path, self.second)}
        self.excluded = self.path.parent.parent / "01_concern/CA-C-9599--unrelated-malformed.md"
        self.excluded.parent.mkdir(parents=True)
        self.excluded.write_bytes(b"---\natom_id: [unrelated\nsubjects: [broken\n---\n")
        journal = self.root / ".caprmedio_caprmedio/_journal/existing-record.bin"
        journal.parent.mkdir(parents=True, exist_ok=True)
        journal.write_bytes(b"Existing canonical Journal evidence.\n")

    def _item(self, path, *, noop=False):
        raw = path.read_bytes()
        metadata = operations.parse_carrier(raw, path).metadata
        patches = [] if noop else [
            {"field": "governs", "old": "Atom/Status", "new": "Atom.State"},
            {"field": "depends_on", "operation": "replace_set", "old": ["Atom", "Atom/Revision"],
             "new": ["Atom.State"]},
        ]
        return {"atom_id": metadata["atom_id"], "version": metadata["version"],
                "sha256": _digest(raw), "subject_patches": patches}

    @asynccontextmanager
    async def _session(self):
        before = _snapshot(self.root)
        server = implementation_server.create_server(self.root)
        self.assertEqual(before, _snapshot(self.root), "registration itself must not prepare/stage")
        async with InMemoryTransport(server, raise_exceptions=True) as streams:
            async with ClientSession(*streams) as session:
                await session.initialize()
                yield session

    async def _call(self, session, request, *, pure=False):
        before = _snapshot(self.root)
        response = await session.call_tool("atom_update", {"request": copy.deepcopy(request)})
        if pure:
            self.assertEqual(before, _snapshot(self.root), "Preview/refusal changed files or membership")
        return response

    def _result(self, response, operation):
        self.assertFalse(response.is_error, response)
        result = response.structured_content
        self.assertEqual({"operation", "preview", "staging", "errors"}, set(result))
        self.assertEqual(operation, result["operation"])
        return result

    def _refusal(self, response, operation):
        result = self._result(response, operation)
        self.assertIsNone(result["preview"])
        self.assertIsNone(result["staging"])
        self.assertTrue(result["errors"])
        for error in result["errors"]:
            self.assertEqual({"code", "message", "stage_root", "retained_artifacts", "unverified_artifacts"},
                             set(error))
        return result

    def _preview(self, response):
        result = self._result(response, "preview_subjects")
        self.assertEqual([], result["errors"])
        self.assertIsNone(result["staging"])
        preview = result["preview"]
        self.assertEqual({"count", "atoms", "noop", "illustrative_updated_at", "subject_profile",
                          "subject_profile_evidence", "preview_sha256"}, set(preview))
        self.assertEqual(preview["preview_sha256"], _sealed({key: value for key, value in preview.items()
                                                          if key != "preview_sha256"}))
        for atom in preview["atoms"]:
            self.assertEqual(atom["subject_intent_sha256"], _sealed(atom["subject_intent"]))
            archive = atom["subject_intent"]["predecessorArchive"]
            if archive is not None:
                self.assertFalse((self.root / archive["path"]).exists(), "planned archive is not an actual effect")
        return preview

    @staticmethod
    def _stage_request(request, preview):
        return {**copy.deepcopy(request), "operation": "stage_subjects",
                "preview_sha256": preview["preview_sha256"],
                "illustrative_updated_at": preview["illustrative_updated_at"]}

    def _expected_candidate(self, original, preview, *, noop=False):
        if noop:
            return original
        newline = b"\r\n" if b"\r\n" in original else b"\n"
        return (original.replace(b'  governs: "Atom/Status"', b'  governs: "Atom.State"', 1)
                .replace(b'  depends_on: [Atom, "Atom/Revision"]', b'  depends_on: ["Atom.State"]', 1)
                .replace(b"version: 7" + newline, b"version: 8" + newline, 1)
                .replace(b'updated_at: "2026-01-01 00:00:00 +0000"',
                         f'updated_at: "{preview["illustrative_updated_at"]}"'.encode(), 1))

    def _scratch_only(self, before):
        after = _snapshot(self.root)
        for relative, value in before.items():
            self.assertEqual(value, after.get(relative), f"staging changed an existing entry: {relative}")
        for relative in set(after) - set(before):
            path = Path(relative)
            self.assertTrue(path.is_relative_to(STAGE_PREFIX) or path == STAGE_PREFIX.parent,
                            f"new effect outside scratch prefix: {relative}")

    def _stage(self, response, preview, before):
        result = self._result(response, "stage_subjects")
        self.assertEqual([], result["errors"])
        self.assertEqual(preview, result["preview"], "Stage must use the earlier sealed preview unchanged")
        stage = result["staging"]
        self.assertEqual({"staging_only", "illustrative", "sources_unchanged", "stage_root",
                          "manifest_path", "manifest_sha256"}, set(stage))
        for flag in ("staging_only", "illustrative", "sources_unchanged"):
            self.assertIs(True, stage[flag])
        batch = Path(stage["stage_root"])
        self.assertEqual(STAGE_PREFIX, batch.parent)
        self.assertRegex(batch.name, r"^[0-9a-f]{32}$")
        self.assertEqual(batch / "manifest.json", Path(stage["manifest_path"]))
        raw = (self.root / stage["manifest_path"]).read_bytes()
        self.assertEqual(stage["manifest_sha256"], _digest(raw))
        manifest = json.loads(raw)
        self.assertEqual({"schema_version", "preview_sha256", "atoms"}, set(manifest))
        self.assertEqual(preview["preview_sha256"], manifest["preview_sha256"])
        self.assertEqual(len(preview["atoms"]), len(manifest["atoms"]))
        for atom, record in zip(preview["atoms"], manifest["atoms"], strict=True):
            candidate = self.root / record["candidate"]["path"]
            self.assertTrue(candidate.is_relative_to(self.root / batch))
            candidate_raw = candidate.read_bytes()
            self.assertEqual(atom["proposed_carrier"].encode(), candidate_raw)
            self.assertEqual(atom["after_sha256"], _digest(candidate_raw))
            self.assertEqual(_digest(candidate_raw), record["candidate"]["sha256"])
            self.assertEqual(0o600, stat.S_IMODE(candidate.stat().st_mode))
            self.assertEqual({"state": "passed", "logical_source_path": atom["selector"]}, record["validation"])
            source = self.root / atom["selector"]
            self.assertEqual(self.originals[source], source.read_bytes())
            frontmatter, body = subject_patch._raw_frontmatter(operations, candidate_raw.decode())
            operations._validate_complete_carrier(self.root, source, frontmatter, body, creating=False)
        self._scratch_only(before)
        return stage

    async def test_registered_schema_has_only_two_preparation_operations_and_truthful_hints(self):
        async with self._session() as session:
            tools = (await session.list_tools()).tools
            matches = [tool for tool in tools if tool.name == "atom_update"]
            self.assertEqual(1, len(matches))
            tool = matches[0]
            self.assertEqual({"request"}, set(tool.input_schema["properties"]))
            serialized = json.dumps(tool.input_schema)
            self.assertIn("preview_subjects", serialized)
            self.assertIn("stage_subjects", serialized)
            self.assertIn("preview_sha256", serialized)
            self.assertIn("illustrative_updated_at", serialized)
            self.assertFalse(tool.annotations.read_only_hint)
            self.assertFalse(tool.annotations.destructive_hint)
            self.assertFalse(tool.annotations.idempotent_hint)
            self.assertFalse(tool.annotations.open_world_hint)

    async def test_preview_changed_fullset_and_noop_preserve_exact_sources_and_history(self):
        async with self._session() as session:
            preview = self._preview(await self._call(session, self.request, pure=True))
            self.assertEqual(2, preview["count"])
            for path, atom in zip((self.path, self.second), preview["atoms"], strict=True):
                original = self.originals[path]
                self.assertEqual(self._expected_candidate(original, preview), atom["proposed_carrier"].encode())
                self.assertEqual(7, atom["before_version"])
                self.assertEqual(8, atom["proposed_version"])
                self.assertIn(b"status: " + (b"Done" if path == self.path else b"Backlog"),
                              atom["proposed_carrier"].encode())
            noop_request = {**self.request, "atoms": [self._item(self.path, noop=True)]}
            noop = self._preview(await self._call(session, noop_request, pure=True))
            self.assertTrue(noop["noop"])
            self.assertIsNone(noop["illustrative_updated_at"])
            self.assertEqual(self.originals[self.path], noop["atoms"][0]["proposed_carrier"].encode())
        self.assertFalse((self.root / STAGE_PREFIX).exists())

    async def test_invalid_and_stale_batch_requests_refuse_before_any_scratch_creation(self):
        invalid = []
        for delta in ({"selector": "anything.md"}, {"destination": "outside"}, {"apply": True},
                      {"session_id": "invented"}, {"operation": "publish"}, {"subject_profile": "unknown"}):
            invalid.append({**self.request, **delta})
        duplicate = copy.deepcopy(self.request)
        duplicate["atoms"].append(copy.deepcopy(duplicate["atoms"][0]))
        invalid.append(duplicate)
        for field, value in (("version", True), ("sha256", "A" * 64), ("atom_id", "9500")):
            request = copy.deepcopy(self.request)
            request["atoms"][0][field] = value
            invalid.append(request)
        index = copy.deepcopy(self.request)
        index["atoms"][0]["subject_patches"][0]["index"] = 0
        invalid.append(index)
        unsupported = copy.deepcopy(self.request)
        unsupported["atoms"][0]["subject_patches"] = [{"field": "depends_on", "operation": "add", "new": "Other"}]
        invalid.append(unsupported)
        async with self._session() as session:
            for request in invalid:
                with self.subTest(request=request):
                    self.assertTrue((await self._call(session, request, pure=True)).is_error)
            for kind in ("pin", "old-set", "overlap"):
                request = copy.deepcopy(self.request)
                if kind == "pin":
                    request["atoms"][-1]["sha256"] = "0" * 64
                elif kind == "old-set":
                    request["atoms"][-1]["subject_patches"][1]["old"] = ["Missing"]
                else:
                    request["atoms"][-1]["subject_patches"].append(
                        {"field": "depends_on", "old": "Atom", "new": "Other"})
                with self.subTest(kind=kind):
                    self._refusal(await self._call(session, request, pure=True), "preview_subjects")
        self.assertFalse((self.root / STAGE_PREFIX).exists())

    async def test_ambiguous_selected_identity_and_source_or_grammar_drift_refuse(self):
        async with self._session() as session:
            before = self.excluded.read_bytes()
            try:
                self.excluded.write_bytes(b"---\natom_id: CA-P-9500\nsubjects: [broken\n---\n")
                self._refusal(await self._call(session, self.request, pure=True), "preview_subjects")
            finally:
                self.excluded.write_bytes(before)
            for target in (self.path, self.root / get_profile("approved").grammar_pins[0].path):
                original = target.read_bytes()
                try:
                    target.write_bytes(original + b"\nExternal source drift.\n")
                    self._refusal(await self._call(session, self.request, pure=True), "preview_subjects")
                finally:
                    target.write_bytes(original)
            hidden = self.root / "hidden-competing-original"
            hidden.mkdir()
            (hidden / self.path.name).write_bytes(self.originals[self.path])
            shadow = self.path.parent.parent / "shadow"
            shadow.mkdir()
            terminal_role = shadow / "03_plan"
            for destination in (hidden, self.root / "missing-role-target"):
                with self.subTest(role_symlink=destination.name):
                    terminal_role.symlink_to(destination, target_is_directory=True)
                    try:
                        self._refusal(await self._call(session, self.request, pure=True), "preview_subjects")
                    finally:
                        terminal_role.unlink()

    async def test_stage_checks_helper_owned_seal_after_resolution_before_writes(self):
        async with self._session() as session:
            preview = self._preview(await self._call(session, self.request, pure=True))
            request = self._stage_request(self.request, preview)
            tampered = {**request, "preview_sha256": "0" * 64}
            with patch.object(staging, "stage_subject_preview", wraps=staging.stage_subject_preview) as native_stage:
                self._refusal(await self._call(session, tampered, pure=True), "stage_subjects")
                self.assertEqual(1, native_stage.call_count)
                self.assertEqual(tampered["preview_sha256"], native_stage.call_args.kwargs["expected_preview_sha256"])
                self.assertEqual(tampered["illustrative_updated_at"], native_stage.call_args.kwargs["timestamp"])
            grammar = self.root / get_profile("approved").grammar_pins[0].path
            original = grammar.read_bytes()
            real_preview = staging.preview_subject_patches
            observed = []

            def drift_before_helper_preview(*args, **kwargs):
                observed.append(True)
                grammar.write_bytes(original + b"\nChanged after target resolution.\n")
                return real_preview(*args, **kwargs)

            try:
                with patch.object(staging, "preview_subject_patches", drift_before_helper_preview):
                    response = await self._call(session, request)
                self.assertTrue(observed, "the staging helper must compute its own preview")
                self._refusal(response, "stage_subjects")
                self.assertFalse((self.root / STAGE_PREFIX).exists())
            finally:
                grammar.write_bytes(original)
            self._refusal(await self._call(session, {**request, "illustrative_updated_at": None}, pure=True),
                          "stage_subjects")

    async def test_stage_readback_creates_only_fresh_scratch_batches_and_noop_keeps_null_time(self):
        async with self._session() as session:
            preview = self._preview(await self._call(session, self.request, pure=True))
            request = self._stage_request(self.request, preview)
            before = _snapshot(self.root)
            first = self._stage(await self._call(session, request), preview, before)
            before = _snapshot(self.root)
            second = self._stage(await self._call(session, request), preview, before)
            self.assertNotEqual(first["stage_root"], second["stage_root"])
            noop_request = {**self.request, "atoms": [self._item(self.path, noop=True)]}
            noop = self._preview(await self._call(session, noop_request, pure=True))
            invalid_noop_time = {**self._stage_request(noop_request, noop),
                                 "illustrative_updated_at": "2026-10-14 01:00:00 +0000"}
            self._refusal(await self._call(session, invalid_noop_time, pure=True), "stage_subjects")
            before = _snapshot(self.root)
            self._stage(await self._call(session, self._stage_request(noop_request, noop)), noop, before)

    async def test_partial_write_readback_and_final_boundary_report_actual_retained_artifacts(self):
        real_write = staging._write_candidate
        real_stage = staging.stage_subject_preview
        for fault in ("partial", "tamper", "boundary"):
            with self.subTest(fault=fault):
                async with self._session() as session:
                    preview = self._preview(await self._call(session, self.request, pure=True))
                    request = self._stage_request(self.request, preview)
                    before = _snapshot(self.root)
                    injected = []
                    original_settings = self.settings.read_bytes()

                    def faulty_write(root, destination, raw):
                        if not injected and destination.name != "manifest.json":
                            injected.append(destination)
                            fingerprint = real_write(root, destination, raw[:16] if fault == "partial" else raw)
                            if fault == "partial":
                                raise operations.ToolError("subject-stage-write-failed", "Injected partial write", {
                                    "created_artifact": {"path": destination.relative_to(root).as_posix(),
                                                         "identity": fingerprint[:2]}})
                            destination.write_bytes(raw + b"\nReadback tamper.\n")
                            return fingerprint
                        return real_write(root, destination, raw)

                    def stage_then_boundary_drift(*args, **kwargs):
                        staged = real_stage(*args, **kwargs)
                        injected.append(self.root / staged["manifest_path"])
                        self.settings.write_bytes(original_settings + b"\n# External boundary drift after staging.\n")
                        before[self.settings.relative_to(self.root).as_posix()] = (
                            "file", self.settings.read_bytes(), stat.S_IMODE(self.settings.stat().st_mode))
                        return staged

                    try:
                        if fault == "boundary":
                            with patch.object(staging, "stage_subject_preview", stage_then_boundary_drift):
                                result = self._refusal(await self._call(session, request), "stage_subjects")
                        else:
                            with patch.object(staging, "_write_candidate", faulty_write):
                                result = self._refusal(await self._call(session, request), "stage_subjects")
                        self.assertTrue(injected)
                        self._scratch_only(before)
                        artifacts = [artifact for error in result["errors"] for artifact in error["retained_artifacts"]]
                        self.assertTrue(artifacts, "partial staging cannot become a zero-effect refusal")
                        references = {artifact["path"] for artifact in artifacts}
                        self.assertIn(injected[0].relative_to(self.root).as_posix(), references)
                        for artifact in artifacts:
                            path = self.root / artifact["path"]
                            self.assertTrue(path.exists())
                            if "sha256" in artifact:
                                self.assertEqual(artifact["sha256"], _digest(path.read_bytes()))
                    finally:
                        if fault == "boundary":
                            self.settings.write_bytes(original_settings)

    async def test_native_cli_without_expected_seal_is_compatible_and_never_publishes(self):
        before = _snapshot(self.root)
        private_items = self.fixture._payload(self.path)
        result = staging.stage_subject_preview(self.root, private_items,
            timestamp="2026-10-14 01:00:00 +0000", subject_profile="legacy")
        self.assertTrue(result["staging_only"])
        self.assertTrue(result["illustrative"])
        self._scratch_only(before)
        self.assertEqual(self.originals[self.path], self.path.read_bytes())
        for atom in result["preview"]["atoms"]:
            archive = atom["subject_intent"]["predecessorArchive"]
            self.assertFalse((self.root / archive["path"]).exists())


if __name__ == "__main__":
    unittest.main()
