import numpy as np
import BrickWall_51 as bw
import ExactDiag_21 as ed
import Entropy as en
import matplotlib.pyplot as plt

N = 8
bond = range(N+1)
psiTarget = ed.exactDiag(N, 1, 0.5)[1].reshape(tuple([2]*N))

fig, ax = plt.subplots()
enExact = [en.S(range(1,i+1), psiTarget) for i in bond]
ax.plot(bond,enExact,'o-k', label='Exact')
ax.set_xlabel('i bond')
ax.set_ylabel('Entropy')

for layer in range(1,4):
	circuit = bw.BrickWallCircuit(8, layer)
	approx = circuit.optimize(psiTarget,0.00001,1000)

	enApprox = [en.S(range(1,i+1), approx) for i in bond]

	ax.plot(bond,enApprox,'o-', label=f'{layer} Layers')


ax.legend()
fig.savefig('../plots/entropyPlots.png',format='png')
plt.show()