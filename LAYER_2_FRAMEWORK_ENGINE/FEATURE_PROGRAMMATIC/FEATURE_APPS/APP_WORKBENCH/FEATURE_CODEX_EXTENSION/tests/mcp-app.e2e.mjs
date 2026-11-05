// CA-E-684@3
// CA-D-681@5
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { createRequire } from 'node:module';
import { dirname, resolve } from 'node:path';
import test from 'node:test';
import { fileURLToPath } from 'node:url';

const extension = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const require = createRequire(resolve(extension, '../FEATURE_WORKBENCH_FRONTEND/package.json'));
const { chromium } = require('playwright');

test('MCP App receives the initial result and calls a separate read-only tool', async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage();
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.setContent('<iframe title="probe"></iframe>');
    await page.evaluate(html => {
      const frame = document.querySelector('iframe');
      window.probeCalls = [];
      window.addEventListener('message', event => {
        if (event.source !== frame.contentWindow || event.data?.jsonrpc !== '2.0') return;
        const { id, method, params } = event.data;
        if (id === undefined) return;
        const send = message => frame.contentWindow.postMessage({ jsonrpc: '2.0', ...message }, '*');
        if (method === 'ui/initialize') {
          send({ id, result: { protocolVersion: '2026-01-26', hostInfo: { name: 'test-host', version: '1' }, hostCapabilities: {} } });
          send({ method: 'ui/notifications/tool-input', params: { arguments: { project_root: '/trusted/project' } } });
          send({ method: 'ui/notifications/tool-result', params: { structuredContent: { message: 'Initial host result' } } });
        } else if (method === 'tools/call') {
          window.probeCalls.push(params);
          send({ id, result: { isError: false, structuredContent: { message: 'Tool bridge passed' } } });
        }
      });
      frame.srcdoc = html;
    }, fs.readFileSync(resolve(extension, 'mcp_app_probe.html'), 'utf8'));
    const frame = page.frameLocator('iframe');
    await frame.getByText('Host bridge connected', { exact: true }).waitFor();
    await frame.getByText('Initial host result', { exact: true }).waitFor();
    await frame.getByRole('button', { name: 'Test tool bridge' }).click();
    await frame.getByText('Tool bridge passed', { exact: true }).waitFor();
    assert.deepEqual(await page.evaluate(() => window.probeCalls), [{
      name: 'workbench_ui_ping', arguments: { project_root: '/trusted/project' },
    }]);
    assert.deepEqual(errors, []);
  } finally {
    await browser.close();
  }
});
