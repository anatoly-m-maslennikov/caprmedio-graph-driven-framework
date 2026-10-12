"""Create bounded subset inputs without semantic choices."""
import argparse,pathlib,json,hashlib
ROOT=pathlib.Path.cwd();D=ROOT/".caprmedio_caprmedio/_projection/core-entity-review/nodes"
SPECS=[{"id":1939,"batch":3,"indexes":[0,1,2,3,4,5,6,7,8,9,10,11,12]},{"id":1940,"batch":3,"indexes":[13,14,15,16,17,18,19,20,21,22,23,24]},{"id":1941,"batch":3,"indexes":[25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42]},{"id":1942,"batch":3,"indexes":[43,44,45,46,47,48,49,50,51,52,53,54,55,56,57]},{"id":1943,"batch":3,"indexes":[58,59,60,61,62,63,64,65,66,67,68,69]},{"id":1944,"batch":3,"indexes":[70,71,72,73,74,75,76,77,78,79]},{"id":1945,"batch":7,"indexes":[0,1,2,3,4,5,6,7,8,9,10,11]},{"id":1946,"batch":7,"indexes":[12,13,14,15,16,17,18,19,20,21,22,23]},{"id":1947,"batch":7,"indexes":[24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]},{"id":1948,"batch":7,"indexes":[40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]},{"id":1949,"batch":7,"indexes":[60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79]}]
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--persist",action="store_true");a=ap.parse_args()
 outs={};report=[]
 for s in SPECS:
  p=D/f"inputs/nodes.batch-{s['batch']}.input.json";raw=p.read_bytes();parent=json.loads(raw)
  x={k:v for k,v in parent.items() if k not in ("nodes","partition_sha256","source_task","identity_count")}
  x.update(source_task="CA-P-"+str(s["id"]),parent_source_task=parent["source_task"],identity_count=len(s["indexes"]),nodes=[parent["nodes"][i] for i in s["indexes"]],parent_input={"path":str(p.relative_to(ROOT)),"sha256":sha(raw),"partition_sha256":parent["partition_sha256"]},subset_indexes=s["indexes"],scope_omission_pin={"path":str((D/"scope.omission.decision.md").relative_to(ROOT)),"sha256":sha((D/"scope.omission.decision.md").read_bytes())})
  x["partition_sha256"]=sha(canon(x));payload=canon(x)+b"\n";out=D/f"inputs/slices/CA-P-{s['id']}.input.json";outs[out]=payload
  report.append({"task":x["source_task"],"batch":s["batch"],"identities":len(x["nodes"]),"path":str(out.relative_to(ROOT)),"sha256":sha(payload),"partition_sha256":x["partition_sha256"]})
 for batch in (3,7):
  parts=[s for s in SPECS if s["batch"]==batch];ids=[i for s in parts for i in s["indexes"]];assert sorted(ids)==list(range(80)) and len(set(ids))==80
 if a.persist:
  for p,raw in outs.items():
   assert p.resolve().is_relative_to(ROOT) and not p.is_symlink()
   if p.exists():assert p.read_bytes()==raw,("refuse-overwrite",p)
  for p,raw in outs.items():
   p.parent.mkdir(parents=True,exist_ok=True)
   if not p.exists():
    with p.open("xb") as h:h.write(raw)
 print(json.dumps({"outcome":"persisted" if a.persist else "dry_run","slices":report},sort_keys=True))
if __name__=="__main__":main()
