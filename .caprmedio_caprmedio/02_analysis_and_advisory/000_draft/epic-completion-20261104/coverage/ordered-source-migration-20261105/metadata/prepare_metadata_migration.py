#!/usr/bin/env python3
"""Read-only preparation for ordered source metadata migration; never applies edits."""
import hashlib, json, re
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[7]
CONTROL=ROOT/'.caprmedio_caprmedio'
OUT=Path(__file__).with_name('planned-operations.json')
ROLE={'01_concern':'C','02_analysis':'A','03_plan':'P','04_requirement':'R','05_method':'M','06_evaluation':'E','07_delivery':'D','09_operations':'O'}
ROLE_NAME={'01_concern':'concern','02_analysis':'analysis','03_plan':'plan','04_requirement':'requirement','05_method':'method','06_evaluation':'evaluation','07_delivery':'delivery','09_operations':'operations'}
EXCLUDE={'archive','archived','journal','journals','_projection','projections','snapshot','snapshots','withdrawn'}

def sha(s): return hashlib.sha256(s.encode()).hexdigest()
def scalar(front,key):
 m=re.search(rf'(?mi)^{key}:\s*["\']?([^\n"\']+)',front); return m.group(1).strip() if m else None
def coherent(role,value):
 v=re.sub(r'[ _-]+','',(value or '').lower()); return v==ROLE_NAME[role] or role=='02_analysis' and v=='analysisadvisory'
def nearest(parts):
 return next((x for x in reversed(parts[:-1]) if x in ROLE),None)
def canonical(path,text):
 rel=path.relative_to(CONTROL); low='/'.join(x.lower() for x in rel.parts); role=nearest(rel.parts)
 if not role or any(x.lower() in EXCLUDE for x in rel.parts) or 'coverage/' in low or 'snapshot' in low: return None
 if any(x.startswith('CA-SU-43_') for x in rel.parts): return ('foreign_workbench',None)
 if not text.startswith('---\n') or '\n---\n' not in text[4:]: return None
 front=text[4:text.find('\n---\n',4)]; aid=scalar(front,'atom_id'); status=(scalar(front,'status') or '').lower()
 if not aid or not re.fullmatch(r'CA-([CAPRMEDO])-\d+(?:@\d+)?(?:-draft)?',aid,re.I): return None
 if aid.split('-')[1].upper()!=ROLE[role] or not path.name.startswith(aid) or not coherent(role,scalar(front,'role')) or status=='archived': return None
 return ('canonical',front)

ops=[]; ambiguous=[]; census=Counter(); pins=[]
for path in sorted(CONTROL.rglob('*.md')):
 text=path.read_text(encoding='utf-8'); result=canonical(path,text)
 if not result: continue
 kind,front=result; rel=str(path.relative_to(CONTROL)); census[kind]+=1
 if kind!='canonical': continue
 pins.append({'path':rel,'before_sha256':sha(text)})
 if re.search(r'(?m)^topics:\s*$',front):
  if re.search(r'(?m)^subjects:\s*$',front): ambiguous.append({'path':rel,'before_sha256':sha(text),'reason':'topics_and_subjects_conflict'}); continue
  continue
 m=re.search(r'(?ms)^subjects:\s*$\n(.*?)(?=^[A-Za-z_][A-Za-z0-9_]*:\s|\Z)',front)
 if not m: continue
 block=m.group(1)
 active=re.search(r'(?m)^  active:\s*(.+)$',block); passive=re.search(r'(?m)^  passive:\s*(.+)$',block)
 unknown=[x for x in re.findall(r'(?m)^  ([A-Za-z_][\w-]*):',block) if x not in {'active','passive'}]
 if unknown: ambiguous.append({'path':rel,'before_sha256':sha(text),'reason':'unsupported_subjects_key','keys':unknown}); continue
 if not active and not passive: ambiguous.append({'path':rel,'before_sha256':sha(text),'reason':'empty_subjects'}); continue
 replacement='topics:\n'
 if active: replacement+='  main_subject: '+active.group(1)+'\n'
 if passive: replacement+='  dependencies: '+passive.group(1)+'\n'
 ops.append({'path':rel,'before_sha256':sha(text),'operation':'subjects_to_topics','replace_exact':m.group(0),'replacement':replacement.rstrip('\n'),'foreign_owner':False,'cfel_action':'none'})
out={'artifact':'ordered source migration preparation','status':'PREPARED_NOT_APPLIED','scope':'canonical Current-group and Draft Atom carriers only; metadata keys only','census':dict(census),'source_pins':pins,'deterministic_operations':ops,'ambiguous_cases':ambiguous,'logical_model_path_map':{'Atom.Header.Subjects.Active':'Atom.Header.Topics.Main Subject','Atom.Header.Subjects.Passive':'Atom.Header.Topics.Dependencies'},'cfel':'No blind glyph replacement. CFEL changes require explicit context/domain review.','apply_gate':['recheck every before_sha256','fail if topics exists','write nonnative analysis backup before any apply','foreign Workbench/workflow owners remain separately tagged']}
OUT.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'census':dict(census),'operations':len(ops),'ambiguous':len(ambiguous),'output':str(OUT)}))
