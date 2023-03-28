import numpy as np

id = np.eye(2)
X = np.array([[0,1],[1,0]])
Y = 1j*np.array([[0,-1],[1,0]])
Z = np.array([[1,0],[0,-1]])
H = 1/np.sqrt(2)*np.array([[1,1],[1,-1]])
CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
RXX = np.cos(np.pi/8)*np.identity(4)-1j*np.sin(np.pi/8)*np.kron(np.array([[0,1],[0,-1]]),np.array([[0,1],[0,-1]]))