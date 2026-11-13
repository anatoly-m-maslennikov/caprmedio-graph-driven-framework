<!-- CA-D-674@26 -->
<script lang="ts">
  import type { SourceSyncStatus } from './types';
  let { status }: { status: SourceSyncStatus } = $props();
  const text = () => status.syncing ? 'Source index: Syncing' : status.last_synced_at ? `Source index: ${new Date(status.last_synced_at).toLocaleString()}` : 'Source index: Not synced yet';
</script>

<span class="sync-status" role="status" aria-label="Source indexing status">{text()}</span>
