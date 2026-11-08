// @ts-nocheck

const record = (value) => value !== null && typeof value === 'object' && !Array.isArray(value);

function invalid(message) {
  throw new Error('Legacy draft migration: ' + message);
}

function readReceipt(storage, key) {
  const raw = storage.getItem(key);
  if (raw === null) return {};
  let value;
  try { value = JSON.parse(raw); } catch { invalid('receipt ' + key + ' is not valid JSON'); }
  if (!record(value)) invalid('receipt ' + key + ' must be an object');
  const receipt = {};
  for (const [sourceId, entry] of Object.entries(value)) {
    if (!sourceId) invalid('receipt ' + key + ' has an invalid source-to-target entry');
    if (typeof entry === 'string' && entry) {
      // Compatibility with the original progress map: a string means fully acknowledged.
      receipt[sourceId] = { targetId: entry, updated: true };
      continue;
    }
    if (!record(entry) || typeof entry.targetId !== 'string' || !entry.targetId || typeof entry.updated !== 'boolean' || Object.keys(entry).some((keyName) => !['targetId', 'updated'].includes(keyName))) {
      invalid('receipt ' + key + ' has an invalid source-to-target entry');
    }
    receipt[sourceId] = { targetId: entry.targetId, updated: entry.updated };
  }
  return receipt;
}

function writeReceipt(storage, key, receipt) {
  const value = {};
  for (const [sourceId, entry] of Object.entries(receipt)) value[sourceId] = { targetId: entry.targetId, updated: entry.updated };
  storage.setItem(key, JSON.stringify(value));
}

function mapping(receipt) {
  return Object.fromEntries(Object.entries(receipt).map(([sourceId, entry]) => [sourceId, entry.targetId]));
}

function draftTabs(draft) {
  if (draft === null || draft === undefined) return [];
  if (!record(draft) || !Array.isArray(draft.tabs)) invalid('legacy draft is malformed');
  const ids = new Set();
  for (const tab of draft.tabs) {
    if (!record(tab) || typeof tab.id !== 'string' || !tab.id || ids.has(tab.id) || typeof tab.sql !== 'string' || !Number.isInteger(tab.cursor) || tab.cursor < 0) {
      invalid('legacy draft contains a malformed or duplicate tab');
    }
    if (tab.name !== undefined && typeof tab.name !== 'string') invalid('legacy draft contains a malformed View name');
    ids.add(tab.id);
  }
  if (draft.activeId !== undefined && draft.activeId !== null && (typeof draft.activeId !== 'string' || !ids.has(draft.activeId))) {
    invalid('legacy draft activeId is not one of its tabs');
  }
  return draft.tabs;
}

function assertState(state) {
  if (!record(state) || !Array.isArray(state.views)) invalid('Workspace state is malformed');
  for (const view of state.views) {
    if (!record(view) || typeof view.id !== 'string' || !view.id || !Number.isInteger(view.revision)) invalid('Workspace state contains an invalid View');
  }
}

function assertView(view, operation) {
  if (!record(view) || typeof view.id !== 'string' || !view.id || !Number.isInteger(view.revision)) invalid(operation + ' returned an invalid View');
}

function cloneState(state) {
  return { ...state, views: state.views.map((view) => ({ ...view })) };
}

function replaceView(state, view) {
  assertView(view, 'Workspace operation');
  const index = state.views.findIndex((item) => item.id === view.id);
  if (index < 0) invalid('Workspace operation returned unknown View ' + view.id);
  const views = state.views.slice();
  views[index] = { ...view };
  return { ...state, views };
}

function pristine(view) {
  return !view.name && typeof view.sql === 'string' && !view.sql.trim() && view.cursor_position === 0 && !view.result;
}

/**
 * Import a parsed legacy standalone draft into a bound Workspace exactly once.
 *
 * Contract:
 * - draft is the parsed result of the existing restore() helper; null means no draft.
 * - state is the current WorkspaceState from WorkspaceApi.open()/get().
 * - api supplies the existing create, rename, update and focus operations.
 * - storage supplies localStorage-compatible getItem/setItem; the legacy draft key is never written or removed.
 * - doneKey is compatible with the existing value done; progressKey accepts the original source-id to target-id string map and writes { targetId, updated } entries for pending/acknowledged imports.
 * - returns { state, sourceToTarget, completed, imported }; partial failures reject after acknowledged entries are persisted.
 *
 * @param {{
 *   draft: object|null,
 *   state: object,
 *   api: {create: Function, rename: Function, update: Function, focus: Function},
 *   storage: {getItem: Function, setItem: Function},
 *   doneKey: string,
 *   progressKey: string
 * }} input
 */
