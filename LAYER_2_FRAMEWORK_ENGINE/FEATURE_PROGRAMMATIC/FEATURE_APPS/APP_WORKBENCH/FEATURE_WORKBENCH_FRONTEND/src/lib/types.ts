// CA-R-2727@4
// CA-M-466@4
// CA-M-467@2
// CA-D-674@7
export type Column = { name: string; type: string };

export type QueryResult = {
  query_id: string;
  columns: Column[];
  rows: unknown[][];
  row_count: number;
  column_count: number;
  offset: number;
  page_size: number;
  has_more: boolean;
};

export type CheckResult = { valid: boolean; row_count: number; column_count: number };
