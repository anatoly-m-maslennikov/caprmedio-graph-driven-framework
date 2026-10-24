"""Prepare or explicitly start one host-wide HTTP MCP container."""

from __future__ import annotations
import argparse
import json
from pathlib import Path
import subprocess
import time
from typing import Any, Callable
from urllib.request import urlopen

from shared_mcp_launch_support import (  # noqa: E402
    SharedLaunchError,
    bounded,
    health_ready,
    inspect_runtime,
    prepare_config,
)


class SharedMcpLauncher:
    """No Docker call is made until ``apply`` is explicitly requested."""

    def __init__(
        self,
        runner: Callable[..., Any] | None = None,
        opener: Callable[..., Any] | None = None,
        sleeper=time.sleep,
        clock=time.monotonic,
    ):
        self.runner = runner or subprocess.run
        self.opener = opener or urlopen
        self.sleeper = sleeper
        self.clock = clock

    def prepare(self, settings_path=None, image=None, *, compose_file=None, timeout=120):
        return prepare_config(settings_path, image, compose_file=compose_file, timeout=timeout)

    def _docker(self, command, environment, timeout):
        try:
            return self.runner(
                command,
                env=environment,
                capture_output=True,
                text=True,
                timeout=timeout,
                check=False,
            )
        except Exception:
            return None

    def apply(
        self,
        settings_path=None,
        image=None,
        *,
        compose_file=None,
        timeout=120,
        readiness_timeout=30,
    ):
        prepared = self.prepare(settings_path, image, compose_file=compose_file, timeout=timeout)
        readiness_budget = bounded(readiness_timeout, "readiness_timeout", 30)
        started = self._docker(prepared["command"], prepared["environment"], timeout)
        if started is None or getattr(started, "returncode", 1) != 0:
            return {
                key: prepared[key]
                for key in ("service", "image", "settings_path", "projects_root", "http_port")
            } | {
                "outcome": "failed",
                "ready": False,
                "condition": "docker_start_failed",
                "docker_returncode": getattr(started, "returncode", None),
            }
        deadline = self.clock() + readiness_budget
        while self.clock() < deadline:
            observed = inspect_runtime(self._docker, prepared, deadline, self.clock)
            if observed is False:
                return {
                    "outcome": "failed",
                    "ready": False,
                    "condition": "runtime_mismatch",
                    "service": "shared-mcp",
                }
            if (
                observed
                and health_ready(self.opener, prepared["http_port"], deadline, self.clock)
                and self.clock() <= deadline
            ):
                return {
                    "outcome": "started",
                    "ready": True,
                    "condition": "ready",
                    "service": "shared-mcp",
                    "image": prepared["image"],
                    "http_port": prepared["http_port"],
                    "shared_runtime_id": prepared["shared_runtime_id"],
                }
            remaining = deadline - self.clock()
            if remaining <= 0:
                break
            self.sleeper(min(0.25, remaining))
        return {
            "outcome": "started",
            "ready": False,
            "condition": "readiness_failed",
            "service": "shared-mcp",
        }


Launcher = SharedMcpLauncher


def prepare(settings_path=None, image=None, **kwargs):
    return SharedMcpLauncher().prepare(settings_path, image, **kwargs)


def apply(settings_path=None, image=None, **kwargs):
    return SharedMcpLauncher().apply(settings_path, image, **kwargs)


def _public_result(result):
    public = {key: value for key, value in result.items() if key not in {"config", "environment"}}
    if result.get("mode") == "dry-run":
        public["environment"] = {
            key: value
            for key, value in result["environment"].items()
            if key.startswith("CAPRMEDIO_")
        }
    return public


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host-settings", "--settings", dest="settings_path")
    parser.add_argument("--image", required=True)
    parser.add_argument("--compose-file", type=Path)
    parser.add_argument("--startup-timeout", type=int, default=120)
    parser.add_argument("--readiness-timeout", type=int, default=30)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)
    try:
        launcher = SharedMcpLauncher()
        result = (launcher.apply if args.apply else launcher.prepare)(
            args.settings_path,
            args.image,
            compose_file=args.compose_file,
            timeout=args.startup_timeout,
            **({"readiness_timeout": args.readiness_timeout} if args.apply else {}),
        )
    except SharedLaunchError as error:
        result = {"outcome": "refused", "ready": False, "condition": str(error)}
    print(
        json.dumps(
            _public_result(result),
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if result.get("mode") == "dry-run" or result.get("ready") is True else 1


if __name__ == "__main__":
    raise SystemExit(main())
