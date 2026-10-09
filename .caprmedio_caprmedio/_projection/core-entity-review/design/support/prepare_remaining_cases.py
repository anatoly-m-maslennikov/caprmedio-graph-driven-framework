"""Seal a partial batch checkpoint and four complete disjoint remaining inputs."""
import hashlib,json,pathlib
ROOT=pathlib.Path.cwd()
D=ROOT/".caprmedio_tmp/planning/core-entity-review/design"
def sha(raw):return hashlib.sha256(raw).hexdigest()
def canonical(data):return json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()
def save(path,data):
 raw=json.dumps(data,ensure_ascii=False,sort_keys=True,indent=2).encode()+b"\n"
 if path.exists():assert path.read_bytes()==raw,path
 else:
  with path.open("xb") as h:h.write(raw)
 return sha(raw)
def main():
 raw=(D/"relations.batch-6.json").read_bytes()
 assert sha(raw)=="43db3bb5f5c82994812afb8bf63950c28298a098fb9e6a535c75ad7c8676c799"
 previous=json.loads(raw);original=json.loads((D/"batch-6.input.json").read_bytes())
 reviewed=[r for r in previous["cases"] if r["disposition"]=="not-native" and r.get("display_candidate") and r["evidence"]]
 assert len(reviewed)==16
 remaining_ids={r["case_id"] for r in previous["cases"]}- {r["case_id"] for r in reviewed}
 remaining=sorted([r for r in original["cases"] if r["case_id"] in remaining_ids],key=lambda r:r["case_id"])
 assert len(remaining)==49
 checkpoint={k:v for k,v in previous.items() if k!="cases"}
 checkpoint.update({"cases":reviewed,"checkpoint_source_sha256":sha(raw),"complete_review":False,
                    "reviewed_cases":16,"remaining_case_ids":sorted(remaining_ids),"remaining_cases":49})
 checkpoint["checkpoint_sha256"]=sha(canonical(checkpoint))
 save(D/"batch-6.reviewed.checkpoint.json",checkpoint)
 partitions=[remaining[:13],remaining[13:25],remaining[25:37],remaining[37:]]
 pins=[]
 for n,rows in enumerate(partitions,1):
  payload={k:v for k,v in original.items() if k not in ("cases","partition_sha256","case_count","source_task")}
  payload.update({"source_task":f"CA-P-{1922+n}","sub_batch_number":n,"case_count":len(rows),"cases":rows,
                  "original_partition_sha256":original["partition_sha256"],"checkpoint_sha256":checkpoint["checkpoint_sha256"]})
  payload["partition_sha256"]=sha(canonical(payload))
  p=D/f"remaining-{n}.input.json";pins.append({"path":str(p.relative_to(ROOT)),"file_sha256":save(p,payload),"source_task":payload["source_task"],"case_count":len(rows),"partition_sha256":payload["partition_sha256"]})
 assert len({r["case_id"] for rows in partitions for r in rows})==49
 manifest={"source_task":"CA-P-1918","reviewed_checkpoint_sha256":checkpoint["checkpoint_sha256"],
           "original_partition_sha256":original["partition_sha256"],"complete_review":False,"reviewed_case_count":16,
           "remaining_case_count":49,"partitions":pins}
 save(D/"remaining.manifest.json",manifest)
 print(json.dumps({"outcome":"sealed","reviewed":16,"remaining":49,"partition_counts":[len(x) for x in partitions]}))
if __name__=="__main__":main()
