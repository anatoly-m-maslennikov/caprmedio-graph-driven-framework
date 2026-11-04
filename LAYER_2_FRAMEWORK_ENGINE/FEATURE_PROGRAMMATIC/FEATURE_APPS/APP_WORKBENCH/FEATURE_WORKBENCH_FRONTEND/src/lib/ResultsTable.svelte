<!-- CA-R-2727@4 CA-M-466@4 CA-M-467@2 CA-D-674@7 -->
<script lang="ts">
  import type { QueryResult } from './types';

  let { result }: { result: QueryResult } = $props();

  function display(value: unknown): string {
    if (value === null) return 'NULL';
    return typeof value === 'object' ? JSON.stringify(value) : String(value);
  }
</script>

<div class="result-summary" aria-live="polite">
  {result.row_count} rows, {result.column_count} columns; showing
  {result.rows.length === 0 ? 'no rows' : `${result.offset + 1}-${result.offset + result.rows.length}`}
</div>
<div class="table-scroll">
  <table>
    <thead><tr>{#each result.columns as column}<th scope="col">{column.name}<small>{column.type}</small></th>{/each}</tr></thead>
    <tbody>{#each result.rows as row}<tr>{#each row as value}<td><div class="cell-value">{display(value)}</div></td>{/each}</tr>{/each}</tbody>
  </table>
</div>
