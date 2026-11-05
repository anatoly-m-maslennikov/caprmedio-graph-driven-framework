import json,re,hashlib,subprocess,yaml
from pathlib import Path
root=Path.cwd(); out=root/'.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/application/ref-id-repair-20261105/identity'; plan=root/'.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/application/property-order-20261105/ref-id-data/adoption-plan.json'; d=json.loads(plan.read_text()); holds=[x for x in d['holds'] if x['reason']=='unallocated or invalid Atom ID' or (x['reason']=='missing explicit Atom ID or Status' and '/draft/CA-' in x['path'])];sha=lambda b:hashlib.sha256(b).hexdigest()
def parse(p):
 try:
  s=p.read_text(); pieces=s.split('---',2);m=yaml.safe_load(pieces[1]);m=m if isinstance(m,dict) else {}; summary=re.search(r'(?ims)^#{1,2}\s+Summary\s*\n(.*?)(?=^#{1,2}\s|\Z)',pieces[2]);return m,summary.group(1).strip().replace('\n',' ') if summary else None,s
 except Exception:return {},None,''
paths=subprocess.check_output(['rg','--files','.caprmedio_caprmedio','-g','*.md'],text=True).splitlines();idx={};forms={}
for x in paths:
 p=root/x;parts=p.parts
 if any(v in parts for v in ('draft','_projection','000_CAPRMEDIO_framework','02_analysis','_journal')):continue
 if not re.match(r'CA-[ACPRMEDO]-\d+',p.name):continue
 m,s,body=parse(p)
 if not s:continue
 historic=any(v in parts for v in ('archive','archived')) or m.get('status')=='Archived';entry={'path':x,'id':m.get('atom_id'),'version':m.get('version'),'status':m.get('status'),'subject':(m.get('topics') or {}).get('main_subject') if isinstance(m.get('topics'),dict) else None,'sha256':sha(p.read_bytes())};idx.setdefault(s.casefold(),[]).append((historic,entry))
 if not historic and m.get('status') not in ('Draft','Archived'):forms.setdefault((str(m.get('role')),str(m.get('form'))),0);forms[(str(m.get('role')),str(m.get('form')))]+=1
rows=[]
for item in holds:
 p=root/item['path'];m,s,body=parse(p);match=idx.get((s or '').casefold(),[]);refs=[]
 for line in body.splitlines():
  if re.search(r'(?:Current|predecessor|successor|existing|replac|source|CA-[ACPRMEDO]-\d+)',line,re.I) and re.search(r'CA-[ACPRMEDO]-\d+',line):refs.append(line.strip()[:500])
 letter=re.match(r'CA-([ACPRMEDO])-',p.name).group(1);role=m.get('role');form=m.get('form');expected={'A':'Analysis','R':'Requirement','M':'Method','E':'Evaluation','D':'Delivery'}[letter];version=m.get('version');
 current=[x for hist,x in match if not hist];history=[x for hist,x in match if hist]; subject=(m.get('topics') or {}).get('main_subject') if isinstance(m.get('topics'),dict) else None
 # A repeated Summary, older multi-version content, or predecessor references need adjudication; identity never inferred from Summary alone.
 action='HOLD_IDENTITY_REVIEW' if current or history or refs or version!=1 else 'PROPOSE_NEW_ID_V1_AFTER_PROVENANCE_REVIEW'
 rows.append({'path':item['path'],'sha256':sha(p.read_bytes()),'atom_id':m.get('atom_id'),'status':m.get('status'),'role':role,'form':form,'role_letter':letter,'role_letter_matches':role==expected,'form_seen_in_current_atoms':forms.get((str(role),str(form)),0),'form_validation':'not established by usage; verify applicable Form Declaration','version_existing':version,'proposed_version':1 if action.startswith('PROPOSE_NEW') else None,'summary':s,'main_subject':subject,'same_summary_current':current,'same_summary_history':history,'id_reference_lines':refs[:12],'action':action})
result={'source_plan':str(plan.relative_to(root)),'source_plan_sha256':sha(plan.read_bytes()),'count':len(rows),'policy':{'new_draft_ids_allocated_at_creation':['CA-D-378','CA-D-650'],'existing_revision':'CA-D-446; current version + 1 with explicitly pinned target','note':'Current candidate status and validation are separate from identity; observed Form usage is not admission proof.'},'rows':rows};(out/'identity-review.json').write_text(json.dumps(result,indent=2)+'\n');print('rows',len(rows),'current matches',sum(bool(x['same_summary_current']) for x in rows),'history',sum(bool(x['same_summary_history']) for x in rows),'refs',sum(bool(x['id_reference_lines']) for x in rows));
for x in rows:print(Path(x['path']).name,'|',x['action'],'|',','.join(str(y['id']) for y in x['same_summary_current']),'|',x['version_existing'],'|',x['role'],x['form'])
