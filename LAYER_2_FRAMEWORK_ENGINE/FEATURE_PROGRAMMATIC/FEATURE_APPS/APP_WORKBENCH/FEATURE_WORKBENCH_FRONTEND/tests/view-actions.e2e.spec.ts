// CA-E-683@6
import { expect, test, type Page } from '@playwright/test';

const url = process.env.WORKBENCH_E2E_URL!;
const projectRoot = new URL(url).searchParams.get('project_root');
const editor = (page: Page) => page.getByRole('textbox', { name: 'Query editor' });
const viewTabs = (page: Page) => page.locator('.tab-strip');
const executionOperations = new Set(['view_run', 'view_check', 'view_save', 'query_run', 'query_check']);

type WorkspaceView = { id: string; sql: string; name?: string; revision: number; cursor_position: number; result?: { query_id?: string | null } };
type WorkspaceState = { workspace_id: string; active_view_id: string; views: WorkspaceView[] };

function tab(page: Page, name: string | RegExp) {
  return viewTabs(page).getByRole('tab', { name, exact: typeof name === 'string' });
}

async function call(workspaceUrl: URL, operation: string, arguments_: Record<string, unknown>) {
  const endpoint = new URL(`${workspaceUrl.pathname.replace(/\/$/, '')}/interface`, workspaceUrl.origin);
  const response = await fetch(endpoint, {
    method: 'POST', headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ operation, arguments: arguments_, ...(projectRoot ? { project_root: projectRoot } : {}) }),
  });
  const body = await response.text();
  expect(response.ok, `${operation} failed: ${body}`).toBeTruthy();
  return JSON.parse(body) as Record<string, any>;
}

async function disposableWorkspace(prefix: string) {
  const workspace = `${prefix}-${Date.now()}-${Math.random().toString(36).slice(2)}`;
  const workspaceUrl = new URL(url);
  workspaceUrl.searchParams.set('workspace', workspace);
  const opened = await call(workspaceUrl, 'workspace_open', { session_id: workspace });
  return { workspace, workspaceUrl, opened: opened as WorkspaceState };
}

async function replaceSql(page: Page, sql: string) {
  const input = editor(page);
  await expect(input).toBeEditable();
  await input.click(); await input.press('Meta+A'); await input.pressSequentially(sql);
  await expect(input).toContainText(sql);
}

async function flushDraft(page: Page, sql: string) {
  const update = page.waitForRequest((request) => request.method() === 'POST'
    && new URL(request.url()).pathname.endsWith('/interface')
    && request.postDataJSON()?.operation === 'view_update'
    && request.postDataJSON()?.arguments?.sql === sql);
  await page.evaluate(() => window.dispatchEvent(new Event('focus')));
  await update;
}

async function saveCurrentView(page: Page, name: string) {
  await page.getByRole('button', { name: 'Run & Save', exact: true }).click();
  const dialog = page.getByRole('dialog', { name: 'Bookmark name' });
  await dialog.getByRole('textbox').fill(name);
  await dialog.getByRole('button', { name: 'Save', exact: true }).click();
  const link = page.locator('.saved-reference a');
  await expect(link).toBeVisible();
  return { id: (await link.textContent())!.trim(), href: (await link.getAttribute('href'))! };
}

async function paletteAction(page: Page, label: string) {
  await page.keyboard.press('Meta+P');
  const palette = page.getByRole('dialog', { name: 'Command palette' });
  await expect(palette).toBeVisible();
  const input = palette.getByRole('textbox');
  await input.fill(label); await input.press('Enter');
}

async function openSaved(page: Page, reference: string) {
  await paletteAction(page, 'Open Saved');
  const dialog = page.getByRole('dialog', { name: 'Open Bookmark or saved View' });
  await expect(dialog).toBeVisible();
  const input = dialog.getByRole('textbox');
  await input.fill(reference); await input.press('Enter');
  await expect(dialog).toBeHidden();
}

async function contextAction(page: Page, viewName: string | RegExp, action: string) {
  await tab(page, viewName).click({ button: 'right' });
  const menu = page.getByRole('menu');
  await expect(menu).toBeVisible();
  await menu.getByRole('menuitem', { name: action, exact: true }).click();
}

function observedOperations(page: Page) {
  const operations: string[] = [];
  page.on('request', (request) => {
    if (request.method() !== 'POST' || !new URL(request.url()).pathname.endsWith('/interface')) return;
    const operation = request.postDataJSON()?.operation;
    if (operation) operations.push(operation);
  });
  return operations;
}

