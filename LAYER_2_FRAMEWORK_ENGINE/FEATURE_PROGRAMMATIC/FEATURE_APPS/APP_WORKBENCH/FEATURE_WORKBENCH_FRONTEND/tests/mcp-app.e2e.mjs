import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createRequire } from 'node:module';
import { dirname, resolve } from 'node:path';
import test from 'node:test';
import { fileURLToPath } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const require = createRequire(resolve(root, 'package.json'));
const { chromium } = require('playwright');
const fixtureUrl = process.env.WORKBENCH_NATIVE_E2E_URL ?? process.env.WORKBENCH_E2E_URL;
const projectRoot = process.env.WORKBENCH_NATIVE_E2E_PROJECT_ROOT ?? (fixtureUrl ? new URL(fixtureUrl).searchParams.get('project_root') : null);
const fixtureReady = Boolean(fixtureUrl && projectRoot);

const interfaceOperations = new Set([
  'workspace_open', 'workspace_list', 'workspace_get', 'view_create', 'view_list', 'view_get',
  'view_update', 'view_run', 'view_check', 'view_fetch', 'view_focus', 'view_rename',
  'view_duplicate', 'view_remove', 'query_log_list', 'query_log_get',
]);
const routes = {
  query_run: 'run', query_check: 'check', query_page: 'page', query_schema: 'schema',
  workbench_status: 'status', query_load: 'load', query_saved_list: 'saved-list', view_save: 'view-save',
};

async function artifact() { return readFile(resolve(root, 'dist/mcp-app.html'), 'utf8'); }

async function backendCall(name, arguments_) {
  const { project_root, ...argumentsWithoutRoot } = arguments_;
  assert.equal(project_root, projectRoot, `${name} must retain the selected Project`);
  const base = new URL(fixtureUrl);
  const usesInterface = interfaceOperations.has(name) || (name === 'view_save' && 'workspace_id' in argumentsWithoutRoot);
  const path = usesInterface ? 'interface' : routes[name];
  assert.ok(path, `unexpected MCP tool ${name}`);
  const endpoint = new URL(`${base.pathname.replace(/\/$/, '')}/${path}`, base.origin);
  const body = usesInterface
    ? { operation: name, arguments: argumentsWithoutRoot, project_root }
    : { ...argumentsWithoutRoot, project_root };
  const response = await fetch(endpoint, {
    method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body),
  });
  const content = await response.json();
  return response.ok ? { isError: false, structuredContent: content }
    : { isError: true, structuredContent: content };
}

async function openWorkspace(sessionId) {
  const result = await backendCall('workspace_open', { session_id: sessionId, project_root: projectRoot });
  assert.equal(result.isError, false);
  return result.structuredContent;
}

async function bridgePage({ input, initial, resultFirst = false, callTool }) {
  const browser = await chromium.launch({ headless: true, ...(process.platform === 'darwin' ? { channel: 'chrome' } : {}) });
  const page = await browser.newPage();
  const html = await artifact();
  const calls = [];
  const toolResults = [];
  const pageErrors = [];
  page.on('pageerror', (error) => pageErrors.push(error.message));
  await page.exposeFunction('__workbenchToolCall', async (params) => {
    calls.push(params);
    try {
      const result = await (callTool ? callTool(params) : { isError: false, structuredContent: {} });
      toolResults.push({ name: params.name, result });
      return result;
    } catch (error) {
      toolResults.push({ name: params.name, error: error instanceof Error ? error.message : String(error) });
      throw error;
    }
  });
  if (fixtureUrl) await page.goto(fixtureUrl);
  await page.setContent('<iframe title="CAPRMEDIO Workbench"></iframe>');
  await page.evaluate(({ html: app, input: toolInput, initial: toolResult, resultFirst: resultBeforeInput }) => {
    const frame = document.querySelector('iframe');
    window.addEventListener('message', (event) => {
      if (event.source !== frame.contentWindow || event.data?.jsonrpc !== '2.0') return;
      const { id, method, params } = event.data;
      const send = (message) => frame.contentWindow.postMessage({ jsonrpc: '2.0', ...message }, '*');
      if (method === 'ui/initialize') {
        send({ id, result: { protocolVersion: '2026-01-26', hostInfo: { name: 'disposable-host', version: '1' } } });
        const sendInput = () => send({ method: 'ui/notifications/tool-input', params: { arguments: toolInput } });
        const sendResult = () => send({ method: 'ui/notifications/tool-result', params: { structuredContent: toolResult } });
        if (resultBeforeInput) { sendResult(); queueMicrotask(sendInput); } else { sendInput(); queueMicrotask(sendResult); }
      } else if (method === 'tools/call') {
        void window.__workbenchToolCall(params).then((result) => send({ id, result }), (error) => send({ id, error: { message: error.message } }));
      }
    });
    frame.srcdoc = app;
  }, { html, input, initial, resultFirst });
  return { browser, page, frame: page.frameLocator('iframe'), calls, toolResults, pageErrors };
}

