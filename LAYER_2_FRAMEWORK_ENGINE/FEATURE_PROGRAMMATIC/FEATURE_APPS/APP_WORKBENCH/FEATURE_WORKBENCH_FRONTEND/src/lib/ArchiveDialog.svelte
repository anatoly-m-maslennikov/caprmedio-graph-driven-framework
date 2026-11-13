<!-- CA-D-718@1 -->
<script lang="ts">
  import { tick } from 'svelte';
  import Button from './Button.svelte';
  import type { ArchiveScope } from './types';

  let { open, loaded, onload, onclose }: {
    open: boolean;
    loaded: ArchiveScope[];
    onload: (scopes: ArchiveScope[]) => Promise<void>;
    onclose: () => void;
  } = $props();

  const emptyScope = (): ArchiveScope => ({ scope_unit: '', role: '' });
  let dialog: HTMLDialogElement;
  let scopes = $state([emptyScope()]);
  let busy = $state(false);
  let error = $state('');
  const valid = $derived(scopes.every((scope) => scope.scope_unit.trim() && scope.role.trim()));

  $effect(() => {
    if (open && !dialog.open) {
      scopes = [emptyScope()];
      error = '';
      dialog.showModal();
      void tick().then(() => dialog.querySelector('input')?.focus());
    }
    if (!open && dialog.open) dialog.close();
  });

  async function load(event: SubmitEvent) {
    event.preventDefault();
    if (busy || !valid) return;
    const requested = scopes.map(({ scope_unit, role }) => ({ scope_unit: scope_unit.trim(), role: role.trim() }));
    busy = true;
    error = '';
    try {
      await onload(requested);
      scopes = [emptyScope()];
    } catch (failure) {
      error = failure instanceof Error ? failure.message : 'Archive load failed.';
    } finally {
      busy = false;
    }
  }

  function cancel(event: Event) {
    event.preventDefault();
    if (!busy) onclose();
  }
</script>

<dialog bind:this={dialog} oncancel={cancel} aria-label="Load Archives">
  <form onsubmit={load}>
    <div class="archive-scopes">
      {#each scopes as scope, index (scope)}
        <div class="archive-scope">
          <label>
            Scope Unit
            <input bind:value={scope.scope_unit} placeholder="Name or ID" aria-label={`Scope Unit ${index + 1}`} disabled={busy} />
          </label>
          <label>
            Role
            <input bind:value={scope.role} placeholder="Requirement" aria-label={`Role ${index + 1}`} disabled={busy} />
          </label>
          {#if scopes.length > 1}
            <Button disabled={busy} onclick={() => scopes.splice(index, 1)}>Remove</Button>
          {/if}
        </div>
      {/each}
    </div>
    <div>
      <Button disabled={busy} onclick={() => scopes.push(emptyScope())}>Add scope</Button>
    </div>
    <section aria-label="Loaded Archive scopes" aria-live="polite">
      <strong>Loaded Archive scopes</strong>
      {#if loaded.length}
        <ul>{#each loaded as scope}<li>{scope.scope_unit} / {scope.role}</li>{/each}</ul>
      {:else}
        <p>None loaded.</p>
      {/if}
    </section>
    {#if error}<p class="error" role="alert">{error}</p>{/if}
    <menu>
      <Button disabled={busy} onclick={onclose}>Close</Button>
      <Button type="submit" disabled={busy || !valid}>{busy ? 'Loading…' : 'Load'}</Button>
    </menu>
  </form>
</dialog>

<style>
  .archive-scopes { display: grid; gap: 8px; max-height: 40vh; overflow: auto; }
  .archive-scope { display: flex; align-items: end; flex-wrap: wrap; gap: 6px; padding: 2px; }
  .archive-scope label { flex: 1 1 110px; }
  section p { margin: 2px 0 0; }
  section ul { display: block; min-width: 0; max-height: 25vh; }
</style>
