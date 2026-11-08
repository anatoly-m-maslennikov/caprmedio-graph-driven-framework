// CA-E-683@6
// CA-E-781@2
// CA-E-782@2
// CA-E-783@4
// CA-E-786@2
import { expect, test, type Page } from '@playwright/test';

const url = process.env.WORKBENCH_E2E_URL!;
const editor = (page: Page) => page.getByRole('textbox', { name: 'Query editor' });
const projectName = new URL(url).pathname.split('/').filter(Boolean).at(-1)!;

async function replaceSql(page: Page, sql: string) {
  const input = editor(page);
  await expect(input).toBeEditable();
  await input.click();
  await input.press('Meta+A');
  await input.pressSequentially(sql);
  await expect(input).toContainText(sql);
}
async function runSql(page: Page) { await editor(page).press('Meta+Enter'); }

async function sharedWorkspace() {
  const workspace = `browser-${Date.now()}`;
  const workspaceUrl = new URL(url);
  workspaceUrl.searchParams.set('workspace', workspace);
  const endpoint = new URL(`${workspaceUrl.pathname.replace(/\/$/, '')}/interface`, workspaceUrl.origin).toString();
  const projectRoot = workspaceUrl.searchParams.get('project_root');
  const call = async (operation: string, arguments_: Record<string, unknown>) => {
    const response = await fetch(endpoint, {
      method: 'POST', headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ operation, arguments: arguments_, ...(projectRoot ? { project_root: projectRoot } : {}) }),
    });
    expect(response.ok, `${operation} failed`).toBeTruthy();
    return response.json() as Promise<Record<string, any>>;
  };
  const opened = await call('workspace_open', { session_id: workspace });
  const created = await call('view_create', { workspace_id: workspace, position: 'last', name: 'External View' });
  const externalId = created.view_id as string;
  const external = created.views.find((item: { id: string }) => item.id === externalId);
  const updated = await call('view_update', { workspace_id: workspace, view_id: externalId, sql: 'SELECT 42 AS external_value', expected_revision: external.revision, cursor_position: 0 });
  await call('view_focus', { workspace_id: workspace, view_id: externalId });
  await call('view_run', { workspace_id: workspace, view_id: externalId, cursor_position: 0 });
  return { externalId, revision: updated.revision as number, workspaceUrl: workspaceUrl.toString(), call };
}

async function persistedAdaptiveWorkspace() {
  const workspace = `cached-grid-${Date.now()}`;
  const workspaceUrl = new URL(url); workspaceUrl.searchParams.set('workspace', workspace);
  const endpoint = new URL(`${workspaceUrl.pathname.replace(/\/$/, '')}/interface`, workspaceUrl.origin).toString();
  const projectRoot = workspaceUrl.searchParams.get('project_root');
  const call = async (operation: string, arguments_: Record<string, unknown>) => {
    const response = await fetch(endpoint, {
      method: 'POST', headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ operation, arguments: arguments_, ...(projectRoot ? { project_root: projectRoot } : {}) }),
    });
    expect(response.ok, `${operation} failed`).toBeTruthy();
    return response.json() as Promise<Record<string, any>>;
  };
  const opened = await call('workspace_open', { session_id: workspace }); const view = opened.views[0];
  await call('view_update', {
    workspace_id: workspace, view_id: view.id,
    sql: "SELECT i AS row_id, CASE WHEN i % 2 = 0 THEN 'alpha' ELSE 'beta' END AS group_name, 20 - i AS sort_value, NULL::VARCHAR AS empty_column FROM range(0, 20) AS rows(i)",
    expected_revision: view.revision, cursor_position: 0,
  });
  await call('view_run', { workspace_id: workspace, view_id: view.id, cursor_position: 0 });
  return workspaceUrl.toString();
}

