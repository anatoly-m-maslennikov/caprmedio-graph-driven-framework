<!-- CA-D-674@11 -->
<script lang="ts">
  import { tick } from 'svelte';
  import { filterCommands, moveSelection } from './palette_helpers.js';
  export type Command = { id: string; label: string; shortcut?: string; enabled: boolean; run: () => void };
  let { open = false, commands, onclose }: { open?: boolean; commands: Command[]; onclose: () => void } = $props();
  let dialog: HTMLDialogElement; let input: HTMLInputElement; let query = $state(''); let selected = $state(0);
  let matches = $derived(filterCommands(commands, query));
  $effect(() => { if (open && !dialog.open) { query = ''; selected = 0; dialog.showModal(); tick().then(() => input.focus()); } if (!open && dialog.open) dialog.close(); });
  function choose(command = matches[selected]) { if (command?.enabled) { command.run(); onclose(); } }
  function keydown(event: KeyboardEvent) {
    if (event.key === 'Escape') { event.preventDefault(); onclose(); }
    else if (event.key === 'ArrowDown' || (event.ctrlKey && event.key.toLowerCase() === 'n')) { event.preventDefault(); selected = moveSelection(selected, matches.length, 1); }
    else if (event.key === 'ArrowUp' || (event.ctrlKey && event.key.toLowerCase() === 'p')) { event.preventDefault(); selected = moveSelection(selected, matches.length, -1); }
    else if (event.key === 'Enter') { event.preventDefault(); choose(); }
  }
</script>
<dialog bind:this={dialog} onclose={onclose} onkeydown={keydown} aria-label="Command palette"><input bind:this={input} bind:value={query} oninput={() => selected = 0} aria-label="Search commands" placeholder="Search commands" /><ul>{#each matches as command, index}<li><button class:active={index === selected} type="button" disabled={!command.enabled} onclick={() => choose(command)}>{command.label}{#if command.shortcut}<small>{command.shortcut}</small>{/if}</button></li>{/each}</ul></dialog>
