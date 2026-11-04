<!-- CA-R-2727@5 -->
<!-- CA-D-674@9 -->
<!-- CA-M-470@1 -->
<script lang="ts">
  import { onMount } from 'svelte';
  import Button from './lib/Button.svelte';
  import Preferences from './lib/Preferences.svelte';
  import ResultsTable from './lib/ResultsTable.svelte';
  import SavedPanel from './lib/SavedPanel.svelte';
  import SqlEditor from './lib/SqlEditor.svelte';
  import WorksheetTabs from './lib/WorksheetTabs.svelte';
  import { ApiError, WorkbenchApi } from './lib/api';
  import type { CheckResult, QueryResult, SavedIdentity, SavedItem, Schema } from './lib/types';
  import { cleanAfterSave, newWorksheet, persistable, restore, storageKey } from './lib/workspace.js';

  type Tab = ReturnType<typeof newWorksheet> & {
    busy?: boolean; error?: string; result?: QueryResult; check?: CheckResult; saved?: SavedIdentity;
  };
  const base = location.pathname.replace(/\/+$/, '');
  const projectName = base.split('/').filter(Boolean).at(-1) ?? '';
  const projectRoot = new URLSearchParams(location.search).get('project_root');
  const namespace = storageKey(projectName);
  const initial = newWorksheet(1) as Tab;
  let tabs = $state<Tab[]>([initial]);
  let activeId = $state(initial.id);
  let schema = $state<Schema>({ tables: {} });
  let savedItems = $state<SavedItem[]>([]);
  let storageError = $state('');
  let collapsed = $state(false);
  let savedBusy = $state(false);
  let api: WorkbenchApi;
  let active = $derived(tabs.find((tab) => tab.id === activeId));

  function tabById(id: string) { return tabs.find((tab) => tab.id === id); }
  function updateTab(id: string, changes: Partial<Tab>) {
    tabs = tabs.map((tab) => tab.id === id ? { ...tab, ...changes } : tab);
  }
  function persist() {
    try { localStorage.setItem(namespace, persistable(tabs, activeId)); storageError = ''; }
    catch { storageError = 'Browser storage is unavailable; local Worksheet drafts are not saved.'; }
  }
  function edit(sql: string, cursor: number) {
    if (!active) return;
    updateTab(active.id, { sql, cursor, dirty: sql !== active.savedSql });
  }
  function addWorksheet() {
    const tab = newWorksheet(tabs.length + 1) as Tab;
    tabs = [...tabs, tab]; activeId = tab.id;
  }
  function closeWorksheet(id: string) {
    const tab = tabById(id);
    if (!tab || (tab.dirty && !confirm(`Close unsaved ${tab.title}?`))) return;
    const remaining = tabs.filter((item) => item.id !== id);
    if (remaining.length) { tabs = remaining; activeId = remaining[0].id; }
    else { const next = newWorksheet(1) as Tab; tabs = [next]; activeId = next.id; }
  }
  function acceptSaved(id: string, saved: SavedIdentity, result?: QueryResult, check?: CheckResult) {
    const current = tabById(id);
    if (!current) return;
    const clean = cleanAfterSave(current, saved.sql) as Tab;
    const changes: Partial<Tab> = { ...clean, saved, busy: false, error: '' };
    if (result) changes.result = result;
    if (check) changes.check = check;
    updateTab(id, changes);
  }
  function savedError(id: string, error: unknown) {
    const details = error instanceof ApiError ? error.details : {};
    updateTab(id, {
      busy: false, error: error instanceof Error ? error.message : 'Request failed',
      saved: typeof details.saved_query_id === 'string' ? details as unknown as SavedIdentity : undefined,
    });
  }
  async function action(kind: 'run' | 'check' | 'save', cursor = active?.cursor ?? 0) {
    const tab = active;
    if (!tab || tab.busy || savedBusy) return;
    updateTab(tab.id, { busy: true, error: '' });
    try {
      if (kind === 'run') { const result = await api.run(tab.sql, cursor); acceptSaved(tab.id, result, result); }
      else if (kind === 'check') { const check = await api.check(tab.sql, cursor); acceptSaved(tab.id, check, undefined, check); }
      else { const saved = await api.save(tab.sql, cursor); acceptSaved(tab.id, saved); }
      await refreshSaved();
    } catch (error) {
      savedError(tab.id, error);
      if (error instanceof ApiError && typeof error.details.saved_query_id === 'string') await refreshSaved();
    }
  }
  async function saveWorksheet() {
    const tab = active;
    if (!tab || tab.busy || savedBusy) return;
    updateTab(tab.id, { busy: true, error: '' });
    try { acceptSaved(tab.id, await api.saveWorksheet(tab.sql)); await refreshSaved(); }
    catch (error) { savedError(tab.id, error); }
  }
  async function page(offset: number) {
    const tab = active;
    if (!tab?.result || tab.busy) return;
    updateTab(tab.id, { busy: true, error: '' });
    try { updateTab(tab.id, { busy: false, result: await api.page(tab.result.query_id, offset, tab.result.page_size) }); }
    catch (error) { savedError(tab.id, error); }
  }
  async function refreshSaved() {
    try { savedItems = (await api.savedList()).items; }
    catch (error) { storageError = error instanceof Error ? error.message : 'Could not load saved SQL.'; }
  }
  async function openSaved(reference: string) {
    if (savedBusy) return;
    savedBusy = true;
    try {
      const saved = await api.load(reference);
      const existing = tabs.find((tab) => !tab.dirty && tab.sql === saved.sql);
      if (existing) { activeId = existing.id; updateTab(existing.id, { saved }); }
      else {
        const tab = { ...(newWorksheet(tabs.length + 1) as Tab), sql: saved.sql, cursor: 0, dirty: false, savedSql: saved.sql, saved };
        tabs = [...tabs, tab]; activeId = tab.id;
      }
    } catch (error) { storageError = error instanceof Error ? error.message : 'Could not load saved SQL.'; }
    finally { savedBusy = false; }
  }

  onMount(() => {
    api = new WorkbenchApi(base, projectRoot);
    try {
      const recovered = restore(localStorage.getItem(namespace) ?? '');
      if (recovered) { tabs = recovered.tabs as Tab[]; activeId = recovered.activeId; }
    } catch { storageError = 'Browser storage is unavailable; local Worksheet drafts cannot be restored.'; }
    void api.schema().then((value) => { schema = value; }).catch(() => {});
    void refreshSaved();
    const requested = new URLSearchParams(location.search).get('query');
    if (requested) void openSaved(requested);
    const unload = (event: BeforeUnloadEvent) => {
      persist();
      if (tabs.some((tab) => tab.dirty)) { event.preventDefault(); event.returnValue = ''; }
    };
    const hide = () => persist();
    window.addEventListener('beforeunload', unload);
    window.addEventListener('pagehide', hide);
    const timer = window.setInterval(persist, 5000);
    return () => { window.clearInterval(timer); window.removeEventListener('beforeunload', unload); window.removeEventListener('pagehide', hide); };
  });
