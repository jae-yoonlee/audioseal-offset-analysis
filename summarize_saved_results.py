"""Recompute paper counts from saved selections; no model inference."""
from pathlib import Path
import argparse,csv,json,hashlib
import numpy as np

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--input',type=Path,default=Path('selected_results.csv'))
 p.add_argument('--output',type=Path,default=Path('computed'))
 args=p.parse_args();rows=list(csv.DictReader(args.input.open(encoding='utf-8-sig',newline='')))
 seen=set()
 for row in rows:
  key=tuple(row[x] for x in ('file','r','K','method','kind'))
  assert key not in seen,('duplicate',key)
  seen.add(key)
  gate=float(row['selected_q'])>.5
  assert gate==bool(int(row['selected_gate'])),('gate',key)
  bits=row['bits'];assert len(bits)==16 and set(bits)<=set('01')
  if row['kind']=='full_watermark':
   truth=row['truth_bits'];assert len(truth)==16 and set(truth)<=set('01')
   errors=sum(a!=b for a,b in zip(bits,truth))
   assert errors==int(float(row['errors'])),('errors',key)
   assert (errors==0)==bool(int(float(row['exact']))),('exact',key)
   assert (gate and errors==0)==bool(int(float(row['joint_selected']))),('joint',key)
 assert len(rows)==6400,len(rows)
 out=[]
 for scope in ('all','r0','r_positive'):
  for k in (1,4,16,64,320):
   for method in ('q','margin'):
    a=[r for r in rows if r['kind']=='full_watermark' and int(r['K'])==k and r['method']==method and (scope=='all' or (int(r['r'])==0 if scope=='r0' else int(r['r'])>0))]
    assert len(a)=={'all':320,'r0':20,'r_positive':300}[scope]
    detected=sum(float(r['selected_q'])>.5 for r in a)
    exact=sum(int(float(r['exact'])) for r in a)
    wrong=sum(float(r['selected_q'])>.5 and int(float(r['errors']))>0 for r in a)
    errors=sum(int(float(r['errors'])) for r in a)
    out.append(dict(scope=scope,K=k,method=method,n=len(a),detected=detected,exact=exact,detected_wrong=wrong,BER=errors/(len(a)*16)))
 a=[r for r in rows if r['kind']=='full_watermark' and int(r['K'])==1 and r['method']=='q' and int(r['r'])>0]
 speakers=sorted({r['speaker'] for r in a});assert len(speakers)==10
 per_speaker=np.array([np.mean([float(r['selected_q'])>.5 and int(float(r['errors']))>0 for r in a if r['speaker']==s]) for s in speakers])
 # This reproduces the saved detected-wrong analysis, not the earlier primary-comparison seed.
 rng=np.random.default_rng(20261019)
 ci=np.quantile(per_speaker[rng.integers(0,len(speakers),(10000,len(speakers)))].mean(axis=1),[.025,.975])
 args.output.mkdir(parents=True,exist_ok=True)
 with (args.output/'summary.csv').open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=out[0]);w.writeheader();w.writerows(out)
 report={'checked_selection_rows':len(rows),'input_sha256':hashlib.sha256(args.input.read_bytes()).hexdigest(),'speakers':speakers,'detected_wrong_r_positive_K1':float(per_speaker.mean()),'CI95':ci.tolist(),'bootstrap_seed':20261019,'bootstrap_replicates':10000,'model_inference_performed':False}
 (args.output/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
 print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
