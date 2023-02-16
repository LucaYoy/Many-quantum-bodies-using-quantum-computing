import numpy as np
import BrickWall_51 as bw
import ExactDiag_21 as ed
import Entropy as en

circuit = bw.BrickWallCircuit(3, 8)
psiTarget = ed.exactDiag(circuit.N, 1.5, 1)[1].reshape(tuple([2]*circuit.N))
#psiTarget = (1/np.sqrt(2))*np.array([1,0,0,1]).reshape(2,2)
print(en.computeEntropy(1, psiTarget))

#circuit.optimize(psiTarget,0.001,1000)