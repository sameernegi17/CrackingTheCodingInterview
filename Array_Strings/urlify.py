"""
 Write a method to replace all spaces in a string with '%20'. 
 You may assume that the string 
has sufficient space at the end to hold the additional characters, 
and that you are given the "true"  length of the string
"""

from test_utils.helper_functions import verify_output

def urlify(data,data_len):
    data = list(data)
    spaces_count = 0
    for i in range(0,data_len):
        if data[i]== " ":
           spaces_count+=1

    index = data_len + (spaces_count * 2)

    for i in range(data_len - 1,0,-1):
        if data[i] == " ":
            data[index - 1] = "0"
            data[index - 2] = "2"
            data[index - 3] = "%"
            index -= 3
        else:
            data[index-1] = data[i]
            index-=1

    return "".join(data)

if __name__ == "__main__":
    verify_output("Mr%20John%20Smith",urlify("Mr John Smith    ", 13))
    verify_output("My%20Name%20Is%20Sameer%20Negi",urlify("My Name Is Sameer Negi        ",22))