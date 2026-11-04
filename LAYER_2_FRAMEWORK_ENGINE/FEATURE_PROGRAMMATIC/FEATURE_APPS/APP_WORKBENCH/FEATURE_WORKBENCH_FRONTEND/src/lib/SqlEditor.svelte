<!-- CA-R-2727@4 CA-M-466@4 CA-M-467@2 CA-D-674@7 -->
<script lang="ts">
  let { value = $bindable(''), disabled = false }: { value?: string; disabled?: boolean } = $props();
</script>

<label for="sql">SQL</label>
<textarea id="sql" bind:value {disabled} rows="12" spellcheck="false"></textarea>
