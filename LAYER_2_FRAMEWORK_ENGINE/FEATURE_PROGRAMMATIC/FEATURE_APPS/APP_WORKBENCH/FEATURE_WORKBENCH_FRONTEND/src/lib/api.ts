// CA-D-673@8
import type { CheckResult, QueryResult, SavedIdentity, SavedItem, Schema } from './types';

export class ApiError extends Error {
  constructor(message: string, readonly details: Record<string, unknown>) { super(message); }
}

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
      throw new ApiError(typeof details.error === 'string' ? details.error : 'Request failed', details);
    }
    return value as T;
  }

  run(sql: string, cursorPosition: number): Promise<QueryResult> {
    return this.post('run', { sql, cursor_position: cursorPosition, page_size: 100 });
  }

  check(sql: string, cursorPosition: number): Promise<CheckResult> {
    return this.post('check', { sql, cursor_position: cursorPosition });
  }

  save(sql: string, cursorPosition: number): Promise<SavedIdentity> {
    return this.post('save', { sql, cursor_position: cursorPosition });
  }

  saveWorksheet(sql: string): Promise<SavedIdentity> {
    return this.post('worksheet-save', { sql });
  }

  page(queryId: string, offset: number, pageSize: number): Promise<QueryResult> {
    return this.post('page', { query_id: queryId, offset, page_size: pageSize });
  }

  schema(): Promise<Schema> { return this.post('schema', {}); }
  load(reference: string): Promise<SavedIdentity> { return this.post('load', { reference }); }
  savedList(): Promise<{ items: SavedItem[] }> { return this.post('saved-list', { limit: 20 }); }
}
