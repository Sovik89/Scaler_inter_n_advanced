from functools import cmp_to_key

def largestNumber(self, A):
    list_A=list(A)
    def my_compare(a,b):
        str_a=str(a)
        str_b=str(b)
            
        if (int(str_a+str_b) < int(str_b+str_a)):
            return 1
        else:
            return -1
        
        
    
    list_A.sort(key=cmp_to_key(my_compare))
        
    return_str=""
    for a in list_A:
        return_str+=str(a)
    
    #corner case        
    if int(return_str) == 0:
        return "0"
    else:
        return return_str


print(largestNumber([3, 30, 34, 5, 9]))