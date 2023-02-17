"""
Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
permutation is a rearrangement of letters. The palindrome does not need to be limited to just
dictionary words.
"""

from test_utils.helper_functions import verify_output

from collections import Counter

def palindrome_permutation(data):
    pass

if __name__ == "__main__":
    verify_output(True,palindrome_permutation("Tact Coa"))
    verify_output(True,palindrome_permutation("abcab"))


