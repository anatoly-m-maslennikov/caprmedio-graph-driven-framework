<!-- CA-R-2727@9 -->
<!-- CA-D-674@13 -->
<!-- CA-M-470@3 -->
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
  import WorksheetTabs from './lib/WorksheetTabs.svelte';
  import { WorkbenchApi } from './lib/api';
  import type { CheckResult, QueryResult, SavedIdentity, SavedItem, Schema } from './lib/types';
  import { cleanAfterSave, newWorksheet, persistable, restore, storageKey } from './lib/workspace.js';

  type Tab = ReturnType<typeof newWorksheet> & { busy?: boolean; error?: string; result?: QueryResult; check?: CheckResult; saved?: SavedIdentity };
  const base = location.pathname.replace(/\/+$/, '');
  const projectName = base.split('/').filter(Boolean).at(-1) ?? '';
  const projectRoot = new URLSearchParams(location.search).get('project_root');
  const namespace = storageKey(projectName);
  const initial = newWorksheet(1) as Tab;
  let tabs = $state<Tab[]>([initial]); let activeId = $state(initial.id); let view = $state<'settings' | 'saved' | 'worksheet'>('worksheet');
  let schema = $state<Schema>({ tables: {} }); let savedItems = $state<SavedItem[]>([]); let storageError = $state(''); let collapsed = $state(false);
  let savedBusy = $state(false); let openSavedDialog = $state(false); let commandOpen = $state(false); let nameDialog = $state(false); let renaming = $state('');
  let preferenceCommands = $state<PreferenceCommand[]>([]); let api: WorkbenchApi; let active = $derived(tabs.find((tab) => tab.id === activeId));
  let commands = $derived(buildCommands());

  function tabById(id: string) { return tabs.find((tab) => tab.id === id); }
  function tabName(tab: Tab) { return tab.name || tab.title; }
  function updateTab(id: string, changes: Partial<Tab>) { tabs = tabs.map((tab) => tab.id === id ? { ...tab, ...changes } : tab); }
  function persist() { try { localStorage.setItem(namespace, persistable(tabs, activeId)); storageError = ''; } catch { storageError = 'Browser storage is unavailable; local Worksheet drafts are not saved.'; } }
  function edit(sql: string, cursor: number) { if (active) updateTab(active.id, { sql, cursor, dirty: sql !== active.savedSql }); }
  function showWorksheet(id: string) { activeId = id; view = 'worksheet'; }
  function showUtility(next: 'settings' | 'saved') { view = next; if (next === 'saved') void refreshSaved(); }
  function addWorksheet() { const tab = newWorksheet(tabs.length + 1) as Tab; tabs = [...tabs, tab]; showWorksheet(tab.id); }
  function renameActiveWorksheet() {
    if (!active) return;
    showWorksheet(active.id); renaming = active.id;
    requestAnimationFrame(() => requestAnimationFrame(() => document.querySelector<HTMLInputElement>('[aria-label="Worksheet name"]')?.focus()));
  }
  function renameWorksheet(id: string, name: string) { updateTab(id, { name: name.trim() || undefined }); renaming = ''; }
  function closeWorksheet(id: string) {
    const tab = tabById(id); if (!tab || (tab.dirty && !confirm(`Close unsaved ${tabName(tab)}?`))) return;
    const remaining = tabs.filter((item) => item.id !== id); if (remaining.length) { tabs = remaining; showWorksheet(remaining[0].id); } else addWorksheet();
  }
  function acceptSaved(id: string, saved: SavedIdentity) {
    const current = tabById(id); if (!current) return;
    const changes: Partial<Tab> = { ...(cleanAfterSave(current, saved.sql) as Tab), saved, busy: false, error: '' };
    updateTab(id, changes);
  }
  function acceptResult(id: string, changes: Pick<Tab, 'result' | 'check'>) {
    updateTab(id, { ...changes, busy: false, error: '' });
  }
  function savedError(id: string, error: unknown) {
    updateTab(id, { busy: false, error: error instanceof Error ? error.message : 'Request failed' });
  }
  async function action(kind: 'run' | 'check' | 'save', cursor = active?.cursor ?? 0, name?: string) {
    const tab = active; if (!tab || tab.busy || savedBusy) return;
    updateTab(tab.id, { busy: true, error: '' });
    try {
      if (kind === 'run') acceptResult(tab.id, { result: await api.run(tab.sql, cursor) });
      else if (kind === 'check') acceptResult(tab.id, { check: await api.check(tab.sql, cursor) });
      else acceptSaved(tab.id, await api.save(tab.sql, cursor, name));
      if (kind === 'save') await refreshSaved();
    } catch (error) { savedError(tab.id, error); }
  }
  function requestSave() { if (active && !active.busy) nameDialog = true; }
  async function saveWorksheet(name = active?.name) {
    const tab = active; if (!tab || tab.busy || savedBusy) return;
    updateTab(tab.id, { busy: true, error: '' });
    try { acceptSaved(tab.id, await api.saveWorksheet(tab.sql, name)); await refreshSaved(); } catch (error) { savedError(tab.id, error); }
  }
  async function page(offset: number) {
    const tab = active; if (!tab?.result || tab.busy) return;
    updateTab(tab.id, { busy: true, error: '' }); try { updateTab(tab.id, { busy: false, result: await api.page(tab.result.query_id, offset, tab.result.page_size) }); } catch (error) { savedError(tab.id, error); }
  }
  async function refreshSaved() { try { savedItems = (await api.savedList()).items; } catch (error) { storageError = error instanceof Error ? error.message : 'Could not load saved items.'; } }
  async function openSaved(reference: string) {
    if (savedBusy) return; savedBusy = true;
    try { const saved = await api.load(reference); const existing = tabs.find((tab) => !tab.dirty && tab.sql === saved.sql); if (existing) { showWorksheet(existing.id); updateTab(existing.id, { saved }); } else { const tab = { ...(newWorksheet(tabs.length + 1) as Tab), ...(saved.name ? { name: saved.name } : {}), sql: saved.sql, cursor: 0, dirty: false, savedSql: saved.sql, saved }; tabs = [...tabs, tab]; showWorksheet(tab.id); } openSavedDialog = false; }
    catch (error) { storageError = error instanceof Error ? error.message : 'Could not load saved item.'; } finally { savedBusy = false; }
  }
  function focusSql() { view = 'worksheet'; collapsed = false; requestAnimationFrame(() => document.querySelector<HTMLElement>('.cm-content')?.focus()); }
  function focusResults() { view = 'worksheet'; requestAnimationFrame(() => document.querySelector<HTMLElement>('.results-panel')?.focus()); }
  function buildCommands(): Command[] {
    const busy = !active || active.busy || savedBusy; const result = active?.result;
    return [
      { id: 'settings', label: 'Settings', enabled: true, run: () => showUtility('settings') }, { id: 'saved', label: 'Saved Queries and Worksheets', enabled: true, run: () => showUtility('saved') },
      { id: 'open', label: 'Open Saved', enabled: !savedBusy, run: () => openSavedDialog = true }, { id: 'focus-sql', label: 'Focus Query editor', enabled: !!active, run: focusSql }, { id: 'focus-results', label: 'Focus Results', enabled: !!result, run: focusResults },
      ...tabs.map((tab) => ({ id: `worksheet-${tab.id}`, label: `Worksheet: ${tabName(tab)}`, enabled: true, run: () => showWorksheet(tab.id) })), { id: 'new', label: 'New Worksheet', enabled: true, run: addWorksheet },
      { id: 'rename', label: 'Rename Worksheet', enabled: !!active, run: renameActiveWorksheet }, { id: 'close', label: 'Close Worksheet', enabled: !!active, run: () => active && closeWorksheet(active.id) },
      { id: 'run', label: 'Run', shortcut: 'Cmd+Enter', enabled: !busy, run: () => action('run') }, { id: 'check', label: 'Check', shortcut: 'Shift+Cmd+Enter', enabled: !busy, run: () => action('check') }, { id: 'save', label: 'Save', enabled: !busy, run: requestSave }, { id: 'save-worksheet', label: 'Save Worksheet', enabled: !busy, run: () => saveWorksheet() },
      { id: 'hide', label: collapsed ? 'Show editor' : 'Hide editor', enabled: !!active, run: () => collapsed = !collapsed }, { id: 'previous-page', label: 'Previous result page', enabled: !!result && result.offset > 0 && !busy, run: () => result && page(Math.max(0, result.offset - result.page_size)) }, { id: 'next-page', label: 'Next result page', enabled: !!result?.has_more && !busy, run: () => result && page(result.offset + result.rows.length) },
      ...preferenceCommands.map((command) => ({ ...command, enabled: true })),
    ];
  }
  onMount(() => {
    api = new WorkbenchApi(base, projectRoot); try { const recovered = restore(localStorage.getItem(namespace) ?? ''); if (recovered) { tabs = recovered.tabs as Tab[]; activeId = recovered.activeId; } } catch { storageError = 'Browser storage is unavailable; local Worksheet drafts cannot be restored.'; }
    void api.schema().then((value) => schema = value).catch(() => {}); void refreshSaved(); const requested = new URLSearchParams(location.search).get('query'); if (requested) void openSaved(requested);
    const unload = (event: BeforeUnloadEvent) => { persist(); if (tabs.some((tab) => tab.dirty)) { event.preventDefault(); event.returnValue = ''; } };
    const keys = (event: KeyboardEvent) => { if (event.metaKey && !event.ctrlKey && !event.altKey && event.key.toLowerCase() === 'p') { event.preventDefault(); nameDialog = false; openSavedDialog = false; commandOpen = true; } };
    window.addEventListener('beforeunload', unload); window.addEventListener('pagehide', persist); window.addEventListener('keydown', keys, true); const timer = window.setInterval(persist, 5000);
    return () => { window.clearInterval(timer); window.removeEventListener('beforeunload', unload); window.removeEventListener('pagehide', persist); window.removeEventListener('keydown', keys, true); };
  });
