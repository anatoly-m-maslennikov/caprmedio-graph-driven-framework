<!-- CA-R-2776@2 -->
<script lang="ts">
  import type { SavedItem } from './types';
  let { items, busy = false, onopen }: { items: SavedItem[]; busy?: boolean; onopen: (reference: string) => void } = $props();
</script>

<section class="saved-panel" aria-label="Saved Queries and Worksheets">
  <ul class="saved-list">
    {#if !items.length}<li class="notice">No saved queries or Worksheets.</li>{/if}
    {#each items as item}
      <li class="saved-item"><button type="button" disabled={busy} onclick={() => onopen(item.saved_query_id)}><span class="saved-kind">{item.kind}</span><span class="saved-preview">{item.name ?? item.preview}</span><small class="saved-meta">{item.saved_at}</small></button></li>
    {/each}
  </ul>
</section>
