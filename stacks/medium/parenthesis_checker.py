
"""
@TODO:
Given an expression string, write a python program to find whether a given string has balanced parentheses or not.
For example:
Input : {[]{()}}, Output : Balanced
Input : [{}{}(], Output : Unbalanced
"""

# O(N) runtime complexity 
def parenthesis_checker(exp_str):
    open_braces = ["{", "(", "["]
    closing_braces = ["}", ")", "]"]

    exp_str = list(exp_str)
    # print(exp_str)
    stack = []
    for ele in exp_str:
        if ele in open_braces:
            stack.append(ele)
        elif ele in closing_braces:
            exp_ind = closing_braces.index(ele)
            if len(stack) > 0 and open_braces[exp_ind] == stack[len(stack) - 1]:
                stack.pop()
            # else:
                # print("Unbalanced")

    if len(stack) == 0:
        print("Balanced")
    else:
        print("Unbalanced")

    return


if __name__ == "__main__":
    parenthesis_checker("{([])}")
    parenthesis_checker("{([]])}[")
    parenthesis_checker("{(}}}}")
    parenthesis_checker("{()}[]")
    
    # Balanced
    # Unbalanced
    # Unbalanced
    # Balanced