test('binds two browser contexts to one Workspace and observes external state', async ({ browser }) => {
  const setup = await sharedWorkspace();
  const firstContext = await browser.newContext();
  const secondContext = await browser.newContext();
  const firstPage = await firstContext.newPage();
  const secondPage = await secondContext.newPage();
  let releaseUpdate: (() => void) | undefined;
  try {
    await test.step('open both contexts with the externally focused View', async () => {
      await Promise.all([firstPage.goto(setup.workspaceUrl), secondPage.goto(setup.workspaceUrl)]);
      const external = firstPage.getByRole('tab', { name: 'External View', exact: true });
      await expect(external).toBeVisible({ timeout: 12_000 });
      await expect(external).toHaveAttribute('aria-selected', 'true');
      await expect(firstPage.getByRole('textbox', { name: 'Query editor' })).toContainText('SELECT 42 AS external_value');
      await expect(firstPage.getByRole('grid')).toBeVisible({ timeout: 12_000 });
      await expect(firstPage.getByRole('columnheader').first()).toHaveText(/external_value\s*INTEGER/);
      await expect(secondPage.getByRole('tab', { name: 'External View', exact: true })).toHaveAttribute('aria-selected', 'true', { timeout: 12_000 });
    });
    let updateStarted!: () => void;
    const held = new Promise<void>((resolve) => releaseUpdate = resolve);
    const started = new Promise<void>((resolve) => updateStarted = resolve);
    let delayed = false;
    await test.step('hold the first foreground autosave', async () => {
      await secondPage.route('**/interface', async (route) => {
        const request = route.request().postDataJSON() as { operation?: string; arguments?: { view_id?: string; sql?: string } };
        if (!delayed && request.operation === 'view_update' && request.arguments?.view_id === setup.externalId && request.arguments.sql === 'SELECT 1 AS first_draft') {
          delayed = true;
          const response = await route.fetch();
          updateStarted(); await held;
          await route.fulfill({ response });
          return;
        }
        await route.continue();
      });
      await secondPage.bringToFront();
      await secondPage.evaluate(() => new Promise<void>((resolve) => requestAnimationFrame(() => resolve())));
      await expect(editor(secondPage)).toBeEditable();
      await replaceSql(secondPage, 'SELECT 1 AS first_draft');
      await expect(editor(secondPage)).toContainText('SELECT 1 AS first_draft');
      await firstPage.bringToFront();
      await secondPage.bringToFront();
      await started;
    });
    await test.step('run the draft edited while the first autosave is held', async () => {
      await replaceSql(secondPage, 'SELECT 2 AS latest_draft');
      const run = runSql(secondPage);
      releaseUpdate?.();
      await run;
      await expect(editor(secondPage)).toContainText('SELECT 2 AS latest_draft');
      await expect(secondPage.getByRole('grid')).toBeVisible({ timeout: 12_000 });
      await expect(secondPage.getByRole('columnheader').first()).toHaveText(/latest_draft\s*INTEGER/);
    });
  } finally {
    releaseUpdate?.();
    await Promise.all([firstContext.close(), secondContext.close()]);
  }
});
test('waits for the initial Workspace binding before accepting SQL input', async ({ page }) => {
  let releaseOpen!: () => void;
  let opened!: () => void;
  const held = new Promise<void>((resolve) => releaseOpen = resolve);
  const openStarted = new Promise<void>((resolve) => opened = resolve);
  await page.route('**/interface', async (route) => {
    const request = route.request().postDataJSON() as { operation?: string };
    if (request.operation === 'workspace_open') {
      const response = await route.fetch();
      opened(); await held;
      await route.fulfill({ response });
      return;
    }
    await route.continue();
  });
  try {
    await page.goto(url); await openStarted;
    await expect(editor(page)).toHaveAttribute('contenteditable', 'false');
    await expect(page.getByRole('button', { name: 'Run Cmd+Enter' })).toBeDisabled();
    releaseOpen();
    await expect(editor(page)).toBeEditable();
    await replaceSql(page, 'SELECT 31 AS bound_input');
    const run = page.waitForRequest((request) => request.method() === 'POST' && request.postDataJSON()?.operation === 'view_run');
    await runSql(page); await run;
    await expect(page.getByRole('grid')).toBeVisible();
  } finally { releaseOpen?.(); }
});
test('opens, leaves, and rebuilds a cached adaptive result without an uncaught Tabulator lifecycle error', async ({ page }) => {
  const workspaceUrl = await persistedAdaptiveWorkspace(); const errors: string[] = [];
  page.on('pageerror', (error) => errors.push(error.message));
  const fetched = page.waitForResponse((response) => response.request().method() === 'POST'
    && response.request().postDataJSON()?.operation === 'view_fetch' && response.status() === 200);
  await page.goto(workspaceUrl); await fetched;
  await expect(page.getByRole('grid')).toBeVisible();
  await expect(page.locator('.result-summary')).toContainText('20 rows, 3 of 4 columns');
  await page.getByRole('tab', { name: 'Settings', exact: true }).click();
  await expect(page.getByRole('region', { name: 'Settings' })).toBeVisible();
  await page.getByRole('tab', { name: 'View 1', exact: true }).click();
  await expect(page.getByRole('grid')).toBeVisible();
  await page.evaluate(() => new Promise<void>((resolve) => requestAnimationFrame(() => requestAnimationFrame(() => resolve()))));
  expect(errors).toEqual([]);
});

