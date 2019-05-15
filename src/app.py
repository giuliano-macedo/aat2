from utils import readkps,timeFunction
from mochiladin import Mochiladin
from multiprocessing import Pool
import json
kps=readkps("../instancias")
def worker(args):
	i,mochilaobj=args
	name=kps[i].name
	t,ans=timeFunction(mochilaobj.run,kps[i].w,len(kps[i].valores))
	it=mochilaobj.n
	return name,t,it,ans
mochilas=[(i,Mochiladin(kp.pesos,kp.valores)) for i,kp in enumerate(kps)]
pool=Pool(8)
print("gerando arquivo result.json...")
data={}
for name,t,it,ans in pool.map(worker,mochilas):
	data[name]={"t":t,"it":it,"ans":ans}
with open("result.json","w") as f:f.write(json.dumps(data,indent=4))
print("pronto")