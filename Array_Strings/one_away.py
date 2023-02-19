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

def oneEditReplace(first,second):
   found_difference = False
   for i in range(0,len(first)):
       if first[i] != second[i]:
           if found_difference:
               return False
          
           found_difference = True
   return True


def oneEditInsert(first,second):
    index1 = 0
    index2 = 0
    while(index1 < len(first) and index2 < len(second)):
        if first[index1] != second[index2]:
            if index1 != index2:
               return False

            index2 +=1
        else:
           index1 +=1
           index2 +=1
    
    return True



def one_away(first,second):
    if (len(first) == len(second)):
       return oneEditReplace(first,second)
    elif (len(first) + 1 == len(second)):
       return oneEditInsert(first,second)
    elif (len(first) - 1 == len(second)):
       return oneEditInsert(second,first)
    return False
    
if __name__ == "__main__":
    verify_output(True,one_away("pale","ple"))
    verify_output(True,one_away("pales","pale"))
    verify_output(True,one_away("pale","bale"))
    verify_output(False,one_away("pale","bae"))


