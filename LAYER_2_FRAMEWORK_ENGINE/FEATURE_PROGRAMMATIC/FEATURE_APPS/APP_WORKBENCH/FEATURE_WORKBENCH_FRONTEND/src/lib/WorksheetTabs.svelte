<!-- CA-R-2727@7 -->
<script lang="ts">
  type Tab = { id: string; title: string; name?: string; dirty: boolean };
  let { tabs, activeId, utility, renaming, onutility, onselect, onclose, onadd, onrename }: {
    tabs: Tab[]; activeId: string; utility: 'settings' | 'saved' | 'worksheet'; renaming?: string;
    onutility: (view: 'settings' | 'saved') => void; onselect: (id: string) => void;
    onclose: (id: string) => void; onadd: () => void; onrename: (id: string, name: string) => void;
  } = $props();
</script>

<div class="tab-strip" role="tablist" aria-label="Workbench views">
  <button class:active={utility === 'settings'} type="button" role="tab" aria-selected={utility === 'settings'} onclick={() => onutility('settings')}>Settings</button>
  <button class:active={utility === 'saved'} type="button" role="tab" aria-label="Saved Queries and Worksheets" title="Saved Queries and Worksheets" aria-selected={utility === 'saved'} onclick={() => onutility('saved')}>Saved</button>
  {#each tabs as tab}
    <div class:active={utility === 'worksheet' && tab.id === activeId} class="tab">
      {#if renaming === tab.id}
        <input aria-label="Worksheet name" value={tab.name ?? ''} onkeydown={(event) => { if (event.key === 'Enter') onrename(tab.id, event.currentTarget.value); if (event.key === 'Escape') onrename(tab.id, tab.name ?? ''); }} onblur={(event) => onrename(tab.id, event.currentTarget.value)} />
      {:else}
        <button type="button" role="tab" aria-selected={utility === 'worksheet' && tab.id === activeId} onclick={() => onselect(tab.id)}>{tab.name || tab.title}{tab.dirty ? ' *' : ''}</button>
      {/if}
      <button class="tab-close" type="button" aria-label={`Close ${tab.name || tab.title}`} onclick={() => onclose(tab.id)}>×</button>
    </div>
  {/each}
  <button class="add-tab" type="button" aria-label="New Worksheet" onclick={onadd}>+</button>
</div>
