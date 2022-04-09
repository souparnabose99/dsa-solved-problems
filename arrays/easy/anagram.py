
"""
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once

@TODO:
Construct an algorithm to check whether two words (or phrases) are anagrams or not!

For example: restful and fluster
"""


# O(N) runtime complexity where N is no of characters in the string
def anagram_check(str_1, str_2):
    val_1 = list(str_1)
    val_2 = list(str_2)
    if len(val_1) != len(val_2):
        print("Lengths dont match, hence ", str_1, " & ", str_2, "are not anagrams!!")
        return False
    for ele in val_1:
        if ele not in val_2:
            print(str_1, " & ", str_2, "are not anagrams!!")
            return False
    print(str_1, " & ", str_2, "are anagrams!!")
    return True


str_1 = "boat"
str_2 = "goat"
str_3 = "restful"
str_4 = "fluster"
anagram_check(str_3, str_4)



