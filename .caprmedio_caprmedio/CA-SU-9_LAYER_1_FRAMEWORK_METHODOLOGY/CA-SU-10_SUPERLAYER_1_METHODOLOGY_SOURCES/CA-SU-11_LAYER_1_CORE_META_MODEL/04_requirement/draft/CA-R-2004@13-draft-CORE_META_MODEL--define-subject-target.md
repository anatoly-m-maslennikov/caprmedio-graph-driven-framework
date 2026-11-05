---
topics:
  main_subject: Entity/Object/Continuant/Governing Objects/Atom.Subjects
  dependencies:
  - Entity
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Governing Objects/Atom.Content Role
  - 'Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Requirement)'
atom_id: CA-R-2004@13-draft
ref_id: CA-R-2004@13-draft
role: Requirement
form: Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
version: 13
updated_at: 2026-10-30 08:49:46 +0400
author: Anatoly Maslennikov
tier: 1
container:
  scope_unit: CA-SU-11
---
## Summary

Define Subject Target

## Claim scope

a direct GOVERNS or DEPENDS_ON target in an Atom's Subjects.

## Claim


A direct GOVERNS or DEPENDS_ON target in Atom.Subjects must be the topic addressed by a canonical Entity-rooted Subject expression and may identify a kind, axis, property, allowed value, or named instance.

## Details

Subject says what an Atom concerns. Content Role says what its content does. They are independent by definition. An Atom of any RMED Role can govern a topic in any declared Subject branch. A topic about how work is performed does not require a separate Method root.

Entity is the canonical expression root. Its branch structure follows the governing Entity Definition in CA-R-1248. A source path retains the declared operators and full qualification; a short display label is not another identity or alias.

The Subject does not repeat or assign the Atom's Local Scope Unit, folder or Carrier. Topic meanings come from source use and Semantics; the Terms Graph derives definitions from those cases rather than creating another authority layer.

Within the shared Atom branch, `Entity/Object/Continuant/Governing Objects/Atom.Content Role` names the Atom's Content Role Property, which is used for classification. `Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Requirement)` names a narrower Atom kind qualified by that Property and its independently admitted value; that kind inherits Atom's applicable features and constraints. The Property remains a directly addressable Subject, without becoming an intermediate narrower kind of Atom or a separate Classification kind. Naming the Property or qualified kind does not assign a role value to an Atom instance.

### Current source pin and pending adoption

Proposed N+1 successor of `/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2004-CORE_META_MODEL--define-subject-target.md`, Atom `CA-R-2004`, version `12`, SHA-256 `f6b8c72feadc58414683ef3a996f60da2298760f226a43d9a2f536955db7c2fa`. This source alignment follows the accepted CA-R-1531@21, CA-R-1248@24, CA-R-1284@24 and CA-R-2150@15 Draft successors; those sources remain pending publication. The existing Current source is unchanged. This temporary preparation performs no publication, native operation, generated-view rebuild or runtime change.
