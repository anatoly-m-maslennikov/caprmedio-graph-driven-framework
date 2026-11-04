// CA-R-2727@3
// CA-M-466@3
// CA-M-467@2
// CA-D-674@6
import { svelte } from '@sveltejs/vite-plugin-svelte';
import { defineConfig } from 'vite';

export default defineConfig({
  base: '/caprmedio/workbench/',
  plugins: [svelte()],
  build: { outDir: 'dist', emptyOutDir: true }
});
