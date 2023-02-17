"""
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""
from test_utils.helper_functions import verify_output


def string_compression(data):
    pass


if __name__ == "__main__":
    verify_output("a2b1c5a3", string_compression("aabcccccaaa"))
    verify_output("a7b2c1b4a1", string_compression("aaaaaaabbcbbbba"))

