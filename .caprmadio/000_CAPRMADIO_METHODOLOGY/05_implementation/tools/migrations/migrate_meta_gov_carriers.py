#!/usr/bin/env python3
"""Migrate root META/GOV methodology artifacts to their canonical carriers.

Invocation:
    python migrate_meta_gov_carriers.py [ROOT] [--apply | --check]
        [--expect-plan-digest SHA256]

``ROOT`` is the target repository root; it defaults to this script's discovered
repository root. Without a mode flag the program prints a validated dry-run
plan. ``--apply`` stages all replacement bytes under
``ROOT/.caprmadio_runtime/migrations`` and then applies the plan transactionally.
``--expect-plan-digest`` binds apply to the digest printed by a prior preview.
``--check`` verifies the completed migration without writing. The migration is
bounded to ``11_layer_meta`` and ``12_layer_gov``: it converts Markdown
property blocks to YAML, adds explicit YAML properties where needed, and
converts TOML-encoded JSON Schemas to canonical JSON while preserving executable
human-edited TOML configuration. Unknown structures, parse failures, symlinks,
collisions, preimage changes, or failed postconditions abort with exit status
1; successful previews, checks, and applies exit 0.
"""

# ruff: noqa: E402, E501

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import tomllib
from dset_migration_tools.models import (
    DeleteOperation,
    MigrationError,
    MigrationPlan,
    WriteOperation,
)
from dset_migration_tools.safety import read_regular_file as _read_regular_file
from dset_migration_tools.safety import sha256 as _sha256
from dset_migration_tools.transaction import apply_transaction

sys.dont_write_bytecode = True

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from dset_toolchain.frontmatter import (  # noqa: E402
    FrontmatterError,
)
from dset_toolchain.frontmatter import (
    parse as parse_frontmatter,
)
from dset_toolchain.frontmatter import (
    render as render_frontmatter,
)

