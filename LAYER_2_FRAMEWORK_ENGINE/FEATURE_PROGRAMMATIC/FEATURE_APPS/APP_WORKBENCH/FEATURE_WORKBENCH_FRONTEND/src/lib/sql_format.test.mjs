import assert from 'node:assert/strict';
import test from 'node:test';
import { formatSql } from './sql_format.js';

test('formats a DuckDB query in the Workbench layout', () => {
  assert.equal(formatSql("select a,b from atoms where x=1 and y='select';"), "SELECT\n  a\n  ,b\nfrom atoms\nwhere x = 1\n  and y = 'select'\n;");
});

test('is idempotent and preserves nested SQL tokens', () => {
  const source = "with source as (select \"FROM\", 'SELECT' as value from atoms where kind = 'claim') select value, (select count(*) from source where value = 'SELECT') as total from source where value is not null -- SELECT remains a comment\n;";
  const formatted = formatSql(source);
  assert.equal(formatSql(formatted), formatted);
  assert.match(formatted, /\"FROM\"/);
  assert.match(formatted, /'SELECT'/);
  assert.match(formatted, /-- SELECT remains a comment/);
  assert.match(formatted, /SELECT/);
  assert.match(formatted, /from source/);
  assert.match(formatted, /where value/);
});

test('surfaces formatter parse failures without replacing the source', () => {
  const invalid = 'select [';
  assert.throws(() => formatSql(invalid));
});
