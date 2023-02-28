from functools import cmp_to_key

def solve(A):
    #res_arr=[]
    def my_compare(a,b):
        
        if a[-2].isnumeric()==True and b[-2].isnumeric()==True:
            if a[-3:]=="100" and b[-3:]!="100":
                return -1
            
            elif b[-3:]=="100" and a[-3:]!="100":
                return 1

            if int(a[-2:]) <= int(b[-2:]):
                return 1
            else:
                return -1
        else:
            if not(a[-2].isnumeric()) and b[-2].isnumeric():
                return 1
            if not(b[-2].isnumeric()) and a[-2].isnumeric():
                return -1
            else:
                if int(a[-1]) <= int(b[-1]):
                    return 1
                else:
                    return -1
        

    A.sort(key=cmp_to_key(my_compare))
    
    return A

# print(solve([
#     "harsh80",
#     "adarsh95",
#     "shivam95"
# ]))

print(solve([
    "harsh95",
    "jack100",
    "john23",
    "jess95",
    "tommy5",
    "phil5"

    
]))


    