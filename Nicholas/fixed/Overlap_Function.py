# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:04:01 2023

@author: msyne
"""

import BrickWall as bw

def overlap(n, m, J, h, g, iterations, runs):
    """ Uses my brick wall function to output the overlaps and iterations
    all in one function.
    The flags are set to the following:
        - gates are randomized
        - overlap is not printed
        - old optimization algorithm
         
    """
    
    
    alloverlaps = []
    for i in range(runs):
        # Sets all the variables as necessary
        Circuit = bw.Circuit(n, m, J, h, g, gatesrandom=True)
        _,overlaps,_, iterations,_,gates = Circuit.optimize_circuit(iterations, 10**-4,
                                                              show_overlap=True)
        alloverlaps.append(overlaps)
        return alloverlaps, gates