test('keeps dirty SQL through Run and Check under the Project Workbench header', async ({ page }) => {
  await page.goto(url);
  const layout = await page.locator('.workspace').evaluate((node) => ({ width: node.getBoundingClientRect().width, viewport: innerWidth }));
  expect(layout.width).toBeGreaterThan(layout.viewport * 0.9);
  const header = page.locator('header');
  await expect(header.getByText('Workbench', { exact: true })).toBeVisible();
  await expect(header.getByText(`Project: ${projectName}`, { exact: true })).toBeVisible();
  await expect(header.getByRole('tab', { name: 'Settings', exact: true })).toBeVisible();
  await expect(header.getByRole('tab', { name: 'Saved Queries and Views' })).toBeVisible();
  await expect(page.getByText('Query editor', { exact: true })).toBeVisible();
  await replaceSql(page, 'SELECT reference FROM atoms ORDER BY reference LIMIT 1');
  await runSql(page);
  await expect(page.getByRole('grid')).toBeVisible();
  await expect(page.getByRole('grid').getByRole('row')).toHaveCount(2);
  await expect(page.getByRole('columnheader').first()).toHaveText(/reference\s*VARCHAR/);
  await page.getByRole('button', { name: /^Check/ }).click();
  await expect(page.getByText('Valid: 1 rows, 1 columns.')).toBeVisible();
  await expect(page.getByRole('tab', { name: /^View 1 \*/ })).toBeVisible();
  await page.getByRole('button', { name: 'Run & Save', exact: true }).click();
  const queryName = page.getByRole('dialog', { name: 'Query name' }).getByRole('textbox');
  await queryName.fill('E2E query');
  await queryName.press('Enter');
  await expect(page.locator('.panel-heading').getByText(/^Saved:/)).toBeVisible();
  await expect(editor(page)).toContainText('SELECT reference FROM atoms ORDER BY reference LIMIT 1');
  await expect(page.getByRole('tab', { name: 'View 1', exact: true })).toBeVisible();
});

