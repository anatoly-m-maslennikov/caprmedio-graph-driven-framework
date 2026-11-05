from pathlib import Path
import collections,hashlib,json,re,yaml,unicodedata
B=Path('.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/coverage/ordered-source-migration-20261105'); O=B/'destinations'; ROOT=Path('.caprmedio_caprmedio');sha=lambda b:hashlib.sha256(b).hexdigest()
snapshot=B/'metadata/adoption-plan.json'; inventory=B.parent.parent/'scope-declaration-check-20261105/inventory.json'
if not inventory.exists(): inventory=Path('.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/coverage/scope-declaration-check-20261105/inventory.json')
census=json.loads(snapshot.read_text()); source={'carriers':[{'path':x['path'],'sha256':x['before_sha256'],'class':'Draft' if '/draft/' in x['path'] else 'Current','foreign_owner':x.get('foreign_owner',False)} for x in census['inventory']]}; conversion=json.loads((O/'container-plan.json').read_text()); overlays={x['path']:x for x in conversion['operations']}; scope_data=json.loads(inventory.read_text());
roles={'Concern':'01_concern','Analysis':'02_analysis','Analysis & Advisory':'02_analysis','Plan':'03_plan','Requirement':'04_requirement','Method':'05_method','Evaluation':'06_evaluation','Delivery':'07_delivery','Operations':'09_operations'}
scopes={}; scope_pins=[]
for pin in conversion['scope_source_pins']:
 p=Path(pin['path']);raw=p.read_bytes();scope_pins.append({'path':str(p),'sha256':sha(raw),'matches_inventory':True,'before_container_sha256':pin['sha256']});body=raw.decode()
 if p.name.startswith('CA-R-2640-'):
  scopes['caprmedio']={'id':'CA-SU-00','root':True,'path':str(ROOT)};continue
 def val(k):
  m=re.search(r'\.'+re.escape(k)+r'\s*==\s*(?:"([^"]+)"|(true|false|\d+))',body);return (m.group(1) or m.group(2)) if m else None
 name=val('Name');parent=re.search(r'\(\(IS_CONTAINED_BY\)\)\s*(?:Scope Unit|Project)//([A-Za-z0-9_]+)',body)
 if name:scopes[name]={'id':val('ID'),'name':name,'label':val('Label'),'ordered':val('order.ordered'),'order':val('order.number'),'parent':parent.group(1) if parent else None,'root':False}

byid=collections.defaultdict(list)
for k,v in scopes.items():
 if v.get('id'):byid[v['id']].append(k)
def scopepath(name,seen=()):
 if name in seen or name not in scopes:return None
 x=scopes[name]
 if x.get('root'):return ROOT
 if not all((x.get('id'),x.get('name'),x.get('parent'))) or x.get('ordered') not in ('true','false'):return None
 parent=scopepath(x['parent'],seen+(name,))
 if parent is None:return None
 fields=[x['id']];
 if x['label']:fields.append(x['label'])
 if x['ordered']=='true':
  if not x['order']:return None
  fields.append(x['order'])
 fields.append(x['name']);return parent/'_'.join(fields)
def carried_summary(body):
 lines=body.splitlines();heads=[];fence=None
 for i,line in enumerate(lines):
  marker=re.match(r'^ {0,3}(`{3,}|~{3,})',line)
  if marker:
   glyph=marker.group(1)
   if fence is None:fence=(glyph[0],len(glyph))
   elif glyph[0]==fence[0] and len(glyph)>=fence[1]:fence=None
   continue
  if fence is None:
   match=re.match(r'^ {0,3}(#{1,6})[ \t]+(.+?)\s*#*\s*$',line)
   if match:heads.append((i,match.group(2).strip()))
 matches=[(i,n) for i,n in heads if n.casefold()=='summary']
 if len(matches)!=1:return None
 start=matches[0][0];end=next((i for i,_ in heads if i>start),len(lines));value=' '.join(' '.join(lines[start+1:end]).split())
 return value or None
def ascii_words(x):
 if not isinstance(x,str) or not x:return None
 decomposed=unicodedata.normalize('NFKD',x);out=[]
 for c in decomposed:
  if unicodedata.combining(c):continue
  if ord(c)>127 and c.isalnum():return None
  out.append(c if ord(c)<128 and c.isalnum() else ' ')
 return ' '.join(''.join(out).split()) or None
def token(x):
 w=ascii_words(x);return w.replace(' ','_').upper() if w else None
def slug(x):
 w=ascii_words(x);return w.replace(' ','-').lower() if w else None

