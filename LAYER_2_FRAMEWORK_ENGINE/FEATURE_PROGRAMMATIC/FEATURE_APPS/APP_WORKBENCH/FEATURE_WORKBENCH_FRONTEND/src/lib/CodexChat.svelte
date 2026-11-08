<script lang="ts">
  import { onMount } from 'svelte';
  import CodexInteraction from './CodexInteraction.svelte';
  import { applyNativeEvent, historyEntries, interaction, sseFrames } from './codex_protocol.js';
  import type { ChatEntry, NativeRequest } from './codex_protocol.js';
  type Command = { id: string; label: string; enabled: boolean; run: () => void };
  let { apiBase, projectRoot = null, oncommands }: { apiBase: string; projectRoot?: string | null; oncommands?: (commands: Command[]) => void } = $props();
  let bridge = $state(''); let ready = $state(false); let activeTurn = $state<string | null>(null); let message = $state('');
  let entries = $state<ChatEntry[]>([]); let pending = $state<NativeRequest[]>([]); let error = $state(''); let busy = $state(false);
  let composer: HTMLTextAreaElement;

  async function json(url: string, body?: unknown) {
    const response = await fetch(url, body === undefined ? {} : { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body) });
    const value = await response.json();
    if (!response.ok) throw new Error(value.error || 'Codex request failed');
    return value;
  }
  async function load() {
    try {
      const url = new URL(`${apiBase}/codex`, location.href);
      if (projectRoot) url.searchParams.set('project_root', projectRoot);
      const state = await json(url.href);
      if (!state.ready || !state.bridge_url) throw new Error('Codex is unavailable. Its host bridge is not running.');
      bridge = state.bridge_url;
      const conversation = await json(`${bridge}/conversation`);
      entries = historyEntries(conversation.thread);
      pending = (conversation.pending_requests || []).map(interaction).filter((request: NativeRequest | null) => request !== null);
      activeTurn = conversation.active_turn_id || null; busy = activeTurn !== null; ready = true;
    } catch (cause) { ready = false; error = cause instanceof Error ? cause.message : 'Codex is unavailable'; }
  }
  async function send() {
    if (!ready || !message.trim() || busy) return;
    const outgoing = message; message = ''; error = ''; busy = true;
    entries = [...entries, { id: crypto.randomUUID(), role: 'You', text: outgoing }];
    let finished = false;
    try {
      const response = await fetch(`${bridge}/turn`, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ message: outgoing }) });
      if (!response.ok) throw new Error((await response.json()).error || 'Codex turn failed');
      if (!response.body) throw new Error('Codex response has no event stream');
      const reader = response.body.getReader(); const decoder = new TextDecoder(); let buffer = '';
      try {
        while (true) {
          const next = await reader.read();
          buffer += decoder.decode(next.value, { stream: !next.done });
          const parsed = sseFrames(buffer); buffer = parsed.rest;
          for (const event of parsed.events) {
            if (event.type === 'started') activeTurn = event.turn_id;
            else if (event.type === 'event') {
              const request = interaction(event.event);
              if (request && !pending.some((item) => item.id === request.id)) pending = [...pending, request];
              entries = applyNativeEvent(entries, event.event);
            } else if (event.type === 'finished') {
              if (!['completed', 'failed', 'interrupted'].includes(event.status)) throw new Error('Invalid Codex completion status');
              finished = true; activeTurn = null; pending = [];
              if (event.status !== 'completed') error = event.error || `Response ${event.status}.`;
            }
          }
          if (next.done) break;
        }
      } finally { reader.releaseLock(); }
      if (!finished) throw new Error('Connection ended before Codex reported completion.');
    } catch (cause) { error = cause instanceof Error ? cause.message : 'Codex turn failed'; }
    finally { busy = false; }
  }
  async function interrupt() {
    if (activeTurn === null) return;
    try { await json(`${bridge}/interrupt`, { turn_id: activeTurn }); }
    catch (cause) { error = cause instanceof Error ? cause.message : 'Could not interrupt Codex'; }
  }
  async function respond(id: string | number, result: unknown) {
    await json(`${bridge}/respond`, { id, result });
    pending = pending.filter((request) => request.id !== id);
  }
  onMount(() => { void load(); });
  $effect(() => oncommands?.([
    { id: 'focus-chat', label: 'Focus Chat', enabled: true, run: () => composer?.focus() },
    { id: 'send-chat', label: 'Send Message', enabled: ready && !!message.trim() && !busy, run: () => void send() },
    { id: 'interrupt-chat', label: 'Interrupt Response', enabled: activeTurn !== null, run: () => void interrupt() },
  ]));
</script>

<aside class="codex-chat" aria-label="Codex Chat">
  <header><strong>Codex Chat</strong><span>{ready ? (busy ? 'Working' : 'Ready') : 'Unavailable'}</span></header>
  <div class="chat-history" aria-live="polite">
    {#if !entries.length}<p>{ready ? 'Ask Codex to use your connected tools.' : 'Connecting to Codex…'}</p>{/if}
    {#each entries as entry (entry.id)}<article class:activity={entry.role === 'Activity'}><b>{entry.role}</b><pre>{entry.text}</pre></article>{/each}
  </div>
  {#each pending as request (request.id)}<CodexInteraction {request} onrespond={(result) => respond(request.id, result)} />{/each}
  {#if error}<p class="error" role="alert">{error}</p>{/if}
  <form onsubmit={(event) => { event.preventDefault(); void send(); }}>
    <textarea bind:this={composer} aria-label="Message Codex" bind:value={message} disabled={!ready || busy} placeholder="Message Codex"></textarea>
    <button type="submit" disabled={!ready || !message.trim() || busy}>Send</button>
    {#if activeTurn}<button type="button" onclick={() => void interrupt()}>Interrupt</button>{/if}
  </form>
</aside>
