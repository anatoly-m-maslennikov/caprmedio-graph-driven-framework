"""Emit the bounded CA-P-1919 design; never write sources or outputs."""
import hashlib
import json
from pathlib import Path


BASELINE = Path('.caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json')
EXPECTED_INVENTORY = '23394abaf6e9c18a585cf3146aedd0a80df166c9dd82be6e86ed7c3c56780bdc'
EXPECTED_FILE = 'bc5d99e91fb7dd4dcb42e59ff33cc24cff1d0901c5904764394c769aaa0a9430'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def main():
    baseline_bytes = BASELINE.read_bytes()
    baseline = json.loads(baseline_bytes)
    assert sha(baseline_bytes) == EXPECTED_FILE
    assert baseline['inventory_sha256'] == EXPECTED_INVENTORY
    assert sha(canonical({k: v for k, v in baseline.items() if k != 'inventory_sha256'})) == EXPECTED_INVENTORY
    sources = {row['atom_id']: row for row in baseline['source_atoms']}
    source_bytes = {}
    for row in baseline['source_atoms'] + baseline['excluded_sources']:
        raw = Path(row['carrier_path']).read_bytes()
        assert sha(raw) == row['carrier_sha256'], row['atom_id']
        source_bytes[row['atom_id']] = raw
    nodes = {row['identity']: row for row in baseline['nodes']}
    evidence = {}

    def ev(atom_id, start, end, token):
        row = sources[atom_id]
        lines = source_bytes[atom_id].decode().splitlines()
        quote = '\n'.join(lines[start - 1:end])
        assert token in quote, (atom_id, start, end)
        assert any(line.startswith('## Claim') or line.startswith('## Scope') or line.startswith('### Inputs') for line in lines[:start])
        key = f'{atom_id}:{start}-{end}'
        evidence[key] = {
            'atom_id': atom_id, 'atom_revision': row['atom_revision'],
            'carrier_path': row['carrier_path'], 'carrier_sha256': row['carrier_sha256'],
            'start_line': start, 'end_line': end, 'quote': quote,
            'text_sha256': sha(quote.encode()),
        }
        return key

    E = {
        'entity': ev('CA-R-1248', 28, 28, 'an Entity **means**'),
        'primary': ev('CA-R-1191', 28, 28, 'does **not** require'),
        'dependent': ev('CA-R-1192', 28, 28, 'immediate bearer'),
        'property': ev('CA-R-1193', 28, 28, 'Dependent Entity'),
        'primary_entity': ev('CA-R-1266', 28, 28, 'NARROWER_THAN Entity'),
        'dependent_entity': ev('CA-R-1267', 28, 28, 'NARROWER_THAN Entity'),
        'artifact_primary': ev('CA-R-1249', 28, 28, 'NARROWER_THAN Primary Entity'),
        'actor_primary': ev('CA-R-1250', 28, 28, 'NARROWER_THAN Primary Entity'),
        'artifact': ev('CA-R-1268', 29, 29, 'persists across'),
        'atom': ev('CA-R-655', 26, 26, 'independently governed Artifact'),
        'action': ev('CA-R-1452', 37, 37, 'reusable operational building block'),
        'workflow': ev('CA-R-1508', 35, 43, 'Workflow Run'),
        'step': ev('CA-R-1509', 34, 41, 'Step Run'),
        'workflow_run': ev('CA-R-1510', 30, 35, 'actual execution'),
        'step_run': ev('CA-R-1511', 32, 36, 'actual execution'),
        'action_run': ev('CA-O-128', 48, 48, 'distinct Action Run identity'),
        'operator': ev('CA-R-1422', 32, 32, 'collective Actor'),
        'plan_atom': ev('CA-R-1574', 32, 32, 'a Plan Atom **means** an Atom'),
        'requirement_role': ev('CA-R-1339', 30, 36, 'Entity model'),
        'analysis_role': ev('CA-R-1337', 29, 29, 'without** normative authority'),
        'analysis_types': ev('CA-R-1232', 29, 29, 'Analysis Report, Rationale'),
        'projection': ev('CA-R-1746', 32, 38, 'non-authoritative generated view'),
        'methodology': ev('CA-R-1213', 36, 38, 'Projection'),
        'scope_unit': ev('CA-R-1757', 29, 29, 'ownership boundary'),
        'carrier_primary': ev('CA-D-414', 28, 28, 'Primary Entity'),
        'file_carrier': ev('CA-D-258', 28, 28, 'Carrier'),
        'directory_carrier': ev('CA-D-259', 28, 28, 'Carrier'),
        'carrier_binding': ev('CA-D-505', 34, 40, 'remains'),
        'non_ephemeral_carrier': ev('CA-D-506', 30, 34, 'non-ephemeral'),
        'carrier_identity': ev('CA-D-507', 30, 30, 'Entity identity'),
        'atom_bundle': ev('CA-D-463', 32, 34, 'Carrier Bundle'),
        'default_vs_inherited': ev('CA-D-485', 32, 36, 'inherited'),
        'analysis_status': ev('CA-R-1875', 28, 36, 'more-specific Status domain'),
        'plan_status': ev('CA-R-1539', 29, 29, 'Active, Backlog, Done, Canceled, Archived'),
        'narrower': ev('CA-R-1435', 28, 38, 'same referent'),
    }

    def member(identity, refs, meaning, confidence=96):
        assert identity in nodes, identity
        return {'qualified_identity': identity, 'disposition': 'proposed',
                'confidence_percent': confidence, 'evidence_refs': refs,
                'display_reason': meaning, 'native_temporal_classification': 'not_performed'}

    continuants = [
        member('Artifact', [E['artifact']], 'The governing identity persists across Artifact Revisions; this is the strongest local continuant display anchor.', 99),
        member('Atom', [E['atom'], E['artifact']], 'A governed information Artifact, not the act of authoring or executing it.'),
        member('Action', [E['action'], E['atom'], E['artifact']], 'Reusable Action definition; not its invocation, Actor, Tool, Task, Journal Record or Carrier.'),
        member('Workflow', [E['workflow'], E['atom'], E['artifact']], 'Reusable graph definition; distinct from actual Workflow Runs.'),
        member('Step', [E['step'], E['atom'], E['artifact']], 'Reusable Step definition; distinct from Step Runs and its referenced Action.'),
        member('Atom/Content Role: Plan/Type: Plan', [E['plan_atom'], E['atom'], E['artifact']], 'The Plan information Artifact stores intended work; it is not an occurrence of that work.'),
        member('Atom/Content Role: Requirement', [E['requirement_role'], E['atom'], E['artifact']], 'A Requirement-role Atom carries a model or required-result Claim; not the modeled Entity or achieved result.'),
        member('Atom/Content Role: Analysis/Type: Analysis Report', [E['analysis_role'], E['analysis_types'], E['atom'], E['artifact']], 'Analysis information Artifact; not an actual analysis activity or a Run inferred from its name.'),
        member('Atom/Content Role: Analysis/Type: Rationale', [E['analysis_role'], E['analysis_types'], E['atom'], E['artifact']], 'A Rationale-type Analysis information Artifact, not normative model authority.'),
        member('Projection', [E['projection']], 'A non-authoritative generated information view; distinguish the view from its generation occurrence and represented facts.', 93),
        member('Applicable Methodology', [E['methodology']], 'A non-authoritative reconciled source-content projection; not a Scope Unit or the compilation execution.', 94),
    ]
    occurrents = [
        member('Action Run', [E['action_run'], E['action']], 'An actual invocation with its own definition/input binding, start/terminal outcome, results/effects and durable evidence; no Run is invented by this grouping.', 98),
        member('Step Run', [E['step_run'], E['step']], 'One actual execution within one Workflow Run; a failure or recorded attempt is not successful completion.', 99),
        member('Workflow Run', [E['workflow_run'], E['workflow']], 'One actual execution of one reusable Workflow against supplied inputs/parameters.', 99),
    ]
    unresolved = [
        {'qualified_identity': identity, 'disposition': 'unresolved', 'confidence_percent': 75,
         'evidence_refs': refs, 'reason': reason, 'question_ref': 'temporal-display-convention',
         'native_temporal_classification': 'not_performed'}
        for identity, refs, reason in [
            ('Actor', [E['actor_primary']], 'Primary-Entity taxonomy alone does not establish temporal persistence.'),
            ('Operator', [E['operator']], 'Collective human Actor definition establishes Actor meaning, not an explicit continuant criterion.'),
            ('Carrier', [E['carrier_primary'], E['carrier_binding']], 'Carrier is a Primary Entity, not a bearer-dependent Property; that does not itself admit a temporal class.'),
            ('File Carrier', [E['file_carrier']], 'Concrete File Carrier kind is preserved; its temporal display membership is not established by taxonomy alone.'),
            ('Directory Carrier', [E['directory_carrier']], 'Concrete Directory Carrier kind is preserved; its temporal display membership is not established by taxonomy alone.'),
            ('Scope Unit', [E['scope_unit']], 'Ownership boundary and optional child Scope Units do not independently establish temporal membership.'),
        ]
    ]
    for row in unresolved:
        assert row['qualified_identity'] in nodes

    additional = []
    for child, parent, proof, support in [
        ('Primary Entity', 'Entity', E['primary_entity'], 'direct Main Content requirement'),
        ('Dependent Entity', 'Entity', E['dependent_entity'], 'direct Main Content requirement'),
        ('Artifact', 'Primary Entity', E['artifact_primary'], 'direct Main Content requirement'),
        ('Actor', 'Primary Entity', E['actor_primary'], 'direct Main Content requirement'),
        ('Carrier', 'Primary Entity', E['carrier_primary'], 'direct Delivery Main Content requirement'),
        ('File Carrier', 'Carrier', E['file_carrier'], 'direct Delivery Main Content classification'),
        ('Directory Carrier', 'Carrier', E['directory_carrier'], 'direct Delivery Main Content classification'),
        ('Atom', 'Artifact', E['atom'], 'same-referent implication of the governing definition'),
        ('Property', 'Dependent Entity', E['property'], 'same-referent implication of the governing definition'),
        ('Operator', 'Actor', E['operator'], 'same-referent implication of the governing definition'),
    ]:
        assert child in nodes and parent in nodes
        additional.append({'relation_id': f'1919-{len(additional) + 1:02d}',
                           'qualified_child': child, 'qualified_parent': parent,
                           'canonical_relation': 'NARROWER_THAN', 'graph_kind': 'terms',
                           'canonical_direction': 'narrower_to_broader', 'display_operator': '/',
                           'disposition': 'proposed', 'confidence_percent': 98,
                           'support': support, 'evidence_refs': [proof, E['narrower']],
                           'provenance_kind': 'new_Main_Content_synthesis_not_old_Subject_occurrence',
                           'native_admission': 'not_performed',
                           'boundary': 'Term same-referent relation, not Property ownership, temporal parentage or a new native Entity relation.'})

    constraints = [
        {'constraint_id': 'entity-identity-and-bearer', 'applies_when': 'The current governing Entity definition applies.',
         'rule': 'Preserve independently identified versus bearer-qualified Entity identity. A Dependent Entity requires exactly one immediate bearer; a Property represents one characteristic of its bearer. Do not turn this into a universal concrete IS_BORNE_BY fact.',
         'evidence_refs': [E['entity'], E['primary'], E['dependent'], E['property']],
         'exceptions_and_preservation': 'No exhaustive or disjoint Primary/Dependent partition is inferred; retain exact qualified baseline identities.'},
        {'constraint_id': 'non-ephemeral-carrier-obligation', 'applies_when': 'An Entity is non-ephemeral under applicable authority.',
         'rule': 'Require at least one Carrier through that Entity/Carrier binding. A Shared Carrier and a location may satisfy the binding; being an Entity does not require a separate file.',
         'evidence_refs': [E['non_ephemeral_carrier'], E['carrier_binding']],
         'exceptions_and_preservation': 'The rule is inherited conditionally, never another Entity\'s concrete Carrier identity, path, representation or location. Carrier stays a Primary Entity; its referring Property is separate.'},
        {'constraint_id': 'atom-revision-bundle', 'applies_when': 'The node denotes an Atom Revision, including an admitted Role/Type specialization of Atom.',
         'rule': 'Require exactly one authoritative Carrier Bundle with exactly one Markdown File Carrier and zero or more additional Carriers admitted by Delivery authority.',
         'evidence_refs': [E['atom_bundle'], E['atom'], E['plan_atom'], E['requirement_role'], E['analysis_role'], E['action'], E['workflow'], E['step']],
         'exceptions_and_preservation': 'Do not copy a parent Atom\'s concrete Carrier, fabricate bundles for display groups or replace the required Markdown File Carrier with an extra Carrier.'},
        {'constraint_id': 'carrier-format-not-identity', 'applies_when': 'A Carrier Format or File Extension changes.',
         'rule': 'That change alone does not establish or change the Entity Identity.',
         'evidence_refs': [E['carrier_identity']],
         'exceptions_and_preservation': 'Preserve distinct File Carrier and Directory Carrier model identities and actual bindings; do not inherit a concrete Carrier from a taxonomy parent.'},
        {'constraint_id': 'defaults-not-inherited-settings', 'applies_when': 'Applicable Delivery rules distinguish defaulted Atom Properties and externally inherited Settings.',
         'rule': 'Carry required defaulted Property values; keep unselected optional overrides absent rather than copying an inherited effective Setting; preserve an explicitly selected override even if equal to the inherited value.',
         'evidence_refs': [E['default_vs_inherited']],
         'exceptions_and_preservation': 'A shared rule is not copied configuration, Property ownership, another bearer\'s value or a new qualified identity.'},
        {'constraint_id': 'qualified-status-domains', 'applies_when': 'An Analysis or Plan Atom uses its applicable Status model.',
         'rule': 'Keep the exact Role/Type domain. The default Analysis domain is Draft/Done/Archived and admits only a governed more-specific override under the exact path; the Core Plan domain is Active/Backlog/Done/Canceled/Archived, without Planned.',
         'evidence_refs': [E['analysis_status'], E['plan_status']],
         'exceptions_and_preservation': 'Do not merge these into one universal Status list or treat Artifact Status as Run outcome, receipt, retry or completion. Other roles/types remain unreviewed here.'},
        {'constraint_id': 'definition-view-run-separation', 'applies_when': 'Reusable operational definitions, information views and actual invocations are displayed together.',
         'rule': 'Keep Action/Step/Workflow definitions, their actual Runs, generated views and Journal evidence distinct. Reference/reuse of a definition is not proof of an invocation or effect, and recording an attempt/failure is not successful completion.',
         'evidence_refs': [E['action'], E['workflow'], E['step'], E['workflow_run'], E['step_run'], E['action_run'], E['projection'], E['methodology']],
         'exceptions_and_preservation': 'No new Run, execution, receipt, Journal event, native temporal taxonomy or Core authority is created by the display.'},
    ]
    for row in constraints:
        row.update(disposition='proposed', confidence_percent=97, native_admission='not_performed',
                   concrete_carrier_inheritance='prohibited')

    reviewed = {row['qualified_identity'] for row in continuants + occurrents + unresolved}
    reviewed |= {row[key] for row in additional for key in ('qualified_child', 'qualified_parent')}
    unreviewed = sorted(set(nodes) - reviewed)
    roots = set(baseline['syntactic_roots'])
    root_reviewed = sorted(roots & reviewed)
    groups = [
        {'display_group': 'Continuant', 'label_is_not_entity_identity': True,
         'disposition': 'proposed', 'confidence_percent': 96, 'native_admission': 'not_performed',
         'meaning': 'Local temporal display lens for persistent/reusable information artifacts; not BFO adoption or a native taxonomy root.',
         'members': continuants},
        {'display_group': 'Occurrent', 'label_is_not_entity_identity': True,
         'disposition': 'proposed', 'confidence_percent': 98, 'native_admission': 'not_performed',
         'meaning': 'Local display lens for actual executions/Runs; not reusable definitions, reports, model Subjects or invented executions.',
         'members': occurrents},
    ]
    output = {
        'source_task': 'CA-P-1919', 'baseline_inventory_sha256': EXPECTED_INVENTORY,
        'baseline_file_sha256': EXPECTED_FILE, 'source_binding': baseline['source_binding'],
        'non_authoritative': True, 'source_migration': 'not_performed', 'semantic_admission': 'not_performed',
        'work_boundary': 'Bounded structure design only; not the complete CA-P-1907 node-disposition review, an accepted graph, a migration or an execution Run.',
        'identity_preservation': {'inventory_path': BASELINE.as_posix(), 'inventory_sha256': EXPECTED_INVENTORY,
                                  'all_node_identities_preserved_by_reference': True, 'node_count': len(nodes),
                                  'rename_drop_or_delete_count': 0, 'generated_qualified_identity_count': 0},
        'display_groups': groups, 'unresolved_display_memberships': unresolved,
        'non_temporal_broad_model_anchors': {
            'qualified_identities': ['Entity', 'Primary Entity', 'Dependent Entity', 'Property'],
            'reason': 'Assessed for identity/bearer and broad-model structure only. These model anchors are not put into either temporal group, and no temporal membership of their instances is inferred.',
            'temporal_membership': 'not_assessed',
        },
        'broad_root_candidates': [
            {'qualified_identity': 'Entity', 'evidence_refs': [E['entity']], 'meaning': 'Broad admitted graph-node model, not an ontology root-count conclusion.'},
            {'qualified_identity': 'Primary Entity', 'evidence_refs': [E['primary'], E['primary_entity']], 'meaning': 'Independent-identity anchor for the directly evidenced Artifact/Actor/Carrier term families.'},
            {'qualified_identity': 'Dependent Entity', 'evidence_refs': [E['dependent'], E['dependent_entity'], E['property']], 'meaning': 'Immediate-bearer identity anchor for the directly evidenced Property family.'},
        ],
        'additional_relations': additional, 'inherited_constraints': constraints,
        'rmed_integration_boundary': {
            'model_skeleton': 'R model definitions and required results plus source-backed D Carrier definitions; not R-only.',
            'separate_views': 'M construction/authoring conventions, E checks/acceptance and D representation/placement pointer views are owned by CA-P-1920.',
            'delivery_definitions_preserved': ['Carrier', 'File Carrier', 'Directory Carrier'],
            'inferred_applicability_from_source_role_or_Subject_incidence': False,
        },
        'root_counts': {
            'before': {'literal_syntactic_roots': len(roots), 'branch_roots': len(baseline['branch_roots']),
                       'standalone_roots': len(baseline['standalone_roots'])},
            'candidate': {'proposed_temporal_display_groups': len(groups), 'explicit_unclassified_display_bucket': 1,
                          'literal_syntactic_roots_after_rendering': None, 'independent_native_ontology_roots': None},
            'method': 'Before counts are exact pinned literal Subject-prefix syntax counts, not native taxonomy or independent ontology roots. Two proposed display containers change presentation only. No complete accepted relation graph or all-node disposition exists, so neither a reduced syntax-root count nor an independent ontology-root count is claimed.',
        },
        'coverage': {
            'baseline_nodes': len(nodes), 'baseline_roots': len(roots),
            'distinct_nodes_assessed_in_this_bounded_design': len(reviewed),
            'proposed_temporal_memberships': len(continuants) + len(occurrents),
            'unresolved_temporal_memberships': len(unresolved),
            'additional_relation_count': len(additional), 'inherited_constraint_count': len(constraints),
            'non_temporal_broad_model_anchor_count': 4,
            'assessed_node_identities': sorted(reviewed), 'assessed_syntactic_root_identities': root_reviewed,
            'unreviewed_node_count': len(unreviewed), 'unreviewed_syntactic_root_count': len(roots - reviewed),
            'unreviewed_identity_set': {'method': 'All baseline node identities minus assessed_node_identities.',
                                        'inventory_path': BASELINE.as_posix(), 'inventory_sha256': EXPECTED_INVENTORY,
                                        'sorted_identity_set_sha256': sha(canonical(unreviewed))},
            'unreviewed_preservation': 'Remain visible in an explicit unclassified bucket using exact baseline identities. No default temporal group, parentage, native kind, locus, Carrier or disposition is inferred.',
            'constraints_are_not_complete_family_reviews': True,
        },
        'questions': [{'question_id': 'temporal-display-convention', 'status': 'pending_Operator',
                       'confidence_percent': 75,
                       'question': 'Should Actor, Carrier and Scope Unit appear as Continuant display candidates by deliberate local view convention, or remain outside the two temporal groups until explicit Core temporal evidence is supplied?',
                       'boundary': 'A positive answer supplies local display convention only; it does not admit native temporal taxonomy or automatically classify all descendants.',
                       'affected_identities': [row['qualified_identity'] for row in unresolved],
                       'asked_through_root': True}],
        'evidence_catalogue': evidence,
        'checks_performed': {
            'baseline_canonical_inventory_digest': 'matched', 'baseline_physical_file_digest': 'matched',
            'selected_source_carrier_pins_verified': len(baseline['source_atoms']),
            'excluded_source_carrier_pins_verified': len(baseline['excluded_sources']),
            'evidence_quotes_and_utf8_digests': 'matched exact inclusive Main Content lines',
            'all_proposed_node_references_in_pinned_baseline': True,
            'fake_old_Subject_occurrences': 0, 'native_temporal_relation_proposals': 0,
            'concrete_carrier_binding_inheritance': 0, 'whole_node_disposition_review': 'not_performed',
            'Core_Subject_Plan_Git_MCP_FPF_runtime_writes': 0,
        },
    }
    assert len(reviewed) + len(unreviewed) == len(nodes)
    print(json.dumps(output, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
