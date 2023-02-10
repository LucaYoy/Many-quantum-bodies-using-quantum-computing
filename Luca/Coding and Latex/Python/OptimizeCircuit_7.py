import numpy as np
import BrickWall_51 as bw
import ExactDiag_21 as ed

circuit = bw.BrickWallCircuit(3, 8)
psiTarget = ed.exactDiag(circuit.N, 1.5, 1)[1].reshape(tuple([2]*circuit.N))

circuit.optimize(psiTarget,0.001,1000)
