<!-- CA-D-674@23 -->
<!-- CA-M-492@3 -->
<script lang="ts">
  import { onMount } from 'svelte';
  import { TabulatorFull as Tabulator } from 'tabulator-tables';
  import 'tabulator-tables/dist/css/tabulator.min.css';
  import type { GridState, QueryResult, ResultDisplayPreferences } from './types';

  let { result, display, grid, layoutVersion = 0, ondisplaychange, ongridchange, oncapacity }: {
    result: QueryResult; display: ResultDisplayPreferences; grid: GridState; layoutVersion?: number;
    ondisplaychange: (next: ResultDisplayPreferences) => void; ongridchange: (next: GridState) => void;
    oncapacity: (size: number, geometry: string) => void;
  } = $props();
  let host: HTMLDivElement; let table: any; let tableReady = false; let mounted = false; let disposed = false; let builtKey = '';
  const visibleColumns = $derived(result.columns.flatMap((column, index) => column.has_values === false ? [] : [{ column, index }]));
  const hiddenColumnCount = $derived(result.columns.length - visibleColumns.length);
  const totalRows = $derived(result.filtered_row_count ?? result.row_count);
  const positive = (value: string) => Number.isInteger(Number(value)) && Number(value) > 0;
  const escape = (value: string) => value.replace(/[&<>"']/g, (char) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[char]!);
  const groupKey = (value: unknown) => JSON.stringify(value) ?? '__undefined__';
  function valueText(value: unknown) { if (value === null) return 'NULL'; try { return typeof value === 'object' ? JSON.stringify(value) : String(value); } catch { return String(value); } }
  function displayText(value: unknown) { const text = valueText(value); if (display.content === 'full') return text; const chars = Array.from(text); return chars.length > display.contentLimit ? `${chars.slice(0, display.contentLimit).join('')}…` : text; }
  function updateDisplay(next: Partial<ResultDisplayPreferences>) { ondisplaychange({ ...display, ...next }); }
  function inputLimit(value: string) { if (positive(value)) updateDisplay({ contentLimit: Number(value) }); }
  function records() { return result.rows.map((row, rowIndex) => Object.fromEntries(result.columns.map((_column, index) => [`c${index}`, row[index]]).concat([['__row', rowIndex]]))); }
  function setSort(index: number, direction: 'asc' | 'desc') { ongridchange({ ...grid, sort: [...grid.sort.filter((item) => item.column !== index), { column: index, direction }] }); }
  function setFilter(index: number) { const value = window.prompt(`Filter ${result.columns[index].name}`, grid.filters.find((item) => item.column === index)?.value ?? ''); if (value === null) return; const filters = grid.filters.filter((item) => item.column !== index); if (value) filters.push({ column: index, operator: 'contains', value }); ongridchange({ ...grid, filters }); }
  function copy(text: string) { void navigator.clipboard?.writeText(text).catch(() => {}); }
  function cellMenu() { return [
    { label: 'Cell Copy value', action: (_event: Event, cell: any) => copy(valueText(cell.getValue())) },
    { label: 'Cell Show full value', action: (_event: Event, cell: any) => window.alert(valueText(cell.getValue())) },
    { label: 'Row Copy row', action: (_event: Event, cell: any) => copy(JSON.stringify(result.rows[cell.getRow().getData().__row])) },
  ]; }
  function rowMenu() { return [
    { label: 'Row Copy row', action: (_event: Event, row: any) => copy(JSON.stringify(result.rows[row.getData().__row])) },
  ]; }
  function headerMenu(index: number) { return [
    { label: 'Column Sort ascending', action: () => setSort(index, 'asc') }, { label: 'Column Sort descending', action: () => setSort(index, 'desc') },
    { label: 'Group by', action: () => ongridchange({ ...grid, group_by: { column: index, direction: 'asc' } }) },
    { label: 'Filter', action: () => setFilter(index) }, { label: 'Clear filter', action: () => ongridchange({ ...grid, filters: grid.filters.filter((item) => item.column !== index) }) },
  ]; }
  function gridKey() { return `${result.query_id}:${visibleColumns.map(({ index }) => index).join(',')}:${JSON.stringify(grid)}:${JSON.stringify(result.groups ?? [])}`; }
  function fitHeight() {
    const pager = host.closest('.results-panel')?.querySelector<HTMLElement>('[aria-label="Result pages"]');
    const scale = Number(getComputedStyle(document.documentElement).getPropertyValue('--interface-scale')) || 1;
    const remaining = (window.innerHeight - host.getBoundingClientRect().top - (pager?.getBoundingClientRect().height ?? 0) - 40) / scale;
    const height = `${Math.max(120, Math.floor(remaining))}px`;
    if (host.style.height === height) return;
    host.style.height = height;
    if (tableReady && table) table.setHeight(height);
  }
  function build() {
    const previous = table; const previousReady = tableReady;
    tableReady = false; table = undefined;
    if (previousReady) previous?.destroy();
    fitHeight();
    const group = grid.group_by;
    const counts = new Map((result.groups ?? []).map((item) => [groupKey(item.value), item.count]));
    const groupValues = new Map((result.groups ?? []).map((item) => [groupKey(item.value), item.value]));
    const originalGroupValue = (key: unknown) => groupValues.has(String(key)) ? groupValues.get(String(key)) : String(key);
    const candidate = new Tabulator(host, {
      data: records(), layout: 'fitDataStretch', height: host.style.height, index: '__row', columnDefaults: { headerSort: false }, popupContainer: '.workbench', rowContextMenu: rowMenu(),
      groupBy: group ? (row: Record<string, unknown>) => groupKey(row[`c${group.column}`]) : false,
      groupHeader: (key: unknown) => `${escape(result.columns[group?.column ?? 0]?.name ?? '')}: ${escape(valueText(originalGroupValue(key)))} (${counts.get(String(key)) ?? '—'})`,
      columns: visibleColumns.map(({ column, index }) => ({ field: `c${index}`, title: `<span class="column-name">${escape(column.name)}</span><small class="column-type">${escape(column.type)}</small>`, formatter: (cell: any) => `<div class="cell-value">${escape(displayText(cell.getValue()))}</div>`, contextMenu: cellMenu(), headerContextMenu: headerMenu(index) })),
    });
    table = candidate; builtKey = gridKey();
    candidate.on('tableBuilt', () => {
      if (disposed || table !== candidate) { candidate.destroy(); return; }
      tableReady = true; refresh();
    });
  }
  function measure(rect?: DOMRectReadOnly) {
    if (display.rowSizing !== 'adaptive' || !table) return;
    const holder = host.querySelector<HTMLElement>('.tabulator-tableholder'); const row = holder?.querySelector<HTMLElement>('.tabulator-row');
    const height = holder?.getBoundingClientRect().height ?? host.getBoundingClientRect().height; const rowHeight = row?.getBoundingClientRect().height ?? 28;
    if (height && rowHeight) oncapacity(Math.max(1, Math.min(1000, Math.floor(height / rowHeight))), `${Math.round(rect?.width ?? host.clientWidth)}x${Math.round(rect?.height ?? host.clientHeight)}`);
  }
  function scheduleMeasure(rect?: DOMRectReadOnly) {
    const candidate = table;
    requestAnimationFrame(() => { if (!disposed && table === candidate && tableReady) measure(rect); });
  }
  function refresh() {
    if (disposed) return;
    fitHeight(); const key = gridKey();
    if (!table) build();
    else if (tableReady && key !== builtKey) build();
    else if (tableReady) void table.replaceData(records());
    scheduleMeasure();
  }
  onMount(() => {
    mounted = true; refresh();
    const resize = () => { fitHeight(); if (tableReady) measure(); };
    const observer = new ResizeObserver((entries) => { fitHeight(); scheduleMeasure(entries[0]?.contentRect); });
    observer.observe(host); window.addEventListener('resize', resize);
    return () => {
      const candidate = table; const ready = tableReady;
      disposed = true; tableReady = false; observer.disconnect(); window.removeEventListener('resize', resize); table = undefined;
      if (ready) candidate?.destroy();
    };
  });
  $effect(() => { result; display; grid; layoutVersion; if (mounted) refresh(); });
</script>

<div class="result-summary result-header" aria-live="polite"><span>{totalRows} rows, {hiddenColumnCount > 0 ? `${visibleColumns.length} of ${result.column_count}` : result.column_count} columns; showing {result.rows.length === 0 ? 'no rows' : `${result.offset + 1}-${result.offset + result.rows.length}`}</span><label>Cell content <select aria-label="Result cell content" value={display.content} onchange={(event) => updateDisplay({ content: (event.currentTarget as HTMLSelectElement).value as 'limited' | 'full' })}><option value="limited">Limited</option><option value="full">Full</option></select></label>{#if display.content === 'limited'}<label>Limit <input aria-label="Inline content character limit" type="number" min="1" step="1" value={display.contentLimit} oninput={(event) => inputLimit(event.currentTarget.value)} /></label>{/if}</div>
<div class="result-grid" bind:this={host} aria-label="Query results grid"></div>
