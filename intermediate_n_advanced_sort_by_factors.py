from functools import cmp_to_key 

def solve(A):
    #use factor for comparison
    
    def my_compare(a,b):
        fact_a=0
        fact_b=0
        i=1
        while i*i<=a:
            if a%i == 0:
                if a//i == i:
                    fact_a+=1
                else:
                    fact_a+=2
            i+=1
        
        i=1
        while i*i<=b:
            if b%i == 0:
                if b//i == i:
                    fact_b+=1
                else:
                    fact_b+=2
            i+=1
                
        if fact_a==fact_b:
            if a>b:
                return 1
            else:
                return -1
        
        elif fact_a>fact_b:
            return 1
        else:
            return -1
        
    A.sort(key=cmp_to_key(my_compare))
        
        
    return A


#print(solve([6, 8, 9]))
        
print(solve([2,4,7]))     