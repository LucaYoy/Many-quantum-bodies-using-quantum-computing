import numpy as np
import BrickWall_51 as bw
import ExactDiag_21 as ed
import Entropy as en

circuit = bw.BrickWallCircuit(8,1, gatesRandomFlag=False)
psiTarget = ed.exactDiag(circuit.N, 1.5, 1)[1].reshape(tuple([2]*circuit.N))
#psiTarget = (1/np.sqrt(2))*np.array([1,0,0,1]).reshape(2,2) #bell state
# A = [1,4,5]
# B = [2]

# entropy = en.S([1,4,5], psiTarget)
# print(entropy)

# mutualI = en.I(A,B, psiTarget)
# print(mutualI)

# print(np.array(en.matrixI(psiTarget)))

circuit.optimize(psiTarget,0.000001,200)