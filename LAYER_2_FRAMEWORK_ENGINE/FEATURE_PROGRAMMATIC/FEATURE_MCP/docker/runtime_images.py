"""Source-bound image admission for the explicit Project MCP launcher.

The Framework source closure is independent of the selected Project.  Only an
inspected immutable Docker image ID leaves this boundary; no runtime resources
are started, replaced or retired here.
"""

# CA-D-705@1
# CA-M-500@3

from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Callable
import hashlib
import json
import os
from pathlib import Path
import platform as host_platform
import re
import subprocess
import tempfile

try:
    from .image_reference import IMMUTABLE_IMAGE
    from .image_metadata import (
        OCI_VERSION_LABEL, docker_created_utc, read_framework_version,
    )
    from .image_display_tags import ensure_display_tag
    from .image_provenance import ImageBuildProvenance, label_arguments
    from .image_relation_registry import RELATION_REGISTRY_COMPILER
    from .image_relation_registry import compile_relation_registry as _compile_relation_registry
    from .image_relation_registry import WORKBENCH_SCHEMA_COMPILER
    from .image_relation_registry import compile_workbench_schema as _compile_workbench_schema
    from .image_relation_registry import TOOL_REGISTRY, TOOL_REGISTRY_COMPILER, TOOL_PROVIDERS
    from .image_relation_registry import compile_tool_registry as _compile_tool_registry
    from .image_docker_client import MAX_OUTPUT as _MAX_OUTPUT
    from .image_docker_client import bounded_run as _bounded_run
    from .image_docker_client import docker_client_environment as _docker_client_environment
except ImportError:  # direct execution/import with docker/ on sys.path
    from image_reference import IMMUTABLE_IMAGE
    from image_metadata import OCI_VERSION_LABEL, docker_created_utc, read_framework_version
    from image_display_tags import ensure_display_tag
    from image_provenance import ImageBuildProvenance, label_arguments
    from image_relation_registry import RELATION_REGISTRY_COMPILER
    from image_relation_registry import compile_relation_registry as _compile_relation_registry
    from image_relation_registry import WORKBENCH_SCHEMA_COMPILER
    from image_relation_registry import compile_workbench_schema as _compile_workbench_schema
    from image_relation_registry import TOOL_REGISTRY, TOOL_REGISTRY_COMPILER, TOOL_PROVIDERS
    from image_relation_registry import compile_tool_registry as _compile_tool_registry
    from image_docker_client import MAX_OUTPUT as _MAX_OUTPUT
    from image_docker_client import bounded_run as _bounded_run
    from image_docker_client import docker_client_environment as _docker_client_environment


ENGINE_ROOT = "LAYER_2_FRAMEWORK_ENGINE"
DOCKER_ROOT = ENGINE_ROOT + "/FEATURE_PROGRAMMATIC/FEATURE_MCP/docker"
DOCKERFILE = DOCKER_ROOT + "/Dockerfile"
DOCKERIGNORE = DOCKER_ROOT + "/Dockerfile.dockerignore"
RELATION_REGISTRY = (ENGINE_ROOT
                     + "/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/"
                     + "canonical_relation_registry.json")
WORKBENCH_SCHEMA = (ENGINE_ROOT
                    + "/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/"
                    + "workbench_schema.json")
_GENERATED_ASSETS = frozenset({RELATION_REGISTRY, WORKBENCH_SCHEMA, TOOL_REGISTRY})
SCHEMA_LABEL = "org.caprmedio.runtime.schema"
FINGERPRINT_LABEL = "org.caprmedio.runtime.fingerprint"
SCHEMA = "1"
_REQUIRED = ("pyproject.toml", "uv.lock", "version.toml", DOCKERFILE, DOCKERIGNORE)
_TRANSIENT_DIRECTORIES = frozenset({
    ".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    ".tox", ".nox", ".venv", ".virtualenv", "venv", "virtualenv",
    "node_modules", "testcache", ".testcache", "tmp",
})
_SECRET_FILES = frozenset({
    "auth.json", "credentials.json", "token.txt", "token.json", "secrets.json", "secrets.txt",
})
_CREDENTIAL_DIRECTORIES = frozenset({
    "vault", ".vault", "secrets", ".secrets", "credentials", ".credentials",
})
_PLATFORM = re.compile(r"linux/(?:amd64|arm64|arm|386|ppc64le|s390x|riscv64)(?:/v[0-9]+)?")
_DEFAULT_EXECUTOR = subprocess.run


