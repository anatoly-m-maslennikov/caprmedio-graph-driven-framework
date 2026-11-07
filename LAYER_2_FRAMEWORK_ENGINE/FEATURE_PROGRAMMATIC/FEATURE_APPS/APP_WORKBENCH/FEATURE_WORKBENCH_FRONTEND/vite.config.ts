import { svelte } from '@sveltejs/vite-plugin-svelte';
import { defineConfig } from 'vite';

const hotReload = process.env.CAPRMEDIO_HOT_RELOAD === '1';
const server = { hmr: hotReload, watch: hotReload ? undefined : null };

export default defineConfig(({ mode }) => mode === 'mcp-app' ? {
  server,
  plugins: [svelte()],
  build: {
    outDir: 'dist/.mcp-app-assets', emptyOutDir: true, cssCodeSplit: false, sourcemap: false,
    rollupOptions: { input: 'src/mcp-app.ts', output: { entryFileNames: 'mcp-app.js', assetFileNames: 'mcp-app.[ext]', inlineDynamicImports: true } },
  },
} : {
  server,
  base: '/caprmedio/workbench/',
  plugins: [svelte()],
  build: { outDir: 'dist', emptyOutDir: true },
});
