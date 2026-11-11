import hashlib, importlib.util, json, re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
root=Path.cwd().resolve()
helper=root/'.caprmedio_caprmedio/03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-header-content-20261103/integration/adopt.py'
spec=importlib.util.spec_from_file_location('model_adopt',helper); a=importlib.util.module_from_spec(spec); spec.loader.exec_module(a); a.ROOT=root
out=root/'.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/application/content-order-20261105'
relative=Path('.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft')
claim='Workflow.Content.Claim'
entries=[
 ('workflow-content-claim',claim, f'{claim}{{::1}} :: []{{::0}};\n\n{claim}.*[in (Mermaid Scheme, Prose Claim, Formal Claim)]{{::1..3}}', 'Workflow Claim has unique child Property names.'),
 ('workflow-content-claim-mermaid-scheme',claim+'.Mermaid Scheme',f'{claim}.Mermaid Scheme{{::1}} :: [markdown]{{::1}};\n\n{claim}.Mermaid Scheme.*[]{{::0}}', 'The Mermaid Scheme shows all Workflow Steps and their substeps in a linear sequence without logic.'),
 ('workflow-content-claim-prose-claim',claim+'.Prose Claim',f'{claim}.Prose Claim{{::0..1}} :: [markdown]{{::1}};\n\n{claim}.Prose Claim.*[]{{::0}}',None),
 ('workflow-content-claim-formal-claim',claim+'.Formal Claim',f'{claim}.Formal Claim{{::0..1}} :: [markdown]{{::1}};\n\n{claim}.Formal Claim.*[]{{::0}}',None)]
receipt=out/'workflow-declarations-receipt.json'
if receipt.exists(): raise RuntimeError('already created')
with a.atom_identity_lock(root):
    retained=list(a.control_root(root).rglob('CA-[RMED]-*.md'))
    maximum=max(int(m[1]) for p in retained if (m:=re.match(r'CA-R-(\d+)',p.name)))
    now=datetime.now(ZoneInfo('Asia/Tbilisi')).strftime('%Y-%m-%d %H:%M:%S %z'); rows=[]
    for slug, subject, formal, semantics in entries:
        while True:
            maximum+=1; identity=f'CA-R-{maximum}'
            if not a.atom_id_has_preserved_history_evidence(root,identity): break
        filename=f'{identity}@1-draft-CORE_META_MODEL-DECLARATION--declare-{slug}.md'; target=a.checked_path((relative/filename).as_posix())
        meta={'atom_id':identity,'status':'Draft','topics':{'main_subject':f'CAPRMEDIO_MODEL <+ {subject}'},'version':1,'relations':{'IS_CONTAINED_BY':{'scope_unit':'CA-SU-11'}},'tier':3,'role':'Requirement','form':'Declaration','updated_at':now,'carrier_destination':{'file':{'name':filename,'path':relative.as_posix()}}}
        body=f'\n\n## Summary\n\nDeclare {subject}\n\n## Claim\n\n### Formal Claim\n\n```CFEL\n# model\n{formal}\n```\n'
        if semantics: body+=f'\n## Semantics\n\n{semantics}\n'
        data=a.render(meta,body)
        with target.open('xb') as f:f.write(data)
        assert target.read_bytes()==data and a.summary(a.read(data)[1])==f'Declare {subject}'
        rows.append({'atom_id':identity,'path':str(target.relative_to(root)),'sha256':hashlib.sha256(data).hexdigest()})
    receipt.write_text(json.dumps({'native_workflow_admission':False,'journal_append':False,'outputs':rows},indent=2)+'\n')
print(json.dumps(rows,indent=2))
