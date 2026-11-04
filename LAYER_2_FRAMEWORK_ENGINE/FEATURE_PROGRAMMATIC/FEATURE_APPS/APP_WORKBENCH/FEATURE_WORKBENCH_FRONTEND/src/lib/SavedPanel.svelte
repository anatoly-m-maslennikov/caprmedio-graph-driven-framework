<!-- CA-R-2776@1 -->
<script lang="ts">
  import type { SavedItem } from './types';

  let { items, busy = false, onopen }: {
    items: SavedItem[]; busy?: boolean; onopen: (reference: string) => void;
  } = $props();
  let reference = $state('');

  function submit(event: SubmitEvent) {
    event.preventDefault();
    if (reference.trim()) onopen(reference.trim());
  }
</script>

<aside class="saved-panel" aria-label="Saved SQL">
  <form class="saved-form" onsubmit={submit}>
    <label for="saved-reference">Open saved</label>
    <input id="saved-reference" bind:value={reference} placeholder="Saved ID or URL" disabled={busy} />
    <button type="submit" disabled={busy || !reference.trim()}>Open</button>
  </form>
  <ul class="saved-list">
    {#each items as item}
      <li class="saved-item">
        <button type="button" disabled={busy} onclick={() => onopen(item.saved_query_id)}>
          <span class="saved-kind">{item.kind}</span><span class="saved-preview">{item.preview}</span>
          <small class="saved-meta">{item.saved_at}</small>
        </button>
      </li>
    {/each}
  </ul>
</aside>
