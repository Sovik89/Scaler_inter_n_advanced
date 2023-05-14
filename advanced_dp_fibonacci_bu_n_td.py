#######################################BOTTOM UP###################################################

# def main():
#     # YOUR CODE GOES HERE
#     # Please take input and print output to standard input/output (stdin/stdout)
#     # E.g. 'input()/raw_input()' for input & 'print' for output

#     #bottom up approach

#     A=int(input())

#     if A<=1:
#         print(A)

#     ans=[0,1]

#     for i in range(2,A+1):

#         value=ans[i-1]+ans[i-2]
#         ans.append(value)
    
    

#     print(ans[A])



#     return 0

# if __name__ == '__main__':
#     main()


#############################################  TOP DOWN APPROACH ##################################

def fibonacci(dp,A):
    if A<=1:
        dp[A]=A
        return dp[A]
    
    if dp[A]==-1:
        dp[A]=fibonacci(dp,A-2)+fibonacci(dp,A-1)
        
    return dp[A] 


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    
    A=int(input())
    
    dp=[-1]*(A+1)
    
    fibonacci(dp,A)
    
    print(dp[A])
    
    return 0


if __name__ == '__main__':
    main()


