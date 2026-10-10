"""Project public-release hooks bound to one selected public Session."""

from __future__ import annotations

from hashlib import sha256
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS"
PUBLIC = TOOLS / "PUBLIC_RELEASE"
for path in (str(TOOLS), str(PUBLIC)):
    if path not in sys.path:
        sys.path.insert(0, path)

from native_bindings import NativePublicReleaseBindings  # noqa: E402
from public_release import (  # noqa: E402
    CommitPushResult,
    FreshPublicNativeFullGateBinding,
    GateResult,
    PRDiscovery,
    PRUpsertResult,
    PrepareResult,
    PublicReleaseError,
    PublicReleaseInterrupted,
    PullRequest,
    SourceProof,
    ToolCallEvidence,
    VerifiedPushReceipt,
)


MODULE_PATH = ROOT / "PROJECT_TOOLS/PUBLIC_RELEASE/native_hooks.py"
SPEC = importlib.util.spec_from_file_location("project_native_public_hooks_test", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


OWNER = "anatoly-m-maslennikov"
REPOSITORY = "caprmedio-graph-driven-framework"
CANDIDATE = "a" * 64


def _call(name: str, *, effect: bool = True) -> ToolCallEvidence:
    return ToolCallEvidence(
        f"inputs/{name}.json", f"results/{name}.json",
        (f"effects/{name}.json",) if effect else (), (f"reports/{name}.json",),
    )


class _Phases:
    def __init__(self) -> None:
        self.events: list[tuple[object, ...]] = []

    def execute(self, phase: str, callback):
        self.events.append(("execute", phase))
        try:
            result = callback()
        except BaseException:
            self.events.append(("fail", phase))
            raise
        self.events.append(("finish", phase, result.call))
        return result

    def begin(self, phase: str) -> None:
        self.events.append(("begin", phase))

    def finish(self, result, *, prior_results=()) -> None:
        self.events.append(("finish", result.call, tuple(item.call for item in prior_results)))

    def fail(self, *, interrupted=False, call=None) -> None:
        self.events.append(("fail", interrupted, call))


class _Bindings(NativePublicReleaseBindings):
    """Typed stand-in: the factory must never accept an untyped callback bag."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self.events: list[tuple[object, ...]] = []

    def _source(self, pull_request: PullRequest | None = None) -> SourceProof:
        def digest(relative: str) -> str:
            return sha256((self.root / relative).read_bytes()).hexdigest()
        history = (self.root / "VERSION_HISTORY.md").read_text(encoding="utf-8")
        bullets = []
        for line in history.splitlines():
            if line.startswith("- "):
                bullets.append(line[2:])
        return SourceProof(
            CANDIDATE, "1.2.3", digest("version.toml"),
            "README.md", digest("README.md"),
            "docs/public-release.md", digest("docs/public-release.md"),
            "VERSION_HISTORY.md", digest("VERSION_HISTORY.md"),
            "; ".join(bullets), pull_request.url if pull_request else None,
            pull_request.number if pull_request else None,
        )

    def discover_matching_pr(self, _parameters):
        self.events.append(("discover",))
        return PRDiscovery(_call("discover", effect=False), ())

    def begin_generated_public_materials(self, _parameters) -> None:
        self.events.append(("begin-documents",))

    def capture_generated_public_materials(self, _parameters, pull_request=None):
        self.events.append(("capture-documents", pull_request.url if pull_request else None))
        return PrepareResult(_call("capture"), self._source(pull_request))

    def run_full_gate(self, _parameters, source, phase):
        self.events.append(("gate", source.version_history_summary, phase))
        return GateResult(_call("gate"), FreshPublicNativeFullGateBinding(object()))

    def commit_and_push(self, _parameters, source, phase):
        self.events.append(("commit", tuple((source.readme_ref, source.pr_body_ref, source.version_history_ref)), phase))
        return CommitPushResult(
            _call("commit"), "b" * 40,
            VerifiedPushReceipt(OWNER, REPOSITORY, "amm/dev", "b" * 40, "receipts/push.json"),
        )

    def upsert_main_pr(self, _parameters, source, known_url, phase):
        self.events.append(("pr", known_url, phase, source.version_history_summary))
        return PRUpsertResult(
            _call("pr"), PullRequest(
                f"https://github.com/{OWNER}/{REPOSITORY}/pull/42", 42, "amm/dev", "main",
            ),
        )

    def begin_generated_history_link(self, _parameters, source):
        self.events.append(("begin-history", source.version_history_summary))


class _InterruptedBindings(_Bindings):
    def commit_and_push(self, _parameters, _source, _phase):
        raise PublicReleaseInterrupted("external-effect-uncertain", "push outcome needs discovery")


class NativePublicHooksTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "version.toml").write_text('[framework]\nversion = "1.2.3"\n', encoding="utf-8")
        (self.root / "README.md").write_text("# Project\n", encoding="utf-8")
        (self.root / "VERSION_HISTORY.md").write_text("# Version History\n", encoding="utf-8")
        self.parameters = {
            "release": {"selected_version": "1.2.3"},
            "source": {
                "candidate_snapshot_manifest_sha256": CANDIDATE,
                "readme_ref": "README.md",
                "pr_body_ref": "docs/public-release.md",
                "version_history_ref": "VERSION_HISTORY.md",
                "version_history_summary": "Frozen baseline.",
            },
        }
        self.config = {
            "branch": "amm/dev", "base": "main",
            "release_paths": ["README.md", "docs/public-release.md", "VERSION_HISTORY.md"],
            "readme_path": "README.md", "notes_path": "docs/public-release.md",
            "version_history_path": "VERSION_HISTORY.md", "candidate_root": ".",
            "changes": ["selected public release"],
        }

    def test_one_selected_session_spans_prompt_capture_gate_pr_and_url_only_followup(self) -> None:
        bindings = _Bindings(self.root)
        phases = _Phases()
        prompts: list[tuple[str, tuple[str, ...]]] = []

        def prompt(_root: Path, version: str, changes: tuple[str, ...]):
            prompts.append((version, changes))
            return {
                "whats_new": ["Selected public path."],
                "whats_fixed": ["Typed source capture."],
                "version_history_bullets": ["Selected public release."],
            }

        with patch.object(MODULE, "_gate", side_effect=lambda result, *_args, **_kwargs: result) as gate:
            result = MODULE.run_selected_public_release(
                self.root, run_id="selected-public-1", config=self.config, bindings=bindings,
                phases=phases, parameters=self.parameters, prompt=prompt,
            )

        self.assertEqual("published", result["status"])
        self.assertEqual([("1.2.3", ("selected public release",))], prompts)
        self.assertEqual(
            ["discover", "begin-documents", "capture-documents", "gate", "commit", "pr",
             "begin-history", "capture-documents", "commit"],
            [event[0] for event in bindings.events],
        )
        self.assertEqual(
            ["discover_matching_pr", "prepare_public_materials", "freeze_and_gate",
             "push_and_upsert_pr", "finalize_history_link"],
            [event[1] for event in phases.events if event[0] in {"execute", "begin"}],
        )
        self.assertEqual(1, len([event for event in bindings.events if event[0] == "gate"]))
        gate.assert_called_once()
        history = (self.root / "VERSION_HISTORY.md").read_text(encoding="utf-8")
        self.assertIn("## 1.2.3 [PR](https://github.com/"
                      f"{OWNER}/{REPOSITORY}/pull/42)", history)
        self.assertIn("- Selected public release.", history)

    def test_uncertain_initial_push_marks_the_active_selected_phase_interrupted(self) -> None:
        bindings = _InterruptedBindings(self.root)
        phases = _Phases()
        (self.root / "docs").mkdir()
        (self.root / "docs/public-release.md").write_text(
            "## What's new\n- New.\n\n## What's fixed\n- Fixed.\n", encoding="utf-8",
        )
        (self.root / "VERSION_HISTORY.md").write_text(
            "## 1.2.3\n- Selected public release.\n", encoding="utf-8",
        )
        hooks = MODULE.create_native_public_hooks(
            self.root, bindings=bindings, phases=phases, parameters=self.parameters,
            prompt=lambda *_args: {},
        )
        hooks.source = bindings._source()

        with self.assertRaises(PublicReleaseInterrupted):
            hooks.commit(
                self.root,
                ("README.md", "docs/public-release.md", "VERSION_HISTORY.md"),
                "release: public v1.2.3",
            )

        self.assertEqual(("fail", True, None), phases.events[-1])

    def test_stale_or_failed_physical_gate_stops_before_the_initial_commit(self) -> None:
        bindings = _Bindings(self.root)
        phases = _Phases()
        with patch.object(
            MODULE, "_gate", side_effect=PublicReleaseError("stale-full-gate", "fresh proof differs"),
        ):
            with self.assertRaisesRegex(PublicReleaseError, "stale-full-gate"):
                MODULE.run_selected_public_release(
                    self.root, run_id="selected-public-stale", config=self.config, bindings=bindings,
                    phases=phases, parameters=self.parameters,
                    prompt=lambda *_args: {
                        "whats_new": ["Selected public path."],
                        "whats_fixed": ["Typed source capture."],
                        "version_history_bullets": ["Selected public release."],
                    },
                )

        self.assertIn(("gate", "Selected public release.", "initial"), bindings.events)
        self.assertFalse(any(event[0] == "commit" for event in bindings.events))


if __name__ == "__main__":
    unittest.main()
