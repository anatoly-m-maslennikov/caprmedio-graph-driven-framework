// CA-M-472@1
// CA-E-678@6
import { defineConfig } from '@playwright/test';

const baseURL = process.env.WORKBENCH_E2E_URL;

if (!baseURL) throw new Error('WORKBENCH_E2E_URL is required for Workbench browser E2E tests.');

export default defineConfig({
  testDir: './tests',
  outputDir: '../../../../../.caprmedio_tmp/workbench/browser-results',
  timeout: 120_000,
  workers: 1,
  retries: 0,
  use: { baseURL, browserName: 'chromium', channel: process.platform === 'darwin' ? 'chrome' : 'chromium' },
});
