import Apply_gates as g
import Entanglement3 as et
import matplotlib.pyplot as plt
import ExactDiagonalization as ed

Qubits = 14
J = 1
h = 1
G = 1

phi = ed.exactDiagSparse(Qubits, J, h, G)[1]

I_matrix, abs_d, sum_I = et.mutual_info_matrix(phi)

all_psi = []
for Layers in range(3,8):
    Circuit = g.Circuit(Qubits, Layers)
    psi = Circuit.brick_wall()
    all_psi.append(psi)
    
plt.plot(abs_d[:7], sum_I[:7], "-o", label="Target State")

for i, psi in enumerate(all_psi):
    I_matrix, abs_d, sum_I = et.mutual_info_matrix(psi)
    if (abs(sum_I) > 10**-5).any():
        sum_I[abs(sum_I) <= 10**-5] = None
        plt.plot(abs_d[:7], sum_I[:7], "-o", label=f"{i+3} Layers")


#plt.xscale("log")
plt.yscale("log")
plt.xlabel('d')
plt.ylabel('J')
plt.title(f'{Qubits} Qubits, J={J}, h={h}, G={G}')
plt.xticks(range(1,8, 1))
plt.ylim(0, 10)
plt.legend()

title = f'{Qubits} Qubits, J={J}, h={h}, G={G} mutual info'

import os

if not os.path.exists(f"Plots/{title}.png"):
    plt.savefig(f"Plots/{title}.png") 

   
plt.show()