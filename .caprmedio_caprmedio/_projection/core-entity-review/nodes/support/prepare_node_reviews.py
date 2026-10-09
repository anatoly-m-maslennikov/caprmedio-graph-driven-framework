"""Prepare disjoint source-pinned node review inputs. No semantic classification."""
import argparse,hashlib,json,pathlib
ROOT=pathlib.Path.cwd()
D=ROOT/".caprmedio_caprmedio/_projection/core-entity-review/nodes"
BASE=ROOT/".caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json"
DECISION=ROOT/".caprmedio_caprmedio/_projection/core-entity-review/design/operator.decisions.md"
EXPECTED="bc5d99e91fb7dd4dcb42e59ff33cc24cff1d0901c5904764394c769aaa0a9430"
def sha(raw):return hashlib.sha256(raw).hexdigest()
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()
def special(s):return ("/Revision" in s or s in ("Revision","Claim","Atom/Claim","Atom/Scope","Atom/Details") or s.startswith("Applicable Methodology") or s.startswith("Atom/Claim/") or "/Claim/" in s or s.endswith("/Claim"))
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--persist",action="store_true");args=ap.parse_args()
 raw=BASE.read_bytes();assert sha(raw)==EXPECTED;b=json.loads(raw)
 nodes=sorted(b["nodes"],key=lambda n:n["identity"]);target=[n for n in nodes if special(n["identity"])]
 rest=[n for n in nodes if not special(n["identity"])]
 assert len(target)==62 and len(rest)==644
 parts=[target]+[rest[(len(rest)*i)//8:(len(rest)*(i+1))//8] for i in range(8)]
 assert sum(map(len,parts))==706 and len({n["identity"] for p in parts for n in p})==706
 outputs={};manifest={"source_task":"CA-P-1907","non_authoritative":True,"semantic_classification":"not_performed","baseline_sha256":EXPECTED,"baseline_inventory_sha256":b["inventory_sha256"],"operator_decision":{"path":str(DECISION.relative_to(ROOT)),"sha256":sha(DECISION.read_bytes())},"partitions":[]}
 for i,p in enumerate(parts):
  packet={"source_task":"CA-P-"+str(1928+i),"batch":i,"non_authoritative":True,"baseline":{"path":str(BASE.relative_to(ROOT)),"sha256":EXPECTED,"inventory_sha256":b["inventory_sha256"]},"operator_decision":manifest["operator_decision"],"identity_count":len(p),"nodes":[{"identity":n["identity"],"occurrence_ids":n["occurrence_ids"],"source_atom_ids":n["source_atom_ids"],"governing_source_atom_ids":n["governing_source_atom_ids"],"is_full_target":n["is_full_target"],"is_syntactic_root":n["is_syntactic_root"]} for n in p]}
  packet["partition_sha256"]=sha(canonical(packet))
  payload=canonical(packet)+b"\n";relative=f"inputs/nodes.batch-{i}.input.json";outputs[D/relative]=payload
  manifest["partitions"].append({"batch":i,"source_task":packet["source_task"],"identity_count":len(p),"path":str((D/relative).relative_to(ROOT)),"sha256":sha(payload),"partition_sha256":packet["partition_sha256"]})
 manifest["manifest_sha256"]=sha(canonical(manifest));outputs[D/"partition.manifest.json"]=json.dumps(manifest,ensure_ascii=False,sort_keys=True,indent=2).encode()+b"\n"
 if args.persist:
  for path,raw in outputs.items():
   assert path.resolve().is_relative_to(ROOT) and not path.is_symlink()
   if path.exists():assert path.read_bytes()==raw,("refuse-overwrite",path)
  for path,raw in outputs.items():
   path.parent.mkdir(parents=True,exist_ok=True)
   if not path.exists():
    with path.open("xb") as handle:handle.write(raw)
 print(json.dumps({"outcome":"persisted" if args.persist else "dry_run","total":706,"partitions":manifest["partitions"],"manifest_sha256":manifest["manifest_sha256"]},sort_keys=True))
if __name__=="__main__":main()
