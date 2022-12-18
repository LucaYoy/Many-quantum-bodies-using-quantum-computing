# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 19:17:13 2022

@author: msyne
"""

import numpy as np

def generate_random_unitary_matrix():
    # create a matrix with random complex numbers
    matrix = np.random.randn(4,4) + 1j * np.random.randn(4,4)

    # compute the QR decomposition of the matrix
    q, r = np.linalg.qr(matrix)

    # normalize the matrix to make it unitary
    matrix = q / np.linalg.norm(q)

    return matrix.reshape(2,2,2,2)

# set the number of matrices to generate
num_matrices = 5

# create an empty list to store the matrices
matrices = []

# generate the matrices
for i in range(num_matrices):
    matrix = generate_random_unitary_matrix()
    matrices.append(matrix)
    
   
    
 
    
    
    