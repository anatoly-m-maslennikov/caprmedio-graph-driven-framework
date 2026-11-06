<!-- CA-R-2727@17 -->
<!-- CA-D-674@22 -->
<script lang="ts">
  import { tick } from 'svelte';
  let { open = false, title, initialValue = '', onsubmit, onclose }: { open?: boolean; title: string; initialValue?: string; onsubmit: (name: string) => void; onclose: () => void } = $props();
  let dialog: HTMLDialogElement; let input: HTMLInputElement; let name = $state('');
  $effect(() => { if (open && !dialog.open) { name = initialValue; dialog.showModal(); tick().then(() => input.focus()); } if (!open && dialog.open) dialog.close(); });
  function submit(event: SubmitEvent) { event.preventDefault(); onsubmit(name.trim()); }
  function closed() { if (!dialog.open) onclose(); }
  function cancel(event: Event) { event.preventDefault(); onclose(); }
</script>
<dialog bind:this={dialog} onclose={closed} oncancel={cancel} aria-label={title}><form method="dialog" onsubmit={submit}><label>{title} <input bind:this={input} bind:value={name} placeholder="Optional name" /></label><menu><button type="button" onclick={onclose}>Cancel</button><button type="submit">Save</button></menu></form></dialog>