MIGRATION_ROOTS = ("11_layer_meta", "12_layer_gov")
SCHEMA_SUFFIX = ".schema.toml"
JSON_SCHEMA_SUFFIX = ".schema.json"
CONFIGURATION_TOML_NAMES = {
    "010_dset-meta-templates-dset-settings.toml",
    "000_dset-meta-templates-package-layered-package.toml",
    "030_dset-gov-templates-change-dependency-map.toml",
    "000_dset-gov-templates-change-layered-change.toml",
    "040_dset-gov-templates-governance-core-v1-profile.toml",
    "060_dset-gov-templates-profiles.toml",
    "090_dset-gov-templates-dset-settings.toml",
    "100_dset-gov-templates-artifact-catalog.toml",
}
TEMPLATE_ROUTES: tuple[tuple[str, str, str | None], ...] = (
    ("domain-spec-authoring", "procedure", "playbook"),
    ("eval-planning", "procedure", "playbook"),
    ("test-planning", "procedure", "playbook"),
    ("package-contracts", "specification", "behavior"),
    ("package-domain", "specification", "domain_model"),
    ("package-eval-plan", "plan", "evaluation_plan"),
    ("package-outcomes", "specification", "behavior"),
    ("package-spec", "specification", "behavior"),
    ("package-stories", "specification", "behavior"),
    ("package-test-plan", "plan", "test_plan"),
    ("change-adoption-decision", "implementation_decision", None),
    ("change-decision", "implementation_decision", None),
    ("change-design", "specification", "design"),
    ("change-eval-plan", "plan", "evaluation_plan"),
    ("change-global-impact", "analysis_report", None),
    ("change-implementation-plan", "plan", "implementation_plan"),
    ("change-specs-package", "specification", "behavior"),
    ("change-tasks", "plan", "implementation_plan"),
    ("change-test-plan", "plan", "test_plan"),
    ("change-verification", "verification", None),
    ("governance-core-v1-architecture", "specification", "architecture"),
    (
        "governance-core-v1-artifact-classification",
        "specification",
        "governance",
    ),
    (
        "governance-core-v1-artifact-maintenance",
        "specification",
        "governance",
    ),
    ("governance-core-v1-work-items", "specification", "governance"),
)
IGNORED_HOST_FILES = {".DS_Store"}
GOV_POLICY_SECTION_START = (
    "## CAPRMADIO-REQUIREMENT-GOV-040 — Project settings are verbose "
    "and all DSET artifacts use TOML\n"
)
GOV_POLICY_SECTION_END = (
    "## CAPRMADIO-DECISION-GOV-014 — TOML null normalization is allowlisted\n"
)
GOV_POLICY_SECTION = """## CAPRMADIO-REQUIREMENT-GOV-040 — Project settings are verbose

The canonical settings and project-manifest carrier is
`.caprmadio/caprmadio_settings.toml`. It must explain its boundary with governing
documents, every setting, every accepted value, the behavior each value
selects, the default, and practical examples. New writers and bootstraps emit
only this path. Retired root settings and split manifests are read-only
migration inputs; if competing carriers exist, validation stops.

Settings own operator-selectable behavior: artifact subtype naming,
medium/high artifact-creation strictness, lazy/strict implementation
preparation, integration-branch/branch-worktree Change workspace selection,
low/medium/high delegation budget selection, and the priority scale/default.
The manifest section owns identity, repository and Work Area structure,
runtime-risk and durability topology, external contracts, release targets,
verification commands, and commit-provenance boundaries. Governing documents
own definitions and policy; settings select registered behavior only.

**Scenario CAPRMADIO-SCENARIO-GOV-037:** A cold reader opens
`.caprmadio/caprmadio_settings.toml`, finds every operator choice and predicts its effect,
and reads the same carrier for runtime topology and release truth. Bootstrap
emits only the canonical path; a repository containing competing settings
carriers fails.

## CAPRMADIO-REQUIREMENT-GOV-097 — Select artifact carriers by their actual job

One concern has one canonical carrier selected by its job:

| Carrier | Canonical use |
|---|---|
| Markdown with YAML frontmatter | Human-governed artifacts with narrative meaning |
| TOML | Human-edited configuration executed directly by tools |
| JSON | External contracts, standardized schemas, wire data, and generated machine data |
| JSONL/NDJSON | Append-only runtime logs and event streams |
| Native format | Source code, CI workflows, lockfiles, and host manifests |

Markdown with restricted, GitHub-compatible YAML frontmatter is the default for
atomic, evergreen, analysis, evidence, verification, navigation, plan, and
other human-governed narrative artifacts. TOML is not a generic structured-data
default; it owns settings and configuration that tools execute directly.
Standards-compliant JSON Schema remains canonical JSON. JSONL/NDJSON is reserved
for append-only runtime records, and implementation ecosystems retain their
native formats.

Migration inventories and validates every source before writing, refuses
unknown structures and collisions, preserves semantic values and narrative
bodies, stages outputs outside the repository, checks exact preimages, rewrites
in-scope references, validates the complete bounded result, and rolls back every
touched file on failure. A second run is a no-op.

**Scenario CAPRMADIO-SCENARIO-GOV-038:** A dry run classifies every in-scope carrier
and reports its exact operation. Apply leaves every narrative Markdown artifact
with YAML frontmatter, every JSON Schema as JSON, every executable human-edited
configuration as TOML, and no competing editable representation of one concern.

`CAPRMADIO-REQUIREMENT-GOV-036` and the universal-TOML clause formerly compiled
under `CAPRMADIO-REQUIREMENT-GOV-040` are historical. The verbose-settings clause of
`CAPRMADIO-REQUIREMENT-GOV-040` remains active; carrier selection is governed by
`CAPRMADIO-REQUIREMENT-GOV-097`.

## Historical CAPRMADIO-DECISION-GOV-014 — TOML null normalization is allowlisted
"""
MAINTENANCE_OLD = """- Use TOML for CAPRMADIO-owned structured artifacts and TOML frontmatter for DSET
  Markdown. Keep host/ecosystem/wire/runtime formats and generated compatibility
  adapters explicit and non-authoritative. Never keep editable YAML/JSON and
  TOML copies of the same claim.
- Keep standards-compliant JSON Schema files as canonical external contract
  carriers. Validate and retain them as JSON; do not create an editable TOML
  duplicate or call them generated without a governed source and freshness map.
"""
MAINTENANCE_NEW = """- Select one canonical carrier by job: Markdown with YAML frontmatter for
  human-governed narrative artifacts; TOML for directly executed human-edited
  configuration; JSON for external contracts, standardized schemas, wire data,
  and generated machine data; JSONL/NDJSON for append-only runtime records; and
  native formats for source code, CI, lockfiles, and host manifests.
- Keep standards-compliant JSON Schema files as canonical JSON. Never keep
  competing editable representations of one concern.
"""
DOMAIN_INVARIANT_OLD = (
    "- **CAPRMADIO-INVARIANT-GOV-026:** Every CAPRMADIO-owned structured artifact has one "
    "canonical TOML encoding. Markdown uses TOML frontmatter. Generated adapters "
    "and host/ecosystem/wire/runtime formats are explicit non-authoritative "
    "boundaries, never parallel writable sources. Migration preserves values, "
    "IDs, references, and provenance or fails before cutover."
)
DOMAIN_INVARIANT_NEW = (
    "- **CAPRMADIO-INVARIANT-GOV-026:** Every governed concern has one canonical "
    "carrier selected by job: Markdown with YAML frontmatter for human-governed "
    "narrative artifacts; TOML for directly executed human-edited configuration; "
    "JSON for external contracts, standardized schemas, wire data, and generated "
    "machine data; JSONL/NDJSON for append-only runtime records; and native "
    "formats for source code, CI, lockfiles, and host manifests. Competing "
    "editable representations fail, and migration preserves meaning or stops "
    "before cutover."
)


