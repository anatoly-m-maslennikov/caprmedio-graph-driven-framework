// CA-E-783@1
// CA-E-786@1
import { expect, test, type Page } from '@playwright/test';

const url = process.env.WORKBENCH_E2E_URL!;
const editor = (page: Page) => page.getByRole('textbox', { name: 'Query editor' });
const sql = `
  SELECT
    i AS row_id,
    CASE WHEN i < 4 THEN 'alpha' WHEN i < 8 THEN 'beta' ELSE 'gamma' END AS group_name,
    100 - i AS sort_value,
    repeat('😀', 180) || '-' || CAST(i AS VARCHAR) AS long_unicode,
    NULL::VARCHAR AS empty_column
  FROM range(0, 12) AS rows(i)
`;

async function workspaceUrl(page: Page) {
  const next = new URL(url);
  const workspace = `grid-${Date.now()}-${Math.random().toString(36).slice(2)}`;
  next.searchParams.set('workspace', workspace);
  const projectRoot = next.searchParams.get('project_root');
  const endpoint = new URL(`${next.pathname.replace(/\/$/, '')}/interface`, next.origin);
  const response = await page.request.post(endpoint.toString(), {
    data: { operation: 'workspace_open', arguments: { session_id: workspace }, ...(projectRoot ? { project_root: projectRoot } : {}) },
  });
  expect(response.ok(), await response.text()).toBeTruthy();
  return next.toString();
}

function interfaceRequest(request: { method(): string; url(): string; postDataJSON(): any }, operation?: string) {
  if (request.method() !== 'POST' || !new URL(request.url()).pathname.endsWith('/interface')) return false;
  return !operation || request.postDataJSON()?.operation === operation;
}

function fetchRequest(request: { method(): string; url(): string; postDataJSON(): any }, column?: number) {
  if (!interfaceRequest(request, 'view_fetch')) return false;
  const grid = request.postDataJSON()?.arguments?.grid;
  return column === undefined || grid?.sort?.some((item: { column?: number }) => item.column === column);
}

async function replaceSql(page: Page, value: string) {
  await editor(page).click();
  await page.keyboard.press('Meta+A');
  await page.keyboard.insertText(value);
}

async function prepare(page: Page, fixedPageSize = 2, query = sql) {
  await page.goto(await workspaceUrl(page));
  await page.getByRole('tab', { name: 'Settings', exact: true }).click();
  await page.getByRole('radio', { name: 'Fixed' }).check();
  const pageSize = page.getByLabel('Fixed rows per page');
  await pageSize.fill(String(fixedPageSize));
  await pageSize.press('Tab');
  await page.getByRole('tab', { name: /^View 1/ }).click();
  await replaceSql(page, query);
}

async function run(page: Page, expectedRows = 12) {
  const request = page.waitForRequest((item) => interfaceRequest(item, 'view_run'));
  await page.keyboard.press('Meta+Enter');
  await request;
  await expect(page.getByRole('grid')).toBeVisible({ timeout: 15_000 });
  await expect(page.locator('.result-summary').first()).toContainText(`${expectedRows} rows`);
}

function column(page: Page, name: string) {
  return page.locator('.tabulator-col').filter({ hasText: name }).first();
}

async function openHeaderMenu(page: Page, name: string) {
  await column(page, name).click({ button: 'right' });
  const menu = page.locator('.tabulator-menu');
  await expect(menu).toBeVisible();
  return menu;
}

async function filterColumn(page: Page, name: string, value: string) {
  const menu = await openHeaderMenu(page, name);
  const dialog = page.waitForEvent('dialog').then(async (event) => {
    expect(event.message()).toContain(`Filter ${name}`);
    await event.accept(value);
  });
  const request = page.waitForRequest((item) => interfaceRequest(item, 'view_fetch'));
  const click = menu.locator('.tabulator-menu-item').getByText('Filter', { exact: true }).click();
  await dialog;
  await click;
  const fetched = await request;
  expect(fetched.postDataJSON()?.arguments?.grid?.filters).toEqual(expect.arrayContaining([expect.objectContaining({ value })]));
}

