class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        
        target_length=len(B)
        check_string=B+"@"+A
        n=len(check_string)
        lps=[0]*n
        count=0
        for i in range(1,n):
            x=lps[i-1]

            while check_string[i]!=check_string[x]:
                if x==0:
                    x=x-1
                    break
                x=lps[x-1]
            lps[i]=x+1
            if lps[i]==target_length:
                count+=1
        
        return count
            