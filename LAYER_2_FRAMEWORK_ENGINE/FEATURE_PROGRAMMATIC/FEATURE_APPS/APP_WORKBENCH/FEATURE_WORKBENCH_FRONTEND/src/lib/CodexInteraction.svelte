<!-- CA-R-2791@1 -->
<!-- CA-D-680@1 -->
<script lang="ts">
  import { inputAnswers, record } from './codex_protocol.js';
  import type { NativeRequest } from './codex_protocol.js';
  let { request, onrespond }: { request: NativeRequest; onrespond: (value: unknown) => Promise<void> } = $props();
  let answers = $state<Record<string, string>>({}); let content = $state('{}'); let error = $state(''); let sending = $state(false);
  const params = $derived(request.params);
  const input = $derived(request.method === 'item/tool/requestUserInput');
  const elicitation = $derived(request.method === 'mcpServer/elicitation/request');
  const permissions = $derived(request.method === 'item/permissions/requestApproval');
  const approval = $derived(['item/commandExecution/requestApproval', 'item/fileChange/requestApproval'].includes(request.method));
  const questions = $derived(Array.isArray(params.questions) ? params.questions : []);
  const url = $derived(elicitation && params.mode === 'url' && typeof params.url === 'string' && /^https?:\/\//.test(params.url) ? params.url : null);
  async function submit(accept: boolean) {
    error = ''; sending = true;
    try {
      let result: unknown;
      if (input) {
        if (questions.some((question) => !answers[question.id]?.trim())) throw new Error('Answer each question before submitting.');
        result = inputAnswers(questions, answers);
      } else if (elicitation) {
        const values = accept && !url ? JSON.parse(content) : undefined;
        if (accept && !url && !record(values)) throw new Error('Enter a JSON object for the requested fields.');
        result = accept ? { action: 'accept', ...(url ? {} : { content: values }) } : { action: 'decline' };
      } else if (permissions) result = { permissions: accept ? params.permissions : {}, scope: 'turn' };
      else if (approval) result = { decision: accept ? 'accept' : 'decline' };
      else result = JSON.parse(content);
      await onrespond(result);
    } catch (cause) { error = cause instanceof Error ? cause.message : 'Could not send the response'; }
    finally { sending = false; }
  }
</script>

<section class="chat-request" aria-label="Codex interaction">
  <p>{params.message || params.reason || params.prompt || 'Codex needs your response.'}</p>
  {#if input}
    {#each questions as question}
      <label>{question.question}
        {#if question.options?.length && !question.isOther}
          <select bind:value={answers[question.id]} required disabled={sending}>
            <option value="">Select an answer</option>
            {#each question.options as option}<option value={option.label}>{option.label} — {option.description || ''}</option>{/each}
          </select>
        {:else}<input type={question.isSecret ? 'password' : 'text'} bind:value={answers[question.id]} disabled={sending} required />{/if}
      </label>
    {/each}
  {:else if elicitation && url}
    <a href={url} target="_blank" rel="noopener noreferrer">Open requested page</a>
  {:else if elicitation}
    <details><summary>Requested fields</summary><pre>{JSON.stringify(params.requestedSchema, null, 2)}</pre></details>
    <label>Response JSON<textarea bind:value={content} disabled={sending} spellcheck="false"></textarea></label>
  {:else if permissions || approval}
    <pre>{typeof params.command === 'string' ? params.command : JSON.stringify(params.permissions || params.changes || params, null, 2)}</pre>
  {:else}
    <details><summary>Request details</summary><pre>{JSON.stringify(request, null, 2)}</pre></details>
    <label>Response JSON<textarea bind:value={content} disabled={sending} spellcheck="false"></textarea></label>
  {/if}
  {#if error}<p class="error" role="alert">{error}</p>{/if}
  <button type="button" disabled={sending} onclick={() => void submit(true)}>{input ? 'Submit answers' : approval || permissions ? 'Approve' : 'Send response'}</button>
  {#if !input && (approval || permissions || elicitation)}<button type="button" disabled={sending} onclick={() => void submit(false)}>Decline</button>{/if}
</section>
