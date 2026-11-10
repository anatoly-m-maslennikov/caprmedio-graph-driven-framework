// @ts-nocheck
// CA-M-468@7
export function statusCompletion(text, cursor, schema, tokenEnd) {
  const match = /"(header(?:\.[a-z0-9_]+)*\.status)"\s*=\s*'((?:[^']|'')*)$/.exec(text.slice(0, cursor));
  if (!match) return null;
  const column = schema.tables.atoms?.find((candidate) => candidate.name === match[1]);
  if (!column) return null;
  const values = column.values ?? [];
  return {
    from: cursor - match[2].length,
    to: tokenEnd ?? (text[cursor] === "'" ? cursor + 1 : cursor),
    values: values.filter((value) => value.toLowerCase().startsWith(match[2].replaceAll("''", "'").toLowerCase())),
  };
}