rows=[]
for entry in source['carriers']:
 p=Path(entry['path']); item={'source':str(p),'owner':'foreign_workbench' if 'WORKBENCH' in str(p).upper() else 'foreign_operations' if '/09_operations/' in str(p) or '/09_ops/' in str(p) else 'foreign_owner' if entry.get('foreign_owner') else 'root_or_other_owner_review','class':entry['class'],'source_sha256':None,'expected_name':None,'expected_path':None,'name_components':{},'issues':[]};rows.append(item)
 if not p.exists() or p.is_symlink():item['issues'].append('source_missing_or_symlink');continue
 raw=p.read_bytes();item['source_sha256']=sha(raw);item['snapshot_matches']=item['source_sha256']==entry['sha256']
 try:
  text=raw.decode(); overlay=overlays.get(str(p));
  if overlay:
   if overlay['after_sha256']==item['source_sha256']:
    item['container_applied_sha256']=overlay['after_sha256']
   elif overlay['before_sha256']==item['source_sha256']:
    text=overlay['after'];item['proposed_container_overlay_sha256']=overlay['after_sha256']
   else:raise ValueError('container preimage drift')
  parts=text.split('---',2);assert len(parts)==3 and parts[0]=='';meta=yaml.safe_load(parts[1]);assert isinstance(meta,dict)
 except Exception:item['issues'].append('frontmatter_unreadable');continue
 id=meta.get('atom_id');role=meta.get('role');form=meta.get('form');status=meta.get('status');version=meta.get('version');summary=carried_summary(parts[2])
 item.update({'atom_id':id,'role':role,'form':form,'status':status,'version':version});sl=slug(summary);label=token(meta.get('label') or form);item['name_components']={'summary':summary,'summary_slug':sl,'effective_label_token':label,'work_sequence_number':meta.get('work_sequence_number')}
 if not isinstance(id,str) or not re.fullmatch(r'CA-[CAPRMEDO]-\d+',id):item['issues'].append('base_atom_id_missing_or_noncanonical')
 if role not in roles:item['issues'].append('role_missing_or_unresolved')
 if not isinstance(form,str) or not form:item['issues'].append('form_missing_or_unresolved')
 if not sl:item['issues'].append('summary_slug_requires_source_backed_normalization')
 if not label:item['issues'].append('label_token_missing_or_requires_source_backed_normalization')
 seg=id
 if entry['class']=='Draft':
  if isinstance(id,str) and isinstance(version,int) and not isinstance(version,bool):seg=f'{id}@{version}-draft'
  else:item['issues'].append('draft_id_or_version_unresolved');seg=None
 if role=='Plan' and seg and sl and label:
  seq=meta.get('work_sequence_number');legacy=re.match(r'^(\d+)-CA-P-',p.name)
  if seq is None and legacy:item['issues'].append('legacy_filename_sequence_needs_property_migration');item['legacy_sequence_evidence']=legacy.group(1)
  elif seq is not None and (not isinstance(seq,int) or isinstance(seq,bool) or seq<1):item['issues'].append('invalid_work_sequence_number')
  else:item['expected_name']=(str(seq)+'-' if seq is not None else '')+seg+('-'+token(meta['label']) if meta.get('label') else '')+'--'+sl+'.md'
 elif role and role!='Plan' and seg and sl and label:
  tokens=[seg];current=meta.get('current_scope_unit');target=meta.get('claim_target_scope_unit');tier=meta.get('tier')
  if current:
   ct=token(current)
   if ct:tokens.append(ct)
   else:item['issues'].append('current_scope_token_unresolvable')
  if tier==0:tokens.append('SCOPE_CONTRACT')
  elif tier is not None and (not isinstance(tier,int) or isinstance(tier,bool)):item['issues'].append('invalid_tier')
  tokens.append(label)
  if target and target!=current:
   tt=token(target)
   if tt:tokens.append(tt);item['target_scope_evidence']='legacy claim_target_scope_unit: verify against active Subject before apply';item['issues'].append('legacy_target_scope_requires_subject_validation')
   else:item['issues'].append('target_scope_token_unresolvable')
  item['expected_name']='-'.join(tokens)+'--'+sl+'.md'
 cont=meta.get('container');
 if not isinstance(cont,dict) or set(cont) not in ({'scope_unit'},{'atom'}):
  item['issues'].append('header_container_missing_or_ambiguous');continue
 field=next(iter(cont));value=cont[field];item['container']={field:value}
 if field=='atom':item['issues'].append('atom_parent_bundle_requires_source_resolver');continue
 if value=='CA-SU--1':item['issues'].append('world_root_declaration_placement_requires_explicit_authority');continue
 if value=='CA-SU-00':
  if role in roles:
   dest=ROOT/roles[role]
   if entry['class']=='Draft':dest=dest/'draft'
   elif role=='Plan':
    st={'Active':'','Backlog':'001_backlog','Done':'done','Canceled':'canceled'}
    if status not in st:item['issues'].append('plan_status_placement_unresolved');continue
    if st[status]:dest=dest/st[status]
   elif status not in ('Active','Current'):item['issues'].append('role_status_placement_requires_authority');continue
   item['expected_path']=str(dest)
  continue
 matches=byid.get(value,[])
 if len(matches)!=1:item['issues'].append('scope_id_unresolved_or_ambiguous');continue
 base=scopepath(matches[0]);
 if base is None:item['issues'].append('scope_chain_unresolved');continue
 if not all(x['matches_inventory'] for x in scope_pins):item['issues'].append('scope_inventory_drift_repin_required');continue
 if role not in roles:continue
 dest=base/roles[role]
 if entry['class']=='Draft':dest=dest/'draft'
 elif role=='Plan':
  st={'Active':'','Backlog':'001_backlog','Done':'done','Canceled':'canceled'}
  if status not in st:item['issues'].append('plan_status_placement_unresolved');continue
  if st[status]:dest=dest/st[status]
 elif status not in ('Active','Current'):item['issues'].append('role_status_placement_requires_authority');continue
 item['expected_path']=str(dest)
