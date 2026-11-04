// CA-D-674@9
export type Column = { name: string; type: string; has_values?: boolean };

export type SavedIdentity = {
  saved_query_id: string;
  saved_query_url: string;
  kind: 'query' | 'worksheet';
  sql: string;
};

export type QueryResult = SavedIdentity & {
  query_id: string;
  columns: Column[];
  rows: unknown[][];
  row_count: number;
  column_count: number;
  offset: number;
  page_size: number;
  has_more: boolean;
};

export type CheckResult = SavedIdentity & { valid: boolean; row_count: number; column_count: number };
export type Schema = { tables: Record<string, Array<{ name: string; type: string }>> };
export type SavedItem = {
  saved_query_id: string;
  saved_query_url: string;
  kind: 'query' | 'worksheet';
  preview: string;
  saved_at: string;
};
