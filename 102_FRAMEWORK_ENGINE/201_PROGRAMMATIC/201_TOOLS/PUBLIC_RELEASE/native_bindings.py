"""Native Git/GitHub bindings for the bounded public-release workflow.

This adapter is deliberately not an executable workflow entrypoint.  The
caller must already have admitted the selected Action Run and must provide
three live seams:

* ``effect_admitter`` revalidates the operator admission immediately before
  every effect;
* ``full_gate_runner`` returns the retained, typed RELEASE_VERSION evidence;
* ``evidence_recorder`` stores command observations and returns references
  which :mod:`public_release` attaches to its existing parent Step/Action
  Runs.

No Tool Run is created here.  In particular, an ordinary subprocess success
is not treated as a release gate, an authorization, or durable evidence.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import tomllib
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol
from urllib.parse import urlparse

from public_release import (
    CommitPushResult,
    FinalizationResult,
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
    _parameters,
    _read_source_file,
    _source,
)


_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_COMMIT = re.compile(r"^[0-9a-f]{40}$")
_REMOTE_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$")
_PR_URL = re.compile(r"^https://github\.com/([^/]+)/([^/]+)/pull/([1-9][0-9]*)$")


class NativePublicReleaseError(PublicReleaseError):
    """A native binding refused an unbound, stale, or uncertain operation."""


@dataclass(frozen=True)
class NativeCommandEvidence:
    """Sanitized observation for the selected-run evidence recorder.

    ``commands`` are argv arrays only.  They deliberately carry neither a
    shell program nor credentials.  The recorder owns durable storage and
    returns ordinary ``ToolCallEvidence`` for the existing parent runs.
    """

    operation: str
    commands: tuple[tuple[str, ...], ...]
    observations: Mapping[str, Any]
    effect: bool


class EffectAdmitter(Protocol):
    """Revalidate the selected operator authorization before one effect."""

    def __call__(self, operation: str, parameters: Mapping[str, Any], source: SourceProof | None) -> None: ...


class CandidateObserver(Protocol):
    """Return the exact current sealed candidate digest for one phase."""

    def __call__(self, parameters: Mapping[str, Any], phase: str) -> str: ...


class EvidenceRecorder(Protocol):
    """Persist an observation without creating a Tool Run."""

    def __call__(self, evidence: NativeCommandEvidence) -> ToolCallEvidence: ...


class FullGateRunner(Protocol):
    """Run/reopen the real full gate and return its existing typed binding."""

    def __call__(self, parameters: Mapping[str, Any], source: SourceProof, phase: str) -> GateResult: ...


class HistoryLinkFinalizer(Protocol):
    """Atomically write the exact history link and reseal the new candidate.

    Returning the new digest makes a caller prove that the source mutation was
    admitted by its existing candidate-sealing capability; this adapter never
    invents a post-mutation candidate digest.
    """

    def __call__(self, parameters: Mapping[str, Any], source: SourceProof,
                 pull_request: PullRequest, history_line: str) -> str: ...


CommandRunner = Callable[..., subprocess.CompletedProcess[str]]


def _default_command_runner(argv: Sequence[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
    return subprocess.run(list(argv), **kwargs)


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _pr_url(value: object, *, owner: str, repository: str) -> tuple[str, int]:
    if not isinstance(value, str) or any(character in value for character in "\r\n\x00"):
        raise NativePublicReleaseError("invalid-pr-url", "GitHub response has no safe PR URL")
    matched = _PR_URL.fullmatch(value)
    if matched is None or matched.group(1) != owner or matched.group(2) != repository:
        raise NativePublicReleaseError("invalid-pr-url", "GitHub response does not bind the selected personal repository")
    return value, int(matched.group(3))


def _history_line(summary: str, pull_request: PullRequest) -> str:
    return f"- {summary} [PR #{pull_request.number}]({pull_request.url})"


class NativePublicReleaseBindings:
    """Concrete, effect-bounded implementation of ``PublicReleaseBindings``.

    It may be constructed by the orchestration host only after it has a live
    selected-run admission bridge.  It intentionally has no CLI/main function
    and cannot manufacture a passed gate, authorization, source seal, or
    evidence reference by itself.
    """

    def __init__(
        self,
        project_root: Path,
        *,
        effect_admitter: EffectAdmitter,
        candidate_observer: CandidateObserver,
        evidence_recorder: EvidenceRecorder,
        full_gate_runner: FullGateRunner | None = None,
        history_link_finalizer: HistoryLinkFinalizer | None = None,
        command_runner: CommandRunner | None = None,
    ) -> None:
        try:
            root = Path(project_root).resolve(strict=True)
        except OSError as error:
            raise NativePublicReleaseError("project-unavailable", "native binding needs one existing selected Project") from error
        if not root.is_dir():
            raise NativePublicReleaseError("project-unavailable", "native binding needs one selected Project directory")
        if not callable(effect_admitter) or not callable(candidate_observer) or not callable(evidence_recorder):
            raise NativePublicReleaseError(
                "native-admission-unavailable",
                "native binding needs live admission, candidate, and evidence callbacks",
            )
        self.root = root
        self._effect_admitter = effect_admitter
        self._candidate_observer = candidate_observer
        self._evidence_recorder = evidence_recorder
        self._full_gate_runner = full_gate_runner
        self._history_link_finalizer = history_link_finalizer
        self._command_runner = command_runner or _default_command_runner

    def discover_matching_pr(self, parameters: Mapping[str, Any]) -> PRDiscovery:
        release = self._bound_release(parameters)
        commands: list[tuple[str, ...]] = []
        matches = self._list_matching_prs(release, commands)
        call = self._record(
            "discover_matching_pr",
            commands,
            {"matches": [self._pr_observation(row) for row in matches]},
            effect=False,
        )
        return PRDiscovery(call, tuple(matches))

    def prepare_public_materials(self, parameters: Mapping[str, Any], pr_url: str | None) -> PrepareResult:
        release = self._bound_release(parameters)
        commands: list[tuple[str, ...]] = []
        pull_request = self._known_pull_request(pr_url, release, commands) if pr_url is not None else None
        source = self._current_source(parameters, release, "prepare_public_materials", pull_request)
        if source.candidate_snapshot_manifest_sha256 != parameters["source"]["candidate_snapshot_manifest_sha256"]:
            raise NativePublicReleaseError("source-proof-mismatch", "prepared source does not bind the selected candidate snapshot")
        call = self._record(
            "prepare_public_materials",
            commands,
            self._source_observation(source),
            effect=False,
        )
        return PrepareResult(call, source)

    def run_full_gate(self, parameters: Mapping[str, Any], source: SourceProof, phase: str) -> GateResult:
        release = self._bound_release(parameters)
        self._require_current_source(parameters, release, f"full_gate:{phase}", source,
                                     self._source_pull_request(source, release))
        self._admit(f"run_full_gate:{phase}", parameters, source)
        if self._full_gate_runner is None:
            raise NativePublicReleaseError(
                "full-gate-binding-required",
                "native public release needs the admitted RELEASE_VERSION full-gate callback",
            )
        result = self._full_gate_runner(parameters, source, phase)
        if not isinstance(result, GateResult):
            raise NativePublicReleaseError("invalid-full-gate", "full-gate callback did not return a typed GateResult")
        return result

    def commit_and_push(self, parameters: Mapping[str, Any], source: SourceProof, phase: str) -> CommitPushResult:
        release = self._bound_release(parameters)
        self._require_current_source(parameters, release, f"commit_and_push:{phase}", source,
                                     self._source_pull_request(source, release))
        self._admit(f"commit_and_push:{phase}", parameters, source)
        allowed = self._source_paths(source)
        self._assert_clean_index_and_public_worktree(allowed)

        commands: list[tuple[str, ...]] = []
        add = ("git", "-C", str(self.root), "add", "--", *allowed)
        self._invoke(add, operation="git-add-public-materials", uncertain=True)
        commands.append(add)
        staged = self._post_effect(
            "git add public materials",
            lambda: self._invoke(("git", "-C", str(self.root), "diff", "--cached", "--name-only"),
                                 operation="git-staged-public-materials"),
        )
        staged_paths = self._post_effect(
            "git add public materials",
            lambda: self._validated_staged_paths(staged.stdout, allowed),
        )
        commit = ("git", "-C", str(self.root), "commit", "-m", f"docs: prepare public release {source.framework_version}")
        self._invoke(commit, operation="git-commit-public-materials", uncertain=True)
        commands.append(commit)
        head = self._post_effect(
            "git commit public materials",
            lambda: self._invoke(("git", "-C", str(self.root), "rev-parse", "HEAD"), operation="git-read-head"),
        )
        commit_sha = self._post_effect("git commit public materials", lambda: self._commit_sha(head.stdout))
        push = ("git", "-C", str(self.root), "push", release["remote"]["name"], f"HEAD:refs/heads/{release['release_branch']}")
        self._invoke(push, operation="git-push-public-release", uncertain=True)
        commands.append(push)
        remote = self._post_effect(
            "git push public release",
            lambda: self._invoke(
                ("git", "-C", str(self.root), "ls-remote", "--heads", release["remote"]["name"], f"refs/heads/{release['release_branch']}"),
                operation="git-verify-public-push",
            ),
        )
        commands.append(("git", "-C", str(self.root), "ls-remote", "--heads", release["remote"]["name"], f"refs/heads/{release['release_branch']}"))
        self._post_effect(
            "git push public release",
            lambda: self._require_remote_head(remote.stdout, commit_sha, release["release_branch"]),
        )
        call = self._post_effect(
            "git push public release",
            lambda: self._record(
                f"commit_and_push:{phase}", commands,
                {"commit_sha": commit_sha, "branch": release["release_branch"], "remote": release["remote"]["name"]},
                effect=True,
            ),
        )
        return CommitPushResult(
            call,
            commit_sha,
            VerifiedPushReceipt(
                release["remote"]["owner"],
                release["remote"]["repository"],
                release["release_branch"],
                commit_sha,
                call.result_ref,
            ),
        )

    def upsert_main_pr(self, parameters: Mapping[str, Any], source: SourceProof,
                       known_url: str | None, phase: str) -> PRUpsertResult:
        release = self._bound_release(parameters)
        self._require_current_source(parameters, release, f"upsert_main_pr:{phase}", source,
                                     self._source_pull_request(source, release))
        commands: list[tuple[str, ...]] = []
        known = self._known_pull_request(known_url, release, commands) if known_url is not None else None
        matches = self._list_matching_prs(release, commands)
        if len(matches) > 1:
            raise NativePublicReleaseError("duplicate-matching-pr", "native discovery found more than one matching open PR")
        if known is not None:
            if len(matches) != 1 or matches[0].url != known.url:
                raise NativePublicReleaseError("pr-currentness-stale", "known PR no longer matches current amm/dev to main discovery")
            pull_request = known
        elif matches:
            pull_request = matches[0]
        else:
            pull_request = None

        self._admit(f"upsert_main_pr:{phase}", parameters, source)
        title = f"CAPRMEDIO {source.framework_version} public release"
        if pull_request is None:
            create = (
                "gh", "pr", "create", "--repo", self._repository_slug(release), "--head", release["release_branch"],
                "--base", release["target_branch"], "--title", title, "--body-file", source.pr_body_ref,
            )
            self._invoke(create, operation="gh-create-main-pr", uncertain=True)
            commands.append(create)
            matches = self._post_effect(
                "gh create main PR",
                lambda: self._list_matching_prs(release, commands),
            )
            if len(matches) != 1:
                raise PublicReleaseInterrupted(
                    "external-effect-uncertain",
                    "PR create completed without one exact discoverable amm/dev to main PR",
                )
            pull_request = matches[0]
        else:
            edit = (
                "gh", "pr", "edit", str(pull_request.number), "--repo", self._repository_slug(release),
                "--title", title, "--body-file", source.pr_body_ref,
            )
            self._invoke(edit, operation="gh-update-main-pr", uncertain=True)
            commands.append(edit)
            pull_request = self._post_effect(
                "gh update main PR",
                lambda: self._read_pr(pull_request.number, release, commands),
            )

        call = self._post_effect(
            "gh upsert main PR",
            lambda: self._record(
                f"upsert_main_pr:{phase}", commands,
                {"pull_request": self._pr_observation(pull_request), "body_ref": source.pr_body_ref}, effect=True,
            ),
        )
        return PRUpsertResult(call, pull_request)

    def finalize_history_link(self, parameters: Mapping[str, Any], source: SourceProof,
                              pull_request: PullRequest) -> FinalizationResult:
        release = self._bound_release(parameters)
        self._require_current_source(parameters, release, "before_history_finalization", source,
                                     self._source_pull_request(source, release))
        if source.version_history_pr_url == pull_request.url:
            call = self._record(
                "finalize_history_link",
                (),
                {"changed": False, "pull_request": self._pr_observation(pull_request)},
                effect=False,
            )
            return FinalizationResult(call, source, False)
        if source.version_history_pr_url is not None:
            raise NativePublicReleaseError("history-link-invalid", "history source binds a different PR identity")
        if self._history_link_finalizer is None:
            raise NativePublicReleaseError(
                "history-finalizer-required",
                "native public release needs an admitted history-link and candidate-reseal callback",
            )
        self._admit("finalize_history_link", parameters, source)
        line = _history_line(source.version_history_summary, pull_request)
        sealed, final_source = self._post_effect(
            "finalize Version History link",
            lambda: self._finalize_and_reopen(parameters, release, source, pull_request, line),
        )
        call = self._post_effect(
            "finalize Version History link",
            lambda: self._record(
                "finalize_history_link",
                (),
                {"changed": True, "pull_request": self._pr_observation(pull_request), "history_line": line,
                 "candidate_snapshot_manifest_sha256": sealed},
                effect=True,
            ),
        )
        return FinalizationResult(call, final_source, True)

    def _finalize_and_reopen(self, parameters: Mapping[str, Any], release: Mapping[str, Any],
                             source: SourceProof, pull_request: PullRequest,
                             line: str) -> tuple[str, SourceProof]:
        """Run the admitted source mutation, then prove its new sealed state.

        This method is always invoked through ``_post_effect``.  Any failure
        after the finalizer starts is therefore terminally uncertain instead
        of a retryable failed run.
        """

        if self._history_link_finalizer is None:  # constructor-time optional seam
            raise NativePublicReleaseError("history-finalizer-required", "history finalizer is unavailable")
        sealed = self._history_link_finalizer(parameters, source, pull_request, line)
        if not isinstance(sealed, str) or _SHA256.fullmatch(sealed) is None:
            raise NativePublicReleaseError("candidate-reseal-unproven", "history finalizer did not return a sealed candidate SHA-256")
        final_source = self._current_source(parameters, release, "after_history_finalization", pull_request)
        if final_source.candidate_snapshot_manifest_sha256 != sealed:
            raise NativePublicReleaseError("candidate-reseal-unproven", "current candidate observer disagrees with history finalizer")
        if final_source.candidate_snapshot_manifest_sha256 == source.candidate_snapshot_manifest_sha256:
            raise NativePublicReleaseError("candidate-reseal-unproven", "history finalization did not create a new sealed candidate")
        return sealed, final_source

    def _bound_release(self, parameters: Mapping[str, Any]) -> dict[str, Any]:
        release = _parameters(parameters)["release"]
        remote = release["remote"]
        if _REMOTE_NAME.fullmatch(remote["name"]) is None:
            raise NativePublicReleaseError("unsafe-remote", "remote name is not a safe explicit Git remote")
        top_level = self._invoke(("git", "-C", str(self.root), "rev-parse", "--show-toplevel"), operation="bind-selected-project")
        try:
            observed_root = Path(top_level.stdout.strip()).resolve(strict=True)
        except OSError as error:
            raise NativePublicReleaseError("project-binding-unproven", "Git did not reopen the selected Project root") from error
        if observed_root != self.root:
            raise NativePublicReleaseError("project-binding-unproven", "Git root differs from the selected Project")
        branch = self._invoke(("git", "-C", str(self.root), "branch", "--show-current"), operation="bind-release-branch")
        if branch.stdout.strip() != release["release_branch"]:
            raise NativePublicReleaseError("unsafe-branch", "native binding must run on the selected amm/dev branch")
        remote_url = self._invoke(("git", "-C", str(self.root), "remote", "get-url", remote["name"]), operation="bind-personal-remote")
        self._assert_remote_target(remote_url.stdout.strip(), remote["owner"], remote["repository"])
        return _parameters(parameters)["release"]

    def _current_source(self, parameters: Mapping[str, Any], release: Mapping[str, Any],
                        phase: str, pull_request: PullRequest | None) -> SourceProof:
        candidate = self._candidate_observer(parameters, phase)
        if not isinstance(candidate, str) or _SHA256.fullmatch(candidate) is None:
            raise NativePublicReleaseError("candidate-currentness-unproven", "candidate observer did not return a SHA-256")
        selected = parameters["source"]
        try:
            readme, readme_sha = _read_source_file(self.root, selected["readme_ref"], "native README")
            pr_body, pr_body_sha = _read_source_file(self.root, selected["pr_body_ref"], "native PR body")
            history, history_sha = _read_source_file(self.root, selected["version_history_ref"], "native Version History")
            version_toml, version_toml_sha = _read_source_file(self.root, "version.toml", "native version.toml")
            version = tomllib.loads(version_toml)["framework"]["version"]
        except (KeyError, TypeError, tomllib.TOMLDecodeError, OSError) as error:
            raise NativePublicReleaseError("source-proof-unavailable", "selected public-release source cannot be reopened") from error
        if not isinstance(version, str):
            raise NativePublicReleaseError("source-proof-invalid", "root version.toml has no string framework version")
        self._assert_exact_history(history, selected["version_history_summary"], pull_request)
        proof = SourceProof(
            candidate, version.removeprefix("v"), version_toml_sha,
            selected["readme_ref"], readme_sha,
            selected["pr_body_ref"], pr_body_sha,
            selected["version_history_ref"], history_sha,
            selected["version_history_summary"],
            pull_request.url if pull_request else None,
            pull_request.number if pull_request else None,
        )
        _source(proof, "native source proof", project_root=self.root, release=release)
        return proof

    def _require_current_source(self, parameters: Mapping[str, Any], release: Mapping[str, Any],
                                phase: str, source: SourceProof,
                                pull_request: PullRequest | None) -> None:
        current = self._current_source(parameters, release, phase, pull_request)
        if current != source:
            raise NativePublicReleaseError("source-proof-stale", "public source bytes or candidate changed after the prior proof")

    def _list_matching_prs(self, release: Mapping[str, Any], commands: list[tuple[str, ...]]) -> list[PullRequest]:
        command = (
            "gh", "pr", "list", "--repo", self._repository_slug(release), "--state", "open",
            "--head", release["release_branch"], "--base", release["target_branch"],
            "--json", "number,url,headRefName,baseRefName,state",
        )
        completed = self._invoke(command, operation="gh-discover-main-pr")
        commands.append(command)
        try:
            rows = json.loads(completed.stdout)
        except json.JSONDecodeError as error:
            raise NativePublicReleaseError("github-response-invalid", "GitHub PR discovery did not return JSON") from error
        if not isinstance(rows, list):
            raise NativePublicReleaseError("github-response-invalid", "GitHub PR discovery must return a list")
        return [self._pull_request(row, release) for row in rows]

    def _read_pr(self, number: int, release: Mapping[str, Any], commands: list[tuple[str, ...]]) -> PullRequest:
        command = (
            "gh", "pr", "view", str(number), "--repo", self._repository_slug(release),
            "--json", "number,url,headRefName,baseRefName,state",
        )
        completed = self._invoke(command, operation="gh-read-main-pr")
        commands.append(command)
        try:
            row = json.loads(completed.stdout)
        except json.JSONDecodeError as error:
            raise NativePublicReleaseError("github-response-invalid", "GitHub PR view did not return JSON") from error
        return self._pull_request(row, release)

    def _known_pull_request(self, url: str, release: Mapping[str, Any],
                            commands: list[tuple[str, ...]]) -> PullRequest:
        _, number = _pr_url(url, owner=release["remote"]["owner"], repository=release["remote"]["repository"])
        return self._read_pr(number, release, commands)

    @staticmethod
    def _pull_request(value: object, release: Mapping[str, Any]) -> PullRequest:
        if not isinstance(value, Mapping):
            raise NativePublicReleaseError("github-response-invalid", "GitHub PR response must be an object")
        number = value.get("number")
        if type(number) is not int or number < 1:
            raise NativePublicReleaseError("github-response-invalid", "GitHub PR has no positive number")
        url, parsed_number = _pr_url(value.get("url"), owner=release["remote"]["owner"], repository=release["remote"]["repository"])
        if parsed_number != number:
            raise NativePublicReleaseError("github-response-invalid", "GitHub PR URL and number disagree")
        if (value.get("headRefName") != release["release_branch"] or value.get("baseRefName") != release["target_branch"]
                or str(value.get("state", "")).lower() != "open"):
            raise NativePublicReleaseError("github-response-invalid", "GitHub PR is not the selected open amm/dev to main PR")
        return PullRequest(url, number, release["release_branch"], release["target_branch"], "open")

    def _assert_clean_index_and_public_worktree(self, allowed: tuple[str, ...]) -> None:
        staged = self._invoke(("git", "-C", str(self.root), "diff", "--cached", "--name-only"), operation="inspect-git-index")
        if staged.stdout.strip():
            raise NativePublicReleaseError("unsafe-index", "native public release refuses a pre-existing staged Git index")
        status = self._invoke(("git", "-C", str(self.root), "status", "--porcelain=v1", "--untracked-files=all"), operation="inspect-public-worktree")
        for row in status.stdout.splitlines():
            if len(row) < 4 or row[:2] == "??" and row[3:].startswith('"'):
                raise NativePublicReleaseError("unsafe-worktree", "native public release cannot safely parse the Git worktree")
            path = row[3:]
            if " -> " in path or path not in allowed:
                raise NativePublicReleaseError("unsafe-worktree", "only declared public release files may be modified")

    @staticmethod
    def _validated_staged_paths(output: str, allowed: tuple[str, ...]) -> tuple[str, ...]:
        staged_paths = tuple(line for line in output.splitlines() if line)
        if not staged_paths or any(path not in allowed for path in staged_paths):
            raise NativePublicReleaseError("unsafe-index", "only declared public release files may be staged")
        return staged_paths

    @staticmethod
    def _commit_sha(output: str) -> str:
        commit_sha = output.strip()
        if _COMMIT.fullmatch(commit_sha) is None:
            raise NativePublicReleaseError("invalid-git-receipt", "Git did not return a full immutable commit SHA")
        return commit_sha

    @staticmethod
    def _require_remote_head(output: str, commit_sha: str, branch: str) -> None:
        if not NativePublicReleaseBindings._remote_head_matches(output, commit_sha, branch):
            raise NativePublicReleaseError("push-receipt-unverified", "remote branch does not point to the exact pushed commit")

    @staticmethod
    def _post_effect(operation: str, observation: Callable[[], Any]) -> Any:
        """Prevent replay after an effect lacks a terminal observation/receipt."""

        try:
            return observation()
        except PublicReleaseInterrupted:
            raise
        except Exception as error:
            raise PublicReleaseInterrupted(
                "external-effect-uncertain",
                f"{operation} completed but its terminal observation/evidence is unavailable; do not replay without discovery",
            ) from error

    def _admit(self, operation: str, parameters: Mapping[str, Any], source: SourceProof | None) -> None:
        try:
            result = self._effect_admitter(operation, parameters, source)
        except PublicReleaseError:
            raise
        except Exception as error:
            raise NativePublicReleaseError("native-admission-unproven", f"{operation} admission callback did not verify current authority") from error
        if result is not None:
            raise NativePublicReleaseError("native-admission-invalid", "admission callback must return None or raise")

    def _record(self, operation: str, commands: Sequence[Sequence[str]], observations: Mapping[str, Any], *, effect: bool) -> ToolCallEvidence:
        frozen = NativeCommandEvidence(operation, tuple(tuple(part) for part in commands), dict(observations), effect)
        try:
            call = self._evidence_recorder(frozen)
        except PublicReleaseError:
            raise
        except Exception as error:
            raise NativePublicReleaseError("evidence-recording-unavailable", f"{operation} could not retain parent-run evidence") from error
        if not isinstance(call, ToolCallEvidence):
            raise NativePublicReleaseError("invalid-tool-evidence", "evidence recorder did not return ToolCallEvidence")
        if effect and not call.effect_refs:
            raise NativePublicReleaseError("effect-evidence-required", "native effect lacks a durable evidence reference")
        if not effect and call.effect_refs:
            raise NativePublicReleaseError("invalid-tool-evidence", "read-only native observation cannot claim an effect")
        return call

    def _invoke(self, argv: Sequence[str], *, operation: str, uncertain: bool = False) -> subprocess.CompletedProcess[str]:
        command = tuple(argv)
        if not command or any(not isinstance(part, str) or not part for part in command):
            raise NativePublicReleaseError("unsafe-command", "native binding requires a non-empty argv array")
        try:
            completed = self._command_runner(
                command, cwd=self.root, stdin=subprocess.DEVNULL, capture_output=True,
                text=True, check=False, timeout=60,
            )
        except subprocess.TimeoutExpired as error:
            if uncertain:
                raise PublicReleaseInterrupted("external-effect-uncertain", f"{operation} timed out; do not replay without discovery") from error
            raise NativePublicReleaseError("native-command-timeout", f"{operation} timed out") from error
        except OSError as error:
            if uncertain:
                raise PublicReleaseInterrupted("external-effect-uncertain", f"{operation} could have started; do not replay without discovery") from error
            raise NativePublicReleaseError("native-command-unavailable", f"{operation} command is unavailable") from error
        if not isinstance(completed, subprocess.CompletedProcess) or completed.returncode != 0:
            if uncertain:
                raise PublicReleaseInterrupted("external-effect-uncertain", f"{operation} returned non-zero; discover before replay")
            raise NativePublicReleaseError("native-command-failed", f"{operation} returned non-zero")
        if not isinstance(completed.stdout, str):
            raise NativePublicReleaseError("native-command-invalid", f"{operation} returned non-text output")
        return completed

    @staticmethod
    def _remote_head_matches(output: str, commit_sha: str, branch: str) -> bool:
        rows = [row.split("\t") for row in output.splitlines() if row]
        return len(rows) == 1 and len(rows[0]) == 2 and rows[0][0] == commit_sha and rows[0][1] == f"refs/heads/{branch}"

    @staticmethod
    def _assert_remote_target(remote_url: str, owner: str, repository: str) -> None:
        if not remote_url or any(character in remote_url for character in "\r\n\x00 "):
            raise NativePublicReleaseError("unsafe-remote", "selected personal remote has an unsafe URL")
        expected_paths = {f"/{owner}/{repository}", f"/{owner}/{repository}.git"}
        if remote_url in {f"git@githuba:{owner}/{repository}", f"git@githuba:{owner}/{repository}.git",
                          f"git@github.com:{owner}/{repository}", f"git@github.com:{owner}/{repository}.git"}:
            return
        parsed = urlparse(remote_url)
        try:
            port = parsed.port
        except ValueError as error:
            raise NativePublicReleaseError("unsafe-remote", "selected personal remote has an invalid port") from error
        if (parsed.scheme not in {"https", "ssh"} or parsed.hostname not in {"github.com", "githuba"}
                or parsed.password is not None or port is not None or parsed.query or parsed.fragment
                or parsed.path not in expected_paths):
            raise NativePublicReleaseError("unsafe-remote", "selected personal remote is not an approved GitHub repository URL")
        if parsed.scheme == "https" and (parsed.hostname != "github.com" or parsed.username is not None):
            raise NativePublicReleaseError("unsafe-remote", "HTTPS remote must be canonical github.com without userinfo")
        if parsed.scheme == "ssh" and parsed.username != "git":
            raise NativePublicReleaseError("unsafe-remote", "SSH remote must use the approved git identity")

    @staticmethod
    def _repository_slug(release: Mapping[str, Any]) -> str:
        return f"{release['remote']['owner']}/{release['remote']['repository']}"

    @staticmethod
    def _source_paths(source: SourceProof) -> tuple[str, ...]:
        return (source.readme_ref, source.pr_body_ref, source.version_history_ref)

    @staticmethod
    def _source_pull_request(source: SourceProof, release: Mapping[str, Any]) -> PullRequest | None:
        if source.version_history_pr_url is None and source.version_history_pr_number is None:
            return None
        if source.version_history_pr_url is None or type(source.version_history_pr_number) is not int:
            raise NativePublicReleaseError("history-link-invalid", "source proof has an incomplete PR identity")
        url, number = _pr_url(source.version_history_pr_url, owner=release["remote"]["owner"],
                              repository=release["remote"]["repository"])
        if number != source.version_history_pr_number:
            raise NativePublicReleaseError("history-link-invalid", "source proof PR number and URL disagree")
        return PullRequest(url, number, release["release_branch"], release["target_branch"], "open")

    @staticmethod
    def _pr_observation(pull_request: PullRequest) -> dict[str, object]:
        return {"number": pull_request.number, "url": pull_request.url, "head": pull_request.head, "base": pull_request.base}

    @staticmethod
    def _source_observation(source: SourceProof) -> dict[str, object]:
        return {
            "candidate_snapshot_manifest_sha256": source.candidate_snapshot_manifest_sha256,
            "readme_ref": source.readme_ref, "readme_sha256": source.readme_sha256,
            "pr_body_ref": source.pr_body_ref, "pr_body_sha256": source.pr_body_sha256,
            "version_history_ref": source.version_history_ref, "version_history_sha256": source.version_history_sha256,
        }

    @staticmethod
    def _assert_exact_history(history: str, summary: object, pull_request: PullRequest | None) -> None:
        if not isinstance(summary, str):
            raise NativePublicReleaseError("history-link-invalid", "selected Version History summary is unavailable")
        rows = [line for line in history.splitlines() if summary in line]
        if len(rows) != 1:
            raise NativePublicReleaseError("history-link-invalid", "Version History needs one exact selected summary bullet")
        expected = f"- {summary}" if pull_request is None else _history_line(summary, pull_request)
        if rows[0] != expected:
            raise NativePublicReleaseError("history-link-invalid", "Version History summary must be a short exact bullet with its actual PR link")
