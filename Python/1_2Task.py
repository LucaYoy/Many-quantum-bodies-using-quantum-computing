import numpy as np

#set up variables
J , h = (1,1)
id = np.eye(2)
X = np.array([[0,1], [1,0]])
Z = np.array([[1,0],[0,-1]])
XX = np.kron(X,X)
Zid = np.kron(Z,id)
idZ = np.kron(id,Z)
H = J*XX + h*(idZ+Zid)

E, M = np.linalg.eigh(H) #solve eigenvalue problem
#print(E,'\n',M)
E0 = E[0] #get groundstate and its associated energy
v0 = M[:,0]
print(E0,v0)
