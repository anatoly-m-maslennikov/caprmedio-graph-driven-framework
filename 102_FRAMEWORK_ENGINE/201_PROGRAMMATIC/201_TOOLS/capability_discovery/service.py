"""Read-only helpers derived from Atom carriers and saved Run evidence."""
import asyncio
import base64
import hashlib
import json
import re
import time
import tomllib
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field

from validate_atoms_workers.parsing import parse_carrier
from project_selection import bound_selection


_DISCOVERY_TOOL_FIELDS = frozenset({
    'source_atom', 'source_path', 'sha256', 'scope_unit', 'summary', 'availability',
})
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_DIRECT_TOOL_CONTRACTS = (
    {
        'name': 'FRAMEWORK_IMAGE_RESTORATION',
        'mcp_name': 'restore_framework_image',
        'entrypoint': '102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/framework_image_restoration_mcp.py',
        'action_id': 'CA-O-187',
        'source_atom': 'CA-D-591',
    },
    {
        'name': 'ADMIT_PACKAGE_SOURCES',
        'mcp_name': 'admit_package_sources',
        'entrypoint': '102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/source_admission_mcp.py',
        'action_id': 'CA-O-199',
        'source_atom': 'CA-D-602',
    },
    {
        'name': 'INSTALL_FRAMEWORK_RUNTIME',
        'mcp_name': 'install_framework_runtime',
        'entrypoint': '102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/framework_runtime_installation_mcp.py',
        'action_id': 'CA-O-200',
        'source_atom': 'CA-D-620',
    },
)


def _direct_contract_claims(tool):
    """Return exact direct-MCP contracts claimed by one source declaration.

    These are deliberately the governed direct Tools, not a caller-supplied
    registry or a route inference rule.  A malformed declaration that claims
    either Tool is still a direct-binding failure, rather than a generic source
    tool that discovery could accidentally present as executable.
    """

    name = tool.get('name')
    mcp_name = tool.get('mcp_name')
    action_ids = tool.get('action_ids')
    if not isinstance(action_ids, list):
        action_ids = []
    return tuple(
        contract for contract in _DIRECT_TOOL_CONTRACTS
        if name == contract['name']
        or mcp_name == contract['mcp_name']
        or contract['action_id'] in action_ids
    )


def _exact_direct_contract(tool):
    """Return one closed source declaration, or no executable direct Tool."""

    claims = _direct_contract_claims(tool)
    if len(claims) != 1:
        return None
    contract = claims[0]
    source_binding_fields = set(tool).difference(_DISCOVERY_TOOL_FIELDS)
    if source_binding_fields != {'name', 'mcp_name', 'entrypoint', 'action_ids'}:
        return None
    if (
        tool.get('name') != contract['name']
        or tool.get('mcp_name') != contract['mcp_name']
        or tool.get('entrypoint') != contract['entrypoint']
        or tool.get('action_ids') != [contract['action_id']]
        or tool.get('source_atom') != contract['source_atom']
    ):
        return None
    return contract


def _source_tool_declaration(body):
    """Return one source declaration solely for package-conflict detection.

    The source tree is never an installed binding provider.  It remains useful
    evidence, however: if a current declaration for a package-projected Atom
    has drifted, the consumer must report ambiguity instead of choosing either
    presentation by traversal order.
    """

    declarations = []
    for block in body.split('```toml')[1:]:
        try:
            document = tomllib.loads(block.split('```', 1)[0])
        except tomllib.TOMLDecodeError:
            return None
        binding = document.get('tool_binding') if isinstance(document, dict) else None
        if isinstance(binding, dict):
            declarations.append(binding)
    return declarations[0] if len(declarations) == 1 else None


class Query(BaseModel):
    model_config = ConfigDict(extra='forbid', strict=True)
    query: str = ''
    limit: int = Field(default=10, ge=1, le=50)
    scope_unit: str | None = None
    include_descendants: bool = False
    availability: str | None = None
    offset: int = Field(default=0, ge=0)


class Context(BaseModel):
    model_config = ConfigDict(extra='forbid', strict=True)
    id: str


class Observation(BaseModel):
    model_config = ConfigDict(extra='forbid', strict=True)
    run_id: str
    include_results: bool = False
    ordinal: int | None = Field(default=None, ge=0)


class Watch(Observation):
    cursor: str | None = None
    timeout_seconds: float = Field(default=0, ge=0, le=30)


