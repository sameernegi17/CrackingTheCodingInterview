"""
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false

"""
from test_utils.helper_functions import verify_output

def one_away(first,second):
    pass
    
if __name__ == "__main__":
    verify_output(True,one_away("pale","ple"))
    verify_output(True,one_away("pales","pale"))
    verify_output(True,one_away("pale","bale"))
    verify_output(False,one_away("pale","bae"))


