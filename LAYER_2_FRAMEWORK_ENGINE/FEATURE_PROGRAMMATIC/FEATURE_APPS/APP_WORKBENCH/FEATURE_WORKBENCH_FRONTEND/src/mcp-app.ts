// CA-R-2902@4
// CA-M-476@4
import { mount } from 'svelte';
import App from './App.svelte';
import './app.css';
import { McpAppTransport } from './lib/mcp_app_transport';

const target = document.getElementById('app')!;
const bridge = new McpAppTransport();

void bridge.initialize().then((native) => {
  mount(App, { target, props: { caller: bridge, native } });
}).catch((error: unknown) => {
  const failure = document.createElement('p');
  failure.className = 'error'; failure.setAttribute('role', 'alert');
  failure.textContent = error instanceof Error ? error.message : 'Native Workbench binding failed.';
  target.replaceChildren(failure);
});
