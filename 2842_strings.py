def subsequencia_strings(str1, str2, n1, n2):
    
    substring = [[None] * (n2 + 1) for i in range(n1 + 1)]
    
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            
            if i == 0 or j == 0:
                substring[i][j] = 0
                
            elif str1[i - 1] == str2[j - 1]:
                substring[i][j] = substring[i - 1][j - 1] + 1
                
            else:
                substring[i][j] = max(substring[i - 1][j], substring[i][j - 1])
                
    return substring[n1][n2]
    
    
str1 = input()
str2 = input()

n1 = len(str1)
n2 = len(str2)

print(n1 + n2 - subsequencia_strings(str1, str2, n1, n2))