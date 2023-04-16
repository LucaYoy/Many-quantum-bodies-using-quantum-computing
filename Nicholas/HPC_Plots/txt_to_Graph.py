# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:41:52 2023

@author: msyne
"""

import matplotlib.pyplot as plt
import numpy as np
import os

n = 14
J = 1
h = 1
g = 1
m = 5
filename = f'sweeps=50_n=6_J=1_h=1_g=1_m=5_gates=Identity.txt'


overlaps_by_run = {}
gates_by_run = {}
min_overlap_change = 0.0000001
store_overlap = True
gates = []
with open(filename, 'r') as f:
        
    filename = os.path.splitext(os.path.basename(f.name))[0]
    
    fig, ax = plt.subplots(figsize=(16,14))
    
    in_gates = False

    
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        if line.startswith('Gates:'):
            in_gates = True
        
        if not in_gates:
            run_name, overlap_str = line.strip().split(':')
            if run_name not in overlaps_by_run:
                overlaps_by_run[run_name] = []
            overlaps = [float(x) for x in overlap_str.strip()[2:-2].split(',')]
            overlaps_by_run[run_name].extend(overlaps) 
        else:
            if line.startswith('Run 1'):
                run_name_g, gate_str = line.strip().split(':')
                if run_name not in overlaps_by_run:
                        gates_by_run[run_name_g] = []
                gates = [complex(x) for x in gate_str.strip()[2:-2].split()]
                gates_by_run[run_name_g].extend(gates)
                        #gate_str += line
                        #gates.append(np.array(eval(gate_str)))
            
                        

            
        
    for i, (run_name, overlaps) in enumerate(overlaps_by_run.items()):
        
        stop_flag = False
        
        for j in range(1, len(overlaps)):
            # Calculate the difference between the current overlap and the previous one
            overlap_diff = abs(overlaps[j] - overlaps[j-1])
            
            # If the overlap difference is smaller than the minimum overlap change and we haven't
            # already plotted a red X for this run, plot it and set plotted_red_x to True
            if overlap_diff < min_overlap_change and not stop_flag:
                plt.plot(j+1, overlaps[j], 'rx')
                stop_flag = True
                #print(f"Stopping condition met at iteration {j+1} for run {run_name}")
        
        plt.plot(range(1, len(overlaps)+1), overlaps, label=f'{run_name}')

        plt.xlabel('Iteration')
        plt.ylabel('1 - Overlap')
        #plt.legend()
        plt.xscale("log")
        plt.yscale("log")

        plt.title(f'Overlaps for {len(overlaps)} sweeps, n={n}, J = {J}, h={h}, g={g}, m={m}, Gates=Identity')
        

if not os.path.exists("HPC_Graphs"):
    os.makedirs("HPC_Graphs")
    

if not os.path.exists(f"HPC_Graphs/{ax.get_title()}.png"):
    plt.savefig(f"HPC_Graphs/{ax.get_title()}.png")
    
plt.show()

