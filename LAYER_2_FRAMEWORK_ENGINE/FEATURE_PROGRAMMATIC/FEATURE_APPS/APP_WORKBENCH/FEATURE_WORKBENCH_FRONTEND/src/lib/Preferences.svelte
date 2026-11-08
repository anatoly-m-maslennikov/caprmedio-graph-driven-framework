<!-- CA-M-469@8 -->
<script lang="ts">
  import { onMount } from 'svelte';
  import type { ResultDisplayPreferences } from './types';

  export type PreferenceCommand = { id: string; label: string; run: () => void };
  type Theme = 'light' | 'dark' | 'system'; type Density = 'compact' | 'comfortable';
  type SavedPreferences = { theme?: Theme; textZoom?: number; contentZoom?: number; interfaceZoom?: number; density?: Density; scale?: number; resultDisplay?: Partial<ResultDisplayPreferences> };
  const scales = [80, 90, 100, 110, 125, 150, 200];
  let { storageKey, embedded = false, visible = false, resultDisplay, onresultdisplaychange, onlayoutchange, oncommands }: {
    storageKey: string; embedded?: boolean; visible?: boolean; resultDisplay: ResultDisplayPreferences;
    onresultdisplaychange: (next: ResultDisplayPreferences) => void; onlayoutchange?: () => void;
    oncommands?: (commands: PreferenceCommand[]) => void;
  } = $props();
  let theme = $state<Theme>('system'); let textZoom = $state(100); let contentZoom = $state(100); let interfaceZoom = $state(100); let density = $state<Density>('comfortable'); let warning = $state(''); let ready = false;
  const positive = (value: unknown, maximum?: number) => Number.isInteger(value) && Number(value) > 0 && (maximum === undefined || Number(value) <= maximum);
  function apply() { document.documentElement.dataset.theme = theme; document.documentElement.dataset.density = density; document.documentElement.style.setProperty('--interface-text-scale', String(textZoom / 100)); document.documentElement.style.setProperty('--content-text-scale', String(contentZoom / 100)); document.documentElement.style.setProperty('--interface-scale', String(interfaceZoom / 100)); }
  function save() { if (!ready) return; try { localStorage.setItem(`${storageKey}:preferences`, JSON.stringify({ theme, textZoom, contentZoom, interfaceZoom, density, resultDisplay })); warning = ''; } catch { warning = 'Browser preferences cannot be saved.'; } }
  function layout() { apply(); save(); onlayoutchange?.(); }
  function setTheme(value: Theme) { theme = value; layout(); }
  function setTextZoom(value: number) { textZoom = value; layout(); }
  function setContentZoom(value: number) { contentZoom = value; layout(); }
  function setInterfaceZoom(value: number) { interfaceZoom = value; layout(); }
  function setDensity(value: Density) { density = value; layout(); }
  function setDisplay(next: Partial<ResultDisplayPreferences>) { onresultdisplaychange({ ...resultDisplay, ...next }); }
  function fixedInput(value: string) { const next = Number(value); if (positive(next, 1000)) setDisplay({ fixedPageSize: next }); }
  function limitInput(value: string) { const next = Number(value); if (positive(next)) setDisplay({ contentLimit: next }); }
  function askFixed() { const value = window.prompt('Rows per page (1-1000)', String(resultDisplay.fixedPageSize)); if (value !== null) fixedInput(value); }
  function askLimit() { const value = window.prompt('Content character limit', String(resultDisplay.contentLimit)); if (value !== null) limitInput(value); }
  function commands() { return [
    ...(['system', 'light', 'dark'] as Theme[]).map((value) => ({ id: `theme-${value}`, label: `Theme: ${value === 'system' ? 'System' : value === 'light' ? 'Light (Day)' : 'Dark (Night)'}`, run: () => setTheme(value) })),
    ...scales.map((value) => ({ id: `interface-text-zoom-${value}`, label: `Interface text zoom: ${value}%`, run: () => setTextZoom(value) })),
    ...scales.map((value) => ({ id: `content-text-zoom-${value}`, label: `Content text zoom: ${value}%`, run: () => setContentZoom(value) })),
    ...scales.map((value) => ({ id: `interface-zoom-${value}`, label: `Interface zoom: ${value}%`, run: () => setInterfaceZoom(value) })),
    ...(['compact', 'comfortable'] as Density[]).map((value) => ({ id: `density-${value}`, label: `Density: ${value}`, run: () => setDensity(value) })),
    { id: 'rows-adaptive', label: 'Result rows: Adaptive', run: () => setDisplay({ rowSizing: 'adaptive' }) }, { id: 'rows-fixed', label: 'Result rows: Fixed', run: () => setDisplay({ rowSizing: 'fixed' }) }, { id: 'rows-fixed-value', label: 'Set fixed rows per page', run: askFixed },
    { id: 'content-limited', label: 'Cell content: Limited', run: () => setDisplay({ content: 'limited' }) }, { id: 'content-full', label: 'Cell content: Full', run: () => setDisplay({ content: 'full' }) }, { id: 'content-limit', label: 'Set content character limit', run: askLimit },
  ]; }
  $effect(() => { resultDisplay; save(); });
  onMount(() => {
    density = embedded ? 'compact' : 'comfortable';
    try {
      const saved = JSON.parse(localStorage.getItem(`${storageKey}:preferences`) ?? '{}') as SavedPreferences;
      if (saved.theme === 'light' || saved.theme === 'dark' || saved.theme === 'system') theme = saved.theme;
      const legacyTextZoom = saved.textZoom ?? saved.scale;
      if (scales.includes(legacyTextZoom ?? 0)) { textZoom = legacyTextZoom!; contentZoom = legacyTextZoom!; }
      if (scales.includes(saved.contentZoom ?? 0)) contentZoom = saved.contentZoom!;
      if (scales.includes(saved.interfaceZoom ?? 0)) interfaceZoom = saved.interfaceZoom!;
      if (saved.density === 'compact' || saved.density === 'comfortable') density = saved.density;
      const display = saved.resultDisplay;
      if (display && (display.rowSizing === 'adaptive' || display.rowSizing === 'fixed') && positive(display.fixedPageSize, 1000) && (display.content === 'limited' || display.content === 'full') && positive(display.contentLimit)) onresultdisplaychange({ rowSizing: display.rowSizing, fixedPageSize: display.fixedPageSize, content: display.content, contentLimit: display.contentLimit });
    } catch { warning = 'Browser preferences cannot be read.'; }
    ready = true; apply(); save(); onlayoutchange?.(); oncommands?.(commands());
  });
