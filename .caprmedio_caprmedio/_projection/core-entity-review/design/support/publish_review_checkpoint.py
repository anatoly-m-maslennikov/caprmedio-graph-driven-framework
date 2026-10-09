"""Create-only durable checkpoint of verified review outputs and exact inputs."""
import hashlib,json,pathlib,shutil
ROOT=pathlib.Path.cwd()
SRC=ROOT/".caprmedio_tmp/planning/core-entity-review/design"
DST=ROOT/".caprmedio_caprmedio/_projection/core-entity-review/design"
def sha(raw):return hashlib.sha256(raw).hexdigest()
def save(path,raw):
 for p in [path,*path.parents]:
  if p==ROOT.parent:break
  assert not p.is_symlink(),p
 path.parent.mkdir(parents=True,exist_ok=True)
 if path.exists():assert path.read_bytes()==raw,f"refuse overwrite: {path}"
 else:
  with path.open("xb") as handle:handle.write(raw)
def main():
 names=[f"relations.batch-{n}.json" for n in range(1,6)]
 names += [f"relations.batch-6.remaining-{n}.json" for n in range(1,5)]
 names += ["batch-6.reviewed.checkpoint.json","rmed.views.json","rmed.views.md","rmed.roles.indented.txt","rmed.entities.indented.txt","structure.design.json"]
 inputs=[f"batch-{n}.input.json" for n in range(1,7)]+[f"remaining-{n}.input.json" for n in range(1,5)]+["partition.manifest.json","remaining.manifest.json","contract.md"]
 supports=sorted(p.name for p in SRC.glob("build_*.py"))
 refs=[]
 for name in names+inputs+supports:
  path=SRC/name;raw=path.read_bytes()
  folder="inputs" if name in inputs else ("support" if name in supports else "")
  dest=DST/folder/name
  save(dest,raw)
  refs.append({"source_path":str(path.relative_to(ROOT)),"path":str(dest.relative_to(ROOT)),"sha256":sha(raw),"bytes":len(raw),"checkpoint_only":name=="structure.design.json"})
 for name in ["verify_design_batches.py","test_design_boundary.py","prepare_design_batches.py","prepare_remaining_cases.py","publish_review_checkpoint.py"]:
  path=SRC.parent/name;raw=path.read_bytes();dest=DST/"support"/name;save(dest,raw)
  refs.append({"source_path":str(path.relative_to(ROOT)),"path":str(dest.relative_to(ROOT)),"sha256":sha(raw),"bytes":len(raw)})
 baseline=json.loads((ROOT/".caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json").read_bytes())
 result={"source_task":"CA-P-1906","projection_kind":"caprmedio.core_graph_design.verified_review_checkpoint",
         "non_authoritative":True,"semantic_admission":"not_performed","source_migration":"not_performed",
         "baseline_inventory_sha256":baseline["inventory_sha256"],"source_binding":baseline["source_binding"],
         "files":refs,"design_complete":False,"pending":"Temporal display convention, batch join and complete design integration/verification."}
 result["checkpoint_sha256"]=sha(json.dumps(result,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode())
 save(DST/"review.checkpoint.json",json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2).encode()+b"\n")
 print(json.dumps({"outcome":"saved","files":len(refs),"checkpoint_sha256":result["checkpoint_sha256"]}))
if __name__=="__main__":main()
