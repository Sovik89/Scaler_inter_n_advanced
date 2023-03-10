def expand(A,p1,p2):
            n=len(A)
            #expansion to left and expansion to right
            while p1>=0 and p2<n and A[p1]==A[p2]:
                p1-=1
                p2+=1
            
            
            return A[p1+1:p2]

def longestPalindrome(A):      
        
        ans=0#lenght of the max palindrom string
        str_val=''
        n=len(A)
        
        
        #for odd palindrom

        for i in range(n):
            if ans != len(expand(A,i,i)):
                ans=max(ans,len(expand(A,i,i)))
                if ans == len(expand(A,i,i)):
                    str_val=expand(A,i,i)

        #for even palindrom

        for i in range(n):
            if ans != len(expand(A,i,i+1)):
                ans=max(ans,len(expand(A,i,i+1)))
                if ans == len(expand(A,i,i+1)):
                    str_val=expand(A,i,i+1)

        return str_val
    

print(longestPalindrome("abcdefbaabxyz"))
        
