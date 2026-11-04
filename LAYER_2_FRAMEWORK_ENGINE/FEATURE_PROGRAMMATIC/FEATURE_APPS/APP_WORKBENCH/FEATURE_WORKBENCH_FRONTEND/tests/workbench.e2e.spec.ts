// CA-E-678@5
import { expect, test, type Page } from '@playwright/test';

const url = process.env.WORKBENCH_E2E_URL!;
const editor = (page: Page) => page.getByRole('textbox', { name: 'Query editor' });
const projectName = new URL(url).pathname.split('/').filter(Boolean).at(-1)!;

async function replaceSql(page: Page, sql: string) {
  await editor(page).click();
  await page.keyboard.press('Meta+A');
  await page.keyboard.insertText(sql);
}

test('keeps dirty SQL through Run and Check under the Project Workbench header', async ({ page }) => {
  await page.goto(url);
  const header = page.locator('header');
  await expect(header.getByText('Workbench', { exact: true })).toBeVisible();
  await expect(header.getByText(`Project: ${projectName}`, { exact: true })).toBeVisible();
  await expect(header.getByRole('tab', { name: 'Settings', exact: true })).toBeVisible();
  await expect(header.getByRole('tab', { name: 'Saved Queries and Worksheets' })).toBeVisible();
  await expect(page.getByText('Query editor', { exact: true })).toBeVisible();
  await replaceSql(page, 'SELECT id FROM atoms ORDER BY id LIMIT 1');
  await page.keyboard.press('Meta+Enter');
  await expect(page.getByRole('table')).toBeVisible();
  await expect(page.getByRole('table').getByRole('row')).toHaveCount(2);
  await page.getByRole('button', { name: /^Check/ }).click();
  await expect(page.getByText('Valid: 1 rows, 1 columns.')).toBeVisible();
  await expect(editor(page)).toContainText('SELECT id FROM atoms ORDER BY id LIMIT 1');
  await expect(page.getByRole('tab', { name: /^Worksheet 1 \*/ })).toBeVisible();
});

test('restores local Worksheet state and opens a saved Worksheet without running it', async ({ page }) => {
  await page.goto(url);
  await page.keyboard.press('Meta+P');
  await page.getByRole('dialog', { name: 'Command palette' }).getByRole('textbox').fill('Rename Worksheet');
  await page.keyboard.press('Enter');
  const title = page.getByRole('textbox', { name: 'Worksheet name' });
  await expect(title).toBeFocused();
  await title.fill('E2E Worksheet');
  await title.press('Enter');
  await replaceSql(page, "SELECT 'saved worksheet'");
  await page.waitForTimeout(5200);
  const restored = await page.context().newPage();
  await restored.goto(url);
  await expect(restored.getByRole('tab', { name: /E2E Worksheet/ })).toBeVisible();
  await expect(editor(restored)).toContainText("SELECT 'saved worksheet'");
  await restored.close();
  await page.getByRole('button', { name: 'Save Worksheet', exact: true }).click();
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
  await page.getByRole('button', { name: /Open Saved/ }).click();
  await page.getByRole('dialog', { name: 'Open saved query or Worksheet' }).getByRole('textbox').fill(id!);
  await page.keyboard.press('Enter');
  await expect(editor(page)).toContainText("SELECT 'saved worksheet'");
  await expect(page.getByRole('table')).toHaveCount(0);
  expect(executionRequests).toBe(0);
});

test('uses palette navigation, quoted status completion, and focus after hiding the editor', async ({ page }) => {
  await page.goto(url);
  await page.keyboard.press('Meta+P');
  const palette = page.getByRole('dialog', { name: 'Command palette' });
  await expect(palette.getByRole('textbox')).toBeFocused();
  await page.keyboard.press('Control+N');
  await page.keyboard.press('Enter');
  await expect(page.getByRole('region', { name: 'Saved Queries and Worksheets' })).toBeVisible();
  await page.keyboard.press('Meta+P');
  await page.keyboard.press('Control+N');
  await page.keyboard.press('Control+P');
  await page.keyboard.press('Enter');
  await expect(page.getByRole('region', { name: 'Settings' })).toBeVisible();
  await page.getByRole('tab', { name: /^Worksheet 1/ }).click();
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
