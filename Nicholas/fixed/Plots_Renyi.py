import matplotlib.pyplot as plt
import Renyi_entropy as re
import ExactDiagonalization as ed
import BrickWall as bw

Qubits = 8
J = 1
H = 1
G = 0
alpha = 0

#phi = ed.exactDiagonalization(Qubits, J, H, G)[1]
phi = ed.exactDiagSparse(Qubits, J, H, G)[1]

entropies_exact = []

for i in range(0, len(phi.shape)+1):
    
    entropy = re.compute_renyi_entropy(list(range(i)), phi, alpha)
    
    entropies_exact.append(entropy)
    
for Layers in range(1,4):
    entropies = []
    Circuit = bw.Circuit(Qubits, Layers, J, H, G, gatesrandom=False)
    psi=Circuit.optimize_circuit(200,10**-4, True, True, True, False)[2]
    
    for i in range(0, len(psi.shape)+1):
        entropy = re.compute_renyi_entropy((range(i)), psi, alpha)
        entropies.append(entropy)
    
    plt.plot(range(0, len(psi.shape)+1), entropies, "-o", label=f"{Layers} Layers")
    
plt.plot(range(0, len(phi.shape)+1), entropies_exact, "-o", label="Target State")

plt.xlabel('Qubit')
plt.ylabel('Entropy')
plt.title(f'alpha = {alpha}')
plt.legend()
plt.show()