async function clearColumnFilter(page: Page, name: string) {
  const menu = await openHeaderMenu(page, name);
  const request = page.waitForRequest((item) => interfaceRequest(item, 'view_fetch'));
  await menu.locator('.tabulator-menu-item').getByText('Clear filter', { exact: true }).click();
  const fetched = await request;
  expect(fetched.postDataJSON()?.arguments?.grid?.filters).toHaveLength(1);
}

test('keeps filtering, sorting and grouping global while paging the cached result', async ({ page }) => {
  let runs = 0;
  page.on('request', (request) => { if (interfaceRequest(request, 'view_run')) runs += 1; });
  await prepare(page);
  await run(page);
  expect(runs).toBe(1);

  const sortedGlobally = page.waitForRequest((item) => fetchRequest(item, 2));
  const sortMenu = await openHeaderMenu(page, 'sort_value');
  await expect(sortMenu.locator('.tabulator-menu-item')).toHaveText([
    'Column Sort ascending', 'Column Sort descending', 'Group by', 'Filter', 'Clear filter',
  ]);
  await sortMenu.locator('.tabulator-menu-item').getByText('Column Sort descending', { exact: true }).click();
  await sortedGlobally;
  await expect(page.locator('.tabulator-row').first().locator('.tabulator-cell').nth(2)).toHaveText('100');
  const sortedNext = page.waitForRequest((item) => interfaceRequest(item, 'view_fetch'));
  await page.getByRole('navigation', { name: 'Result pages' }).getByRole('button', { name: 'Next' }).click();
  await sortedNext;
  await expect(page.locator('.tabulator-row').first().locator('.tabulator-cell').nth(2)).toHaveText('98');

  const grouped = page.waitForRequest((item) => interfaceRequest(item, 'view_fetch') && item.postDataJSON()?.arguments?.grid?.group_by?.column === 1);
  const groupMenu = await openHeaderMenu(page, 'group_name');
  await groupMenu.locator('.tabulator-menu-item').getByText('Group by', { exact: true }).click();
  await grouped;
  await expect(page.locator('.tabulator-group')).toContainText('group_name: alpha (4)');
  await expect(page.locator('.tabulator-group')).not.toContainText('beta');

  const next = page.getByRole('navigation', { name: 'Result pages' }).getByRole('button', { name: 'Next' });
  for (let index = 0; index < 2; index += 1) {
    const request = page.waitForRequest((item) => interfaceRequest(item, 'view_fetch'));
    await next.click();
    await request;
  }
  await expect(page.locator('.tabulator-group')).toContainText('group_name: beta (4)');

  await page.keyboard.press('Meta+P');
  const palette = page.getByRole('dialog', { name: 'Command palette' });
  await palette.getByRole('textbox').fill('Result grid: Sort column descending');
  const sorted = page.waitForRequest((item) => fetchRequest(item, 1));
  const prompt = page.waitForEvent('dialog').then(async (dialog) => {
    expect(dialog.message()).toContain('Result column index');
    await dialog.accept('1');
  });
  const enter = page.keyboard.press('Enter');
  await prompt;
  await enter;
  await sorted;
  expect(runs).toBe(1);
});

test('keeps another column filter when one column filter is cleared', async ({ page }) => {
  let runs = 0;
  page.on('request', (request) => { if (interfaceRequest(request, 'view_run')) runs += 1; });
  await prepare(page, 4);
  await run(page);
  await filterColumn(page, 'group_name', 'beta');
  await filterColumn(page, 'row_id', '5');
  await expect(page.locator('.result-summary').first()).toContainText('1 rows');
  await clearColumnFilter(page, 'group_name');
  await expect(page.locator('.result-summary').first()).toContainText('1 rows');
  expect(runs).toBe(1);
});

