<!-- CA-D-674@23 -->
<script lang="ts">
  import { onMount, tick } from 'svelte';
  type Tab = { id: string; title: string; name?: string; dirty: boolean };
  type ContextMenu = { id: string; x: number; y: number };
  let { tabs, activeId, utility, ready = true, onselect, onclose, onadd, onrenamerequest, onduplicate }: {
    tabs: Tab[]; activeId: string; utility: 'settings' | 'saved' | 'view';
    ready?: boolean;
    onselect: (id: string) => void;
    onclose: (id: string) => void; onadd: () => void; onrenamerequest: (id: string) => void; onduplicate: (id: string) => void;
  } = $props();
  let menu = $state<ContextMenu | null>(null);
  let menuElement = $state<HTMLDivElement | undefined>(undefined);
  let firstMenuItem = $state<HTMLButtonElement | undefined>(undefined);

  function menuPosition(x: number, y: number) {
    const scale = Number(getComputedStyle(document.documentElement).getPropertyValue('--interface-scale')) || 1;
    return { x: x / scale, y: y / scale };
  }

  function openMenu(event: MouseEvent, id: string) {
    if (!ready) return;
    event.preventDefault();
    menu = { id, ...menuPosition(event.clientX, event.clientY) };
    void tick().then(() => firstMenuItem?.focus());
  }
  function openKeyboardMenu(event: KeyboardEvent, id: string) {
    if (!ready) return;
    if (event.key !== 'ContextMenu' && !(event.key === 'F10' && event.shiftKey)) return;
    event.preventDefault();
    const target = event.currentTarget as HTMLElement;
    const bounds = target.getBoundingClientRect();
    menu = { id, ...menuPosition(bounds.left, bounds.bottom) };
    void tick().then(() => firstMenuItem?.focus());
  }
  function choose(action: (id: string) => void) {
    const id = menu?.id;
    menu = null;
    if (id) action(id);
  }
  onMount(() => {
    const dismiss = (event: PointerEvent) => { if (menu && !menuElement?.contains(event.target as Node)) menu = null; };
    const escape = (event: KeyboardEvent) => { if (event.key === 'Escape' && menu) { event.preventDefault(); menu = null; } };
    document.addEventListener('pointerdown', dismiss);
    document.addEventListener('keydown', escape);
    return () => { document.removeEventListener('pointerdown', dismiss); document.removeEventListener('keydown', escape); };
  });
</script>

<div class="tab-strip" role="tablist" aria-label="Workbench views">
  {#each tabs as tab}
    <div class:active={utility === 'view' && tab.id === activeId} class="tab">
      <button type="button" role="tab" aria-haspopup="menu" disabled={!ready} aria-selected={utility === 'view' && tab.id === activeId} onclick={() => onselect(tab.id)} ondblclick={() => onrenamerequest(tab.id)} oncontextmenu={(event) => openMenu(event, tab.id)} onkeydown={(event) => openKeyboardMenu(event, tab.id)}>{tab.name || tab.title}{tab.dirty ? ' *' : ''}</button>
      <button class="tab-close" type="button" disabled={!ready} aria-label={`Close ${tab.name || tab.title}`} onclick={() => onclose(tab.id)}>×</button>
    </div>
  {/each}
  <button class="add-tab" type="button" aria-label="New View" disabled={!ready} onclick={() => onadd()}>+</button>
</div>
{#if menu}
  <div class="tab-context-menu" bind:this={menuElement} role="menu" aria-label="View actions" style={`left: ${menu.x}px; top: ${menu.y}px;`}>
    <button bind:this={firstMenuItem} type="button" role="menuitem" onclick={() => choose(onrenamerequest)}>Rename</button>
    <button type="button" role="menuitem" onclick={() => choose(onduplicate)}>Duplicate</button>
  </div>
{/if}
