# CCE and text-writing check

This check concerns writing only: syntax, vocabulary, structure, formatting and content. Workflow/Step model changes, tools, validators, projections and formal-model design are out of scope. No Current Method or shared Method Draft was edited.

## What already fits

- M294 already requires simpler, familiar words when they keep the meaning.
- M442 now permits familiar names and short instructions as Summaries and keeps DRY/MECE unchanged.
- M444 already requires clear sentences and shared openings with lists.
- M445 keeps readable model names separate from technical key spelling.

## What needs attention

1. **M138:** “the strictest syntax needed” encourages the wrong choice. Prefer the simplest syntax that keeps the needed meaning.
2. **M311/M314:** fixed words such as “to” and “means” are required even when the meaning is already clear. These are wording rules, not a reason to change the role model.
3. **M123/M309:** Definitions of Done must use a fixed negative opening and parentheses. Review that writing requirement with its governing definition; do not silently change its logic.
4. **M236:** clear phrases such as “both A and B” are forcibly changed to symbolic grouping. Keep required formal syntax where needed; do not force it onto ordinary text.
5. **M113/M294:** the simple-language guidance is buried among repeated naming rules and examples. Keep naming rules in their own scope; keep the writing guide short. Words such as “anaphora” and “ellipsis” can be explained in plain English.
6. **M442/M443/M444:** parts of my recent rewrites are still too wordy. “one statement” in M443 can also suggest a one-sentence limit, which was not intended. A Summary must cover the full meaning; related statements may stay together.
7. **M229:** its special casing rule keeps ordinary sentence openings lowercase. The draft guide follows normal English unless a supplied format requires exact case. This needs an explicit match before treating the guide as an adopted CCE rule.
8. **Several citations:** M113/M125/M304 contain an old filename attached to the Current M444 ID. This is a reference cleanup, not a language-model redesign.

## Drafts

M113, M125 and M237 Drafts have the same Version as their Current sources. M111 and M301 Drafts refer to identities now replaced by M442 and M444. They cannot be promoted unchanged. A next Version number alone does not prove a Draft is ready.

The coordinated Term proposal intentionally changes some roles and naming rules. That is not treated here as a wording defect or permission to undo it. Shared Drafts remain unchanged.

## Two prompt drafts

- [Writing style guide](writing-style-guide.prompt.md)
- [Writing style eval](writing-style-eval.prompt.md)

The eval uses the guide as its checklist, so the rules are not maintained twice. These are prompt drafts, not promoted Method/Evaluation Atoms or new runtime behavior. The retained source snapshots and review details are in `.caprmedio_tmp/writing-methods-review-20261030/`. The broad first scan was narrowed after the Operator's scope clarification; its out-of-scope findings are not proposed changes here.
