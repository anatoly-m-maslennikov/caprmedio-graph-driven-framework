<!-- CA-R-2727@5 -->
<script lang="ts">
  type Tab = { id: string; title: string; dirty: boolean };
  let { tabs, activeId, onselect, onclose, onadd }: {
    tabs: Tab[]; activeId: string; onselect: (id: string) => void;
    onclose: (id: string) => void; onadd: () => void;
  } = $props();
</script>

<div class="tab-strip" role="tablist" aria-label="Worksheets">
  {#each tabs as tab}
    <div class:active={tab.id === activeId} class="tab">
      <button type="button" role="tab" aria-selected={tab.id === activeId} onclick={() => onselect(tab.id)}>
        {tab.title}{tab.dirty ? ' *' : ''}
      </button>
      <button class="tab-close" type="button" aria-label={`Close ${tab.title}`} onclick={() => onclose(tab.id)}>×</button>
    </div>
  {/each}
  <button class="add-tab" type="button" aria-label="New Worksheet" onclick={onadd}>+</button>
</div>
