def isPalindrome(s):

        n=len(s)
        
        string_alnum=""
        string_source=""

        for i in range(n):
            if s[i].isalpha():
                string_alnum+=s[i]
            elif s[i].isnumeric():
                string_alnum+=s[i]

        n1=len(string_alnum)

        if string_alnum=="":
            return True
        print(string_source)  
        for i in range(n1):
            if s[i].isalpha():
                string_source+=string_alnum[i]
        print(string_source)    
        if string_source=="":
            return False
        val=string_source.lower()
        print(val)   
        reverse_string=val[::-1]
        
        print(reverse_string)

        if reverse_string == val:
            return True
        else:
            return False
        

print(isPalindrome("A man, a plan, a canal: Panama"))