"""Lint a selected Python Model Claim against Current Project Declarations."""

from collections import defaultdict
from pathlib import Path
import re
import sys

from ATOM_LIFECYCLE.source import bind_query_reader, select_sources
from FEATURE_APPS.APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relation_registry import compile_relation_registry
from FEATURE_FORMAL_MODEL_ENGINE.model_catalog import class_bindings
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier
from carrier_aliases import carrier_read_view, named_value_token
from lint_python_model_claim import _markdown_blocks, lint_python_model_claim, _canonical_address

_GRAPH_TOOLS = Path(__file__).resolve().parents[1] / "FEATURE_TOOLS" / "GENERATE_ENTITY_GRAPH"
if str(_GRAPH_TOOLS) not in sys.path:
    sys.path.insert(0, str(_GRAPH_TOOLS))

from cfel_claim_constraints import extract_claim_constraints
from contract_graph import compose_contract_graph
from subject_projection_audits import select_model_subjects
from subject_projection_data import _property_parts, _rule_groups

_DECLARATION_FORMS = (
    "declaration", "definition", "entity_definition", "relation_definition",
    "relation_declaration", "operator_declaration", "construct_declaration", "function_declaration",
)


def _column(columns, *names):
    fields = [f'"{name}"' for name in names if name in columns]
    return "coalesce(" + ", ".join(fields) + ")" if len(fields) > 1 else next(iter(fields), "NULL")


def _project_rows(workbench, reference):
    columns = {column["name"] for column in workbench.schema()["tables"]["atoms"]}
    role = _column(columns, "header.context.role", "header.role", "header.content_role")
    form = _column(columns, "header.context.form", "header.form", "header.type")
    version = _column(columns, "header.state.version", "header.state.version_number",
                      "header.version", "header.version_number")
    quoted_reference = "'" + reference.replace("'", "''") + "'"
    sql = f"""
        SELECT reference, relative_path, filename, status_group, {version}, hash
        FROM atoms
        WHERE reference = {quoted_reference} OR (
            status_group = 'Current' AND lower({role}) = 'requirement' AND
            replace(lower({form}), ' ', '_') IN {_DECLARATION_FORMS}
        )
        ORDER BY reference, relative_path, filename
    """
    page = workbench.run(sql, save=False, result_delivery="inline")
    count, query_id = page["row_count"], page["query_id"]
    offset = 0
    while True:
        rows = page["rows"]
        if page["offset"] != offset or (not rows and offset < count):
            raise ValueError("Incomplete Workbench query result")
        yield from rows
        offset += len(rows)
        if not page["has_more"]:
            if offset != count:
                raise ValueError("Incomplete Workbench query result")
            return
        page = workbench.page(query_id, offset, result_delivery="inline")


def graph_claim_addresses(graph):
    """Supply exact Model addresses and their unique short spellings for linting."""
    nodes = [node for key in ("entities", "components", "namespaces") for node in graph[key]]
    owned = {node["target"] for node in nodes}
    addresses = {node["target"] for node in nodes if len(node["own"]) == 1}
    properties = {address: _property_parts(address) for address in owned}
    ancestors = {node["target"]: [parent["target"] for parent in node["transitive_ancestors"]]
                 for node in nodes if node["kind"] == "primary_node"}
    names = defaultdict(set)
    for node in nodes:
        target = node["target"]
        if node["kind"] != "primary_node":
            continue
        short = target.rsplit("/", 1)[-1]
        if short != target and "(" not in short and short not in owned:
            names[short].add(target)
        if target not in addresses:
            continue
        rules = []
        for prop in node["inherited_property_declarations"]:
            origin = prop["target"]
            if (parts := properties.get(origin)) is not None:
                rules.append({"identity": origin, "origin_entity": parts[0], "relative_name": parts[1],
                              "declaration_refs": prop["declaration_refs"], "source_refs": []})
        effective = _rule_groups(target, rules, ancestors, lambda rule: rule["relative_name"])
        inherited = defaultdict(set)
        for rule in effective["inherited"]:
            inherited[rule["relative_name"]].add(rule["identity"])
        addresses.update(f"{target}.{suffix}" for suffix, origins in inherited.items()
                         if f"{target}.{suffix}" not in owned and len(origins) == 1 and origins <= addresses)
    aliases = {short: target for short, targets in names.items() if len(targets) == 1
               for target in targets if target in addresses}
    primary = {node["target"] for node in nodes if node["kind"] == "primary_node"
               and len(node["own"]) == 1}
    tree = graph["narrowing_tree"]
    identities = {node["id"]: node["identity"] for node in tree["nodes"]}
    paths = defaultdict(set)
    for edge in tree["edges"]:
        child = identities[edge["relation_source"]]
        parent = identities[edge["relation_target"]]
        terminal = child.rsplit("/", 1)[-1]
        if (child not in primary or parent not in primary or not edge.get("source_bindings")
                or not re.fullmatch(r"[A-Za-z_][A-Za-z_0-9 -]*", terminal)
                or not re.fullmatch(r"[A-Za-z_][A-Za-z_0-9 -]*", parent)):
            continue
        paths[parent + "/" + terminal].add(child)
    for path, targets in paths.items():
        if len(targets) == 1 and path not in owned and path not in aliases:
            target = next(iter(targets))
            if "/" not in target:
                aliases[path] = target
    return addresses, aliases