async function state(workspaceUrl: URL, workspaceId: string) {
  return await call(workspaceUrl, 'workspace_get', { workspace_id: workspaceId }) as WorkspaceState;
}

test('reuses exact saved View identity without navigation or equal-SQL merging', async ({ page }) => {
  const fixture = await disposableWorkspace('saved-actions');
  const sourceId = fixture.opened.views[0].id;
  const sql = 'SELECT 11 AS retained_value';
  const operations = observedOperations(page);

  await page.goto(fixture.workspaceUrl.toString());
  await replaceSql(page, sql);
  const firstName = `First saved ${fixture.workspace}`;
  const first = await saveCurrentView(page, firstName);
  await page.getByRole('tab', { name: 'Bookmarks and saved Views', exact: true }).click();
  const savedItem = page.locator('.saved-item').filter({ has: page.locator('.saved-preview', { hasText: firstName }) });
  await expect(savedItem.locator('.saved-kind')).toHaveText('Bookmark');
  await tab(page, 'View 1').click();
  await page.getByRole('button', { name: 'New View', exact: true }).click();
  await expect(tab(page, 'View 2')).toHaveAttribute('aria-selected', 'true');
  await replaceSql(page, sql);
  const second = await saveCurrentView(page, 'Second saved');
  expect(second.id).not.toBe(first.id);
  const secondId = (await state(fixture.workspaceUrl, fixture.workspace)).views.find((view) => view.id !== sourceId)!.id;

  await tab(page, 'View 1').click();
  await expect(page.getByRole('grid')).toBeVisible();
  const seeded = await state(fixture.workspaceUrl, fixture.workspace);
  const retainedQueryId = seeded.views.find((view) => view.id === sourceId)!.result?.query_id;
  const draft = 'SELECT 12 AS unsaved_edit';
  await replaceSql(page, draft); await flushDraft(page, draft);
  await expect(page.getByRole('grid')).toContainText('retained_value');

  const countBefore = await viewTabs(page).getByRole('tab').count();
  const beforeUrl = page.url();
  await page.locator('.saved-reference a').click();
  expect(page.url()).toBe(beforeUrl);
  await expect(editor(page)).toContainText(draft);
  await expect(page.getByRole('grid')).toBeVisible();
  let current = await state(fixture.workspaceUrl, fixture.workspace);
  expect(current.views).toHaveLength(countBefore);
  expect(current.active_view_id).toBe(sourceId);
  expect(current.views.find((view) => view.id === sourceId)!.result?.query_id).toBe(retainedQueryId);

  await tab(page, 'View 2').click();
  operations.length = 0;
  await openSaved(page, first.id);
  current = await state(fixture.workspaceUrl, fixture.workspace);
  expect(current.active_view_id).toBe(sourceId);
  expect(current.views).toHaveLength(2);
  expect(operations).not.toContain('view_create');
  await expect(editor(page)).toContainText(draft);

  await tab(page, /View 2(?: \*)?/).click();
  operations.length = 0;
  await openSaved(page, new URL(second.href, page.url()).toString());
  current = await state(fixture.workspaceUrl, fixture.workspace);
  expect(current.active_view_id).toBe(secondId);
  expect(current.views).toHaveLength(2);
  expect(operations).not.toContain('view_create');

  await openSaved(page, first.id);
  await expect(page.locator('.saved-reference a')).toHaveText(first.id);
  await expect(editor(page)).toContainText(draft);
  await page.evaluate(() => window.dispatchEvent(new Event('pagehide')));
  await page.reload();
  await expect(tab(page, /View 1(?: \*)?/)).toHaveAttribute('aria-selected', 'true');
  await expect(page.locator('.saved-reference a')).toHaveText(first.id);
  await expect(editor(page)).toContainText(draft);
});

