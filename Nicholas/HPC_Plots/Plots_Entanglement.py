# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 15:02:52 2023

@author: msyne
"""

import Entanglement3 as et
import matplotlib.pyplot as plt
import gate_restorer as gr
import ExactDiagonalization as ed

Qubits = 6
J = 1
H = 1
G = 1

phi = ed.exactDiagSparse(Qubits, J, H, G)[1]

entropies_exact_phi = []

for i in range(0, len(phi.shape)+1):
    
    entropy = et.compute_entropy(list(range(i)), phi)
    
    entropies_exact_phi.append(entropy)


Circuit = gr.Circuit(6, 5, 1, 1, 1)
phi = Circuit.finalpsi()

entropies_exact = []

for i in range(0, len(phi.shape)+1):
    
    entropy = et.compute_entropy(list(range(i)), phi)
    
    entropies_exact.append(entropy)

    
plt.plot(range(0, len(phi.shape)+1), entropies_exact, "-o", label="Target State")
plt.plot(range(0, len(phi.shape)+1), entropies_exact_phi, "-o", label="Target State")
plt.xlabel('Qubit')
plt.ylabel('Entropy')
plt.legend()
plt.show()