test('restores local View state and opens a saved View without running it', async ({ page }) => {
  await page.goto(url);
  const view = page.getByRole('tab', { name: 'View 1', exact: true });
  await view.dblclick();
  const renameDialog = page.getByRole('dialog', { name: 'View name' });
  const title = renameDialog.getByRole('textbox');
  await expect(title).toHaveValue('View 1');
  await renameDialog.getByRole('button', { name: 'Cancel' }).click();
  await expect(view).toBeVisible();
  await view.dblclick();
  await page.keyboard.press('Escape');
  await expect(renameDialog).toHaveCount(0);
  await expect(view).toBeVisible();
  await page.keyboard.press('Meta+P');
  const palette = page.getByRole('dialog', { name: 'Command palette' });
  const paletteInput = palette.getByRole('textbox');
  await paletteInput.fill('Rename View');
  await expect(palette.getByRole('button', { name: 'Rename View', exact: true })).toBeEnabled();
  await paletteInput.press('Enter');
  await expect(title).toHaveValue('View 1');
  await expect(title).toBeFocused();
  await title.fill('E2E View');
  await title.press('Enter');
  await replaceSql(page, "SELECT 'saved worksheet'");
  await page.waitForTimeout(5200);
  const restored = await page.context().newPage();
  await restored.goto(url);
  await expect(restored.getByRole('tab', { name: /E2E View/ })).toBeVisible();
  await expect(editor(restored)).toContainText("SELECT 'saved worksheet'");
  await restored.close();
  await page.getByRole('button', { name: 'Save View', exact: true }).click();
  const queryHeader = page.locator('.panel-heading');
  await expect(queryHeader.getByText('Query editor', { exact: true })).toBeVisible();
  await expect(queryHeader.getByText(/^Saved:/)).toBeVisible();
  const saved = queryHeader.getByRole('link');
  await expect(saved).toBeVisible();
  const href = await saved.getAttribute('href');
  expect(href).toContain('?query=');
  const id = new URL(href!, url).searchParams.get('query');
  let executionRequests = 0;
  page.on('request', (request) => {
    if (request.method() === 'POST' && /\/(run|check)$/.test(new URL(request.url()).pathname)) executionRequests += 1;
  });
  await expect(page.getByRole('button', { name: 'Open Saved', exact: true })).toHaveCount(0);
  await page.keyboard.press('Meta+P');
  await page.getByRole('dialog', { name: 'Command palette' }).getByRole('textbox').fill('Open Saved');
  await page.keyboard.press('Enter');
  const referenceInput = page.getByRole('dialog', { name: 'Open saved query or View' }).getByRole('textbox');
  await expect(referenceInput).toBeFocused();
  await referenceInput.fill(id!);
  await page.keyboard.press('Enter');
  await expect(editor(page)).toContainText("SELECT 'saved worksheet'");
  await expect(page.getByRole('grid')).toHaveCount(0);
  expect(executionRequests).toBe(0);
});

