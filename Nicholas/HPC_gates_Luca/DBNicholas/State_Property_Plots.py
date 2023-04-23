import Entanglement3 as et
import matplotlib.pyplot as plt
import Apply_gates as g
import time 
start_time = time.time()

Qubits = 12
J = 1
h = 1
G = 1

# Generate psi
p = 3
all_psi = []
for Layers in range(p,8):
    Circuit = g.Circuit(Qubits, Layers)
    psi = Circuit.brick_wall()
    all_psi.append(psi)

import ExactDiagonalization as ed

#Generate phi
phi = ed.exactDiagSparse(Qubits, J, h, G)[1]

entropies_phi = []

for i in range(0, len(phi.shape)+1):
    
    entropy = et.compute_entropy(list(range(i)), phi)
    
    entropies_phi.append(entropy)

plt.plot(range(0, len(phi.shape)+1), entropies_phi, '-o', label='Target State')


for i,psi in enumerate(all_psi):
    
    entropies_psi = []
    
    for j in range(0, len(psi.shape)+1):
    
        entropy = et.compute_entropy(list(range(j)), psi)
        
        entropies_psi.append(entropy)

    plt.plot(range(0, len(psi.shape)+1), entropies_psi, '-o', label=f'{i+p} Layers')
title = f"Entanglement Entropy for {Qubits} Qubits, J = {J}, h = {h}, G = {G}"
plt.title(f"Entanglement Entropy for {Qubits} Qubits, J = {J}, h = {h}, G = {G}")
plt.xlabel('Qubit')
plt.ylabel('Entropy')
plt.legend()

import os

if not os.path.exists("Plots"):
    os.makedirs("Plots")
    
if not os.path.exists(f"Plots/{title}.png"):
    plt.savefig(f"Plots/{title}.png")    
    
plt.show()

print ("Took", time.time() - start_time, "seconds to run")
    
    
    
