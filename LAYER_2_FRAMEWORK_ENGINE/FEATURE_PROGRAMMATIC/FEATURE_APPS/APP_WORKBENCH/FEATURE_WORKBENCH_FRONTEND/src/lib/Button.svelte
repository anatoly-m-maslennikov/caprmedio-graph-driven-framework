<script lang="ts">
  let { children, disabled = false, type = 'button', class: className = '', onclick }: {
    children: import('svelte').Snippet;
    disabled?: boolean;
    type?: 'button' | 'submit';
    class?: string;
    onclick?: (event: MouseEvent) => void;
  } = $props();
</script>

<button class={className} {type} {disabled} {onclick}>{@render children()}</button>
