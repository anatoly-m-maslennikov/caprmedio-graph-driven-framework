<!-- CA-R-2727@12 -->
<!-- CA-R-2776@5 -->
<!-- CA-R-2902@1 -->
<!-- CA-M-470@6 -->
<!-- CA-D-674@16 -->
<!-- CA-D-681@1 -->
<script lang="ts">
  import { onMount } from 'svelte';
  import Button from './lib/Button.svelte';
  import CommandPalette, { type Command } from './lib/CommandPalette.svelte';
  import NameDialog from './lib/NameDialog.svelte';
  import OpenSavedDialog from './lib/OpenSavedDialog.svelte';
  import Preferences, { type PreferenceCommand } from './lib/Preferences.svelte';
  import ResultsTable from './lib/ResultsTable.svelte';
  import SavedPanel from './lib/SavedPanel.svelte';
  import SqlEditor from './lib/SqlEditor.svelte';
  import ViewTabs from './lib/ViewTabs.svelte';
  import { WorkbenchApi, WorkspaceApi } from './lib/api';
  import type { CheckResult, QueryLogItem, QueryResult, SavedIdentity, SavedItem, Schema, ViewResult, WorkspaceState, WorkspaceView } from './lib/types';
  import { cleanAfterSave, newView, persistable, restore, storageKey, workspaceTabs } from './lib/workspace.js';

  type Tab = ReturnType<typeof newView> & { busy?: boolean; error?: string; result?: QueryResult; check?: CheckResult; saved?: SavedIdentity; revision?: number; run?: ViewResult; conflict?: boolean; serverSql?: string; serverRevision?: number };
  const base = location.pathname.replace(/\/+$/, '');
  const projectName = base.split('/').filter(Boolean).at(-1) ?? '';
  const parameters = new URLSearchParams(location.search);
  const projectRoot = parameters.get('project_root');
  const workspaceId = parameters.get('workspace');
  const namespace = storageKey(projectName, workspaceId ?? undefined, projectRoot ?? undefined);
  const initial = newView(1) as Tab;
  let tabs = $state<Tab[]>([initial]); let activeId = $state(initial.id); let view = $state<'settings' | 'saved' | 'view'>('view');
  let schema = $state<Schema>({ tables: {} }); let savedItems = $state<SavedItem[]>([]); let logItems = $state<QueryLogItem[]>([]); let storageError = $state(''); let collapsed = $state(false);
  let savedBusy = $state(false); let openSavedDialog = $state(false); let commandOpen = $state(false); let nameDialog = $state(false); let renaming = $state('');
  let preferenceCommands = $state<PreferenceCommand[]>([]); let api: WorkbenchApi; let boundApi: WorkspaceApi | undefined; const syncing = new Map<string, Promise<boolean>>();
  let active = $derived(tabs.find((tab) => tab.id === activeId)); let commands = $derived(buildCommands());

  const message = (error: unknown) => error instanceof Error ? error.message : 'Request failed';
  function tabById(id: string) { return tabs.find((tab) => tab.id === id); }
  function tabName(tab: Tab) { return tab.name || tab.title; }
  function updateTab(id: string, changes: Partial<Tab>) { tabs = tabs.map((tab) => tab.id === id ? { ...tab, ...changes } : tab); }
  function persist() { try { localStorage.setItem(namespace, persistable(tabs, activeId)); storageError = ''; } catch { storageError = 'Browser storage is unavailable; local View drafts are not saved.'; } }
  function fail(id: string, error: unknown, conflict = false) { updateTab(id, { busy: false, error: message(error), ...(conflict ? { conflict: true } : {}) }); }
  function edit(sql: string, cursor: number) { if (active) updateTab(active.id, { sql, cursor, dirty: sql !== active.savedSql, conflict: false, error: '' }); }
  function showView(id: string) {
    activeId = id; view = 'view';
    if (boundApi) void boundApi.focus(id).then(({ active_view_id }) => activeId = active_view_id).catch((error) => fail(id, error));
  }
  function showUtility(next: 'settings' | 'saved') { view = next; if (next === 'saved') void refreshSaved(); }
  function applyServerView(server: WorkspaceView, clean = false) {
    const current = tabById(server.id); if (!current) return;
    if (!clean && current.dirty && server.sql !== current.savedSql) {
      updateTab(server.id, { ...(server.name === undefined ? { name: undefined } : { name: server.name }), run: server.result, serverSql: server.sql, serverRevision: server.revision });
      return;
    }
    updateTab(server.id, {
      ...(server.name === undefined ? { name: undefined } : { name: server.name }), revision: server.revision, run: server.result,
      ...(clean ? { sql: server.sql, savedSql: server.sql, cursor: server.cursor_position, dirty: false, conflict: false, result: undefined, check: undefined, serverSql: undefined, serverRevision: undefined } : {}),
    });
  }
  function fetchRemoteResult(id: string) {
    const tab = tabById(id); const queryId = tab?.run?.query_id;
    if (!boundApi || !tab || !queryId || tab.result?.query_id === queryId) return;
    void boundApi.fetch(id).then((result) => { if (tabById(id)?.run?.query_id === queryId) updateTab(id, { result, error: '' }); }).catch((error) => fail(id, error));
  }
  function applyState(state: WorkspaceState) {
    const merged = workspaceTabs(state, tabs); tabs = merged.tabs as Tab[]; activeId = merged.activeId ?? activeId;
    const current = tabById(activeId);
    if (current?.run?.status === 'failed') updateTab(current.id, { error: current.run.error || 'Query failed' });
    else if (current) fetchRemoteResult(current.id);
  }
  async function refreshWorkspace() {
    if (!boundApi) return;
    try { applyState(await boundApi.get()); } catch (error) { storageError = message(error); }
  }
  function syncDraft(id: string): Promise<boolean> {
    const pending = syncing.get(id); if (pending) return pending;
    const tab = tabById(id);
    if (!boundApi || !tab?.dirty || tab.conflict) return Promise.resolve(!tab?.conflict);
    if (!Number.isInteger(tab.revision)) { fail(id, new Error('View revision is unavailable'), true); return Promise.resolve(false); }
    const submitted = { sql: tab.sql, cursor: tab.cursor, revision: tab.revision };
    let request!: Promise<boolean>;
    request = (async () => {
      try {
        const server = await boundApi!.update(id, submitted.sql, submitted.revision, submitted.cursor);
        const latest = tabById(id);
        if (latest && (latest.sql !== submitted.sql || latest.cursor !== submitted.cursor)) {
          updateTab(id, { revision: server.revision, savedSql: server.sql, run: server.result, result: undefined, check: undefined, dirty: latest.sql !== server.sql, conflict: false, serverSql: undefined, serverRevision: undefined });
        } else applyServerView(server, true);
        return true;
      } catch (error) { fail(id, error, true); return false; }
      finally { if (syncing.get(id) === request) syncing.delete(id); }
    })();
    syncing.set(id, request);
    return request;
  }
  async function syncBeforeRun(id: string) {
    const pending = syncing.get(id); if (pending && !await pending) return false;
    return !tabById(id)?.dirty || await syncDraft(id);
  }
  async function flushDrafts() { for (const tab of tabs) if (tab.dirty && !tab.busy && !tab.conflict) await syncDraft(tab.id); }
  async function addView(position: 'first' | 'last' = 'last') {
    if (!boundApi) { const tab = newView(tabs.length + 1) as Tab; tabs = [...tabs, tab]; showView(tab.id); return; }
    try { const state = await boundApi.create(position); applyState(state); showView(state.view_id); } catch (error) { storageError = message(error); }
  }
  function renameActiveView() {
    if (!active) return;
    showView(active.id); renaming = active.id;
    requestAnimationFrame(() => requestAnimationFrame(() => document.querySelector<HTMLInputElement>('[aria-label="View name"]')?.focus()));
  }
  async function renameView(id: string, name: string) {
    renaming = '';
    if (!boundApi) { updateTab(id, { name: name.trim() || undefined }); return; }
    try { applyServerView(await boundApi.rename(id, name.trim()), false); } catch (error) { fail(id, error); }
  }
  async function closeView(id: string) {
    const tab = tabById(id); if (!tab || (tab.dirty && !confirm(`Close unsaved ${tabName(tab)}?`))) return;
    if (!boundApi) { const remaining = tabs.filter((item) => item.id !== id); if (remaining.length) { tabs = remaining; showView(remaining[0].id); } else void addView(); return; }
    if (tabs.length === 1) { fail(id, new Error('The last View cannot be removed.')); return; }
    try { await boundApi.remove(id); await refreshWorkspace(); } catch (error) { fail(id, error); }
  }
  function acceptSaved(id: string, saved: SavedIdentity) {
    const current = tabById(id); if (!current) return;
    updateTab(id, { ...(cleanAfterSave(current, saved.sql) as Tab), saved, busy: false, error: '' });
  }
  function acceptResult(id: string, changes: Pick<Tab, 'result' | 'check'>) { updateTab(id, { ...changes, busy: false, error: '' }); }
  function reportLogWarning(id: string, warning?: string) { if (warning) updateTab(id, { error: `${tabById(id)?.error ? `${tabById(id)!.error} ` : ''}Query log warning: ${warning}` }); }
  function savedFrom(result: QueryResult): SavedIdentity | undefined {
    return result.saved_query_id && result.saved_query_url && result.kind === 'query' ? { saved_query_id: result.saved_query_id, saved_query_url: result.saved_query_url, kind: result.kind, sql: result.sql, ...(result.name ? { name: result.name } : {}) } : undefined;
  }
  async function action(kind: 'run' | 'check' | 'save', cursor = active?.cursor ?? 0, name?: string) {
    const tab = active; if (!tab || tab.busy || savedBusy) return;
    updateTab(tab.id, { busy: true, error: '' });
    if (boundApi) {
      if (!await syncBeforeRun(tab.id)) return;
      const current = tabById(tab.id); if (!current) return;
      try {
        if (kind === 'check') acceptResult(current.id, { check: await boundApi.check(current.id, cursor) });
        else {
          const response = await boundApi.run(current.id, cursor, kind === 'save' ? { save: true, ...(name ? { name } : {}) } : {});
          updateTab(current.id, { revision: response.revision, run: response, result: undefined });
          if (response.status === 'failed') updateTab(current.id, { busy: false, error: response.error || 'Query failed' });
          else if (response.query_id) acceptResult(current.id, { result: await boundApi.fetch(current.id) });
          else updateTab(current.id, { busy: false });
          if (kind === 'save') {
            if (response.save_error) updateTab(current.id, { error: response.save_error });
            else if (response.saved_query_id && response.saved_query_url) acceptSaved(current.id, { saved_query_id: response.saved_query_id, saved_query_url: response.saved_query_url, kind: 'query', sql: current.sql, ...(name ? { name } : {}) });
            await refreshSaved();
          }
          reportLogWarning(current.id, response.query_log_error);
        }
      } catch (error) { fail(current.id, error); }
      return;
    }
    try {
      if (kind === 'run') { const result = await api.run(tab.sql, cursor); acceptResult(tab.id, { result }); reportLogWarning(tab.id, result.query_log_error); }
      else if (kind === 'check') acceptResult(tab.id, { check: await api.check(tab.sql, cursor) });
      else { const result = await api.run(tab.sql, cursor, { save: true, ...(name ? { name } : {}) }); acceptResult(tab.id, { result }); const saved = savedFrom(result); if (result.save_error) updateTab(tab.id, { error: result.save_error }); else if (saved) { acceptSaved(tab.id, saved); await refreshSaved(); } reportLogWarning(tab.id, result.query_log_error); }
    } catch (error) { fail(tab.id, error); }
  }
  function requestSave() { if (active && !active.busy) nameDialog = true; }
  async function saveView(name = active?.name) {
    const tab = active; if (!tab || tab.busy || savedBusy) return;
    updateTab(tab.id, { busy: true, error: '' });
    if (boundApi) {
      if (!await syncBeforeRun(tab.id)) return;
      try { const saved = await boundApi.save(tab.id); acceptSaved(tab.id, { ...saved, sql: tabById(tab.id)?.sql ?? tab.sql, ...(name ? { name } : {}) }); await refreshSaved(); } catch (error) { fail(tab.id, error); }
      return;
    }
    try { acceptSaved(tab.id, await api.saveView(tab.sql, name)); await refreshSaved(); } catch (error) { fail(tab.id, error); }
  }
  async function page(offset: number) {
    const tab = active; if (!tab?.result || tab.busy) return;
    updateTab(tab.id, { busy: true, error: '' });
    try { updateTab(tab.id, { busy: false, result: boundApi ? await boundApi.fetch(tab.id, offset, tab.result.page_size) : await api.page(tab.result.query_id, offset, tab.result.page_size) }); } catch (error) { fail(tab.id, error); }
  }
  async function refreshSaved() {
    try { savedItems = (await api.savedList()).items; if (boundApi) logItems = (await boundApi.queryLogList()).items; }
    catch (error) { storageError = message(error); }
  }
  async function openLog(logId: string) { if (!boundApi) return; try { const item = await boundApi.queryLogGet(logId); storageError = `${item.outcome}: ${item.row_count ?? 'unknown'} rows, ${item.column_count ?? 'unknown'} columns${item.error ? ` — ${item.error}` : ''}`; } catch (error) { storageError = message(error); } }
  async function openSaved(reference: string) {
    if (savedBusy) return; savedBusy = true;
    try {
      const saved = await api.load(reference);
      if (!boundApi) {
        const existing = tabs.find((tab) => !tab.dirty && tab.sql === saved.sql);
        if (existing) { showView(existing.id); updateTab(existing.id, { saved }); } else { const tab = { ...(newView(tabs.length + 1) as Tab), ...(saved.name ? { name: saved.name } : {}), sql: saved.sql, cursor: 0, dirty: false, savedSql: saved.sql, saved }; tabs = [...tabs, tab]; showView(tab.id); }
      } else {
        const state = await boundApi.create('last', saved.name); applyState(state); const server = state.views.find((item) => item.id === state.view_id); if (!server) throw new Error('Created View is unavailable');
        applyServerView(await boundApi.update(server.id, saved.sql, server.revision, 0), true); showView(server.id); updateTab(server.id, { saved });
      }
      openSavedDialog = false;
    } catch (error) { storageError = message(error); } finally { savedBusy = false; }
  }
  function focusSql() { view = 'view'; collapsed = false; requestAnimationFrame(() => document.querySelector<HTMLElement>('.cm-content')?.focus()); }
  function focusResults() { view = 'view'; requestAnimationFrame(() => document.querySelector<HTMLElement>('.results-panel')?.focus()); }
  function buildCommands(): Command[] {
    const busy = !active || active.busy || savedBusy; const result = active?.result;
    return [
      { id: 'settings', label: 'Settings', enabled: true, run: () => showUtility('settings') }, { id: 'saved', label: 'Saved Queries and Views', enabled: true, run: () => showUtility('saved') },
      { id: 'open', label: 'Open Saved', enabled: !savedBusy, run: () => openSavedDialog = true }, { id: 'focus-sql', label: 'Focus Query editor', enabled: !!active, run: focusSql }, { id: 'focus-results', label: 'Focus Results', enabled: !!result, run: focusResults },
      ...tabs.map((tab) => ({ id: `view-${tab.id}`, label: `View: ${tabName(tab)}`, enabled: true, run: () => showView(tab.id) })), { id: 'new-first', label: 'New View first', enabled: true, run: () => addView('first') }, { id: 'new-last', label: 'New View last', enabled: true, run: () => addView('last') },
      { id: 'rename', label: 'Rename View', enabled: !!active, run: renameActiveView }, { id: 'close', label: 'Close View', enabled: !!active, run: () => active && closeView(active.id) },
      { id: 'run', label: 'Run', shortcut: 'Cmd+Enter', enabled: !busy, run: () => action('run') }, { id: 'check', label: 'Check', shortcut: 'Shift+Cmd+Enter', enabled: !busy, run: () => action('check') }, { id: 'save', label: 'Run & Save', enabled: !busy, run: requestSave }, { id: 'save-view', label: 'Save View', enabled: !busy, run: () => saveView() },
      { id: 'hide', label: collapsed ? 'Show editor' : 'Hide editor', enabled: !!active, run: () => collapsed = !collapsed }, { id: 'previous-page', label: 'Previous result page', enabled: !!result && result.offset > 0 && !busy, run: () => result && page(Math.max(0, result.offset - result.page_size)) }, { id: 'next-page', label: 'Next result page', enabled: !!result?.has_more && !busy, run: () => result && page(result.offset + result.rows.length) },
      ...preferenceCommands.map((command) => ({ ...command, enabled: true })),
    ];
  }
  onMount(() => {
    api = new WorkbenchApi(base, projectRoot);
    try { const recovered = restore(localStorage.getItem(namespace) ?? ''); if (recovered) { tabs = recovered.tabs as Tab[]; activeId = recovered.activeId; } } catch { storageError = 'Browser storage is unavailable; local View drafts cannot be restored.'; }
    const initialize = async () => {
      if (workspaceId) { boundApi = new WorkspaceApi(base, projectRoot, workspaceId); try { applyState(await boundApi.open()); } catch (error) { storageError = message(error); } }
      void api.schema().then((value) => schema = value).catch(() => {}); await refreshSaved(); const requested = parameters.get('query'); if (requested) await openSaved(requested);
    };
    void initialize();
    const unload = (event: BeforeUnloadEvent) => { persist(); if (tabs.some((tab) => tab.dirty)) { event.preventDefault(); event.returnValue = ''; } };
    const keys = (event: KeyboardEvent) => { if (event.metaKey && !event.ctrlKey && !event.altKey && event.key.toLowerCase() === 'p') { event.preventDefault(); nameDialog = false; openSavedDialog = false; commandOpen = true; } };
    window.addEventListener('beforeunload', unload); window.addEventListener('pagehide', persist); window.addEventListener('keydown', keys, true);
    const timer = window.setInterval(() => { persist(); if (boundApi) { void flushDrafts(); void refreshWorkspace(); } }, 5000);
    return () => { window.clearInterval(timer); window.removeEventListener('beforeunload', unload); window.removeEventListener('pagehide', persist); window.removeEventListener('keydown', keys, true); };
  });
