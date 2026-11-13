// CA-E-683@11
import { expect, test, type Page } from '@playwright/test';

const url = process.env.WORKBENCH_E2E_URL!;

async function openWorkspace(page: Page, sessionId: string) {
  const workbench = new URL(url);
  const endpoint = new URL(`${workbench.pathname.replace(/\/$/, '')}/interface`, workbench.origin);
  const response = await page.request.post(endpoint.toString(), { data: { operation: 'workspace_open', arguments: { session_id: sessionId } } });
  const body = await response.text(); expect(response.ok(), body).toBeTruthy();
  return JSON.parse(body) as { project_root: string };
}

test('cleans only this browser legacy standalone URL and preserves explicit Workspace links', async ({ browser }) => {
  const context = await browser.newContext(); const page = await context.newPage();
  const ownId = `standalone-url-own-${Date.now()}`; const foreignId = `chat-workspace-${Date.now()}`;
  try {
    const own = await openWorkspace(page, ownId); await openWorkspace(page, foreignId);
    const sessionKey = `caprmedio.workbench.${own.project_root}.standalone-session`;
    await page.addInitScript(({ key, value }) => localStorage.setItem(key, value), { key: sessionKey, value: ownId });

    const legacy = new URL(url);
    legacy.searchParams.set('workspace', ownId); legacy.searchParams.set('project_root', own.project_root);
    legacy.searchParams.set('query', ''); legacy.searchParams.set('keep', 'value'); legacy.hash = 'standalone-fragment';
    const clean = new URL(legacy); clean.searchParams.delete('workspace');
    await page.goto(legacy.toString()); await expect(page.getByRole('button', { name: 'Run Cmd+Enter' })).toBeEnabled();
    expect(page.url()).toBe(clean.toString());
    await page.reload(); await expect(page.getByRole('button', { name: 'Run Cmd+Enter' })).toBeEnabled();
    expect(page.url()).toBe(clean.toString());

    const foreign = new URL(clean);
    foreign.searchParams.set('workspace', foreignId); foreign.searchParams.set('chat', '1'); foreign.hash = 'chat-fragment';
    await page.goto(foreign.toString()); await expect(page.getByRole('button', { name: 'Run Cmd+Enter' })).toBeEnabled();
    expect(page.url()).toBe(foreign.toString());

    const embedded = new URL(clean);
    embedded.searchParams.set('workspace', ownId); embedded.searchParams.set('embedded', '1'); embedded.hash = 'embedded-fragment';
    const embeddedClean = new URL(embedded); embeddedClean.searchParams.delete('workspace');
    await page.goto(embedded.toString()); await expect(page.getByRole('button', { name: 'Run Cmd+Enter' })).toBeEnabled();
    expect(page.url()).toBe(embeddedClean.toString());
    await expect(page.locator('html')).toHaveAttribute('data-density', 'compact');
    await page.reload(); await expect(page.getByRole('button', { name: 'Run Cmd+Enter' })).toBeEnabled();
    expect(page.url()).toBe(embeddedClean.toString());
  } finally { await context.close(); }
});

for (const method of ['getItem', 'setItem']) {
  test(`keeps unsaved SQL usable when browser storage ${method} fails`, async ({ page }) => {
    await page.addInitScript((operation) => {
      Object.defineProperty(Storage.prototype, operation, {
        value() { throw new DOMException('Storage is unavailable', 'SecurityError'); },
      });
    }, method);
    await page.goto(url);
    const warning = page.getByRole('alert').filter({ hasText: 'Browser storage is unavailable' });
    await expect(warning).toHaveText('Browser storage is unavailable. Reloading or closing Workbench may lose unsaved edits.');
    const editor = page.getByRole('textbox', { name: 'Query editor' });
    await expect(editor).toBeEditable();
    await editor.click();
    await page.keyboard.insertText('SELECT 7 AS in_memory');
    await page.getByRole('button', { name: 'Run Cmd+Enter' }).click();
    await expect(page.getByRole('columnheader')).toHaveText(/in_memory/);
    await expect(editor).toHaveText('SELECT 7 AS in_memory');
    await expect(warning).toBeVisible();
  });
}

test('uses the canonical Project name and rejects a Workspace without it', async ({ page }) => {
  let omitName = false;
  await page.route(/\/(?:interface|api\/workspace_open)$/, async (route) => {
    if (route.request().url().endsWith('/interface') && route.request().postDataJSON()?.operation !== 'workspace_open') {
      await route.continue();
      return;
    }
    const response = await route.fetch();
    expect(response.ok(), await response.text()).toBeTruthy();
    const result = await response.json();
    const { project_name, ...rest } = result;
    expect(project_name).toEqual(expect.any(String));
    await route.fulfill({ response, json: omitName ? rest : { ...result, project_name: 'Canonical Project' } });
  });
  await page.goto(url);
  const run = page.getByRole('button', { name: 'Run Cmd+Enter' });
  await expect(run).toBeEnabled();
  await expect(page.locator('header')).toContainText('Project: Canonical Project');
  omitName = true;
  await page.reload();
  await expect(page.getByRole('alert')).toContainText('Workspace binding requires the Project name.');
  await expect(run).toBeDisabled();
});
