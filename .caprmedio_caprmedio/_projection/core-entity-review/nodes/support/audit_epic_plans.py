import json,pathlib,re,sys,collections,subprocess
sys.path.insert(0,"102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH")
import generate_entity_graph as g
epic=pathlib.Path(sys.argv[1])
root=epic.with_suffix("")
paths=[epic]+sorted(root.rglob("*.md"))
items={};issues=[]
def targets(fm,key):
    m=re.search(r"^  "+re.escape(key)+r":(?:[ \t]*([^\n]+))?\n?((?:    -[^\n]*\n?)*)",fm,re.M)
    return re.findall(r"CA-P-\d+"," ".join(m.groups(default=""))) if m else []
for p in paths:
    text=p.read_text()
    try: fm=g.split_frontmatter(p.read_bytes(),str(p))
    except Exception as e: issues.append([str(p),"frontmatter",str(e)]);continue
    aid=g.top_scalar(fm,"atom_id")
    if aid in items: issues.append([str(p),"duplicate_id",aid])
    parents=targets(fm,"is_decomposition_of");blocks=targets(fm,"blocks")
    items[aid]={"id":aid,"path":str(p),"status":g.top_scalar(fm,"status"),"label":g.top_scalar(fm,"label"),"author":g.top_scalar(fm,"author"),"assignee":g.top_scalar(fm,"assignee"),"sequence":g.top_scalar(fm,"work_sequence_number"),"parents":parents,"blocks":blocks,"text":text}
    for key in ("content_role","type","current_scope_unit","claim_target_scope_unit","local_tier","global_tier","author","status","version","updated_at"):
        if not g.top_scalar(fm,key):issues.append([aid,"missing_metadata",key])
    for h in ("# Summary","## Objective","## Details","### Definition of Done"):
        if text.splitlines().count(h)!=1:issues.append([aid,"heading_count",h])
    if "## Scope" in text:issues.append([aid,"duplicate_scope"])
    summary=text.split("# Summary\n\n",1)[1].split("\n\n",1)[0] if "# Summary\n\n" in text else ""
    if not p.stem.endswith("--"+summary.lower().replace(" ","-")):issues.append([aid,"stem_summary",summary])
    if len(parents)!=1:issues.append([aid,"parent_cardinality",parents])
    container=p.parent
    while container.name in ("done","canceled","archived"):container=container.parent
    carrier=re.search(r"CA-P-\d+",container.name)
    if carrier and parents!=[carrier.group()]:issues.append([aid,"carrier_parent",parents,carrier.group()])
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)",text):
        if "://" not in target and not target.startswith("#"):
            resolved=(p.parent/target.split("#",1)[0]).resolve()
            if not resolved.exists():issues.append([aid,"broken_relative_link",target])
children=collections.defaultdict(list);incoming=collections.defaultdict(list)
for aid,item in items.items():
    for parent in item["parents"]: children[parent].append(aid)
    for target in item["blocks"]:incoming[target].append(aid)
for aid,item in items.items():
    if not children[aid]:
        if not item["assignee"]:issues.append([aid,"leaf_missing_assignee"])
        if not re.search(r"(?:<=|≤|up to|:)\s*(?:5|10|15)\s*(?:minutes|min)",item["text"],re.I):issues.append([aid,"leaf_estimate_not_found"])
    else:
        if item["assignee"]:issues.append([aid,"composite_assignee_review",item["assignee"]])
    for required in re.findall(r"Required start prerequisite: (CA-P-\d+)",item["text"]):
        if required not in incoming[aid]:issues.append([aid,"text_prerequisite_without_incoming_blocks",required])
seq=collections.defaultdict(list)
for aid,item in items.items():
    seq[(tuple(item["parents"]),item["sequence"])].append(aid)
for k,v in seq.items():
    if len(v)>1:issues.append(["duplicate_sibling_sequence",k,v])
def cycles(edges):
    visiting=set();done=set();out=[]
    def visit(aid,trail):
        if aid in visiting:out.append(trail+[aid]);return
        if aid in done:return
        visiting.add(aid)
        for target in edges.get(aid,[]):
            if target in items:visit(target,trail+[aid])
        visiting.remove(aid);done.add(aid)
    for aid in items:visit(aid,[])
    return out
for kind,edges in (("blocks",{i:v["blocks"] for i,v in items.items()}),("decomposition",{i:v["parents"] for i,v in items.items()})):
    for cycle in cycles(edges):issues.append([kind+"_cycle",cycle])
external=sorted({t for v in items.values() for t in v["parents"]+v["blocks"] if t not in items})
print(json.dumps({"epic_tree_plans":len(items),"leaves":sum(not children[i] for i in items),"structural_issues":issues,"external_plan_targets":external,"statuses":dict(collections.Counter(v["status"] for v in items.values()))},indent=2))
