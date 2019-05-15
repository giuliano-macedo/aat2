mem={}
def mochiladin(w , n): 
	if n == 0 or w == 0:return 0
	ans=mem.get((w,n),None)
	if ans!=None:return ans
	if pesos[n-1]>w: 
		ans=mochiladin(w , n-1) 
		mem[w,n]=ans
		return ans
	ans=max(valores[n-1] + mochiladin(w-pesos[n-1] , n-1), 
			   mochiladin(w , n-1)) 
	mem[w,n]=ans
	return ans
class Mochiladin:
	def __init__(self,pesos,valores):
		self.pesos=pesos
		self.valores=valores
		self.mem={}
		self.n=0
	def run(self,w,n):
		self.n+=1
		if n == 0 or w == 0:return 0
		ans=self.mem.get((w,n),None)
		if ans!=None:return ans
		if self.pesos[n-1]>w: 
			ans=self.run(w , n-1) 
			self.mem[w,n]=ans
			return ans
		ans=max(self.valores[n-1] + self.run(w-self.pesos[n-1] , n-1), 
				   self.run(w , n-1)) 
		self.mem[w,n]=ans
		return ans
if __name__=="__main__":
	pesos= [5,4,3,6]
	valores=[1,2,4,14]
	n=len(pesos)
	print(mochiladin(6,n))
	print(mochiladin(14,n))
	print(mochiladin(20,n))
	print(mochiladin(21,n))