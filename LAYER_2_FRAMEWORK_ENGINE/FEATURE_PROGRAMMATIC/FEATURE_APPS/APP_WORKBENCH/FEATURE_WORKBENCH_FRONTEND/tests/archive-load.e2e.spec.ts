import { expect, test } from '@playwright/test';

test('loads only submitted Archive scopes and displays their returned coverage', async ({ page }) => {
  const url = new URL(process.env.WORKBENCH_E2E_URL!);
  url.searchParams.set('project_root', '/fixture/project');
  url.searchParams.delete('workspace');
  const requested = [
    { scope_unit: 'WORKBENCH_BACKEND', role: 'Requirement' },
    { scope_unit: 'CA-SU-14', role: 'Plan' },
  ];
  const canonical = [requested[0], { scope_unit: 'FRAMEWORK_ENGINE', role: 'Plan' }];
  const requests: unknown[] = [];
  let loaded: typeof canonical = [];
  await page.route('**/interface', (route) => {
    const { operation, arguments: args } = route.request().postDataJSON();
    const json = operation === 'query_log_list' ? { items: [] } : {
      workspace_id: args.session_id ?? args.workspace_id,
      project_name: 'Fixture Project',
      active_view_id: 'fixture-view',
      views: [{ id: 'fixture-view', sql: '', cursor_position: 0, revision: 0 }],
    };
    return route.fulfill({ json });
  });
  await page.route('**/schema', (route) => route.fulfill({ json: { tables: {} } }));
  await page.route('**/saved-list', (route) => route.fulfill({ json: { items: [] } }));
  await page.route('**/status', (route) => route.fulfill({
    json: { syncing: false, last_synced_at: null, loaded_archive_scopes: loaded },
  }));
  await page.route('**/archive-load', (route) => {
    requests.push(route.request().postDataJSON());
    if (requests.length === 1) return route.fulfill({ status: 400, json: { error: 'Archive load rejected.' } });
    loaded = canonical;
    return route.fulfill({ json: { loaded_archive_scopes: loaded } });
  });

  await page.goto(url.toString());
  const commands = page.getByRole('button', { name: /^Commands/ });
  await commands.click();
  await page.getByRole('dialog', { name: 'Command palette' })
    .getByRole('button', { name: 'Load Archives', exact: true }).click();
  const dialog = page.getByRole('dialog', { name: 'Load Archives' });
  const load = dialog.getByRole('button', { name: 'Load', exact: true });
  await expect(dialog.getByText('None loaded.')).toBeVisible();
  await expect(load).toBeDisabled();
  await dialog.getByRole('textbox', { name: 'Scope Unit 1' }).fill('  WORKBENCH_BACKEND  ');
  await dialog.getByRole('textbox', { name: 'Role 1' }).fill('Requirement');
  await dialog.getByRole('button', { name: 'Add scope' }).click();
  await dialog.getByRole('textbox', { name: 'Scope Unit 2' }).fill('CA-SU-14');
  await dialog.getByRole('textbox', { name: 'Role 2' }).fill('Plan');
  expect(requests).toEqual([]);

  await load.click();
  await expect(dialog.getByRole('alert')).toHaveText('Archive load rejected.');
  await expect(dialog.getByRole('textbox', { name: 'Scope Unit 2' })).toHaveValue('CA-SU-14');
  await load.click();
  const coverage = dialog.getByRole('region', { name: 'Loaded Archive scopes' });
  await expect(coverage.getByRole('listitem')).toHaveText(['WORKBENCH_BACKEND / Requirement', 'FRAMEWORK_ENGINE / Plan']);
  expect(requests).toEqual(Array(2).fill({ scopes: requested, project_root: '/fixture/project' }));
  await expect(load).toBeDisabled();
  await dialog.getByRole('button', { name: 'Close' }).click();
  await expect(dialog).toBeHidden();
});
