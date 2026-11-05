// CA-R-2729@7
// CA-R-2776@4
// CA-D-673@11
// CA-R-2791@1
// CA-D-680@1
import type { CheckResult, QueryResult, QueryLogItem, SavedIdentity, SavedItem, Schema, ViewRunResponse, WorkspaceState, WorkspaceView } from './types';

export class WorkbenchApi {
  constructor(private readonly base: string, private readonly projectRoot: string | null) {}

  private async post<T>(path: string, body: Record<string, unknown>): Promise<T> {
    const response = await fetch(`${this.base}/${path}`, {
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

  run(sql: string, cursorPosition: number, options: { save?: boolean; name?: string } = {}): Promise<QueryResult> {
    return this.post('run', { sql, cursor_position: cursorPosition, page_size: 100, ...options });
  }

  check(sql: string, cursorPosition: number): Promise<CheckResult> {
    return this.post('check', { sql, cursor_position: cursorPosition });
  }

  saveView(sql: string, name?: string): Promise<SavedIdentity> {
    return this.post('view-save', { sql, ...(name ? { name } : {}) });
  }

  page(queryId: string, offset: number, pageSize: number): Promise<QueryResult> {
    return this.post('page', { query_id: queryId, offset, page_size: pageSize });
  }

  schema(): Promise<Schema> { return this.post('schema', {}); }
  load(reference: string): Promise<SavedIdentity> { return this.post('load', { reference }); }
  savedList(): Promise<{ items: SavedItem[] }> { return this.post('saved-list', { limit: 20 }); }
}

// CA-R-2902@1
// CA-D-681@1
export class WorkspaceApi {
  constructor(
    private readonly base: string, private readonly projectRoot: string | null, readonly workspaceId: string,
  ) {}

  private async call<T>(operation: string, arguments_: Record<string, unknown>): Promise<T> {
    const response = await fetch(`${this.base}/interface`, {
      method: 'POST', headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ operation, arguments: arguments_, ...(this.projectRoot ? { project_root: this.projectRoot } : {}) }),
    });
    const value = await response.json() as T | Record<string, unknown>;
    if (!response.ok) {
      const details = value as Record<string, unknown>;
      throw new Error(typeof details.error === 'string' ? details.error : 'Request failed');
    }
    return value as T;
  }

  open(): Promise<WorkspaceState> { return this.call('workspace_open', { session_id: this.workspaceId }); }
  get(): Promise<WorkspaceState> { return this.call('workspace_get', { workspace_id: this.workspaceId }); }
  create(position: 'first' | 'last' = 'last', name?: string): Promise<WorkspaceState & { view_id: string }> {
    return this.call('view_create', { workspace_id: this.workspaceId, position, ...(name ? { name } : {}) });
  }
  update(viewId: string, sql: string, expectedRevision: number, cursorPosition: number): Promise<WorkspaceView> {
    return this.call('view_update', { workspace_id: this.workspaceId, view_id: viewId, sql, expected_revision: expectedRevision, cursor_position: cursorPosition });
  }
  run(viewId: string, cursorPosition: number, options: { save?: boolean; name?: string } = {}): Promise<ViewRunResponse> {
    return this.call('view_run', { workspace_id: this.workspaceId, view_id: viewId, cursor_position: cursorPosition, ...options });
  }
  check(viewId: string, cursorPosition: number): Promise<CheckResult> {
    return this.call('view_check', { workspace_id: this.workspaceId, view_id: viewId, cursor_position: cursorPosition });
  }
  fetch(viewId: string, offset = 0, pageSize = 100): Promise<QueryResult> {
    return this.call('view_fetch', { workspace_id: this.workspaceId, view_id: viewId, offset, page_size: pageSize });
  }
  focus(viewId: string): Promise<{ workspace_id: string; active_view_id: string }> { return this.call('view_focus', { workspace_id: this.workspaceId, view_id: viewId }); }
  rename(viewId: string, name: string): Promise<WorkspaceView> { return this.call('view_rename', { workspace_id: this.workspaceId, view_id: viewId, name }); }
  remove(viewId: string): Promise<{ workspace_id: string; active_view_id: string; views: Array<Pick<WorkspaceView, 'id' | 'name' | 'revision' | 'result'>> }> { return this.call('view_remove', { workspace_id: this.workspaceId, view_id: viewId }); }
  save(viewId: string): Promise<SavedIdentity> { return this.call('view_save', { workspace_id: this.workspaceId, view_id: viewId }); }
  queryLogList(): Promise<{ items: QueryLogItem[] }> { return this.call('query_log_list', { limit: 20 }); }
  queryLogGet(logId: string): Promise<QueryLogItem> { return this.call('query_log_get', { log_id: logId }); }
}
