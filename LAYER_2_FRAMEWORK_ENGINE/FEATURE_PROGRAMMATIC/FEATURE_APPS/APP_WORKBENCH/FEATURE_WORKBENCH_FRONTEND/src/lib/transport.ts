// CA-D-674@26
// CA-D-721@1
export interface OperationCaller {
  call<T>(name: string, arguments_: Record<string, unknown>): Promise<T>;
}

const HTTP_ROUTES: Record<string, string> = {
  query_run: 'run', query_check: 'check', query_page: 'page', query_schema: 'schema',
  workbench_status: 'status', workbench_archive_load: 'archive-load', query_load: 'load', query_saved_list: 'saved-list',
};

const INTERFACE_OPERATIONS = new Set([
  'workspace_open', 'workspace_list', 'workspace_get', 'view_create', 'view_list', 'view_get',
  'view_duplicate', 'view_update', 'view_run', 'view_check', 'view_fetch', 'view_focus', 'view_rename',
  'view_remove', 'query_log_list', 'query_log_get',
]);

export class HttpOperationCaller implements OperationCaller {
  constructor(private readonly base: string, private readonly projectRoot: string | null) {}

  call<T>(name: string, arguments_: Record<string, unknown>): Promise<T> {
    if (INTERFACE_OPERATIONS.has(name) || (name === 'view_save' && 'workspace_id' in arguments_)) {
      return this.post('interface', { operation: name, arguments: arguments_ });
    }
    if (name === 'view_save') return this.post('view-save', arguments_);
    const path = HTTP_ROUTES[name];
    if (!path) return Promise.reject(new Error(`Unsupported Workbench operation: ${name}`));
    return this.post(path, arguments_);
  }

  private async post<T>(path: string, body: Record<string, unknown>): Promise<T> {
    const apiBase = this.base.replace(/^\/caprmedio\/workbench\/([^/]+)$/, '/caprmedio/$1/api');
    const response = await fetch(`${apiBase}/${path}`, {
      method: 'POST', headers: { 'content-type': 'application/json' },
      body: JSON.stringify(this.projectRoot ? { ...body, project_root: this.projectRoot } : body),
    });
    const value = await response.json() as T | Record<string, unknown>;
    if (!response.ok) {
      const details = value as Record<string, unknown>;
      throw new Error(typeof details.error === 'string' ? details.error : 'Request failed');
    }
    return value as T;
  }
}
