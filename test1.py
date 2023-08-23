def backspaceCompare(s: str, t: str) -> bool:
    list_s=list(s)
    list_t=list(t)
    fin_s=""
    fin_t=""
    count_s=0
    count_t=0
    for i in range(len(list_s)-1,-1,-1):
        if list_s[i]=="#":
            count_s+=1
        elif list_s[i]!="#" and count_s>0:
            count_s-=1
        elif list_s[i]!="#" and count_s==0:
            fin_s+=list_s[i]
    fin_s=fin_s[::-1]
    for i in range(len(list_t)-1,-1,-1):
        if list_t[i]=="#":
            count_t+=1
        elif list_t[i]!="#" and count_t>0:
            count_t-=1
        elif list_t[i]!="#" and count_t==0:
            fin_t+=list_t[i]
    fin_t=fin_t[::-1]
    
    if fin_s==fin_t:
        return True        
    return False
            
#print(backspaceCompare("ab#c","ad#c"))
#print(backspaceCompare("ab##","c#d#"))
print(backspaceCompare("a#c","b"))