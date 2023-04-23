import matplotlib.pyplot as plt
import Renyi_entropy as re
import ExactDiagonalization as ed
import BrickWall as bw

Qubits = 8
J = 1
H = 1.5
G = 0


phi = ed.exactDiagSparse(Qubits, J, H, G)[1]

for alpha in range(2,7):
    entropies = []
    for i in range(0, len(phi.shape)+1):
    
        entropy = re.compute_renyi_entropy(list(range(i)), phi, alpha)
        entropies.append(entropy)
        
    plt.plot(range(0, len(phi.shape)+1), entropies, "-o", label=f"{alpha}")

plt.xlabel('Qubit')
plt.ylabel('Entropy')
plt.title(f'alpha = {alpha}')
plt.legend()
plt.show()
        
    