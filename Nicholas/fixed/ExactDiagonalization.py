import numpy as np
import Gates as g

def exactDiagonalization(n,J,h,G):
    
    H = np.zeros((2**n,2**n))
    
    sum1 = 0
    sum2 = 0
    sum3 = 0
    
    for i in range(1,n):
        
        sum1 += -J * np.kron(np.kron(np.eye(2**(i-1)),g.X) ,np.kron(g.X,np.eye(2**(n-i-1))))
        
    for i in range(1,n+1):
        
        sum2 += h * np.kron(np.eye(2**(i-1)), np.kron(g.Z, np.eye(2**(n-i))))
        
    for i in range(1,n+1):
        
        sum3 += G * np.kron(np.eye(2**(i-1)), np.kron(g.X, np.eye(2**(n-i))))
        
    H = sum1 + sum2 + sum3
    
    E, V = np.linalg.eigh(H)
    
    return E[0], V[:,0].reshape(tuple([2]*n)), H


# Also add the exact diagonalization sparse approach

import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

def exactDiagSparse(n,j,h,G):

    H = sp.csc_matrix((2**n,2**n))

    for i in range(1,n-1):
        H += j*sp.kron(sp.kron(sp.eye(2**i),sp.kron(g.X,g.X)),sp.eye(2**(n-i-2)))

    for i in range(1,n):
        H += h*sp.kron(sp.kron(sp.eye(2**i),g.Z),sp.eye(2**(n-i-1)))

    for i in range(1,n):
        H += G*sp.kron(sp.kron(sp.eye(2**i),g.X),sp.eye(2**(n-i-1)))

    E, V = eigsh(H, k=1, which='SA')  # we only need the lowest eigenvalue / eigenvector

    return E[0],V[:,0].reshape(tuple([2]*n)), H


#if __name__ == "__main__":

    #p = exactDiagonalization(4, 1, 1, 1)
    
    #q = exactDiagSparse(4, 1, 1, 1)
    
    
