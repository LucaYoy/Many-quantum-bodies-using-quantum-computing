import numpy as np
import Gates as g

def exactDiagonalization(n,J,h):
    
    H = np.zeros((2**n,2**n))
    
    sum1 = 0
    sum2 = 0
    
    for i in range(1,n):
        
        sum1 += -J * np.kron(np.kron(np.eye(2**(i-1)),g.X) ,np.kron(g.X,np.eye(2**(n-i-1))))
        
    for i in range(1,n+1):
        
        sum2 += h * np.kron(np.eye(2**(i-1)), np.kron(g.Z, np.eye(2**(n-i))))
        
    H = sum1 + sum2
    
    _, V = np.linalg.eigh(H)
    
    return V[:,0].reshape(tuple([2]*n))

if __name__ == "__main__":

    p = exactDiagonalization(4, 1, 1)
    
    
