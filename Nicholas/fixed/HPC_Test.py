# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:07:50 2023

@author: msyne
"""

import Overlap_Function as op
import sys

which = int(sys.argv[1])

parameters = [{'n':6, 'J':1, 'h':1,'m':3, 'iterations':1000, 'runs':10},
              {'n':6, 'J':1, 'h':1.5,'m':3, 'iterations':1000, 'runs':10}]

param = parameters[which]

n, J, h, m, iterations, runs = param.values()
op.overlap(n, m, J, h, iterations, runs)