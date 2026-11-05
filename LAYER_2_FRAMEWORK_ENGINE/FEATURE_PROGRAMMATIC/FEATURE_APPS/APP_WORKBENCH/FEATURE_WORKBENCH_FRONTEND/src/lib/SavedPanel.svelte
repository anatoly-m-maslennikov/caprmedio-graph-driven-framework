<!-- CA-R-2776@5 -->
<!-- CA-R-2902@1 -->
<!-- CA-D-681@1 -->
<script lang="ts">
  import type { QueryLogItem, SavedItem } from './types';
  let { items, logs = [], busy = false, onopen, onopenlog }: { items: SavedItem[]; logs?: QueryLogItem[]; busy?: boolean; onopen: (reference: string) => void; onopenlog?: (id: string) => void } = $props();
</script>

<section class="saved-panel" aria-label="Saved Queries and Views">
  <ul class="saved-list">
    {#if !items.length}<li class="notice">No saved queries or Views.</li>{/if}
    {#each items as item}
      <li class="saved-item"><button type="button" disabled={busy} onclick={() => onopen(item.saved_query_id)}><span class="saved-kind">{item.kind}</span><span class="saved-preview">{item.name ?? item.preview}</span><small class="saved-meta">{item.saved_at}</small></button></li>
    {/each}
  </ul>
  {#if logs.length}
    <h2>Recent runs</h2>
    <ul class="saved-list" aria-label="Recent query runs">
      {#each logs as item}
        <li class="saved-item"><button type="button" disabled={busy} onclick={() => onopenlog?.(item.log_id)}><span class="saved-kind">{item.outcome}</span><span class="saved-preview">{item.sql}</span><small class="saved-meta">{item.at} · {item.row_count ?? 'unknown'} rows, {item.column_count ?? 'unknown'} columns{item.error ? ` — ${item.error}` : ''}</small></button></li>
      {/each}
    </ul>
  {/if}
</section>
