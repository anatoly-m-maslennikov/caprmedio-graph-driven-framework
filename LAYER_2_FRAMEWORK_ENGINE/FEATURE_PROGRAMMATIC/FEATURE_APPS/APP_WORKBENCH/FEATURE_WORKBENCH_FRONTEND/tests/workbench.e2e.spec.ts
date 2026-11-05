// CA-E-683@2
// CA-E-684@1
import { expect, test, type Page } from '@playwright/test';

const url = process.env.WORKBENCH_E2E_URL!;
const editor = (page: Page) => page.getByRole('textbox', { name: 'Query editor' });
const projectName = new URL(url).pathname.split('/').filter(Boolean).at(-1)!;

async function replaceSql(page: Page, sql: string) {
  await editor(page).click();
  await page.keyboard.press('Meta+A');
  await page.keyboard.insertText(sql);
}

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

test('binds two browser contexts to one Workspace and observes external state', async ({ browser }) => {
  const setup = await sharedWorkspace();
  const firstContext = await browser.newContext();
  const secondContext = await browser.newContext();
  const firstPage = await firstContext.newPage();
  const secondPage = await secondContext.newPage();
  let releaseUpdate: (() => void) | undefined;
  try {
    await Promise.all([firstPage.goto(setup.workspaceUrl), secondPage.goto(setup.workspaceUrl)]);
    const external = firstPage.getByRole('tab', { name: 'External View', exact: true });
    await expect(external).toBeVisible({ timeout: 12_000 });
    await expect(external).toHaveAttribute('aria-selected', 'true');
    await expect(firstPage.getByRole('textbox', { name: 'Query editor' })).toContainText('SELECT 42 AS external_value');
    await expect(firstPage.getByRole('table')).toBeVisible({ timeout: 12_000 });
    await expect(firstPage.getByRole('columnheader').first()).toHaveText(/external_value\s+INTEGER/);

    await expect(secondPage.getByRole('tab', { name: 'External View', exact: true })).toHaveAttribute('aria-selected', 'true', { timeout: 12_000 });
    let updateStarted!: () => void;
    const held = new Promise<void>((resolve) => releaseUpdate = resolve);
    const started = new Promise<void>((resolve) => updateStarted = resolve);
    let delayed = false;
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
    await replaceSql(secondPage, 'SELECT 1 AS first_draft');
    await started;
    await replaceSql(secondPage, 'SELECT 2 AS latest_draft');
    const run = secondPage.keyboard.press('Meta+Enter');
    releaseUpdate?.();
    await run;
    await expect(editor(secondPage)).toContainText('SELECT 2 AS latest_draft');
    await expect(secondPage.getByRole('table')).toBeVisible({ timeout: 12_000 });
    await expect(secondPage.getByRole('columnheader').first()).toHaveText(/latest_draft\s+INTEGER/);
  } finally {
    releaseUpdate?.();
    await Promise.all([firstContext.close(), secondContext.close()]);
  }
});

test('keeps dirty SQL through Run and Check under the Project Workbench header', async ({ page }) => {
  await page.goto(url);
  const header = page.locator('header');
  await expect(header.getByText('Workbench', { exact: true })).toBeVisible();
  await expect(header.getByText(`Project: ${projectName}`, { exact: true })).toBeVisible();
  await expect(header.getByRole('tab', { name: 'Settings', exact: true })).toBeVisible();
  await expect(header.getByRole('tab', { name: 'Saved Queries and Views' })).toBeVisible();
  await expect(page.getByText('Query editor', { exact: true })).toBeVisible();
  await replaceSql(page, 'SELECT id FROM atoms ORDER BY id LIMIT 1');
  await page.keyboard.press('Meta+Enter');
  await expect(page.getByRole('table')).toBeVisible();
  await expect(page.getByRole('table').getByRole('row')).toHaveCount(2);
  await expect(page.getByRole('columnheader').first()).toHaveText(/id\s+VARCHAR/);
  await page.getByRole('button', { name: /^Check/ }).click();
  await expect(page.getByText('Valid: 1 rows, 1 columns.')).toBeVisible();
  await expect(page.getByRole('tab', { name: /^View 1 \*/ })).toBeVisible();
  await page.getByRole('button', { name: 'Run & Save', exact: true }).click();
  const queryName = page.getByRole('dialog', { name: 'Query name' }).getByRole('textbox');
  await queryName.fill('E2E query');
  await queryName.press('Enter');
  await expect(page.getByRole('group', { name: 'Query editor header' }).getByText(/^Saved:/)).toBeVisible();
  await expect(editor(page)).toContainText('SELECT id FROM atoms ORDER BY id LIMIT 1');
  await expect(page.getByRole('tab', { name: 'View 1', exact: true })).toBeVisible();
});

test('restores local View state and opens a saved View without running it', async ({ page }) => {
  await page.goto(url);
  await page.keyboard.press('Meta+P');
  await page.getByRole('dialog', { name: 'Command palette' }).getByRole('textbox').fill('Rename View');
  await page.keyboard.press('Enter');
  const title = page.getByRole('textbox', { name: 'View name' });
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
  const queryHeader = page.getByRole('group', { name: 'Query editor header' });
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
  await expect(page.getByRole('table')).toHaveCount(0);
  expect(executionRequests).toBe(0);
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
  expect(schema.tables.atoms.find((column) => column.name === 'status')?.values).toContain('Active');
  await page.keyboard.press('Meta+P');
  const palette = page.getByRole('dialog', { name: 'Command palette' });
  await expect(palette.getByRole('textbox')).toBeFocused();
  await page.keyboard.press('Control+N');
  await page.keyboard.press('Enter');
  await expect(page.getByRole('region', { name: 'Saved Queries and Views' })).toBeVisible();
  await page.keyboard.press('Meta+P');
  await page.keyboard.press('Control+N');
  await page.keyboard.press('Control+P');
  await page.keyboard.press('Enter');
  await expect(page.getByRole('region', { name: 'Settings' })).toBeVisible();
  await page.getByRole('tab', { name: /^View 1/ }).click();
  await replaceSql(page, "SELECT status FROM atoms WHERE status = 'Act'");
  await page.keyboard.press('ArrowLeft');
  await page.keyboard.press('Control+Space');
  const active = page.getByRole('option', { name: 'Active', exact: true });
  await expect(active).toBeVisible();
  await active.click();
  await expect(editor(page)).toContainText("status = 'Active'");
  await page.getByRole('button', { name: 'Hide editor' }).click();
  await page.keyboard.press('Meta+P');
  await palette.getByRole('textbox').fill('Focus Query editor');
  await page.keyboard.press('Enter');
  await expect(editor(page)).toBeFocused();
});
