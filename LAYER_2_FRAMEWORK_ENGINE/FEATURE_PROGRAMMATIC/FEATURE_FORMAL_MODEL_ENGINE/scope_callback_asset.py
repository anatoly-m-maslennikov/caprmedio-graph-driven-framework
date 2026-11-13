"""Build and load the reviewed Scope structural-level callback."""
import ast
import importlib.util
import sys
import base64
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from importlib.machinery import SourcelessFileLoader
import py_compile
import json
from pathlib import Path

from FEATURE_FORMAL_MODEL_ENGINE.compiler_claim import compile_scope_level_with_check
from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import parse_native_model_claim
from FEATURE_FORMAL_MODEL_ENGINE.scope_levels import ScopeUnit
from carrier_aliases import carrier_read_view, matches_named_value
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier

from markdown_it import MarkdownIt


def formal_claim(body):
    headings, found = [], []
    tokens = MarkdownIt("commonmark").parse(body)
    for index, token in enumerate(tokens):
        if token.type == "heading_open":
            level = int(token.tag[1:])
            headings = [item for item in headings if item[0] < level]
            headings.append((level, tokens[index + 1].content.strip().casefold()))
        elif (token.type == "fence" and token.info.strip().casefold() == "python"
              and tuple(name for _, name in headings) == ("claim", "formal claim")):
            found.append(token.content)
    if len(found) != 1:
        raise ValueError("Expected one Python Formal Claim")
    return found[0]


def generated_assets(raw, *, pin, release_sources):
    """Build only a source revision selected by the trusted release frontier."""
    if pin is None:
        return None
    if pin not in release_sources:
        raise ValueError("No selected release source pin")
    parsed = parse_carrier(raw, Path("scope-source.md"))
    view = carrier_read_view(parsed.metadata)
    if (view.get("atom_id") != pin["atom_id"] or view.get("ref_id") != pin["atom_id"]
            or view.get("version") != pin["version"] or str(view.get("status", "")).casefold() != "active"):
        raise ValueError("Source is not the selected Current revision")
    if (not matches_named_value(view.get("role"), "Requirement")
            or not matches_named_value(view.get("form"), "Declaration")):
        raise ValueError("Source must be a Requirement Declaration")
    if sha256(raw).hexdigest() != pin["carrier_sha256"]:
        raise ValueError("Source Carrier does not match release pin")
    claim = formal_claim(parsed.body)
    if sha256(claim.encode()).hexdigest() != pin["claim_sha256"]:
        raise ValueError("Claim does not match release pin")
    declaration = parse_native_model_claim(claim)
    check = declaration.get("instance_check")
    if check is None or check["parameter_type"] != "ScopeUnit":
        raise ValueError("Expected the Scope Unit instance check")
    statements, check = compile_scope_level_with_check(declaration)
    # This narrow asset supports only local names and selected pure builtins.
    # Reject unresolved imported/global dependencies before emitting code.
    tree = ast.parse(check["source"])
    locals_ = {check["parameter"], check["name"]}
    locals_.update(node.id for node in ast.walk(tree) if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store))
    allowed = locals_ | {"ScopeUnit", "bool", "None", "True", "False", "abs", "min", "max", "len"}
    unknown = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load)} - allowed
    if unknown:
        raise ValueError("Unsupported Scope check dependencies: " + ", ".join(sorted(unknown)))

    reference = f'{pin["atom_id"]}@{pin["version"]}'
    prefix = (
        "# Generated from the selected reviewed Formal Claim.\n"
        f"SOURCE_REFERENCE = {reference!r}\n"
        f"SOURCE_SHA256 = {pin['carrier_sha256']!r}\n"
        f"CLAIM_SHA256 = {pin['claim_sha256']!r}\n"
        "from FEATURE_FORMAL_MODEL_ENGINE.scope_levels import ScopeUnit\n\n"
    )
    source = (prefix + check["source"] + "\n").encode()
    snapshot = (json.dumps({reference: base64.b64encode(raw).decode("ascii")},
                           sort_keys=True, separators=(",", ":")) + "\n").encode()
    return {"source": source, "snapshot": snapshot, "statements": statements,
            "entry_point": check["name"], "reference": reference, "trusted_artifact_sha256": pin["artifact_sha256"]}


