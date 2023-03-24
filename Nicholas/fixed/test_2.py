# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 13:00:23 2023

@author: msyne
"""
import sys

which = int(sys.argv[1])

print(which)

with open(f'data_{which}.txt', 'w') as f:
    f.write(f'This is job number {which}')