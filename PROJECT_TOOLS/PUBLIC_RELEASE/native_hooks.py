"""Project-owned selected-session hooks for the simple public-release core.

This module intentionally has no command-line entrypoint.  Its caller already
owns one admitted selected MCP Session and supplies the one host-controlled
ImplementationAgent prompt callable.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
from typing import Any, Callable, Mapping, Sequence

from native_bindings import FinalizationResult, GateResult, NativePublicReleaseBindings, NativePublicReleaseError
from public_release import PublicReleaseInterrupted, ToolCallEvidence, _gate


Prompt = Callable[[Path, str, Sequence[str]], Mapping[str, object]]


def _core_module():
    """Load the Project core under a private name, never as legacy public_release."""
    name = "_caprmedio_project_public_release_core"
    existing = sys.modules.get(name)
    if existing is not None:
        return existing
    path = Path(__file__).with_name("public_release.py")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise NativePublicReleaseError("project-core-unavailable", "Project public-release core is unavailable")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class NativePublicReleaseHooks:
    """Translate the simple core callbacks into one existing selected Session."""

    def __init__(self, project_root: Path, *, bindings: NativePublicReleaseBindings,
                 phases: Any, parameters: Mapping[str, Any], prompt: Prompt) -> None:
        root = Path(project_root).resolve(strict=True)
        if not isinstance(bindings, NativePublicReleaseBindings):
            raise NativePublicReleaseError("native-bindings-required", "Project public hooks need NativePublicReleaseBindings")
        if not isinstance(parameters, Mapping) or not callable(prompt):
            raise NativePublicReleaseError("public-hooks-invalid", "Project public hooks need sealed parameters and one prompt callable")
        required = ("begin", "finish", "fail", "execute")
        if any(not callable(getattr(phases, name, None)) for name in required):
            raise NativePublicReleaseError("public-session-required", "Project public hooks need selected-session phases")
        self.root = root
        self.bindings = bindings
        self.phases = phases
        self.parameters = parameters
        self.prompt_callback = prompt
        self.source: Any | None = None
        self.discovered: Any | None = None
        self.pull_request: Any | None = None
        self._documents_token: object | None = None
        self._prepared: Any | None = None
        self._initial_commit: Any | None = None
        self._history_token: object | None = None
        self._history_capture: Any | None = None
        self._history_commit: Any | None = None
        self._history_finalization: FinalizationResult | None = None

    def discover_matching_pr(self) -> None:
        result = self.phases.execute(
            "discover_matching_pr", lambda: self.bindings.discover_matching_pr(self.parameters),
        )
        if len(result.matches) > 1:
            raise NativePublicReleaseError("duplicate-matching-pr", "selected public discovery found more than one matching PR")
        self.discovered = result.matches[0] if result.matches else None

    def begin_document_admission(self, project_root: Path, version: str, changes: Sequence[str]) -> object:
        self._require_root_and_version(project_root, version)
        if self._documents_token is not None or self.source is not None:
            raise NativePublicReleaseError("public-hooks-order", "generated public documents were already admitted")
        self.phases.begin("prepare_public_materials")
        try:
            self.bindings.begin_generated_public_materials(self.parameters)
        except BaseException:
            self.phases.fail()
            raise
        self._documents_token = object()
        return self._documents_token

    def prompt(self, project_root: Path, version: str, changes: Sequence[str]) -> Mapping[str, object]:
        self._require_root_and_version(project_root, version)
        if self._documents_token is None:
            raise NativePublicReleaseError("public-hooks-order", "ImplementationAgent prompt requires active O192 admission")
        result = self.prompt_callback(self.root, version, changes)
        if not isinstance(result, Mapping):
            raise NativePublicReleaseError("prompt-output-invalid", "ImplementationAgent prompt must return structured release text")
        return result

    def capture_document_admission(self, token: object) -> None:
        self._require_document_token(token)
        try:
            self._prepared = self.bindings.capture_generated_public_materials(self.parameters, self.discovered)
        except BaseException as error:
            self._fail_active(error)
            self._documents_token = None
            raise

    def finish_document_admission(self, token: object) -> None:
        self._require_document_token(token)
        if self._prepared is None:
            raise NativePublicReleaseError("public-hooks-order", "generated public documents need physical SourceProof capture")
        self.phases.finish(self._prepared)
        self.source = self._prepared.source
        self._documents_token = None

    def abort_document_admission(self, token: object) -> None:
        if token is self._documents_token:
            self.phases.fail()
            self._documents_token = None

    def test(self, project_root: Path, candidate_root: Path) -> GateResult:
        self._require_root_and_version(project_root, self._version())
        if Path(candidate_root).resolve(strict=True) != self.root or self.source is None:
            raise NativePublicReleaseError("public-hooks-order", "fresh public gate needs the selected Project and captured source")
        def reopen_gate() -> GateResult:
            result = self.bindings.run_full_gate(self.parameters, self.source, "initial")
            if not isinstance(result, GateResult):
                raise NativePublicReleaseError("invalid-full-gate", "selected public gate did not return typed GateResult")
            _gate(
                result, "initial full gate", self.source,
                project_root=self.root, selected_version=self._version(),
            )
            return result

        return self.phases.execute("freeze_and_gate", reopen_gate)

    def commit(self, project_root: Path, paths: Sequence[str], message: str) -> Any:
        self._require_root_and_version(project_root, self._version())
        if not isinstance(message, str) or not message:
            raise NativePublicReleaseError("public-hooks-invalid", "public commit needs one message")
        if self.source is None:
            raise NativePublicReleaseError("public-hooks-order", "public commit needs captured source")
        if self._history_finalization is not None:
            if not self._history_finalization.changed:
                raise NativePublicReleaseError("public-hooks-order", "an unchanged Version History link has no follow-up commit")
            if tuple(paths) != (self.source.version_history_ref,):
                raise NativePublicReleaseError("public-hooks-paths", "URL-only follow-up may commit only Version History")
            if self._history_commit is not None:
                raise NativePublicReleaseError("public-hooks-order", "Version History follow-up was already committed")
            self._history_commit = self.bindings.commit_and_push(
                self.parameters, self._history_finalization.source, "history_link_final",
            )
            return self._history_commit
        if self._history_token is not None:
            if tuple(paths) != (self.source.version_history_ref,):
                raise NativePublicReleaseError("public-hooks-paths", "URL-only follow-up may commit only Version History")
            self._history_capture = self.bindings.capture_generated_public_materials(self.parameters, self.pull_request)
            self._history_commit = self.bindings.commit_and_push(
                self.parameters, self._history_capture.source, "history_link_final",
            )
            return self._history_commit
        expected = (self.source.readme_ref, self.source.pr_body_ref, self.source.version_history_ref)
        if tuple(paths) != expected or self._initial_commit is not None:
            raise NativePublicReleaseError("public-hooks-paths", "initial public commit must contain exactly the generated documents")
        self.phases.begin("push_and_upsert_pr")
        try:
            self._initial_commit = self.bindings.commit_and_push(self.parameters, self.source, "initial")
        except BaseException as error:
            self._fail_active(error)
            raise
        return self._initial_commit

    def push(self, project_root: Path, branch: str) -> Any:
        self._require_root_and_version(project_root, self._version())
        if branch != "amm/dev":
            raise NativePublicReleaseError("public-hooks-branch", "selected public push is amm/dev only")
        if self._history_finalization is not None:
            if not self._history_finalization.changed or self._history_commit is None:
                raise NativePublicReleaseError("public-hooks-order", "Version History push needs the admitted scoped commit")
            return self._history_commit
        if self._history_token is not None:
            if self._history_commit is None:
                raise NativePublicReleaseError("public-hooks-order", "history push needs the admitted scoped commit")
            return self._history_commit
        if self._initial_commit is None:
            raise NativePublicReleaseError("public-hooks-order", "initial push needs the admitted scoped commit")
        return self._initial_commit

    def pr(self, project_root: Path, branch: str, base: str, body: str) -> Mapping[str, object]:
        self._require_root_and_version(project_root, self._version())
        if branch != "amm/dev" or base != "main" or not isinstance(body, str) or not body:
            raise NativePublicReleaseError("public-hooks-pr", "selected public PR is amm/dev to main with one body")
        if self._initial_commit is None or self.source is None:
            raise NativePublicReleaseError("public-hooks-order", "selected public PR needs its admitted initial push")
        try:
            result = self.bindings.upsert_main_pr(
                self.parameters, self.source, self.discovered.url if self.discovered else None, "initial",
            )
            self.phases.finish(result, prior_results=(self._initial_commit,))
        except BaseException as error:
            self._fail_active(error)
            raise
        self.pull_request = result.pull_request
        return {"url": self.pull_request.url}

    def existing_history_pr_url(self, project_root: Path, version: str) -> str | None:
        self._require_root_and_version(project_root, version)
        return self.discovered.url if self.discovered is not None else None

    def finalize_history_link(self, project_root: Path, version: str, url: str) -> FinalizationResult:
        self._require_root_and_version(project_root, version)
        if (self.source is None or self.pull_request is None or url != self.pull_request.url
                or self._history_token is not None or self._history_finalization is not None):
            raise NativePublicReleaseError("public-hooks-history", "Version History must bind the actual selected PR URL once")
        self.phases.begin("finalize_history_link")
        try:
            result = self.bindings.finalize_history_link(self.parameters, self.source, self.pull_request)
            if not isinstance(result, FinalizationResult):
                raise NativePublicReleaseError("history-finalization-invalid", "selected history finalizer did not return FinalizationResult")
        except BaseException as error:
            self._fail_active(error)
            raise
        self._history_finalization = result
        return result

    def begin_history_finalization(self, project_root: Path, version: str, url: str) -> object:
        self._require_root_and_version(project_root, version)
        if self.pull_request is None or url != self.pull_request.url:
            raise NativePublicReleaseError("public-hooks-history", "Version History must bind the actual selected PR URL")
        self.phases.begin("finalize_history_link")
        try:
            self.bindings.begin_generated_history_link(self.parameters, self.source)
        except BaseException as error:
            self._fail_active(error)
            raise
        self._history_token = object()
        return self._history_token

    def finish_history_finalization(self, token: object) -> None:
        if token is self._history_finalization:
            finalization = self._history_finalization
            if finalization.changed:
                if self._history_commit is None:
                    raise NativePublicReleaseError("public-hooks-order", "changed Version History needs its scoped commit")
                self.phases.finish(self._history_commit, prior_results=(finalization,))
            else:
                self.phases.finish(finalization)
            self.source = finalization.source
            self._history_finalization = None
            self._history_commit = None
            return
        if token is not self._history_token or self._history_capture is None or self._history_commit is None:
            raise NativePublicReleaseError("public-hooks-order", "Version History finalization is incomplete")
        self.phases.finish(self._history_commit, prior_results=(self._history_capture,))
        self._history_token = None

    def abort_history_finalization(self, token: object) -> None:
        if token is self._history_finalization:
            self.phases.fail()
            self._history_finalization = None
            self._history_commit = None
            return
        if token is self._history_token:
            self.phases.fail()
            self._history_token = None

    def journal(self, _event: Mapping[str, object]) -> None:
        """The selected Session terminal rows/evidence remain the sole Journal owner."""

    def _require_document_token(self, token: object) -> None:
        if token is not self._documents_token:
            raise NativePublicReleaseError("public-hooks-order", "generated document admission token is invalid")

    def _fail_active(self, error: BaseException) -> None:
        """Keep uncertain native effects pending; ordinary refusals are failed."""
        if isinstance(error, PublicReleaseInterrupted):
            call = getattr(error, "call", None)
            self.phases.fail(interrupted=True, call=call if isinstance(call, ToolCallEvidence) else None)
            return
        self.phases.fail()

    def _require_root_and_version(self, project_root: Path, version: str) -> None:
        if Path(project_root).resolve(strict=True) != self.root or version != self._version():
            raise NativePublicReleaseError("public-hooks-binding", "public hook differs from the selected Project or frozen Version")

    def _version(self) -> str:
        release = self.parameters.get("release") if isinstance(self.parameters, Mapping) else None
        value = release.get("selected_version") if isinstance(release, Mapping) else None
        if not isinstance(value, str):
            raise NativePublicReleaseError("public-hooks-invalid", "selected public release has no frozen Version")
        return value.removeprefix("v")


def create_native_public_hooks(project_root: Path, *, bindings: NativePublicReleaseBindings,
                               phases: Any, parameters: Mapping[str, Any], prompt: Prompt) -> NativePublicReleaseHooks:
    return NativePublicReleaseHooks(project_root, bindings=bindings, phases=phases,
                                    parameters=parameters, prompt=prompt)


def run_selected_public_release(project_root: Path, *, run_id: str, config: Mapping[str, object],
                                bindings: NativePublicReleaseBindings, phases: Any,
                                parameters: Mapping[str, Any], prompt: Prompt) -> dict[str, object]:
    """Main Project path: discover, then run the core under selected-session hooks."""
    source = parameters.get("source") if isinstance(parameters, Mapping) else None
    expected = (source.get("readme_ref"), source.get("pr_body_ref"), source.get("version_history_ref")) if isinstance(source, Mapping) else ()
    if (not isinstance(config, Mapping) or tuple(config.get("release_paths", ())) != expected
            or config.get("readme_path") != expected[0] or config.get("notes_path") != expected[1]
            or config.get("version_history_path") != expected[2]):
        raise NativePublicReleaseError("public-hooks-paths", "Project config must declare exactly the selected three document paths")
    hooks = create_native_public_hooks(project_root, bindings=bindings, phases=phases,
                                       parameters=parameters, prompt=prompt)
    hooks.discover_matching_pr()
    return _core_module().run_public_release(project_root, run_id=run_id, hooks=hooks, config=config)


__all__ = ["NativePublicReleaseHooks", "create_native_public_hooks", "run_selected_public_release"]