test('native artifact inlines the shared UI assets', async () => {
  const html = await artifact();
  assert.equal(/<script\b[^>]*\bsrc=/i.test(html), false);
  assert.equal(/<link\b[^>]*\brel=["']stylesheet/i.test(html), false);
  assert.ok(html.includes('ui/initialize'));
  assert.ok(html.includes('tools/call'));
});

test('native bridge binds reordered host context to the actual Workbench backend', { skip: !fixtureReady }, async () => {
  const sessionId = `native-bridge-${Date.now()}`;
  const initial = await openWorkspace(sessionId);
  const host = await bridgePage({
    input: { session_id: sessionId, project_root: projectRoot }, initial, resultFirst: true,
    callTool: ({ name, arguments: arguments_ }) => backendCall(name, arguments_),
  });
  try {
    const projectBasename = projectRoot.replace(/\\+$/, '').split('/').at(-1);
    assert.equal(typeof initial.project_name, 'string');
    assert.ok(initial.project_name.length > 0);
    assert.notEqual(initial.project_name, projectBasename, 'fixture must expose a declared name distinct from its root basename');
    await host.frame.getByText(`Project: ${initial.project_name}`, { exact: true }).waitFor();
    const editor = host.frame.getByRole('textbox', { name: 'Query editor' });
    await editor.waitFor();
    await editor.click(); await editor.press('Meta+A'); await editor.pressSequentially('SELECT 17 AS native_bridge');
    await editor.press('Meta+Enter');
    try { await host.frame.getByRole('grid').waitFor({ timeout: 10_000 }); }
    catch (error) {
      const alerts = await host.frame.getByRole('alert').allTextContents();
      const body = await host.frame.locator('body').innerText();
      assert.fail(`${error instanceof Error ? error.message : error}\nalerts=${JSON.stringify(alerts)}\npageErrors=${JSON.stringify(host.pageErrors)}\ncalls=${JSON.stringify(host.calls)}\ntoolResults=${JSON.stringify(host.toolResults)}\nbody=${body}`);
    }
    const names = host.calls.map((call) => call.name);
    assert.ok(names.includes('view_update'));
    assert.ok(names.includes('view_run'));
    assert.ok(names.includes('view_fetch'));
    await host.frame.getByRole('textbox', { name: 'Query editor' }).press('Meta+P');
    const palette = host.frame.getByRole('dialog', { name: 'Command palette' });
    await palette.getByRole('textbox').fill('Duplicate View');
    await palette.getByRole('textbox').press('Enter');
    await host.frame.getByRole('tab', { name: /View 1\(1\)/ }).waitFor();
    const duplicate = host.calls.find((call) => call.name === 'view_duplicate');
    assert.ok(duplicate, 'native UI must dispatch view_duplicate through the MCP bridge');
    assert.equal(duplicate.arguments.workspace_id, initial.workspace_id);
    const duplicateResult = host.toolResults.find((entry) => entry.name === 'view_duplicate');
    assert.equal(typeof duplicateResult?.result?.structuredContent?.view_id, 'string');
    assert.equal(names.includes('workspace_open'), false, 'native bootstrap must not open a second Workspace');
    for (const call of host.calls) assert.equal(call.arguments.project_root, projectRoot);
  } finally {
    await host.browser.close();
  }
});

test('native bridge rejects missing host context before tool calls', { skip: !fixtureReady }, async () => {
  const host = await bridgePage({
    input: { project_root: '/trusted/project' },
    initial: { workspace_id: 'missing-session', active_view_id: 'view-1', views: [] },
  });
  try {
    await host.frame.getByRole('alert').getByText('Native Workbench binding requires session_id and project_root.').waitFor();
    assert.deepEqual(host.calls, []);
  } finally {
    await host.browser.close();
  }
});

test('native bridge rejects a missing project name before tool calls', { skip: !fixtureReady }, async () => {
  const sessionId = `missing-project-name-${Date.now()}`;
  const host = await bridgePage({
    input: { session_id: sessionId, project_root: projectRoot },
    initial: { workspace_id: sessionId, active_view_id: 'view-1', views: [] },
  });
  try {
    await host.frame.getByRole('alert').getByText('Native Workbench binding requires the initial Workspace project name.').waitFor();
    assert.deepEqual(host.calls, []);
  } finally {
    await host.browser.close();
  }
});
