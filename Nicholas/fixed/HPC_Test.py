# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:07:50 2023

@author: msyne
"""

import Overlap_Function as op
import sys

which = int(sys.argv[1])

parameters = [{'n':8, 'J':1, 'h':1,'m':5, 'iterations':1000, 'runs':3},{'n':8, 'J':1, 'h':1,'m':5, 'iterations':1000, 'runs':3}]
param = parameters[which]

n, J, h, m, iterations, runs = param.values()

for i in range(runs):
	overlaps, gates = op.overlap(n, m, J, h, iterations, runs)

	with open(f'overlaps_n={n}_J={J}_h={h}_m={m}.txt', 'w') as f:
    		for j, overlap in enumerate(overlaps):
        		f.write(f"Run {j+1}: {overlap}\n")
