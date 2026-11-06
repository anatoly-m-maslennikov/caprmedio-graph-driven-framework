// @ts-nocheck
// CA-R-2726@5
// CA-E-675@6
// CA-M-468@2
export function statusCompletion(text, cursor, schema) {
  const match = /\b(header_(?:state_)?status)\s*=\s*'([^']*)$/.exec(text.slice(0, cursor));
  if (!match) return null;
  const values = schema.tables.atoms?.find((column) => column.name === match[1])?.values ?? [];
  return {
    from: cursor - match[2].length,
    to: text[cursor] === "'" ? cursor + 1 : cursor,
    values: values.filter((value) => value.toLowerCase().startsWith(match[2].toLowerCase())),
  };
}
