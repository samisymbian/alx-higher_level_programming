#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    "returns squares"
    newm = []
    for col in matrix:
        sq = list(map(lambda x: x**2, col))
        newm.append(sq)
    return newm
