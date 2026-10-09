"""Mechanical evidence and coverage checks; never semantic adoption."""
import argparse,collections,hashlib,json,pathlib
ROOT=pathlib.Path.cwd();D=ROOT/".caprmedio_caprmedio/_projection/core-entity-review/nodes"
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()
CHECKS={"duplicates","redundancy","empty_definition","distinct_meaning","generalization"}
DISPOSITIONS={"retain","move","inherit","consolidate","generalize","drop_candidate","question"}
def verify(batch):
 p=D/f"inputs/nodes.batch-{batch}.input.json";inp=json.loads(p.read_bytes())
 assert sha(canon({k:v for k,v in inp.items() if k!="partition_sha256"}))==inp["partition_sha256"]
 bpath=ROOT/inp["baseline"]["path"];assert sha(bpath.read_bytes())==inp["baseline"]["sha256"]
 b=json.loads(bpath.read_bytes());pins={s["atom_id"]:s for s in b["source_atoms"]}
 out=D/f"nodes.batch-{batch}.review.json";raw=out.read_bytes();review=json.loads(raw)
 assert review["source_task"]==inp["source_task"] and review["batch"]==batch
 assert review["input_file_sha256"]==sha(p.read_bytes())
 assert review["partition_sha256"]==inp["partition_sha256"]
 assert review["baseline_inventory_sha256"]==inp["baseline"]["inventory_sha256"]
 assert review["non_authoritative"] is True
 assert review["semantic_admission"]==review["source_migration"]=="not_performed"
 expected={n["identity"] for n in inp["nodes"]};rows=review["nodes"]
 assert len(rows)==len(expected) and {r["identity"] for r in rows}==expected
 assert len({r["identity"] for r in rows})==len(rows)
 cache={}
 def source(aid):
  if aid not in cache:
   s=pins[aid];raw=(ROOT/s["carrier_path"]).read_bytes();assert sha(raw)==s["carrier_sha256"],aid
   cache[aid]=(s,raw.decode().splitlines())
  return cache[aid]
 catalogue=review["evidence_catalogue"]
 if isinstance(catalogue,list):
  assert all(isinstance(e,dict) and e.get("evidence_ref") for e in catalogue)
  assert len({e["evidence_ref"] for e in catalogue})==len(catalogue)
  catalogue={e["evidence_ref"]:e for e in catalogue}
 assert isinstance(catalogue,dict)
 for key,e in catalogue.items():
  s,lines=source(e["atom_id"])
  for field in ("atom_revision","carrier_path","carrier_sha256"):assert e[field]==s[field],(key,field)
  start,end=e["start_line"],e["end_line"]
  assert type(start) is int and type(end) is int and 1<=start<=end<=len(lines)
  assert start>next(i for i,l in enumerate(lines[1:],2) if l=="---"),key
  q="\n".join(lines[start-1:end]);assert e["quote"] in (q,q+"\n"),key
  assert e["text_sha256"]==sha(e["quote"].encode())
  heads=[l for l in lines[:start] if l.startswith(("# ","## ","### "))]
  assert heads and any(l.startswith(("## Claim","## Scope","## Details","## Operation","## Procedure","## Condition","## Evaluation","## Definition")) for l in heads),key
  assert not heads[-1].startswith("# Summary"),key
 for r in rows:
  ident=r["identity"];assert r["disposition"] in DISPOSITIONS,ident
  assert isinstance(r["confidence_percent"],(int,float)) and 0<=r["confidence_percent"]<=100,ident
  assert r["reason"] and set(r["checks"])==CHECKS,ident
  for name,check in r["checks"].items():
   assert isinstance(check,dict) and check.get("finding") and check.get("reason"),(ident,name)
   assert set(check.get("evidence_refs",[]))<=set(catalogue),(ident,name)
  assert set(r["evidence_refs"])<=set(catalogue),ident
  assert r["checked_source_atom_ids"],ident
  for aid in r["checked_source_atom_ids"]:source(aid)
  if r["disposition"]=="question" or r["confidence_percent"]<90:
   assert r.get("question") and r.get("proposal") is None,ident
  else:
   assert r["evidence_refs"],ident
  if r["disposition"] in {"consolidate","generalize","drop_candidate"} and r["confidence_percent"]>=90:
   proposal=r.get("proposal");assert isinstance(proposal,dict) and proposal,ident
   assert r["evidence_refs"],ident
 return {"batch":batch,"identities":len(rows),"dispositions":dict(collections.Counter(r["disposition"] for r in rows)),"evidence_spans":len(catalogue),"current_sources_checked":len(cache),"file_sha256":sha(raw),"mechanical_checks":"pass","semantic_adoption":"not_performed"}
if __name__=="__main__":
 ap=argparse.ArgumentParser();ap.add_argument("batches",nargs="+",type=int);a=ap.parse_args()
 print(json.dumps([verify(n) for n in a.batches],sort_keys=True))
