// @ts-nocheck
// CA-M-470@1
const empty = () => ({ id: crypto.randomUUID(), title: 'Worksheet', sql: '', cursor: 0, dirty: false });

export function newWorksheet(number) {
  return { ...empty(), title: `Worksheet ${number}` };
}

export function storageKey(projectName) {
  return `caprmedio.workbench.${projectName}.workspace`;
}

export function persistable(tabs, activeId) {
  return JSON.stringify({
    activeId,
    tabs: tabs.map(({ id, title, sql, cursor, dirty, savedSql }) => ({ id, title, sql, cursor, dirty, savedSql })),
  });
}

export function restore(raw) {
  try {
    const value = JSON.parse(raw);
    if (!Array.isArray(value.tabs) || !value.tabs.length) return null;
    const tabs = value.tabs.filter((tab) => typeof tab.id === 'string' && typeof tab.sql === 'string')
      .map((tab, index) => ({
        id: tab.id, title: typeof tab.title === 'string' ? tab.title : `Worksheet ${index + 1}`,
        sql: tab.sql, cursor: Number.isInteger(tab.cursor) ? tab.cursor : 0,
        dirty: Boolean(tab.dirty), savedSql: typeof tab.savedSql === 'string' ? tab.savedSql : undefined,
      }));
    return tabs.length ? { tabs, activeId: tabs.some((tab) => tab.id === value.activeId) ? value.activeId : tabs[0].id } : null;
  } catch { return null; }
}

export function cleanAfterSave(tab, savedSql) {
  return { ...tab, savedSql, dirty: tab.sql !== savedSql };
}
