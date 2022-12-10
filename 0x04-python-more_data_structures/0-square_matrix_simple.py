#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if matrix:
        return([[x*x for x in elem] for elem in matrix])
