import numpy as np
from functools import reduce
import usefulGates as gt

def exactDiag(n,j,h,g):
	
	# sum1 = 0
	# sum2 = 0
	# for i in range(1,n):
	# 	iter1 = [g.id for k in range(i-1)]+[g.X,g.X]+[g.id for k in range(n-i-1)]
	# 	sum1 = sum1 + np.array(reduce(np.kron,iter1))

	# 	iter2 = [g.id for k in range(i-1)]+[g.Z]+[g.id for k in range(n-i)]
	# 	sum2 = sum2 + np.array(reduce(np.kron,iter2))
	# sum2 = sum2 + reduce(np.kron,[g.id for k in range(n-1)]+[g.Z])

	sum1 = np.sum([np.array(reduce(np.kron, [gt.id for k in range(i-1)]+[gt.X,gt.X]+[gt.id for k in range(n-i-1)])) for i in range(1,n)],axis = 0) #Ising
	sum2 = np.sum([np.array(reduce(np.kron, [gt.id for k in range(i-1)]+[gt.Z]+[gt.id for k in range(n-i)])) for i in range(1,n+1)],axis = 0) #Transverse
	sum3 = np.sum([np.array(reduce(np.kron, [gt.id for k in range(i-1)]+[gt.X]+[gt.id for k in range(n-i)])) for i in range(1,n+1)],axis = 0) #Longitudinal

	H = j*sum1+h*sum2+g*sum3
	E, V = np.linalg.eigh(H)
	return H,E[0],V[:,0]

#print(exactDiag(2, 1.5, 1,0))



