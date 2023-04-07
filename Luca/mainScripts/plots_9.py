import numpy as np
import Entropy as en
import matplotlib.pyplot as plt

def plotEnergy(psiTarget,j,h,g,approxStates,exactE,H):
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
	fig.savefig(f'../plots/energyPlot{N}_{j}{h}{g}_{len(approxStates)}.pdf',format='pdf')
	plt.show()

def plotOvelap(psiTarget,j,h,g,approxStates):
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
	fig.savefig(f'../plots/overlapPlot{N}_{j}{h}{g}_{len(approxStates)}.pdf',format='pdf')
	plt.show()

def plotS(psiTarget,j,h,g,approxStates,layers):
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
	fig.savefig(f'../plots/entropyPlots{N}_{j}{h}{g}.pdf',format='pdf')
	plt.show()

def plotMatrixI(psiTarget,j,h,g,approxStates,layers):
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
	fig.savefig(f'../plots/matrixCmPlots{N}_{j}{h}{g}.pdf',format='pdf')
	plt.show()

def plotJ(psiTarget,j,h,g,approxStates,layers,log=False):
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
		if log:
			approxJ[np.abs(approxJ)<10**-12] = None
		print(approxJ)
		ax.plot(d,approxJ,'o-',label=f'Layers: {layer}')
		if log:
			ax.set_yscale('log')
			ax.set_xscale('log')	

	ax.legend()
	fig.savefig(f'../plots/JPlots{N}_{j}{h}{g}log={log}.pdf',format='pdf')
	plt.show() 

def plotOvelap_sweeps1(N,j,h,g,layers,approxStates1,approxStates2,GDvsPolar=False):
	fig, ax = plt.subplots(len(layers),2,layout='constrained')
	if len(layers) == 1:
		ax = np.array([ax])

	for approx1Bach,approx2Bach,layer in zip(approxStates1,approxStates2,layers):
		#layer = np.where(approxStates1==approxR)[0][0]+1
		for  approx1,approx2 in zip(approx1Bach,approx2Bach):
			overlapArray, criteria1, criteria2 = approx1
			ax[layers.index(layer),0].plot(range(1,len(overlapArray)+1),1-overlapArray, '-b')
			if criteria1!=None:	
				ax[layers.index(layer),0].plot(criteria1[0],1-criteria1[1],'xr')
			if criteria2!=None:	
				ax[layers.index(layer),0].plot(criteria2[0],1-criteria2[1],'xg')
			ax[layers.index(layer),0].set_yscale('log')
			ax[layers.index(layer),0].set_xscale('log')
			ax[layers.index(layer),0].set_ylabel('log(1-|Overlap|)')
			ax[layers.index(layer),0].set_xlabel('log(sweeps)')

			overlapArray, criteria1, criteria2 = approx2
			ax[layers.index(layer),1].plot(range(1,len(overlapArray)+1),1-overlapArray,'-b')
			if criteria1!=None:
				ax[layers.index(layer),1].plot(criteria1[0],1-criteria1[1],'xr')
			if criteria2!=None:
				ax[layers.index(layer),1].plot(criteria2[0],1-criteria2[1],'xg')
			ax[layers.index(layer),1].set_yscale('log')
			ax[layers.index(layer),1].set_xscale('log')
			ax[layers.index(layer),1].set_ylabel('log(1-|Overlap|)')
			ax[layers.index(layer),1].set_xlabel('log(sweeps)')

	ax[0,0].set_title('Polar method' if GDvsPolar else 'Random gates initialized')
	ax[0,1].set_title('Gradient descent method' if GDvsPolar else 'Close to Id gates initialized')
	fig.set_size_inches(12,8)
	fig.savefig(f'../plots/GDvsPolar{N}_{j}{h}{g}.pdf' if GDvsPolar else f'../plots/RandomVScloseToId{N}_{j}{h}{g}.pdf',format='pdf',dpi=100)
	plt.show()

def plotOvelap_sweeps2(approxStates,comapringDict):
	fig, ax = plt.subplots(1,len(approxStates),layout='constrained')

	for i in range(len(approxStates)):
		overlapArray, criteria1, criteria2 = approxStates[i]
		ax[i].plot(range(1,len(overlapArray)+1),1-overlapArray,'-b')
		if criteria1!=None:	
			ax[i].plot(criteria1[0],1-criteria1[1],'xr')
		if criteria2!=None:	
			ax[i].plot(criteria2[0],1-criteria2[1],'xg')
		ax[i].set_yscale('log')
		ax[i].set_xscale('log')
		ax[i].set_ylabel('log(1-|Overlap|)')
		ax[i].set_xlabel('log(sweeps)')

	for i in range(len(approxStates)):
		ax[i].set_title(f"{comapringDict['type']} {comapringDict['items'][i]}")


	plt.show()
	fig.set_size_inches(16,12)
	fig.savefig(f"../plots/Compare{comapringDict['type']}Using{comapringDict['optimization']}optimizationWithFixed_{comapringDict['fixed'][0]}_{comapringDict['fixed'][1]}.pdf",format='pdf',dpi=100)

def plotOvelap_sweeps3(approxState,i=''):
	fig,ax = plt.subplots()

	overlapArray, criteria1, criteria2 = approxState
	ax.plot(range(1,len(overlapArray)+1),1-overlapArray,'-b')
	if criteria1!=None:	
		ax.plot(criteria1[0],1-criteria1[1],'xr')
	if criteria2!=None:	
		ax.plot(criteria2[0],1-criteria2[1],'xg')
	ax.set_yscale('log')
	ax.set_xscale('log')
	ax.set_ylabel('log(1-|Overlap|)')
	ax.set_xlabel('log(sweeps)')
	

	plt.show()
	fig.set_size_inches(16,12)
	fig.savefig(f'../plots/PlotTesting{i}.pdf',format='pdf',dpi=100)


