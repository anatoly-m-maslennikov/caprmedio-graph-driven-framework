// CA-D-674@26
import type { ArchiveScope, CheckResult, GridState, QueryResult, QueryLogItem, SavedIdentity, SavedItem, Schema, SourceSyncStatus, ViewRunResponse, WorkspaceState, WorkspaceView } from './types';
import type { OperationCaller } from './transport';

export class WorkbenchApi {
  constructor(private readonly caller: OperationCaller) {}

  run(sql: string, cursorPosition: number, options: { save?: boolean; name?: string } = {}): Promise<QueryResult> {
    return this.caller.call('query_run', { result_delivery: 'inline', sql, cursor_position: cursorPosition, page_size: 100, ...options });
  }

  check(sql: string, cursorPosition: number): Promise<CheckResult> {
    return this.caller.call('query_check', { sql, cursor_position: cursorPosition });
  }

  saveView(sql: string, name?: string): Promise<SavedIdentity> {
    return this.caller.call('view_save', { sql, ...(name ? { name } : {}) });
  }

  page(queryId: string, offset: number, pageSize: number, grid?: GridState): Promise<QueryResult> {
    return this.caller.call('query_page', { result_delivery: 'inline', query_id: queryId, offset, page_size: pageSize, ...(grid ? { grid } : {}) });
  }

  schema(): Promise<Schema> { return this.caller.call('query_schema', {}); }
  status(): Promise<SourceSyncStatus> { return this.caller.call('workbench_status', {}); }
  loadArchives(scopes: ArchiveScope[]): Promise<{ loaded_archive_scopes: ArchiveScope[] }> {
    return this.caller.call('workbench_archive_load', { scopes });
  }
  load(reference: string): Promise<SavedIdentity> { return this.caller.call('query_load', { reference }); }
  savedList(): Promise<{ items: SavedItem[] }> { return this.caller.call('query_saved_list', { limit: 20 }); }
}

export class WorkspaceApi {
  constructor(private readonly caller: OperationCaller, readonly workspaceId: string) {}

  open(): Promise<WorkspaceState> { return this.caller.call('workspace_open', { session_id: this.workspaceId }); }
  get(): Promise<WorkspaceState> { return this.caller.call('workspace_get', { workspace_id: this.workspaceId }); }
  create(position: 'first' | 'last' = 'last', name?: string): Promise<WorkspaceState & { view_id: string }> {
    return this.caller.call('view_create', { workspace_id: this.workspaceId, position, ...(name ? { name } : {}) });
  }
  duplicate(viewId: string): Promise<WorkspaceState & { view_id: string }> {
    return this.caller.call('view_duplicate', { workspace_id: this.workspaceId, view_id: viewId });
  }
  update(viewId: string, sql: string, expectedRevision: number, cursorPosition: number): Promise<WorkspaceView> {
    return this.caller.call('view_update', { workspace_id: this.workspaceId, view_id: viewId, sql, expected_revision: expectedRevision, cursor_position: cursorPosition });
  }
  run(viewId: string, cursorPosition: number, options: { save?: boolean; name?: string } = {}): Promise<ViewRunResponse> {
    return this.caller.call('view_run', { workspace_id: this.workspaceId, view_id: viewId, cursor_position: cursorPosition, ...options });
  }
  check(viewId: string, cursorPosition: number): Promise<CheckResult> {
    return this.caller.call('view_check', { workspace_id: this.workspaceId, view_id: viewId, cursor_position: cursorPosition });
  }
  fetch(viewId: string, offset = 0, pageSize = 100, grid?: GridState): Promise<QueryResult> {
    return this.caller.call('view_fetch', { result_delivery: 'inline', workspace_id: this.workspaceId, view_id: viewId, offset, page_size: pageSize, ...(grid ? { grid } : {}) });
  }
  focus(viewId: string): Promise<{ workspace_id: string; active_view_id: string }> { return this.caller.call('view_focus', { workspace_id: this.workspaceId, view_id: viewId }); }
  rename(viewId: string, name: string): Promise<WorkspaceView> { return this.caller.call('view_rename', { workspace_id: this.workspaceId, view_id: viewId, name }); }
  remove(viewId: string): Promise<{ workspace_id: string; active_view_id: string; views: Array<Pick<WorkspaceView, 'id' | 'name' | 'revision' | 'result'>> }> { return this.caller.call('view_remove', { workspace_id: this.workspaceId, view_id: viewId }); }
  save(viewId: string): Promise<SavedIdentity> { return this.caller.call('view_save', { workspace_id: this.workspaceId, view_id: viewId }); }
  queryLogList(): Promise<{ items: QueryLogItem[] }> { return this.caller.call('query_log_list', { limit: 20 }); }
  queryLogGet(logId: string): Promise<QueryLogItem> { return this.caller.call('query_log_get', { log_id: logId }); }
}
