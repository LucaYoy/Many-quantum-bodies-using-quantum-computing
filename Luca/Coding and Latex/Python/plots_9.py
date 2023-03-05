import numpy as np
import BrickWall_51 as bw
import ExactDiag_21 as ed
import Entropy as en
import matplotlib.pyplot as plt

N = 8
psiTarget = ed.exactDiag(N, 1, 0.5)[1].reshape(tuple([2]*N))

def plotS(psiTarget,layers):
	bond = range(len(psiTarget.shape)+1)
	fig, ax = plt.subplots()
	enExact = [en.S(range(1,i+1), psiTarget) for i in bond]
	ax.plot(bond,enExact,'o-k', label='Exact')
	ax.set_xlabel('i bond')
	ax.set_ylabel('Entropy')

	for layer in layers:
		circuit = bw.BrickWallCircuit(8, layer)
		approx = circuit.optimize(psiTarget,0.00001,1000)

		enApprox = [en.S(range(1,i+1), approx) for i in bond]

		ax.plot(bond,enApprox,'o-', label=f'{layer} Layers')


	ax.legend()
	fig.savefig('../plots/entropyPlots.png',format='png')
	plt.show()

def plotMatrixI(psiTarget,layers):
	N = len(psiTarget.shape)
	fig , axs = plt.subplots(1,len(layers)+1,layout='constrained')
	alpha = ['']+list(range(1,N+1))

	exact = en.matrixI(psiTarget)
	cax = axs[0].matshow(exact,cmap=plt.cm.Oranges)
	
	axs[0].set_xlabel('qubit')
	axs[0].set_ylabel('qubit')
	axs[0].set_xticklabels(alpha)
	axs[0].set_yticklabels(alpha)
	axs[0].set_title(f'Exact', weight='bold')

	for layer in layers:
		circuit = bw.BrickWallCircuit(8, layer)
		approx = circuit.optimize(psiTarget,0.00001,1000)
		matrixApprox = en.matrixI(approx) 

		axs[layer].matshow(matrixApprox,cmap=plt.cm.Oranges)
		axs[layer].set_title(f'Layers: {layer}', weight='bold')
		axs[layer].set_xticklabels([])
		axs[layer].set_yticklabels([])

	fig.colorbar(cax,location='left')
	fig.savefig('../plots/matrixCmPlots.png',format='png')
	plt.show()


#plotS(psiTarget,[1,2,3])
plotMatrixI(psiTarget, [1,2,3])