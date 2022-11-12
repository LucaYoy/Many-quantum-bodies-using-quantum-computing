import numpy as np
from functools import reduce

def exactDiag(n,j,h):
	id = np.eye(2)
	X = np.array([[0,1],[1,0]])
	Z = np.array([[1,0],[0,-1]])
	sum1 = 0
	sum2 = 0

	for i in range(1,n):
		iter1 = [id for k in range(i-1)]+[X,X]+[id for k in range(n-i-1)]
		sum1 = sum1 + np.array(reduce(np.kron,iter1))

		iter2 = [id for k in range(i-1)]+[Z]+[id for k in range(n-i)]
		sum2 = sum2 + np.array(reduce(np.kron,iter2))
	sum2 = sum2 + reduce(np.kron,[id for k in range(n-1)]+[Z])

	H = j*sum1+h*sum2
	E, V = np.linalg.eigh(H)
	return E[0],V[:,0]

print(exactDiag(10, 0, 1))