def _relation_declaration_context(view):
    relation_declaration = None
    if (view and named_value_token(view.get("content_role")) == "requirement"
            and named_value_token(view.get("type")) in {"declaration", "relation_declaration"}):
        subjects = view.get("subjects")
        active = subjects.get("active", subjects.get("governs")) if isinstance(subjects, dict) else None
        if isinstance(active, str):
            try:
                address = _canonical_address(active)
                match = re.fullmatch(r"CFEL <\+ Relation//([A-Za-z_][A-Za-z_0-9]*)", address)
                if match and active.startswith("CAPRMEDIO_MODEL <+ "):
                    relation_declaration = match.group(1)
            except ValueError:
                pass
    return relation_declaration


def lint_project_claim(workbench, selection, reference: str) -> tuple[str, ...]:
    """Check the indexed source's syntax and references without executing its Claim."""
    if not isinstance(reference, str) or not reference:
        raise ValueError("Expected an Atom reference")
    indexed = list(_project_rows(workbench, reference))
    references = {row[0] for row in indexed if isinstance(row[0], str)}
    if reference not in references:
        raise ValueError(f"{reference}: no indexed Atom source")
    candidates = {path for _, path in workbench.lifecycle_candidates(selection, references=tuple(sorted(references)))}
    rows = {}
    for ref, directory, filename, group, version, _row_hash in indexed:
        path = selection.root / directory / filename
        if path not in candidates:
            continue
        if ref in rows:
            raise ValueError(f"{ref}: ambiguous indexed Atom source")
        rows[ref] = (path, group, version)
    if reference not in rows:
        raise ValueError(f"{reference}: no indexed authoritative Atom source")
    with workbench.lifecycle_read_scope(), bind_query_reader(workbench):
        pins = select_sources(selection, list(rows))
    if (list(_project_rows(workbench, reference)) != indexed
            or workbench.lifecycle_declarations().digest != selection.declaration_digest):
        raise ValueError("Project Declaration inventory changed during lint")

    current = []
    blocks = []
    selected_view = None
    for ref, pin in pins.items():
        path, group, version = rows[ref]
        if pin.path != path or pin.version != version:
            raise ValueError(f"{ref}: indexed Atom source changed")
        parsed = parse_carrier(pin.raw, path)
        if ref == reference:
            blocks = list(_markdown_blocks(parsed.text))
        view = carrier_read_view(parsed.metadata)
        if ref == reference:
            selected_view = view
        if (group != "Current" or named_value_token(view.get("content_role")) != "requirement"
                or named_value_token(view.get("type")) not in _DECLARATION_FORMS):
            continue
        source = {"path": str(path.relative_to(selection.root)), "atom_id": pin.atom_id,
                  "version": pin.version, "sha256": pin.sha256}
        current.append({"source": source, "read_view": view, "subjects": view.get("subjects"),
                        "body": parsed.body, "metadata": parsed.metadata})
    if not blocks:
        return (f"{rows[reference][0]}: no Python Formal Claim",)

    selected, _ = select_model_subjects(current)
    graph = compose_contract_graph(selected)
    addresses, address_bindings = graph_claim_addresses(graph)
    bindings = {name: {records[0][0]} for name, records in class_bindings(selected).items() if len(records) == 1}
    registry = compile_relation_registry([
        {"status_group": "Current", "source_path": row["source"]["path"],
         "id": row["source"]["atom_id"], "ref": row["source"]["atom_id"], "version": row["source"]["version"],
         "role": row["read_view"].get("content_role"), "form": row["read_view"].get("type"),
         "content_markdown": row["body"], "_model_class_bindings": bindings}
        for row in selected
    ])
    operators, glyphs = defaultdict(list), defaultdict(set)
    ambiguous_relations = {row["target"] for row in graph["relations"] if len(row["own"]) != 1}
    relations = (registry.names - ambiguous_relations) | {
        alias for alias, canonical in registry.aliases.items()
        if canonical not in ambiguous_relations and alias not in ambiguous_relations
    }
    for row in graph["relations"]:
        if len(row["own"]) == 1 and row["target"] in relations:
            for item in row["metadata"]:
                if item["kind"] in {"notation", "reverse_notation"}:
                    glyphs[item["value"]].add(row["target"])
    operator_clauses = [clause for node in graph["entities"] + graph["components"]
                        for entry in node["own"] for clause in entry["clauses"]]
    for row in selected:
        if named_value_token(row["read_view"].get("type")) == "operator_declaration":
            clauses, _ = extract_claim_constraints(row)
            operator_clauses.extend(clauses)
    for clause in operator_clauses:
        if clause["kind"] == "operator_symbol":
            operators[clause["operator"]].append(clause["symbol"])

    relation_declaration = _relation_declaration_context(selected_view)
    return tuple(diagnostic for code, line in blocks for diagnostic in lint_python_model_claim(
        code, path=str(rows[reference][0]), first_line=line, declared_addresses=addresses,
        relation_names=relations,
        relation_aliases={glyph: next(iter(names)) for glyph, names in glyphs.items() if len(names) == 1},
        python_class_bindings=bindings, operator_catalog=operators, require_declared_aliases=True,
        address_bindings=address_bindings, relation_declaration=relation_declaration,
    ))
