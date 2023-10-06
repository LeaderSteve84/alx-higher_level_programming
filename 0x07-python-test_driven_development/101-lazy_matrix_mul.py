#!/usr/bin/python3
# 101-lazy_matrix_mul.py
'''function that multiplies 2 matrices by using the module NumPy'''
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    '''return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints or floats): First matrix.
        m_b (list of lists of ints or floats): Second matrix.
    '''

    return (np.matmul(m_a, m_b))
