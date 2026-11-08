# CA-M-508@5
# CA-E-799@3
# CA-E-800@3
"""Owned Docker boundary shared by the short guard and opt-in soak."""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import unittest
from uuid import uuid4


ROOT = Path(__file__).resolve().parents[5]
RUNNER = Path(__file__).with_name("workbench_soak_runner.py").relative_to(ROOT)


def run_resource_case(case: unittest.TestCase, seconds: int) -> None:
    image = os.environ["CAPRMEDIO_IMAGE"]
    name = f"caprmedio-workbench-resource-{uuid4().hex}"
    command = [
        "docker", "run", "--rm", "--name", name,
        "--label", "caprmedio.test=workbench-resource",
        "--cpus=1", "--memory=1536m", "--memory-swap=1536m",
        "--tmpfs", "/tmp:rw,nosuid,nodev,size=256m",
    ]
    # Test containers must never look like an installed Project service.
    for label in ("project", "service", "control_root", "host_project_root"):
        command += ["--label", f"org.caprmedio.{label}="]
    command += [
        "--env", f"CAPRMEDIO_IMAGE={image}",
        "--entrypoint", "/opt/venv/bin/python", image, str(RUNNER),
        "--seconds", str(seconds),
    ]
    try:
        result = subprocess.run(
            command, cwd=ROOT, text=True, capture_output=True,
            timeout=seconds + 600, check=False,
        )
        print(result.stdout, end="", flush=True)
        print(result.stderr, end="", flush=True)
        case.assertEqual(0, result.returncode, result.stdout[-12000:] + result.stderr[-12000:])
        records = [
            json.loads(line.removeprefix("WORKBENCH_RESOURCE "))
            for line in result.stdout.splitlines() if line.startswith("WORKBENCH_RESOURCE ")
        ]
        case.assertTrue(records, "runner must report resource acceptance")
    finally:
        subprocess.run(["docker", "rm", "--force", name], capture_output=True, check=False)
