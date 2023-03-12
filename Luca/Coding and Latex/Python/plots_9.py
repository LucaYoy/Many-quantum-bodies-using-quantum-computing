import numpy as np
import BrickWall_51 as bw
import ExactDiag_21 as ed
import Entropy as en
import matplotlib.pyplot as plt

N = 8
exactD = ed.exactDiag(N, 1, 0.5)
psiTarget = exactD[2].reshape(tuple([2]*N))
exactE = exactD[1]
H = exactD[0]

def plotEnergy(psiTarget,exactE,H,maxLayers):
	N = len(psiTarget.shape)
	fig, ax = plt.subplots()
	x = range(1,maxLayers+1)
	ax.plot([1,maxLayers],[exactE,exactE],'--k',label='Exact')
	ax.set_xlabel('Layers')
	ax.set_ylabel('Energy')
	E = []

	for layer in x:
		circuit = bw.BrickWallCircuit(N, layer)
		approx = circuit.optimize(psiTarget,0.00001,1000).flatten()
		E.append(np.vdot(approx,np.matmul(H,approx)))

	ax.plot(x,E,'o-',label='Approximation')
	ax.legend()
	fig.savefig('../plots/energyPlot.png',format='png')
	plt.show()

def plotOvelap(psiTarget,maxLayers):
	N = len(psiTarget.shape)
	fig, ax = plt.subplots()
	x = range(1,maxLayers+1)
	ax.plot([1,maxLayers],[0,0],'--k',label='Exact')
	ax.set_xlabel('Layers')
	ax.set_ylabel('1-|Overlap|')
	overlap = []

	for layer in x:
		circuit = bw.BrickWallCircuit(N, layer)
		approx = circuit.optimize(psiTarget,0.00001,1000).flatten()
		overlap.append(np.abs(np.vdot(approx,psiTarget.flatten())))

	ax.plot(x,1-np.array(overlap),'o-',label='Approximation')
	ax.legend()
	fig.savefig('../plots/overlapPlot.png',format='png')
	plt.show()

def plotS(psiTarget,layers):
	N = len(psiTarget.shape)
	bond = range(N+1)
	fig, ax = plt.subplots()
	enExact = [en.S(range(1,i+1), psiTarget) for i in bond]
	ax.plot(bond,enExact,'o-k', label='Exact')
	ax.set_xlabel('i bond')
	ax.set_ylabel('Entropy')

	for layer in layers:
		circuit = bw.BrickWallCircuit(N, layer)
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

def plotJ(psiTarget,layers,log=False):
	N = len(psiTarget.shape)
	fig, ax  = plt.subplots()
	d = np.array(range(1,N))
	exactJ = np.array([en.J(dist, psiTarget) for dist in d])
	
	ax.plot(d,exactJ,'o-k',label='Exact')
	if log:
		ax.set_yscale('log')
		ax.set_xscale('log')
		ax.set_xlabel('log(d)')
		ax.set_ylabel('log(J)')
	else:
		ax.set_xlabel('d')
		ax.set_ylabel('J')

	for layer in layers:
		circuit = bw.BrickWallCircuit(N, layer)
		approx = circuit.optimize(psiTarget,0.00001,1000)
		approxJ = np.array([en.J(dist, approx) for dist in d])

		ax.plot(d,approxJ,'o-',label=f'Layers: {layer}')
		if log:
			ax.set_yscale('log')
			ax.set_xscale('log')	

	fig.savefig('../plots/JPlots.png',format='png')
	ax.legend()
	plt.show() 

#plotS(psiTarget,[1,2,3])
#plotMatrixI(psiTarget, [1,2,3])
#plotJ(psiTarget, [1,2,3],False)
#plotEnergy(psiTarget, exactE, H, 6)
#plotOvelap(psiTarget, 10)