test('keeps SQL NULL and the literal null in separate groups', async ({ page }) => {
  const query = `
    SELECT CASE WHEN i < 2 THEN NULL::VARCHAR ELSE 'null' END AS group_value
    FROM range(0, 3) AS rows(i)
  `;
  await prepare(page, 3, query);
  await run(page, 3);
  const grouped = page.waitForRequest((item) => (
    interfaceRequest(item, 'view_fetch')
    && item.postDataJSON()?.arguments?.grid?.group_by?.column === 0
  ));
  const menu = await openHeaderMenu(page, 'group_value');
  await menu.locator('.tabulator-menu-item').getByText('Group by', { exact: true }).click();
  await grouped;
  await expect.poll(async () => page.locator('[role="rowgroup"]').evaluateAll((nodes) => nodes
    .map((node) => node.textContent?.trim() ?? '')
    .filter((text) => /^group_value: (?:NULL|null) \(\d+\)$/.test(text))))
    .toEqual(expect.arrayContaining(['group_value: NULL (2)', 'group_value: null (1)']));
});

test('preserves full Unicode values and hidden columns in row actions, with zoomed menus', async ({ browser }) => {
  const context = await browser.newContext({ permissions: ['clipboard-read', 'clipboard-write'] });
  const page = await context.newPage();
  let runs = 0;
  page.on('request', (request) => { if (interfaceRequest(request, 'view_run')) runs += 1; });
  try {
    await prepare(page, 4);
    await run(page);
    expect(runs).toBe(1);

    const longCell = page.locator('.tabulator-row').first().locator('.tabulator-cell').nth(3);
    await longCell.click({ button: 'right' });
    const fullValue = page.waitForEvent('dialog');
    const showFull = page.locator('.tabulator-menu-item').getByText('Cell Show full value', { exact: true }).click();
    const fullDialog = await fullValue;
    expect(Array.from(fullDialog.message()).length).toBeGreaterThan(150);
    expect(fullDialog.message()).toContain('😀');
    await fullDialog.dismiss();
    await showFull;

    await page.locator('.tabulator-row').first().locator('.tabulator-cell').first().click({ button: 'right' });
    const copy = page.locator('.tabulator-menu-item').getByText('Row Copy row', { exact: true });
    await copy.click();
    const copied = JSON.parse(await page.evaluate(() => navigator.clipboard.readText())) as unknown[];
    expect(copied).toHaveLength(5);
    expect(copied[4]).toBeNull();
    expect(Array.from(String(copied[3])).length).toBeGreaterThan(150);

    await column(page, 'row_id').click({ button: 'right' });
    const baselineMenu = page.locator('.tabulator-menu');
    const baselineFontSize = await baselineMenu.evaluate((node) => getComputedStyle(node).fontSize);
    const baselineWidth = (await baselineMenu.boundingBox())!.width;
    const baselineSort = page.waitForRequest((item) => interfaceRequest(item, 'view_fetch'));
    await baselineMenu.locator('.tabulator-menu-item').getByText('Column Sort ascending', { exact: true }).click();
    await baselineSort;
    await page.keyboard.press('Meta+P');
    const palette = page.getByRole('dialog', { name: 'Command palette' });
    await palette.getByRole('textbox').fill('Text zoom: 125%');
    await page.keyboard.press('Enter');
    await column(page, 'row_id').click({ button: 'right' });
    const menu = page.locator('.tabulator-menu');
    const zoomedFontSize = await menu.evaluate((node) => getComputedStyle(node).fontSize);
    expect(zoomedFontSize).not.toBe(baselineFontSize);
    expect(await menu.locator('.tabulator-menu-item').count()).toBe(5);
    const textZoomSort = page.waitForRequest((item) => interfaceRequest(item, 'view_fetch'));
    await menu.locator('.tabulator-menu-item').getByText('Column Sort ascending', { exact: true }).click();
    await textZoomSort;
    await page.keyboard.press('Meta+P');
    await page.getByRole('dialog', { name: 'Command palette' }).getByRole('textbox').fill('Interface zoom: 125%');
    await page.keyboard.press('Enter');
    await column(page, 'row_id').click({ button: 'right' });
    expect((await page.locator('.tabulator-menu').boundingBox())!.width).toBeGreaterThan(baselineWidth * 1.1);

    expect(runs).toBe(1);
  } finally {
    await context.close();
  }
});
