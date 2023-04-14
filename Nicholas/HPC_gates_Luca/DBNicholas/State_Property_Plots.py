import Entanglement3 as et
import matplotlib.pyplot as plt
import Apply_gates as g

Qubits = 8

# Generate psi
p = 3
all_psi = []
for Layers in range(p,8):
    Circuit = g.Circuit(Qubits, Layers)
    psi = Circuit.brick_wall()
    all_psi.append(psi)

import ExactDiagonalization as ed

#Generate phi
phi = ed.exactDiagSparse(Qubits, 1, 1.5, 0)[1]

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


plt.xlabel('Qubit')
plt.ylabel('Entropy')
plt.legend()
plt.show()