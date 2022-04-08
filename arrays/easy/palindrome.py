
"""
A palindrome is a string that reads the same forward and backward
For example: radar or madam

@TODO:
Design an optimal algorithm for checking whether a given string is palindrome or not!
"""


# Creates an additional list for storing elements in reverse
# O(N) runtime complexity = no of items in the list of string
def is_palindrome(val):
    val = list(val)
    rev_list = val[::-1]
    print(rev_list)
    for i in range(len(val)):
        if val[i] != rev_list[i]:
            print("".join(val), " is not a Palindrome!!")
            return
    print("".join(val), " is a Palindrome!!")
    return


def rev_array(data):
    data = list(data)
    i = 0
    j = len(data) - 1
    while j >= i:
        data[i], data[j] = data[j], data[i]
        i += 1
        j -= 1
    return ''.join(data)


def palindrome_check(s):
    rev_str = rev_array(s)
    if s == rev_str:
        print("True")
        return True
    print("False")
    return False


str_1 = "radar"
str_2 = "pilot"

is_palindrome(str_1)
is_palindrome(str_2)

palindrome_check(str_1)
palindrome_check(str_2)