class ImageError(RuntimeError):
    """One safe launcher condition, without captured Docker diagnostics."""

    def __init__(self, code: str, message: str | None = None):
        self.code = code
        defaults = {
            "IMAGE_INPUT_UNAVAILABLE": "Supply a readable --source-root Framework build closure",
            "IMAGE_REFUSED": "A matching immutable runtime image could not be admitted",
            "BUILD_FAILED": "Runtime image build did not produce an admitted immutable image",
        }
        super().__init__(message or defaults.get(code, "Runtime image operation failed"))


@dataclass(frozen=True)
class BuildInput:
    path: str
    sha256: str
    mode: int


@dataclass(frozen=True)
class ImageIdentity:
    fingerprint: str
    tag: str
    version: str
    platform: str
    manifest: tuple[BuildInput, ...]
    uid: int
    gid: int
    relation_registry: bytes
    workbench_schema: bytes
    tool_registry: bytes


def _canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def _excluded_directory(name: str) -> bool:
    return (name in _TRANSIENT_DIRECTORIES or name in _CREDENTIAL_DIRECTORIES
            or name.startswith(".caprmedio_"))


def _excluded_file(name: str) -> bool:
    return (_excluded_directory(name)
            or name == ".env" or name.startswith(".env.") or name.endswith(".env")
            or name in _SECRET_FILES or name == ".DS_Store"
            or Path(name).suffix in {".pyc", ".pyo", ".pem", ".key"})


def _unique_object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("duplicate image inspection member")
        value[key] = item
    return value


