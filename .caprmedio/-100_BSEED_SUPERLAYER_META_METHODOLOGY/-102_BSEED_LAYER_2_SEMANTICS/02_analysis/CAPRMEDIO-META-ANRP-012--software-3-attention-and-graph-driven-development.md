---
cce_version: cce_1
cce_form: rationale
subjects:
  declared:
    continuant:
      - methodology
subject_scope: semantics
version: 4
updated_at: 2026-08-23 15:00:38
---
# Software 3.0, attention, and graph-driven development

## Source

- [YouTube talk by Andrej Karpathy](https://www.youtube.com/watch?v=XdbpCM4yGyE)
- User-supplied transcript of the linked video, reviewed on 2026-08-16

## Question

What does the talk actually say about prompting and graphs, and which parts support CAPRMEDIO's graph-driven development model?

## Software progression

Karpathy describes three programming paradigms:

1. **Software 1.0** designs explicit algorithms and source code.
2. **Software 2.0** designs datasets and training processes whose result is a neural network.
3. **Software 3.0** designs prompts that configure a general-purpose GPT to execute natural-language programs.

The talk does not argue that prompting is disappearing. It says that “these prompts really matter” and describes Software 3.0 as designing the prompt. Prompts are programs expressed in natural language, while ordinary code MAY still surround the model and provide tools, interfaces, constraints, and deterministic behavior.

## Quote status

The formulation “Prompting is going away. Delete everything, keep Graph.” does not occur in the supplied transcript.

The closest deletion phrase is:

> “Delete everything, keep attention.”

It refers to the Transformer architecture removing recurrent-neural-network machinery while retaining attention. The closest explicit graph phrase describes attention as “data dependent message passing on directed graphs.” These are connected technical ideas, but neither is a claim that persistent project graphs replace prompting.

CAPRMEDIO's statement “Prompts execute the work. The graph preserves what the work means.” is therefore a framework synthesis, not a quotation or close paraphrase of the video.

## The graph in the talk

Karpathy explains attention as the communication phase of a Transformer:

- tokens or other elements are nodes holding vectors;
- queries and keys compute data-dependent affinity between nodes;
- normalized affinities determine how values flow across directed edges;
- the received values update each node;
- multi-layer perceptrons perform per-node computation between communication phases; and
- causal masking restricts which nodes MAY communicate so future information cannot leak backward.

This is a transient computational graph constructed inside a model execution. CAPRMEDIO's graph is different: it is a persistent semantic and governance graph whose nodes and typed relations survive across executions. The useful connection is structural rather than identical.

## External memory

The talk also discusses finite context and an externally saved notebook or scratchpad that a model can learn to consult. This anticipates a durable memory layer outside the model activation state. The notebook is not yet a governed knowledge system, but it reinforces the need to separate temporary execution context from persistent external state.

## CAPRMEDIO mapping

| Talk mechanism | CAPRMEDIO equivalent |
|---|---|
| Natural-language program in a prompt | Versioned prompt or agent program in Implementation |
| General-purpose GPT execution | Temporary executor over governed task context |
| Attention-selected communication | Relation-aware selection of task-relevant graph context |
| Causal mask | Lifecycle- and authority-aware visibility rules |
| External notebook or scratchpad | Working-memory Journal or temporary execution state |
| Dataset and data-engine iteration | Evaluation and Ops feedback driving governed improvement |
| Ordinary surrounding code | Deterministic native Implementation and control shell |

The semantic graph should determine which accepted claims, evidence, instructions, and Implementation bindings enter an execution. The model then performs temporary work over that bounded context. Its results return as Ops evidence, Analysis, generated Projections, or proposed graph changes rather than silently rewriting authority.

## Ideas worth adopting

1. Treat prompts as versioned executable artifacts with model, configuration, source-frontier, Requirement, Method, and Evaluation bindings.
2. Build a context compiler that traverses typed relations and produces a bounded task-specific Projection for each agent execution.
3. Apply lifecycle and authority filters so drafts, superseded revisions, and generated views cannot masquerade as current authority.
4. Separate working memory from admitted project knowledge and define an explicit promotion path through Analysis and Plan.
5. Keep deterministic code around LLM execution for validation, permissions, data movement, stop conditions, and reproducible operations.
6. Use Ops evidence and Evaluation evaluations as the data engine that demonstrates whether graph changes improve outcomes.

## What the talk does not establish

- It does not propose a persistent semantic knowledge graph.
- It does not define typed relations, authority, provenance, lifecycle, or admission gates.
- It does not mention the LLM Wiki pattern in the supplied transcript.
- It does not claim that graphs improve automatically or that prompts are obsolete.
- It does not replace native code, tests, evaluation, or deterministic control with prompting.

## CAPRMEDIO gaps exposed

CAPRMEDIO defines a persistent semantic graph but does not yet implement the execution bridge suggested by the talk. Missing pieces include a context compiler, prompt and model provenance, lifecycle-aware traversal, working-memory Journals, deterministic agent-control adapters, and measured Ops-to-Evaluation feedback proving that a graph revision changes real outcomes.

## Conclusion

The video supports two narrower claims: prompts are a real programming surface, and attention can be understood as data-dependent message passing over directed graphs. CAPRMEDIO combines these with a separate persistent-governance thesis: prompts and models are replaceable executors, while the governed graph carries durable meaning, authority, lineage, and evidence across executions.
