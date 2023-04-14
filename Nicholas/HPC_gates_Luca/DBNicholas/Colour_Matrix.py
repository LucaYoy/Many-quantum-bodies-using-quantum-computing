import Apply_gates as g
import Entanglement3 as et
import matplotlib.pyplot as plt
import ExactDiagonalization as ed

Qubits = 8
J = 1
h = 1.5
G = 0

phi = ed.exactDiagSparse(Qubits, J, h, G)[1]

matrix_phi,_,_ = et.mutual_info_matrix(phi)

fig, axs = plt.subplots(1, 6, figsize=(12,2), sharey=True)
fig.suptitle("Mutual Information Matrix")
fig.text(0.5, 0.01, 'Qubits', ha='center', va='center')
axs[0].set_ylabel('Qubit')

axs[0].set_xticks([0,Qubits-1])
axs[0].set_yticks([0, Qubits-1])

im1 = axs[0].imshow(matrix_phi, cmap='Greens')
axs[0].set_title('Exact')
axs[0].set_aspect('equal')
axs[0].set_xticks([])
axs[0].set_yticks([])

all_psi = []
for Layers in range(3,8):
    Circuit = g.Circuit(Qubits, Layers)
    psi = Circuit.brick_wall()
    all_psi.append(psi)
    
all_matrices = []
for psi in all_psi:
    matrix,_,_ = et.mutual_info_matrix(psi)
    all_matrices.append(matrix)
    
for i, matrix in enumerate(all_matrices):
    ax = axs[i+1]
    im = ax.imshow(matrix, cmap='Greens')
    ax.set_title(f'Layers = {i+3}')
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    

fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.10, 0.05, 0.7])
fig.colorbar(im1, cax=cbar_ax)
   
plt.show()