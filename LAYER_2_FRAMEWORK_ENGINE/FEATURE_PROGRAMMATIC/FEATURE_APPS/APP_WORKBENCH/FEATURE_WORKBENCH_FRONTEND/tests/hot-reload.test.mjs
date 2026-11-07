// CA-E-797@1
import assert from 'node:assert/strict';
import { dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import test from 'node:test';
import { loadConfigFromFile } from 'vite';

const configFile = fileURLToPath(new URL('../vite.config.ts', import.meta.url));
const root = dirname(configFile);

test('Vite code hot reload is disabled by default and explicitly enabled', async () => {
  const previous = process.env.CAPRMEDIO_HOT_RELOAD;
  try {
    for (const mode of ['development', 'mcp-app']) {
      delete process.env.CAPRMEDIO_HOT_RELOAD;
      const disabled = await loadConfigFromFile({ command: 'serve', mode }, configFile, root);
      assert.equal(disabled.config.server.hmr, false);
      assert.equal(disabled.config.server.watch, null);
      process.env.CAPRMEDIO_HOT_RELOAD = '1';
      const enabled = await loadConfigFromFile({ command: 'serve', mode }, configFile, root);
      assert.equal(enabled.config.server.hmr, true);
      assert.equal(enabled.config.server.watch, undefined);
    }
  } finally {
    if (previous === undefined) delete process.env.CAPRMEDIO_HOT_RELOAD;
    else process.env.CAPRMEDIO_HOT_RELOAD = previous;
  }
});
