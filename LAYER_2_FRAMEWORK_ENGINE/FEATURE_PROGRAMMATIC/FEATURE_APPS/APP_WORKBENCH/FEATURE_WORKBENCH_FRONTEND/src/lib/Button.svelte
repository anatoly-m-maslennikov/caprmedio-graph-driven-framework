<!-- CA-R-2727@3 CA-M-466@3 CA-M-467@2 CA-D-674@6 -->
<script lang="ts">
  let { children, disabled = false, type = 'button', onclick }: {
    children: import('svelte').Snippet;
    disabled?: boolean;
    type?: 'button' | 'submit';
    onclick?: (event: MouseEvent) => void;
  } = $props();
</script>

<button {type} {disabled} {onclick}>{@render children()}</button>
