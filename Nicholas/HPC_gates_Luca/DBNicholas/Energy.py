import Apply_gates as g
import matplotlib.pyplot as plt
import ExactDiagonalization as ed
import numpy as np

Qubits = 8
J = 1
h = 1
G = 0


phi,_ , H = ed.exactDiagSparse(Qubits, J, h, G)

#all_psi = []
#energies = []
#for Layers in range(3,8):
    

Circuit = g.Circuit(Qubits, 3)
psi = Circuit.brick_wall()
psi = psi.flatten()
#all_psi.append(psi)
print(psi.shape)
print(H.shape)

p = np.matmul(H, psi)
P = np.vdot(psi, p.conj())
#E = np.vdot(psi, np.matmul(H, psi.conj()))
#energies.append(E)