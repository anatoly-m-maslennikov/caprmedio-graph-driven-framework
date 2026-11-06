import assert from 'node:assert/strict';
import test from 'node:test';

import { statusCompletion } from './editor_helpers.js';

test('completes values from either observed Header Status column', () => {
  const schema = { tables: { atoms: [
    { name: 'header_status', values: ['Active', 'Done'] },
    { name: 'header_state_status', values: ['Canceled'] },
  ] } };
  const flat = "SELECT * FROM atoms WHERE header_status = 'Act";
  const nested = "SELECT * FROM atoms WHERE header_state_status = 'Can";
  assert.deepEqual(statusCompletion(flat, flat.length, schema)?.values, ['Active']);
  assert.deepEqual(statusCompletion(nested, nested.length, schema)?.values, ['Canceled']);
  assert.equal(statusCompletion("SELECT * FROM atoms WHERE status = 'Act", 39, schema), null);
});