</script>

<main class="workbench"><header class="app-header"><span class="brand-mark">CA</span><span class="app-name">Workbench</span><span class="project-label">Project: {projectName}</span><div class="header-utilities" role="tablist" aria-label="Workbench views"><button class:active={view === 'settings'} type="button" role="tab" aria-selected={view === 'settings'} onclick={() => showUtility('settings')}>Settings</button><button class:active={view === 'saved'} type="button" role="tab" aria-label="Saved Queries and Views" title="Saved Queries and Views" aria-selected={view === 'saved'} onclick={() => showUtility('saved')}>Saved</button></div></header><section class="workspace"><div class="work-main">
  <div class="workspace-toolbar"><div class="toolbar-main"><ViewTabs {tabs} {activeId} utility={view} {renaming} onselect={showView} onclose={closeView} onadd={addView} onrename={renameView} /></div><div class="toolbar-actions"><Button onclick={() => commandOpen = true}>Commands <span class="shortcut">Cmd+P</span></Button></div></div>
  <Preferences storageKey={namespace} visible={view === 'settings'} oncommands={(items) => preferenceCommands = items} />
  {#if view === 'saved'}<SavedPanel items={savedItems} logs={logItems} busy={savedBusy} onopen={openSaved} onopenlog={openLog} />{/if}
  {#if view === 'view' && active}<section class="editor-panel"><div class="panel-heading" role="group" aria-label="Query editor header"><span>Query editor</span>{#if active.saved}<span class="saved-reference">Saved: <a href={active.saved.saved_query_url}>{active.saved.saved_query_id}</a></span>{/if}</div><div class="editor-content" hidden={collapsed}>{#key active.id}<SqlEditor value={active.sql} cursor={active.cursor} disabled={active.busy} {schema} onchange={edit} onaction={(kind, cursor) => action(kind, cursor)} />{/key}</div><div class="query-actions"><Button disabled={active.busy || savedBusy} onclick={() => action('run')}>Run <span class="shortcut">Cmd+Enter</span></Button><Button disabled={active.busy || savedBusy} onclick={() => action('check')}>Check <span class="shortcut">Shift+Cmd+Enter</span></Button><Button disabled={active.busy || savedBusy} onclick={requestSave}>Run &amp; Save</Button><Button disabled={active.busy || savedBusy} onclick={() => saveView()}>Save View</Button><Button class="editor-toggle" onclick={() => collapsed = !collapsed}>{collapsed ? 'Show editor' : 'Hide editor'}</Button></div>{#if active.error}<p class="error" role="alert">{active.error}</p>{/if}</section>
    <section class="results-panel" tabindex="-1"><div class="status-line"><span class="status-badge">{active.busy ? 'Working' : 'Ready'}</span>{#if active.check}<span class="notice">Valid: {active.check.row_count} rows, {active.check.column_count} columns.</span>{/if}</div>{#if active.result}<ResultsTable result={active.result} /><nav class="query-actions" aria-label="Result pages"><Button disabled={active.busy || active.result.offset === 0} onclick={() => page(Math.max(0, active.result!.offset - active.result!.page_size))}>Previous</Button><Button disabled={active.busy || !active.result.has_more} onclick={() => page(active.result!.offset + active.result!.rows.length)}>Next</Button></nav>{/if}</section>{/if}
  {#if storageError}<p class="error" role="alert">{storageError}</p>{/if}
</div></section></main>
<OpenSavedDialog open={openSavedDialog} busy={savedBusy} onopen={openSaved} onclose={() => openSavedDialog = false} />
<NameDialog open={nameDialog} title="Query name" onsubmit={(name) => { nameDialog = false; action('save', active?.cursor, name); }} onclose={() => nameDialog = false} />
<CommandPalette open={commandOpen} {commands} onclose={() => commandOpen = false} />
