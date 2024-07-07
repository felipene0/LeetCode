def longestCommonPrefix(strs):

    r = ""

    for i, c in enumerate(strs[0]):
        for string in strs[1:]:
            if i == len(string) or string[i] != c:
                return r
        r += c
    return r
            

teste = longestCommonPrefix(["flower","flow","flight"])

print(teste)
