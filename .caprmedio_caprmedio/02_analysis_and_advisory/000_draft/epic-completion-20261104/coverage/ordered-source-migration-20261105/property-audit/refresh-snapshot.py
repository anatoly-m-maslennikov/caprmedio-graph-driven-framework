from pathlib import Path
import yaml,json,re,hashlib,collections
root=Path('.caprmedio_caprmedio');base=root/'02_analysis/draft/epic-completion-20261104/coverage/ordered-source-migration-20261105/property-audit';base.mkdir(parents=True,exist_ok=True)
rolepat=re.compile(r'\d\d_(concern|analysis|plan|requirement|method|evaluation|delivery|implementation|operations|ops)$');fnpat=re.compile(r'CA-[A-Z]-(?:\d+(?:@(?:\d+-draft|draft))?|draft|)-');exclusions={'archive','archived','_journal','_projection','000_CAPRMEDIO_framework','goals_archive'}
roleforms={'Operator Declaration','Construct Declaration','Relation Declaration','Function Declaration'}
rows=[];types=collections.Counter();counts=collections.Counter();parse=[]
legacy_evidence=root/'02_analysis/draft/epic-completion-20261104/coverage/ordered-source-migration-20261105/verification/legacy-scope-directories.json'
legacy_paths={record['path'] for group in json.loads(legacy_evidence.read_text())['group_roots'] for record in group['records']}
for p in sorted(root.rglob('*.md')):
 if p.is_symlink() or not p.is_file():continue
 if any(x in exclusions or x.startswith('TEST-SU-') for x in p.parts):continue
 rel=p.relative_to(root); parts=rel.parts; roleidx=next((i for i,z in enumerate(parts[:-1]) if rolepat.fullmatch(z)),None)
 if roleidx is None:
  if p.parent!=root or not re.match(r'CA-R-\d+-',p.name):continue
  isdraft=False
 else:
  if any(not re.fullmatch(r'CA-SU-\d+_.+',z) for z in parts[:roleidx]) and str(p) not in legacy_paths:continue
  role_dir=parts[roleidx]; tail=parts[roleidx+1:-1]
  expected={'01_concern':'C','02_analysis':'A','03_plan':'P','04_requirement':'R','05_method':'M','06_evaluation':'E','07_delivery':'D','09_operations':'O','09_ops':'O'}
  if role_dir not in expected:continue
  code=expected[role_dir];statuses={'draft','backlog','done','canceled','cancelled','active'}
  if not all(z.lower() in statuses or re.match(r'(?:\d+-)?CA-'+code+r'-\d+[-@]',z) for z in tail):continue
  if not re.match(r'(?:\d+-)?CA-'+code+r'-(?:\d+|draft)(?:[-@.]|$)',p.name):
   if not (tail==('draft',) and p.name.startswith('CA-'+code+'--')):continue
  isdraft=any(z.lower()=='draft' for z in tail)
 data=p.read_bytes();t=data.decode('utf-8');item={'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'class':'Draft' if isdraft else 'Current','checks':{},'legacy_fields':[]}
 if not re.match(r'(?:\d+-)?CA-[A-Z]-\d+(?:@\d+-draft)?-',p.name):item['identity_review']='legacy or unnumbered filename; check identity/version separately'
 try:
  if not t.startswith('---\n'): raise ValueError('missing frontmatter')
  a=yaml.safe_load(t.split('---',2)[1]);assert isinstance(a,dict)
 except Exception as e:
  item['checks']['frontmatter']={'result':'inconsistent','evidence':str(e),'disposition':'manual repair'};rows.append(item);continue
 if str(a.get('status')).lower()=='archived':continue
 item['id']=a.get('atom_id');item['status']=a.get('status');c=item['checks']
 def setcheck(k,res,detail='',disposition=None):
  c[k]={'result':res,'detail':detail};
  if disposition:c[k]['disposition']=disposition
 topics=a.get('topics')
 if topics is None:
  old=a.get('subjects');setcheck('topics.main_subject','missing','legacy subjects present' if old is not None else 'no legacy subjects','review mapping; do not blindly rename active')
  setcheck('topics.dependencies','missing_optional','0+ allows omission')
 elif not isinstance(topics,dict):
  setcheck('topics.main_subject','inconsistent','topics is not a mapping','manual repair');setcheck('topics.dependencies','declared_unknown','topics malformed')
 else:
  main=topics.get('main_subject');setcheck('topics.main_subject','ok' if isinstance(main,str) and main.strip() else 'missing' if main is None else 'inconsistent','requires one nonempty string','semantic subject selection' if not isinstance(main,str) or not main.strip() else None)
  deps=topics.get('dependencies');setcheck('topics.dependencies','missing_optional' if deps is None else 'ok' if isinstance(deps,list) and all(isinstance(x,str) and x.strip() for x in deps) else 'inconsistent','zero or more strings','review values' if deps is not None and not (isinstance(deps,list) and all(isinstance(x,str) and x.strip() for x in deps)) else None)
 for k in ('role','form'):
  v=a.get(k);setcheck(k,'ok' if isinstance(v,str) and v.strip() else 'missing' if v is None else 'inconsistent','requires one nonempty string','determine from declared role and form authority; avoid name-only inference' if not isinstance(v,str) or not v.strip() else None)
 role=a.get('role');form=a.get('form');setcheck('role_form_admission','ok_staged' if role=='Requirement' and form in roleforms else 'inconsistent' if form in roleforms and role!='Requirement' else 'declared_unknown','four new Requirement Forms are staged; other pair admission not established by this bounded check')
 co=a.get('container'); contid=a.get('atom_id');isroot=contid=='CA-R-2640'
 if co is None:
  rel=a.get('relations');legacy=rel.get('IS_CONTAINED_BY') if isinstance(rel,dict) else None
  setcheck('container','effective_default' if isroot else 'missing','predefined world default for root' if isroot else ('legacy relation value exists' if legacy is not None else 'no stored Container'),'verify approved direct conversion' if legacy is not None else 'identify actual container')
 elif not isinstance(co,dict):setcheck('container','inconsistent','container is not a mapping','inspect value')
 else:
  keys=set(co);vals=[(k,v) for k,v in co.items() if k in ('atom','scope_unit') and isinstance(v,str) and v.strip()];setcheck('container','ok' if len(vals)==1 and len(keys)==1 else 'inconsistent','requires exactly one atom or scope_unit key with nonempty identifier','review identity and target resolution' if not(len(vals)==1 and len(keys)==1) else None)
 cd=a.get('carrier_destination');f=cd.get('file') if isinstance(cd,dict) else None
 for k in ('name','path'):
  v=f.get(k) if isinstance(f,dict) else None
  if v is None:setcheck('carrier_destination.file.'+k,'missing','requires one string','derive only from approved target plan')
  elif not isinstance(v,str) or not v.strip():setcheck('carrier_destination.file.'+k,'inconsistent','requires one nonempty string','review target plan')
  elif k=='name' and ('/' in v or '\\' in v):setcheck('carrier_destination.file.name','inconsistent','filename cannot contain a path','split using approved target plan')
  elif k=='path' and Path(v).is_absolute():setcheck('carrier_destination.file.path','inconsistent','path must be repository-relative directory','review target plan')
  elif k=='path' and Path(v).exists() and not Path(v).is_dir():setcheck('carrier_destination.file.path','inconsistent','existing target is not a directory','review target plan')
  else:setcheck('carrier_destination.file.'+k,'ok','string; target existence and admission not validated')
 ref=a.get('ref_id');setcheck('ref_id','missing' if ref is None else 'ok' if isinstance(ref,str) and ref.strip() else 'inconsistent','Current R2966 requires one nonempty string; value-to-identity check is separate','derive only after identity/status/version validation' if not isinstance(ref,str) or not ref.strip() else None)
 item['physical_header_key_order']=list(a.keys())
 legacy_subjects=a.get('subjects')
 if topics is not None and legacy_subjects is not None:
  setcheck('topics_legacy_subjects','declared_unknown','both Topics and legacy Subjects are present; identity and dependency correspondence require evidence','review before retiring legacy fields')
 legacy_rel=a.get('relations');old_container=legacy_rel.get('IS_CONTAINED_BY') if isinstance(legacy_rel,dict) else None
 if co is not None and old_container is not None:
  setcheck('container_duplicate_storage','inconsistent','Container and legacy Relations.IS_CONTAINED_BY are both present','compare identities and remove duplication only after approved migration')
 for k in ('subjects','current_scope_unit','claim_target_scope_unit','relations'):
  if k in a:item['legacy_fields'].append(k)
 for k,v in c.items():counts[k+':'+v['result']]+=1
 types[item['class']]+=1;rows.append(item)
core=root/'CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement';pins=[]
for i in ('2702','2703','2708','2713','2714','2715','2716','2717','2718','2965','2966','2967'):
 p=next(core.glob('CA-R-'+i+'-*'));pins.append({'id':'CA-R-'+i,'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'Current old Subject vocabulary' if i in ('2708','2713','2714') else 'Current'})
for i in ('2779','2783','2784','2953','2954','2955','2956'):
 ps=list((core/'draft').glob('CA-R-'+i+'@*-*'))
 if ps:
  p=ps[-1];pins.append({'id':'CA-R-'+i,'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'Draft'})
obj={'status':'PRE_MIGRATION_SNAPSHOT_REFRESH_AFTER_STAGE_1','scope':'Planner native_role source boundary: role directories under CA-SU prefixes, status and matching role-ID bundle descendants, including prefixed filenames; additionally include two root Atoms, four direct unnumbered double-hyphen Drafts, and 21 live GIT/FPF carriers supported by the pinned group-root report; their physical placement remains held. Includes legacy names flagged for identity review. Excludes archive, archived, 000_CAPRMEDIO_framework, tests, journal, projections, and analysis packet descendants. Physical frontmatter keys represent logical Atom.Header properties. Counts include canonical concern lifecycle statuses; Draft denotes directory, not inferred status. Filename/role matching is a structural classifier, not full semantic or identity validation. Not a claim of exhaustive project instance inventory.','source_authorities':pins,'decisions_not_yet_declared':'Topics main_subject one and dependencies zero or more per latest user decision; source declaration IDs not yet identified in this snapshot. Do not claim Current authority has changed. Four Requirement Forms and Header.Container are staged Drafts.','counts':{'carriers':len(rows),'classes':dict(types),'checks':dict(sorted(counts.items()))},'carriers':rows,'limits':['Snapshot taken before stage 1; paths, hashes, counts and checks must be refreshed after in-place migration.','Does not validate full Relation semantics, Subject resolution, role/Form registry membership beyond the four staged forms, exact ID grammar, graph targets, target existence or all other mandatory Properties.','A missing Topics field is a future schema finding, not proof Current violates its existing Subjects declaration. No general subjects.active-to-main_subject or passive-to-dependencies mapping is assumed.','A missing Container may be mechanically convertible only after one valid legacy relation and ownership target are verified; root default is an explicit exception.','A destination path is a directory, not a filename; an absent directory is not automatically invalid. Existing filenames or locations do not alone establish the approved destination.']};(base/'snapshot.json').write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n');(base/'REPORT.md').write_text('# Atom property readiness snapshot\n\nSource-only snapshot; refresh after stage 1: '+str(len(rows))+' numbered native carriers ('+', '.join(k+' '+str(v) for k,v in types.items())+'). Refresh after stage 1.\n\nThe JSON records each source hash and per-field status for Topics, Role/Form, Container, and Carrier Destination. Topics checks reflect the latest decision and are not yet a claim about Current declarations. Optional dependencies may be absent. Existing Subject fields are retained as evidence, with no automatic rename assumed.\n\nCurrent Carrier Destination Declarations require Name and Path; Path is a repository-relative containing directory. Container and four additional Requirement Forms are staged. The root Project Declaration has a predefined world default. The snapshot checks value shape, not identity resolution, complete Form admission or runtime conformance. See JSON for exclusions and other limits.\n');print(json.dumps(obj['counts'],indent=2))
