import type { OperationCaller } from './transport';
import type { WorkspaceState } from './types';

type JsonObject = Record<string, unknown>;
type NativeWorkspaceState = WorkspaceState & { project_name: string };

export type NativeBootstrap = {
  sessionId: string;
  projectRoot: string;
  workspace: NativeWorkspaceState;
};

const object = (value: unknown): JsonObject | undefined => value !== null && typeof value === 'object' && !Array.isArray(value)
  ? value as JsonObject : undefined;
const nonEmpty = (value: unknown): string | undefined => typeof value === 'string' && value.trim() ? value : undefined;

function workspace(value: unknown): NativeWorkspaceState | undefined {
  const candidate = object(value);
  const workspaceId = nonEmpty(candidate?.workspace_id);
  const activeViewId = nonEmpty(candidate?.active_view_id);
  const projectName = nonEmpty(candidate?.project_name);
  return candidate && workspaceId && Array.isArray(candidate.views) && activeViewId && projectName
    ? { ...candidate, workspace_id: workspaceId, active_view_id: activeViewId, project_name: projectName } as NativeWorkspaceState
    : undefined;
}

export class McpAppTransport implements OperationCaller {
  private readonly pending = new Map<number, { resolve: (value: unknown) => void; reject: (error: Error) => void }>();
  private readonly initial: Promise<NativeBootstrap>;
  private resolveInitial!: (value: NativeBootstrap) => void;
  private rejectInitial!: (error: Error) => void;
  private nextId = 1;
  private initialized = false;
  private failed = false;
  private input?: Pick<NativeBootstrap, 'sessionId' | 'projectRoot'>;
  private initialWorkspace?: NativeWorkspaceState;

  constructor(private readonly host: Window = window.parent) {
    this.initial = new Promise((resolve, reject) => { this.resolveInitial = resolve; this.rejectInitial = reject; });
    window.addEventListener('message', this.receive);
  }

  async initialize(): Promise<NativeBootstrap> {
    try {
      await this.request('ui/initialize', {
        appInfo: { name: 'CAPRMEDIO Workbench', version: '0.0.1' },
        appCapabilities: {}, protocolVersion: '2026-01-26',
      });
      this.initialized = true;
      this.host.postMessage({ jsonrpc: '2.0', method: 'ui/notifications/initialized', params: {} }, '*');
      this.bindWhenReady();
    } catch (error) {
      this.fail(error instanceof Error ? error : new Error('MCP App initialization failed'));
    }
    return this.initial;
  }

  async call<T>(name: string, arguments_: Record<string, unknown>): Promise<T> {
    const projectRoot = this.input?.projectRoot;
    if (!projectRoot) throw new Error('Native Workbench context is unavailable.');
    const result = object(await this.request('tools/call', {
      name, arguments: { ...arguments_, project_root: projectRoot },
    }));
    if (!result || result.isError === true) throw new Error('Workbench tool call failed.');
    if (!('structuredContent' in result)) throw new Error('Workbench tool result is missing structured content.');
    return result.structuredContent as T;
  }

  private request(method: string, params: JsonObject): Promise<unknown> {
    const id = this.nextId++;
    const plainParams = JSON.parse(JSON.stringify(params)) as JsonObject;
    return new Promise((resolve, reject) => {
      this.pending.set(id, { resolve, reject });
      this.host.postMessage({ jsonrpc: '2.0', id, method, params: plainParams }, '*');
    });
  }

  private receive = (event: MessageEvent<unknown>) => {
    if (event.source !== this.host) return;
    const message = object(event.data);
    if (!message || message.jsonrpc !== '2.0') return;
    if (message.method === 'ui/notifications/tool-input') { this.receiveInput(object(message.params)); return; }
    if (message.method === 'ui/notifications/tool-result') { this.receiveResult(object(message.params)); return; }
    if (typeof message.id !== 'number') return;
    const pending = this.pending.get(message.id);
    if (!pending) return;
    this.pending.delete(message.id);
    if (message.error) pending.reject(new Error(object(message.error)?.message as string || 'MCP App request failed.'));
    else pending.resolve(message.result);
  };

  private receiveInput(params: JsonObject | undefined) {
    if (this.failed || this.input) return;
    const arguments_ = object(params?.arguments);
    const sessionId = nonEmpty(arguments_?.session_id);
    const projectRoot = nonEmpty(arguments_?.project_root);
    if (!sessionId || !projectRoot) { this.fail(new Error('Native Workbench binding requires session_id and project_root.')); return; }
    this.input = { sessionId, projectRoot };
    this.bindWhenReady();
  }

  private receiveResult(params: JsonObject | undefined) {
    if (this.failed || this.initialWorkspace) return;
    if (params?.isError === true) { this.fail(new Error('Native Workbench opening failed.')); return; }
    const initialWorkspace = workspace(params?.structuredContent);
    if (!initialWorkspace) {
      const candidate = object(params?.structuredContent);
      const hasWorkspaceShape = !!candidate && !!nonEmpty(candidate.workspace_id)
        && Array.isArray(candidate.views) && !!nonEmpty(candidate.active_view_id);
      this.fail(new Error(hasWorkspaceShape
        ? 'Native Workbench binding requires the initial Workspace project name.'
        : 'Native Workbench binding requires the initial Workspace result.'));
      return;
    }
    this.initialWorkspace = initialWorkspace;
    this.bindWhenReady();
  }

  private bindWhenReady() {
    if (!this.initialized || this.failed || !this.input || !this.initialWorkspace) return;
    if (this.initialWorkspace.workspace_id !== this.input.sessionId) {
      this.fail(new Error('Native Workbench Workspace does not match the supplied session.'));
      return;
    }
    this.resolveInitial({ ...this.input, workspace: this.initialWorkspace });
  }

  private fail(error: Error) {
    if (this.failed) return;
    this.failed = true;
    this.rejectInitial(error);
  }
}
