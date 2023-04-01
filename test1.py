def reverseWords(s):

        resultant_string=""
        n=len(s)
        p1=0
        p2=0
        while p2!=n:
            
            if s[p2]!=" ":
                p2+=1
            else:
                temp=""

                temp=s[p1:p2]
                temp_rev=temp[::-1]
                resultant_string+=(temp_rev+" ")
                p1=p2+1
                p2=p1
        tmp=s[p1:p2]
        resultant_string+=tmp[::-1]

        return resultant_string
    

print(reverseWords("Let's take LeetCode contest"))