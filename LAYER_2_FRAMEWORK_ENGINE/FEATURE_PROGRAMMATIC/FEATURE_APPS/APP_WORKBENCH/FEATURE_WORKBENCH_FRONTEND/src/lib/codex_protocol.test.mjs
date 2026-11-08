import assert from 'node:assert/strict';
import test from 'node:test';
import { applyNativeEvent, historyEntries, interaction, inputAnswers, sseFrames } from './codex_protocol.js';

test('native deltas accumulate once and completed items replace the final text', () => {
  const delta = (text) => ({ method: 'item/agentMessage/delta', params: { itemId: 'a', delta: text } });
  let entries = applyNativeEvent([], delta('Hello'));
  entries = applyNativeEvent(entries, delta(' world'));
  entries = applyNativeEvent(entries, { method: 'item/completed', params: { item: { type: 'agentMessage', id: 'a', text: 'Hello world!' } } });
  assert.deepEqual(entries, [{ id: 'a', role: 'Codex', text: 'Hello world!' }]);
});

test('native history restores readable user and assistant messages', () => {
  assert.deepEqual(historyEntries({ turns: [{ items: [
    { id: 'u', type: 'userMessage', content: [{ type: 'text', text: 'SELECT 1' }] },
    { id: 'a', type: 'agentMessage', text: 'One row.' },
  ] }] }), [{ id: 'u', role: 'You', text: 'SELECT 1' }, { id: 'a', role: 'Codex', text: 'One row.' }]);
});

test('interaction IDs retain their native types and answers stay separate', () => {
  assert.equal(interaction({ id: 7, method: 'item/tool/requestUserInput', params: {} }).id, 7);
  assert.equal(interaction({ method: 'turn/completed', params: {} }), null);
  assert.deepEqual(inputAnswers([{ id: 'one' }, { id: 'two' }], { one: 'yes', two: 'no' }), {
    answers: { one: { answers: ['yes'] }, two: { answers: ['no'] } },
  });
});

test('SSE chunk boundaries and CRLF preserve native packets', () => {
  const first = sseFrames('data: {"type":"started","turn_id":"t"}\r\n\r\ndata: {"type":"fin');
  assert.equal(first.events[0].turn_id, 't');
  const last = sseFrames(first.rest + 'ished","status":"completed"}\n\n');
  assert.equal(last.events[0].status, 'completed');
  assert.equal(last.rest, '');
  assert.throws(() => sseFrames('data: invalid\n\n'));
});
