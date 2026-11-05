<!-- CA-R-2727@8 -->
<script lang="ts">
  type Tab = { id: string; title: string; name?: string; dirty: boolean };
  let { tabs, activeId, utility, renaming, onselect, onclose, onadd, onrename }: {
    tabs: Tab[]; activeId: string; utility: 'settings' | 'saved' | 'view'; renaming?: string;
    onselect: (id: string) => void;
    onclose: (id: string) => void; onadd: () => void; onrename: (id: string, name: string) => void;
  } = $props();
</script>

<div class="tab-strip" role="tablist" aria-label="Workbench views">
  {#each tabs as tab}
    <div class:active={utility === 'view' && tab.id === activeId} class="tab">
      {#if renaming === tab.id}
        <input aria-label="View name" value={tab.name ?? ''} onkeydown={(event) => { if (event.key === 'Enter') onrename(tab.id, event.currentTarget.value); if (event.key === 'Escape') onrename(tab.id, tab.name ?? ''); }} onblur={(event) => onrename(tab.id, event.currentTarget.value)} />
      {:else}
        <button type="button" role="tab" aria-selected={utility === 'view' && tab.id === activeId} onclick={() => onselect(tab.id)}>{tab.name || tab.title}{tab.dirty ? ' *' : ''}</button>
      {/if}
      <button class="tab-close" type="button" aria-label={`Close ${tab.name || tab.title}`} onclick={() => onclose(tab.id)}>×</button>
    </div>
  {/each}
  <button class="add-tab" type="button" aria-label="New View" onclick={onadd}>+</button>
</div>
