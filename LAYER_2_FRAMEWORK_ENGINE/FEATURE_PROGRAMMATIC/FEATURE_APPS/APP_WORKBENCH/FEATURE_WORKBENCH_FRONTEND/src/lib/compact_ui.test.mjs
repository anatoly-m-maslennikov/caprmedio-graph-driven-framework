import assert from 'node:assert/strict';
import test from 'node:test';
import { statusCompletion } from './editor_helpers.js';
import { filterCommands, moveSelection } from './palette_helpers.js';
import { persistable, restore } from './workspace.js';

test('named worksheets persist with their complete scripts', () => {
  const recovered = restore(persistable([{ id: 'one', title: 'Weekly check', sql: 'SELECT 1', cursor: 8, dirty: true }], 'one'));
  assert.equal(recovered.tabs[0].title, 'Weekly check');
  assert.equal(recovered.tabs[0].sql, 'SELECT 1');
});
test('status completion is local and closes the quote once', () => {
  const sql = "SELECT * FROM atoms WHERE status = 'Act'";
  const completion = statusCompletion(sql, sql.length - 1, { tables: { atoms: [{ name: 'status', type: 'VARCHAR', values: ['Active', 'Archived'] }] } });
  assert.deepEqual(completion.values, ['Active']);
  assert.equal(completion.to, sql.length);
});
test('palette filters and clamps keyboard navigation', () => {
  assert.deepEqual(filterCommands([{ label: 'Run' }, { label: 'Open Saved' }], 'saved').map((item) => item.label), ['Open Saved']);
  assert.equal(moveSelection(0, 2, -1), 0); assert.equal(moveSelection(1, 2, 1), 1);
});
