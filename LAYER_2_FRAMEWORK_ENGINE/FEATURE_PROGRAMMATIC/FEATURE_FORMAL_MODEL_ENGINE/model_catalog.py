"""Bind native class names to selected Model Declaration targets."""
from collections import defaultdict
from collections.abc import Mapping
from markdown_it import MarkdownIt
from model_class_subject import model_class_target
from carrier_aliases import matches_named_value


def _native_block(body):
    headings = []
    for index, token in enumerate(tokens := MarkdownIt("commonmark").parse(body)):
        if token.type == "heading_open":
            level = int(token.tag[1:])
            headings = [item for item in headings if item[0] < level]
            headings.append((level, tokens[index + 1].content.casefold().strip()))
        elif token.type == "fence" and token.info.strip().casefold() == "python" and tuple(x[1] for x in headings) == ("claim", "formal claim"):
            yield token.content


def class_bindings(selected_carriers):
    from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import parse_native_model_claim
    declarations = defaultdict(list)
    for carrier in selected_carriers:
        view = carrier.get("read_view", {})
        if not matches_named_value(view.get("content_role"), "Requirement") or not matches_named_value(view.get("type"), "Declaration"):
            continue
        subjects = carrier.get("subjects")
        if not isinstance(subjects, Mapping):
            continue
        subject = subjects.get("governs")
        for code in _native_block(carrier.get("body", "")):
            declaration = parse_native_model_claim(code)
            if declaration is None or declaration["kind"] != "entity":
                continue
            name = declaration["arguments"].get("entity_class")
            target = model_class_target(subject, declaration["arguments"].get("entity_name"))
            if target is not None and name is not None and any(row["name"] == name for row in declaration["classes"]):
                declarations[name].append((target, dict(carrier["source"])))
    return dict(declarations)

def compile_native(code, bindings):
    from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import parse_native_model_claim
    from FEATURE_FORMAL_MODEL_ENGINE.compiler_claim import compiler_model_statements
    declaration = parse_native_model_claim(code)
    lookup = {name: {rows[0][0]} for name, rows in bindings.items() if len(rows) == 1}
    return compiler_model_statements(declaration, model_class_bindings=lookup)

def bindings_from_workbench_rows(rows):
    """Build a fresh catalog from exactly the selected Workbench source rows."""
    import hashlib
    from carrier_aliases import carrier_read_view
    from FEATURE_WORKBENCH_BACKEND.content_schema import _is_declaration
    carriers = []
    for row in rows:
        if not _is_declaration(row):
            continue
        metadata = row.get('header_json')
        body = row.get('_content_bytes')
        if not isinstance(metadata, dict) or not isinstance(body, bytes):
            continue
        view = carrier_read_view(metadata)
        atom_id, version = view.get('atom_id'), view.get('version')
        if not isinstance(atom_id, str) or type(version) is not int:
            continue
        source = {'atom_id': atom_id, 'version': version, 'path': row.get('source_path',''), 'sha256': hashlib.sha256(body).hexdigest()}
        carriers.append({'source': source, 'subjects': view.get('subjects'), 'metadata': metadata,
                         'read_view': view, 'body': body.decode('utf-8'), 'raw_body': body.decode('utf-8')})
    catalog = class_bindings(carriers)
    return {name: {records[0][0]} for name, records in catalog.items() if len(records) == 1}
