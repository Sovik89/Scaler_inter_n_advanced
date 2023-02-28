def lengthOfLongestSubstring(s: str) -> int:
    start = 0
    end=0
    n=len(s)
    i=0
    temp_arr=""
    while True:
        if s[i] not in temp_arr:
            temp_arr+=s[i]
            i+=1
    end=len(temp_arr)-1    
    longest=end-start+1
    if longest==n:
        return longest
    else:
        while s[start]!=s[i]:
            start+=1
    start=start+1
    if start==end:
        end+=1
    
    while (end<n-1) and (start<end):
        if s[start]!=s[end]:
            end+=1
        else:
            longest=max(len(s[start:end]),longest)
            start+=1
    
    longest=max(longest,len(s[start:end]))
    
    return longest        
        



print(lengthOfLongestSubstring("abcabcbb"))
    
            
        
    
            
            
    