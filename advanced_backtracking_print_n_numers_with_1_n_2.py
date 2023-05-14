def print_n_numbers(arr,i,n):
    if i == n:
        print(arr)
        return
    arr[i]=1
    print_n_numbers(arr,i+1,n)
    arr[i]=2
    print_n_numbers(arr,i+1,n)
    



n=int(input("Enter the value of n: "))


arr=[0]*n


print_n_numbers(arr,0,n)