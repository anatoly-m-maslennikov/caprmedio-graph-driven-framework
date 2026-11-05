// CA-E-683@1
import assert from 'node:assert/strict';
import test from 'node:test';
import { cleanAfterSave, newView, persistable, restore, storageKey, workspaceTabs } from './workspace.js';

test('a new empty view starts clean', () => {
  const tab = newView(1);
  assert.equal(tab.sql, tab.savedSql);
  assert.equal(tab.dirty, false);
  assert.equal(tab.name, undefined);
});

test('single-statement save does not mark a multi-statement view clean', () => {
  const tab = { id: 'a', title: 'Worksheet 1', sql: 'SELECT 1; SELECT 2', cursor: 0, dirty: true };
  assert.equal(cleanAfterSave(tab, 'SELECT 1').dirty, true);
  assert.equal(cleanAfterSave({ ...tab, sql: 'SELECT 1' }, 'SELECT 1').dirty, false);
});

test('persisted workspaces keep scripts but never result rows', () => {
  const raw = persistable([{ id: 'a', title: 'One', name: 'Daily report', sql: 'SELECT 1', cursor: 8, dirty: true, result: { rows: [[1]] } }], 'a');
  assert.deepEqual(restore(raw), { tabs: [{ id: 'a', title: 'One', name: 'Daily report', sql: 'SELECT 1', cursor: 8, dirty: true, savedSql: undefined }], activeId: 'a' });
});

test('historical generated tab names become Views without losing the draft', () => {
  const result = restore(JSON.stringify({ activeId: 'old', tabs: [{ id: 'old', title: 'Worksheet 2', sql: 'SELECT 42', cursor: 3, dirty: true, name: 'My report' }] }));
  assert.equal(result.tabs[0].title, 'View 2');
  assert.equal(result.tabs[0].name, 'My report');
  assert.equal(result.tabs[0].sql, 'SELECT 42');
  assert.equal(result.activeId, 'old');
});

test('bound drafts use their own Project and Workspace key', () => {
  assert.equal(storageKey('caprmedio'), 'caprmedio.workbench.caprmedio.workspace');
  assert.equal(storageKey('caprmedio', 'chat-a', '/projects/a'), 'caprmedio.workbench./projects/a.workspace.chat-a');
});

test('polling a result-free bound View does not dereference a missing local result', () => {
  const { tabs } = workspaceTabs({ active_view_id: 'a', views: [{ id: 'a', sql: '', cursor_position: 0, revision: 0 }] });
  assert.equal(tabs[0].id, 'a');
  assert.equal(tabs[0].result, undefined);
});

test('polling leaves an unsynced draft on its original revision', () => {
  const state = { active_view_id: 'a', views: [{ id: 'a', sql: 'SELECT remote', name: 'Remote', revision: 3 }] };
  const { tabs } = workspaceTabs(state, [{ id: 'a', title: 'View 1', sql: 'SELECT local', savedSql: 'SELECT old', dirty: true, revision: 2 }]);
  assert.equal(tabs[0].sql, 'SELECT local');
  assert.equal(tabs[0].revision, 2);
  assert.equal(tabs[0].serverSql, 'SELECT remote');
  assert.equal(tabs[0].serverRevision, 3);
});