test('renames and duplicates Views from context and palette without copying results or saved identity', async ({ page }) => {
  const fixture = await disposableWorkspace('duplicate-actions');
  const sourceId = fixture.opened.views[0].id;
  const operations = observedOperations(page);

  await page.goto(fixture.workspaceUrl.toString());
  await replaceSql(page, 'SELECT 21 AS source_value');
  await saveCurrentView(page, 'Source saved');

  await paletteAction(page, 'Rename View');
  const rename = page.getByRole('dialog', { name: 'View name' });
  const renameInput = rename.getByRole('textbox');
  await expect(renameInput).toHaveValue('View 1');
  await renameInput.fill('Report'); await renameInput.press('Enter');
  await expect(tab(page, 'Report')).toBeVisible();

  await page.getByRole('button', { name: 'New View', exact: true }).click();
  await expect(tab(page, 'View 2')).toHaveAttribute('aria-selected', 'true');
  await tab(page, 'Report').click();
  await contextAction(page, 'View 2', 'Rename');
  const contextRename = page.getByRole('dialog', { name: 'View name' });
  await expect(contextRename.getByRole('textbox')).toHaveValue('View 2');
  await contextRename.getByRole('textbox').fill('Context Renamed');
  await contextRename.getByRole('textbox').press('Enter');
  await expect(tab(page, 'Context Renamed')).toBeVisible();
  await tab(page, 'Report').click();

  const editedSql = 'SELECT 22 AS copied_value';
  await replaceSql(page, editedSql); await flushDraft(page, editedSql);
  const source = (await state(fixture.workspaceUrl, fixture.workspace)).views.find((view) => view.id === sourceId)!;
  expect(source.result?.query_id).toBeTruthy();
  expect(source.cursor_position).toBeGreaterThan(0);
  const sourceQueryId = source.result!.query_id;
  operations.length = 0;
  await contextAction(page, /^Report(?: \*)?$/, 'Duplicate');
  await expect(tab(page, /^Report\(1\)(?: \*)?$/)).toHaveAttribute('aria-selected', 'true');
  let current = await state(fixture.workspaceUrl, fixture.workspace);
  const firstCopy = current.views.find((view) => view.name === 'Report(1)')!;
  const currentSource = current.views.find((view) => view.id === sourceId)!;
  expect(firstCopy.id).not.toBe(sourceId);
  expect(firstCopy.revision).toBe(0);
  expect(firstCopy.sql).toBe(currentSource.sql);
  expect(firstCopy.cursor_position).toBe(currentSource.cursor_position);
  expect(firstCopy.result).toBeUndefined();
  expect(currentSource.sql).toBe(editedSql);
  expect(currentSource.result?.query_id).toBe(sourceQueryId);
  expect(current.active_view_id).toBe(firstCopy.id);
  expect(current.views[current.views.findIndex((view) => view.id === sourceId) + 1].id).toBe(firstCopy.id);
  expect(operations).toContain('view_duplicate');
  expect(operations.filter((operation) => executionOperations.has(operation))).toEqual([]);
  await expect(page.getByRole('grid')).toHaveCount(0);
  await expect(page.locator('.saved-reference a')).toHaveCount(0);

  await tab(page, /^Report(?: \*)?$/).click();
  await expect(page.getByRole('grid')).toBeVisible();
  operations.length = 0;
  await paletteAction(page, 'Duplicate View');
  await expect(tab(page, /^Report\(2\)(?: \*)?$/)).toHaveAttribute('aria-selected', 'true');
  current = await state(fixture.workspaceUrl, fixture.workspace);
  const secondCopy = current.views.find((view) => view.name === 'Report(2)')!;
  expect(secondCopy.id).not.toBe(sourceId);
  expect(secondCopy.id).not.toBe(firstCopy.id);
  expect(secondCopy.revision).toBe(0);
  expect(secondCopy.sql).toBe(editedSql);
  expect(secondCopy.cursor_position).toBe(currentSource.cursor_position);
  expect(secondCopy.result).toBeUndefined();
  expect(current.active_view_id).toBe(secondCopy.id);
  expect(current.views[current.views.findIndex((view) => view.id === sourceId) + 1].id).toBe(secondCopy.id);
  expect(operations).toContain('view_duplicate');
  expect(operations.filter((operation) => executionOperations.has(operation))).toEqual([]);
  await expect(page.getByRole('grid')).toHaveCount(0);
  await expect(page.locator('.saved-reference a')).toHaveCount(0);

  await editor(page).press('Meta+Enter');
  await expect(page.getByRole('grid')).toBeVisible();
  current = await state(fixture.workspaceUrl, fixture.workspace);
  expect(current.views.find((view) => view.id === sourceId)!.result?.query_id).toBe(sourceQueryId);
  expect(current.views.find((view) => view.id === secondCopy.id)!.result?.query_id).not.toBe(sourceQueryId);

  await page.evaluate(() => window.dispatchEvent(new Event('pagehide')));
  await page.reload();
  await expect(tab(page, /^Report\(2\)(?: \*)?$/)).toHaveAttribute('aria-selected', 'true');
  await expect(page.getByRole('grid')).toBeVisible();
  await tab(page, /^Report(?: \*)?$/).click();
  await expect(editor(page)).toContainText(editedSql);
  await expect(page.locator('.saved-reference a')).toBeVisible();
  await expect(page.getByRole('grid')).toBeVisible();
});
