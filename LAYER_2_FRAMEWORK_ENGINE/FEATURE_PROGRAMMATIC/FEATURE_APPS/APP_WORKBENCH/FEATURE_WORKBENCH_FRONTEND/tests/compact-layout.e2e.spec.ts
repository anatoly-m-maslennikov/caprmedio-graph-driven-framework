// CA-E-683@9
import { expect, test } from '@playwright/test';

const url = process.env.WORKBENCH_E2E_URL!;

test('keeps the compact editor scrollable and controls usable across settings', async ({ page }) => {
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto(url);
  const tab = page.getByRole('tab', { name: /^View 1/ });
  const settings = page.getByRole('tab', { name: 'Settings' });
  const editor = page.getByRole('textbox', { name: 'Query editor' });
  await expect(editor).toBeEditable();
  await settings.click();
  await page.getByLabel('Density', { exact: true }).selectOption('compact');
  await tab.click();

  const query = 'SELECT\n  1\n  ,2\n  ,3\n  ,4\n  ,5\n;';
  await editor.click(); await editor.press('Meta+A'); await editor.pressSequentially(query);
  const scroller = page.locator('.editor-content .cm-scroller');
  await expect.poll(() => scroller.evaluate((element) => element.scrollHeight > element.clientHeight)).toBe(true);
  await editor.press('Meta+End');
  await expect.poll(() => scroller.evaluate((element) => element.scrollTop > 0)).toBe(true);
  await expect(editor).toContainText(';');

  const hide = page.getByRole('button', { name: /Query editor.*Hide editor/ });
  await hide.focus(); await page.keyboard.press('Enter');
  const show = page.getByRole('button', { name: /Query editor.*Show editor/ });
  await expect(show).toHaveAttribute('aria-expanded', 'false');
  await page.keyboard.press('Enter');
  await expect(editor).toBeVisible();
  await expect(editor).toContainText(';');

  await settings.click();
  await page.getByLabel('Theme', { exact: true }).selectOption('dark');
  await page.getByLabel('Content text zoom', { exact: true }).selectOption('125');
  await page.getByLabel('Interface text zoom', { exact: true }).selectOption('125');
  await page.getByLabel('Interface zoom', { exact: true }).selectOption('125');
  await tab.click();
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'dark');
  await expect(editor).toBeVisible();
  await expect(page.getByRole('button', { name: /^Run / })).toBeVisible();
  await expect.poll(() => scroller.evaluate((element) => element.scrollHeight > element.clientHeight)).toBe(true);

  await page.setViewportSize({ width: 600, height: 900 });
  await expect(page.getByRole('button', { name: /^Run / })).toBeVisible();
  const layout = await page.locator('.editor-panel').evaluate((panel) => {
    const editorBox = panel.querySelector('.editor-content')!.getBoundingClientRect();
    const actionsBox = panel.querySelector('.query-actions')!.getBoundingClientRect();
    return { editorBottom: editorBox.bottom, actionsTop: actionsBox.top };
  });
  expect(layout.actionsTop).toBeGreaterThanOrEqual(layout.editorBottom - 1);

  await settings.click();
  await page.getByLabel('Density', { exact: true }).selectOption('comfortable');
  await tab.click();
  await expect(page.locator('html')).toHaveAttribute('data-density', 'comfortable');
  await expect(scroller).toHaveCSS('max-height', 'none');
});
