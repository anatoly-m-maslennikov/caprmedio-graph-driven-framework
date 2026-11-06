// CA-E-683@4
import { expect, test, type Page } from '@playwright/test';

const url = process.env.WORKBENCH_E2E_URL!;
const editor = (page: Page) => page.getByRole('textbox', { name: 'Query editor' });
const executionOperations = new Set(['view_run', 'view_check', 'view_save', 'query_run', 'query_check']);
const editorSource = (page: Page) => page.locator('.cm-line').evaluateAll((lines) => lines.map((line) => line.textContent ?? '').join('\n'));

async function replaceSql(page: Page, sql: string) {
  const input = editor(page);
  await expect(input).toBeEditable();
  await input.click();
  await input.press('Meta+A');
  await input.pressSequentially(sql);
  await expect(input).toContainText(sql);
}

function observedOperations(page: Page) {
  const operations: string[] = [];
  page.on('request', (request) => {
    if (request.method() === 'POST' && new URL(request.url()).pathname.endsWith('/interface')) {
      const payload = request.postDataJSON() as { operation?: string };
      if (payload.operation) operations.push(payload.operation);
    }
  });
  return operations;
}

async function seededWorkspace(sql: string) {
  const workspaceUrl = new URL(url); workspaceUrl.searchParams.set('workspace', `formatter-${Date.now()}`);
  const endpoint = new URL(`${workspaceUrl.pathname.replace(/\/$/, '')}/interface`, workspaceUrl.origin);
  const projectRoot = workspaceUrl.searchParams.get('project_root');
  const call = async (operation: string, arguments_: Record<string, unknown>) => {
    const response = await fetch(endpoint, {
      method: 'POST', headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ operation, arguments: arguments_, ...(projectRoot ? { project_root: projectRoot } : {}) }),
    });
    expect(response.ok, `${operation} failed`).toBeTruthy();
    return response.json() as Promise<Record<string, any>>;
  };
  const opened = await call('workspace_open', { session_id: workspaceUrl.searchParams.get('workspace') });
  const view = opened.views[0];
  const updated = await call('view_update', { workspace_id: opened.workspace_id, view_id: view.id, sql, expected_revision: view.revision, cursor_position: 0 });
  const run = await call('view_run', { workspace_id: opened.workspace_id, view_id: view.id, cursor_position: 0 });
  return { workspaceUrl: workspaceUrl.toString(), workspaceId: opened.workspace_id as string, viewId: view.id as string, revision: updated.revision as number, queryId: run.query_id as string, call };
}

test('formats a result-bearing current View from the button and palette without executing it', async ({ page }) => {
  const seed = await seededWorkspace("select 1 as retained_value from (select 1) source where 1=1 and 'SELECT'='SELECT';");
  const operations = observedOperations(page);
  const formatted = "SELECT\n  1 as retained_value\nfrom (\n    SELECT\n      1\n  ) source\nwhere 1 = 1\n  and 'SELECT' = 'SELECT'\n;";
  await page.goto(seed.workspaceUrl);
  await expect(page.getByRole('grid')).toBeVisible();
  await page.getByRole('button', { name: 'Format', exact: true }).click();
  await expect.poll(() => editorSource(page)).toBe(formatted);
  await page.keyboard.press('Meta+P');
  const palette = page.getByRole('dialog', { name: 'Command palette' });
  await palette.getByRole('textbox').fill('Format');
  await palette.getByRole('textbox').press('Enter');
  await expect.poll(() => editorSource(page)).toBe(formatted);
  const autosave = page.waitForRequest((request) => request.method() === 'POST'
    && request.postDataJSON()?.operation === 'view_update' && request.postDataJSON()?.arguments?.sql === formatted);
  await page.evaluate(() => window.dispatchEvent(new Event('focus')));
  await autosave;
  const state = await seed.call('workspace_get', { workspace_id: seed.workspaceId });
  const current = state.views.find((view: { id: string }) => view.id === seed.viewId);
  expect(current.sql).toBe(formatted);
  expect(current.result?.query_id).toBe(seed.queryId);
  await expect(page.getByRole('grid')).toBeVisible();
  expect(operations.filter((operation) => executionOperations.has(operation))).toEqual([]);
});

test('keeps a result-bearing current View and its query identity when formatting fails', async ({ page }) => {
  const seed = await seededWorkspace('SELECT 2 AS retained_value');
  const operations = observedOperations(page);
  await page.goto(seed.workspaceUrl);
  await expect(page.getByRole('grid')).toBeVisible();
  await replaceSql(page, 'select [');
  await page.getByRole('button', { name: 'Format', exact: true }).click();
  await expect(editor(page)).toContainText('select [');
  await expect(page.getByRole('alert')).toContainText(/Parse error/);
  const state = await seed.call('workspace_get', { workspace_id: seed.workspaceId });
  const current = state.views.find((view: { id: string }) => view.id === seed.viewId);
  expect(current.sql).toBe('SELECT 2 AS retained_value');
  expect(current.result?.query_id).toBe(seed.queryId);
  await expect(page.getByRole('grid')).toBeVisible();
  expect(operations.filter((operation) => executionOperations.has(operation))).toEqual([]);
});
