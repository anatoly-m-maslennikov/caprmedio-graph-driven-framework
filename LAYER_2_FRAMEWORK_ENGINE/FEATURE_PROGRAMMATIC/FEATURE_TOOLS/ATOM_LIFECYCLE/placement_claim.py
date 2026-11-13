"""Parse literal Python Delivery placement claims without executing source."""
import ast
from pathlib import PurePosixPath


def _folder(value):
    if value in ('', '<status folder>'):
        return
    if (not isinstance(value, str) or '\\' in value or '\x00' in value
            or PurePosixPath(value).is_absolute() or str(PurePosixPath(value)) != value
            or any(part in ('', '.', '..') for part in value.split('/'))):
        raise ValueError('Unsafe placement folder')


def parse_placement_claim(body):
    """Return native rows, or None for non-native Claims. Never execute Python."""
    from markdown_it import MarkdownIt
    from FEATURE_WORKBENCH_BACKEND.markdown_content import content_key

    tokens = MarkdownIt('commonmark').parse(body)
    headings, fences = [], []
    for index, token in enumerate(tokens):
        if token.type == 'heading_open':
            level = int(token.tag[1:])
            headings = [h for h in headings if h[0] < level]
            headings.append((level, content_key(tokens[index + 1].content)))
        elif token.type == 'fence' and tuple(h[1] for h in headings) == ('claim', 'formal_claim'):
            fences.append(token)
    candidates = [rules for fence in fences if fence.info.strip().casefold() == 'python'
                  and (rules := parse_placement_rules(fence.content)) is not None]
    if not candidates:
        return None
    if len(fences) != 1:
        raise ValueError('Native placement Claim requires one formal fence')
    return candidates[0]


def parse_placement_rules(source):
    """Return literal placement rules, or None for a different Python Claim."""
    if "placement_rules" not in source:
        return None
    try:
        tree = ast.parse(source)
    except SyntaxError as error:
        raise ValueError('Invalid placement Python syntax') from error
    if not any(isinstance(node, ast.Name) and node.id == 'placement_rules' and isinstance(node.ctx, ast.Store)
               for node in ast.walk(tree)):
        return None
    if (len(tree.body) != 1 or not isinstance(tree.body[0], ast.Assign)
            or len(tree.body[0].targets) != 1 or not isinstance(tree.body[0].targets[0], ast.Name)
            or tree.body[0].targets[0].id != 'placement_rules'):
        raise ValueError('Expected one placement_rules assignment')
    value = tree.body[0].value
    if not isinstance(value, ast.Tuple) or not value.elts:
        raise ValueError('Expected nonempty placement rule tuple')
    for entry in value.elts:
        if not isinstance(entry, ast.Dict) or any(not isinstance(k, ast.Constant) or type(k.value) is not str for k in entry.keys):
            raise ValueError('Placement rules require literal string keys')
        keys = [key.value for key in entry.keys]
        if len(keys) != len(set(keys)):
            raise ValueError('Duplicate placement rule key')
    try:
        rules = ast.literal_eval(value)
    except (ValueError, SyntaxError, TypeError) as error:
        raise ValueError('Placement rules require literal data') from error
    for rule in rules:
        if rule.get('kind') == 'role_root':
            if set(rule) != {'kind'}:
                raise ValueError('Invalid role root rule')
        elif rule.get('kind') == 'status':
            if (set(rule) != {'kind', 'role', 'status', 'base', 'folder'}
                    or rule['base'] not in ('role', 'container')
                    or not isinstance(rule['status'], str) or not rule['status']
                    or (rule['role'] is not None and (not isinstance(rule['role'], str) or not rule['role']))
                    or not isinstance(rule['folder'], str)):
                raise ValueError('Invalid status placement rule')
            if rule['status'] == '*' and (rule['role'] is not None or rule['base'] != 'container'
                                          or rule['folder'] != '<status folder>'):
                raise ValueError('Invalid wildcard placement rule')
            _folder(rule['folder'])
        else:
            raise ValueError('Unknown placement rule kind')
    return rules
