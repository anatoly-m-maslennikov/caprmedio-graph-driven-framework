#!/usr/bin/env python3
"""Read-only hash-pinned Role/Form migration preparation."""
import hashlib,json
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[7]; BASE=Path(__file__).resolve().parents[1]; PLAN=BASE/'metadata/adoption-plan.json'; OUT=Path(__file__).with_name('planned-operations.json')
def h(x): return hashlib.sha256(x.encode()).hexdigest()
def parts(x):
 e=x.find('\n---\n',4); assert x.startswith('---\n') and e>0; return x[4:e],x[e+5:]
def nodes(f):
 n=yaml.compose(f,Loader=yaml.SafeLoader); return {k.value:(k,v) for k,v in n.value}
def rename(f,k,new):
 node=nodes(f)[k][0]; a=node.start_mark.index; b=node.end_mark.index; return f[:a]+new+f[b:]
ops=[]; holds=[]
for row in json.loads(PLAN.read_text())['inventory']:
 p=ROOT/row['path']; raw=p.read_text(); f,b=parts(raw); d=nodes(f); after=f; expected=yaml.safe_load(f)
 for old,new in [('content_role','role'),('type','form')]:
  if old not in d: continue
  oval=yaml.safe_load(f[d[old][1].start_mark.index:d[old][1].end_mark.index])
  if new in d:
   nval=yaml.safe_load(f[d[new][1].start_mark.index:d[new][1].end_mark.index])
   if oval!=nval: holds.append({'path':row['path'],'reason':old+'_'+new+'_conflict','before_sha256':h(raw)}); break
   # delete exact key/value lines only when scalar key/value spans occupy one line
   line_start=f.rfind('\n',0,d[old][0].start_mark.index)+1; line_end=f.find('\n',d[old][1].end_mark.index)+1
   after=after[:line_start]+after[line_end:]; expected.pop(old,None)
  else:
   after=rename(after,old,new); expected[new]=expected.pop(old)
 else:
  whole='---\n'+after+'\n---\n'+b
  if whole!=raw:
   assert yaml.safe_load(after)==expected and b==parts(whole)[1]
   ops.append({'path':row['path'],'before_sha256':h(raw),'after_sha256':h(whole),'before_content':raw,'after_content':whole,'operation':'key_only_role_form','checks':['yaml_semantic_equality','body_byte_identity']})
OUT.write_text(json.dumps({'status':'PREPARED_NOT_APPLIED','inventory_count':len(json.loads(PLAN.read_text())['inventory']),'deterministic_operations':ops,'holds':holds,'distinct_legacy_cce_form':'reported_only_not_mapped','self_checks':['YAML node-span keys','full before/after hashes','parsed expected equality','body bytes identical']},indent=2)+'\n')
print(len(ops),len(holds))
