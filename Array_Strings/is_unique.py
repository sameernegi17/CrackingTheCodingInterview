"""
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

"""
from test_utils.helper_functions import verify_output

def is_unique(data):
    temp_set = set(data)
    print("Tempory set ", temp_set)

    if len(temp_set) == len(data):
        return True
    else:
        return False
    
if __name__ == "__main__":
    verify_output(True,is_unique("asewrt"))
    verify_output(False,is_unique("aseer"))


