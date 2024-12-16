# if there is no common  prefix return ""
# all in lowercase

def longestCommonPrefix(strs: list[str]) -> str:
    res = ""
    
    for i in range(len(strs[0])):
        for word in strs:
            if i == len(word) or word[i] != strs[0][i]:
                return res
            
        res += strs[0][i]

    return res

arr = ["comer", "co", "correr"]
print(longestCommonPrefix(arr))
