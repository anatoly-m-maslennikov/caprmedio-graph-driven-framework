<!-- CA-R-2776@9 -->
<!-- CA-D-674@23 -->
<!-- CA-M-466@6 -->
<!-- CA-M-468@5 -->
<!-- CA-M-469@8 -->
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
  import SyncStatus from './lib/SyncStatus.svelte';
  import ViewTabs from './lib/ViewTabs.svelte';
  import { WorkbenchApi, WorkspaceApi } from './lib/api';
  import { migrateLegacyDraft } from './lib/legacy_drafts.js';
  import type { NativeBootstrap } from './lib/mcp_app_transport';
  import { formatSql } from './lib/sql_format.js';
  import type { OperationCaller } from './lib/transport';
  import type { CheckResult, GridState, QueryLogItem, QueryResult, ResultDisplayPreferences, SavedIdentity, SavedItem, Schema, SourceSyncStatus, ViewResult, WorkspaceState, WorkspaceView } from './lib/types';
  import { cleanAfterSave, newView, persistable, restore, storageKey, workspaceTabs } from './lib/workspace.js';

  type Tab = ReturnType<typeof newView> & { busy?: boolean; error?: string; result?: QueryResult; check?: CheckResult; saved?: SavedIdentity; revision?: number; run?: ViewResult; conflict?: boolean; syncDirty?: boolean; serverSql?: string; serverRevision?: number };
  const props = $props<{ caller: OperationCaller; native?: NativeBootstrap }>();
  const caller = props.caller;
  const native = props.native;
  function standaloneContext() {
    const base = location.pathname.replace(/\/+$/, '');
    const projectName = base.split('/').filter(Boolean).at(-1) ?? '';
    const parameters = new URLSearchParams(location.search);
    const projectRoot = parameters.get('project_root');
    const explicitWorkspaceId = parameters.get('workspace');
    const embedded = parameters.get('embedded') === '1';
    const standaloneSessionKey = `caprmedio.workbench.${projectRoot || projectName}.standalone-session`;
    // An explicit URL is native unless it names this browser's own persisted Workspace.
    // That exception lets an interrupted one-time unbound-draft adoption resume.
    const persistedStandaloneId = !embedded ? localStorage.getItem(standaloneSessionKey) : null;
    const standaloneBinding = !embedded && (!explicitWorkspaceId || explicitWorkspaceId === persistedStandaloneId);
    const workspaceId = (() => {
      if (!standaloneBinding) return explicitWorkspaceId ?? undefined;
      const existing = localStorage.getItem(standaloneSessionKey); if (existing) return existing;
      const created = `standalone-${crypto.randomUUID()}`; localStorage.setItem(standaloneSessionKey, created); return created;
    })();
    if (explicitWorkspaceId && explicitWorkspaceId === persistedStandaloneId) {
      parameters.delete('workspace');
      const search = parameters.toString(); history.replaceState(null, '', `${base}${search ? `?${search}` : ''}${location.hash}`);
    }
    const namespace = storageKey(projectName, workspaceId, projectRoot ?? undefined);
    const migrationKey = `${standaloneSessionKey}.unbound-migrated`;
    return {
      parameters, projectName, projectRoot, workspaceId, embedded, standaloneBinding, namespace,
      legacyNamespace: storageKey(projectName, undefined, projectRoot ?? undefined), migrationKey,
      migrationProgressKey: `${migrationKey}.progress`,
    };
  }
  const standalone = native === undefined ? standaloneContext() : undefined;
  const projectRoot = native?.projectRoot ?? standalone!.projectRoot;
  const projectName = native ? native.workspace.project_name : standalone!.projectName;
  const workspaceId = native?.sessionId ?? standalone!.workspaceId;
  const embedded = native !== undefined || standalone?.embedded === true;
  const standaloneBinding = standalone?.standaloneBinding ?? false;
  const namespace = native ? storageKey(projectName, native.sessionId, native.projectRoot) : standalone!.namespace;
  const legacyNamespace = standalone?.legacyNamespace ?? '';
  const migrationKey = standalone?.migrationKey ?? '';
  const migrationProgressKey = standalone?.migrationProgressKey ?? '';
  const initial = newView(1) as Tab;
  let tabs = $state<Tab[]>([initial]); let activeId = $state(initial.id); let view = $state<'settings' | 'saved' | 'view'>('view');
  let schema = $state<Schema>({ tables: {} }); let savedItems = $state<SavedItem[]>([]); let logItems = $state<QueryLogItem[]>([]); let syncStatus = $state<SourceSyncStatus>({ syncing: false, last_synced_at: null }); let storageError = $state(''); let collapsed = $state(false);
  let workspaceReady = $state(false); let savedBusy = $state(false); let openSavedDialog = $state(false); let commandOpen = $state(false); let nameDialog = $state<{ kind: 'save' | 'rename'; id?: string; initialValue: string } | null>(null);
  let preferenceCommands = $state<PreferenceCommand[]>([]); let api: WorkbenchApi; let boundApi: WorkspaceApi | undefined; const syncing = new Map<string, Promise<boolean>>(); const paging = new Map<string, number>(); let pageRequest = 0;
  let resultDisplay = $state<ResultDisplayPreferences>({ rowSizing: 'adaptive', fixedPageSize: 100, content: 'limited', contentLimit: 150 }); let grid = $state<GridState>({ sort: [], filters: [] }); let gridLayoutVersion = $state(0); let adaptedGeometry = $state('');
  let active = $derived(tabs.find((tab) => tab.id === activeId)); let commands = $derived(buildCommands());

  const message = (error: unknown) => error instanceof Error ? error.message : 'Request failed';
  function tabById(id: string) { return tabs.find((tab) => tab.id === id); }
  function tabName(tab: Tab) { return tab.name || tab.title; }
  function updateTab(id: string, changes: Partial<Tab>) { tabs = tabs.map((tab) => tab.id === id ? { ...tab, ...changes } : tab); }
  function persist() { if (native) return; try { localStorage.setItem(namespace, persistable(tabs, activeId)); storageError = ''; } catch { storageError = 'Browser storage is unavailable; local View drafts are not saved.'; } }
  function fail(id: string, error: unknown, conflict = false) { updateTab(id, { busy: false, error: message(error), ...(conflict ? { conflict: true } : {}) }); }
  function edit(sql: string, cursor: number) { if (active && (active.sql !== sql || active.cursor !== cursor)) updateTab(active.id, { sql, cursor, dirty: sql !== active.savedSql, syncDirty: true, conflict: false, error: '' }); }
  function formatActive() {
    const tab = active;
    if (!workspaceReady || !tab || tab.busy || savedBusy) return;
    try {
      const formatted = formatSql(tab.sql);
      edit(formatted, Math.min(tab.cursor, formatted.length));
    } catch (error) { updateTab(tab.id, { error: message(error) }); }
  }
  function showView(id: string) {
    if (view === 'view' && activeId === id) return;
    activeId = id; view = 'view'; grid = { sort: [], filters: [] }; fetchRemoteResult(id);
    if (boundApi) void boundApi.focus(id).then(({ active_view_id }) => activeId = active_view_id).catch((error) => fail(id, error));
  }
  function showUtility(next: 'settings' | 'saved') { view = next; if (next === 'saved') void refreshSaved(); }
  function applyServerView(server: WorkspaceView, replace = false) {
    const current = tabById(server.id); if (!current) return;
    if (!replace && (current.syncDirty || current.dirty) && server.sql !== current.sql) {
      updateTab(server.id, { ...(server.name === undefined ? { name: undefined } : { name: server.name }), run: server.result, serverSql: server.sql, serverRevision: server.revision });
      return;
    }
    updateTab(server.id, {
      ...(server.name === undefined ? { name: undefined } : { name: server.name }), revision: server.revision, run: server.result,
      ...(replace ? { sql: server.sql, savedSql: server.sql, cursor: server.cursor_position, dirty: false, syncDirty: false, conflict: false, result: undefined, check: undefined, serverSql: undefined, serverRevision: undefined } : {}),
    });
  }
  function fetchRemoteResult(id: string) {
    const tab = tabById(id); const queryId = tab?.run?.query_id;
    if (!boundApi || !tab || !queryId || tab.result?.query_id === queryId) return;
    void boundApi.fetch(id, 0, resultDisplay.rowSizing === 'fixed' ? resultDisplay.fixedPageSize : 100, grid).then((result) => { if (tabById(id)?.run?.query_id === queryId) updateTab(id, { result, error: '' }); }).catch((error) => fail(id, error));
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
  async function migrateUnboundDraft(state: WorkspaceState, draft: ReturnType<typeof restore>) {
    if (!boundApi || !standaloneBinding || !draft || localStorage.getItem(migrationKey) === 'done') return;
    const migrated = await migrateLegacyDraft({ draft, state, api: boundApi, storage: localStorage, doneKey: migrationKey, progressKey: migrationProgressKey });
    applyState(migrated.state as WorkspaceState);
    for (const source of draft.tabs) {
      const target = migrated.sourceToTarget[source.id];
      if (target) updateTab(target, { sql: source.sql, cursor: source.cursor, dirty: source.dirty, savedSql: source.savedSql ?? source.sql, syncDirty: false });
    }
  }
  async function refreshStatus() { try { syncStatus = await api.status(); } catch {} }
  function syncDraft(id: string): Promise<boolean> {
    const pending = syncing.get(id); if (pending) return pending;
    const tab = tabById(id);
    if (!boundApi || !tab?.syncDirty || tab.conflict) return Promise.resolve(!tab?.conflict);
    if (!Number.isInteger(tab.revision)) { fail(id, new Error('View revision is unavailable'), true); return Promise.resolve(false); }
    const submitted = { sql: tab.sql, cursor: tab.cursor, revision: tab.revision };
    let request!: Promise<boolean>;
    request = (async () => {
      try {
        const server = await boundApi!.update(id, submitted.sql, submitted.revision, submitted.cursor);
        const latest = tabById(id);
        if (latest && (latest.sql !== submitted.sql || latest.cursor !== submitted.cursor)) {
          updateTab(id, { revision: server.revision, run: server.result, result: undefined, check: undefined, syncDirty: true, conflict: false, serverSql: undefined, serverRevision: undefined });
        } else updateTab(id, { revision: server.revision, run: server.result, syncDirty: false, conflict: false, serverSql: undefined, serverRevision: undefined });
        return true;
      } catch (error) { fail(id, error, true); return false; }
      finally { if (syncing.get(id) === request) syncing.delete(id); }
    })();
    syncing.set(id, request);
    return request;
  }
  async function syncBeforeRun(id: string) {
    const pending = syncing.get(id); if (pending && !await pending) return false;
    return !tabById(id)?.syncDirty || await syncDraft(id);
  }
  async function flushDrafts() { for (const tab of tabs) if (tab.syncDirty && !tab.busy && !tab.conflict) await syncDraft(tab.id); }
  async function addView(position: 'first' | 'last' = 'last') {
    if (!workspaceReady || !boundApi) { storageError = 'Workspace is unavailable.'; return; }
    try { const state = await boundApi.create(position); applyState(state); showView(state.view_id); } catch (error) { storageError = message(error); }
  }
  async function duplicateView(id = active?.id) {
    const source = id ? tabById(id) : undefined;
    if (!workspaceReady || !boundApi || !source || source.busy || savedBusy) return;
    if (!await syncBeforeRun(source.id) || tabById(source.id)?.syncDirty || tabById(source.id)?.conflict) return;
    try {
      const state = await boundApi.duplicate(source.id);
      applyState(state);
      if (!tabById(state.view_id)) throw new Error('Duplicated View is unavailable.');
      updateTab(state.view_id, { savedSql: '', dirty: true, syncDirty: false, saved: undefined, result: undefined, check: undefined, run: undefined, error: '' });
      showView(state.view_id);
    }
    catch (error) { fail(source.id, error); }
  }
  function renameActiveView() {
    if (active) requestRename(active.id);
  }
  function requestRename(id: string) { const tab = tabById(id); if (!tab) return; showView(id); nameDialog = { kind: 'rename', id, initialValue: tabName(tab) }; }
  function submitName(name: string) { const request = nameDialog; nameDialog = null; if (request?.kind === 'rename' && request.id) void renameView(request.id, name); else void action('save', active?.cursor, name); }
  async function renameView(id: string, name: string) {
    if (!boundApi) { storageError = 'Workspace is unavailable.'; return; }
    try { applyServerView(await boundApi.rename(id, name.trim()), false); } catch (error) { fail(id, error); }
  }
  async function closeView(id: string) {
    const tab = tabById(id); if (!tab || (tab.dirty && !confirm(`Close unsaved ${tabName(tab)}?`))) return;
    if (!boundApi) { storageError = 'Workspace is unavailable.'; return; }
    if (tabs.length === 1) { fail(id, new Error('The last View cannot be removed.')); return; }
    try { await boundApi.remove(id); await refreshWorkspace(); } catch (error) { fail(id, error); }
  }
  function acceptSaved(id: string, saved: SavedIdentity) {
    const current = tabById(id); if (!current) return;
    updateTab(id, { ...(cleanAfterSave(current, saved.sql) as Tab), syncDirty: false, saved, busy: false, error: '' });
  }
  function acceptResult(id: string, changes: Pick<Tab, 'result' | 'check'>) { updateTab(id, { ...changes, busy: false, error: '' }); }
  function reportLogWarning(id: string, warning?: string) { if (warning) updateTab(id, { error: `${tabById(id)?.error ? `${tabById(id)!.error} ` : ''}Query log warning: ${warning}` }); }
  function savedFrom(result: QueryResult): SavedIdentity | undefined {
    return result.saved_query_id && result.saved_query_url && result.kind === 'query' ? { saved_query_id: result.saved_query_id, saved_query_url: result.saved_query_url, kind: result.kind, sql: result.sql, ...(result.name ? { name: result.name } : {}) } : undefined;
  }
  async function action(kind: 'run' | 'check' | 'save', cursor = active?.cursor ?? 0, name?: string) {
    const tab = active; if (!workspaceReady || !tab || tab.busy || savedBusy) return;
    updateTab(tab.id, { busy: true, error: '' });
    if (!boundApi) { fail(tab.id, new Error('Workspace is unavailable.')); return; }
    if (!await syncBeforeRun(tab.id)) { updateTab(tab.id, { busy: false }); return; }
    const current = tabById(tab.id); if (!current) return;
    try {
      if (kind === 'check') acceptResult(current.id, { check: await boundApi.check(current.id, cursor) });
      else {
        const response = await boundApi.run(current.id, cursor, kind === 'save' ? { save: true, ...(name ? { name } : {}) } : {});
        grid = { sort: [], filters: [] }; updateTab(current.id, { revision: response.revision, run: response, result: undefined });
        if (response.status === 'failed') updateTab(current.id, { busy: false, error: response.error || 'Query failed' });
        else if (response.query_id) acceptResult(current.id, { result: await boundApi.fetch(current.id, 0, resultDisplay.rowSizing === 'fixed' ? resultDisplay.fixedPageSize : 100, grid) });
        else updateTab(current.id, { busy: false });
        if (kind === 'save') {
          if (response.save_error) updateTab(current.id, { error: response.save_error });
          else if (response.saved_query_id && response.saved_query_url) acceptSaved(current.id, { saved_query_id: response.saved_query_id, saved_query_url: response.saved_query_url, kind: 'query', sql: current.sql, ...(name ? { name } : {}) });
          await refreshSaved();
        }
        reportLogWarning(current.id, response.query_log_error);
      }
    } catch (error) { fail(current.id, error); }
  }
  function requestSave() { if (workspaceReady && active && !active.busy) nameDialog = { kind: 'save', initialValue: '' }; }
  async function saveView(name = active?.name) {
    const tab = active; if (!workspaceReady || !tab || tab.busy || savedBusy) return;
    updateTab(tab.id, { busy: true, error: '' });
    if (!boundApi) { fail(tab.id, new Error('Workspace is unavailable.')); return; }
    if (!await syncBeforeRun(tab.id)) { updateTab(tab.id, { busy: false }); return; }
    try { const saved = await boundApi.save(tab.id); acceptSaved(tab.id, { ...saved, sql: tabById(tab.id)?.sql ?? tab.sql, ...(name ? { name } : {}) }); await refreshSaved(); } catch (error) { fail(tab.id, error); }
  }
  async function page(offset: number, pageSize = active?.result?.page_size, nextGrid = grid) {
    const tab = active; if (!tab?.result || tab.busy) return;
    const queryId = tab.result.query_id;
    const request = ++pageRequest; paging.set(tab.id, request);
    try {
      if (!boundApi || !pageSize) throw new Error('Workspace is unavailable.');
      const result = await boundApi.fetch(tab.id, offset, pageSize, nextGrid);
      const latest = tabById(tab.id);
      if (paging.get(tab.id) === request && !latest?.busy && latest?.result?.query_id === queryId) updateTab(tab.id, { error: '', result });
    } catch (error) {
      const latest = tabById(tab.id);
      if (paging.get(tab.id) === request && !latest?.busy && latest?.result?.query_id === queryId) updateTab(tab.id, { error: message(error) });
    }
    finally { if (paging.get(tab.id) === request) paging.delete(tab.id); }
  }
  function setResultDisplay(next: ResultDisplayPreferences) {
    const sizingChanged = next.rowSizing !== resultDisplay.rowSizing || next.fixedPageSize !== resultDisplay.fixedPageSize;
    resultDisplay = next; if (sizingChanged) gridLayoutVersion += 1;
    if (next.rowSizing === 'fixed' && active?.result) void page(active.result.offset, next.fixedPageSize);
  }
  function setGrid(next: GridState) { grid = next; if (active?.result) void page(0, active.result.page_size, next); }
  function adaptPage(size: number, geometry: string) {
    const result = active?.result; if (!result || resultDisplay.rowSizing !== 'adaptive') return;
    const key = `${result.query_id}:${gridLayoutVersion}:${JSON.stringify(grid)}:${geometry}`;
    if (adaptedGeometry === key || result.page_size === size) return;
    adaptedGeometry = key; void page(result.offset, size);
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
      if (!boundApi) throw new Error('Workspace is unavailable.');
      const existing = tabs.filter((tab) => tab.saved?.saved_query_id === saved.saved_query_id).find((tab) => tab.id === activeId) ?? tabs.find((tab) => tab.saved?.saved_query_id === saved.saved_query_id);
      if (existing) { showView(existing.id); openSavedDialog = false; return; }
      const state = await boundApi.create('last', saved.name); applyState(state); const server = state.views.find((item) => item.id === state.view_id); if (!server) throw new Error('Created View is unavailable');
      applyServerView(await boundApi.update(server.id, saved.sql, server.revision, 0), true); showView(server.id); updateTab(server.id, { saved });
      openSavedDialog = false;
    } catch (error) { storageError = message(error); } finally { savedBusy = false; }
  }
  function savedLink(event: MouseEvent, id: string) {
    if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    showView(id);
  }
  function focusSql() { view = 'view'; collapsed = false; requestAnimationFrame(() => document.querySelector<HTMLElement>('.cm-content')?.focus()); }
  function focusResults() { view = 'view'; requestAnimationFrame(() => document.querySelector<HTMLElement>('.results-panel')?.focus()); }
  function gridColumn() {
    const result = active?.result; if (!result) return -1;
    const value = window.prompt(`Result column index (0-${result.columns.length - 1})`, '0');
    if (value === null) return -1;
    const index = Number(value); return Number.isInteger(index) && index >= 0 && index < result.columns.length ? index : -1;
  }
  function gridRow() {
    const result = active?.result; if (!result) return -1;
    const value = window.prompt(`Result row index on this page (0-${result.rows.length - 1})`, '0');
    if (value === null) return -1;
    const index = Number(value); return Number.isInteger(index) && index >= 0 && index < result.rows.length ? index : -1;
  }
  function resultValue(value: unknown) { if (value === null) return 'NULL'; try { return typeof value === 'object' ? JSON.stringify(value) : String(value); } catch { return String(value); } }
  function copyResult(value: unknown) { void navigator.clipboard?.writeText(resultValue(value)).catch(() => {}); }
  function filterGrid() { const column = gridColumn(); if (column < 0) return; const value = window.prompt(`Filter ${active!.result!.columns[column].name}`, grid.filters.find((item) => item.column === column)?.value ?? ''); if (value === null) return; const filters = grid.filters.filter((item) => item.column !== column); if (value) filters.push({ column, operator: 'contains', value }); setGrid({ ...grid, filters }); }
  function buildCommands(): Command[] {
    const busy = !workspaceReady || !active || active.busy || savedBusy; const result = active?.result;
    return [
      { id: 'settings', label: 'Settings', enabled: true, run: () => showUtility('settings') }, { id: 'saved', label: 'Bookmarks and saved Views', enabled: true, run: () => showUtility('saved') },
      { id: 'open', label: 'Open Saved', enabled: !savedBusy, run: () => openSavedDialog = true }, { id: 'focus-sql', label: 'Focus Query editor', enabled: !!active, run: focusSql }, { id: 'focus-results', label: 'Focus Results', enabled: !!result, run: focusResults },
      ...tabs.map((tab) => ({ id: `view-${tab.id}`, label: `View: ${tabName(tab)}`, enabled: workspaceReady, run: () => showView(tab.id) })), { id: 'new-first', label: 'New View first', enabled: workspaceReady, run: () => addView('first') }, { id: 'new-last', label: 'New View last', enabled: workspaceReady, run: () => addView('last') },
      { id: 'rename', label: 'Rename View', enabled: workspaceReady && !!active, run: renameActiveView }, { id: 'duplicate', label: 'Duplicate View', enabled: workspaceReady && !!active && !active.busy && !savedBusy, run: () => active && duplicateView(active.id) }, { id: 'close', label: 'Close View', enabled: workspaceReady && !!active, run: () => active && closeView(active.id) },
      { id: 'run', label: 'Run', shortcut: 'Cmd+Enter', enabled: !busy, run: () => action('run') }, { id: 'check', label: 'Check', shortcut: 'Shift+Cmd+Enter', enabled: !busy, run: () => action('check') }, { id: 'format', label: 'Format', enabled: !busy, run: formatActive }, { id: 'save', label: 'Run & Save', enabled: !busy, run: requestSave }, { id: 'save-view', label: 'Save View', enabled: !busy, run: () => saveView() },
      { id: 'hide', label: collapsed ? 'Show editor' : 'Hide editor', enabled: !!active, run: () => collapsed = !collapsed }, { id: 'previous-page', label: 'Previous result page', enabled: !!result && result.offset > 0 && !busy, run: () => result && page(Math.max(0, result.offset - result.page_size)) }, { id: 'next-page', label: 'Next result page', enabled: !!result?.has_more && !busy, run: () => result && page(result.offset + result.rows.length) },
      { id: 'grid-copy-value', label: 'Result grid: Copy cell value', enabled: !!result, run: () => { const row = gridRow(); const column = gridColumn(); if (row >= 0 && column >= 0) copyResult(result!.rows[row][column]); } }, { id: 'grid-show-value', label: 'Result grid: Show full cell value', enabled: !!result, run: () => { const row = gridRow(); const column = gridColumn(); if (row >= 0 && column >= 0) window.alert(resultValue(result!.rows[row][column])); } }, { id: 'grid-copy-row', label: 'Result grid: Copy row', enabled: !!result, run: () => { const row = gridRow(); if (row >= 0) copyResult(result!.rows[row]); } },
      { id: 'grid-sort-asc', label: 'Result grid: Sort column ascending', enabled: !!result, run: () => { const column = gridColumn(); if (column >= 0) setGrid({ ...grid, sort: [...grid.sort.filter((item) => item.column !== column), { column, direction: 'asc' }] }); } }, { id: 'grid-sort-desc', label: 'Result grid: Sort column descending', enabled: !!result, run: () => { const column = gridColumn(); if (column >= 0) setGrid({ ...grid, sort: [...grid.sort.filter((item) => item.column !== column), { column, direction: 'desc' }] }); } },
      { id: 'grid-group-asc', label: 'Result grid: Group column ascending', enabled: !!result, run: () => { const column = gridColumn(); if (column >= 0) setGrid({ ...grid, group_by: { column, direction: 'asc' } }); } }, { id: 'grid-group-desc', label: 'Result grid: Group column descending', enabled: !!result, run: () => { const column = gridColumn(); if (column >= 0) setGrid({ ...grid, group_by: { column, direction: 'desc' } }); } }, { id: 'grid-clear-group', label: 'Result grid: Clear grouping', enabled: !!grid.group_by, run: () => setGrid({ ...grid, group_by: undefined }) }, { id: 'grid-filter', label: 'Result grid: Filter column', enabled: !!result, run: filterGrid }, { id: 'grid-clear-filter', label: 'Result grid: Clear filter', enabled: grid.filters.length > 0, run: () => setGrid({ ...grid, filters: [] }) },
      ...preferenceCommands.map((command) => ({ ...command, enabled: true })),
    ];
  }
  onMount(() => {
    api = new WorkbenchApi(caller);
    if (!native) try { const recovered = restore(localStorage.getItem(namespace) ?? ''); if (recovered) { tabs = recovered.tabs as Tab[]; activeId = recovered.activeId; } } catch { storageError = 'Browser storage is unavailable; local View drafts cannot be restored.'; }
    const initialize = async () => {
      if (native) {
        boundApi = new WorkspaceApi(caller, native.sessionId); applyState(native.workspace);
      } else if (!workspaceId) storageError = 'Embedded workspace URL is missing a session ID.';
      else {
        boundApi = new WorkspaceApi(caller, workspaceId);
        try {
          const state = standaloneBinding ? await boundApi.open() : await boundApi.get(); applyState(state);
          if (standaloneBinding) { const draft = restore(localStorage.getItem(legacyNamespace) ?? ''); await migrateUnboundDraft(state, draft); }
        } catch (error) { storageError = message(error); }
      }
      workspaceReady = true;
      void refreshStatus(); void api.schema().then((value) => schema = value).catch(() => {}); await refreshSaved(); const requested = standalone?.parameters.get('query'); if (requested) await openSaved(requested);
    };
    void initialize();
    const unload = (event: BeforeUnloadEvent) => { persist(); if (tabs.some((tab) => tab.dirty)) { event.preventDefault(); event.returnValue = ''; } };
    const keys = (event: KeyboardEvent) => { if (workspaceReady && event.metaKey && !event.ctrlKey && !event.altKey && event.key.toLowerCase() === 'p') { event.preventDefault(); nameDialog = null; openSavedDialog = false; commandOpen = true; } };
    const catchUpSync = () => { if (boundApi) void flushDrafts(); };
    window.addEventListener('beforeunload', unload); window.addEventListener('pagehide', persist); window.addEventListener('keydown', keys, true);
    window.addEventListener('focus', catchUpSync); document.addEventListener('visibilitychange', catchUpSync);
    const timer = window.setInterval(() => { persist(); void refreshStatus(); if (boundApi) { void flushDrafts(); void refreshWorkspace(); } }, 5000);
    return () => { window.clearInterval(timer); window.removeEventListener('beforeunload', unload); window.removeEventListener('pagehide', persist); window.removeEventListener('keydown', keys, true); window.removeEventListener('focus', catchUpSync); document.removeEventListener('visibilitychange', catchUpSync); };
  });
