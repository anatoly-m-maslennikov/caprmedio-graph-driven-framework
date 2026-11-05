from pathlib import Path
import json,hashlib,collections,re,yaml,copy
from yaml.nodes import MappingNode,ScalarNode
B=Path('.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/coverage/ordered-source-migration-20261105');O=B/'destinations';plan=B/'metadata/adoption-plan.json';inventory=json.loads(plan.read_text())['inventory'];sha=lambda b:hashlib.sha256(b).hexdigest();scope_file=Path('.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/coverage/scope-declaration-check-20261105/inventory.json');scope=json.loads(scope_file.read_text());scope_names=collections.defaultdict(set);scope_ids=set()
scope_pins=[]
for row in inventory:
 p=Path(row['path'])
 if '/draft/' in str(p): continue
 try:
  raw=p.read_bytes(); text=raw.decode(); meta=yaml.safe_load(text.split('---',2)[1])
  if not isinstance(meta,dict) or meta.get('form')!='Scope Unit Declaration': continue
  if meta.get('atom_id')=='CA-R-2640':
   scope_names['caprmedio'].add('CA-SU-00');scope_ids.add('CA-SU-00');scope_pins.append({'path':str(p),'sha256':sha(raw)});continue
  nm=re.search(r'Scope Unit//([A-Za-z0-9_]+)\.Name\s*==\s*"([^"]+)"',text)
  si=re.search(r'Scope Unit//([A-Za-z0-9_]+)\.ID\s*==\s*"(CA-SU-[0-9]+)"',text)
  if not nm or not si or nm.group(1)!=si.group(1):continue
  scope_names[nm.group(1)].add(si.group(2));scope_names[nm.group(2)].add(si.group(2));scope_ids.add(si.group(2));scope_pins.append({'path':str(p),'sha256':sha(raw)})
 except (OSError,ValueError,yaml.YAMLError):continue

# Derive physical Scope Unit paths from pinned Declaration fields, never directory names alone.
scope_defs={'CA-SU-00':{'name':'caprmedio','path':Path('.caprmedio_caprmedio'),'source':next(x['path'] for x in scope_pins if Path(x['path']).name.startswith('CA-R-2640-'))}}
for pin in scope_pins:
 p=Path(pin['path']);text=p.read_text()
 if p.name.startswith('CA-R-2640-'):continue
 def field(k):
  match=re.search(r'\.'+re.escape(k)+r'\s*==\s*(?:"([^"]+)"|(true|false|\d+))',text);return (match.group(1) or match.group(2)) if match else None
 sid=field('ID'); name=field('Name'); parent=re.search(r'\(\(IS_CONTAINED_BY\)\)\s*(?:Scope Unit|Project)//([A-Za-z0-9_]+)',text)
 if sid and name and parent:scope_defs[sid]={'name':name,'label':field('Label'),'ordered':field('order.ordered'),'number':field('order.number'),'parent':parent.group(1),'source':str(p)}
def scope_path(sid,seen=()):
 if sid in seen or sid not in scope_defs:return None
 row=scope_defs[sid]
 if 'path' in row:return row['path']
 parents=scope_names.get(row['parent'],set())
 if len(parents)!=1:return None
 parent=scope_path(next(iter(parents)),seen+(sid,))
 if parent is None or row['ordered'] not in ('true','false'):return None
 parts=[sid]
 if row['label']:parts.append(row['label'])
 if row['ordered']=='true':
  if not row['number']:return None
  parts.append(row['number'])
 parts.append(row['name']);return parent/'_'.join(parts)
