import { svelte } from '@sveltejs/vite-plugin-svelte';
import { defineConfig } from 'vite';

export default defineConfig(({ mode }) => mode === 'mcp-app' ? {
  plugins: [svelte()],
  build: {
    outDir: 'dist/.mcp-app-assets', emptyOutDir: true, cssCodeSplit: false, sourcemap: false,
    rollupOptions: { input: 'src/mcp-app.ts', output: { entryFileNames: 'mcp-app.js', assetFileNames: 'mcp-app.[ext]', inlineDynamicImports: true } },
  },
} : {
  base: '/caprmedio/workbench/',
  plugins: [svelte()],
  build: { outDir: 'dist', emptyOutDir: true },
});
