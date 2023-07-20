#!/usr/bin/python3
def best_score(a_dictionnary):
    if a_dictionnary and len(a_dictionnary):
        maxval = list(a_dictionnary.keys())[0]
        for key in a_dictionnary
            if a_dictionnary[key] > a_dictionnary[maxval]:
                maxval = key
        return maxval
    return None
