#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            print("{}".format(j), end="")
            if i.index(j) == len(i) - 1:
                break
            else:
                print(end=" ")
        print()
