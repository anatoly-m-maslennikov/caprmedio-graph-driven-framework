import hashlib, json, re, sys
from dataclasses import replace
from collections import defaultdict
from pathlib import Path

root=Path.cwd()
tools=root/'LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS'
sys.path[:0]=[str(tools),str(tools/'GENERATE_ENTITY_GRAPH')]
from current_entity_sources import _read_atom
from contract_graph import _target
from cfel_claim_constraints import claim_prose, extract_claim_constraints, section_text
import subject_notation as notation

frontier=root/'.caprmedio_caprmedio/02_analysis/draft/model-completeness-audit-20261103/model-supplier-frontier.json'
ops=json.loads(frontier.read_text())['operations']
carriers=[_read_atom(root/o['destination_path'],root) for o in ops]
rows=defaultdict(lambda:{'declarations':[],'other_forms':[],'subject_references':[],'formal_references':[]})
limitations=[]; scaffolding=[]; excluded=[]

def evidence(c, text, category):
    raw=c['raw'].decode('utf-8'); needle=text.strip()
    line=next((i for i,s in enumerate(raw.splitlines(),1) if needle in s),None)
    result={'atom_id':c['source']['atom_id'],'path':c['source']['path'],'line':line,'evidence':text,'kind':category,'role':c['read_view'].get('content_role'),'form':c['read_view'].get('type')}
    if category=='other_forms' and result['role']=='Requirement' and result['form'] in {'Entity Definition','Relation Definition'}:
        result['claim']=claim_prose(c) or section_text(c,'Claim')
    return result

def add_target(target,c,subject,category):
    if not target: return
    kind,name=target
    if kind=='component' and ('//' in name or ':' in name):
        if name.startswith('Term//') or ':' in name:
            excluded.append(evidence(c,subject,'instance_or_term')); return
        kind='model_instance'
    if kind=='component' and '.' in name:
        kind='property'
    if kind=='instance':
        if name.startswith(('Atom//','Term//','Entity/Object/Continuant/Term//')):
            excluded.append(evidence(c,subject,'instance_or_term')); return
        kind='model_instance'
    if kind not in {'primary_node','property','component','relation','model_instance'}: return
    key=f'{kind}:{name}'
    rows[key][category].append(evidence(c,subject,category))

for c in carriers:
    view=c['read_view']; subjects=c['subjects']; active=subjects.get('governs',subjects.get('active',[])); depends=subjects.get('depends_on',subjects.get('passive',[]))
    for role, values in [('governs',active),('depends_on',depends)]:
        for subject in values if isinstance(values,list) else [values]:
            if not isinstance(subject,str): continue
            if re.match(r'^\s*CAPRMEDIO_STRUCTURE(?:\s*<\+|\s*$)',subject): continue
            if re.match(r'^\s*CAPRMEDIO_(?!MODEL\b)[A-Z_]+\b',subject): continue
            if subject.strip()=='CAPRMEDIO_MODEL':
                scaffolding.append(evidence(c,subject,'namespace_root')); continue
            try: expression=notation.parse_subject_expression(subject,subject_profile='approved').expression
            except notation.SubjectNotationError:
                limitations.append(evidence(c,subject,'subject_parse')); continue
            target=_target(expression)
            if target is None:
                limitations.append(evidence(c,subject,'conditional_or_complex_subject')); continue
            # Only governed exact targets carry the declaration identity.
            category=('declarations' if view.get('content_role')=='Requirement' and view.get('type')=='Declaration' else 'other_forms') if role=='governs' else 'subject_references'
            add_target(target,c,subject,category)
    # CFEL Property selectors are evidence of uses, not automatically declarations.
    # Only read claims from sources whose governed Subject explicitly belongs to MODEL.
    active_values=active if isinstance(active,list) else [active]
    if not any(isinstance(s,str) and not re.match(r'^\s*CAPRMEDIO_STRUCTURE\b',s) for s in active_values): continue
    clauses,diagnostics=extract_claim_constraints(c)
    for clause in clauses:
        unquoted=re.sub(r"\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*'", '', clause.get('expression',''))
        for name in re.findall(r'(?<![A-Za-z0-9_])Relation//([A-Za-z][A-Za-z0-9_]*)',unquoted):
            add_target(('relation',name),c,clause['expression'],'formal_references')
        if clause.get('kind')=='relation_cardinality':
            name=clause.get('relation')
            if isinstance(name,str) and re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*',name) and f'(({name}))' in unquoted:
                add_target(('relation',name),c,clause['expression'],'formal_references')
            if '"' in clause['expression'] or "'" in clause['expression']:
                continue
            for endpoint in (clause.get('source_selector'),clause.get('target_selector')):
                if not isinstance(endpoint,str) or any(ch in endpoint for ch in '$[]{}():=@') or endpoint.startswith('Relation//'):
                    continue
                try: parsed=notation.parse_subject_expression(endpoint,subject_profile='approved').expression
                except notation.SubjectNotationError: continue
                candidate=_target(parsed)
                if candidate and candidate[0] in {'primary_node','property','component'}:
                    add_target(candidate,c,clause['expression'],'formal_references')
        selector=clause.get('property_selector')
        if clause.get('kind') not in {'property_constraint','allowed_literal'} or not isinstance(selector,str): continue
        try: expression=notation.parse_subject_expression(selector,subject_profile='approved').expression
        except notation.SubjectNotationError: continue
        target=_target(expression)
        if target and target[0]=='property': add_target(target,c,clause['expression'],'formal_references')

