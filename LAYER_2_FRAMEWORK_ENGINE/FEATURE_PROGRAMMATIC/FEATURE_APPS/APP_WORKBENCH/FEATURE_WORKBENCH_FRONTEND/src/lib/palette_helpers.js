// @ts-nocheck
// CA-D-674@26
export function filterCommands(commands, query) { return commands.filter((command) => command.label.toLowerCase().includes(query.toLowerCase())); }
export function moveSelection(index, count, direction) { return Math.max(0, Math.min(index + direction, Math.max(0, count - 1))); }
