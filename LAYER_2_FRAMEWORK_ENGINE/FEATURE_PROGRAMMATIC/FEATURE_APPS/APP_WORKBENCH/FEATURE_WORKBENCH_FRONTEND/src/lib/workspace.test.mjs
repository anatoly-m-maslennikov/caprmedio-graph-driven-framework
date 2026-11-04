import assert from 'node:assert/strict';
import test from 'node:test';
import { cleanAfterSave, persistable, restore } from './workspace.js';

test('single-statement save does not mark a multi-statement worksheet clean', () => {
  const tab = { id: 'a', title: 'Worksheet 1', sql: 'SELECT 1; SELECT 2', cursor: 0, dirty: true };
  assert.equal(cleanAfterSave(tab, 'SELECT 1').dirty, true);
  assert.equal(cleanAfterSave({ ...tab, sql: 'SELECT 1' }, 'SELECT 1').dirty, false);
});

test('persisted workspaces keep scripts but never result rows', () => {
  const raw = persistable([{ id: 'a', title: 'One', sql: 'SELECT 1', cursor: 8, dirty: true, result: { rows: [[1]] } }], 'a');
  assert.deepEqual(restore(raw), { tabs: [{ id: 'a', title: 'One', sql: 'SELECT 1', cursor: 8, dirty: true, savedSql: undefined }], activeId: 'a' });
});
