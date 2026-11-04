// @ts-nocheck
// CA-M-468@2
export function statusCompletion(text, cursor, schema) {
  const match = /\bstatus\s*=\s*'([^']*)$/.exec(text.slice(0, cursor));
  if (!match) return null;
  const values = schema.tables.atoms?.find((column) => column.name === 'status')?.values ?? [];
  return {
    from: cursor - match[1].length,
    to: text[cursor] === "'" ? cursor + 1 : cursor,
    values: values.filter((value) => value.toLowerCase().startsWith(match[1].toLowerCase())),
  };
}
