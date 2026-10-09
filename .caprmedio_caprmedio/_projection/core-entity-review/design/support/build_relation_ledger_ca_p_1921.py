"""CA-P-1921 deterministic integration. Default is read-only; --persist is create-only."""
import argparse
import collections
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path.cwd().resolve()
DESIGN = '.caprmedio_caprmedio/_projection/core-entity-review/design'
TEMP = '.caprmedio_tmp/planning/core-entity-review/design'
BASELINE = '.caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json'
BASELINE_SHA = 'bc5d99e91fb7dd4dcb42e59ff33cc24cff1d0901c5904764394c769aaa0a9430'
INVENTORY_SHA = '23394abaf6e9c18a585cf3146aedd0a80df166c9dd82be6e86ed7c3c56780bdc'
EPIC = '.caprmedio_caprmedio/03_plan/14-CA-P-1105-EPIC--validate-atoms-and-their-derived-graphs/05-CA-P-1110-TASK--build-entities-graph-and-terms-graph-generators/01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca'
BATCH_SHAS = [
    '6038646bf9aad5fa7d2254978f90bfae5b62dda23ee8a36d855af3d8e2c6c631',
    'f1bcafd79233fea0ced091fc7df91d1f7fda47edaf1d5b52d130cf2b45c08729',
    '9bc2309603eaa8283fbda2ff9f99df543c594102457db7824e7a583a7621bafe',
    '3ad64852b98716443257e0d726346b0a6d6105f4f96ed9d90953dcabc4d3da44',
    '108005779ebd301ada886e8a9ae2f57cda2f6576805325ba65f679faf29d6697',
    '5bef9b0c040b4ffad63df24c2c9290e3e539aa1b434792c7f6b27d6151130812',
]
PREREQUISITES = {
    'CA-P-1905': '85abb34a3050db6d2360543a5340561d93c1fca853f3e439df4d432a5ed5ab9a',
    'CA-P-1913': '0b02fcc89fa2af9279f78f36c3d2f41666dc8ecee2d041c081aeac2b896be684',
    'CA-P-1914': '60eb4523c75216babfd9f29042600b9b610c5cab8d393d4b26e7a12a27764009',
    'CA-P-1915': '5521f8e38eec326af9cb9650386125b597cd97ce4e10f3cbf8e356e0231b6315',
    'CA-P-1916': 'a0da349d1cb7b487bd0f46c2ae94b80ba1ddfeb2cd037bf1f79aa8ce63689613',
    'CA-P-1917': '9eabb25ca6fa1886680c5f34f931237bbeb71651d8514acfffeaa7b80adb06f1',
    'CA-P-1918': 'c9463e665eaedebba2191fc24e08e47d5a5a7731420f1d6be03c2ae7481567c7',
    'CA-P-1919': 'b70e6a5d3fbffa239de409011345a1cf956a5908906b573b98a7bfc1d544f3f6',
    'CA-P-1920': '50643235849ee4f43c53c0bc0d2f4a8cd71f10cc5efafa844d998dfcd4ad5635',
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def serialized(value):
    return canonical(value) + b'\n'


def safe_path(relative):
    path = ROOT / relative
    assert path.resolve().is_relative_to(ROOT), relative
    assert not path.is_symlink(), relative
    for parent in path.parents:
        if parent == ROOT:
            break
        assert not parent.is_symlink(), relative
    return path


def load_pinned(relative, expected):
    raw = safe_path(relative).read_bytes()
    assert sha(raw) == expected, ('input-pin-stale', relative)
    return json.loads(raw), {'path': relative, 'sha256': expected, 'bytes': len(raw)}


def plan_pin(atom_id, expected):
    import generate_entity_graph as graph
    matches = []
    for path in (ROOT / EPIC).rglob(f'*-{atom_id}-*.md'):
        if 'archive' in path.parts:
            continue
        raw = safe_path(path.relative_to(ROOT).as_posix()).read_bytes()
        frontmatter = graph.split_frontmatter(raw, path.relative_to(ROOT).as_posix())
        assert frontmatter is not None, ('Plan-frontmatter-missing', atom_id)
        version = graph.top_scalar(frontmatter, 'version')
        assert version is not None and re.fullmatch(r'[1-9][0-9]*', version), ('Plan-version-invalid', atom_id)
        metadata = {'atom_id': graph.top_scalar(frontmatter, 'atom_id'),
                    'status': graph.top_scalar(frontmatter, 'status'), 'version': int(version)}
        if metadata.get('atom_id') == atom_id:
            matches.append((raw, metadata))
    assert len(matches) == 1, ('Plan-identity-ambiguous-or-missing', atom_id)
    raw, metadata = matches[0]
    assert sha(raw) == expected and metadata['status'] == 'Done', ('prerequisite-stale', atom_id)
    return {'atom_id': atom_id, 'carrier_sha256': expected, 'version': metadata['version'], 'status': 'Done'}


def evidence_check(row, sources, contents):
    source = sources[row['atom_id']]
    for key in ('atom_revision', 'carrier_path', 'carrier_sha256'):
        assert row[key] == source[key], (row['atom_id'], key)
    lines = contents[row['atom_id']].decode().splitlines()
    start, end = row['start_line'], row['end_line']
    assert type(start) is int and type(end) is int and 1 <= start <= end <= len(lines)
    assert start > next(i for i, line in enumerate(lines[1:], 2) if line == '---')
    expected = '\n'.join(lines[start - 1:end])
    assert row['quote'] in (expected, expected + '\n')
    assert row['text_sha256'] == sha(row['quote'].encode())
    assert any(line.startswith(('## Claim', '## Procedure', '## Condition', '## Operation', '## Definition', '## Details', '## Scope', '## Evaluation')) for line in lines[:start])


def build():
    baseline, baseline_pin = load_pinned(BASELINE, BASELINE_SHA)
    assert baseline['inventory_sha256'] == INVENTORY_SHA
    assert sha(canonical({k: v for k, v in baseline.items() if k != 'inventory_sha256'})) == INVENTORY_SHA
    graph, graph_pin = load_pinned(baseline['baseline']['path'], baseline['baseline']['sha256'])
    assert sha(canonical({k: v for k, v in graph.items() if k != 'graph_sha256'})) == graph['graph_sha256']
    profile = graph['producer']
    assert sha(canonical(profile['profile_payload'])) == profile['profile_sha256'] == baseline['baseline']['producer_profile_sha256']
    for name in ('implementation', 'snapshot', 'source_reader', 'subject_parser', 'fact_context'):
        item = profile['profile_payload'][name]
        path = Path(item['loaded_path'])
        assert path.resolve().is_relative_to(ROOT) and sha(path.read_bytes()) == item['sha256'], ('producer-stale', name)
    sys.path.insert(0, str(ROOT / '102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH'))
    import subject_notation_snapshot as snapshot
    carriers, frontier, selection = snapshot.current_core_inputs(ROOT)
    current = snapshot.prepare_subject_notation_snapshot(ROOT, carriers, frontier, selection).as_dict()
    assert current['source_binding'] == baseline['source_binding'] and selection == baseline['selection']
    assert current['source_atoms'] == baseline['source_atoms'] and current['excluded_sources'] == baseline['excluded_sources']
    sources = {row['atom_id']: row for row in baseline['source_atoms']}
    contents = {}
    for source in baseline['source_atoms'] + baseline['excluded_sources']:
        raw = safe_path(source['carrier_path']).read_bytes()
        assert sha(raw) == source['carrier_sha256'], source['atom_id']
        if source['atom_id'] in sources:
            contents[source['atom_id']] = raw
    registration = baseline['registration']['source']
    assert sha(safe_path(registration['carrier_path']).read_bytes()) == registration['carrier_sha256']
    prerequisites = [plan_pin(atom_id, digest) for atom_id, digest in sorted(PREREQUISITES.items())]
    batches, input_pins, case_reviews, case_origins = [], [baseline_pin, graph_pin], [], {}
    for number, digest in enumerate(BATCH_SHAS, 1):
        name = f'relations.batch-{number}' + ('.final' if number == 6 else '') + '.json'
        batch, pin = load_pinned(f'{DESIGN}/{name}', digest)
        assert batch['baseline_inventory_sha256'] == INVENTORY_SHA and batch['source_binding'] == baseline['source_binding']
        assert batch['batch_number'] == number and batch['semantic_admission'] == 'not_performed' and batch['source_migration'] == 'not_performed'
        for child in batch.get('child_completion_pins', []):
            plan_pin(child['atom_id'], child['carrier_sha256'])
        for receipt in batch.get('reviewed_partition_receipts', []):
            load_pinned(receipt['path'], receipt['sha256'])
        if batch.get('input_checkpoint'):
            load_pinned(batch['input_checkpoint']['path'], batch['input_checkpoint']['sha256'])
        batches.append(batch)
        input_pins.append(pin)
        for row in batch['cases']:
            assert row['disposition'] in ('proposed', 'not-native', 'unresolved')
            assert row['case_id'] not in case_origins
            assert row['disposition'] == 'proposed' or row['proposal'] is None
            assert row['reason'] and row['checks_performed']
            if row['disposition'] == 'unresolved':
                assert row['question']
            for evidence in row['evidence']:
                evidence_check(evidence, sources, contents)
            if row.get('display_candidate'):
                assert row['evidence'] and row['confidence_percent'] >= 90
            case_reviews.append(row)
            case_origins[row['case_id']] = {'input_pin': pin, 'source_task': batch['source_task'], 'batch_number': number}
    case_reviews.sort(key=lambda row: row['case_id'])
    by_pair = {(row['old_parent'], row['old_child']): row for row in case_reviews}
    segments = baseline['relation_segment_inventory']
    slash_pairs = {(row['original_qualified_parent'], row['original_qualified_child']) for row in segments if row['source_separator'] == '/'}
    assert len(case_reviews) == len(by_pair) == 294 and set(by_pair) == slash_pairs
    assert len(segments) == 3093 and collections.Counter(row['source_separator'] for row in segments) == {'/': 2275, ':': 818}
    structure, structure_pin = load_pinned(f'{DESIGN}/structure.design.json', '10733c9f1b6b8d5946acdc469e7cfe3ee710ed515f1de77eed765c2252652b9e')
    rmed, rmed_pin = load_pinned(f'{DESIGN}/rmed.views.json', 'd7fd113a408c3bb70e17ab55cc86fd6746c3d5c74ff27a9a864632ec6de999aa')
    for item in (structure, rmed):
        assert item['baseline_inventory_sha256'] == INVENTORY_SHA and item['source_binding'] == baseline['source_binding']
    input_pins.extend([structure_pin, rmed_pin])
    for evidence in structure['evidence_catalogue'].values():
        evidence_check(evidence, sources, contents)

    crosswalk = []
    for node in baseline['nodes']:
        identity = node['identity']
        steps = snapshot._prefix_steps(identity)
        markers = list(re.finditer(r'[/:]', identity))
        chain, blockers, characters = [], [], list(identity)
        for index, (parent, child, operator, left, right) in enumerate(steps):
            if operator == ':':
                chain.append({'segment_index': index, 'source_separator': ':', 'disposition': 'unchanged-syntax', 'display_operator': ':', 'assignment_inferred': False, 'native_relation': None})
                continue
            row = by_pair[(parent, child)]
            display = row.get('display_candidate')
            chosen = (display or {}).get('display_operator', (display or {}).get('operator'))
            evidenced = bool(display and row['evidence'] and row['confidence_percent'] >= 90 and chosen in ('.', '/', '@') and row['disposition'] != 'unresolved')
            chain.append({'segment_index': index, 'source_separator': '/', 'case_id': row['case_id'], 'disposition': row['disposition'], 'display_operator': chosen if evidenced else None, 'native_relation': None})
            if evidenced:
                characters[markers[index].start()] = chosen
            else:
                blockers.append({'case_id': row['case_id'], 'disposition': row['disposition'], 'reason': 'No evidenced display candidate for this exact slash segment.'})
        proposed_path = ''.join(characters) if not blockers else identity
        crosswalk.append({'baseline_identity': identity, 'preserved_identity': identity, 'proposed_display_path': proposed_path,
                          'display_rebase': 'blocked_chain_original_preserved' if blockers else ('evidenced_display_only' if proposed_path != identity else 'unchanged'),
                          'qualification_chain': chain, 'blocking_decisions': blockers,
                          'canonical_identity_rewrite': 'not_performed', 'serialized_Subject_rewrite': 'not_performed',
                          'display_path_is_not_Subject_grammar': True, 'native_relation_inferred': False})
    proposed_names = collections.defaultdict(list)
    for row in crosswalk:
        proposed_names[row['proposed_display_path']].append(row)
    collisions = []
    for display, rows in sorted(proposed_names.items()):
        if len(rows) <= 1:
            continue
        collisions.append({'display_path': display, 'baseline_identities': [row['baseline_identity'] for row in rows]})
        for row in rows:
            row['proposed_display_path'] = row['baseline_identity']
            row['display_rebase'] = 'blocked_display_collision_original_preserved'
            row['blocking_decisions'].append({'disposition': 'unresolved', 'reason': 'Distinct preserved identities would share an ambiguous display path.'})
    by_identity = {row['baseline_identity']: row for row in crosswalk}
    assert len(crosswalk) == len(by_identity) == 706
    assert len({row['proposed_display_path'] for row in crosswalk}) == 706

    occurrence_crosswalk, segment_reviews = [], []
    segment_ids_by_occurrence = collections.defaultdict(list)
    for segment in segments:
        segment_ids_by_occurrence[segment['occurrence_id']].append(segment['segment_id'])
        if segment['source_separator'] == ':':
            review = {'segment_id': segment['segment_id'], 'case_id': None, 'disposition': 'unchanged-syntax', 'native_proposal': None, 'display_candidate_ref': None, 'assignment_inferred': False, 'allowed_value_relation_admitted': False}
        else:
            row = by_pair[(segment['original_qualified_parent'], segment['original_qualified_child'])]
            review = {'segment_id': segment['segment_id'], 'case_id': row['case_id'], 'disposition': row['disposition'], 'native_proposal': row['proposal'], 'display_candidate_ref': row['case_id'] if row.get('display_candidate') else None, 'native_admission': 'not_performed'}
        segment_reviews.append(review)
    for occurrence in baseline['occurrences']:
        row = by_identity[occurrence['subject_path']]
        source = occurrence['source_ref']
        span = source['contribution']
        raw = contents[source['atom_id']].splitlines(keepends=True)
        assert sha(b''.join(raw[span['start_line'] - 1:span['end_line']])) == span['text_sha256']
        occurrence_crosswalk.append({'occurrence_id': occurrence['occurrence_id'], 'original_subject_path': occurrence['subject_path'],
                                    'preserved_identity': occurrence['subject_path'], 'proposed_display_path': row['proposed_display_path'],
                                    'display_rebase': row['display_rebase'], 'original_role': occurrence['role'],
                                    'original_segment_ids': segment_ids_by_occurrence[occurrence['occurrence_id']],
                                    'source_coordinates_and_pins': 'retained verbatim in relations.ledger.json original_occurrences and original_segments',
                                    'serialized_Subject_rewrite': 'not_performed'})
    assert len(occurrence_crosswalk) == len(baseline['occurrences']) == 4534
    dispositions = dict(collections.Counter(row['disposition'] for row in case_reviews))
    counts = {'slash_cases': 294, 'original_segments': 3093, 'slash_segments': 2275, 'colon_segments': 818,
              'original_occurrences': 4534, 'preserved_node_identities': 706, 'case_dispositions': dispositions,
              'evidenced_display_candidates': sum(bool(row.get('display_candidate')) for row in case_reviews),
              'identity_display_rebases': dict(collections.Counter(row['display_rebase'] for row in crosswalk)),
              'additional_Term_relation_proposals': 10, 'inherited_constraints': 7,
              'temporal_display_memberships': 20, 'structure_nodes_assessed': 24, 'structure_nodes_unreviewed': 682,
              'display_namespace_collisions': len(collisions), 'native_slash_proposals': sum(row['proposal'] is not None for row in case_reviews)}
    assert len(structure['additional_relations']) == 10 and len(structure['inherited_constraints']) == 7
    assert structure['coverage']['total_temporal_memberships'] == 20 and structure['coverage']['distinct_nodes_assessed_in_this_bounded_design'] == 24 and structure['coverage']['unreviewed_node_count'] == 682
    envelope = {'schema_version': 1, 'source_task': 'CA-P-1921', 'non_authoritative': True,
                'semantic_admission': 'not_performed', 'source_migration': 'not_performed', 'Operator_acceptance': 'not_performed',
                'baseline_inventory_sha256': INVENTORY_SHA, 'source_binding': baseline['source_binding'],
                'input_pins': input_pins, 'prerequisite_completion_pins': prerequisites,
                'prerequisite_locator_rule': 'Locate current unarchived Plan Carrier by exact Atom ID and verify frozen bytes/status; carrier moves do not alter this canonical output.',
                'producer': {'path': f'{DESIGN}/support/build_relation_ledger_ca_p_1921.py', 'sha256': sha(Path(__file__).read_bytes())},
                'checks_performed': {'complete_current_Core_frontier_selection_collection': 'matched', 'source_pins_verified': 951,
                                     'producer_profile_and_five_components': 'matched', 'original_contribution_spans': 'matched',
                                     'Main_Content_evidence_spans': 'matched', 'source_and_Model_identity_namespaces': 'kept_distinct',
                                     'all_original_identity_occurrence_segment_sets': 'preserved', 'native_display_inference': 'not_performed'},
                'counts': counts}
    ledger = {**envelope, 'projection_kind': 'caprmedio.core_entity_review.proposed_relation_ledger',
              'original_nodes': baseline['nodes'], 'original_occurrences': baseline['occurrences'], 'original_segments': segments,
              'case_reviews': case_reviews, 'case_review_origins': case_origins, 'segment_reviews': segment_reviews,
              'node_identity_crosswalk': crosswalk, 'occurrence_crosswalk': occurrence_crosswalk,
              'colon_policy': 'Retain original syntax only: no assignment or native allowed-value relation is invented.',
              'display_policy': 'All relevant slash segments need their own evidenced display candidate. Missing candidates and unresolved chains retain original identity; a dot or named canonical kind inside raw display evidence never becomes a native fact.',
              'display_collisions': collisions,
              'additional_relations': {'source_pin': structure_pin, 'proposals': structure['additional_relations'], 'evidence_catalogue': structure['evidence_catalogue'], 'fabricated_original_occurrences': False},
              'inherited_constraints': {'source_pin': structure_pin, 'constraints': structure['inherited_constraints'], 'concrete_Carrier_inheritance': 'prohibited'},
              'shared_RMED_views': {'input_pin': rmed_pin, 'role_centered_view': 'role_centered_overview', 'Entity_centered_view': 'entity_centered_view', 'authority_copied_or_inferred': False}}
    ledger_bytes = serialized(ledger)
    candidate = {**envelope, 'projection_kind': 'caprmedio.core_entity_review.non_authoritative_candidate_structure',
                 'relation_ledger': {'path': f'{DESIGN}/relations.ledger.json', 'sha256': sha(ledger_bytes)},
                 'preserved_node_ids': [row['identity'] for row in baseline['nodes']], 'node_identity_crosswalk': crosswalk,
                 'occurrence_crosswalk': occurrence_crosswalk, 'native_edges_from_display_rewrites': [],
                 'qualification_display_decisions': [{'case_id': row['case_id'], 'qualified_parent': row['old_parent'], 'qualified_child': row['old_child'], 'display_candidate_as_reviewed': row.get('display_candidate'), 'native_relation': None, 'semantic_admission': 'not_performed'} for row in case_reviews if row.get('display_candidate')],
                 'unresolved_case_refs': [row['case_id'] for row in case_reviews if row['disposition'] == 'unresolved'],
                 'unresolved_questions_and_reasons': 'Preserved without alteration in pinned relation_ledger case_reviews.',
                 'display_groups': structure['display_groups'], 'structure_coverage': structure['coverage'],
                 'non_temporal_broad_model_anchors': structure['non_temporal_broad_model_anchors'],
                 'operator_display_decisions': structure['operator_display_decisions'],
                 'occurrence_record_and_persistence_boundary': structure['occurrence_record_and_persistence_boundary'],
                 'structure_evidence_reference': {'input_pin': structure_pin, 'field': 'evidence_catalogue'},
                 'additional_Term_relations_reference': {'ledger_field': 'additional_relations', 'count': 10, 'native_admission': 'not_performed'},
                 'inherited_constraints_reference': {'ledger_field': 'inherited_constraints', 'count': 7, 'concrete_Carrier_inheritance': 'prohibited'},
                 'shared_RMED_views': ledger['shared_RMED_views'], 'root_counts': structure['root_counts'],
                 'candidate_is_not_accepted_or_serialized_Subjects': True, 'display_collisions': collisions}
    return ledger_bytes, serialized(candidate), counts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--artifact', choices=('summary', 'ledger', 'candidate'), default='summary')
    parser.add_argument('--persist', action='store_true')
    parser.add_argument('--verify-output', action='store_true')
    args = parser.parse_args()
    assert not (args.persist and args.verify_output)
    ledger, candidate, counts = build()
    expected = {f'{folder}/{name}': raw for folder in (DESIGN, TEMP) for name, raw in [('relations.ledger.json', ledger), ('candidate.structure.json', candidate)]}
    if args.persist or args.verify_output:
        for relative, raw in expected.items():
            path = safe_path(relative)
            assert path.parent.is_dir()
            if path.exists():
                assert path.is_file() and path.read_bytes() == raw, ('existing-artifact-differs-no-overwrite', relative)
            elif args.verify_output:
                raise AssertionError(('output-missing', relative))
        if args.persist:
            for relative, raw in expected.items():
                path = safe_path(relative)
                if not path.exists():
                    with path.open('xb') as handle:
                        handle.write(raw)
    if args.artifact == 'ledger':
        sys.stdout.buffer.write(ledger)
    elif args.artifact == 'candidate':
        sys.stdout.buffer.write(candidate)
    else:
        print(json.dumps({'outcome': 'verified' if args.verify_output else ('persisted_or_existing_identical' if args.persist else 'dry_run'),
                          'counts': counts, 'outputs': [{'path': relative, 'sha256': sha(raw), 'bytes': len(raw)} for relative, raw in expected.items()]}, sort_keys=True))


if __name__ == '__main__':
    main()