class Service:
    def __init__(self, root, exposed=()):
        self.root = Path(root).resolve(strict=True)
        self.exposed = set(exposed)

    def read(self, path):
        path = Path(path)
        if not path.is_relative_to(self.root):
            raise ValueError('Path outside Project')
        for part in path.relative_to(self.root).parts:
            if part.startswith('.env') or part.endswith('.env'):
                raise ValueError('Protected path')
        current = self.root
        for part in path.relative_to(self.root).parts:
            current /= part
            if current.is_symlink():
                raise ValueError('Symlink carrier')
        if path.stat().st_size > 8 * 1024 * 1024:
            raise ValueError('Carrier exceeds read limit')
        from validate_atoms_workers.read_io import open_regular
        import os
        descriptor = open_regular(path)
        with os.fdopen(descriptor, 'rb') as stream:
            raw = stream.read(8 * 1024 * 1024 + 1)
            if len(raw) > 8 * 1024 * 1024:
                raise ValueError('Carrier exceeds read limit')
            return raw

    def _control_root(self):
        """Resolve the Project's declared control root from its one settings Carrier."""
        selection = bound_selection(self.root)
        if selection is not None:
            return selection.control_root
        settings_paths = sorted(
            path for path in self.root.glob('.caprmedio_*/caprmedio_project_settings.toml')
            if path.is_file() and not path.is_symlink() and not path.parent.is_symlink()
        )
        if len(settings_paths) != 1:
            raise ValueError('Project settings carrier is missing or ambiguous')
        settings_path = settings_paths[0]
        try:
            settings = tomllib.loads(self.read(settings_path).decode())
        except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
            raise ValueError('Invalid Project settings carrier') from error
        paths = settings.get('paths', {})
        if not isinstance(paths, dict):
            raise ValueError('Invalid Project control root')
        default = settings_path.parent.relative_to(self.root).as_posix()
        value = paths.get('control_root', default)
        if not isinstance(value, str) or not value:
            raise ValueError('Invalid Project control root')
        control = Path(value)
        if control.is_absolute() or '..' in control.parts or control.as_posix() in ('', '.'):
            raise ValueError('Invalid Project control root')
        control_path = self.root / control
        resolved = control_path.resolve()
        if control_path.is_symlink() or not resolved.is_relative_to(self.root) or not resolved.is_dir():
            raise ValueError('Invalid Project control root')
        return resolved

    def _admitted_selected_route_tools(self, issues):
        """Return synthetic discovery rows for source-admitted selected routes only.

        Selected routes intentionally have no Atom ``tool_binding``: their public
        MCP names are registered from the fail-closed canonical manifest.  Keep
        that distinction in discovery rather than treating a source carrier as
        executable.  Importing and loading the existing manifest is therefore
        the sole admission path here as well.
        """
        if not self.exposed:
            return []
        try:
            from selected_routes import load_selected_manifest
            manifest = load_selected_manifest(self.root)
        except (ImportError, OSError):
            # The catalog is public discovery output: do not expose exception
            # details, paths, or evidence content while reporting recovery.
            issues.append('binding evidence unavailable: restore or regenerate binding evidence, then re-preview selected routes')
            return []
        except ValueError as error:
            if str(error).casefold().startswith((
                'source pin is stale',
                'selected source registry pin is stale',
            )):
                issues.append('binding evidence stale: refresh source bindings, then re-preview selected routes')
            else:
                issues.append('binding evidence invalid: correct bindings, then re-preview selected routes')
            return []

        rows = []
        for entry in manifest.get("routes", []):
            if not isinstance(entry, dict):
                continue
            route = entry.get("route")
            workflow = entry.get("workflow")
            actions = entry.get("ordered_actions")
            if route not in self.exposed or not isinstance(workflow, dict) or not isinstance(actions, list):
                continue
            workflow_id = workflow.get("atom_id")
            action_ids = [item.get("atom_id") for item in actions if isinstance(item, dict)]
            if (not isinstance(route, str) or not isinstance(workflow_id, str) or not action_ids
                    or not all(isinstance(identity, str) for identity in action_ids)):
                continue
            rows.append({
                "name": route, "mcp_name": route, "availability": "mcp", "source_atom": workflow_id,
                "workflow_ids": [workflow_id], "action_ids": action_ids, "selected_route": True,
                "definition_manifest": {"manifest_ref": manifest["manifest_ref"],
                                        "manifest_digest": manifest["canonical_manifest_sha256"]},
                "source_freshness": manifest["source_freshness"],
                "summary": f"Selected route admitted by the current binding manifest: {route}.",
            })
        return rows

    def _current_verified_package(self, issues):
        """Reopen the one selected package without deriving it from checkout.

        A missing selector retains the legacy source-only discovery surface for
        an uninstalled Project.  Once a selector exists, even an invalid one
        is a fail-closed package-discovery boundary: callers do not fall back
        to source declarations.
        """

        selector_path = self.root / '.caprmedio_install' / 'current.toml'
        try:
            selector_path.lstat()
        except FileNotFoundError:
            return False, None
        except OSError:
            issues.append('installed package binding unavailable')
            return True, None
        try:
            from framework_package import (
                FrameworkPackageError,
                verify_current_package_selector,
                verify_framework_package,
            )

            payload = self.read(selector_path)
            selector = tomllib.loads(payload.decode('utf-8'))
            manifest = selector.get('package_manifest_sha256') if isinstance(selector, dict) else None
            if not isinstance(manifest, str) or _SHA256.fullmatch(manifest) is None:
                raise ValueError('package selector manifest is invalid')
            if selector.get('release_relpath') != f'releases/{manifest}':
                raise ValueError('package selector release is not canonical')
            package = verify_framework_package(
                self.root / '.caprmedio_install' / 'releases' / manifest,
            )
            verify_current_package_selector(payload, package)
            return True, package
        except (FrameworkPackageError, OSError, UnicodeDecodeError, tomllib.TOMLDecodeError, ValueError):
            issues.append('installed package binding unavailable')
            return True, None

    @staticmethod
    def _package_binding_conflicts(projection, current_sources):
        """Whether an active source declaration conflicts with package identity.

        A same-byte declaration of the same projected Atom is a second
        presentation of one verified identity.  Every other source declaration
        sharing its Atom, source path, Tool name, MCP name, or Action claim is
        ambiguous.  Package discovery must not choose a duplicate claimant by
        traversal order after replacing the source-tool rows.
        """

        expected_binding = dict(projection.tool_binding)
        expected_actions = expected_binding.get('action_ids')
        expected_action_ids = set(expected_actions) if isinstance(expected_actions, list) else set()
        expected_name = expected_binding.get('name')
        expected_name = expected_name if isinstance(expected_name, str) and expected_name else None
        expected_mcp_name = expected_binding.get('mcp_name')
        expected_mcp_name = (
            expected_mcp_name
            if isinstance(expected_mcp_name, str) and expected_mcp_name
            else None
        )
        for candidates in current_sources.values():
            for candidate in candidates:
                if (
                    candidate['atom_id'] == projection.atom_id
                    and candidate['source_path'] == projection.source_path
                    and candidate['sha256'] == projection.source_sha256
                    and candidate['tool_binding'] == expected_binding
                ):
                    continue
                binding = candidate['tool_binding']
                if candidate['atom_id'] == projection.atom_id or candidate['source_path'] == projection.source_path:
                    return True
                if not isinstance(binding, dict):
                    continue
                candidate_actions = binding.get('action_ids')
                if (
                    (expected_name is not None and binding.get('name') == expected_name)
                    or (expected_mcp_name is not None and binding.get('mcp_name') == expected_mcp_name)
                    or (
                        isinstance(candidate_actions, list)
                        and bool(expected_action_ids.intersection(candidate_actions))
                    )
                ):
                    return True
        return False

    def _selected_package_tools(self, current_sources, issues):
        """Expose only projections physically reopened from selected package bytes."""

        package_selected, package = self._current_verified_package(issues)
        if not package_selected:
            return False, []
        if package is None:
            return True, []
        try:
            from framework_package import FrameworkPackageError, read_verified_binding_projections

            projections = read_verified_binding_projections(package)
        except (FrameworkPackageError, OSError, ValueError):
            issues.append('installed package binding unavailable')
            return True, []

        # The projection reader reopens package bytes; also ensure selection
        # did not move to a different package between selector admission and
        # that physical read.  A raced selector never falls back to checkout.
        selected_after, package_after = self._current_verified_package([])
        if not selected_after or package_after != package:
            issues.append('installed package binding changed during discovery')
            return True, []

        tools = []
        for projection in projections:
            if self._package_binding_conflicts(projection, current_sources):
                issues.append(f'ambiguous package binding: {projection.atom_id}')
                continue
            try:
                parsed = parse_carrier(projection.source_payload, Path(projection.source_path))
            except (ValueError, TypeError):
                issues.append(f'installed package binding invalid: {projection.atom_id}')
                continue
            metadata = parsed.metadata
            body = parsed.body
            tool = {
                **dict(projection.tool_binding),
                'source_atom': projection.atom_id,
                'source_path': projection.source_path,
                'sha256': projection.source_sha256,
                'scope_unit': metadata.get('current_scope_unit'),
                'summary': body.split('##', 1)[0].replace('# Summary', '').strip(),
            }
            contract = _exact_direct_contract(tool)
            if _direct_contract_claims(tool):
                tool['availability'] = (
                    'mcp' if contract is not None and tool.get('mcp_name') in self.exposed else 'unresolved'
                )
            else:
                # The package reader has already established that entrypoint is
                # a regular Engine member; never consult a root checkout path.
                tool['availability'] = 'mcp' if tool.get('mcp_name') in self.exposed else 'source'
            tools.append(tool)
        return True, tools

    @staticmethod
    def _selected_route_input_schema(route: str):
        """Compact contract for the generic selected-route MCP request object."""
        digest = {"type": "string", "pattern": "^[0-9a-f]{64}$"}
        return {
            "type": "object",
            "additionalProperties": False,
            "required": ["operation_route", "request_id", "parameters", "parameters_digest",
                         "target_frontier", "target_frontier_digest", "effects", "effects_digest",
                         "definition_manifest", "source_freshness", "initiative"],
            "properties": {
                "operation_route": {"const": route},
                "mode": {"enum": ["preview", "execute"], "default": "preview"},
                "request_id": {"type": "string"}, "parameters": {"type": "object"},
                "parameters_digest": digest, "target_frontier": {"type": "array", "minItems": 1},
                "target_frontier_digest": digest, "effects": {"type": "array"},
                "effects_digest": digest, "definition_manifest": {"type": "object"},
                "source_freshness": {"type": "object"}, "initiative": {"type": "object"},
                "lineage": {"type": "array"}, "expected_definition_revisions": {"type": "array"},
                "proposal_receipt": {"type": "object"}, "proposal_receipt_digest": digest,
                "assigned_action_id": {"type": "string"}, "requested_runs": {"type": "array", "minItems": 1},
                "operator_authorization": {"type": "object"},
            },
            "allOf": [{"if": {"properties": {"mode": {"const": "execute"}}, "required": ["mode"]},
                       "then": {"required": ["proposal_receipt", "proposal_receipt_digest",
                                             "assigned_action_id", "requested_runs", "operator_authorization"]}}],
        }

    @staticmethod
    def _direct_tool_input_schema(request_id, row, tools):
        """Load one exact admitted direct-MCP schema without route inference."""
        candidates = [
            (tool, _exact_direct_contract(tool)) for tool in tools
            if tool.get('availability') == 'mcp'
            and request_id in {
                tool.get("name"), tool.get("source_atom"),
                *tool.get("action_ids", []), *tool.get("workflow_ids", []),
            }
        ]
        candidates = [(tool, contract) for tool, contract in candidates if contract is not None]
        if len(candidates) != 1:
            return None
        try:
            import sys
            mcp_root = Path(__file__).resolve().parents[2] / "204_MCP"
            if str(mcp_root) not in sys.path:
                sys.path.insert(0, str(mcp_root))
            tool, contract = candidates[0]
            if contract['name'] == 'FRAMEWORK_IMAGE_RESTORATION':
                from framework_image_restoration_mcp import binding_is_admitted, input_schema
            elif contract['name'] == 'ADMIT_PACKAGE_SOURCES':
                from source_admission_mcp import binding_is_admitted, input_schema
            elif contract['name'] == 'INSTALL_FRAMEWORK_RUNTIME':
                from framework_runtime_installation_mcp import binding_is_admitted, input_schema
            else:  # pragma: no cover - contracts above are closed and exhaustive.
                return None
            return input_schema() if binding_is_admitted(tool) else None
        except (ImportError, OSError, ValueError, TypeError):
            # A source declaration is not executable if its implementation
            # schema cannot be loaded.  Leave context incomplete rather than
            # inventing a callable request grammar.
            return None

    def catalog(self):
        control = self._control_root()
        atoms, source_tools, current_sources, issues = {}, [], {}, []
        started, total = time.monotonic(), 0
        excluded = {'archive', 'archived', 'draft', 'done', 'resolved', 'canceled',
                    'cancelled', '_journal', '_projection'}
        def excluded_component(part):
            return (part == control.name or part == '_release_materialized'
                    or part.lower() in excluded or part.startswith('.env')
                    or part.endswith('.env'))
        def current_source(path):
            relative = path.relative_to(control).parts
            if any(excluded_component(part) for part in relative):
                return False
            return ('00_APPLICABLE_METHODOLOGY' not in relative
                    or '000_APPLICABLE_MTHD_sources' in relative)
        def source_candidates():
            # Prune before descending: delivered copies and saved evidence can
            # dwarf the current source frontier.  File admission still applies
            # below, including canonical methodology and duplicate checks.
            for directory, directories, files in control.walk():
                directories[:] = [name for name in directories
                                  if not excluded_component(name)
                                  and not (directory / name).is_symlink()]
                for name in files:
                    path = directory / name
                    if name.endswith('.md') and current_source(path):
                        yield path
        # M318/D520 omit delivered copies before counting source candidates;
        # canonical methodology sources still participate in duplicate checks.
        candidates = source_candidates()
        for number, path in enumerate(candidates):
            if number >= 10000 or time.monotonic() - started > 60:
                issues.append('incomplete: catalog limit reached')
                break
            try:
                raw = self.read(path)
                total += len(raw)
                if total > 256 * 1024 * 1024:
                    issues.append('incomplete: total read limit reached')
                    break
                parsed = parse_carrier(raw, path)
                data = parsed.metadata
                if str(data.get('status', '')).lower() != 'active':
                    continue
                identity = data.get('atom_id')
                if not isinstance(identity, str):
                    continue
                row = {'id': identity, 'scope_unit': data.get('current_scope_unit'),
                       'type': data.get('type'), 'content_role': data.get('content_role'),
                       'source_path': str(path.relative_to(self.root)),
                       'sha256': hashlib.sha256(raw).hexdigest(), 'content': parsed.body,
                       'properties': json.loads(json.dumps(data, default=str))}
                if identity in atoms:
                    issues.append(f'ambiguous Atom ID: {identity}')
                    atoms[identity] = None
                else:
                    atoms[identity] = row
                binding = _source_tool_declaration(parsed.body)
                current_sources.setdefault(identity, []).append({
                    'atom_id': identity,
                    'source_path': row['source_path'],
                    'sha256': row['sha256'],
                    'tool_binding': binding,
                })
                if binding is not None:
                    entry = self.root / binding.get('entrypoint', '')
                    tool = {**binding, 'source_atom': identity,
                            'source_path': row['source_path'],
                            'sha256': row['sha256'], 'scope_unit': row['scope_unit'],
                            'summary': parsed.body.split('##', 1)[0].replace('# Summary', '').strip()}
                    if _direct_contract_claims(tool):
                        # Direct Tool source is only an executable capability
                        # after the one closed declaration is server-exposed.
                        tool['availability'] = (
                            'mcp' if (_exact_direct_contract(tool) is not None
                                      and tool.get('mcp_name') in self.exposed) else 'unresolved'
                        )
                    else:
                        tool['availability'] = ('mcp' if binding.get('mcp_name') in self.exposed
                                                else 'source' if entry.is_file() else 'missing')
                    source_tools.append(tool)
            except (ValueError, OSError, KeyError, TypeError) as error:
                issues.append(f'{path.relative_to(self.root)}: {type(error).__name__}')
        valid = {key: value for key, value in atoms.items() if value}
        package_selected, tools = self._selected_package_tools(current_sources, issues)
        if not package_selected:
            tools = source_tools
        counts = {}
        for tool in tools:
            counts[tool['name']] = counts.get(tool['name'], 0) + 1
        tools = [
            tool for tool in tools
            if counts[tool['name']] == 1
            and (package_selected or tool['source_atom'] in valid)
        ]
        tools.extend(self._admitted_selected_route_tools(issues))
        return valid, tools, issues

    def discover(self, request, operations=False):
        atoms, tools, issues = self.catalog()
        rows = list(atoms.values()) if operations else tools
        if operations:
            rows = [row for row in rows if row['content_role'] == 'Operations']
            for row in rows:
                bindings = [tool for tool in tools if row['id'] in tool.get('action_ids', []) + tool.get('workflow_ids', [])]
                direct = [tool for tool in bindings if _direct_contract_claims(tool)]
                # D591 and D602 are direct MCP Actions, not generic source
                # fallbacks: source-only, malformed, or ambiguous bindings
                # remain unresolved even when their carriers are readable.
                if direct:
                    row['availability'] = 'mcp' if any(tool['availability'] == 'mcp' for tool in direct) else 'unresolved'
                else:
                    row['availability'] = 'mcp' if any(tool['availability'] == 'mcp' for tool in bindings) else 'source' if bindings else 'unresolved'
                row['tools'] = [tool['name'] for tool in bindings]
                row['summary'] = row['content'].split('##', 1)[0].replace('# Summary', '').strip()
        words = request.query.lower().split()
        rows = [row for row in rows if all(word in json.dumps(row).lower() for word in words)]
        if request.scope_unit:
            structure = tomllib.loads(self.read(self._control_root() / 'project_structure.toml').decode())
            units = structure.get('scope_units', [])
            selected = {request.scope_unit}
            if not any(unit['scope_unit_name'] == request.scope_unit for unit in units):
                raise ValueError('Unknown Scope Unit')
            if request.include_descendants:
                for _ in units:
                    selected.update(unit['scope_unit_name'] for unit in units if unit.get('parent') in selected)
            rows = [row for row in rows if row.get('scope_unit', atoms.get(row.get('source_atom'), {}).get('scope_unit')) in selected]
        if request.availability:
            rows = [row for row in rows if row.get('availability') == request.availability]
        rows.sort(key=lambda row: row.get('name', row.get('id', '')))
        return {'matches': [{key: value for key, value in row.items() if key != 'content'}
                            for row in rows[request.offset:request.offset + request.limit]],
                'total': len(rows), 'next_offset': request.offset + request.limit
                if request.offset + request.limit < len(rows) else None,
                'coverage_issues': issues}

    def context(self, request):
        atoms, tools, issues = self.catalog()
        row = atoms.get(request.id)
        if row is None:
            matches = [tool for tool in tools if tool['name'] == request.id]
            if len(matches) != 1:
                raise ValueError('Unknown or ambiguous capability')
            row = matches[0]
        selected = [item for item in tools if item.get("selected_route") and request.id in {
            item["name"], item["source_atom"], *item["action_ids"]
        }]
        if selected:
            definition = dict(row)
            routes = sorted(item["name"] for item in selected)
            definition.update({"availability": "mcp", "tools": routes,
                               "definition_manifest": selected[0]["definition_manifest"],
                               "source_freshness": selected[0]["source_freshness"]})
            return {"definition": definition, "related_definitions": [],
                    "input_schema": (self._selected_route_input_schema(routes[0])
                                     if len(routes) == 1 else None),
                    "context_complete": True, "coverage_issues": issues}
        identities = set(row.get('action_ids', []) + row.get('workflow_ids', []))
        if 'source_atom' in row:
            identities.add(row['source_atom'])
        content = row.get('content', '') + json.dumps(row.get('properties', {}))
        import re
        identities.update(re.findall(r'CA-[RMEDO]-\d+', content))
        related = [atoms[identity] for identity in sorted(identities) if identity in atoms and identity != request.id]
        related.extend(item for item in atoms.values() if item['scope_unit'] == row.get('scope_unit')
                       and item['content_role'] in ('Requirement', 'Method', 'Evaluation', 'Delivery')
                       and item not in related and item['id'] != request.id)
        budget, selected = 256 * 1024, []
        used = len(json.dumps(row).encode())
        for item in related:
            size = len(json.dumps(item).encode())
            if used + size > budget:
                break
            selected.append(item)
            used += size
        models = {'DISCOVER_TOOLS': Query, 'DISCOVER_OPERATIONS': Query,
                  'GET_EXECUTION_CONTEXT': Context, 'GET_EXECUTION_STATUS': Observation,
                  'RESUME_EXECUTION_CONTEXT': Observation, 'WATCH_EXECUTION': Watch}
        direct_schema = self._direct_tool_input_schema(request.id, row, tools)
        return {'definition': row, 'related_definitions': selected,
                'input_schema': (direct_schema if direct_schema is not None
                                 else models[request.id].model_json_schema() if request.id in models else None),
                'context_complete': len(selected) == len(related) and used <= budget,
                'coverage_issues': issues}

    def status(self, request):
        import re
        if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,127}', request.run_id):
            raise ValueError('Invalid Run ID')
        path = self.root / '.caprmedio_tmp/rmed-base-revise' / request.run_id / 'progress.json'
        if not path.is_file():
            admission = self.root / '.caprmedio_install/workflow_orchestrator/runs' / request.run_id / 'request.json'
            if admission.is_file():
                import sys
                sys.path.insert(0, str(Path(__file__).resolve().parents[2] / '203_APPS/WORKFLOW_ORCHESTRATOR'))
                from backend import status as queued_status
                from contracts import Status
                result = queued_status(self.root, Status(run_id=request.run_id))
                saved = json.loads(self.read(admission))
                return result, {'request': saved['request'], 'selection': saved['selection_bindings'],
                                'criteria': saved['rule_bindings'], 'events': [], 'reports': [], 'handoffs': []}
            raise ValueError('Run not found; only RMED Atoms Base Revise backend is registered')
        state = json.loads(self.read(path))
        result = {key: state.get(key) for key in ('workflow_run_id', 'workflow_name', 'outcome',
                  'progress', 'report_path', 'recording_blockers', 'updated_at', 'coverage_gates')}
        result['operator_question'] = next((row['operator_question'] for row in
            state.get('coverage_gates', {}).values() if row.get('operator_question')), None)
        if request.include_results:
            result['results'] = state.get('reports', [])
            result['history'] = state.get('history', [])
            if request.ordinal is not None:
                if request.ordinal >= len(result['results']):
                    raise ValueError('Ordinal outside frozen selection')
                result['results'] = [result['results'][request.ordinal]]
                result['history'] = [result['history'][request.ordinal]] if result['history'] else []
        return result, state

    def resume(self, request):
        result, state = self.status(request)
        result.update({key: state.get(key) for key in ('request', 'selection', 'criteria', 'handoffs')})
        result['pending'] = state.get('progress', {}).get('states', [])
        drift = []
        for selected in state.get('selection', []):
            source = selected.get('source', {})
            try:
                digest = hashlib.sha256(self.read(self.root / source['path'])).hexdigest()
                if digest != source.get('sha256'):
                    drift.append({'atom_id': selected.get('atom_id'), 'state': 'changed'})
            except (OSError, ValueError, KeyError):
                drift.append({'atom_id': selected.get('atom_id'), 'state': 'unavailable'})
        result['source_drift'] = drift
        return result

    async def watch(self, request):
        previous = None
        if request.cursor:
            if len(request.cursor) > 4096:
                raise ValueError('Oversized cursor')
            try:
                previous = json.loads(base64.urlsafe_b64decode(request.cursor).decode())
                if previous['run_id'] != request.run_id:
                    raise ValueError('Cursor belongs to another Run')
                if not all(key in previous for key in ('position', 'fingerprint', 'prefix')):
                    raise ValueError('Incomplete cursor')
            except (ValueError, KeyError, TypeError, UnicodeError) as error:
                raise ValueError('Invalid cursor') from error
        deadline = time.monotonic() + request.timeout_seconds
        while True:
            result, state = await asyncio.to_thread(self.status, request)
            events = []
            for row in state.get('events', []):
                if not row.get('receipt'):
                    break
                events.append(row['event'])
            fingerprint = hashlib.sha256(json.dumps(result, sort_keys=True).encode()).hexdigest()
            position = previous['position'] if previous else 0
            if not isinstance(position, int) or position < 0:
                raise ValueError('Invalid cursor position')
            if position > len(events):
                raise ValueError('Cursor is ahead of recorded evidence')
            prefix = hashlib.sha256(json.dumps(events[:position], sort_keys=True).encode()).hexdigest()
            if previous and previous.get('prefix') != prefix:
                raise ValueError('Recorded evidence differs from cursor')
            changed = previous is None or previous['fingerprint'] != fingerprint or position != len(events)
            terminal = result['outcome'] in ('completed', 'failed', 'interrupted')
            if changed or terminal or time.monotonic() >= deadline:
                cursor = base64.urlsafe_b64encode(json.dumps({'run_id': request.run_id,
                    'position': len(events), 'fingerprint': fingerprint,
                    'prefix': hashlib.sha256(json.dumps(events, sort_keys=True).encode()).hexdigest()}).encode()).decode()
                return {'status': result, 'notifications': events[position:], 'changed': changed,
                        'terminal': terminal, 'cursor': cursor}
            await asyncio.sleep(0.2)
