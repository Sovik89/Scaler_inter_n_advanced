def check_multiple(A,B):
    head=A
    
    cur = head
    
    while cur:
        # check_val=B
        # i=1
        # while check_val<cur.val:
        #     check_val=(B*i)
        #     if check_val>=cur.val:
        #         break
        #     i+=1
        # cur.val=check_val        
        # cur=cur.next
        
        quotient=cur.val//B
        reminder=cur.val%B
        if reminder>0:
            cur.val=(quotient+1)*B
        else:
            cur.val=(quotient)*B
        cur=cur.next
        
    return head