def _scope_path(path: Path) -> list[str]:
    if path.parts[0] == "11_layer_meta":
        return ["layer:meta"]
    if path.parts[0] == "12_layer_gov":
        return ["layer:gov"]
    raise MigrationError(f"path is outside META/GOV: {path}")


def _is_obsolete(relative: Path) -> bool:
    """Keep explicitly retired META/GOV material outside the active contract."""
    return "_obsolete" in relative.parts


def _document_metadata(relative: Path) -> dict[str, Any]:
    """Classify a non-template methodology document without guessing."""
    name = relative.name
    scope_path = _scope_path(relative)
    route = _document_route(name, relative)
    return {
        "artifact_type": route[0],
        "artifact_subtype": route[1],
        "scope_path": scope_path,
        "priority": route[2],
    }


def _document_route(name: str, relative: Path) -> tuple[str, str, str]:
    """Return the type, subtype, and priority for one document filename."""
    if "hub" in name:
        return "navigation", "hub", "medium"
    if "navigation" in name:
        return "navigation", "index", "medium"
    if "procedure" in name or "guides-" in name:
        return "procedure", "playbook", "medium"
    if "specification-" in name:
        return "specification", _specification_subtype(name, relative), "high"
    raise MigrationError(f"unrecognized Markdown artifact: {relative}")


def _specification_subtype(name: str, relative: Path) -> str:
    routes = {
        "architecture": "architecture",
        "artifact-classification": "governance",
        "artifact-maintenance": "governance",
        "contracts": "behavior",
        "domain": "domain_model",
        "methodology": "governance",
        "outcomes": "behavior",
        "user-stories": "behavior",
        "work-items": "governance",
    }
    matches = [
        subtype
        for subject, subtype in routes.items()
        if f"specification-{subject}" in name
    ]
    if len(matches) != 1:
        raise MigrationError(
            f"unrecognized or ambiguous specification subject: {relative}"
        )
    return matches[0]


def _template_metadata(relative: Path) -> dict[str, Any]:
    """Classify the artifact emitted from a Markdown template."""
    name = relative.name
    if "hub" in name:
        return _template_hub_metadata()
    matches = [
        (artifact_type, artifact_subtype)
        for token, artifact_type, artifact_subtype in TEMPLATE_ROUTES
        if token in name
    ]
    if len(matches) != 1:
        raise MigrationError(f"unrecognized or ambiguous Markdown template: {relative}")
    return _template_route_metadata(*matches[0])


def _template_hub_metadata() -> dict[str, Any]:
    return {
        "artifact_type": "navigation",
        "artifact_subtype": "hub",
        "scope_path": [],
        "priority": "medium",
    }


