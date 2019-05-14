items={(1,5),(2,4),(4,3),(14,6)} #valor -> peso
def mochila(w):
	if w<=0:return -float("inf")
	if w==4:return 2
	a= max([valor+mochila(w-peso) for valor,peso in items])
	return a
if __name__=="__main__":
	print(mochila(6)) #14
	print(mochila(15)) #20
	print(mochila(20)) #21