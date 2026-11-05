// CA-R-2791@1
// CA-D-680@1

/** @typedef {{id: string, role: string, text: string}} ChatEntry */
/** @typedef {{id: string | number, method: string, params: Record<string, any>}} NativeRequest */

/** @param {unknown} value @returns {value is Record<string, any>} */
export function record(value) { return value !== null && typeof value === 'object' && !Array.isArray(value); }

/** @param {unknown} value @returns {string} */
function contentText(value) {
  if (typeof value === 'string') return value;
  if (!Array.isArray(value)) return '';
  return value.map((part) => record(part) && typeof part.text === 'string' ? part.text : '').filter(Boolean).join('\n');
}

/** @param {unknown} thread @returns {ChatEntry[]} */
export function historyEntries(thread) {
  if (!record(thread) || !Array.isArray(thread.turns)) return [];
  return thread.turns.flatMap((turn) => (Array.isArray(turn.items) ? turn.items : []).flatMap(
    /** @param {Record<string, any>} item */ (item) => {
      if (item.type !== 'userMessage' && item.type !== 'agentMessage') return [];
      const text = contentText(item.type === 'userMessage' ? item.content : item.text);
      return text ? [{ id: String(item.id), role: item.type === 'userMessage' ? 'You' : 'Codex', text }] : [];
    },
  ));
}

/** @param {unknown} packet @returns {NativeRequest | null} */
export function interaction(packet) {
  return record(packet) && (typeof packet.id === 'string' || typeof packet.id === 'number') && typeof packet.method === 'string'
    ? { id: packet.id, method: packet.method, params: record(packet.params) ? packet.params : {} } : null;
}

/** @param {ChatEntry[]} entries @param {unknown} packet @returns {ChatEntry[]} */
export function applyNativeEvent(entries, packet) {
  if (!record(packet) || !record(packet.params)) return entries;
  const params = packet.params;
  let id = ''; let text = ''; let role = 'Codex'; let append = false;
  if (packet.method === 'item/agentMessage/delta' && typeof params.delta === 'string') {
    id = params.itemId; text = params.delta; append = true;
  } else if (packet.method === 'item/completed' && params.item?.type === 'agentMessage') {
    id = params.item.id; text = contentText(params.item.text);
  } else if (['item/started', 'item/completed'].includes(packet.method) && params.item?.type === 'mcpToolCall') {
    const item = params.item; id = `tool-${item.id}`; role = 'Activity';
    text = `${item.server || 'MCP'} · ${item.tool || 'Tool'} — ${item.status || (packet.method === 'item/completed' ? 'completed' : 'working')}`;
  }
  if (typeof id !== 'string' || !id || !text) return entries;
  const previous = entries.find((entry) => entry.id === id);
  const next = { id, role, text: append && previous ? previous.text + text : text };
  return previous ? entries.map((entry) => entry.id === id ? next : entry) : [...entries, next];
}

/** @param {string} buffer @returns {{events: Record<string, any>[], rest: string}} */
export function sseFrames(buffer) {
  const frames = buffer.replace(/\r\n/g, '\n').split('\n\n');
  const rest = frames.pop() || '';
  return { rest, events: frames.flatMap((frame) => {
    const data = frame.split('\n').filter((line) => line.startsWith('data:')).map((line) => line.slice(5).trimStart()).join('\n');
    if (!data) return [];
    const value = JSON.parse(data);
    if (!record(value)) throw new Error('Invalid Codex event');
    return [value];
  }) };
}

/** @param {Array<{id: string}>} questions @param {Record<string, string>} answers */
export function inputAnswers(questions, answers) {
  return { answers: Object.fromEntries(questions.map((question) => [question.id, { answers: [answers[question.id] || ''] }])) };
}
