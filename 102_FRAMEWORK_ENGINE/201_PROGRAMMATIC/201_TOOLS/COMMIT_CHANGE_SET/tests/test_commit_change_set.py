"""Disposable Git fixture shared by COMMIT_CHANGE_SET acceptance tests."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


SCRIPT = Path(__file__).resolve().parents[1] / "commit_change_set.py"
SPEC = importlib.util.spec_from_file_location("commit_change_set", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
commit_change_set = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = commit_change_set
SPEC.loader.exec_module(commit_change_set)
UNSET = object()


class CommitChangeSetTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        (self.root / ".caprmedio").mkdir()
        (self.root / ".caprmedio_caprmedio").mkdir()
        (self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").write_text(
            '[artifact_timestamps]\ntimezone = "Asia/Tbilisi"\n\n[paths]\ncontrol_root = ".caprmedio_caprmedio"\njournal_root = ".caprmedio_caprmedio/_journal"\nruntime_root = ".caprmedio_runtime"\n',
            encoding="utf-8",
        )
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "user.name", "CAPRMEDIO Test")
        self.git("config", "github.username", "anatoly-m-maslennikov")
        self.write_atom(
            ".caprmedio_caprmedio/04_requirement/CA-R-001-REQUIREMENT--parent.md",
            version=1,
            relations={},
        )
        self.write_atom(
            ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md",
            version=1,
            relations={"child_of": ["CA-R-001-REQUIREMENT--parent"]},
            body="first",
        )
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")
        self.subject = ".caprmedio_caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md"
        self.write_atom(
            self.subject,
            version=2,
            relations={"child_of": ["CA-R-001-REQUIREMENT--parent"]},
            body="second",
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def git(self, *arguments: str) -> str:
        return subprocess.run(
            ["git", "-C", str(self.root), *arguments], check=True, capture_output=True, text=True
        ).stdout

    def write_atom(
        self, path: str, *, version: int, relations: dict[str, list[str]], body: str = "Body"
    ) -> None:
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        relation_lines = "relations:\n" + "".join(
            f"  {kind}:\n" + "".join(f"    - {item}\n" for item in values)
            for kind, values in relations.items()
        )
        target.write_text(
            f"---\nversion: {version}\n{relation_lines}---\n# {target.stem}\n\n{body}\n",
            encoding="utf-8",
        )

    def trigger(
        self,
        before_path: object = UNSET,
        after_path: object = UNSET,
        *,
        source_event_id: str = "source-event-1",
    ) -> dict[str, object]:
        git_directory = (self.root / self.git("rev-parse", "--git-dir").strip()).resolve()
        repository_identity = hashlib.sha256(
            json.dumps(
                {
                    "repository_root": self.root.resolve().as_posix(),
                    "git_directory": git_directory.as_posix(),
                },
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        adapter_id = "codex-test"
        trigger_id = hashlib.sha256(
            json.dumps(
                {
                    "schema_version": 1,
                    "adapter_id": adapter_id,
                    "source_event_id": source_event_id,
                    "repository_id": repository_identity,
                },
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        return {
            "schema_version": 1,
            "trigger_id": trigger_id,
            "adapter": {"id": adapter_id},
            "source_event_id": source_event_id,
            "repository": {"root": str(self.root), "identity": repository_identity},
            "observed_at": "2026-08-20T20:21:22Z",
            "before_path": self.subject if before_path is UNSET else before_path,
            "after_path": self.subject if after_path is UNSET else after_path,
            "llm_session": {"app": "codex", "uuid": "019f591f-04f6-70f2-8de7-828b7cccc69d"},
        }

    def snapshot(self) -> dict[str, object]:
        def files(path: Path) -> dict[str, str]:
            if not path.exists():
                return {}
            return {
                item.relative_to(self.root).as_posix(): hashlib.sha256(
                    item.read_bytes()
                ).hexdigest()
                for item in sorted(path.rglob("*"))
                if item.is_file()
            }

        return {
            "status": self.git("status", "--porcelain=v1"),
            "index": (self.root / ".git/index").read_bytes(),
            "head": self.git("rev-parse", "HEAD").strip(),
            "runtime": files(self.root / ".caprmedio_runtime"),
            "journal": files(self.root / ".caprmedio_caprmedio/_journal"),
        }
