import numpy as np
from functools import reduce
import usefulGates as g

def exactDiag(n,j,h):
	
	# sum1 = 0
	# sum2 = 0
	# for i in range(1,n):
	# 	iter1 = [g.id for k in range(i-1)]+[g.X,g.X]+[g.id for k in range(n-i-1)]
	# 	sum1 = sum1 + np.array(reduce(np.kron,iter1))

	# 	iter2 = [g.id for k in range(i-1)]+[g.Z]+[g.id for k in range(n-i)]
	# 	sum2 = sum2 + np.array(reduce(np.kron,iter2))
	# sum2 = sum2 + reduce(np.kron,[g.id for k in range(n-1)]+[g.Z])

	sum1 = np.sum([np.array(reduce(np.kron, [g.id for k in range(i-1)]+[g.X,g.X]+[g.id for k in range(n-i-1)])) for i in range(1,n)],axis = 0)
	sum2 = np.sum([np.array(reduce(np.kron, [g.id for k in range(i-1)]+[g.Z]+[g.id for k in range(n-i)])) for i in range(1,n+1)],axis = 0)

	H = j*sum1+h*sum2
	E, V = np.linalg.eigh(H)
	return E[0],V[:,0]

print(exactDiag(2, 1.5, 1))



