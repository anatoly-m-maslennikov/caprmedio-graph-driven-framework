// CA-E-683@6
import { expect, test } from '@playwright/test';

test('browser fetches inline rows while MCP defaults to files', async ({ page }) => {
  const url = new URL(process.env.WORKBENCH_E2E_URL!);
  const fetched: Record<string, unknown>[] = [];
  page.on('request', request => {
    if (request.method() !== 'POST' || !request.url().endsWith('/interface')) return;
    const input = request.postDataJSON();
    if (input?.operation === 'view_fetch') fetched.push(input.arguments);
  });
  await page.goto(url.toString());
  const editor = page.getByRole('textbox', { name: 'Query editor' });
  await expect(editor).toBeEditable();
  await editor.click();
  await editor.press('Meta+A');
  await editor.pressSequentially('SELECT 42 AS inline_result');
  await editor.press('Meta+Enter');
  await expect(page.getByRole('grid')).toBeVisible();
  await expect(page.getByRole('grid')).toContainText('inline_result');
  await expect(page.getByRole('grid')).toContainText('42');
  expect(fetched.length).toBeGreaterThan(0);
  expect(fetched.every(input => input.result_delivery === 'inline')).toBe(true);
});
