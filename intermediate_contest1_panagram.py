def solve(A):
    #panagram means the list of words consists of all the letters in small case of english alphabet
    hash_set=set()
    for a in A:
        n=len(a)
        for i in range(n):
            if a[i] not in hash_set:
                hash_set.add(a[i])
        
    if len(hash_set) == 26:
        return 1
    else:
        return 0
    
print(solve(["the","quick","brown","fox","jumps","over","the","lazy","dog"]))
print(solve(["bit","scale"]))