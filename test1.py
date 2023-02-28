def palindrome(value:int)->bool:
    str1=str(value)
    print(str1)
    str2=str1[::-1]
    if str1 == str2:
        return True
    else:
        return False
    
print(palindrome(1213))