</script>
{#if visible}
  <section class="preferences" aria-label="Settings">
    <label>Theme <select value={theme} onchange={(event) => setTheme((event.currentTarget as HTMLSelectElement).value as Theme)} aria-label="Theme"><option value="system">System</option><option value="light">Light (Day)</option><option value="dark">Dark (Night)</option></select></label>
    <label>Interface text zoom <select value={textZoom} onchange={(event) => setTextZoom(Number((event.currentTarget as HTMLSelectElement).value))} aria-label="Interface text zoom">{#each scales as value}<option value={value}>{value}%</option>{/each}</select></label>
    <label>Content text zoom <select value={contentZoom} onchange={(event) => setContentZoom(Number((event.currentTarget as HTMLSelectElement).value))} aria-label="Content text zoom">{#each scales as value}<option value={value}>{value}%</option>{/each}</select></label>
    <label>Interface zoom <select value={interfaceZoom} onchange={(event) => setInterfaceZoom(Number((event.currentTarget as HTMLSelectElement).value))} aria-label="Interface zoom">{#each scales as value}<option value={value}>{value}%</option>{/each}</select></label>
    <label>Density <select value={density} onchange={(event) => setDensity((event.currentTarget as HTMLSelectElement).value as Density)} aria-label="Density"><option value="compact">Compact</option><option value="comfortable">Comfortable</option></select></label>
    <fieldset><legend>Rows per page</legend><label><input type="radio" name="row-sizing" checked={resultDisplay.rowSizing === 'adaptive'} onchange={() => setDisplay({ rowSizing: 'adaptive' })} /> Adaptive</label><label><input type="radio" name="row-sizing" checked={resultDisplay.rowSizing === 'fixed'} onchange={() => setDisplay({ rowSizing: 'fixed' })} /> Fixed</label>{#if resultDisplay.rowSizing === 'fixed'}<label>Fixed rows <input aria-label="Fixed rows per page" type="number" min="1" max="1000" step="1" value={resultDisplay.fixedPageSize} oninput={(event) => fixedInput(event.currentTarget.value)} /></label>{/if}</fieldset>
    <fieldset><legend>Cell content</legend><label><input type="radio" name="content-mode" checked={resultDisplay.content === 'limited'} onchange={() => setDisplay({ content: 'limited' })} /> Limited</label><label><input type="radio" name="content-mode" checked={resultDisplay.content === 'full'} onchange={() => setDisplay({ content: 'full' })} /> Full</label>{#if resultDisplay.content === 'limited'}<label>Character limit <input aria-label="Content character limit" type="number" min="1" step="1" value={resultDisplay.contentLimit} oninput={(event) => limitInput(event.currentTarget.value)} /></label>{/if}</fieldset>
    {#if warning}<span class="notice" role="status">{warning}</span>{/if}
  </section>
{/if}
