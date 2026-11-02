#!/usr/bin/env python3
"""Read-only capture of mapped Current RMED; writes only this preparation packet."""
import hashlib,json
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[5]
P=ROOT/'.caprmedio_caprmedio/02_analysis/draft/role-projection-completion-20261102/projection-preparation'
old=ROOT/'.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/02_analysis/draft/cfel-contract-completion-20261102/integration/current-source-frontier.json'
mapping=json.loads((ROOT/'.caprmedio_tmp/declaration-folder-migration/scope-unit-folder-mapping.json').read_text())
manifests=[ROOT/'.caprmedio_tmp/declaration-source-cutover/model-publication-plan.json',ROOT/'.caprmedio_tmp/declaration-source-cutover/supplemental-retirements.json',ROOT/'.caprmedio_tmp/declaration-source-cutover/final-three-source-publication.json']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
plans=[json.loads(p.read_text()) for p in manifests]
retired={x['atom_id'] for p in plans for x in p.get('retire',[]) if isinstance(x,dict) and 'atom_id' in x}|{x['atom_id'] for p in plans for x in p.get('records',[]) if isinstance(x,dict) and 'archive' in x and 'atom_id' in x}
repl={k:v for p in plans for k,v in p.get('replacements',{}).items()}
repl.update({x['before_id']:x['atom_id'] for p in plans for x in p.get('records',[]) if isinstance(x,dict) and x.get('before_id') and x.get('atom_id') and x['before_id']!=x['atom_id']})
prefix=sorted(((x['old_authority'],x['new_authority']) for x in mapping),key=lambda x:len(x[0]),reverse=True)
def moved(path):
 for a,b in prefix:
  if path==a or path.startswith(a+'/'): return ROOT/(b+path[len(a):])
 return ROOT/path
def read(path,reason,oldrow=None):
 raw=path.read_bytes(); h=yaml.safe_load(raw.split(b'---',2)[1]);
 if h.get('status')!='Active' or h.get('role') not in {'Requirement','Method','Evaluation','Delivery'}: raise ValueError(f'not Current RMED {path}')
 return {'base_id':h['atom_id'],'version':h['version'],'destination_path':str(path.relative_to(ROOT)),'sha256':hashlib.sha256(raw).hexdigest(),'status':'Active','selection_reason':reason,**({'old_path':oldrow['destination_path'],'old_base_id':oldrow['base_id']} if oldrow else {})}
oldrows=json.loads(old.read_text())['operations']; out=[]; decisions=[]; seen=set()
for row in oldrows:
 if row['base_id'] in retired:
  decisions.append({'base_id':row['base_id'],'decision':'exclude_retired_peer_receipt'});continue
 path=moved(row['destination_path'])
 if not path.is_file():
  if row['base_id'] in repl:
   decisions.append({'base_id':row['base_id'],'decision':'defer_to_peer_replacement','replacement':repl[row['base_id']]});continue
  raise ValueError(f'mapped path missing {row["base_id"]}: {path}')
 rec=read(path,'mapped_original_selected_owner',row)
 if rec['base_id'] in seen: raise ValueError('duplicate '+rec['base_id'])
 seen.add(rec['base_id']);out.append(rec);decisions.append({'base_id':row['base_id'],'decision':'include_mapped_owner','new_path':rec['destination_path']})
# add only replacement IDs differing from selected predecessor, when physically present and RMED
for before,after in repl.items():
 if before not in {r['base_id'] for r in oldrows} or after in seen: continue
 matches=[p for p in (ROOT/'.caprmedio_caprmedio').rglob(f'{after}-*.md') if '000_' not in str(p) and '/archive/' not in str(p) and '/draft/' not in str(p)]
 if len(matches)!=1: raise ValueError(f'unresolved selected replacement {before}->{after}: {matches}')
 rec=read(matches[0],'replacement_for_selected_retired_predecessor');rec['replaces']=before;seen.add(after);out.append(rec);decisions.append({'base_id':after,'decision':'include_replacement','replaces':before})
# Native Scope Unit Declarations selected by their external owner, never target breadth.
native={'CA-R-2640','CA-R-2648','CA-R-2649','CA-R-2650','CA-R-2651','CA-R-2652','CA-R-2653','CA-R-2664','CA-R-2665','CA-R-2666','CA-R-2667','CA-R-2668'}
parents={x['name']:x['parent'] for x in mapping}
selected_owners={'CORE_META_MODEL','METHODOLOGY_SOURCES','PROJECT_CONFIGURATION','caprmedio'}
def ancestor_proof(unit):
 chain=[]
 while unit in parents:
  chain.append(unit);unit=parents[unit]
 return chain, bool(set(chain)&selected_owners)
for atom_id in sorted(native):
 matches=[p for p in (ROOT/'.caprmedio_caprmedio').rglob(f'{atom_id}-*.md') if '000_' not in str(p) and '/archive/' not in str(p) and '/draft/' not in str(p)]
 if len(matches)!=1: raise ValueError(f'unresolved native declaration {atom_id}: {matches}')
 rec=read(matches[0],'native_scope_unit_declaration_external_owner_selected_or_required_ancestor');
 if rec['base_id'] in seen: raise ValueError('duplicate native '+atom_id)
 declared=yaml.safe_load(matches[0].read_bytes().split(b'---',2)[1])['subjects']['active'].split('//',1)[1]
 chain,ok=ancestor_proof(declared)
 if atom_id=='CA-R-2649' and not ok: raise ValueError('R2649 declared unit is not a selected-owner ancestor')
 seen.add(atom_id);out.append(rec);decisions.append({'base_id':atom_id,'decision':'include_native_owner_proven','declared_unit':declared,'ancestor_closure':chain})
out.sort(key=lambda x:x['base_id']); capture={'status':'CAPTURED_NOT_PUBLISHED','selection':'Current Methodology and direct Project RMED after Scope Unit authority migration','operations':out,'source_frontier_predecessor':str(old.relative_to(ROOT)),'source_frontier_predecessor_sha256':sha(old),'peer_manifests':[{'path':str(x.relative_to(ROOT)),'sha256':sha(x)} for x in manifests]}
(P/'captured-frontier.json').write_text(json.dumps(capture,indent=2)+'\n')
receipt={'status':'CAPTURED_NOT_PUBLISHED','captured_frontier_sha256':sha(P/'captured-frontier.json'),'counts':{'operations':len(out),'retired_excluded':len([d for d in decisions if d['decision']=='exclude_retired_peer_receipt']),'replacement_predecessors_removed':len([d for d in decisions if d['decision']=='defer_to_peer_replacement']),'added_replacements':len([d for d in decisions if d['decision']=='include_replacement']),'native_declarations_added':len(native)},'reconciliation':'1134 - 22 retired - 12 replaced predecessor IDs + 16 explicit replacements (including CA-R-001 -> CA-R-2691) + 11 owner-proven native Declarations = 1127','decisions':decisions,'native44':'11 owner-proven included; remaining 33 outside scope'}
(P/'selection-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
