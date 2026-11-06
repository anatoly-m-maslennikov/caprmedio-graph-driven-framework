// @ts-nocheck
// CA-M-470@8
const empty = () => ({ id: crypto.randomUUID(), title: 'View', sql: '', savedSql: '', cursor: 0, dirty: false });

export function newView(number) {
  return { ...empty(), title: `View ${number}` };
}

export function storageKey(projectName, workspaceId, projectRoot) {
  if (!workspaceId) return `caprmedio.workbench.${projectName}.workspace`;
  return `caprmedio.workbench.${projectRoot || projectName}.workspace.${workspaceId}`;
}

export function persistable(tabs, activeId) {
  return JSON.stringify({
    activeId,
    tabs: tabs.map(({ id, title, name, sql, cursor, dirty, syncDirty, savedSql, revision, saved }) => ({ id, title, ...(name ? { name } : {}), sql, cursor, dirty, syncDirty, savedSql, ...(Number.isInteger(revision) ? { revision } : {}), ...(saved ? { saved } : {}) })),
  });
}

function savedIdentity(value) {
  if (!value || typeof value !== 'object') return undefined;
  if (typeof value.saved_query_id !== 'string' || !value.saved_query_id || typeof value.saved_query_url !== 'string' || !value.saved_query_url || typeof value.sql !== 'string') return undefined;
  if (value.kind !== 'query' && value.kind !== 'view') return undefined;
  return { saved_query_id: value.saved_query_id, saved_query_url: value.saved_query_url, kind: value.kind, sql: value.sql, ...(typeof value.name === 'string' ? { name: value.name } : {}) };
}

export function restore(raw) {
  try {
    const value = JSON.parse(raw);
    if (!Array.isArray(value.tabs) || !value.tabs.length) return null;
    const tabs = value.tabs.filter((tab) => typeof tab.id === 'string' && typeof tab.sql === 'string')
      .map((tab, index) => ({
        id: tab.id, title: typeof tab.title === 'string' ? tab.title.replace(/^Worksheet( \d+)?$/, 'View$1') : `View ${index + 1}`,
        ...(typeof tab.name === 'string' && tab.name ? { name: tab.name } : {}),
        sql: tab.sql, cursor: Number.isInteger(tab.cursor) ? tab.cursor : 0,
        dirty: Boolean(tab.dirty), syncDirty: Boolean(tab.syncDirty ?? tab.dirty), savedSql: typeof tab.savedSql === 'string' ? tab.savedSql : undefined,
        ...(Number.isInteger(tab.revision) ? { revision: tab.revision } : {}), ...(savedIdentity(tab.saved) ? { saved: savedIdentity(tab.saved) } : {}),
      }));
    return tabs.length ? { tabs, activeId: tabs.some((tab) => tab.id === value.activeId) ? value.activeId : tabs[0].id } : null;
  } catch { return null; }
}

export function cleanAfterSave(tab, savedSql) {
  return { ...tab, savedSql, dirty: tab.sql !== savedSql };
}

export function workspaceTabs(state, previous = []) {
  const old = new Map(previous.map((tab) => [tab.id, tab]));
  const tabs = state.views.map((view, index) => {
    const local = old.get(view.id);
    const remote = {
      id: view.id, title: `View ${index + 1}`,
      ...(view.name ? { name: view.name } : {}), sql: view.sql, savedSql: view.sql,
      cursor: view.cursor_position, dirty: false, revision: view.revision, run: view.result,
    };
    const localAcknowledged = local?.sql === view.sql || (Number.isInteger(local?.revision) && local.revision >= view.revision);
    if (!local?.syncDirty) return {
      ...remote, busy: local?.busy, error: local?.error, check: local?.check, saved: local?.saved,
      ...(localAcknowledged ? { sql: local.sql, cursor: local.cursor, dirty: local.dirty, savedSql: local.savedSql, revision: Number.isInteger(local.revision) ? local.revision : view.revision, syncDirty: false } : {}),
      ...(local?.result && local.result.query_id === view.result?.query_id ? { result: local.result } : {}),
    };
    // Keep a draft on the old revision so the next update reports, rather than hides, a conflict.
    return { ...remote, ...local, serverSql: view.sql, serverRevision: view.revision };
  });
  return { tabs, activeId: state.active_view_id && tabs.some((tab) => tab.id === state.active_view_id) ? state.active_view_id : tabs[0]?.id };
}
