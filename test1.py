def strStr(haystack: str, needle: str) -> int:
    
    len_needle=len(needle)
    len_haystack=len(haystack)
    
    i=0
    gap=len_needle
    while (len_haystack-i+1)>=len_needle:
        print(haystack[i:gap])
        if haystack[i:gap]==needle:
            return i
        i+=1
        gap+=1
        
    return -1


#print(strStr("badbutsad","sad"))
print(strStr("leetcode","leeto"))
            
            