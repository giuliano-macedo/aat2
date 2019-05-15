def mochila(w , n): 
	if n == 0 or w == 0:return 0
	if(pesos[n-1]>w): return mochila(w , n-1) 
	return max(valores[n-1] + mochila(w-pesos[n-1] , n-1), 
			   mochila(w , n-1)) 
if __name__=="__main__":
	# pesos= [5,4,3,6]
	# valores=[1,2,4,14]
	pesos=list(range(1,21))
	valores=list(range(1,21))
	n=len(pesos)
	print(mochila(1e100,n))