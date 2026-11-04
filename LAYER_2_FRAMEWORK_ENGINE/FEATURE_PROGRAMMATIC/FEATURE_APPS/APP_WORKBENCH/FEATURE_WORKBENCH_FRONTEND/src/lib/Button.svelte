<!-- CA-R-2727@4 CA-M-466@5 CA-M-467@2 CA-D-674@8 -->
<script lang="ts">
  let { children, disabled = false, type = 'button', onclick }: {
    children: import('svelte').Snippet;
    disabled?: boolean;
    type?: 'button' | 'submit';
    onclick?: (event: MouseEvent) => void;
  } = $props();
</script>

<button {type} {disabled} {onclick}>{@render children()}</button>
