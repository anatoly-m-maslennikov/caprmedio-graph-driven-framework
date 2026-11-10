// CA-E-683@9
import assert from 'node:assert/strict';
import test from 'node:test';

import { statusCompletion } from './editor_helpers.js';

test('completes values from actual dotted Header Status columns', () => {
  const schema = { tables: { atoms: [
    { name: 'header.status', values: ['Active', 'Done'] },
    { name: 'header.state.status', values: ['Active', 'Done'] },
  ] } };
  const flat = `SELECT * FROM atoms WHERE "header.status" = 'Do`;
  const dotted = `SELECT * FROM atoms WHERE "header.state.status" = 'Act`;
  assert.deepEqual(statusCompletion(flat, flat.length, schema)?.values, ['Done']);
  assert.deepEqual(statusCompletion(dotted, dotted.length, schema)?.values, ['Active']);
  const unavailable = `SELECT * FROM atoms WHERE "header.state.status" = 'Arc`;
  assert.deepEqual(statusCompletion(unavailable, unavailable.length, schema)?.values, []);
  const unknown = `SELECT * FROM atoms WHERE "header.unknown.status" = 'Act`;
  assert.equal(statusCompletion(unknown, unknown.length, schema), null);
  assert.equal(statusCompletion("SELECT * FROM atoms WHERE header_status = 'Act", 47, schema), null);
});

test('matches SQL-escaped status prefixes without changing their source value', () => {
  const schema = { tables: { atoms: [{ name: 'header.state.status', values: ["O'Reilly", 'Open'] }] } };
  const text = `SELECT * FROM atoms WHERE "header.state.status" = 'O''R`;
  assert.deepEqual(statusCompletion(text, text.length, schema)?.values, ["O'Reilly"]);
});

test('replaces the complete Status literal when the SQL token extends beyond the cursor', () => {
  const schema = { tables: { atoms: [{ name: 'header.state.status', values: ['Active'] }] } };
  const text = `SELECT * FROM atoms WHERE "header.state.status" = 'Active'`;
  const cursor = text.indexOf('Active') + 3;
  assert.equal(statusCompletion(text, cursor, schema, text.length)?.to, text.length);
});
