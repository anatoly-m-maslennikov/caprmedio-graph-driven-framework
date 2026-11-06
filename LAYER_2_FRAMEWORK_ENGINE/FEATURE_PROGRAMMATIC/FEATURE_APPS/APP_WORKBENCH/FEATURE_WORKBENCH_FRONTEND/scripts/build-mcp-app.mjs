import { build } from 'vite';
import { readdir, readFile, rm, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';

const root = process.cwd();
const assets = resolve(root, 'dist/.mcp-app-assets');
const output = resolve(root, 'dist/mcp-app.html');

await build({ configFile: resolve(root, 'vite.config.ts'), mode: 'mcp-app' });
const files = await readdir(assets);
const script = files.find((file) => file.endsWith('.js'));
const stylesheet = files.find((file) => file.endsWith('.css'));
if (!script || !stylesheet || files.some((file) => ![script, stylesheet].includes(file))) {
  throw new Error('MCP App build must produce exactly one JavaScript and one CSS asset.');
}
const [javascript, css] = await Promise.all([readFile(resolve(assets, script), 'utf8'), readFile(resolve(assets, stylesheet), 'utf8')]);
const inlineScript = javascript.replace(/<\/script/gi, '<\\/script');
const html = `<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>CAPRMEDIO Workbench</title><style>${css}</style><div id="app"></div><script type="module">${inlineScript}</script></html>`;
if (/<script\b[^>]*\bsrc=|<link\b[^>]*\brel=["']stylesheet/i.test(html)) throw new Error('MCP App must not reference external assets.');
await writeFile(output, html);
await rm(assets, { recursive: true, force: true });
