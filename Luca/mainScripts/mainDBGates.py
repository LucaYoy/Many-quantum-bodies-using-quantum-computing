import pickle
import os
import BrickWall_51 as bw

for h,g in zip([1,1,1.5],[1,0,0]):
	for N in [8,10,12,14]:
		for M in [3,4,5,6,7]:
			f = open(f'pklFiles/DB/approxOptimizedCircuit1{h}{g}_{N}_{M}_.pkl','rb')
			i = open(f'pklFiles/DBNicholas/optimizedGates1{h}{g}_{N}_{M}.pkl','wb')
			pickle.dump(pickle.load(f).gates, i)
			f.close()
			i.close()
			


# f = open(f'pklFiles/DB/approxOptimizedCircuit111_8_3_.pkl','rb')
# g = open(f'pklFiles/DBNicholas/optimizedGates111_8_3.pkl','wb')
# pickle.dump(pickle.load(f).gates, g)
# f.close()
# g.close()