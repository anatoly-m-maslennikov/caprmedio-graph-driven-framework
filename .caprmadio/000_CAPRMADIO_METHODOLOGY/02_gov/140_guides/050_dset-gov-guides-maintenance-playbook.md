---
artifact_type: procedure
artifact_subtype: playbook
scope_path: layer:gov
priority: medium
---

# Maintain governed artifacts

## Trigger

Use this procedure when a durable governed artifact, maintained surface, or
stable hub navigation needs to change.

## Procedure

1. **Check authorization.** If the request is exploration, comparison, or an
   unaccepted idea, remain in Exploration Mode: write no artifact and make no
   governance commit. Continue only after explicit operator acceptance of a
   durable conclusion.
2. **Resolve local authority.** Read the current project-local governance and
   settings carriers. Select one registered and enabled Type (and direct
   subtype only when applicable), then resolve its route. Stop on an unknown
   or materially ambiguous Type, subtype, route, authority, scope, or relation;
   do not infer a route from a filename, folder, tool, or workflow.
3. **Choose the Revision mode.** Use exactly one of `atomic`, `append_only`,
   or `maintained`; Type separately determines the artifact's meaning and
   governance location.
4. **Apply the mode.**
   - For `atomic`, emit one independently reviewable claim. Use the type-local
     `drafts/`, active, and `archive/` locations only when the project has
     implemented that layout. Otherwise stop: the layout migration remains
     open under `CAPRMADIO-PROBLEM-GOV-011`.
     Do not add a status field. Archive only by byte-preserving move and the
     applicable archive commit trailers.
   - For `append_only`, append complete records in order; never rewrite an
     accepted record.
   - For `maintained`, revise the carrier through Git and its registered
     procedure.
5. **Maintain navigation narrowly.** Hubs list stable folders and maintained
   surfaces, never individual atoms or runtime state. Update only the
   navigation that has a stable reader route.
6. **Validate and deliver.** Run the validation and delivery gates configured
   by the project. Commit locally with provenance-bearing trailers as
   applicable: `Implements:` for implemented authority, `Resolves:` for a
   resolved Problem, and `Session:` for the working session. Delivery follows
   project configuration; a pull request is not inherently required.

## Checks

- The selected Type is registered and enabled by the current project settings.
- The Revision mode permits the intended write.
- Atomic archiving preserves bytes and uses the applicable archive trailers.
- Links are GitHub-readable and contain no private machine paths.
- A hub exposes only stable navigation; no atom or runtime inventory was added.
- Project-configured validation and delivery gates pass before claiming the
  change complete.

## Stop conditions

Stop and return to exploration or record the appropriate unresolved work when
operator acceptance, governing authority, enabled classification, route,
scope, relation, or configured validation is missing or ambiguous. Do not
create a placeholder carrier, silently choose a route, rewrite an append-only
record, or claim that the type-local atomic layout already exists.
