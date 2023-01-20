"""
Given two strings, write a method to decide if one is a permutation of the
other

"""
from test_utils.helper_functions import verify_output

def check_permutation(input_1,input2):
    pass





if __name__ == "__main__":
    verify_output(True,check_permutation("sameer","masere"))
    verify_output(True,check_permutation("sameer","saeerm"))
    verify_output(False,check_permutation("sameer","samqer"))


