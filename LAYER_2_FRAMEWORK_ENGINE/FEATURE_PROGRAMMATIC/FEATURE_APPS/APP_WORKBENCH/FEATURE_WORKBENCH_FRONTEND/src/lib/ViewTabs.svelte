<!-- CA-R-2727@14 -->
<!-- CA-D-674@18 -->
<script lang="ts">
  type Tab = { id: string; title: string; name?: string; dirty: boolean };
  let { tabs, activeId, utility, onselect, onclose, onadd, onrenamerequest }: {
    tabs: Tab[]; activeId: string; utility: 'settings' | 'saved' | 'view';
    onselect: (id: string) => void;
    onclose: (id: string) => void; onadd: () => void; onrenamerequest: (id: string) => void;
  } = $props();
</script>

<div class="tab-strip" role="tablist" aria-label="Workbench views">
  {#each tabs as tab}
    <div class:active={utility === 'view' && tab.id === activeId} class="tab">
      <button type="button" role="tab" aria-selected={utility === 'view' && tab.id === activeId} onclick={() => onselect(tab.id)} ondblclick={() => onrenamerequest(tab.id)}>{tab.name || tab.title}{tab.dirty ? ' *' : ''}</button>
      <button class="tab-close" type="button" aria-label={`Close ${tab.name || tab.title}`} onclick={() => onclose(tab.id)}>×</button>
    </div>
  {/each}
  <button class="add-tab" type="button" aria-label="New View" onclick={onadd}>+</button>
</div>
