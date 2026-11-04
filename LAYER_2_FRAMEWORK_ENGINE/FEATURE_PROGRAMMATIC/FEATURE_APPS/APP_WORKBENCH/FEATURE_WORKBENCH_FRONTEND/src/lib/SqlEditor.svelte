<!-- CA-M-468@1 -->
<script lang="ts">
  import { autocompletion, type Completion, type CompletionContext } from '@codemirror/autocomplete';
  import { defaultKeymap, history, historyKeymap } from '@codemirror/commands';
  import { syntaxHighlighting } from '@codemirror/language';
  import { classHighlighter } from '@lezer/highlight';
  import { sql } from '@codemirror/lang-sql';
  import { Compartment, EditorState, Prec } from '@codemirror/state';
  import { EditorView, keymap } from '@codemirror/view';
  import { onMount } from 'svelte';
  import type { Schema } from './types';

  type Action = 'run' | 'check';
  let { value = $bindable(''), cursor = 0, disabled = false, schema = { tables: {} }, onchange, onaction }: {
    value?: string; cursor?: number; disabled?: boolean; schema?: Schema;
    onchange?: (value: string, cursor: number) => void;
    onaction?: (action: Action, cursor: number) => void;
  } = $props();
  let host: HTMLDivElement;
  let view: EditorView | undefined;
  const editable = new Compartment();
  const completion = new Compartment();

  const quoted = (name: string) => `"${name.replaceAll('"', '""')}"`;
  function options(currentSchema: Schema): Completion[] {
    return Object.entries(currentSchema.tables).flatMap(([table, columns]) => [
      { label: table, type: 'class' },
      ...columns.map((column) => ({ label: `${table}.${quoted(column.name)}`, apply: quoted(column.name), detail: column.type, type: 'property' })),
    ]);
  }
  function source(context: CompletionContext, currentSchema = schema) {
    const word = context.matchBefore(/[\w."]*/);
    if (!context.explicit && (!word || word.from === word.to)) return null;
    return { from: word?.from ?? context.pos, options: options(currentSchema) };
  }
  const position = () => view?.state.selection.main.head ?? cursor;
  function shortcut(event: KeyboardEvent) {
    if (disabled || event.repeat || !event.metaKey || event.ctrlKey || event.altKey || event.key !== 'Enter') return false;
    event.preventDefault();
    onaction?.(event.shiftKey ? 'check' : 'run', position());
    return true;
  }

  onMount(() => {
    view = new EditorView({
      parent: host,
      state: EditorState.create({
        doc: value, selection: { anchor: Math.min(cursor, value.length) },
        extensions: [
          sql(), syntaxHighlighting(classHighlighter), history(), keymap.of([...defaultKeymap, ...historyKeymap]),
          editable.of(EditorView.editable.of(!disabled)),
          completion.of(autocompletion({ override: [source] })),
          EditorView.contentAttributes.of({ 'aria-label': 'SQL editor' }),
          Prec.highest(EditorView.domEventHandlers({ keydown: shortcut })),
          EditorView.updateListener.of((update) => {
            if (update.docChanged || update.selectionSet) onchange?.(update.state.doc.toString(), update.state.selection.main.head);
          }),
        ],
      }),
    });
    return () => view?.destroy();
  });

  $effect(() => {
    if (!view) return;
    const current = view.state.doc.toString();
    const nextCursor = Math.min(cursor, value.length);
    if (current !== value) view.dispatch({ changes: { from: 0, to: current.length, insert: value }, selection: { anchor: nextCursor } });
    else if (view.state.selection.main.head !== nextCursor) view.dispatch({ selection: { anchor: nextCursor } });
  });
  $effect(() => {
    const currentSchema = schema;
    if (!view) return;
    view.dispatch({ effects: [
      editable.reconfigure(EditorView.editable.of(!disabled)),
      completion.reconfigure(autocompletion({ override: [(context) => source(context, currentSchema)] })),
    ] });
  });
</script>

<span>SQL</span>
<div id="sql-editor" class="sql-editor" bind:this={host}></div>