physical_scopes={sid:scope_path(sid) for sid in scope_defs};physical_scopes={sid:p for sid,p in physical_scopes.items() if p is not None}
inventory_paths={x['path'] for x in inventory}
def owner_from_evidence(path,obj):
 value=obj.get('current_scope_unit')
 if not isinstance(value,str):return None,'legacy_owner_missing',None
 candidates={value} if value in scope_ids else scope_names.get(value,set())
 if len(candidates)!=1:return None,'legacy_owner_not_unique',None
 sid=next(iter(candidates));matches=[(len(sp.parts),q) for q,sp in physical_scopes.items() if path.is_relative_to(sp)]
 if not matches:return None,'no_declared_physical_scope_ancestor',None
 depth=max(x[0] for x in matches);deep=[q for d,q in matches if d==depth]
 if len(deep)!=1 or deep[0]!=sid:return None,'legacy_owner_physical_scope_mismatch',None
 proof={'legacy_owner':value,'resolved_scope_id':sid,'scope_declaration':scope_defs[sid]['source'],'scope_declaration_sha256':sha(Path(scope_defs[sid]['source']).read_bytes()),'declared_scope_folder':str(physical_scopes[sid])}
 for directory in path.parents:
  if directory==physical_scopes[sid]:break
  found=re.match(r'^(?:[0-9]+-)?(CA-P-[0-9]+)(?:-|--)',directory.name)
  if not found:continue
  parent_file=directory.parent/(directory.name+'.md')
  if str(parent_file) not in inventory_paths or not parent_file.is_file() or parent_file.is_symlink():return None,'physical_plan_parent_carrier_missing',proof
  try:
   data=parent_file.read_bytes();pm=yaml.safe_load(data.decode().split('---',2)[1]);assert isinstance(pm,dict)
   if pm.get('atom_id')!=found.group(1) or pm.get('role',pm.get('content_role'))!='Plan' or pm.get('status') in ('Draft','Archived'):raise ValueError()
   if pm.get('current_scope_unit') not in (None,value,sid):raise ValueError()
  except Exception:return None,'physical_plan_parent_identity_unresolved',proof
  if all_ids[found.group(1)]!=1:return None,'physical_plan_parent_nonunique',proof
  proof.update({'plan_parent':found.group(1),'plan_carrier':str(parent_file),'plan_carrier_sha256':sha(data),'plan_bundle':str(directory)})
  return {'atom':found.group(1)},None,proof
 return {'scope_unit':sid},None,proof

all_ids=collections.Counter(r.get('atom_id') for r in inventory if r.get('status') not in ('Draft','Archived') and '/draft/' not in r['path'])
def parse(p):
 raw=p.read_bytes();text=raw.decode('utf-8');assert text.startswith('---\n');end=text.find('\n---\n',4);assert end>=0;fm=text[4:end];obj=yaml.safe_load(fm);node=yaml.compose(fm);assert isinstance(obj,dict) and isinstance(node,MappingNode);return raw,text,fm,end,obj,node
def pair(node,key):return [(k,v) for k,v in node.value if isinstance(k,ScalarNode) and k.value==key]
def normalize(field,value):
 if field=='atom':
  if not isinstance(value,str) or not re.fullmatch(r'CA-[CAPRMEDO]-\d+',value):return None,'invalid_parent_atom_id'
  if all_ids[value]!=1:return None,'parent_atom_missing_or_nonunique'
  return {'atom':value},None
 if field!='scope_unit' or not isinstance(value,str):return None,'invalid_containment_shape'
 if value in scope_ids:return {'scope_unit':value},None
 if len(scope_names[value])==1:return {'scope_unit':next(iter(scope_names[value]))},None
 return None,'scope_identity_missing_or_nonunique'
