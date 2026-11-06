#!/usr/bin/env python3
"""Read-only Header-group reference impact census; no source rewrite."""
import hashlib,json,re
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5]; C=ROOT/'.caprmedio_caprmedio'; OUT=Path(__file__).with_name('impact.json'); SNAP=C/'02_analysis/draft/header-groups-20261106/native-snapshot.json'
MAP={'ID':'Identity.ID','Ref ID':'Identity.RefID','RefID':'Identity.RefID','Container':'Context.Container','Role':'Context.Role','Form':'Context.Form','Label':'Context.Label','Topics':'Context.Topics','Tier':'Context.Tier','Status':'State.Status','Version':'State.Version','Updated At':'State.UpdatedAt','UpdatedAt':'State.UpdatedAt','Carrier Destination':'Destination','CarrierDestination':'Destination'}
EX={'archive','archived','journal','journals','_projection','projections','snapshot','snapshots','coverage','generated','history','000_caprmedio_framework','02_analysis','application','previews','prepared','prospective','evidence'}
FENCE=re.compile(r'(?ms)^```.*?^```[ \t]*$')
def h(s):return hashlib.sha256(s.encode()).hexdigest()
def eligible(p,t):
 rel=p.relative_to(C); low='/'.join(x.lower() for x in rel.parts)
 if any(x in low for x in EX) or not t.startswith('---\n'):return False
 e=t.find('\n---\n',4); f=t[4:e] if e>0 else ''
 return bool(re.search(r'(?mi)^status:\s*(?!Archived\b)\S+',f) and re.search(r'(?mi)^atom_id:\s*CA-[A-Z]-',f))
rows=[]; counts=Counter(); amb=[]
pat=re.compile(r'(?<![\w.])(?:(Atom|\$[A-Za-z_][\w-]*)\.)Header\.('+'|'.join(MAP)+r')\b')
for carrier in json.loads(SNAP.read_text())['carriers']:
 rel=carrier['path']; p=ROOT/rel; t=p.read_text(); counts['carriers']+=1
 for m in pat.finditer(t):
  # generic participant is only safe when its name denotes declared Atom/Carrier context.
  head=m.group(1); field=m.group(2)
  bound=bool(re.search(re.escape(head)+r'\s*\[\s*<Atom>\b',t) or re.search(r'Atom//'+re.escape(head.lstrip('$'))+r'\b',t)) if head!='Atom' else True
  if not bound:
   amb.append({'path':rel,'offset':m.start(),'token':m.group(0),'reason':'participant_kind_unproven'});continue
  rows.append({'path':rel,'before_sha256':h(t),'token':m.group(0),'replacement':head+'.Header.'+MAP[field],'field':field,'in_fence':bool(any(x.start()<=m.start()<x.end() for x in FENCE.finditer(t)))})
  counts[field]+=1
OUT.write_text(json.dumps({'status':'READ_ONLY_PREPARATION','mapping':MAP,'native_current_draft_carriers':counts.pop('carriers',0),'unambiguous_references':rows,'counts':dict(counts),'ambiguous':amb,'tools_considered':['YAML compose/node marks for headers','fence-aware claim migration sections/migrate_claim'],'non_claims':['No source rewrite','Generic Entity.ID/Status and unproven participant headers held']},indent=2)+'\n')
print(json.dumps({'references':len(rows),'ambiguous':len(amb)}))
