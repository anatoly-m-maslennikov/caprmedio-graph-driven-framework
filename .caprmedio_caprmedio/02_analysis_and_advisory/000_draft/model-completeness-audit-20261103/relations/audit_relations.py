"""Read-only inventory of selected Current Relation declarations and formal uses."""
from pathlib import Path
import json,re,hashlib
import yaml
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'.git').exists())
OUT=Path(__file__).resolve().parent
FRONT=ROOT/'.caprmedio_caprmedio/02_analysis/draft/model-completeness-audit-20261103/model-supplier-frontier.json'
f=json.loads(FRONT.read_text());sources=[];catalog={};uses={};aliases={};bindings=[];suspects=[];quoted_templates=[];carrier_uses={};glyph_uses=[]
for entry in f['operations']:
 p=ROOT/entry['destination_path'];s=p.read_text();h=yaml.safe_load(s.split('---',2)[1]);body=s.split('---',2)[2];head=h.get('Header',h);subjects=head.get('Subjects',head.get('subjects',{}));active=subjects.get('Active',subjects.get('active','')) if isinstance(subjects,dict) else ''
 aid=head.get('Atom ID',head.get('atom_id',entry['base_id']));role=head.get('Role',head.get('role'));form=head.get('Form',head.get('form'));status=head.get('Status',head.get('status'))
 record={'atom_id':aid,'path':entry['destination_path'],'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'frontier_sha256':entry['sha256'],'pin_matches':hashlib.sha256(p.read_bytes()).hexdigest()==entry['sha256'],'role':role,'form':form,'status':status,'active_subject':active}
 sources.append(record)
 for name, targets in (head.get('Relations',head.get('relations',{})) or {}).items():
  carrier_uses.setdefault(name,[]).append({**record,'targets':targets})
 m=re.search(r'Relation//([A-Za-z_][A-Za-z_0-9]*)\s*$',str(active))
 if m and role=='Requirement' and form=='Declaration' and status=='Active':
  rel=m[1];catalog.setdefault(rel,[]).append({**record,'text':s,'formal':[],'prose':[]})
 for block in re.finditer(r'```CFEL[^\n]*\n(.*?)```',s,re.S):
  start=s[:block.start(1)].count('\n')+1
  for offset,line in enumerate(block[1].splitlines()):
   item={'atom_id':aid,'path':entry['destination_path'],'line':start+offset,'text':line}
   unquoted=re.sub(r'"(?:\\.|[^"\\])*"','',line)
   for rel in re.findall(r'<?\(\(([A-Za-z_][A-Za-z_0-9]*|\*)\)\)',unquoted):uses.setdefault(rel,[]).append(item)
   if re.search(r'<?\(\(\w+\)\)',line) and not re.search(r'<?\(\(\w+\)\)',unquoted):quoted_templates.append(item)
   if re.search(r'>\||\|<',unquoted):glyph_uses.append({**item,'relation':'HAS_CLASSIFICATION'})
   for rel,token in re.findall(r'alias\(Relation//([A-Za-z_][A-Za-z_0-9]*)\)\s*==\s*"([^"]*)"',line):aliases.setdefault(token,[]).append({**item,'relation':rel})
   for a,rev,b in re.findall(r'Relation//(\w+)\s*(<)?\(\(HAS_INVERSE\)\)\s*Relation//(\w+)',line):bindings.append({**item,'direct':b if rev else a,'inverse':a if rev else b,'reverse_written':bool(rev)})
   if re.search(r'^\s*\(\(\w+\)\)|\(\(\w+\)\)\s*>\||alias\((?!Relation//)[A-Za-z_]|@(?=[A-Za-z_])',line):suspects.append({**item,'kind':'legacy-object-or-alias-reference-syntax'})
   if re.search(r'\(\(\w+\)\)\s*:',line):suspects.append({**item,'kind':'colon-after-relation-operator-check'})
   if m and role=='Requirement' and form=='Declaration' and status=='Active':catalog[m[1]][-1]['formal'].append(item)
# Compact JSON inventory retains complete declaration body in separate source files, not duplicate report text.
for name,entries in catalog.items():
 for entry in entries:
  text=entry.pop('text')
  chunks=re.split(r'^### Prose Claim\s*$',text,flags=re.M)
  prose=chunks[1] if len(chunks)>1 else ''
  semantics=re.search(r'^## Semantics\s*\n(.*?)(?=^## |\Z)',text,re.M|re.S)
  entry['effective_own_prose']=prose.strip()
  entry['separate_semantics']=semantics[1].strip() if semantics else ''
  direct={x['inverse']:x['direct'] for x in bindings}
  entry['inverse_source_relation']=direct.get(name)
  entry['effective_endpoint_semantics_owner']=direct.get(name,name)
  entry['derived_non_inverse']=name=='IS_DEFINED_BY'
  entry['own_unbounded_signature_is_not_permission']=True
unknown={k:v for k,v in uses.items() if k not in catalog and k!='*'}
result={'frontier':str(FRONT.relative_to(ROOT)),'frontier_sha256':hashlib.sha256(FRONT.read_bytes()).hexdigest(),'selected_sources':len(sources),'sources':sources,'declaredRelations':len(catalog),'catalog':catalog,'actual_named_relation_uses':uses,'undeclared_predicates':unknown,'aliases':aliases,'alias_collisions':{k:v for k,v in aliases.items() if len({x['relation'] for x in v})>1},'inverse_bindings':bindings,'syntax_suspects':suspects,'duplicate_declarations':{k:v for k,v in catalog.items() if len(v)!=1},'source_drift':[x for x in sources if not x['pin_matches']],'quoted_operator_templates':quoted_templates,'carrier_relation_uses':carrier_uses,'undeclared_carrier_keys':{k:v for k,v in carrier_uses.items() if k not in catalog},'formal_classification_alias_uses':glyph_uses}
(OUT/'inventory.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:(len(v) if isinstance(v,(dict,list)) else v) for k,v in result.items() if k not in ('frontier','frontier_sha256')},indent=2))
