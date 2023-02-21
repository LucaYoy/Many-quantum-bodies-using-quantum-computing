import numpy as np
import Gates as g

def exactDiagonalization(n,J,h):
    
    H = np.zeros((2**n,2**n))
    
    for i in range(1,n):
        
        H += -J * np.kron(np.kron(np.eye(2**(i-1)),g.X) ,np.kron(g.X,np.eye(2**(n-i-1))))
        
        H += h * np.kron(np.eye(2**(i)), np.kron(g.Z, np.eye(2**(n-i-1))))
    
    _, V = np.linalg.eigh(H)
    
    return V[:,0].reshape(tuple([2]*n))


if __name__ == "__main__":

    H = exactDiagonalization(3,1,0)

    E,V = np.linalg.eigh(H)
    
    
