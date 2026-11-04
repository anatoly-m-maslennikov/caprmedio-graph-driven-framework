<!-- CA-M-469@1 -->
<script lang="ts">
  import { onMount } from 'svelte';
  type Theme = 'light' | 'dark' | 'system';
  const scales = [80, 90, 100, 110, 125, 150, 200];
  let { storageKey }: { storageKey: string } = $props();
  let theme = $state<Theme>('system');
  let scale = $state(100);
  let warning = $state('');
  function apply() { document.documentElement.dataset.theme = theme; document.documentElement.style.setProperty('--text-scale', String(scale / 100)); }
  function save() { try { localStorage.setItem(`${storageKey}:preferences`, JSON.stringify({ theme, scale })); warning = ''; } catch { warning = 'Browser preferences cannot be saved.'; } }
  function update() { apply(); save(); }
  onMount(() => {
    try { const saved = JSON.parse(localStorage.getItem(`${storageKey}:preferences`) ?? '{}') as { theme?: Theme; scale?: number }; if (saved.theme === 'light' || saved.theme === 'dark' || saved.theme === 'system') theme = saved.theme; if (scales.includes(saved.scale ?? 0)) scale = saved.scale!; } catch { warning = 'Browser preferences cannot be read.'; }
    apply();
  });
</script>
<div class="preferences">
  <fieldset>
    <legend>Appearance</legend>
    <label>Theme <select bind:value={theme} onchange={update} aria-label="Theme"><option value="system">System</option><option value="light">Light (Day)</option><option value="dark">Dark (Night)</option></select></label>
    <label>Text <select bind:value={scale} onchange={update} aria-label="Text size">{#each scales as value}<option value={value}>{value}%</option>{/each}</select></label>
  </fieldset>
  {#if warning}<span class="notice" role="status">{warning}</span>{/if}
</div>