</script>

<main class="workbench"><header class="app-header"><span class="brand-mark">CA</span><span class="app-name">Workbench</span><span class="project-label">Project: {projectName}</span><div class="header-utilities" role="tablist" aria-label="Workbench views"><button class:active={view === 'settings'} type="button" role="tab" aria-selected={view === 'settings'} onclick={() => showUtility('settings')}>Settings</button><button class:active={view === 'saved'} type="button" role="tab" aria-label="Saved Queries and Worksheets" title="Saved Queries and Worksheets" aria-selected={view === 'saved'} onclick={() => showUtility('saved')}>Saved</button></div></header><section class="workspace">
  <div class="workspace-toolbar"><div class="toolbar-main"><WorksheetTabs {tabs} {activeId} utility={view} {renaming} onselect={showWorksheet} onclose={closeWorksheet} onadd={addWorksheet} onrename={renameWorksheet} /></div><div class="toolbar-actions"><Button onclick={() => commandOpen = true}>Commands <span class="shortcut">Cmd+P</span></Button></div></div>
  <Preferences storageKey={namespace} visible={view === 'settings'} oncommands={(items) => preferenceCommands = items} />
  {#if view === 'saved'}<SavedPanel items={savedItems} busy={savedBusy} onopen={openSaved} />{/if}
  {#if view === 'worksheet' && active}<section class="editor-panel"><div class="panel-heading" role="group" aria-label="Query editor header"><span>Query editor</span>{#if active.saved}<span class="saved-reference">Saved: <a href={active.saved.saved_query_url}>{active.saved.saved_query_id}</a></span>{/if}</div><div class="editor-content" hidden={collapsed}>{#key active.id}<SqlEditor value={active.sql} cursor={active.cursor} disabled={active.busy} {schema} onchange={edit} onaction={(kind, cursor) => action(kind, cursor)} />{/key}</div><div class="query-actions"><Button disabled={active.busy || savedBusy} onclick={() => action('run')}>Run <span class="shortcut">Cmd+Enter</span></Button><Button disabled={active.busy || savedBusy} onclick={() => action('check')}>Check <span class="shortcut">Shift+Cmd+Enter</span></Button><Button disabled={active.busy || savedBusy} onclick={requestSave}>Save</Button><Button disabled={active.busy || savedBusy} onclick={() => saveWorksheet()}>Save Worksheet</Button><Button class="editor-toggle" onclick={() => collapsed = !collapsed}>{collapsed ? 'Show editor' : 'Hide editor'}</Button></div>{#if active.error}<p class="error" role="alert">{active.error}</p>{/if}</section>
    <section class="results-panel" tabindex="-1"><div class="status-line"><span class="status-badge">{active.busy ? 'Working' : 'Ready'}</span>{#if active.check}<span class="notice">Valid: {active.check.row_count} rows, {active.check.column_count} columns.</span>{/if}</div>{#if active.result}<ResultsTable result={active.result} /><nav class="query-actions" aria-label="Result pages"><Button disabled={active.busy || active.result.offset === 0} onclick={() => page(Math.max(0, active.result!.offset - active.result!.page_size))}>Previous</Button><Button disabled={active.busy || !active.result.has_more} onclick={() => page(active.result!.offset + active.result!.rows.length)}>Next</Button></nav>{/if}</section>{/if}
  {#if storageError}<p class="error" role="alert">{storageError}</p>{/if}
</section></main>
<OpenSavedDialog open={openSavedDialog} busy={savedBusy} onopen={openSaved} onclose={() => openSavedDialog = false} />
<NameDialog open={nameDialog} title="Query name" onsubmit={(name) => { nameDialog = false; action('save', active?.cursor, name); }} onclose={() => nameDialog = false} />
<CommandPalette open={commandOpen} {commands} onclose={() => commandOpen = false} />
