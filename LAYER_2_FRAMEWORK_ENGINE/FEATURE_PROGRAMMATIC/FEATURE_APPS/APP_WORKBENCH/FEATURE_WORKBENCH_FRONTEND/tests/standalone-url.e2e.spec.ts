// CA-D-674@19
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
    await page.goto(embedded.toString()); await expect(page.getByRole('button', { name: 'Run Cmd+Enter' })).toBeEnabled();
    expect(page.url()).toBe(embedded.toString());
  } finally { await context.close(); }
});
