def isPalindrome(x):
    str_x = str(x)

    return str_x == str_x[::-1]

x = 109903
r = isPalindrome(x)
print(r)