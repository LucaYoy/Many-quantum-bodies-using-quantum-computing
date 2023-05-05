import numpy as np
import Entropy as en
import matplotlib.pyplot as plt

def plotEnergy(psiTarget,j,h,g,exactE,EList,layers,H):
	N = len(psiTarget.shape)
	fig, ax = plt.subplots()
	x = layers
	ax.plot([x[0],x[-1]],[exactE,exactE],'--k',label='Exact')
	ax.set_xlabel('Layers')
	ax.set_ylabel('Energy')

	ax.plot(x,EList,'o-',label='Approximation')
	ax.legend()
	plt.rcParams['font.size'] = 10
	fig.set_size_inches(5.9,3.6)
	fig.savefig(f'../plots/energyPlot{N}_{j}{h}{g}.pdf',format='pdf')
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
	plt.rcParams['font.size'] = 10
	fig.set_size_inches(5.9,3.6)
	fig.savefig(f'../plots/overlapPlot{N}_{j}{h}{g}_{len(approxStates)}.pdf',format='pdf')
	plt.show()

def plotS(psiTarget,j,h,g,entropies,layers):
	N = len(psiTarget.shape)
	bond = range(N+1)
	fig, ax = plt.subplots()
	enExact = [en.S(range(1,i+1), psiTarget) for i in bond]
	ax.plot(bond,enExact,'o-k', label='Exact')
	ax.set_xlabel('i bond')
	ax.set_ylabel('Entropy')

	for entropyList,layer in zip(entropies,layers):
		ax.plot(bond,entropyList,'o-',label=f'{layer} Layers')


	ax.legend()
	plt.rcParams['font.size'] = 10
	fig.set_size_inches(5.9,3.6)
	fig.savefig(f'../plots/entropyPlots{N}_{j}{h}{g}.pdf',format='pdf')
	plt.show()

def plotMatrixI(psiTarget,j,h,g,Imatrices,layers):
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

	for i in range(len(layers)): 
		axs[i+1].matshow(Imatrices[i],cmap=plt.cm.Oranges)
		axs[i+1].set_title(f'Layers: {layers[i]}', weight='bold')
		axs[i+1].set_xticklabels([])
		axs[i+1].set_yticklabels([])

	fig.colorbar(cax,location='left')
	plt.rcParams['font.size'] = 10
	fig.set_size_inches(5.9,3.6)
	fig.savefig(f'../plots/matrixCmPlots{N}_{j}{h}{g}.pdf',format='pdf')
	plt.show()

def plotJ(psiTarget,j,h,g,Js,layers,log=False):
	N = len(psiTarget.shape)
	fig, ax  = plt.subplots()
	d = np.array(range(1,N))
	exactJ = np.array([en.J(dist, psiTarget) for dist in d])
	
	ax.plot(d,exactJ,'o-k',label='Exact')
	if log:
		ax.set_yscale('log')
		ax.set_xscale('log')
	
	ax.set_xlabel('d')
	ax.set_ylabel('J')

	for Jlist,layer in zip(Js,layers):
		if log:
			Jlist[np.abs(Jlist)<10**-12] = None
		# print(approxJ)
		ax.plot(d,Jlist,'o-',label=f'Layers: {layer}')
		if log:
			ax.set_yscale('log')
			ax.set_xscale('log')	

	ax.legend()
	plt.rcParams['font.size'] = 10
	fig.set_size_inches(5.9,3.6)
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

			overlapArray, criteria1, criteria2 = approx2
			ax[layers.index(layer),1].plot(range(1,len(overlapArray)+1),1-overlapArray,'-b')
			if criteria1!=None:
				ax[layers.index(layer),1].plot(criteria1[0],1-criteria1[1],'xr')
			if criteria2!=None:
				ax[layers.index(layer),1].plot(criteria2[0],1-criteria2[1],'xg')
			ax[layers.index(layer),1].set_yscale('log')
			ax[layers.index(layer),1].set_xscale('log')

	
	ax[0,0].set_xticks([10**0,10**2,10**4])
	ax[0,1].set_xticks([10**0,10**2,10**4])
	ax[0,0].set_ylabel('1-|Overlap|')
	ax[0,0].set_xlabel('sweeps')
	plt.rcParams['font.size'] = 10
	ax[0,0].set_title('Polar method' if GDvsPolar else 'Random gates initialized')
	ax[0,1].set_title('Gradient descent method' if GDvsPolar else 'Close to Id gates initialized')
	fig.set_size_inches(5.9,3.6)
	plt.show()
	fig.savefig(f'../plots/HPC_plots/GDvsPolar{N}_{j}{h}{g}.pdf' if GDvsPolar else f'../plots/HPC_plots/RandomVScloseToId{N}_{j}{h}{g}.pdf',format='pdf',dpi=100)

def plotOvelap_sweeps2(approxStates,comapringDict,i=''):
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
		ax[i].set_xticks([10**0,10**3,10**5])

	for i in range(len(approxStates)):
		ax[i].set_title(f"{comapringDict['type']} = {comapringDict['items'][i]}")
		ax[i].set_xticks([10**1,10**3,10**5])

	ax[0].set_yticks([10**-1,0.03])
	ax[0].set_yticklabels([0.1,0.03])
	ax[0].set_ylabel('1-|Overlap|')
	ax[0].set_xlabel('sweeps')
	plt.rcParams['font.size'] = 10
	fig.set_size_inches(5.9,3.6)
	plt.show()
	fig.savefig(f"../plots/HPC_plots/Compare{comapringDict['type']}Using{comapringDict['optimization']}optimizationWithFixed_{comapringDict['fixed'][0]}_{comapringDict['fixed'][1]}{i}.pdf",format='pdf',dpi=100)

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
	ax.set_ylabel('1-|Overlap|')
	ax.set_xlabel('sweeps')
	

	plt.rcParams['font.size'] = 10
	fig.set_size_inches(5.9,3.8)
	plt.show()
	fig.savefig(f'../plots/PlotTesting{i}.pdf',format='pdf',dpi=100)