export async function migrateLegacyDraft({ draft, state, api, storage, doneKey, progressKey }) {
  assertState(state);
  if (!record(storage) || typeof storage.getItem !== 'function' || typeof storage.setItem !== 'function') invalid('storage is unavailable');
  if (!record(api) || typeof api.create !== 'function' || typeof api.rename !== 'function' || typeof api.update !== 'function' || typeof api.focus !== 'function') invalid('WorkspaceApi contract is incomplete');
  if (typeof doneKey !== 'string' || !doneKey || typeof progressKey !== 'string' || !progressKey) invalid('migration keys are missing');

  const tabs = draftTabs(draft);
  const sourceIds = new Set(tabs.map((tab) => tab.id));
  const receipt = readReceipt(storage, progressKey);
  const targetIds = new Set(state.views.map((view) => view.id));
  const acknowledgedTargets = new Set();
  for (const [sourceId, entry] of Object.entries(receipt)) {
    if (!sourceIds.has(sourceId)) invalid('receipt acknowledges unknown source Draft ' + sourceId);
    if (!targetIds.has(entry.targetId)) invalid('receipt points to missing target View ' + entry.targetId);
    if (acknowledgedTargets.has(entry.targetId)) invalid('receipt maps multiple source Drafts to View ' + entry.targetId);
    acknowledgedTargets.add(entry.targetId);
  }

  const marker = storage.getItem(doneKey);
  if (marker !== null && marker !== 'done') invalid('migration marker ' + doneKey + ' is malformed');
  const allAcknowledged = tabs.every((tab) => receipt[tab.id]?.updated === true);
  if (marker === 'done') {
    if (!allAcknowledged) invalid('done marker has unacknowledged source Drafts');
    return { state, sourceToTarget: mapping(receipt), completed: true, imported: false };
  }
  if (!tabs.length) return { state, sourceToTarget: mapping(receipt), completed: false, imported: false };

  let nextState = cloneState(state);
  let starter = nextState.views.length === 1 && pristine(nextState.views[0]) ? nextState.views[0] : undefined;
  if (starter && Object.values(receipt).some((entry) => entry.targetId === starter.id)) starter = undefined;
  let importedCount = 0;

  for (const source of tabs) {
    if (receipt[source.id]?.updated === true) continue;

    let target = receipt[source.id]
      ? nextState.views.find((view) => view.id === receipt[source.id].targetId)
      : starter;
    if (receipt[source.id] && !target) invalid('pending receipt target is missing from the current Workspace state');
    if (!target) {
      const created = await api.create('last', source.name || undefined);
      if (!record(created) || !Array.isArray(created.views) || typeof created.view_id !== 'string') invalid('view_create returned an invalid Workspace state');
      nextState = cloneState(created);
      target = nextState.views.find((view) => view.id === created.view_id);
      if (!target) invalid('view_create returned no created View');
      assertView(target, 'view_create');
      receipt[source.id] = { targetId: target.id, updated: false };
      writeReceipt(storage, progressKey, receipt);
    }
    starter = undefined;
    assertView(target, 'view_create');

    const sourceName = source.name || '';
    const targetName = target.name || '';
    if (targetName && targetName !== sourceName) invalid('pending target View has unrelated name changes');
    const blankTarget = typeof target.sql === 'string' && !target.sql.trim() && !target.result;
    if (!blankTarget && target.sql !== source.sql) invalid('pending target View has unrelated query changes');

    if (source.name && target.name !== source.name) {
      target = await api.rename(target.id, source.name);
      assertView(target, 'view_rename');
      nextState = replaceView(nextState, target);
    }

    if (target.sql !== source.sql || target.cursor_position !== source.cursor) {
      target = await api.update(target.id, source.sql, target.revision, source.cursor);
      assertView(target, 'view_update');
      nextState = replaceView(nextState, target);
    }

    receipt[source.id] = { targetId: target.id, updated: true };
    writeReceipt(storage, progressKey, receipt);
    importedCount += 1;
  }

  const sourceToTarget = mapping(receipt);
  const activeTarget = draft.activeId ? sourceToTarget[draft.activeId] : undefined;
  if (activeTarget) {
    const focused = await api.focus(activeTarget);
    if (!record(focused) || focused.active_view_id !== activeTarget) invalid('view_focus returned an invalid active View');
    nextState = { ...nextState, active_view_id: focused.active_view_id };
  }

  if (!tabs.every((tab) => receipt[tab.id]?.updated === true)) invalid('migration ended before all source Drafts were acknowledged');
  storage.setItem(doneKey, 'done');
  return { state: nextState, sourceToTarget, completed: true, imported: importedCount > 0 };
}

