#!/usr/bin/python3
"""
    Module to find the max integer in a list
    using the module NumPy
    Prototype: def lazy_matrix_mul(m_a, m_b):
"""


import numpy as npy


def lazy_matrix_mul(m_a, m_b):
    """ multiply two matrix with numpy """
    return npy.dot(m_a, m_b)
