"""
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""
from test_utils.helper_functions import verify_output


def string_compression(data):
    data = data + "$"
    compressedString = ""
    count = 1
    for i in range(1,len(data)):
        if data[i-1] == data[i]:
            count+=1
        else:
            compressedString += data[i-1] + str(count)
            count = 1

    return compressedString




if __name__ == "__main__":
    verify_output("a2b1c5a3", string_compression("aabcccccaaa"))
    verify_output("a7b2c1b4a1", string_compression("aaaaaaabbcbbbba"))

