import numpy as np
import BrickWall_51 as bw
import ExactDiag_21 as ed
import Entropy as en
import matplotlib.pyplot as plt

# N = 6
# j,h = 1,1
# exactD = ed.exactDiag(N, j, h)
# psiTarget = exactD[2].reshape(tuple([2]*N))
# exactE = exactD[1]
# H = exactD[0]

def plotEnergy(psiTarget,approxStates,exactE,H):
	N = len(psiTarget.shape)
	fig, ax = plt.subplots()
	x = range(1,len(approxStates)+1)
	ax.plot([1,len(approxStates)],[exactE,exactE],'--k',label='Exact')
	ax.set_xlabel('Layers')
	ax.set_ylabel('Energy')
	E = []

	for approx in approxStates:
		approx = approx.flatten()
		E.append(np.vdot(approx,np.matmul(H,approx)))

	ax.plot(x,E,'o-',label='Approximation')
	ax.legend()
	fig.savefig('../plots/energyPlot.png',format='png')
	plt.show()

def plotOvelap(psiTarget,approxStates):
	N = len(psiTarget.shape)
	fig, ax = plt.subplots()
	x = range(1,len(approxStates)+1)
	ax.plot([1,len(approxStates)],[0,0],'--k',label='Exact')
	ax.set_xlabel('Layers')
	ax.set_ylabel('1-|Overlap|')
	overlap = []

	for approx in approxStates:
		approx = approx.flatten()
		overlap.append(np.abs(np.vdot(approx,psiTarget.flatten())))

	ax.plot(x,1-np.array(overlap),'o-',label='Approximation')
	ax.legend()
	fig.savefig('../plots/overlapPlot.png',format='png')
	plt.show()

def plotS(psiTarget,approxStates,layers):
	N = len(psiTarget.shape)
	bond = range(N+1)
	fig, ax = plt.subplots()
	enExact = [en.S(range(1,i+1), psiTarget) for i in bond]
	ax.plot(bond,enExact,'o-k', label='Exact')
	ax.set_xlabel('i bond')
	ax.set_ylabel('Entropy')

	for approx,layer in zip(approxStates,layers):
		enApprox = [en.S(range(1,i+1), approx) for i in bond]
		ax.plot(bond,enApprox,'o-',label=f'{layer} Layers')


	ax.legend()
	fig.savefig('../plots/entropyPlots.png',format='png')
	plt.show()

def plotMatrixI(psiTarget,approxStates,layers):
	N = len(psiTarget.shape)
	fig , axs = plt.subplots(1,len(approxStates)+1,layout='constrained')
	alpha = ['']+list(range(1,N+1))

	exact = en.matrixI(psiTarget)
	cax = axs[0].matshow(exact,cmap=plt.cm.Oranges)
	
	axs[0].set_xlabel('qubit')
	axs[0].set_ylabel('qubit')
	axs[0].set_xticklabels(alpha)
	axs[0].set_yticklabels(alpha)
	axs[0].set_title(f'Exact', weight='bold')

	for approx,layer in zip(approxStates,layers):
		matrixApprox = en.matrixI(approx) 

		axs[layer].matshow(matrixApprox,cmap=plt.cm.Oranges)
		axs[layer].set_title(f'Layers: {layer}', weight='bold')
		axs[layer].set_xticklabels([])
		axs[layer].set_yticklabels([])

	fig.colorbar(cax,location='left')
	fig.savefig('../plots/matrixCmPlots.png',format='png')
	plt.show()

def plotJ(psiTarget,approxStates,layers,log=False):
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

	for approx,layer in zip(approxStates,layers):
		approxJ = np.array([en.J(dist, approx) for dist in d])

		ax.plot(d,approxJ,'o-',label=f'Layers: {layer}')
		if log:
			ax.set_yscale('log')
			ax.set_xscale('log')	

	fig.savefig('../plots/JPlots.png',format='png')
	ax.legend()
	plt.show() 

def plotOvelap_sweeps(psiTarget,j,h,approxStatesRand,approxStatesId,layers):
	N = len(psiTarget.shape)
	fig, ax = plt.subplots(len(layers),2,layout='constrained')

	for approxRBach,approxIdBach,layer in zip(approxStatesRand,approxStatesId,layers):
		#layer = np.where(approxStatesRand==approxR)[0][0]+1
		for  approxR,approxId in zip(approxRBach,approxIdBach):
			overlapArray, criteria1, criteria2 = approxR
			ax[layer-1,0].plot(range(1,len(overlapArray)+1),1-overlapArray, '-b')
			if criteria1!=None:	
				ax[layer-1,0].plot(criteria1[0],1-criteria1[1],'xr')
			if criteria2!=None:	
				ax[layer-1,0].plot(criteria2[0],1-criteria2[1],'xg')
			ax[layer-1,0].set_yscale('log')
			ax[layer-1,0].set_xscale('log')
			ax[layer-1,0].set_ylabel('log(1-|Overlap|)')
			ax[layer-1,0].set_xlabel('log(sweeps)')

			overlapArray, criteria1, criteria2 = approxId
			ax[layer-1,1].plot(range(1,len(overlapArray)+1),1-overlapArray,'-b')
			if criteria1!=None:
				ax[layer-1,1].plot(criteria1[0],1-criteria1[1],'xr')
			if criteria2!=None:
				ax[layer-1,1].plot(criteria2[0],1-criteria2[1],'xg')
			ax[layer-1,1].set_yscale('log')
			ax[layer-1,1].set_xscale('log')
			ax[layer-1,1].set_ylabel('log(1-|Overlap|)')
			ax[layer-1,1].set_xlabel('log(sweeps)')

	ax[0,0].set_title('Random gates initialized')
	ax[0,1].set_title('Close to Id gates initialized')
	fig.set_size_inches(16,12)
	fig.savefig(f'../plots/{N}qb_params{j}{h}.png',format='png',dpi=100)
	plt.show()


#plotS(psiTarget,[1,2,3])
#plotMatrixI(psiTarget, [1,2,3])
#plotJ(psiTarget, [1,2,3],True)
#plotEnergy(psiTarget, exactE, H, 10)
#plotOvelap(psiTarget, 10)
#plotOvelap_sweeps(psiTarget,j,h, [1,2,3], 300, 10)