test('shows source indexing status in local time and keeps settings independent', async ({ browser }) => {
  const standalone = await browser.newContext();
  const page = await standalone.newPage();
  try {
    const statusResponse = page.waitForResponse((response) => response.request().method() === 'POST' && new URL(response.url()).pathname.endsWith('/status') && response.status() === 200);
    await page.goto(url);
    const status = await (await statusResponse).json() as { syncing: boolean; last_synced_at: string | null };
    expect(Object.keys(status).sort()).toEqual(['last_synced_at', 'syncing']);
    const localTime = status.last_synced_at && await page.evaluate((timestamp) => new Date(timestamp).toLocaleString(), status.last_synced_at);
    await expect(page.getByRole('status', { name: 'Source indexing status' })).toHaveText(status.syncing ? 'Source index: Syncing' : localTime ? `Source index: ${localTime}` : 'Source index: Not synced yet');
    await expect.poll(() => page.evaluate(() => ({ theme: document.documentElement.dataset.theme, density: document.documentElement.dataset.density, interfaceText: getComputedStyle(document.documentElement).getPropertyValue('--interface-text-scale').trim(), contentText: getComputedStyle(document.documentElement).getPropertyValue('--content-text-scale').trim(), interface: getComputedStyle(document.documentElement).getPropertyValue('--interface-scale').trim() }))).toEqual({ theme: 'system', density: 'comfortable', interfaceText: '1', contentText: '1', interface: '1' });

    await page.getByRole('tab', { name: 'Settings', exact: true }).click();
    const settings = page.getByRole('region', { name: 'Settings' });
    await expect(settings.getByLabel('Theme')).toHaveValue('system');
    await expect(settings.getByLabel('Interface text zoom')).toHaveValue('100');
    await expect(settings.getByLabel('Content text zoom')).toHaveValue('100');
    await expect(settings.getByLabel('Interface zoom')).toHaveValue('100');
    await expect(settings.getByLabel('Density')).toHaveValue('comfortable');
    const y = await Promise.all(['Theme', 'Interface text zoom', 'Content text zoom', 'Interface zoom', 'Density'].map(async (name) => (await settings.getByLabel(name).boundingBox())?.y));
    expect(y[0]).toBeLessThan(y[1]!); expect(y[1]).toBeLessThan(y[2]!); expect(y[2]).toBeLessThan(y[3]!); expect(y[3]).toBeLessThan(y[4]!);

    await page.keyboard.press('Meta+P');
    const palette = page.getByRole('dialog', { name: 'Command palette' });
    await palette.getByRole('textbox').fill('Interface text zoom: 125%');
    await page.keyboard.press('Enter');
    await expect.poll(() => page.evaluate(() => getComputedStyle(document.documentElement).getPropertyValue('--interface-text-scale').trim())).toBe('1.25');
    await expect(palette).toBeHidden();
    await page.keyboard.press('Meta+P');
    await page.getByRole('dialog', { name: 'Command palette' }).getByRole('textbox').fill('Content text zoom: 150%');
    await page.keyboard.press('Enter');
    await expect.poll(() => page.evaluate(() => getComputedStyle(document.documentElement).getPropertyValue('--content-text-scale').trim())).toBe('1.5');
    await expect(palette).toBeHidden();
    await page.getByLabel('Interface zoom').selectOption('90');
    await page.getByLabel('Density').selectOption('compact');
    await expect.poll(() => page.evaluate(() => ({ density: document.documentElement.dataset.density, interface: getComputedStyle(document.documentElement).getPropertyValue('--interface-scale').trim() }))).toEqual({ density: 'compact', interface: '0.9' });
    await page.reload();
    await page.getByRole('tab', { name: 'Settings', exact: true }).click();
    await expect(page.getByLabel('Interface text zoom')).toHaveValue('125');
    await expect(page.getByLabel('Content text zoom')).toHaveValue('150');
    await expect(page.getByLabel('Interface zoom')).toHaveValue('90');
    await expect(page.getByLabel('Density')).toHaveValue('compact');
  } finally { await standalone.close(); }

  const embedded = await browser.newContext();
  const embeddedPage = await embedded.newPage();
  try {
    const embeddedUrl = new URL(url); embeddedUrl.searchParams.set('embedded', '1');
    await embeddedPage.goto(embeddedUrl.toString());
    await expect.poll(() => embeddedPage.evaluate(() => document.documentElement.dataset.density)).toBe('compact');
  } finally { await embedded.close(); }
});

test('scales interface and query content text independently', async ({ page }) => {
  await page.goto(url);
  const sizes = () => page.evaluate(() => ({
    title: Number.parseFloat(getComputedStyle(document.querySelector('.app-name')!).fontSize),
    editor: Number.parseFloat(getComputedStyle(document.querySelector('.cm-content')!).fontSize),
  }));
  const initial = await sizes();
  await page.getByRole('tab', { name: 'Settings', exact: true }).click();
  await page.getByLabel('Interface text zoom').selectOption('125');
  await page.getByRole('tab', { name: /^View 1/ }).click();
  const interfaceZoomed = await sizes();
  expect(interfaceZoomed.title).toBeGreaterThan(initial.title);
  expect(interfaceZoomed.editor).toBe(initial.editor);
  await page.getByRole('tab', { name: 'Settings', exact: true }).click();
  await page.getByLabel('Content text zoom').selectOption('150');
  await page.getByRole('tab', { name: /^View 1/ }).click();
  const contentZoomed = await sizes();
  expect(contentZoomed.title).toBe(interfaceZoomed.title);
  expect(contentZoomed.editor).toBeGreaterThan(interfaceZoomed.editor);
});

