def romanToInt(s):
    result = 0
    
    traduction = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for i in range(len(s)):
        if i + 1 < len(s) and traduction[s[i]] < traduction[s[i+1]]:
            result -= traduction[s[i]]
        else:
            result += traduction[s[i]]

    return result

r = romanToInt('MCMXCIV') #998

print(r)