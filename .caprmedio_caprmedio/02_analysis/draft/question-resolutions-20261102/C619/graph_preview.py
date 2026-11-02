import copy, json, sys
from pathlib import Path

repo = Path.cwd().resolve()
tool = repo / '102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH'
sys.path.insert(0, str(tool))
sys.path.insert(0, str(tool.parent))
from current_entity_sources import _read_atom
from contract_graph import compose_contract_graph

frontier_path = repo / '.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/02_analysis/draft/cfel-contract-completion-20261102/integration/current-source-frontier.json'
frontier = json.loads(frontier_path.read_text())
selected = {row['destination_path'] for row in frontier['operations'] if row.get('destination_path')}
root = repo / '.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL'
carriers = []
for relative in sorted(selected):
    path = repo / relative
    if not path.is_file():
        continue
    item = _read_atom(path, repo)
    if item is not None:
        carriers.append(item)

def summary(graph):
    cov = graph['coverage']
    return {
        'coverage': cov,
        'outcome': graph['outcome'],
        'display_coverage': graph['display_coverage'],
        'gap_ids': sorted({row['source']['atom_id'] for row in graph['coverage_gaps']}),
        'outside_scope_count': len(graph['outside_model_scope']),
        'duplicate_targets': [row['target'] for row in graph['conflicts']],
        'instance_kind_gaps': graph['instance_kind_gaps'],
        'inheritance_diagnostics': graph['inheritance_diagnostics'],
    }

baseline = compose_contract_graph(carriers)
counter = []
for carrier in carriers:
    atom = carrier['source']['atom_id']
    if atom == 'CA-R-2627':
        continue
    item = copy.deepcopy(carrier)
    if atom == 'CA-R-2532':
        for key in ('body', 'raw_body'):
            item[key] = item[key].replace(', Extension Selections,', ',').replace('{:3..13}', '{:3..12}')
    counter.append(item)
counterfactual = compose_contract_graph(counter)
baseline_gaps = set(summary(baseline)['gap_ids'])
counterfactual_gaps = set(summary(counterfactual)['gap_ids'])
out = {
    'kind': 'C619_counterfactual_contract_graph_preview',
    'frontier': str(frontier_path.relative_to(repo)),
    'selection_count': len(carriers),
    'counterfactual': 'remove CA-R-2627; edit CA-R-2532 in memory only',
    'baseline': summary(baseline),
    'counterfactual_graph': summary(counterfactual),
    'delta': {
        key: counterfactual['coverage'][key] - baseline['coverage'][key]
        for key in baseline['coverage'] if isinstance(baseline['coverage'][key], int)
    },
    'new_gap_ids': sorted(counterfactual_gaps - baseline_gaps),
}
print(json.dumps(out, indent=2, sort_keys=True))
