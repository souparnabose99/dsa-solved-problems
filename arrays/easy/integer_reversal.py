
"""
@TODO:
Design an efficient algorithm to reverse a given integer.
For example if the input of the algorithm is 1234 then the output should be 4321.
"""


# O(N) runtime complexity where N is no of digits in the integer
def integer_reversal(num):
    rev = 0
    while num:
        rev = (rev * 10) + (num % 10)
        num = num // 10
    print("Integer reversed : ", str(rev))
    return rev


n = 57892
integer_reversal(n)