test('migrates one standalone draft without running it and keeps close protection after sync', async ({ browser }) => {
  const context = await browser.newContext(); const page = await context.newPage();
  const parsed = new URL(url); const root = parsed.searchParams.get('project_root') ?? projectName;
  const legacyKey = `caprmedio.workbench.${root}.workspace`;
  await page.addInitScript(({ key }) => localStorage.setItem(key, JSON.stringify({ activeId: 'legacy', tabs: [{ id: 'legacy', title: 'View 1', sql: 'SELECT 41 AS migrated_draft', cursor: 0, dirty: true, savedSql: '' }] })), { key: legacyKey });
  let runs = 0; const opened: string[] = [];
  page.on('request', (request) => {
    if (request.method() !== 'POST' || !new URL(request.url()).pathname.endsWith('/interface')) return;
    const payload = request.postDataJSON(); if (payload?.operation === 'view_run') runs += 1;
    if (payload?.operation === 'workspace_open') opened.push(payload.arguments?.session_id);
  });
  try {
    await page.goto(url);
    await expect(editor(page)).toContainText('SELECT 41 AS migrated_draft');
    expect(new URL(page.url()).searchParams.get('workspace')).toBeNull();
    const session = await page.evaluate(() => Object.entries(localStorage).find(([key]) => key.endsWith('.standalone-session'))?.[1]);
    expect(session).toMatch(/^standalone-/); expect(opened).toEqual([session]); expect(runs).toBe(0);
    await page.reload(); await expect(editor(page)).toContainText('SELECT 41 AS migrated_draft');
    expect(new URL(page.url()).searchParams.get('workspace')).toBeNull(); await expect.poll(() => opened).toEqual([session, session]);

    const update = page.waitForRequest((request) => request.method() === 'POST' && new URL(request.url()).pathname.endsWith('/interface') && request.postDataJSON()?.operation === 'view_update' && request.postDataJSON()?.arguments?.sql === 'SELECT 42 AS autosaved_draft');
    await replaceSql(page, 'SELECT 42 AS autosaved_draft'); await update;
    const close = page.locator('button[aria-label^="Close "]').first();
    let message = ''; page.once('dialog', (dialog) => { message = dialog.message(); void dialog.dismiss(); });
    await close.click(); expect(message).toContain('Close unsaved');
    await expect(editor(page)).toContainText('SELECT 42 AS autosaved_draft'); expect(runs).toBe(0);
  } finally { await context.close(); }
});

test('resumes a partial standalone migration without overwriting existing Views or duplicate acknowledgements', async ({ browser }) => {
  const context = await browser.newContext(); const page = await context.newPage(); const workspace = `standalone-existing-${Date.now()}`;
  const parsed = new URL(url); const endpoint = new URL(`${parsed.pathname.replace(/\/$/, '')}/interface`, parsed.origin).toString(); const root = parsed.searchParams.get('project_root') ?? projectName;
  const call = async (operation: string, arguments_: Record<string, unknown>) => {
    const response = await fetch(endpoint, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ operation, arguments: arguments_, ...(parsed.searchParams.get('project_root') ? { project_root: parsed.searchParams.get('project_root') } : {}) }) });
    expect(response.ok, `${operation} failed`).toBeTruthy(); return response.json() as Promise<Record<string, any>>;
  };
  const opened = await call('workspace_open', { session_id: workspace }); const initial = opened.views[0];
  await call('view_update', { workspace_id: workspace, view_id: initial.id, sql: 'SELECT 7 AS existing_view', expected_revision: initial.revision, cursor_position: 0 });
  const legacyKey = `caprmedio.workbench.${root}.workspace`; const sessionKey = `caprmedio.workbench.${root}.standalone-session`;
  const legacy = JSON.stringify({ activeId: 'second', tabs: [
    { id: 'first', title: 'View 1', sql: 'SELECT 8 AS imported_once', cursor: 0, dirty: true, savedSql: '' },
    { id: 'second', title: 'View 2', sql: 'SELECT 9 AS resumed_import', cursor: 0, dirty: true, savedSql: '' },
  ] });
  await page.addInitScript(({ draftKey, sessionKey: key, session, draft }) => { localStorage.setItem(key, session); localStorage.setItem(draftKey, draft); }, { draftKey: legacyKey, sessionKey, session: workspace, draft: legacy });
  let failSecond = true;
  await page.route('**/interface', async (route) => {
    const request = route.request().postDataJSON() as { operation?: string; arguments?: { sql?: string } };
    if (failSecond && request.operation === 'view_update' && request.arguments?.sql === 'SELECT 9 AS resumed_import') return route.fulfill({ status: 500, contentType: 'application/json', body: '{"error":"temporary import failure"}' });
    await route.continue();
  });
  try {
    await page.goto(url); await expect(page.getByRole('alert')).toContainText('temporary import failure');
    let state = await call('workspace_get', { workspace_id: workspace });
    expect(state.views.filter((item: { sql: string }) => item.sql === 'SELECT 7 AS existing_view')).toHaveLength(1);
    expect(state.views.filter((item: { sql: string }) => item.sql === 'SELECT 8 AS imported_once')).toHaveLength(1);
    failSecond = false; await page.reload(); await expect(editor(page)).toContainText('SELECT 9 AS resumed_import');
    state = await call('workspace_get', { workspace_id: workspace });
    expect(state.views.filter((item: { sql: string }) => item.sql === 'SELECT 7 AS existing_view')).toHaveLength(1);
    expect(state.views.filter((item: { sql: string }) => item.sql === 'SELECT 8 AS imported_once')).toHaveLength(1);
    expect(state.views.filter((item: { sql: string }) => item.sql === 'SELECT 9 AS resumed_import')).toHaveLength(1);
    expect(state.views).toHaveLength(3);
    await expect.poll(() => page.evaluate((key) => localStorage.getItem(key), legacyKey)).toBe(legacy);
  } finally { await context.close(); }
});