rows=[];ops=[];counts=collections.Counter()
for item in inventory:
 p=Path(item['path']);row={'path':str(p),'foreign_owner':bool(item.get('foreign_owner')),'snapshot_sha256':item['before_sha256']};rows.append(row)
 try:raw,text,fm,end,obj,node=parse(p)
 except Exception as e:row['result']='hold';row['reason']='unreadable_or_malformed_frontmatter';counts[row['reason']]+=1;continue
 row['before_sha256']=sha(raw);row['snapshot_matches']=row['before_sha256']==item['before_sha256'];row['atom_id']=obj.get('atom_id');rel=obj.get('relations'); candidates=[]
 if isinstance(rel,dict):
  for k,v in rel.items():
   if k.lower() not in ('is_contained_by','contained_by'):continue
   if isinstance(v,dict) and len(v)==1:
    field,value=next(iter(v.items()));candidates.append((k,field,value))
   elif isinstance(v,list) and len(v)==1 and isinstance(v[0],str):candidates.append((k,'atom',v[0]))
   else:candidates.append((k,None,None))
 existing=obj.get('container')
 if row['atom_id']=='CA-R-2640':
  if not candidates and existing=={'scope_unit':'CA-SU--1'}: row.update(result='already_correct',proposed_container=existing);counts['already_correct']+=1;continue
  if candidates or existing is not None: row.update(result='hold',reason='root_already_has_explicit_containment_review');counts[row['reason']]+=1;continue
  target={'scope_unit':'CA-SU--1'};key=None
 elif len(candidates)==1:
  key,field,value=candidates[0];target,error=normalize(field,value)
  if error:row.update(result='hold',reason=error,observed_containment=candidates[0]);counts[error]+=1;continue
 elif len(candidates)>1:row.update(result='hold',reason='multiple_containment_bindings');counts[row['reason']]+=1;continue
 else:
  target,error,proof=owner_from_evidence(p,obj);key=None
  if error:row.update(result='hold',reason=error,legacy_scope=obj.get('current_scope_unit'),proof=proof);counts[error]+=1;continue
  row['ownership_proof']=proof
 if existing is not None and existing!=target:row.update(result='hold',reason='existing_container_conflicts',proposed=target);counts[row['reason']]+=1;continue
 edits=[]
 if key is not None:
  rp=pair(node,'relations');
  if len(rp)!=1 or not isinstance(rp[0][1],MappingNode):row.update(result='hold',reason='relations_node_not_block_mapping');counts[row['reason']]+=1;continue
  rk,rv=rp[0];found=pair(rv,key)
  if len(found)!=1 or rk.start_mark.line==found[0][0].start_mark.line:row.update(result='hold',reason='inline_or_duplicate_relation_key');counts[row['reason']]+=1;continue
  lines=fm.splitlines(keepends=True);k,v=found[0];start=sum(len(x) for x in lines[:k.start_mark.line]);later=[other.start_mark.line for other,_ in rv.value if other.start_mark.line>k.start_mark.line];last=min(later) if later else v.end_mark.line+(1 if v.end_mark.column else 0);stop=sum(len(x) for x in lines[:last]);
  if len(rv.value)==1:
   start=sum(len(x) for x in lines[:rk.start_mark.line]);stop=sum(len(x) for x in lines[:max(last,rk.start_mark.line+1)]);edits.append((start,stop,'relations: {}\n'))
  else:edits.append((start,stop,''))
 if existing is None:edits.append((len(fm),len(fm),'\ncontainer:\n  '+next(iter(target))+': '+next(iter(target.values()))))
 new=fm
 for a,z,v in sorted(edits,reverse=True):new=new[:a]+v+new[z:]
 try:
  result=yaml.safe_load(new);expected=copy.deepcopy(obj)
  if key is not None:del expected['relations'][key]
  expected['container']=target
  assert result==expected
 except Exception:row.update(result='hold',reason='roundtrip_preservation_check_failed');counts[row['reason']]+=1;continue
 after=(text[:4]+new+text[end:]).encode();row.update(result='candidate',proposed_container=target,removed_relation_key=key,after_sha256=sha(after));ops.append({'path':str(p),'foreign_owner':row['foreign_owner'],'atom_id':row['atom_id'],'before_sha256':sha(raw),'after_sha256':sha(after),'before':text,'after':after.decode(),'container':target,'source':'root world explicit decision' if row['atom_id']=='CA-R-2640' else ('declared scope and physical Plan bundle proof' if key is None else 'existing direct containment fact'),'ownership_proof':row.get('ownership_proof')});counts['candidate']+=1
out={'status':'PINNED_PREVIEW_ONLY_NO_APPLY','input_census':str(plan),'input_census_sha256':sha(plan.read_bytes()),'scope_inventory':str(scope_file),'scope_inventory_sha256':sha(scope_file.read_bytes()),'scope_ids_resolved':len(scope_ids),'scope_source_pins':scope_pins,'counts':dict(counts),'rows':rows,'operations':ops,'limits':['No source writes. Recheck every live preimage and resolve stage-1 topics overlaps sequentially before any apply.','Legacy current_scope_unit is used only with a unique pinned declaration and matching deepest physical scope ancestor; nested Plan bundles additionally require a unique matching native Plan Carrier.','Root CA-R-2640 -> predefined world is a prospective accepted decision; root ID CA-SU-00 reflects accepted pending source Draft, not Current adoption.','Name-to-ID mapping only when exactly one live pinned Scope Unit declaration resolves it; invalid or ambiguous references held.','Physical ancestry is used only with the selected user-approved D264 Scope/Plan bundle proof; no child_of fallback or automatic foreign owner execution.']};(O/'container-plan.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'counts':dict(counts),'ops':len(ops),'scope_ids':len(scope_ids)},indent=2))
