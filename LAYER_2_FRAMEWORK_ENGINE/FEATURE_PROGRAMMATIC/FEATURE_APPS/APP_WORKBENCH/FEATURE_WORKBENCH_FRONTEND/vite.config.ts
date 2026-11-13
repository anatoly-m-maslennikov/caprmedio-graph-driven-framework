// CA-M-466@9
// CA-M-551@2
import { svelte } from '@sveltejs/vite-plugin-svelte';
import { defineConfig } from 'vite';

const server = { hmr: false as const, watch: null };

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
