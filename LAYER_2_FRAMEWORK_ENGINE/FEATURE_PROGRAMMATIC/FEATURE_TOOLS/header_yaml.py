# CA-D-657@11

"""Safe, source-preserving scalar reads for declared Headers."""


from typing import Any

import yaml
from yaml.events import AliasEvent, MappingEndEvent, MappingStartEvent, SequenceEndEvent, SequenceStartEvent
from yaml.nodes import MappingNode, Node, ScalarNode, SequenceNode

from carrier_aliases import carrier_read_view
from header_groups import header_path


_STRING = "tag:yaml.org,2002:str"


def _metadata(document: Node) -> dict[str, Any]:
    if not isinstance(document, MappingNode):
        raise ValueError("Header must contain one mapping.")
    seen: set[int] = set()
    pending = [(document, 1)]
    while pending:
        node, depth = pending.pop()
        if id(node) in seen or depth > 64 or len(seen) >= 100_000:
            raise ValueError("Header aliases or excessive YAML resources are unsupported.")
        seen.add(id(node))
        if isinstance(node, MappingNode):
            keys = [key.value for key, _ in node.value if isinstance(key, ScalarNode) and key.tag == _STRING]
            if len(keys) != len(node.value) or len(set(keys)) != len(keys):
                raise ValueError("Header keys must be unique strings; merge keys are unsupported.")
            pending.extend((child, depth + 1) for pair in node.value for child in pair)
        elif isinstance(node, SequenceNode):
            pending.extend((child, depth + 1) for child in node.value)
    loader = yaml.SafeLoader("")
    try:
        metadata = loader.construct_object(document, deep=True)
    except (yaml.YAMLError, RecursionError) as error:
        raise ValueError("Header YAML is invalid.") from error
    finally:
        loader.dispose()
    if not isinstance(metadata, dict):
        raise ValueError("Header must contain one mapping.")
    carrier_read_view(metadata)
    return metadata


def _check_resources(frontmatter: str) -> None:
    depth = 0
    for count, event in enumerate(yaml.parse(frontmatter, Loader=yaml.SafeLoader), 1):
        if isinstance(event, AliasEvent):
            raise ValueError("Header YAML aliases are unsupported.")
        if isinstance(event, (MappingStartEvent, SequenceStartEvent)):
            depth += 1
        if isinstance(event, (MappingEndEvent, SequenceEndEvent)):
            depth -= 1
        if depth > 64 or count > 100_000:
            raise ValueError("Header YAML exceeds the parser safety ceiling.")


def _document(frontmatter: str) -> MappingNode:
    try:
        _check_resources(frontmatter)
        document = yaml.compose(frontmatter, Loader=yaml.SafeLoader)
        if document is None:
            mark = yaml.error.Mark("<Header>", 0, 0, 0, frontmatter, 0)
            document = MappingNode("tag:yaml.org,2002:map", [], mark, mark, flow_style=False)
        if not isinstance(document, MappingNode):
            raise ValueError("Header must contain one mapping.")
        _metadata(document)
        return document
    except (yaml.YAMLError, RecursionError) as error:
        raise ValueError("Header YAML is invalid.") from error


def parse_header(frontmatter: str) -> dict[str, Any]:
    """Read actual Header keys with the same duplicate and alias safety as scalar access."""
    return _metadata(_document(frontmatter))


def _node(document: MappingNode, path: tuple[str, ...]) -> Node | None:
    current: Node = document
    for part in path:
        if not isinstance(current, MappingNode):
            raise ValueError("Header Property parent must be a mapping.")
        matches = [value for key, value in current.value if key.value == part]
        if not matches:
            return None
        current = matches[0]
    return current


def header_scalar_node(document: MappingNode, name: str) -> ScalarNode | None:
    """Return the original scalar node, retaining exact source marks."""
    metadata = _metadata(document)
    node = _node(document, header_path(name, metadata))
    if node is not None and not isinstance(node, ScalarNode):
        raise ValueError(f"Header {name} must be a scalar.")
    return node


def header_scalar(frontmatter: str, name: str) -> str | None:
    node = header_scalar_node(_document(frontmatter), name)
    return node.value if node is not None else None
