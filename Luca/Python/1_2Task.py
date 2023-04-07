import numpy as np
import usefulGates as g

#set up variables
J , h = (1.5,1)
g.id = np.eye(2)
g.X = np.array([[0,1], [1,0]])
g.Z = np.array([[1,0],[0,-1]])
XX = np.kron(g.X,g.X)
Zid = np.kron(g.Z,g.id)
idZ = np.kron(g.id,g.Z)
H = J*XX + h*(idZ+Zid)

E, M = np.linalg.eigh(H) #solve eigenvalue problem
#print(E,'\n',M)
E0 = E[0] #get groundstate and its associated energy
v0 = M[:,0]
print(E0,v0)