# Resolve Plan parent folders only from a unique calculated Current parent, never its old path.
parent_index=collections.defaultdict(list)
for x in rows:
 if x.get('class')=='Current' and isinstance(x.get('atom_id'),str):parent_index[x['atom_id']].append(x)
for _ in range(20):
 changed=False
 for x in rows:
  if 'atom_parent_bundle_requires_source_resolver' not in x['issues'] or x.get('role')!='Plan':continue
  refs=parent_index.get(x.get('container',{}).get('atom'),[])
  if len(refs)!=1:continue
  parent=refs[0]
  if parent.get('role')!='Plan' or parent.get('issues') or not parent.get('expected_name') or not parent.get('expected_path'):continue
  if x['class']=='Draft' or x.get('status')=='Archived':continue
  statusfolders={'Active':'','Backlog':'001_backlog','Done':'done','Canceled':'canceled'};folder=statusfolders.get(x.get('status'))
  if folder is None:continue
  directory=Path(parent['expected_path'])/parent['expected_name'].removesuffix('.md')
  if folder:directory=directory/folder
  x['expected_path']=str(directory);x['parent_calculated_source']=parent['source'];x['issues'].remove('atom_parent_bundle_requires_source_resolver');changed=True
 if not changed:break
counts=collections.Counter(('calculated_no_local_issues' if not x['issues'] and x['expected_name'] and x['expected_path'] else 'held') for x in rows);issues=collections.Counter(i for x in rows for i in x['issues']);targets=collections.defaultdict(list)
for x in rows:
 if x['expected_path'] and x['expected_name']:targets[str(Path(x['expected_path'])/x['expected_name'])].append(x['source'])
collisions={k:v for k,v in targets.items() if len(v)>1};o={'status':'PROSPECTIVE_PRE_MIGRATION_PLAN_NOT_APPLY','snapshot':str(snapshot),'snapshot_sha256':sha(snapshot.read_bytes()),'container_plan':str(O/'container-plan.json'),'container_plan_sha256':sha((O/'container-plan.json').read_bytes()),'scope_inventory':str(inventory),'scope_inventory_sha256':sha(inventory.read_bytes()),'scope_source_pins':scope_pins,'counts':{'sources':len(rows),'readiness':dict(counts),'issues':dict(issues),'duplicate_calculated_targets':len(collisions)},'target_collisions':collisions,'rows':rows,'limits':['Calculated against live post-Topics, post-Role/Form and post-Container sources; recheck all current pins and remaining Source authority. This plan does not authorize writes or moves.','Optional-token policy derives scope, effective Label, tier 0 and differing target from Properties; legacy target values require Subject validation. Atom-container paths still require a parent-bundle resolver.','Current source pins are hash-only observations; foreign owner tagging does not authorize edits.','No native source or physical carrier changes made.']};(O/'plan.json').write_text(json.dumps(o,indent=2)+'\n');print(json.dumps(o['counts'],indent=2))
