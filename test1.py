def compare(string1,string2):
            value=''
            min_len=min(len(string1),len(string2))

            for i in range(min_len):              
                
                if string1[i]==string2[i]:
                    value+=string1[i]#string append
                else:
                    break
            return value

def longestCommonPrefix(A):
        longest_val=''
        longest_val=A[0]
        n=len(A)
        
        for i in range(1,n):
            temp = A[i]
            longest_val = compare(longest_val,temp)
        
        return longest_val


print(longestCommonPrefix(["abcdefgh", "aefghijk", "abcefgh"]))
            
            