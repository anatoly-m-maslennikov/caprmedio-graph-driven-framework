<!-- CA-R-2727@4 CA-M-466@5 CA-M-467@2 CA-D-674@8 -->
<script lang="ts">
  import Button from './lib/Button.svelte';
  import ResultsTable from './lib/ResultsTable.svelte';
  import SqlEditor from './lib/SqlEditor.svelte';
  import type { CheckResult, QueryResult } from './lib/types';

  const base = location.pathname.replace(/\/+$/, '');
  const projectRoot = new URLSearchParams(location.search).get('project_root');
  let sql = 'SELECT id, role, status FROM atoms LIMIT 20';
  let result: QueryResult | null = null;
  let check: CheckResult | null = null;
  let error = '';
  let loading = false;

  async function request<T>(path: string, body: object): Promise<T> {
    const response = await fetch(`${base}/${path}`, {
      method: 'POST', headers: { 'content-type': 'application/json' },
      body: JSON.stringify(projectRoot ? { ...body, project_root: projectRoot } : body)
    });
    const value = await response.json() as T | { error?: string };
    if (!response.ok) throw new Error('error' in value ? value.error || 'Query failed' : 'Query failed');
    return value as T;
  }

  async function run() {
    loading = true; error = ''; check = null;
    try { result = await request<QueryResult>('run', { sql, page_size: 100 }); }
    catch (cause) { result = null; error = cause instanceof Error ? cause.message : 'Query failed'; }
    finally { loading = false; }
  }

  async function validate() {
    loading = true; error = ''; result = null;
    try { check = await request<CheckResult>('check', { sql }); }
    catch (cause) { check = null; error = cause instanceof Error ? cause.message : 'Query failed'; }
    finally { loading = false; }
  }

  async function page(offset: number) {
    if (!result) return;
    loading = true; error = '';
    try { result = await request<QueryResult>('page', { query_id: result.query_id, offset, page_size: result.page_size }); }
    catch (cause) { error = cause instanceof Error ? cause.message : 'Query failed'; }
    finally { loading = false; }
  }
</script>

<main>
  <h1>Workbench</h1>
  <form onsubmit={(event) => { event.preventDefault(); run(); }}>
    <SqlEditor bind:value={sql} disabled={loading} />
    <div class="actions"><Button type="submit" disabled={loading}>Run</Button><Button type="button" disabled={loading} onclick={validate}>Check</Button></div>
  </form>
  {#if loading}<p aria-live="polite">Loading query result…</p>{/if}
  {#if error}<p class="error" role="alert">{error}</p>{/if}
  {#if check}<p class="result-summary" aria-live="polite">Query is valid: {check.row_count} rows, {check.column_count} columns.</p>{/if}
  {#if result}
    <ResultsTable {result} />
    <nav aria-label="Result pages" class="actions">
      <Button disabled={loading || result.offset === 0} onclick={() => page(Math.max(0, result.offset - result.page_size))}>Previous</Button>
      <Button disabled={loading || !result.has_more} onclick={() => page(result.offset + result.rows.length)}>Next</Button>
    </nav>
  {/if}
</main>
