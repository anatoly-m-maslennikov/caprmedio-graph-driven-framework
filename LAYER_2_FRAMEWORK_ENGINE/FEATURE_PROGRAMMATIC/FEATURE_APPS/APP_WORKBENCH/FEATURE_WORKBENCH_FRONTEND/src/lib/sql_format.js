// CA-R-2727@16
// CA-M-468@4
// CA-D-674@21
import { sql } from '@codemirror/lang-sql';
import { duckdb, formatDialect } from '@dlh.io/dlh-sql-formatter';

/** @type {import('@dlh.io/dlh-sql-formatter').FormatOptionsWithDialect} */
const options = {
  dialect: duckdb,
  keywordCase: 'lower',
  commaPosition: 'leading',
  tabWidth: 2,
  logicalOperatorNewline: 'before',
  newlineBeforeSemicolon: true,
};

/** @param {string} source */
function leaves(source) {
  const cursor = sql().language.parser.parse(source).cursor();
  const tokens = [];
  for (;;) {
    if (cursor.firstChild()) continue;
    tokens.push({ name: cursor.name, from: cursor.from, to: cursor.to });
    while (!cursor.nextSibling()) if (!cursor.parent()) return tokens;
  }
}

/** @param {string} source */
function adapter(source) {
  const replacements = [];
  const tokens = leaves(source);
  for (let index = 0; index < tokens.length; index += 1) {
    const token = tokens[index];
    const text = source.slice(token.from, token.to);
    if (token.name === 'Keyword' && text === 'select') replacements.push({ from: token.from, to: token.to, text: 'SELECT' });
    if (token.name !== 'Keyword' || !['from', 'where'].includes(text)) continue;
    const next = tokens[index + 1];
    if (!next || /Comment$/.test(next.name)) continue;
    const whitespace = source.slice(token.to, next.from);
    if (/\n/.test(whitespace) && /^\s*$/.test(whitespace)) replacements.push({ from: token.to, to: next.from, text: ' ' });
  }
  return replacements.reverse().reduce((formatted, replacement) => `${formatted.slice(0, replacement.from)}${replacement.text}${formatted.slice(replacement.to)}`, source);
}

/** @param {string} source */
export function formatSql(source) {
  return adapter(formatDialect(source, options));
}
