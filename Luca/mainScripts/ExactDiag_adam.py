import numpy as np
from functools import reduce
import usefulGates as gt

# exact diag using numpy
def exactDiag(n,j,h,g):

    H = np.zeros((2**n,2**n))

    for i in range(n-1):
        H += j*np.kron(np.kron(np.eye(2**i),np.kron(gt.X,gt.X)),np.eye(2**(n-i-2)))  # Ising

    for i in range(n):
        H += h*np.kron(np.kron(np.eye(2**i),gt.Z),np.eye(2**(n-i-1)))  # Transverse

    for i in range(n):
        H += g*np.kron(np.kron(np.eye(2**i),gt.X),np.eye(2**(n-i-1)))  # Longitudinal

    E, V = np.linalg.eigh(H)   
    
    return H,E[0],V[:,0]


# exact diag using sparse matrices
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

def exactDiagSparse(n,j,h,g):

    H = sp.csc_matrix((2**n,2**n))

    for i in range(n-1):
        H += j*sp.kron(sp.kron(sp.eye(2**i),sp.kron(gt.X,gt.X)),sp.eye(2**(n-i-2)))

    for i in range(n):
        H += h*sp.kron(sp.kron(sp.eye(2**i),gt.Z),sp.eye(2**(n-i-1)))

    for i in range(n):
        H += g*sp.kron(sp.kron(sp.eye(2**i),gt.X),sp.eye(2**(n-i-1)))

    E, V = eigsh(H, k=1, which='SA')  # we only need the lowest eigenvalue / eigenvector

    return H,E[0],V[:,0]





