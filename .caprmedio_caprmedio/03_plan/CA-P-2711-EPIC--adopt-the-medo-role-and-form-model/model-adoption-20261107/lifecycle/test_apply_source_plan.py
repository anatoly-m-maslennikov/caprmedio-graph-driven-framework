import json,os,tempfile,unittest
from contextlib import nullcontext
from pathlib import Path
import importlib.util
HERE=Path(__file__).parent; spec=importlib.util.spec_from_file_location('a',HERE/'apply_source_plan.py'); a=importlib.util.module_from_spec(spec); spec.loader.exec_module(a); a.atom_identity_lock=lambda root:nullcontext()
def atom(i,v,status='Active'): return f'---\natom_id: {i}\nversion: {v}\nstatus: {status}\n---\n# Summary\n\nX\n'
class TestPlan(unittest.TestCase):
 def setUp(self):
  self.d=tempfile.TemporaryDirectory(); self.root=Path(self.d.name); self.base=self.root/'.caprmedio_caprmedio/CA-SU-1/04_requirement'; self.base.mkdir(parents=True)
  self.cur=self.base/'CA-R-1.md'; self.draft=self.base/'draft/CA-R-1@3-draft.md'; self.draft.parent.mkdir(); self.cur.write_text(atom('CA-R-1',2)); self.draft.write_text(atom('CA-R-1',3,'Draft')); os.chmod(self.cur,0o640)
 def tearDown(self): self.d.cleanup()
 def plan(self,ops,version=4):
  pins=[]
  for p in (self.cur,self.draft): pins.append({'path':p.relative_to(self.root).as_posix(),'sha256':a.sha(p.read_bytes()),'atom_id':'CA-R-1','version':int(__import__('re').search(r'version: (\d+)',p.read_text()).group(1))})
  q=self.root/'p.json'; q.write_text(json.dumps({'operations':ops,'version_pins':pins,'selected_versions':{'CA-R-1':version},'outputs':[]})); return q
 def op(self,p,before,after): return {'path':p.relative_to(self.root).as_posix(),'before':before,'before_sha256':a.sha(before.encode()) if before else None,'after':after,'after_sha256':a.sha(after.encode()) if after else None}
 def test_happy_and_mode(self):
  after=atom('CA-R-1',4); plan=self.plan([self.op(self.cur,self.cur.read_text(),after),self.op(self.draft,self.draft.read_text(),None)]); a.apply(self.root,plan,self.root/'r.json'); self.assertEqual(self.cur.read_text(),after); self.assertFalse(self.draft.exists()); self.assertEqual(self.cur.stat().st_mode&0o777,0o640)
 def test_stale_preimage(self):
  plan=self.plan([self.op(self.cur,self.cur.read_text(),atom('CA-R-1',4))]); self.cur.write_text('drift')
  with self.assertRaises(ValueError): a.apply(self.root,plan,self.root/'r.json')
 def test_collision_new_target(self):
  new=self.base/'CA-R-2.md'; new.write_text('occupied'); plan=self.plan([self.op(new,None,'new')])
  with self.assertRaises(ValueError): a.apply(self.root,plan,self.root/'r.json')
 def test_midbatch_rollback(self):
  sentinel=self.base/'sentinel.md'; sentinel.write_text('keep'); before=self.cur.read_text(); plan=self.plan([self.op(self.cur,before,atom('CA-R-1',4)),self.op(sentinel,'keep','changed')])
  real=a.os.replace; calls=[0]
  def fail(src,dst):
   calls[0]+=1
   if calls[0]==2: raise OSError('forced')
   return real(src,dst)
  a.os.replace=fail
  try:
   with self.assertRaises(OSError): a.apply(self.root,plan,self.root/'r.json')
  finally:a.os.replace=real
  self.assertEqual(self.cur.read_text(),before); self.assertTrue(self.draft.exists()); self.assertEqual(sentinel.read_text(),'keep')
 def test_occupied_draft_requires_four(self):
  plan=self.plan([],3)
  with self.assertRaises(ValueError): a.apply(self.root,plan,self.root/'r.json')
 def test_archive_and_nested_identity_raise_next_version(self):
  arc=self.base/'archive/CA-R-1@4.md'; arc.parent.mkdir(); arc.write_text(atom('CA-R-1',4,'Archived'))
  plan=self.plan([],5); plan.write_text(json.dumps({'operations':[],'version_pins':[],'selected_versions':{'CA-R-1':5},'outputs':[]})); a.apply(self.root,plan,self.root/'r.json')
if __name__=='__main__':unittest.main()
