from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import subprocess
from dataclasses import replace
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "PROJECT_TOOLS/RELEASE_VERSION/native_hooks.py"
SPEC = importlib.util.spec_from_file_location("test_native_local_hooks_module", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
hooks = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = hooks
SPEC.loader.exec_module(hooks)


class NativeLocalHooksExportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.export_root = self.root / "sealed-methodology"
        atom = self.export_root / "001_CORE_META_MODEL/04_requirement/CA-R-1.md"
        support = self.export_root / "001_CORE_META_MODEL/caprmedio_framework_default_settings.toml"
        atom.parent.mkdir(parents=True)
        atom.write_bytes(b"---\natom_id: CA-R-1\nstatus: Active\nversion: 1\n---\nbody\n")
        support.write_bytes(b"[release_suite]\nunit_timeout_seconds = 60\n")
        self.atom = atom
        self.support = support
        self.export = SimpleNamespace(
            candidate=SimpleNamespace(project_root=str(self.root)),
            source_export_root="sealed-methodology",
        )

    @staticmethod
    def _digest(path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def _inventory(self) -> None:
        payload = {
            "atoms": [{
                "atom_id": "CA-R-1",
                "destination_path": "001_CORE_META_MODEL/04_requirement/CA-R-1.md",
                "digest": self._digest(self.atom),
                "sha256": self._digest(self.atom),
                "source_path": "001_CORE_META_MODEL/04_requirement/CA-R-1.md",
                "version": 1,
            }],
            "support": [{
                "path": "001_CORE_META_MODEL/caprmedio_framework_default_settings.toml",
                "sha256": self._digest(self.support),
            }],
        }
        (self.export_root / "inventory.json").write_text(json.dumps(payload), encoding="utf-8")

    def test_exact_active_atoms_and_default_support_copy_without_history(self) -> None:
        self._inventory()
        atoms = hooks._export_atoms(self.export)
        supports = hooks._export_supports(self.export, atoms)
        product = self.root / "product/sources"
        for relative, digest in tuple((atom.relative, atom.digest) for atom in atoms) + supports:
            source = self.export_root.joinpath(*relative.parts)
            target = product.joinpath(*relative.parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())
            self.assertEqual(digest, self._digest(target))
        hooks._same_exported_files(self.root, product, tuple((atom.relative, atom.digest) for atom in atoms) + supports)
        self.assertTrue((product / "001_CORE_META_MODEL/caprmedio_framework_default_settings.toml").is_file())
        self.assertFalse((product / "archive").exists())

    def test_tampered_support_is_refused_before_product_copy(self) -> None:
        self._inventory()
        self.support.write_bytes(b"changed")
        atoms = hooks._export_atoms(self.export)
        with self.assertRaises(hooks.ReleaseContractError) as rejected:
            hooks._export_supports(self.export, atoms)
        self.assertEqual(rejected.exception.code, "local-release-export-invalid")


class NativeLocalHooksGitCheckpointTests(unittest.TestCase):
    """Real fixture-local Git checks only, never native Full Gate evidence."""

    def setUp(self) -> None:
        # No global Git identity, signing, hooks, index, or repository is used.
        self.git_environment = patch.dict(os.environ, {
            "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
            "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": "/dev/null",
        }, clear=True)
        self.git_environment.start()
        self.addCleanup(self.git_environment.stop)
        self.root = Path(tempfile.mkdtemp(prefix="native-local-git-checkpoint-", dir="/private/tmp"))
        self.product = self.root / "101_FRAMEWORK_METHODOLOGY"
        self.product.mkdir()
        self.owned = self.product / "owned.md"
        self.owned.write_bytes(b"original owned content\n")
        self.other_tracked = self.root / "other-tracked.md"
        self.other_tracked.write_bytes(b"original unrelated content\n")
        self._git("init", "-q")
        self._git("config", "user.name", "Disposable Local Release Test")
        self._git("config", "user.email", "local-release-test@example.invalid")
        self._git("config", "commit.gpgsign", "false")
        self._git("add", "--", "101_FRAMEWORK_METHODOLOGY/owned.md", "other-tracked.md")
        self._git("commit", "-q", "-m", "test: initial fixture")
        self.initial_commit = self._git("rev-parse", "HEAD").decode().strip()
        self.workflow_run_id = "workflow-local-checkpoint-test"
        self.action_run_id = "action-local-checkpoint-test"
        # These fields are deliberately unused by _commit_changes. No gate,
        # Session admission, export validation, or publication is claimed.
        self.bindings = hooks.SelectedLocalReleaseBindings(
            root=self.root, layout=None, export=None, packet=None, atoms=(), supports=(),
            workflow_run_id=self.workflow_run_id, action_run_id=self.action_run_id,
        )
        self.core = hooks._local_release_module()

    def _git(self, *arguments: str) -> bytes:
        result = subprocess.run(["git", "-C", str(self.root), *arguments],
                                capture_output=True, timeout=30, check=False)
        self.assertEqual(0, result.returncode, result.stderr.decode(errors="replace"))
        return result.stdout

    def _snapshot(self):
        return self.core._snapshot(self.product, root=self.root, preserve=frozenset())

    def test_commit_contains_only_changed_owned_file_and_exact_run_receipt(self) -> None:
        before = self._snapshot()
        self.owned.write_bytes(b"changed owned content\n")
        self.bindings._commit_changes(before, self._snapshot(), "copy_active_sources")
        commit = self._git("rev-parse", "HEAD").decode().strip()
        self.assertNotEqual(self.initial_commit, commit)
        self.assertRegex(commit, r"^[0-9a-f]{40}$")
        changed = self._git("diff-tree", "--no-commit-id", "--name-only", "-r", commit).decode().splitlines()
        self.assertEqual(["101_FRAMEWORK_METHODOLOGY/owned.md"], changed)
        self.assertEqual(b"", self._git("diff", "--cached", "--name-only"))
        self.assertEqual(1, len(self.bindings.checkpoint_refs))
        receipt_ref = self.bindings.checkpoint_refs[0]
        self.assertEqual(f".caprmedio_tmp/local_release/{self.workflow_run_id}/copy_active_sources.json", receipt_ref)
        receipt = json.loads((self.root / receipt_ref).read_bytes())
        self.assertEqual({"workflow_run_id": self.workflow_run_id, "action_run_id": self.action_run_id,
                          "phase": "copy_active_sources", "commit": commit,
                          "paths": ["101_FRAMEWORK_METHODOLOGY/owned.md"]}, receipt)

    def test_unrelated_untracked_file_remains_untracked_and_unchanged(self) -> None:
        unrelated = self.root / "unrelated-untracked.md"
        unrelated.write_bytes(b"preserve this unrelated change\n")
        before = self._snapshot()
        self.owned.write_bytes(b"changed owned content\n")
        self.bindings._commit_changes(before, self._snapshot(), "compile_product")
        self.assertEqual(b"preserve this unrelated change\n", unrelated.read_bytes())
        self.assertEqual(b"", self._git("ls-files", "--", "unrelated-untracked.md"))
        self.assertIn("?? unrelated-untracked.md", self._git("status", "--porcelain=1", "--untracked-files=all").decode())
        self.assertEqual(b"original unrelated content\n", self.other_tracked.read_bytes())

    def test_existing_nonempty_index_refuses_without_staging_owned_change(self) -> None:
        self.other_tracked.write_bytes(b"existing staged change\n")
        self._git("add", "--", "other-tracked.md")
        staged_before = self._git("diff", "--cached", "--binary")
        before = self._snapshot()
        self.owned.write_bytes(b"changed owned content\n")
        with self.assertRaises(hooks.ReleaseContractError) as rejected:
            self.bindings._commit_changes(before, self._snapshot(), "clear_product")
        self.assertEqual("local-release-git-index-not-empty", rejected.exception.code)
        self.assertEqual(staged_before, self._git("diff", "--cached", "--binary"))
        self.assertEqual(self.initial_commit, self._git("rev-parse", "HEAD").decode().strip())
        self.assertEqual(b"changed owned content\n", self.owned.read_bytes())
        self.assertEqual([], self.bindings.checkpoint_refs)
        self.assertFalse((self.root / ".caprmedio_tmp/local_release").exists())

    def test_unchanged_snapshot_creates_neither_commit_nor_receipt(self) -> None:
        before = self._snapshot()
        self.bindings._commit_changes(before, self._snapshot(), "compile_product")
        self.assertEqual(self.initial_commit, self._git("rev-parse", "HEAD").decode().strip())
        self.assertEqual(b"", self._git("status", "--porcelain=1"))
        self.assertEqual([], self.bindings.checkpoint_refs)
        self.assertFalse((self.root / ".caprmedio_tmp/local_release").exists())

    def test_installed_product_mismatch_refuses_before_package_or_launcher(self) -> None:
        # Only the preceding retained-gate reopen is mocked for this negative
        # boundary check; this test provides no Full Gate or live MCP proof.
        installed = self.root / ".caprmedio_demo/000_CAPRMEDIO_framework"
        installed.mkdir(parents=True)
        installed_file = installed / "owned.md"
        bindings = replace(self.bindings, layout=SimpleNamespace(
            installed_root=installed.relative_to(self.root).as_posix(),
            product_root=self.product.relative_to(self.root).as_posix(),
        ))
        for mismatch in ("bytes", "mode"):
            with self.subTest(mismatch=mismatch):
                installed_file.write_bytes(b"different content\n" if mismatch == "bytes" else self.owned.read_bytes())
                installed_file.chmod(0o644 if mismatch == "bytes" else 0o600)
                with patch.object(hooks.SelectedLocalReleaseBindings, "_reopen") as reopen, \
                        patch("framework_package.verify_framework_package") as package, \
                        patch("installed_mcp_runtime.launch_installed_mcp_http") as launcher:
                    with self.assertRaises(hooks.ReleaseContractError) as rejected:
                        bindings.start_and_check_mcp(SimpleNamespace())
                    self.assertEqual("local-release-installed-product-mismatch", rejected.exception.code)
                    reopen.assert_called_once_with()
                    package.assert_not_called()
                    launcher.assert_not_called()
                self.assertFalse((self.root / ".caprmedio_tmp/local_release").exists())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
