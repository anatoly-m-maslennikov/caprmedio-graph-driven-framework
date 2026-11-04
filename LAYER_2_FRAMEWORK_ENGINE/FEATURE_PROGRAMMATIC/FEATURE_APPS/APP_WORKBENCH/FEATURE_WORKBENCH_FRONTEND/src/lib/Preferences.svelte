<!-- CA-M-469@3 -->
<script lang="ts">
  import { onMount } from 'svelte';
  export type PreferenceCommand = { id: string; label: string; run: () => void };
  type Theme = 'light' | 'dark' | 'system';
  const scales = [80, 90, 100, 110, 125, 150, 200];
  let { storageKey, visible = false, oncommands }: { storageKey: string; visible?: boolean; oncommands?: (commands: PreferenceCommand[]) => void } = $props();
  let theme = $state<Theme>('system');
  let scale = $state(100);
  let warning = $state('');
  function apply() { document.documentElement.dataset.theme = theme; document.documentElement.style.setProperty('--text-scale', String(scale / 100)); }
  function save() { try { localStorage.setItem(`${storageKey}:preferences`, JSON.stringify({ theme, scale })); warning = ''; } catch { warning = 'Browser preferences cannot be saved.'; } }
  function setTheme(value: Theme) { theme = value; apply(); save(); }
  function setScale(value: number) { scale = value; apply(); save(); }
  function commands() { return [
    ...(['system', 'light', 'dark'] as Theme[]).map((value) => ({ id: `theme-${value}`, label: `Theme: ${value === 'system' ? 'System' : value === 'light' ? 'Light (Day)' : 'Dark (Night)'}`, run: () => setTheme(value) })),
    ...scales.map((value) => ({ id: `zoom-${value}`, label: `Zoom: ${value}%`, run: () => setScale(value) })),
  ]; }
  onMount(() => {
    try { const saved = JSON.parse(localStorage.getItem(`${storageKey}:preferences`) ?? '{}') as { theme?: Theme; scale?: number }; if (saved.theme === 'light' || saved.theme === 'dark' || saved.theme === 'system') theme = saved.theme; if (scales.includes(saved.scale ?? 0)) scale = saved.scale!; } catch { warning = 'Browser preferences cannot be read.'; }
    apply(); oncommands?.(commands());
  });
</script>
{#if visible}
  <section class="preferences" aria-label="Settings">
    <label>Theme <select value={theme} onchange={(event) => setTheme((event.currentTarget as HTMLSelectElement).value as Theme)} aria-label="Theme"><option value="system">System</option><option value="light">Light (Day)</option><option value="dark">Dark (Night)</option></select></label>
    <label>Zoom <select value={scale} onchange={(event) => setScale(Number((event.currentTarget as HTMLSelectElement).value))} aria-label="Zoom">{#each scales as value}<option value={value}>{value}%</option>{/each}</select></label>
    {#if warning}<span class="notice" role="status">{warning}</span>{/if}
  </section>
{/if}
