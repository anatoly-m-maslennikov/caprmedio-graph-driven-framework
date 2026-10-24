"""Small deterministic fixtures for shared-host launcher tests."""

import io
import json
from subprocess import CompletedProcess


IMAGE = "sha256:" + "a" * 64


class FakeRunner:
    def __init__(self, config, image=IMAGE, *, failure=False):
        self.config, self.image, self.failure, self.commands = config, image, failure, []

    def __call__(self, command, **kwargs):
        self.commands.append((command, kwargs))
        if self.failure:
            return CompletedProcess(command, 17, "", "daemon unavailable")
        if command[-4:] == ["ps", "--all", "-q", "shared-mcp"]:
            return CompletedProcess(command, 0, "container-id\n", "")
        if command[:3] == ["docker", "container", "inspect"]:
            row = {
                "Image": self.image,
                "State": {"Status": "running"},
                "Mounts": [
                    {
                        "Type": "bind",
                        "Source": str(self.config.projects_root),
                        "Destination": str(self.config.projects_root),
                        "RW": True,
                    },
                    {
                        "Type": "bind",
                        "Source": str(self.config.source_path),
                        "Destination": str(self.config.source_path),
                        "RW": False,
                    },
                ],
                "NetworkSettings": {
                    "Ports": {
                        "8092/tcp": [
                            {"HostIp": "127.0.0.1", "HostPort": str(self.config.http_port)}
                        ]
                    }
                },
            }
            return CompletedProcess(command, 0, json.dumps(row), "")
        return CompletedProcess(command, 0, "", "")


class FakeResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()


class FakeClock:
    def __init__(self):
        self.value = 0.0

    def __call__(self):
        return self.value

    def advance(self, seconds):
        self.value += seconds
