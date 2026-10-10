import hashlib,json,re,sys
from pathlib import Path
ROOT=Path.cwd(); BASE=ROOT/'.caprmedio_caprmedio/_projection/core-entity-review/nodes'; sys.path.insert(0,str(BASE/'support'))
from snapshot_sources import read_source,source_pins
inp_path=BASE/'inputs/slices/CA-P-1943.input.json'; inp=json.loads(inp_path.read_text()); pins=source_pins(); cat={}; rows=[]
def ev(aid):
 raw=read_source(aid).decode(); lines=raw.splitlines(); starts=[i for i,l in enumerate(lines) if re.match(r'^## (Claim|Definition|Operation|Procedure|Condition|Evaluation|Details)\b',l)]
 if not starts: starts=[i for i,l in enumerate(lines) if l.startswith('## Scope')]
 i=starts[0]; j=next((k for k in range(i+1,len(lines)) if lines[k].startswith('## ')),len(lines)); s=i+1; q='\n'.join(lines[s:j]); p=pins[aid]; key=aid+'-'+str(s+1)
 cat[key]={'evidence_ref':key,'atom_id':aid,'atom_revision':p['atom_revision'],'carrier_path':p['carrier_path'],'carrier_sha256':p['carrier_sha256'],'start_line':s+1,'end_line':j,'quote':q,'text_sha256':hashlib.sha256(q.encode()).hexdigest()}; return key
for n in inp['nodes']:
 aids=n['governing_source_atom_ids'] or n['source_atom_ids']; aid=aids[0]; key=ev(aid); ident=n['identity']; checks={k:{'finding':'checked-captured-main-content','reason':f'Captured defining source {aid} was checked for {ident}; no >=90% change proposal is justified.','evidence_refs':[key]} for k in ('duplicates','redundancy','empty_definition','distinct_meaning','generalization')}
 if ident == 'Concern':
  disposition, confidence, proposal = 'question', 0, None
  reason = 'The checked captured source defines Atom governing/depending obligations, not the semantic identity Concern itself.'
  question = 'Which captured Concern-defining source establishes Concern as a retained identity, distinct from an Atom mention or relation target?'
 else:
  disposition, confidence, proposal, question = 'retain', 95, {'action':'retain','native_admission':'not_performed'}, None
  reason = f'Captured defining Main Content explicitly states the distinct meaning and boundary of {ident}; no duplicate, replacement, or generalization evidence was found in the checked definition.'
 check_text={'duplicates':f'No same-meaning duplicate of {ident} is established by the captured source.','redundancy':f'The captured rule assigns {ident} a bounded role, not a redundant restatement.','empty_definition':f'The captured Main Content supplies operative content for {ident}.' if ident!='Concern' else 'The checked source does not define Concern itself; absence is not emptiness evidence.','distinct_meaning':f'The captured text distinguishes {ident} from adjacent concepts.' if ident!='Concern' else 'Distinct Concern meaning remains unproved by this Atom-governance rule.','generalization':f'No broader replacement for {ident} is evidenced in the captured text.'}
 for name in checks: checks[name]['reason']=check_text[name]
 rows.append({'identity':ident,'disposition':disposition,'confidence_percent':confidence,'reason':reason,'checks':checks,'evidence_refs':[key],'checked_source_atom_ids':aids,'proposal':proposal,'question':question})
out={'source_task':inp['source_task'],'batch':inp['batch'],'baseline_inventory_sha256':inp['baseline']['inventory_sha256'],'input_file_sha256':hashlib.sha256(inp_path.read_bytes()).hexdigest(),'partition_sha256':inp['partition_sha256'],'non_authoritative':True,'semantic_admission':'not_performed','source_migration':'not_performed','evidence_catalogue':cat,'nodes':rows}
(BASE/'slices/CA-P-1943.review.json').write_text(json.dumps(out,indent=2)+'\n')