items=[]
for key, fields in sorted(rows.items()):
    kind,name=key.split(':',1); n=len(fields['declarations']);
    # Facts observed solely in other RMED or formal selectors need semantic review.
    definitions=[e for e in fields['other_forms'] if e['role']=='Requirement' and e['form'] in {'Entity Definition','Relation Definition'}]
    status='duplicate' if n>1 else 'declared' if n==1 else 'definition_only' if definitions else 'unresolved_candidate'
    items.append({'kind':kind,'identity':name,'status':status,**fields})
declarations={(x['kind'],x['identity']):x for x in items if x['declarations']}
filtered=[]; inherited_uses=[]; conditional_selections=[]
for item in items:
    if item['declarations']:
        filtered.append(item); continue
    try: expression=notation.parse_subject_expression(item['identity'],subject_profile='approved').expression
    except notation.SubjectNotationError:
        filtered.append(item); continue
    if isinstance(expression,notation.Path) and any(isinstance(step.operand,notation.Qualification) for step in expression.steps):
        steps=tuple(step for step in expression.steps if not isinstance(step.operand,notation.Qualification))
        base=notation.render_subject(replace(expression,steps=steps))
        if item['kind']=='property' and ('property',base) in declarations:
            inherited_uses.append({'identity':item['identity'],'declared_origin':base,'evidence':item['other_forms']+item['subject_references']+item['formal_references']})
        else:
            conditional_selections.append(item)
        continue
    filtered.append(item)
items=filtered
declared=[item for item in items if item['status']=='declared']
for item in items:
    if item['status']!='definition_only': continue
    leaf=item['identity'].split('.')[-1].split('/')[-1].casefold()
    item['same_leaf_declared_candidates']=[x['identity'] for x in declared if x['kind']==item['kind'] and x['identity'].split('.')[-1].split('/')[-1].casefold()==leaf]
    if item['identity']=='Carrier/File.Format':
        item['identity_review']='possible_inherited_property'; item['possible_origin']='Carrier.Format'
        item['review_reason']='File is a narrower Carrier; both Definition Claims describe the Carrier representation format. Confirm inherited identity before counting separately.'
    elif item['identity']=='Format//markdown':
        item['identity_review']='alias_unknown'
        item['review_reason']='Named Format instance; check identity against any alternative format-addressing paths before counting separately.'
    else:
        item['identity_review']='high_confidence_distinct'
        item['review_reason']='Definition Claim identifies a distinct modeled concept or bearer Property; same-leaf names on other bearers do not establish identity.'
report={'selected':len(carriers),'frontier':str(frontier.relative_to(root)),'frontier_sha256_mismatches':[o['destination_path'] for o in ops if hashlib.sha256((root/o['destination_path']).read_bytes()).hexdigest()!=o['sha256']],'criteria':'Requirement / Declaration only; exact governed target','entities':items,'inherited_property_uses':inherited_uses,'conditional_selections':conditional_selections,'namespace_scaffolding':scaffolding,'complex_subject_limitations':limitations,'excluded_instance_or_term_occurrences':len(excluded), 'limitations':['Unprefixed supplier Subjects are retained; their MODEL scope remains subject to semantic review.','Candidate Property uses may be inherited; no missing Declaration is asserted without inheritance review.','Formal-reference inventory is bounded to recognized Property selectors; unsupported CFEL and complex Subjects remain unclassified.','Term registry entries and concrete Atom instances are excluded; modeled Operator instances and Relation objects are retained.']}
out=Path(__file__).parent; (out/'entity-declaration-map.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
from collections import Counter
print('counts',Counter((x['kind'],x['status']) for x in items),'complex',len(limitations),'inherited',len(inherited_uses),'conditional',len(conditional_selections),'scaffolding',len(scaffolding),'excluded',len(excluded))
for item in items:
 if item['status']!='declared':
  print(item['kind'],item['identity'],item['status'], 'decl',len(item['declarations']),'other',len(item['other_forms']),'refs',len(item['subject_references']),'formal',len(item['formal_references']))
