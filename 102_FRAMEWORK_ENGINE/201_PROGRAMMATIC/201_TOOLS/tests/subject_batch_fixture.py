"""Disposable current-authority batch fixture; native effects stay real."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
APP = TOOLS.parent / "203_APPS/WORKFLOW_ORCHESTRATOR"
for location in (TOOLS, APP, TOOLS / "ATOM_UPDATE/tests"):
    sys.path.insert(0, str(location))

from atom_subject_patch import prepare_subject_intent  # noqa: E402
from ATOM_UPDATE.atom_update import SOURCE_PINS  # noqa: E402
from lifecycle_intents import carrier_descriptor  # noqa: E402
from selected_execution import SelectedExecution  # noqa: E402
from subject_batch import build_subject_batch_requested_runs  # noqa: E402
from test_subject_apply_portfolio import REPOSITORY, SubjectApplyProject  # noqa: E402
from selected_workflows_docker_fixture import digest  # noqa: E402


class SubjectBatchProject:
    def __init__(self, case, *, count=2, role="Requirement", status="Active"):
        scratch = REPOSITORY / ".caprmedio_tmp/tests/subject-batch"
        scratch.mkdir(parents=True, exist_ok=True)
        directory = tempfile.TemporaryDirectory(dir=scratch)
        case.addCleanup(directory.cleanup)
        self.fixture = SubjectApplyProject(Path(directory.name).resolve(), role=role, status=status)
        self.root, self.golden = self.fixture.root, self.fixture.golden
        report = self.fixture.parameters["semantic_assessment_report"]
        (self.root / report["path"]).unlink()
        for pin in SOURCE_PINS:
            destination = self.root / pin["path"]
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPOSITORY / pin["path"], destination)
        self.paths = [self.fixture.path]
        self.paths.extend(
            self.golden.status_atom(role, status, number=8100 + ordinal)
            for ordinal in range(1, count)
        )
        self.before = {path: path.read_bytes() for path in self.paths}
        self.targets = [
            carrier_descriptor(self.root, path.relative_to(self.root).as_posix())
            for path in self.paths
        ]
        self.git("init", "--quiet")
        self.git("add", ".caprmedio_caprmedio")
        self.git(
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "--quiet",
            "-m",
            "Fixture pre-state",
        )
        self.packet = {
            "schema_version": 1,
            "subject_profile": "approved",
            "git_checkpoint": self.git("rev-parse", "HEAD").strip(),
            "atoms": [
                {"target": target, "subject_patches": self.fixture.patches}
                for target in self.targets
            ],
        }
        self.packet_path = self.root / ".caprmedio_tmp/subject-batch.json"
        self.packet_path.parent.mkdir(parents=True, exist_ok=True)
        self.save_packet()

    def git(self, *arguments):
        return subprocess.run(
            ["git", *arguments],
            cwd=self.root,
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        ).stdout

    def save_packet(self):
        raw = json.dumps(self.packet, ensure_ascii=False, sort_keys=True).encode()
        self.packet_path.write_bytes(raw)
        self.parameters = {
            "subject_batch": {
                "path": self.packet_path.relative_to(self.root).as_posix(),
                "digest": hashlib.sha256(raw).hexdigest(),
            }
        }
        self.golden._semantic_update_parameters = self.parameters

    def use_reviewed_packet(self, pin):
        self.parameters = {"subject_batch": pin}
        self.packet_path = self.root / pin["path"]
        self.packet = json.loads(self.packet_path.read_bytes())
        self.golden._semantic_update_parameters = self.parameters

    def execution(self, run_id="subject-batch-fixture", *, request_transform=None):
        request = self.golden.request(request_id=run_id)
        frontier, effects = [], []
        for item in self.packet["atoms"]:
            prepared = prepare_subject_intent(
                self.root, item["target"], item["subject_patches"], subject_profile="approved"
            )
            target = item["target"]
            if prepared["subject_intent"]["noop"]:
                frontier.append(target["path"])
                continue
            archive = prepared["subject_intent"]["predecessorArchive"]
            frontier.extend([target["path"], archive["path"]])
            effects.extend(
                [
                    {
                        "type": "subjectUpdate",
                        "path": target["path"],
                        "atom_id": target["atom_id"],
                        "before_version": target["version"],
                        "version": target["version"] + 1,
                        "subject_intent_sha256": prepared["subject_intent_sha256"],
                    },
                    {"type": "predecessorArchive", **archive},
                ]
            )
        request.update(
            target_frontier=frontier,
            target_frontier_digest=digest(frontier),
            effects=effects,
            effects_digest=digest(effects),
        )
        if request_transform is not None:
            request_transform(request)
            request["target_frontier_digest"] = digest(request["target_frontier"])
            request["effects_digest"] = digest(request["effects"])
        runner = SelectedExecution(self.root)
        graph_request = {**request, "mode": "execute"}
        graph = runner._validate_graph(graph_request)
        tracker = runner._shared_tracker({"graph": graph, "request": {"execution": graph_request}})
        preview = tracker.run_selected_operation(request)
        runs = build_subject_batch_requested_runs(graph, run_id, len(self.packet["atoms"]))
        with patch.object(self.golden, "_requested_runs", return_value=runs):
            execute = self.golden.request(
                request_id=run_id,
                mode="execute",
                receipt=preview["proposal_receipt"],
                receipt_digest=preview["proposal_receipt_digest"],
            )
        for field in ("target_frontier", "target_frontier_digest", "effects", "effects_digest"):
            execute[field] = request[field]
        for field in ("target_frontier_digest", "effects_digest"):
            execute["operator_authorization"][field] = request[field]
        return runner, runner.freeze(
            {"operation": "enqueue_selected", "run_id": run_id, "execution": execute}
        )

    def archives(self):
        return [
            self.root
            / prepare_subject_intent(
                self.root, item["target"], item["subject_patches"], subject_profile="approved"
            )["subject_intent"]["predecessorArchive"]["path"]
            for item in self.packet["atoms"]
        ]