</script>

<main class="workbench"><header class="app-header"><span class="brand-mark">CA</span><span class="app-name">Workbench</span><span class="project-label">Project: {projectName}</span><div class="header-right"><SyncStatus status={syncStatus} /><div class="header-utilities" role="tablist" aria-label="Workbench views"><button class:active={view === 'settings'} type="button" role="tab" aria-selected={view === 'settings'} onclick={() => showUtility('settings')}>Settings</button><button class:active={view === 'saved'} type="button" role="tab" aria-label="Bookmarks and saved Views" title="Bookmarks and saved Views" aria-selected={view === 'saved'} onclick={() => showUtility('saved')}>Saved</button></div></div></header><section class="workspace"><div class="work-main">
  <div class="workspace-toolbar"><div class="toolbar-main"><ViewTabs {tabs} {activeId} utility={view} ready={workspaceReady} onselect={showView} onclose={closeView} onadd={addView} onrenamerequest={requestRename} onduplicate={duplicateView} /></div><div class="toolbar-actions"><Button disabled={!workspaceReady} onclick={() => commandOpen = true}>Commands <span class="shortcut">Cmd+P</span></Button></div></div>
  <Preferences storageKey={namespace} {embedded} visible={view === 'settings'} {resultDisplay} onresultdisplaychange={setResultDisplay} onlayoutchange={() => gridLayoutVersion += 1} oncommands={(items) => preferenceCommands = items} />
  {#if view === 'saved'}<SavedPanel items={savedItems} logs={logItems} busy={savedBusy} onopen={openSaved} onopenlog={openLog} />{/if}
  {#if view === 'view' && active}<section class="editor-panel"><div class="panel-heading"><button class="editor-heading" type="button" aria-expanded={!collapsed} aria-controls={`query-editor-${active.id}`} onclick={() => collapsed = !collapsed}><span>Query editor</span><span class="editor-heading-state">{collapsed ? 'Show editor' : 'Hide editor'}</span></button>{#if active.saved}<span class="saved-reference">Saved: <a href={active.saved.saved_query_url} onclick={(event) => savedLink(event, active.id)}>{active.saved.saved_query_id}</a></span>{/if}</div><div class="editor-content" id={`query-editor-${active.id}`} hidden={collapsed}>{#key active.id}<SqlEditor value={active.sql} cursor={active.cursor} disabled={!workspaceReady || active.busy} {schema} onchange={edit} onaction={(kind, cursor) => action(kind, cursor)} />{/key}</div><div class="query-actions"><Button disabled={!workspaceReady || active.busy || savedBusy} onclick={() => action('run')}>Run <span class="shortcut">Cmd+Enter</span></Button><Button disabled={!workspaceReady || active.busy || savedBusy} onclick={() => action('check')}>Check <span class="shortcut">Shift+Cmd+Enter</span></Button><Button disabled={!workspaceReady || active.busy || savedBusy} onclick={formatActive}>Format</Button><Button disabled={!workspaceReady || active.busy || savedBusy} onclick={requestSave}>Run &amp; Save</Button><Button disabled={!workspaceReady || active.busy || savedBusy} onclick={() => saveView()}>Save View</Button></div>{#if active.error}<p class="error" role="alert">{active.error}</p>{/if}</section>
    <section class="results-panel" tabindex="-1"><div class="status-line"><span class="status-badge">{active.busy ? 'Working' : 'Ready'}</span>{#if active.check}<span class="notice">Valid: {active.check.row_count} rows, {active.check.column_count} columns.</span>{/if}</div>{#if active.result}<ResultsTable result={active.result} display={resultDisplay} {grid} layoutVersion={gridLayoutVersion} ondisplaychange={setResultDisplay} ongridchange={setGrid} oncapacity={adaptPage} /><nav class="query-actions" aria-label="Result pages"><Button disabled={active.busy || active.result.offset === 0} onclick={() => page(Math.max(0, active.result!.offset - active.result!.page_size))}>Previous</Button><Button disabled={active.busy || !active.result.has_more} onclick={() => page(active.result!.offset + active.result!.rows.length)}>Next</Button></nav>{/if}</section>{/if}
  {#if storageError}<p class="error" role="alert">{storageError}</p>{/if}
</div></section></main>
<OpenSavedDialog open={openSavedDialog} busy={savedBusy} onopen={openSaved} onclose={() => openSavedDialog = false} />
<NameDialog open={nameDialog !== null} title={nameDialog?.kind === 'rename' ? 'View name' : 'Bookmark name'} initialValue={nameDialog?.initialValue ?? ''} onsubmit={submitName} onclose={() => nameDialog = null} />
<CommandPalette open={commandOpen} {commands} onclose={() => commandOpen = false} />
