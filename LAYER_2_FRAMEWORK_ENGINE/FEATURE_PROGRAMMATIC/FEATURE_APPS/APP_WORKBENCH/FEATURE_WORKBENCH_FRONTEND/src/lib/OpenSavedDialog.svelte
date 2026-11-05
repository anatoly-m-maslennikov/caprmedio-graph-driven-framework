<!-- CA-R-2776@5 -->
<script lang="ts">
  import { tick } from 'svelte';
  let { open = false, busy = false, onopen, onclose }: { open?: boolean; busy?: boolean; onopen: (reference: string) => void; onclose: () => void } = $props();
  let dialog: HTMLDialogElement; let input: HTMLInputElement; let reference = $state('');
  $effect(() => { if (open && !dialog.open) { reference = ''; dialog.showModal(); tick().then(() => input.focus()); } if (!open && dialog.open) dialog.close(); });
  function submit(event: SubmitEvent) { event.preventDefault(); if (reference.trim()) onopen(reference.trim()); }
</script>
<dialog bind:this={dialog} onclose={onclose} aria-label="Open saved query or View"><form method="dialog" onsubmit={submit}><label>Saved ID or URL <input bind:this={input} bind:value={reference} disabled={busy} /></label><menu><button type="button" onclick={onclose}>Cancel</button><button type="submit" disabled={busy || !reference.trim()}>Open</button></menu></form></dialog>