test('uses persisted adaptive or fixed display and global grid actions without rerunning SQL', async ({ browser }) => {
  const context = await browser.newContext(); const page = await context.newPage(); let runs = 0;
  page.on('request', (request) => { if (request.method() === 'POST' && new URL(request.url()).pathname.endsWith('/interface') && request.postDataJSON()?.operation === 'view_run') runs += 1; });
  try {
    await page.goto(url);
    await replaceSql(page, "SELECT i AS ordinal, repeat('😀', 151) AS long_value FROM range(0, 220) AS t(i)");
    await runSql(page);
    await expect(page.getByRole('grid')).toBeVisible(); await expect(page.getByLabel('Result cell content')).toHaveValue('limited');
    expect(runs).toBe(1);
    await page.getByRole('tab', { name: 'Settings', exact: true }).click();
    await expect(page.getByRole('radio', { name: 'Adaptive' })).toBeChecked();
    await expect(page.getByRole('radio', { name: 'Limited' })).toBeChecked();
    await expect(page.getByLabel('Fixed rows per page')).toHaveCount(0);
    await page.getByRole('radio', { name: 'Fixed' }).check();
    const rows = page.getByLabel('Fixed rows per page'); await expect(rows).toHaveValue('100');
    const fixedPage = page.waitForRequest((request) => request.method() === 'POST' && request.postDataJSON()?.operation === 'view_fetch' && request.postDataJSON()?.arguments?.page_size === 25);
    await rows.fill('25'); await fixedPage;
    await page.getByRole('tab', { name: /^View 1/ }).click();
    await expect(page.locator('.result-summary')).toContainText('220 rows');
    await expect(page.getByRole('navigation', { name: 'Result pages' })).toBeInViewport();
    await page.getByRole('tab', { name: 'Settings', exact: true }).click();
    await page.getByRole('radio', { name: 'Adaptive' }).check(); await expect(rows).toHaveCount(0);
    await page.getByRole('tab', { name: /^View 1/ }).click();
    await page.getByLabel('Result cell content').selectOption('full');
    await expect(page.getByLabel('Inline content character limit')).toHaveCount(0);
    expect(runs).toBe(1);

    const cell = page.locator('.tabulator-row .tabulator-cell').nth(1);
    await cell.click({ button: 'right' });
    await expect(page.locator('.tabulator-menu-item')).toHaveText(['Cell Copy value', 'Cell Show full value', 'Row Copy row']);
    await page.getByText('Cell Copy value', { exact: true }).click();
    const header = page.getByRole('columnheader').first(); await header.click({ button: 'right' });
    await expect(page.locator('.tabulator-menu-item')).toHaveText(['Column Sort ascending', 'Column Sort descending', 'Group by', 'Filter', 'Clear filter']);
    const sort = page.waitForRequest((request) => request.method() === 'POST' && request.postDataJSON()?.operation === 'view_fetch' && request.postDataJSON()?.arguments?.grid?.sort?.[0]?.direction === 'desc');
    await page.getByText('Column Sort descending', { exact: true }).click(); await sort;
    expect(runs).toBe(1);
    await page.reload(); await page.getByRole('tab', { name: 'Settings', exact: true }).click();
    await expect(page.getByRole('radio', { name: 'Adaptive' })).toBeChecked(); await expect(page.getByRole('radio', { name: 'Full' })).toBeChecked();
  } finally { await context.close(); }
});

