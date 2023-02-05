"""
Given two strings, write a method to decide if one is a permutation of the
other

"""
from test_utils.helper_functions import verify_output

from collections import Counter

def check_permutation(input_1,input2):
    
    x = Counter(input_1)
    for item in input2:
        if item  not in x:
            return False
        else:
            x[item]-=1
            if x[item] < 0:
                return False

    if x.total():
        return False

    return True


if __name__ == "__main__":
    verify_output(True,check_permutation("sameer","masere"))
    verify_output(True,check_permutation("sameer","saeerm"))
    verify_output(False,check_permutation("sameer","samqer"))
    verify_output(False,check_permutation("sameer","samee"))
    verify_output(False,check_permutation("sameer","sameee"))