</script>

<main class="workbench">
  <header class="app-header"><span class="brand-mark">CA</span><div class="brand-copy"><span class="project-label">{projectName}</span><h1 class="app-name">Workbench</h1></div><Preferences storageKey={namespace} /></header>
  <section class="workspace">
    <div class="workspace-toolbar"><div class="toolbar-main"><WorksheetTabs {tabs} {activeId} onselect={(id) => activeId = id} onclose={closeWorksheet} onadd={addWorksheet} /></div><div class="toolbar-actions"><Button onclick={() => collapsed = !collapsed}>{collapsed ? 'Show editor' : 'Hide editor'}</Button></div></div>
    {#if active}
      <section class="editor-panel"><div class="panel-heading"><h2>{active.title}</h2><Button class="editor-toggle" onclick={() => collapsed = !collapsed}>{collapsed ? 'Show editor' : 'Hide editor'}</Button></div>
        <div class="editor-content" hidden={collapsed}>{#key active.id}<SqlEditor value={active.sql} cursor={active.cursor} disabled={active.busy} {schema} onchange={edit} onaction={(kind, cursor) => action(kind, cursor)} />{/key}</div>
        <div class="query-actions"><Button type="button" disabled={active.busy || savedBusy} onclick={() => action('run')}>Run</Button><Button type="button" disabled={active.busy || savedBusy} onclick={() => action('check')}>Check</Button><Button type="button" disabled={active.busy || savedBusy} onclick={() => action('save')}>Save</Button><Button type="button" disabled={active.busy || savedBusy} onclick={saveWorksheet}>Save Worksheet</Button><span class="shortcut">Cmd+Enter Run · Shift+Cmd+Enter Check</span></div>
        {#if active.error}<p class="error" role="alert">{active.error}</p>{/if}
        {#if active.saved}<p class="notice">Saved: <a href={active.saved.saved_query_url}>{active.saved.saved_query_id}</a></p>{/if}
      </section>
      <section class="results-panel"><div class="panel-heading"><h2>Results</h2><p class="status-line"><span class="status-badge">{active.busy ? 'Working' : 'Ready'}</span></p></div>
        {#if active.check}<p class="notice">Query is valid: {active.check.row_count} rows, {active.check.column_count} columns.</p>{/if}
        {#if active.result}<ResultsTable result={active.result} /><nav class="query-actions" aria-label="Result pages"><Button disabled={active.busy || active.result.offset === 0} onclick={() => page(Math.max(0, active.result!.offset - active.result!.page_size))}>Previous</Button><Button disabled={active.busy || !active.result.has_more} onclick={() => page(active.result!.offset + active.result!.rows.length)}>Next</Button></nav>{/if}
      </section>
    {/if}
    {#if storageError}<p class="error" role="alert">{storageError}</p>{/if}
    <SavedPanel items={savedItems} busy={savedBusy} onopen={openSaved} />
  </section>
</main>
