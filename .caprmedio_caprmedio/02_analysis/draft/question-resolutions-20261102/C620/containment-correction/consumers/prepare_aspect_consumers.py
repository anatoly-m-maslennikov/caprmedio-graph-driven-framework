#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[7]; BASE=Path(__file__).resolve().parent; OUT=BASE/'drafts'
FRONTIER=ROOT/'.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/02_analysis/draft/cfel-contract-completion-20261102/integration/current-source-frontier.json'
INVENTORY=ROOT/'.caprmedio_caprmedio/02_analysis/draft/question-resolutions-20261102/C620/aspect-consumer-inventory.json'
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def mp(s):
    if s=='Entity/Aspect/Product: CAPRMEDIO Framework': return 'Aspects <+ Product'
    return 'Aspects <+ '+' <+ '.join(s[14:].split('/')) if s.startswith('Entity/Aspect/') else None
def parse(t):
    _,_,r=t.partition('---\n'); m,sep,b=r.partition('---\n');
    if not sep: raise ValueError('missing frontmatter')
    return yaml.safe_load(m),b
def occ(m):
    return [(k,x) for k,v in (m.get('subjects') or {}).items() for x in (v if isinstance(v,list) else [v]) if isinstance(x,str)]
def main():
    f=json.loads(FRONTIER.read_text()); inv=json.loads(INVENTORY.read_text()); forms=[x[0] for x in inv['unique_concrete_aspect_subjects']]; assert len(forms)==31
    mapping={x:mp(x) for x in forms}; assert all(mapping.values()) and mapping['Entity/Aspect/Product: CAPRMEDIO Framework']=='Aspects <+ Product'
    OUT.mkdir(parents=True,exist_ok=True)
    for p in OUT.glob('*.md'): p.unlink()
    counts={k:0 for k in ('active_before','passive_before','active_after','passive_after')}; records=[]; all_hits=[]
    for op in f['operations']:
        src=ROOT/op['destination_path']; assert digest(src)==op['sha256'],op['base_id']; original=src.read_text(); meta,body=parse(original); pairs=occ(meta); hits=sorted({s for _,s in pairs if s in mapping}); all_hits += [{'source_id':op['base_id'],'old_address':s} for s in mapping if s in body]
        if not hits: continue
        for k,s in pairs:
            if k in ('active','passive') and s in mapping: counts[k+'_before']+=1
        nm=json.loads(json.dumps(meta)); subs=nm.get('subjects') or {}
        for k,v in list(subs.items()):
            vals=v if isinstance(v,list) else [v]; new=[mapping.get(x,x) for x in vals]; subs[k]=new if isinstance(v,list) else new[0]
        nm['subjects']=subs; ver=int(op['version'])+1; did=f"{op['base_id']}@{ver}-draft"; nm.update(version=ver,atom_id=did,status='Draft')
        for k,s in occ(nm):
            if k in ('active','passive') and s.startswith('Aspects <+'): counts[k+'_after']+=1
        dest=OUT/f'{did}.md'; dest.write_text('---\n'+yaml.safe_dump(nm,sort_keys=False,allow_unicode=True).rstrip()+'\n---\n'+body); parsed,parsed_body=parse(dest.read_text()); assert parsed_body==body; assert all(meta[k]==parsed[k] for k in meta if k not in {'subjects','atom_id','version','status'})
        records.append({'source_id':op['base_id'],'source_version':op['version'],'draft_id':did,'source_path':op['destination_path'],'source_sha256':op['sha256'],'draft_path':str(dest.relative_to(ROOT)),'draft_sha256':digest(dest),'mapping':{s:mapping[s] for _,s in pairs if s in mapping},'body_old_address_hits':sorted({s for s in hits if s in body}),'body_unchanged':True})
    assert len(mapping)==31 and not any('Entity/Aspect/' in s for r in records for _,s in occ(parse((ROOT/r['draft_path']).read_text())[0]))
    assert len({r['source_id'] for r in records if 'Entity/Aspect/Product: CAPRMEDIO Framework' in r['mapping']})==47
    out={'source_frontier':{'path':str(FRONTIER.relative_to(ROOT)),'sha256':digest(FRONTIER),'selected_operations':len(f['operations'])},'inventory':{'path':str(INVENTORY.relative_to(ROOT)),'sha256':digest(INVENTORY),'unique_mapping_count':31},'mapping_table':mapping,'counts':counts,'affected_source_count':len(records),'affected_source_ids':[r['source_id'] for r in records],'all_selected_body_old_address_hits':all_hits,'records':records}
    (BASE/'consumer-manifest.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n'); print(json.dumps({'affected_sources':len(records),'counts':counts,'body_hits':len(all_hits)},indent=2))
if __name__=='__main__': main()
