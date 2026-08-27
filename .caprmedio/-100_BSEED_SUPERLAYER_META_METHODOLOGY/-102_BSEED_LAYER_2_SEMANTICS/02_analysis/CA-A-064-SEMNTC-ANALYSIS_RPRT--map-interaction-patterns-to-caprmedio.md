---
atom_id: CA-A-064
cce_version: cce_1
cce_form: rationale
subjects:
  declared:
    continuant:
      - relation-model
      - scope-topology
    occurrent:
      - interaction
version: 1
updated_at: 2026-08-26 19:52:34 +0400
relations:
  analysis_of:
    - CA-R-878
    - CA-R-881
    - CA-R-885
    - CA-R-926
    - CA-R-932
    - CA-R-933
    - CA-R-935
    - CA-R-945
    - CA-R-950
---
# Map interaction patterns to CAPRMEDIO

## Conclusion

CAPRMEDIO already has the topology and value-dependency primitives needed to represent Collaboration, X-as-a-Service, and Facilitating, but it does not yet govern these three concepts as explicit interaction modes. X-as-a-Service is already a strong composition of Consumer, Producer, `depends_on`, Demand, exact Implementation result, and result flow. Collaboration is only partially expressible through a shared Feature or common-scope relational arrangement plus explicit Demands. Facilitating is not ancestor authority and must not be represented as an ancestor-descendant Demand.

The three concepts should remain orthogonal to structural topology. Scope topology states where the parties are and whether they are ancestors, descendants, ordered peers, or unordered peers. A result relationship states what one Scope consumes from another through dependency, Demand, and result flow. An interaction mode states how the parties work together over a bounded period. Conflating these dimensions would incorrectly turn structural authority into assistance or temporary collaboration into permanent architectural dependency.

## Current CAPRMEDIO primitives

| Dimension | Current primitive | Meaning for interaction patterns |
|---|---|---|
| Structural topology | Scope Unit ancestry, peer order, and narrowest-common-scope ownership | Locates the participants and owns cross-branch relational Atoms without defining how the participants interact. |
| Value dependency | Consumer-to-Producer `depends_on` | Records that one Scope consumes a result from another; direction is from Consumer to Producer. |
| Requested result | Consumer-owned Demand directed to a Producer Claim Scope | Constrains exactly one Implementation result on which the Consumer has an exact declared dependency. |
| Result flow | Producer Claim Scope to Consumer Current Scope | Describes delivery direction without transferring authority over the rest of the Producer Scope. |
| Parent authority | Parent-owned Job for a direct child Scope | Defines the child's enduring result or responsibility; it is governance, not facilitation. |
| Interaction mode | No explicit current primitive | Collaboration, X-as-a-Service, and Facilitating are not yet governed as changeable ways of working between participants. |

## Collaboration

A shared Feature or common-scope relational arrangement can identify the joint outcome, while relational Demands can state each exact cross-scope dependency. Cross-branch relational Atoms already belong to the participants' narrowest enabled common Scope, which supplies a suitable ownership location for the shared arrangement.

This composition does not fully define Collaboration. A Demand is intentionally asymmetric: one Consumer requests one exact result from one Producer. Two reciprocal Demands remain two directional result contracts and do not by themselves mean that the parties jointly discover or solve one problem. Collaboration additionally implies temporarily shared work, high-bandwidth coordination, a common outcome, and an exit or transition condition.

The closest candidate composition is a common-scope Feature or Epic naming the participant Scopes, shared result, time boundary, and exit condition. Demands should be added only for exact directional dependencies that exist inside that collaboration, not as a substitute for the joint interaction mode.

## X-as-a-Service

X-as-a-Service is already represented strongly by the current model. The Consumer owns a Demand directed to the Producer, declares `depends_on` toward that Producer, and names one exact Implementation result. The result flows from Producer to Consumer, while the Demand cannot constrain Producer authority outside that result.

Ordered Layers are one valid topology for this pattern, but not its definition. Between ordered peer Scope Units, the Producer must be earlier and the Consumer later. A platform, capability, or service relationship may instead connect unordered peer Scope Units or separate descendant branches, provided the dependency and Demand remain valid. X-as-a-Service therefore composes with topology rather than requiring a Layer topology.

If later operational evidence requires a richer service contract, interface identity, availability expectation, service-level objective, discovery mechanism, or lifecycle policy can be added through their own independently replaceable authority. None is necessary merely to recognize the interaction pattern.

## Facilitating

Facilitating should not be identified with ancestor-level Scope. An ancestor may own authority that applies to descendants, and a direct parent defines a non-Project child's Job, but neither fact means that one Scope temporarily helps another acquire capability. Current authority also explicitly prohibits a Demand between ancestor and descendant Scopes in either direction.

The Facilitator and Beneficiary may occupy any otherwise valid topology. The defining result belongs to the Beneficiary: it acquires or strengthens its own capability. The Facilitator supplies bounded enabling work, while the Beneficiary retains authority over its Scope and resulting capability. Successful Facilitation ends in self-sufficiency or an explicit transition, not a permanent Consumer dependency on the Facilitator.

The closest candidate composition is a time-bounded Plan, Method, or Delivery naming the Facilitator, Beneficiary, target capability gap, intervention, evidence of capability acquisition, and exit condition. A future `facilitates` or `enables` relation may be justified, but only through separately accepted semantic and governance authority; it should not reuse `depends_on` when no enduring result dependency is intended.

## Recommended model boundary

CAPRMEDIO should preserve three independent axes:

| Axis | Question answered |
|---|---|
| Topology | Where are the participant Scopes, and what structural authority or order relates them? |
| Result relationship | Who consumes which exact result from which Producer? |
| Interaction mode | How are the participants working together now, and when does that arrangement end or change? |

Teams need not become a new Structural kind. Scope Units remain the governed interaction endpoints, while actual teams, Operators, or organizational owners remain realizations or external owners of those Scopes. An interaction-mode model should classify a relationship without changing Scope ownership, ancestor authority, dependency direction, or result ownership.

## Disposition

No new Requirement is accepted by this Analysis. X-as-a-Service needs no new dependency primitive. Collaboration needs an explicit joint and time-bounded interaction meaning if CAPRMEDIO must distinguish it from reciprocal service dependencies. Facilitating needs an explicit enabling meaning if CAPRMEDIO must distinguish capability transfer from ancestor authority and enduring dependency. The current prohibition on ancestor-descendant Demand remains coherent and should not be weakened to encode Facilitation.

## Reopening conditions

Reopen this Analysis if CAPRMEDIO adds an explicit interaction-mode Artifact or relation, permits Demand between ancestor and descendant Scopes, changes Demand from an exact result contract into a joint-work relation, or introduces governed team identities distinct from Scope Units and external owners.
