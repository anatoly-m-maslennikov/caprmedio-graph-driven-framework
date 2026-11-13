// CA-E-683@10
import { expect, test, type Page } from '@playwright/test';

const url = process.env.WORKBENCH_E2E_URL!;
const editor = (page: Page) => page.getByRole('textbox', { name: 'Query editor' });

async function typeQuery(page: Page, sql: string) {
  await editor(page).click();
  await editor(page).press('Meta+A');
  await editor(page).pressSequentially(sql);
  await expect(editor(page)).toHaveText(sql);
}

async function moveBefore(page: Page, suffix: string) {
  for (let index = 0; index < suffix.length; index += 1) await page.keyboard.press('ArrowLeft');
}

test('completes qualified columns and escapes Status values without executing SQL', async ({ page }) => {
  const operations: string[] = [];
  page.on('request', (request) => {
    if (request.method() !== 'POST') return;
    const path = new URL(request.url()).pathname;
    if (path.endsWith('/interface')) operations.push(request.postDataJSON()?.operation);
    else if (/\/(run|check|view-save)$/.test(path)) operations.push(path);
  });
  await page.route('**/schema', async (route) => {
    const response = await route.fetch();
    const schema = await response.json();
    const status = schema.tables.atoms.find((column: { name: string }) => column.name === 'header.state.status');
    expect(status).toBeTruthy();
    status.values = [...(status.values ?? []), "O'Reilly"];
    await route.fulfill({ response, json: schema });
  });
  const schemaReady = page.waitForResponse(response => response.url().endsWith('/schema') && response.ok());
  await page.goto(url);
  await (await schemaReady).finished();
  await page.evaluate(() => new Promise<void>(resolve => requestAnimationFrame(() => resolve())));
  await expect(editor(page)).toBeEditable();

  for (const qualifier of ['atoms', 'a']) {
    const suffix = qualifier === 'a' ? ' FROM atoms AS a' : '';
    await typeQuery(page, `SELECT ${qualifier}.head${suffix}`);
    await moveBefore(page, suffix);
    await page.keyboard.press('Control+Space');
    await page.getByRole('option', { name: /header\.state\.status/ }).first().click();
    await expect(editor(page)).toHaveText(`SELECT ${qualifier}."header.state.status"${suffix}`);
  }

  await typeQuery(page, 'SELECT atoms."header.st"');
  await page.keyboard.press('ArrowLeft');
  await page.keyboard.press('Control+Space');
  await page.getByRole('option', { name: /header\.state\.status/ }).first().click();
  await expect(editor(page)).toHaveText('SELECT atoms."header.state.status"');

  await typeQuery(page, 'SELECT header.st');
  await page.keyboard.press('Control+Space');
  await page.getByRole('option', { name: /header\.state\.status/ }).first().click();
  await expect(editor(page)).toHaveText('SELECT "header.state.status"');

  for (const [qualifier, suffix] of [['"a"', ' FROM atoms AS "a"'], ['header', ' FROM atoms AS header']]) {
    await typeQuery(page, `SELECT ${qualifier}.head${suffix}`);
    await moveBefore(page, suffix);
    await page.keyboard.press('Control+Space');
    await page.getByRole('option', { name: /header\.state\.status/ }).first().click();
    await expect(editor(page)).toHaveText(`SELECT ${qualifier}."header.state.status"${suffix}`);
  }

  await typeQuery(page, 'SELECT atoms."header.state.status" FROM atoms');
  await moveBefore(page, 'ate.status" FROM atoms');
  await page.keyboard.press('Control+Space');
  await page.getByRole('option', { name: /header\.state\.status/ }).first().click();
  await expect(editor(page)).toHaveText('SELECT atoms."header.state.status" FROM atoms');

  await typeQuery(page, 'SELECT "header.state.status" FROM atoms');
  await moveBefore(page, 'ate.status" FROM atoms');
  await page.keyboard.press('Control+Space');
  await page.getByRole('option', { name: /header\.state\.status/ }).first().click();
  await expect(editor(page)).toHaveText('SELECT "header.state.status" FROM atoms');

  await typeQuery(page, `SELECT * FROM atoms WHERE "header.state.status" = 'Active'`);
  await moveBefore(page, `ive'`);
  await page.keyboard.press('Control+Space');
  await page.getByRole('option', { name: 'Active', exact: true }).click();
  await expect(editor(page)).toHaveText(`SELECT * FROM atoms WHERE "header.state.status" = 'Active'`);

  await typeQuery(page, `SELECT * FROM atoms WHERE "header.state.status" = 'O''R'`);
  await page.keyboard.press('ArrowLeft');
  await page.keyboard.press('Control+Space');
  await page.getByRole('option', { name: "O'Reilly", exact: true }).click();
  await expect(editor(page)).toHaveText(`SELECT * FROM atoms WHERE "header.state.status" = 'O''Reilly'`);
  await moveBefore(page, `eilly'`);
  await page.keyboard.press('Control+Space');
  await page.getByRole('option', { name: "O'Reilly", exact: true }).click();
  await expect(editor(page)).toHaveText(`SELECT * FROM atoms WHERE "header.state.status" = 'O''Reilly'`);
  expect(operations.filter((operation) => /(?:view_run|view_check|query_run|query_check|view_save|\/run|\/check|\/view-save)/.test(operation))).toEqual([]);
});
