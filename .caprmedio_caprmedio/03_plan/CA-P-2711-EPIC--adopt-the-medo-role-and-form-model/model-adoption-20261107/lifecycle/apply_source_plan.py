"""One-off sealed source-plan applier; caller supplies a reviewed JSON plan."""
import hashlib,json,os,re,tempfile
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[5]
sys.path.insert(0,str(ROOT/'LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS'))
from atom_operations import atom_identity_lock
def sha(x): return hashlib.sha256(x).hexdigest() if x is not None else None
def safe(root,value):
 p=Path(value)
 if p.is_absolute() or '..' in p.parts or p.suffix!='.md' or not str(p).startswith('.caprmedio_caprmedio/CA-SU-'): raise ValueError('unsafe source path')
 q=root/p
 chain=[]; x=q
 while x != root:
  chain.append(x); x=x.parent
 if any(x.is_symlink() for x in chain): raise ValueError('symlink path')
 return q
def pin_safe(root,value):
 p=Path(value)
 if p.is_absolute() or '..' in p.parts or p.suffix!='.md' or not str(p).startswith('.caprmedio_caprmedio/'): raise ValueError('unsafe pin path')
 q=root/p
 chain=[]; x=q
 while x != root: chain.append(x); x=x.parent
 if any(x.is_symlink() for x in chain): raise ValueError('symlink pin')
 return q
def versions(root):
 out={}
 for p in (root/'.caprmedio_caprmedio').rglob('*.md'):
  t=p.read_text(errors='ignore'); e=t.find('\n---\n',4); t=t[4:e] if t.startswith('---\n') and e>0 else ''
  i=re.search(r'(?m)^(?:atom_id|\s+(?:id|atom_id)):\s*(CA-[A-Z]-\d+)\s*$',t); v=re.search(r'(?m)^(?:version|\s+version):\s*(\d+)\s*$',t)
  if i and v: out.setdefault(i.group(1),[]).append((p.relative_to(root).as_posix(),sha(p.read_bytes()),int(v.group(1))))
 return out
def write_atomic(path,data,mode):
 path.parent.mkdir(parents=True,exist_ok=True)
 fd,tmp=tempfile.mkstemp(dir=path.parent)
 try:
  with os.fdopen(fd,'wb') as stream:
   stream.write(data);stream.flush();os.fsync(stream.fileno())
  os.chmod(tmp,mode);os.replace(tmp,path)
 finally:
  if os.path.exists(tmp):os.unlink(tmp)
def apply(root,plan_path,receipt_path):
 plan=json.loads(Path(plan_path).read_text()); ops=plan['operations']; seen=set()
 if Path(receipt_path).exists(): raise ValueError('receipt exists')
 with atom_identity_lock(root):
  observed=versions(root)
  for i,n in plan['selected_versions'].items():
   if n!=max((x[2] for x in observed.get(i,[])),default=0)+1: raise ValueError('version footprint drift '+i)
  expected={}
  for pin in plan['version_pins']:
   p=pin_safe(root,pin['path']); raw=p.read_bytes();
   if sha(raw)!=pin['sha256']: raise ValueError('version pin drift')
   expected.setdefault(pin['atom_id'],[]).append((pin['path'],pin['sha256'],pin['version']))
  for i,rows in expected.items():
   if sorted(rows)!=sorted(observed.get(i,[])): raise ValueError('exact version footprint drift '+i)
  for o in ops:
   p=safe(root,o['path']);
   if o['path'] in seen: raise ValueError('duplicate path')
   seen.add(o['path']); raw=p.read_bytes() if p.exists() else None
   if sha(raw)!=o['before_sha256'] or (raw.decode() if raw else None)!=o['before']: raise ValueError('preimage drift')
   if sha(o['after'].encode() if o['after'] is not None else None)!=o['after_sha256']: raise ValueError('after hash')
  done=[];modes={}
  for o in ops:
   p=safe(root,o['path']);modes[o['path']]=(p.stat().st_mode & 0o777) if p.exists() else None
   if o.get('before_mode',modes[o['path']])!=modes[o['path']]:raise ValueError('mode drift')
  try:
   for o in ops:
    p=safe(root,o['path']); raw=p.read_bytes() if p.exists() else None
    if sha(raw)!=o['before_sha256']: raise ValueError('concurrent drift')
    if o['after'] is None:
     # Check every published source/archive before removing a sealed preimage.
     for prior in done:
      q=safe(root,prior['path'])
      if sha(q.read_bytes() if q.exists() else None)!=prior['after_sha256']:raise ValueError('publication readback drift')
     if sha(p.read_bytes())!=o['before_sha256']: raise ValueError('pre-delete readback drift')
    done.append(o)
    if o['after'] is None:
     p.unlink()
    else:
     write_atomic(p,o['after'].encode(),o.get('after_mode',modes[o['path']] or 0o644))
   for o in ops:
    p=safe(root,o['path']); assert sha(p.read_bytes() if p.exists() else None)==o['after_sha256']
  except BaseException:
   for o in reversed(done):
    p=safe(root,o['path']); raw=p.read_bytes() if p.exists() else None
    if sha(raw)==o['before_sha256']:continue
    if sha(raw)!=o['after_sha256']: raise RuntimeError('rollback external drift')
    if o['before'] is None: p.unlink()
    else: write_atomic(p,o['before'].encode(),modes[o['path']])
   raise
 with Path(receipt_path).open('x') as stream:
  stream.write(json.dumps({'status':'SOURCE_ADOPTION_APPLIED_VERIFIED','plan_sha256':sha(Path(plan_path).read_bytes()),'run':False,'journal_append':False,'outputs':plan.get('outputs',[])},indent=2)+'\n')
