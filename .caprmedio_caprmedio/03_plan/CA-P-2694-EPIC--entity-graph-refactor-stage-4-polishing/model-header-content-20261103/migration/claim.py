"""Conservative, fence-aware conversion of ordinary RMED Claim sections."""
import re

ROOT = {'summary', 'claim scope', 'claim', 'semantics', 'details'}
CHILD = {'formal claim', 'prose claim'}
HEADING = re.compile(r'^(#{2,3})[ \t]+(.+?)[ \t]*\r?\n?$')
FENCE = re.compile(r'^\s*(`{3,}|~{3,})([^\r\n]*)')


class Ambiguous(ValueError):
    pass


def sections(body):
    lines = body.splitlines(keepends=True)
    found = []
    fence = None
    for i, line in enumerate(lines):
        match = FENCE.match(line)
        if fence:
            if match and match.group(1)[0] == fence[0] and len(match.group(1)) >= len(fence) and not match.group(2).strip():
                fence = None
            continue
        if match:
            fence = match.group(1)
            continue
        match = HEADING.match(line)
        if match:
            level, name = len(match.group(1)), match.group(2).strip().lower()
            if (level == 2 and name in ROOT) or (level == 3 and name in CHILD):
                found.append((i, level, name))
    if fence:
        raise Ambiguous(f'line {len(lines)}: unclosed fence')
    return lines, found


def migrate_claim(body):
    lines, found = sections(body)
    roots = [(i, name) for i, level, name in found if level == 2]
    for name in ROOT:
        occurrences = [i for i, n in roots if n == name]
        if len(occurrences) > 1:
            raise Ambiguous(f'line {occurrences[1] + 1}: duplicate {name}')
    claims = [i for i, name in roots if name == 'claim']
    if len(claims) != 1:
        raise Ambiguous('line 1: expected one Claim')
    start = claims[0]
    end = next((i for i, _ in roots if i > start), len(lines))
    scopes = [i for i, name in roots if name == 'claim scope']
    scope = scopes[0] if scopes else None
    if scope is not None and scope > start:
        raise Ambiguous(f'line {scope + 1}: Claim scope follows Claim')
    scope_end = next((i for i, _ in roots if scope is not None and i > scope), len(lines)) if scope is not None else None
    children = [(i, name) for i, level, name in found if level == 3 and start < i < end]
    if len({name for _, name in children}) != len(children):
        raise Ambiguous(f'line {children[0][0] + 1}: duplicate Claim child')
    if children and scope is None and not ''.join(lines[start + 1:children[0][0]]).strip():
        valid = True
        for index, (position, name) in enumerate(children):
            stop = children[index + 1][0] if index + 1 < len(children) else end
            value = ''.join(lines[position + 1:stop])
            if not value.strip():
                raise Ambiguous(f'line {position + 1}: empty {name}')
            if name == 'formal claim' and not re.fullmatch(r'\s*(?:`{3,}|~{3,})CFEL[^\n]*\n[\s\S]*?(?:`{3,}|~{3,})\s*', value, re.I):
                valid = False
        if valid:
            return body
    # Existing child labels delimit values; fence parsing below retains their content.
    content = [line for index, line in enumerate(lines[start + 1:end], start + 1)
               if index not in {position for position, _ in children}]
    blocks = []
    outside = []
    i = 0
    while i < len(content):
        match = FENCE.match(content[i])
        if not match:
            outside.append(content[i]); i += 1; continue
        marker, info = match.groups()
        j = i + 1
        while j < len(content):
            close = FENCE.match(content[j])
            if close and close.group(1)[0] == marker[0] and len(close.group(1)) >= len(marker) and not close.group(2).strip():
                break
            j += 1
        if j == len(content):
            raise Ambiguous(f'line {start + i + 2}: unclosed fence')
        block = content[i:j + 1]
        if info.strip().lower() == 'cfel':
            blocks.append((i, j + 1, block))
        else:
            outside.extend(block)
        i = j + 1
    if len(blocks) > 1:
        raise Ambiguous(f'line {start + blocks[1][0] + 2}: multiple CFEL fences')
    if blocks and ''.join(outside).strip():
        prose_words = ''.join(outside)
        if re.search(r'\b(?:following|preceding|above|below)\s+(?:CFEL|formula|predicate|code|block)|\b(?:CFEL|formula|predicate|code|block)\s+(?:above|below)\b', prose_words, re.I):
            raise Ambiguous(f'line {start + 1}: positional prose reference around CFEL requires review')
    scope_text = lines[scope + 1:scope_end] if scope is not None else []
    prose = scope_text + outside
    if not ''.join(prose).strip() and not blocks:
        raise Ambiguous(f'line {start + 1}: empty Claim')
    nl = '\r\n' if lines[start].endswith('\r\n') else '\n'
    replacement = [lines[start], nl]
    if blocks:
        replacement += ['### Formal Claim' + nl, nl] + blocks[0][2]
        if not replacement[-1].endswith(('\n', '\r')): replacement.append(nl)
        replacement.append(nl)
    if ''.join(prose).strip():
        replacement += ['### Prose Claim' + nl, nl] + prose
    result = lines[:start] + replacement + lines[end:]
    if scope is not None:
        del result[scope:scope_end]
    return ''.join(result)
