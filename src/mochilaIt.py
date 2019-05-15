def mochila(w,n):
	n=len(pesos)
	def dotVec(x,bs):
		s=0
		m=1
		for i in range(len(x)):
			if bs&m:s+=x[i]
			m<<=1
		return s
	ans=0
	for bs in range(2**n):
		if dotVec(pesos,bs)<=w:
			ans=max(ans,dotVec(valores,bs))
		# print(bin(bs)[2::])
	return ans
if __name__=="__main__":
	# pesos  =[5,4,3,6 ]
	# valores=[1,2,4,14]
	pesos=list(range(1,21))
	valores=list(range(1,21))
	n=len(pesos)
	print(mochila(1e100,n)) #14