import hashlib,json
from pathlib import Path
root=Path.cwd();core=root/'.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL';out=root/'.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/application/property-order-20261105/layout';manifest=out/'manifest.json'; old=json.loads(manifest.read_text()); h=lambda b:hashlib.sha256(b).hexdigest();rows=[]
def make(id,src,fn):
 p=core/src;b=p.read_bytes();text=fn(b.decode());q=out/f'{id}.preview.md';q.write_text(text);rows.append({'id':id,'source':str(p.relative_to(root)),'source_sha256':h(b),'preview':str(q.relative_to(root)),'preview_sha256':h(text.encode())})
def repl(t,a,b):assert t.count(a)==1,(a,t.count(a));return t.replace(a,b)
def head(t):return repl(t,'in(ID, Role, Form, Version, Status, Updated At, Label, Tier, Topics, Relations, Container, Carrier Destination, Priority, AI Agent Confidence Threshold, Work Sequence Number)','in(ID, Ref ID, Role, Form, Version, Status, Updated At, Label, Tier, Topics, Relations, Container, Carrier Destination, Priority, AI Agent Confidence Threshold, Work Sequence Number)')
make('R2719','04_requirement/draft/CA-R-2719@2-draft-CORE_META_MODEL-DECLARATION--declare-atom-header.md',head)
for r in old['outputs']:
 if r['id'] in ('R2709','D657-current','D657-draft'):
  p=root/r['source'];q=root/r['preview'];assert h(p.read_bytes())==r['source_sha256'] and h(q.read_bytes())==r['preview_sha256'];rows.append(r)
for r in rows:
 if r['id'] in ('D657-current','D657-draft'):
  p=root/r['preview'];t=p.read_text();t=repl(t,'Serialize Header keys in the declared Property order, omitting absent optional Properties.','Serialize Header keys in the declared Property order, omitting absent optional Properties. Place other admitted Header Properties after the ordered base Properties, with no required order among them.');p.write_text(t);r['preview_sha256']=h(t.encode())
def d479(t):
 old='Serialize declared Content Properties in this order: `## Summary`, `## Claim`, `## Semantics`, then `## Details`. Omit absent optional Properties. Within Claim, place `### Prose Claim` before `### Formal Claim` when present. For a Workflow or Step, place `### Mermaid Scheme` first within Claim when present, before Prose Claim and Formal Claim.'
 new='Serialize Content headings in the declared sibling Property order, omitting absent optional Properties. Place other admitted sibling Properties after the ordered Properties, with no required order among them. For a Step, place `### Mermaid Scheme` first within Claim when present, before Prose Claim and Formal Claim.'
 return repl(t,old,new)
make('D479-draft','07_delivery/draft/CA-D-479@31-draft-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties.md',d479)
def current(t):
 old='For ordinary RMED, carry one `## Summary` and one `## Claim` as sibling Properties, optionally followed by `## Semantics` and `## Details` in that order. Claim has no direct value and contains one or both `### Formal Claim` and `### Prose Claim`, with unique sibling names. Formal Claim contains a CFEL-labelled code fence; Prose Claim contains ordinary Markdown. Omit absent optional Properties. Do not duplicate Claim in frontmatter.'
 new='Serialize Content headings in the declared sibling Property order, omitting absent optional Properties. Place other admitted sibling Properties after the ordered Properties, with no required order among them. For a Workflow, when Mermaid Scheme is declared as a Claim child, serialize it before Prose Claim and Formal Claim when present.\n\nFor ordinary RMED, carry one `## Summary` and one `## Claim` as sibling Properties. Claim has no direct value and contains one or both `### Prose Claim` and `### Formal Claim`, with unique sibling names. Formal Claim contains a CFEL-labelled code fence; Prose Claim contains ordinary Markdown. Do not duplicate Claim in frontmatter.'
 return repl(t,old,new)
make('D479-current','07_delivery/CA-D-479-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties.md',current)
header=['ID','Ref ID','Container','Role','Form','Label','Topics','Tier','Relations','Status','Version','Updated At','Carrier Destination']; content=['Summary','Claim','Semantics','Details'];hfields=['Atom.Header.'+x for x in header];cfields=['Atom/(.Header.Role in RMED).Content.'+x for x in content];facts=[f'{x} ;> {y}' for a in (hfields,cfields) for x,y in zip(a,a[1:])];facts.append('Atom/(.Header.Role in RMED).Content.Claim.Prose Claim ;> Atom/(.Header.Role in RMED).Content.Claim.Formal Claim')
body='## Summary\n\nOrder Atom Header and Content Properties\n\n## Claim\n\n### Prose Claim\n\nWhen Workflow.Content.Claim.Mermaid Scheme is declared as a Claim child, it precedes Prose Claim and Formal Claim when those children are present. Other admitted sibling Properties follow the ordered Properties, without a required order among them.\n\n### Formal Claim\n\n```CFEL\n# model\n'+';\n\n'.join(facts)+'\n```\n';q=out/'R-UNALLOCATED-property-order.preview.txt';q.write_text(body)
new=[r for r in old['new_candidates'] if r['id']=='UNALLOCATED'];new.append({'id':'UNALLOCATED_ORDER_RULE','main_subject':'CAPRMEDIO_MODEL <+ Node.**','preview':str(q.relative_to(root)),'preview_sha256':h(body.encode())})
manifest.write_text(json.dumps({'status':'provisional_preview_not_native','superseded':['R2498','R2500','R2961'],'outputs':rows,'new_candidates':new},indent=2)+'\n')
