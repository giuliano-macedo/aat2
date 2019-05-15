from os import listdir
import os.path
from collections import namedtuple
from time import time
def readkp(filename):
	f=open(filename)
	state=0
	valores=[]
	pesos=[]
	for line in f.readlines():
		try:temp=[int(t)for t in line.strip().split(" ")]
		except Exception:continue
		if   state==0:
			n=temp[0]
			state+=1
		elif state==1:
			w=temp[0]
			state+=1
		else:
			valores.append(temp[0])
			pesos.append(temp[1])
	f.close()
	assert len(valores)==len(pesos)==n
	return w,valores,pesos
def readkps(directory):
	ans=[]
	KP=namedtuple("KP",["name","w","valores","pesos"])
	for filename in sorted(listdir(directory)):
		ans.append(KP(filename,*readkp(os.path.join(directory,filename))))
	return ans
def timeFunction(f,*args):
	start=time()
	ans=f(*args)
	return (time()-start,ans)
if __name__=="__main__":
	data=readkps("../instancias")
	for kp in data:
		print(kp.name,kp.w)