class ImageManager:
    def __init__(self, source_root: Path | str, executor: Callable[..., subprocess.CompletedProcess[str]] = _DEFAULT_EXECUTOR,
                 timeout: float = 600, *, uid: int | None = None, gid: int | None = None,
                 platform: str | None = None, build_temp_root: Path | str | None = None,
                 build_provenance: ImageBuildProvenance | None = None,
                 project_root: Path | str) -> None:
        self.source_root = Path(source_root)
        if project_root is None:
            raise ImageError("IMAGE_INPUT_UNAVAILABLE", "An explicit selected Project root is required")
        self.project_root = Path(project_root)
        self.build_temp_root = Path(build_temp_root) if build_temp_root is not None else None
        if build_provenance is not None and not isinstance(build_provenance, ImageBuildProvenance):
            raise ImageError("IMAGE_INPUT_UNAVAILABLE", "Image build provenance must be explicitly typed")
        self.build_provenance = build_provenance
        self.executor = executor
        if isinstance(timeout, bool) or not isinstance(timeout, (int, float)) or not 0 < timeout <= 900:
            raise ImageError("IMAGE_INPUT_UNAVAILABLE", "Image timeout must be within (0, 900] seconds")
        self.timeout = timeout
        self.uid = os.getuid() if uid is None else uid
        self.gid = os.getgid() if gid is None else gid
        for value in (self.uid, self.gid):
            if type(value) is not int or not 0 <= value <= 2147483647:
                raise ImageError("IMAGE_INPUT_UNAVAILABLE", "Runtime UID and GID must be bounded nonnegative integers")
        machine = host_platform.machine().lower()
        machine = {"aarch64": "arm64", "x86_64": "amd64"}.get(machine, machine)
        self.platform = "linux/" + machine if platform is None else platform
        if not isinstance(self.platform, str) or _PLATFORM.fullmatch(self.platform) is None:
            raise ImageError("IMAGE_INPUT_UNAVAILABLE", "Supply a supported explicit Linux image platform")

    @staticmethod
    def _input_error():
        return ImageError("IMAGE_INPUT_UNAVAILABLE",
                          "Framework image inputs are unavailable or changed; supply a readable --source-root build closure")

    def _root(self) -> Path:
        try:
            if self.source_root.is_symlink() or not self.source_root.is_dir():
                raise self._input_error()
            return self.source_root.resolve(strict=True)
        except (OSError, ValueError) as error:
            raise self._input_error() from error

    def _project_root(self) -> Path:
        try:
            if self.project_root.is_symlink() or not self.project_root.is_dir():
                raise self._input_error()
            return self.project_root.resolve(strict=True)
        except (OSError, ValueError) as error:
            raise self._input_error() from error

    def _generated_assets(self, root: Path) -> tuple[bytes, bytes, bytes]:
        try:
            project = self._project_root()
            registry = _compile_relation_registry(
                root, project, timeout=self.timeout, max_output=_MAX_OUTPUT,
            )
            schema = _compile_workbench_schema(
                root, project, timeout=self.timeout, max_output=_MAX_OUTPUT,
            )
            tools = _compile_tool_registry(root, timeout=self.timeout, max_output=_MAX_OUTPUT)
        except Exception as error:
            raise self._input_error() from error
        if not all(isinstance(asset, bytes) and asset for asset in (registry, schema, tools)):
            raise self._input_error()
        return registry, schema, tools

    def _build_parent(self) -> Path:
        temporary = self._project_root() / ".caprmedio_tmp"
        parent = self.build_temp_root or temporary
        try:
            if (temporary.is_symlink() or not temporary.is_dir()
                    or parent.is_symlink() or not parent.is_dir()):
                raise OSError("unsafe private image temporary root")
            expected = temporary.resolve(strict=True)
            resolved = parent.resolve(strict=True)
            if (not parent.is_absolute() or ".." in parent.parts or resolved != parent
                    or not resolved.is_relative_to(expected)):
                raise OSError("unsafe private image temporary root")
            return resolved
        except (OSError, ValueError) as error:
            raise ImageError("BUILD_FAILED", "Private image build context is unavailable") from error

    def _file(self, root: Path, relative: str) -> Path:
        path = root
        for part in Path(relative).parts:
            path /= part
            if path.is_symlink():
                raise self._input_error()
        if not path.is_file():
            raise self._input_error()
        return path

    def _files(self, root: Path) -> tuple[Path, ...]:
        required = tuple(self._file(root, relative) for relative in _REQUIRED)
        engine = root / ENGINE_ROOT
        if engine.is_symlink() or not engine.is_dir():
            raise self._input_error()
        selected = set(required)

        def unavailable(_error):
            raise self._input_error()

        for current, directories, names in os.walk(engine, followlinks=False, onerror=unavailable):
            folder = Path(current)
            retained = []
            for name in sorted(directories):
                if _excluded_directory(name) or _excluded_file(name):
                    continue
                path = folder / name
                if path.is_symlink() or not path.is_dir():
                    raise self._input_error()
                retained.append(name)
            directories[:] = retained
            for name in sorted(names):
                if _excluded_file(name):
                    continue
                path = folder / name
                relative = path.relative_to(root).as_posix()
                if relative in _GENERATED_ASSETS:
                    if path.is_symlink() or not path.is_file():
                        raise self._input_error()
                    continue
                if path.is_symlink() or not path.is_file():
                    raise self._input_error()
                selected.add(path)
        return tuple(sorted(selected, key=lambda path: path.relative_to(root).as_posix()))

    def identity(self, *, use_packaged_assets: bool = False) -> ImageIdentity:
        """Fingerprint the source closure with fresh or packaged generated assets."""
        root = self._root()
        try:
            version = read_framework_version(self._file(root, "version.toml"))
            if use_packaged_assets:
                registry, schema, tools = (
                    self._file(root, path).read_bytes()
                    for path in (RELATION_REGISTRY, WORKBENCH_SCHEMA, TOOL_REGISTRY)
                )
                if not all((registry, schema, tools)):
                    raise self._input_error()
            else:
                registry, schema, tools = self._generated_assets(root)
            rows = [BuildInput(path.relative_to(root).as_posix(),
                               hashlib.sha256(path.read_bytes()).hexdigest(),
                               path.stat().st_mode & 0o777)
                    for path in self._files(root)]
            rows.append(BuildInput(RELATION_REGISTRY, hashlib.sha256(registry).hexdigest(), 0o644))
            rows.append(BuildInput(WORKBENCH_SCHEMA, hashlib.sha256(schema).hexdigest(), 0o644))
            rows.append(BuildInput(TOOL_REGISTRY, hashlib.sha256(tools).hexdigest(), 0o644))
            rows = tuple(sorted(rows, key=lambda row: row.path))
        except (OSError, ValueError, UnicodeError) as error:
            raise self._input_error() from error
        payload = {"schema": SCHEMA, "platform": self.platform,
                   "build_arguments": {"RUNTIME_UID": self.uid, "RUNTIME_GID": self.gid},
                   "files": [[row.path, row.sha256, row.mode] for row in rows]}
        fingerprint = hashlib.sha256(_canonical(payload)).hexdigest()
        return ImageIdentity(fingerprint, "caprmedio-runtime:inputs-" + fingerprint, version,
                             self.platform, rows, self.uid, self.gid, registry, schema, tools)

    def _run(self, argv, *, code="IMAGE_REFUSED", cwd=None, buildx_config=None,
             allow_failure=False):
        build = len(argv) > 1 and argv[1] == "build"
        try:
            if self.executor is _DEFAULT_EXECUTOR:
                result = _bounded_run(list(argv), cwd=cwd or self._root(), timeout=self.timeout,
                                      capture_stdout=not build, max_output=_MAX_OUTPUT,
                                      buildx_config=buildx_config)
            else:
                # Test executors keep the existing CompletedProcess interface.
                kwargs = {"cwd": cwd or self._root(), "stdin": subprocess.DEVNULL,
                          "capture_output": True, "text": True, "shell": False,
                          "timeout": self.timeout, "check": False}
                if buildx_config is not None:
                    kwargs["env"] = _docker_client_environment(buildx_config=buildx_config)
                result = self.executor(list(argv), **kwargs)
        except subprocess.TimeoutExpired:
            message = ("Image build timed out; its effect is uncertain and was not retried"
                       if code == "BUILD_FAILED" else "Docker image inspection timed out")
            raise ImageError(code, message) from None
        except (OSError, ValueError):
            raise ImageError(code, "Docker image operation is unavailable") from None
        if (not isinstance(result, subprocess.CompletedProcess)
                or type(result.returncode) is not int):
            raise ImageError(code, "Docker image operation failed")
        if result.returncode != 0:
            if allow_failure:
                return None
            raise ImageError(code, "Docker image operation failed")
        output = "" if build else result.stdout
        if not isinstance(output, str) or len(output.encode("utf-8")) > _MAX_OUTPUT:
            raise ImageError(code, "Docker image output is incomplete or invalid")
        return output

    def _inspect_details(self, image: str, identity: ImageIdentity, *,
                         code: str = "IMAGE_REFUSED", built: bool = False) -> str:
        raw = self._run(("docker", "image", "inspect", image), code=code)
        try:
            values = json.loads(raw, object_pairs_hook=_unique_object)
            if not isinstance(values, list) or len(values) != 1 or not isinstance(values[0], dict):
                raise ValueError("one image is required")
            value = values[0]
            labels = value["Config"]["Labels"]
            if built and self.build_provenance is not None:
                if not isinstance(labels, dict) or any(labels.get(key) != expected for key, expected in self.build_provenance.labels().items()):
                    raise ValueError("built image provenance differs")
            platform = identity.platform.split("/")
            if (value["Id"] != image or not isinstance(labels, dict)
                    or labels.get(SCHEMA_LABEL) != SCHEMA
                    or labels.get(FINGERPRINT_LABEL) != identity.fingerprint
                    or labels.get(OCI_VERSION_LABEL) != identity.version
                    or value.get("Os") != platform[0] or value.get("Architecture") != platform[1]
                    or (len(platform) == 3 and value.get("Variant") != platform[2])):
                raise ValueError("image identity differs")
            created = value["Created"]
            docker_created_utc(created)
        except (ValueError, TypeError, KeyError) as error:
            raise ImageError(code, "Image schema, source fingerprint, platform or immutable identity does not match") from error
        return created

    def _inspect(self, image: str, identity: ImageIdentity, *, code: str = "IMAGE_REFUSED", built: bool = False) -> str:
        self._inspect_details(image, identity, code=code, built=built)
        return image

    def ensure_display_tag(self, image: str, version: str, created: object) -> str:
        return ensure_display_tag(
            self._run, image, version, created,
            lambda message: ImageError("IMAGE_REFUSED", message),
        )

    def _current(self, identity: ImageIdentity, *, use_packaged_assets: bool = False):
        if self.identity(use_packaged_assets=use_packaged_assets) != identity:
            raise self._input_error()

    def resolve(self, explicit_id: str | None = None, build_if_missing: bool = True) -> str:
        if explicit_id is not None and (not isinstance(explicit_id, str)
                                       or IMMUTABLE_IMAGE.fullmatch(explicit_id) is None):
            raise ImageError("IMAGE_REFUSED", "An explicit image must be one lowercase immutable sha256 ID")
        if type(build_if_missing) is not bool:
            raise ImageError("IMAGE_REFUSED", "Image build selection must be a boolean")
        use_packaged_assets = not build_if_missing
        identity = self.identity(use_packaged_assets=use_packaged_assets)
        if explicit_id is not None:
            image = explicit_id
            created = self._inspect_details(explicit_id, identity)
        else:
            raw = self._run(("docker", "image", "ls", "--all", "--quiet", "--no-trunc",
                             "--filter", f"label={SCHEMA_LABEL}={SCHEMA}",
                             "--filter", f"label={FINGERPRINT_LABEL}={identity.fingerprint}"))
            ids = {line.strip() for line in raw.splitlines() if line.strip()}
            if any(IMMUTABLE_IMAGE.fullmatch(value) is None for value in ids) or len(ids) > 1:
                raise ImageError("IMAGE_REFUSED", "Matching local image identity is invalid or ambiguous")
            if ids:
                image = next(iter(ids))
                created = self._inspect_details(image, identity)
            elif build_if_missing:
                self._current(identity)
                return self._build(identity)
            else:
                raise ImageError("IMAGE_REFUSED", "No matching local runtime image is present; build is disabled")
        self._current(identity, use_packaged_assets=use_packaged_assets)
        self.ensure_display_tag(image, identity.version, created)
        return image

    def _build(self, identity: ImageIdentity) -> str:
        """Build one image, then add its inspect-derived display tag if safe."""
        self._current(identity)
        try:
            # Retain one private attempt as build evidence.  Cleanup must never
            # mask a build result or retry a denied directory deletion.
            parent = self._build_parent()
            attempt = Path(tempfile.mkdtemp(prefix="caprmedio-runtime-image-", dir=parent))
            attempt.chmod(0o700)
            context = attempt / "context"
            context.mkdir()
            buildx = attempt / "buildx"
            buildx.mkdir(mode=0o700)
            buildx.chmod(0o700)
        except OSError as error:
            raise ImageError("BUILD_FAILED", "Private image build context is unavailable") from error
        self._assemble(context, identity)
        iidfile = attempt / "image.id"
        self._current(identity)
        self._verify_context(context, identity)
        command = ("docker", "build", "--iidfile", str(iidfile),
                   "--label", f"{SCHEMA_LABEL}={SCHEMA}",
                   "--label", f"{FINGERPRINT_LABEL}={identity.fingerprint}",
                   "--label", f"{OCI_VERSION_LABEL}={identity.version}",
                   *label_arguments(self.build_provenance),
                   "--platform", identity.platform,
                   "--build-arg", f"RUNTIME_UID={identity.uid}",
                   "--build-arg", f"RUNTIME_GID={identity.gid}",
                   "--file", str(context / DOCKERFILE), str(context))
        self._run(command, code="BUILD_FAILED", cwd=context, buildx_config=buildx)
        self._current(identity)
        self._verify_context(context, identity)
        try:
            if iidfile.is_symlink() or not iidfile.is_file() or iidfile.stat().st_size > 1024:
                raise ValueError("immutable builder identity is absent")
            image = iidfile.read_text(encoding="ascii").strip()
            if IMMUTABLE_IMAGE.fullmatch(image) is None:
                raise ValueError("immutable builder identity is invalid")
        except (OSError, ValueError, UnicodeError) as error:
            raise ImageError("BUILD_FAILED", "Builder did not capture one immutable sha256 image ID") from error
        created = self._inspect_details(image, identity, code="BUILD_FAILED", built=True)
        self.ensure_display_tag(image, identity.version, created)
        self._current(identity)
        self._verify_context(context, identity)
        return image

    def _assemble(self, context: Path, identity: ImageIdentity):
        root = self._root()
        try:
            for row in identity.manifest:
                if row.path == RELATION_REGISTRY:
                    payload = identity.relation_registry
                elif row.path == WORKBENCH_SCHEMA:
                    payload = identity.workbench_schema
                elif row.path == TOOL_REGISTRY:
                    payload = identity.tool_registry
                else:
                    source = self._file(root, row.path)
                    payload = source.read_bytes()
                if hashlib.sha256(payload).hexdigest() != row.sha256:
                    raise self._input_error()
                destination = context / row.path
                destination.parent.mkdir(parents=True, exist_ok=True)
                with destination.open("xb") as stream:
                    stream.write(payload)
                destination.chmod(row.mode)
                if row.path not in _GENERATED_ASSETS and source.stat().st_mode & 0o777 != row.mode:
                    raise self._input_error()
        except OSError as error:
            raise ImageError("BUILD_FAILED", "Private image context could not be assembled") from error
        self._verify_context(context, identity)

    def _verify_context(self, context: Path, identity: ImageIdentity):
        expected = {row.path: row for row in identity.manifest}
        expected_directories = {parent.as_posix() for row in identity.manifest
                                for parent in Path(row.path).parents if parent != Path(".")}
        observed = set()
        observed_directories = set()
        if context.is_symlink() or not context.is_dir():
            raise self._input_error()

        def unavailable(_error):
            raise self._input_error()

        try:
            for current, directories, names in os.walk(context, followlinks=False, onerror=unavailable):
                folder = Path(current)
                for name in directories:
                    path = folder / name
                    relative = path.relative_to(context).as_posix()
                    if (relative not in expected_directories
                            or path.is_symlink() or not path.is_dir()):
                        raise self._input_error()
                    observed_directories.add(relative)
                for name in names:
                    path = folder / name
                    relative = path.relative_to(context).as_posix()
                    if relative not in expected or path.is_symlink() or not path.is_file():
                        # Reject an unadmitted name before any content read.
                        raise self._input_error()
                    row = expected[relative]
                    if (hashlib.sha256(path.read_bytes()).hexdigest() != row.sha256
                            or path.stat().st_mode & 0o777 != row.mode):
                        raise self._input_error()
                    observed.add(relative)
        except OSError as error:
            raise self._input_error() from error
        if observed != expected.keys() or observed_directories != expected_directories:
            raise self._input_error()