def write_package(directory, generated):
    """Create a fixed Python module and reviewed-source snapshot at asset refresh."""
    directory.mkdir(parents=True, exist_ok=True)
    module = directory / "scope_level_check.py"
    snapshot = directory / "scope_level_sources.json"
    module.write_bytes(generated["source"])
    snapshot.write_bytes(generated["snapshot"])
    artifact = directory / "scope_level_check.bin"
    py_compile.compile(str(module), cfile=str(artifact), dfile="scope_level_check.py", doraise=True, invalidation_mode=py_compile.PycInvalidationMode.CHECKED_HASH)
    artifact_sha256 = sha256(artifact.read_bytes()).hexdigest()
    if artifact_sha256 != generated["trusted_artifact_sha256"]:
        raise ValueError("Scope artifact differs from reviewed source selection")
    metadata = {
        "artifact_sha256": artifact_sha256,
        "python_magic": importlib.util.MAGIC_NUMBER.hex(),
        "python_version": list(sys.version_info[:3]),
        "module_sha256": sha256(generated["source"]).hexdigest(),
        "snapshot_sha256": sha256(generated["snapshot"]).hexdigest(),
        "reference": generated["reference"],
        "entry_point": generated["entry_point"],
    }
    (directory / "scope_level_metadata.json").write_text(json.dumps(metadata, sort_keys=True) + "\n")
    return metadata


def load_packaged_module(directory, *, release_pin):
    """Load only packaged Python; release_pin is trusted build metadata."""
    metadata = json.loads((directory / "scope_level_metadata.json").read_text())
    if metadata != release_pin:
        raise ValueError("Installed Scope metadata changed")
    module_path = directory / "scope_level_check.py"
    if sha256(module_path.read_bytes()).hexdigest() != release_pin["module_sha256"]:
        raise ValueError("Installed Scope predicate changed")
    artifact_path = directory / "scope_level_check.bin"
    artifact = artifact_path.read_bytes()
    if (release_pin.get("python_magic") != importlib.util.MAGIC_NUMBER.hex()
            or release_pin.get("python_version") != list(sys.version_info[:3])
            or not artifact.startswith(importlib.util.MAGIC_NUMBER)):
        raise ValueError("Scope artifact requires a different Python interpreter")
    if sha256(artifact).hexdigest() != release_pin["artifact_sha256"]:
        raise ValueError("Installed Scope artifact changed")
    spec = spec_from_file_location("scope_level_check", artifact_path, loader=SourcelessFileLoader("scope_level_check", str(artifact_path)))
    if spec is None or spec.loader is None:
        raise ValueError("Installed Scope predicate is unavailable")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    if module.SOURCE_REFERENCE != release_pin["reference"]:
        raise ValueError("Installed Scope predicate reference changed")
    return getattr(module, release_pin["entry_point"])


def verify_packaged_assets(directory, raw, *, pin, release_sources):
    """Validate prebuilt release bytes without writing or evaluating a callback."""
    generated = generated_assets(raw, pin=pin, release_sources=release_sources)
    metadata = json.loads((directory / "scope_level_metadata.json").read_bytes())
    module = (directory / "scope_level_check.py").read_bytes()
    snapshot = (directory / "scope_level_sources.json").read_bytes()
    artifact = (directory / "scope_level_check.bin").read_bytes()
    if (module != generated["source"] or snapshot != generated["snapshot"]
            or metadata.get("reference") != generated["reference"]
            or metadata.get("entry_point") != generated["entry_point"]
            or metadata.get("module_sha256") != sha256(module).hexdigest()
            or metadata.get("snapshot_sha256") != sha256(snapshot).hexdigest()
            or metadata.get("artifact_sha256") != sha256(artifact).hexdigest()
            or metadata.get("artifact_sha256") != pin.get("artifact_sha256")
            or metadata.get("python_magic") != importlib.util.MAGIC_NUMBER.hex()
            or metadata.get("python_version") != list(sys.version_info[:3])
            or not artifact.startswith(importlib.util.MAGIC_NUMBER)):
        raise ValueError("Invalid packaged Scope assets")
    return metadata
