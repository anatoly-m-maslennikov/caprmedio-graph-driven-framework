<!-- CA-R-2776@9 -->
<!-- CA-D-674@26 -->
<!-- CA-M-469@11 -->
<script lang="ts">
  import { tick } from 'svelte';
  let { open = false, busy = false, onopen, onclose }: { open?: boolean; busy?: boolean; onopen: (reference: string) => void; onclose: () => void } = $props();
  let dialog: HTMLDialogElement; let input: HTMLInputElement; let reference = $state('');
  $effect(() => { if (open && !dialog.open) { reference = ''; dialog.showModal(); tick().then(() => input.focus()); } if (!open && dialog.open) dialog.close(); });
  function submit(event: SubmitEvent) { event.preventDefault(); if (reference.trim()) onopen(reference.trim()); }
  function closed() { if (!dialog.open) onclose(); }
  function cancel(event: Event) { event.preventDefault(); onclose(); }
</script>
<dialog bind:this={dialog} onclose={closed} oncancel={cancel} aria-label="Open Bookmark or saved View"><form method="dialog" onsubmit={submit}><label>Saved ID or URL <input bind:this={input} bind:value={reference} disabled={busy} /></label><menu><button type="button" onclick={onclose}>Cancel</button><button type="submit" disabled={busy || !reference.trim()}>Open</button></menu></form></dialog>