test('keeps NULL and text null group counts distinct', async ({ page }) => {
  await page.goto(url);
  await replaceSql(page, "SELECT CASE WHEN i < 2 THEN NULL::VARCHAR ELSE 'null' END AS marker FROM range(0, 5) AS t(i)");
  await runSql(page); await expect(page.getByRole('grid')).toBeVisible();
  const grouped = page.waitForRequest((request) => request.method() === 'POST' && request.postDataJSON()?.operation === 'view_fetch' && request.postDataJSON()?.arguments?.grid?.group_by?.column === 0);
  await page.getByRole('columnheader').first().click({ button: 'right' });
  await page.getByText('Group by', { exact: true }).click(); await grouped;
  await expect(page.locator('.tabulator-group').filter({ hasText: 'marker: NULL (2)' })).toHaveCount(1);
  await expect(page.locator('.tabulator-group').filter({ hasText: 'marker: null (3)' })).toHaveCount(1);
});

test('uses palette navigation, quoted status completion, and focus after hiding the editor', async ({ page }) => {
  const schemaResponse = page.waitForResponse((response) => (
    response.request().method() === 'POST'
    && new URL(response.url()).pathname.endsWith('/schema')
    && response.status() === 200
  ));
  await page.goto(url);
  const schema = await (await schemaResponse).json() as {
    tables: { atoms: Array<{ name: string; values?: string[] }> };
  };
  expect(schema.tables.atoms.find((column) => column.name === 'header.state.status')?.values).toContain('Active');
  await page.keyboard.press('Meta+P');
  const palette = page.getByRole('dialog', { name: 'Command palette' });
  await expect(palette.getByRole('textbox')).toBeFocused();
  await page.keyboard.press('Control+N');
  await page.keyboard.press('Enter');
  await expect(palette).toBeHidden();
  await expect(page.getByRole('region', { name: 'Saved Queries and Views' })).toBeVisible();
  await page.keyboard.press('Meta+P');
  await expect(palette).toBeVisible();
  await expect(palette.getByRole('textbox')).toBeFocused();
  await page.keyboard.press('Control+N');
  await page.keyboard.press('Control+P');
  await page.keyboard.press('Enter');
  await expect(palette).toBeHidden();
  await expect(page.getByRole('region', { name: 'Settings' })).toBeVisible();
  await page.getByRole('tab', { name: /^View 1/ }).click();
  await replaceSql(page, "SELECT \"header.state.status\" FROM atoms WHERE \"header.state.status\" = 'Act'");
  await page.keyboard.press('ArrowLeft');
  await page.keyboard.press('Control+Space');
  const active = page.getByRole('option', { name: 'Active', exact: true });
  await expect(active).toBeVisible();
  await active.click();
  await expect(editor(page)).toContainText("header.state.status\" = 'Active'");
  const editorToggle = page.getByRole('button', { name: /Query editor.*Hide editor/ });
  await expect(editorToggle).toHaveAttribute('aria-expanded', 'true');
  await editorToggle.click();
  await expect(page.getByRole('button', { name: /Query editor.*Show editor/ })).toHaveAttribute('aria-expanded', 'false');
  await page.keyboard.press('Meta+P');
  await expect(palette).toBeVisible();
  await expect(palette.getByRole('textbox')).toBeFocused();
  await palette.getByRole('textbox').fill('Focus Query editor');
  await page.keyboard.press('Enter');
  await expect(editor(page)).toBeFocused();
});
