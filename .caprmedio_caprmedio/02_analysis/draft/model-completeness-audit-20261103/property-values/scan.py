import json,re,hashlib,csv
from pathlib import Path
root=Path('.'); frontier=root/'.caprmedio_caprmedio/03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-header-content-20261103/integration/current-source-frontier.json'; out=Path(__file__).parent
rows=[]
for x in json.loads(frontier.read_text())['operations']:
 p=root/x['destination_path']; b=p.read_bytes(); t=b.decode(); m=re.search(r'^  active: ["\']?CAPRMEDIO_MODEL <\+ (.+?)["\']?$',t,re.M)
 if not m or not re.search(r'^form: Declaration$',t,re.M): continue
 path=m[1]; stripped=re.sub(r'\([^)]*\)','',path)
 if '.' not in stripped or path.startswith(('CFEL <+', 'Carrier <+')): continue
 address=path.replace(' := ', ': '); matches=[]
 for n,line in enumerate(t.splitlines(),1):
  if address in line: matches.append(f'{n}: {line.strip()}')
 direct=[s for s in matches if re.search(re.escape(address)+r'\s*\{:[^}]+\}\s*:\s*\[[^]]*\]\s*\{:[^}]+\}',s)]
 rows.append({'id':x['base_id'],'path':path,'source':str(p),'sha256':hashlib.sha256(b).hexdigest(),'frontier_drift':hashlib.sha256(b).hexdigest()!=x['sha256'],'matching_lines':' | '.join(matches),'direct_explicit':bool(direct),'effective_status':'unknown: inheritance, prose, qualified contexts and additional declarations require review'})
with (out/'inventory.json').open('w') as f: json.dump({'status':'partial conservative inventory; not an effective-contract audit','scope':'Current frontier Declaration active Property subjects; no wildcard expansion','rows':rows},f,indent=2); f.write('\n')
print('candidate subjects',len(rows),'direct syntax matches',sum(x['direct_explicit'] for x in rows),'drift',sum(x['frontier_drift'] for x in rows)); print('unmatched',[(x['id'],x['path']) for x in rows if not x['direct_explicit']])