def _template_route_metadata(
    artifact_type: str,
    artifact_subtype: str | None,
) -> dict[str, Any]:
    metadata: dict[str, Any] = {
        "artifact_type": artifact_type,
        "scope_path": [],
        "priority": "medium",
    }
    if artifact_subtype is not None:
        metadata["artifact_subtype"] = artifact_subtype
    if artifact_type in {"implementation_decision", "analysis_report"}:
        metadata["artifact_id"] = "{{semantic_artifact_id}}"
        metadata["llm_session_ids"] = []
    return metadata


def _new_markdown_metadata(relative: Path) -> dict[str, Any]:
    if any(part.endswith("_templates") for part in relative.parts):
        return _template_metadata(relative)
    return _document_metadata(relative)


def _normalized_markdown(relative: Path, content: bytes) -> bytes:
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError as error:
        raise MigrationError(f"Markdown is not UTF-8: {relative}") from error
    try:
        parsed = parse_frontmatter(text)
    except FrontmatterError as error:
        raise MigrationError(f"invalid frontmatter in {relative}: {error}") from error
    if parsed is None:
        metadata = _new_markdown_metadata(relative)
        body = text if text.startswith("\n") else f"\n{text}"
    else:
        metadata, body, _format = parsed
        if not metadata:
            raise MigrationError(f"empty frontmatter in {relative}")
    rendered = render_frontmatter(metadata, body, format="yaml")
    reparsed = parse_frontmatter(rendered)
    if reparsed is None or reparsed[2] != "yaml" or reparsed[0] != metadata:
        raise MigrationError(f"YAML frontmatter round trip failed: {relative}")
    return rendered.encode("utf-8")


