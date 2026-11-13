"""Canonicalize declared Model class Subjects without depending on graph code."""
import re
import subject_notation as notation


def model_class_target(subject, entity_name, *, require_namespace=True):
    if not isinstance(subject, str) or not isinstance(entity_name, str):
        return None
    try:
        expression = notation.parse_subject_expression(subject, subject_profile="approved").expression
    except notation.SubjectNotationError:
        return None
    if (isinstance(expression, notation.Path) and isinstance(expression.head, notation.Name)
            and expression.head.value == "CAPRMEDIO_MODEL" and not expression.steps):
        return "CAPRMEDIO_MODEL" if entity_name.casefold() == "model" else None
    root = expression.endpoints[0] if isinstance(expression, notation.RelationChain) else expression
    root_name = root.head.value if isinstance(root.head, notation.Name) else None
    if root_name in {"CAPRMEDIO_STRUCTURE", "CAPRMEDIO"}:
        if root_name != "CAPRMEDIO" or not isinstance(expression, notation.RelationChain) or len(expression.endpoints) < 2 or not isinstance(expression.endpoints[1].head, notation.Name) or expression.endpoints[1].head.value != "MODEL":
            return None
    local = notation.namespace_local_expression(expression)
    if local is None:
        if require_namespace or root_name == "CAPRMEDIO_MODEL":
            return None
        local = expression
    if isinstance(local, notation.RelationChain):
        if (len(local.endpoints) != 2 or len(local.links) != 1
                or local.links[0].operator != "<+" or local.links[0].relation_type is not None
                or not isinstance(local.endpoints[0].head, notation.Name)
                or local.endpoints[0].head.value != "CFEL" or local.endpoints[0].steps):
            return None
        local = local.endpoints[1]
    if (not isinstance(local, notation.Path) or not isinstance(local.head, notation.Name)
            or local.value_format is not None or local.value_cardinality is not None
            or any(step.operator != "/" or not isinstance(step.operand, (notation.Name, notation.Qualification)) for step in local.steps)):
        return None
    terminal = local.steps[-1].operand if local.steps else local.head
    if isinstance(terminal, notation.Qualification):
        steps = terminal.relative_path.steps
        if not steps or steps[-1].operator != ":=" or not isinstance(steps[-1].operand, notation.ValueLiteral):
            return None
        terminal = steps[-1].operand
    if not isinstance(terminal, (notation.Name, notation.ValueLiteral)):
        return None
    norm = lambda value: re.sub(r"[^a-z0-9]", "", value.casefold())
    if norm(terminal.value) != norm(entity_name):
        return None
    return notation.render_subject(local)
