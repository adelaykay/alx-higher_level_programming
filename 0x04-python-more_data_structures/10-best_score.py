#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        best = {}
        for k, v in a_dictionary.items():
            if v == sorted(a_dictionary.values())[len(a_dictionary.keys())-1]:
                return(k)