def _normalized_schema(relative: Path, content: bytes) -> bytes:
    try:
        data = tomllib.loads(content.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise MigrationError(
            f"invalid TOML JSON Schema: {relative}: {error}"
        ) from error
    if data.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise MigrationError(f"unsupported or missing JSON Schema dialect: {relative}")
    if not isinstance(data.get("type"), (str, list)):
        raise MigrationError(f"JSON Schema has no root type: {relative}")
    identifier = data.get("$id")
    if identifier is not None:
        if not isinstance(identifier, str) or not identifier.endswith(".schema.toml"):
            raise MigrationError(
                f"unexpected JSON Schema $id: {relative}: {identifier!r}"
            )
        data["$id"] = identifier[: -len(SCHEMA_SUFFIX)] + JSON_SCHEMA_SUFFIX
    rendered = (json.dumps(data, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    reparsed = json.loads(rendered)
    if reparsed != data:
        raise MigrationError(f"JSON Schema round trip failed: {relative}")
    return rendered


def _replace_schema_references(content: bytes) -> bytes:
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError as error:
        raise MigrationError("scoped text reference file is not UTF-8") from error
    return text.replace(SCHEMA_SUFFIX, JSON_SCHEMA_SUFFIX).encode("utf-8")


def _replace_once_or_confirm(
    text: str,
    old: str,
    new: str,
    relative: Path,
) -> str:
    """Replace one exact block, accepting an already-migrated result."""
    old_count = text.count(old)
    if old_count == 1:
        return text.replace(old, new, 1)
    if old_count == 0 and text.count(new) == 1:
        return text
    if old_count == 0 and text.count(new) == 0:
        return text
    raise MigrationError(
        f"guarded replacement mismatch in {relative}: "
        f"old={old_count}, new={text.count(new)}"
    )


def _rewrite_governance_policy(relative: Path, content: bytes) -> bytes:
    """Apply exact, idempotent policy replacements to current GOV owners."""
    if not _is_governance_policy_owner(relative):
        return content
    text = content.decode("utf-8")
    if relative.name == "080_dset-gov-specification-methodology.md":
        text = _rewrite_methodology_policy(relative, text)
    elif relative.name == "070_dset-gov-specification-domain.md":
        text = _replace_once_or_confirm(
            text, DOMAIN_INVARIANT_OLD, DOMAIN_INVARIANT_NEW, relative
        )
    elif relative.name.endswith("artifact-maintenance.md"):
        text = _replace_once_or_confirm(
            text, MAINTENANCE_OLD, MAINTENANCE_NEW, relative
        )
    else:
        text = _replace_once_or_confirm(
            text,
            '"title": "DSET native Evidence Record TOML frontmatter"',
            '"title": "DSET native Evidence Record YAML frontmatter"',
            relative,
        )
    return text.encode("utf-8")


def _is_governance_policy_owner(relative: Path) -> bool:
    return relative.as_posix() in {
        "12_layer_gov/050_dset-gov-specification-artifact-maintenance.md",
        "12_layer_gov/070_dset-gov-specification-domain.md",
        "12_layer_gov/080_dset-gov-specification-methodology.md",
        ("12_layer_gov/120_schemas/060_dset-gov-schemas-evidence-record.schema.json"),
        (
            "12_layer_gov/130_templates/050_governance/000_core-v1/"
            "030_dset-gov-templates-governance-core-v1-artifact-maintenance.md"
        ),
    }


def _rewrite_methodology_policy(relative: Path, text: str) -> str:
    start_count = text.count(GOV_POLICY_SECTION_START)
    if start_count == 1:
        start = text.index(GOV_POLICY_SECTION_START)
        end = text.find(GOV_POLICY_SECTION_END, start)
        if end < 0:
            raise MigrationError(f"policy section end marker missing in {relative}")
        return (
            text[:start]
            + GOV_POLICY_SECTION
            + text[end + len(GOV_POLICY_SECTION_END) :]
        )
    current_policy = text.count(
        "## CAPRMADIO-REQUIREMENT-GOV-097 — Select artifact carriers by their actual job"
    )
    evolved_policy = all(
        marker in text
        for marker in ("## Mechanical migrations", "## Carrier and preview policy")
    )
    if start_count == 0 and (
        current_policy == 1
        or ("all DSET artifacts use TOML" not in text and evolved_policy)
    ):
        return text
    raise MigrationError(f"policy section markers are ambiguous in {relative}")


def _render_schema_hub(
    hub: Path,
    content: bytes,
    schema_names: list[str],
) -> bytes:
    """Render one exact schema inventory while preserving hub metadata."""
    parsed = parse_frontmatter(content.decode("utf-8"))
    if parsed is None or parsed[2] != "yaml":
        raise MigrationError(f"schema hub requires YAML frontmatter: {hub}")
    metadata = parsed[0]
    title, description, footer = _schema_hub_text(hub, schema_names)
    inventory = "\n".join(f"- `{name}`" for name in schema_names)
    body = f"\n# {title} schemas\n\n{description}\n\n{inventory}\n{footer}"
    rendered = render_frontmatter(metadata, body, format="yaml").encode("utf-8")
    reparsed = parse_frontmatter(rendered.decode("utf-8"))
    if reparsed is None or reparsed[0] != metadata or reparsed[2] != "yaml":
        raise MigrationError(f"schema hub round trip failed: {hub}")
    return rendered


def _schema_hub_text(hub: Path, schema_names: list[str]) -> tuple[str, str, str]:
    if hub.parts[0] == "11_layer_meta":
        if any("project" in name for name in schema_names):
            description = (
                "Project, version, package, and package-fragment schemas owned by META:"
            )
            footer = ""
        else:
            description = (
                "Version, package, and package-fragment schemas owned by META:"
            )
            footer = (
                "\nProject settings and artifact-carrier schemas belong to GOV "
                "because they\ncontrol governed storage, routing, and validation.\n"
            )
        return "META", description, footer
    elif hub.parts[0] == "12_layer_gov":
        description = "Repository-governance schemas owned by GOV:"
        footer = (
            "\nOther schema families live with their META, TOOL, SKILL, "
            "IMPL, or OPS owner.\n"
        )
        return "GOV", description, footer
    else:
        raise MigrationError(f"schema hub is outside META/GOV: {hub}")


def build_plan(root: Path) -> MigrationPlan:
    """Build a complete plan against exact current working-tree bytes."""
    root = root.resolve()
    if not (root / ".git").exists():
        raise MigrationError(f"not a repository root: {root}")
    writes: dict[Path, WriteOperation] = {}
    deletes: dict[Path, DeleteOperation] = {}
    schema_sources: list[Path] = []
    for root_name in MIGRATION_ROOTS:
        _scan_layer(root, root_name, writes, deletes, schema_sources)
    _validate_schema_source_count(root, schema_sources)
    _plan_reference_rewrites(root, writes, deletes)
    _plan_schema_hubs(root, writes)
    overlap = set(writes) & set(deletes)
    if overlap:
        raise MigrationError(f"write/delete collision: {sorted(overlap)}")
    return MigrationPlan(
        root=root,
        writes=tuple(sorted(writes.values(), key=lambda item: item.path)),
        deletes=tuple(sorted(deletes.values(), key=lambda item: item.path)),
    )


def _scan_layer(
    root: Path,
    root_name: str,
    writes: dict[Path, WriteOperation],
    deletes: dict[Path, DeleteOperation],
    schema_sources: list[Path],
) -> None:
    layer_root = root / root_name
    if not layer_root.is_dir() or layer_root.is_symlink():
        raise MigrationError(f"missing or unsafe migration root: {layer_root}")
    for path in sorted(layer_root.rglob("*")):
        if path.is_symlink():
            raise MigrationError(f"symlink is outside the migration contract: {path}")
        if path.is_dir() or _is_obsolete(path.relative_to(root)):
            continue
        _plan_source_file(root, path, writes, deletes, schema_sources)


def _plan_source_file(
    root: Path,
    path: Path,
    writes: dict[Path, WriteOperation],
    deletes: dict[Path, DeleteOperation],
    schema_sources: list[Path],
) -> None:
    relative = path.relative_to(root)
    content = _read_regular_file(path)
    if path.name in IGNORED_HOST_FILES:
        return
    if path.suffix == ".md":
        _plan_markdown(path, relative, content, writes)
    elif path.name.endswith(SCHEMA_SUFFIX):
        _plan_toml_schema(root, path, relative, content, writes, deletes)
        schema_sources.append(path)
    elif path.name.endswith(JSON_SCHEMA_SUFFIX):
        _validate_json_schema(relative, content)
    elif path.suffix == ".toml":
        _validate_configuration_toml(relative, path.name, content)
    else:
        raise MigrationError(f"unclassified carrier: {relative}")


def _plan_markdown(
    path: Path,
    relative: Path,
    content: bytes,
    writes: dict[Path, WriteOperation],
) -> None:
    normalized = _normalized_markdown(relative, content)
    if normalized != content:
        writes[path] = WriteOperation(
            path, _sha256(content), normalized, "use Markdown with YAML frontmatter"
        )


def _plan_toml_schema(
    root: Path,
    path: Path,
    relative: Path,
    content: bytes,
    writes: dict[Path, WriteOperation],
    deletes: dict[Path, DeleteOperation],
) -> None:
    target = path.with_name(path.name[: -len(SCHEMA_SUFFIX)] + JSON_SCHEMA_SUFFIX)
    if target.exists():
        raise MigrationError(f"JSON Schema target already exists: {target}")
    normalized = _normalized_schema(relative, content)
    normalized = _rewrite_governance_policy(target.relative_to(root), normalized)
    writes[target] = WriteOperation(
        target, None, normalized, "use canonical JSON Schema"
    )
    deletes[path] = DeleteOperation(
        path, _sha256(content), "replaced by canonical JSON Schema"
    )


def _validate_json_schema(relative: Path, content: bytes) -> None:
    try:
        data = json.loads(content)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise MigrationError(f"invalid JSON Schema: {relative}") from error
    if data.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise MigrationError(f"unsupported JSON Schema: {relative}")


def _validate_configuration_toml(
    relative: Path,
    name: str,
    content: bytes,
) -> None:
    if name not in CONFIGURATION_TOML_NAMES:
        raise MigrationError(f"unclassified TOML carrier: {relative}")
    try:
        tomllib.loads(content.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise MigrationError(f"invalid configuration TOML: {relative}") from error


def _validate_schema_source_count(root: Path, schema_sources: list[Path]) -> None:
    if schema_sources:
        return
    existing_json = sum(
        1
        for root_name in MIGRATION_ROOTS
        for _path in (root / root_name).rglob(f"*{JSON_SCHEMA_SUFFIX}")
    )
    if existing_json != 15:
        raise MigrationError(
            "expected either 15 TOML JSON Schemas to migrate or 15 JSON results"
        )


def _plan_reference_rewrites(
    root: Path,
    writes: dict[Path, WriteOperation],
    deletes: dict[Path, DeleteOperation],
) -> None:
    for root_name in MIGRATION_ROOTS:
        for path in sorted((root / root_name).rglob("*")):
            if not _is_rewritable_source(root, path, deletes):
                continue
            content = writes[path].content if path in writes else path.read_bytes()
            rewritten = _replace_schema_references(content)
            rewritten = _rewrite_governance_policy(path.relative_to(root), rewritten)
            if rewritten != content:
                before_hash = (
                    writes[path].before_sha256 if path in writes else _sha256(content)
                )
                writes[path] = WriteOperation(
                    path,
                    before_hash,
                    rewritten,
                    "update in-scope JSON Schema references",
                )


def _is_rewritable_source(
    root: Path,
    path: Path,
    deletes: dict[Path, DeleteOperation],
) -> bool:
    return (
        path.is_file()
        and path not in deletes
        and path.suffix in {".md", ".toml", ".json"}
        and not _is_obsolete(path.relative_to(root))
    )


def _plan_schema_hubs(
    root: Path,
    writes: dict[Path, WriteOperation],
) -> None:
    schema_hubs = {
        Path("11_layer_meta/100_schemas/000_dset-meta-schemas-hub.md"): (
            Path("11_layer_meta/100_schemas")
        ),
        Path("12_layer_gov/120_schemas/000_dset-gov-schemas-hub.md"): (
            Path("12_layer_gov/120_schemas")
        ),
    }
    for hub_relative, directory_relative in schema_hubs.items():
        hub = root / hub_relative
        content = writes[hub].content if hub in writes else _read_regular_file(hub)
        schema_directory = root / directory_relative
        schema_names = sorted(
            {path.name for path in schema_directory.glob(f"*{JSON_SCHEMA_SUFFIX}")}
            | {
                path.name
                for path in writes
                if path.parent == schema_directory
                and path.name.endswith(JSON_SCHEMA_SUFFIX)
            }
        )
        rendered = _render_schema_hub(hub_relative, content, schema_names)
        if rendered != content:
            writes[hub] = WriteOperation(
                hub,
                writes[hub].before_sha256 if hub in writes else _sha256(content),
                rendered,
                "synchronize the exact JSON Schema inventory",
            )


def _assert_preimages(plan: MigrationPlan) -> None:
    for operation in plan.writes:
        if operation.before_sha256 is None:
            if operation.path.exists():
                raise MigrationError(
                    f"new target appeared after planning: {operation.path}"
                )
            continue
        content = _read_regular_file(operation.path)
        if _sha256(content) != operation.before_sha256:
            raise MigrationError(f"file changed after planning: {operation.path}")
    for operation in plan.deletes:
        content = _read_regular_file(operation.path)
        if _sha256(content) != operation.before_sha256:
            raise MigrationError(f"file changed after planning: {operation.path}")


def verify(root: Path) -> None:
    """Verify the bounded carrier policy after migration."""
    root = root.resolve()
    markdown_count = 0
    schema_count = 0
    for root_name in MIGRATION_ROOTS:
        counts = _verify_layer(root, root_name)
        markdown_count += counts[0]
        schema_count += counts[1]
    expected_markdown_count = (
        72
        if any(
            (root / root_name / "_obsolete").exists() for root_name in MIGRATION_ROOTS
        )
        else 77
    )
    if markdown_count != expected_markdown_count:
        raise MigrationError(
            f"expected {expected_markdown_count} active Markdown artifacts, "
            f"found {markdown_count}"
        )
    if schema_count != 15:
        raise MigrationError(f"expected 15 JSON Schemas, found {schema_count}")
    _verify_no_stale_schema_references(root)


def _verify_layer(root: Path, root_name: str) -> tuple[int, int]:
    markdown_count = 0
    schema_count = 0
    for path in sorted((root / root_name).rglob("*")):
        if path.is_symlink():
            raise MigrationError(f"symlink is outside the migration contract: {path}")
        if path.is_dir() or _is_obsolete(path.relative_to(root)):
            continue
        kind = _verify_file(root, path)
        markdown_count += kind == "markdown"
        schema_count += kind == "schema"
    return markdown_count, schema_count


def _verify_file(root: Path, path: Path) -> str:
    relative = path.relative_to(root)
    if path.name in IGNORED_HOST_FILES:
        return "ignored"
    if path.suffix == ".md":
        parsed = parse_frontmatter(path.read_text(encoding="utf-8"))
        if parsed is None or parsed[2] != "yaml" or not parsed[0]:
            raise MigrationError(
                f"Markdown lacks nonempty YAML frontmatter: {relative}"
            )
        return "markdown"
    if path.name.endswith(JSON_SCHEMA_SUFFIX):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            raise MigrationError(f"invalid JSON Schema dialect: {relative}")
        return "schema"
    if path.name.endswith(SCHEMA_SUFFIX):
        raise MigrationError(f"TOML-encoded JSON Schema remains: {relative}")
    if path.suffix == ".toml":
        _validate_configuration_toml(relative, path.name, path.read_bytes())
        return "configuration"
    raise MigrationError(f"unclassified carrier: {relative}")


def _verify_no_stale_schema_references(root: Path) -> None:
    for root_name in MIGRATION_ROOTS:
        for path in (root / root_name).rglob("*"):
            if (
                path.is_file()
                and path.suffix in {".md", ".toml", ".json"}
                and SCHEMA_SUFFIX in path.read_text(encoding="utf-8")
            ):
                raise MigrationError(
                    f"stale in-scope TOML schema reference: {path.relative_to(root)}"
                )


def apply_plan(plan: MigrationPlan) -> None:
    """Apply a validated plan with staged bytes and rollback on failure."""
    apply_transaction(plan, _validate_staged_results, verify)


def _validate_staged_results(
    plan: MigrationPlan,
    staged: dict[Path, Path],
) -> None:
    """Validate every candidate carrier before any live replacement."""
    if set(staged) != {operation.path for operation in plan.writes}:
        raise MigrationError("staged write set does not match the migration plan")
    for target, staged_path in staged.items():
        _validate_staged_carrier(plan.root, target, staged_path.read_bytes())


def _validate_staged_carrier(root: Path, target: Path, content: bytes) -> None:
    relative = target.relative_to(root)
    if target.suffix == ".md":
        parsed = parse_frontmatter(content.decode("utf-8"))
        if parsed is None or parsed[2] != "yaml" or not parsed[0]:
            raise MigrationError(f"staged Markdown is not canonical YAML: {relative}")
    elif target.name.endswith(JSON_SCHEMA_SUFFIX):
        _validate_json_schema(relative, content)
    elif target.suffix == ".toml":
        _validate_configuration_toml(relative, target.name, content)
    else:
        raise MigrationError(f"staged target has an unsupported carrier: {relative}")
    if target.suffix in {".md", ".toml", ".json"} and SCHEMA_SUFFIX in content.decode(
        "utf-8"
    ):
        raise MigrationError(f"staged carrier has a stale schema reference: {relative}")


def _arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=REPOSITORY_ROOT,
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--check", action="store_true")
    parser.add_argument(
        "--expect-plan-digest",
        help="apply only when the rebuilt plan matches this preview digest",
    )
    return parser.parse_args()


def main() -> int:
    """Run the dry-run, apply, or verification mode."""
    arguments = _arguments()
    try:
        if arguments.check:
            verify(arguments.root)
            print("META/GOV carrier verification passed")
            return 0
        plan = build_plan(arguments.root)
        print(plan.summary())
        if arguments.apply:
            _assert_expected_digest(plan, arguments.expect_plan_digest)
            apply_plan(plan)
            print("META/GOV carrier migration applied and verified")
        else:
            print("DRY RUN: pass --apply to execute this exact class of operations")
        return 0
    except (MigrationError, FrontmatterError, OSError, json.JSONDecodeError) as error:
        print(f"BLOCKED: {error}", file=sys.stderr)
        return 1


def _assert_expected_digest(plan: MigrationPlan, expected: str | None) -> None:
    if expected is not None and plan.digest() != expected:
        raise MigrationError(
            f"plan digest changed: expected {expected}, rebuilt {plan.digest()}"
        )


if __name__ == "__main__":
    raise SystemExit(main())
