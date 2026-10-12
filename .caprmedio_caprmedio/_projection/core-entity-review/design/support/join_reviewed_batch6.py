"""Join only completed reviewed partitions, create-only and without semantic decisions."""
import hashlib,json,pathlib,importlib.util,re
ROOT=pathlib.Path.cwd()
D=ROOT/".caprmedio_caprmedio/_projection/core-entity-review/design"
T=ROOT/".caprmedio_tmp/planning/core-entity-review/design"
def sha(raw):return hashlib.sha256(raw).hexdigest()
def canonical(value):return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()
def read(path):return json.loads(path.read_bytes())
def save(path,raw):
 path.parent.mkdir(parents=True,exist_ok=True)
 if path.exists():assert path.read_bytes()==raw, f"refuse overwrite: {path}"
 else:
  with path.open("xb") as handle:handle.write(raw)
def main():
 specs=[]
 for aid in range(1923,1927):
  matches=list((ROOT/".caprmedio_caprmedio/03_plan").rglob(f"*-CA-P-{aid}-TASK--*.md"))
  assert len(matches)==1,(aid,matches)
  raw=matches[0].read_bytes();assert re.search(rb"^status: Done$",raw,re.M),aid
  specs.append({"atom_id":f"CA-P-{aid}","carrier_path":str(matches[0].relative_to(ROOT)),"carrier_sha256":sha(raw),"status":"Done"})
 original=read(D/"inputs/batch-6.input.json");checkpoint=read(D/"batch-6.reviewed.checkpoint.json")
 assert checkpoint["reviewed_cases"]==16 and checkpoint["remaining_cases"]==49
 rows=list(checkpoint["cases"]);refs=[]
 vp=ROOT/".caprmedio_tmp/planning/core-entity-review/verify_design_batches.py"
 spec=importlib.util.spec_from_file_location("v",vp);v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
 for n in range(1,5):
  p=D/f"relations.batch-6.remaining-{n}.json";data=read(p)
  check=v.verify_batch(6,D/f"inputs/remaining-{n}.input.json",p)
  rows.extend(data["cases"]);refs.append({"path":str(p.relative_to(ROOT)),"sha256":sha(p.read_bytes()),"validation":check})
 assert len(rows)==65 and len({r["case_id"] for r in rows})==65
 assert {r["case_id"] for r in rows}=={r["case_id"] for r in original["cases"]}
 final={k:value for k,value in checkpoint.items() if k not in ("cases","checkpoint_sha256","checkpoint_source_sha256","complete_review","reviewed_cases","remaining_case_ids","remaining_cases")}
 final.update({"source_task":"CA-P-1918","producer_task":"CA-P-1927","cases":sorted(rows,key=lambda r:r["case_id"]),"complete_review":True,
               "input_checkpoint":{"path":str((D/"batch-6.reviewed.checkpoint.json").relative_to(ROOT)),"sha256":sha((D/"batch-6.reviewed.checkpoint.json").read_bytes())},
               "child_completion_pins":specs,"reviewed_partition_receipts":refs})
 final["review_sha256"]=sha(canonical(final))
 raw=json.dumps(final,ensure_ascii=False,sort_keys=True,indent=2).encode()+b"\n"
 target=D/"relations.batch-6.final.json";save(target,raw);save(T/"relations.batch-6.final.json",raw)
 check=v.verify_batch(6,D/"inputs/batch-6.input.json",target)
 print(json.dumps({"outcome":"joined","path":str(target.relative_to(ROOT)),"review_sha256":final["review_sha256"],"validation":check},sort_keys=True))
if __name__=="__main__":main()
