<!-- CA-D-674@11 -->
<script lang="ts">
  import type { QueryResult } from './types';

  let { result }: { result: QueryResult } = $props();

  const visibleColumns = $derived(
    result.columns.flatMap((column, index) => column.has_values === false ? [] : [{ column, index }])
  );
  const hiddenColumnCount = $derived(result.columns.length - visibleColumns.length);

  function display(value: unknown): string {
    if (value === null) return 'NULL';
    return typeof value === 'object' ? JSON.stringify(value) : String(value);
  }
</script>

<div class="result-summary" aria-live="polite">
  {result.row_count} rows, {hiddenColumnCount > 0 ? `${visibleColumns.length} of ${result.column_count}` : result.column_count} columns; showing
  {result.rows.length === 0 ? 'no rows' : `${result.offset + 1}-${result.offset + result.rows.length}`}
</div>
<div class="table-scroll">
  <table>
    <thead><tr>{#each visibleColumns as { column }}<th scope="col">{column.name}<small>{column.type}</small></th>{/each}</tr></thead>
    <tbody>{#each result.rows as row}<tr>{#each visibleColumns as { index }}<td><div class="cell-value">{display(row[index])}</div></td>{/each}</tr>{/each}</tbody>
  </table>
</div>
