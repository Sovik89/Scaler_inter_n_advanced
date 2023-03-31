class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


head = None
size_of_ll = 0
head3 =None


def insert_node(position, value):
    global head
    global size_of_ll
    if position >= 1 and position <= size_of_ll + 1:
        temp = ListNode(value)
        # insert at head
        if position == 1:
            temp.next = head
            head = temp
        else:
            count = 1
            prev = head
            # traverse till the previous node
            while count < position - 1:
                prev = prev.next
                count += 1
            temp.next = prev.next
            prev.next = temp
        size_of_ll += 1

def print_ll():
    global head
    tmp = head
    ans = []
    # traverse the entire linked list
    while tmp is not None:
    #     ans.append(str(tmp.val))
    #     tmp = tmp.next
    # print(" ".join(ans))
        print(tmp.val,end=" ")
        tmp=tmp.next
    print()

# def print_ll_order():
#     global head3
#     tmp = head3
#     ans = []
#     # traverse the entire linked list
#     while tmp is not None:
#     #     ans.append(str(tmp.val))
#     #     tmp = tmp.next
#     # print(" ".join(ans))
#         print(tmp.val,end=" ")
#         tmp=tmp.next
#     print()
        
#17 -> 4 -> 12 -> 10 -> 5

def reverse():
    global head
    
    #edge case
    if head ==None or head.next==None:
        return head
    
    #Initialize
    prev=None#node before current
    cur=head#current as in head
    tmp=cur.next#next value of current
    
    #we check while curis not none or tmp is not none
    while cur is not None and tmp is not None:
        #prev=cur
        cur.next=tmp.next#connect cur with node next to tmp
        tmp.next=cur#connect tmp's next value with curr
        if prev is None:
            head=tmp#we establish head as cur.next when prev == None
        else:
            prev.next=tmp # else if tmp is not head we give the interchanged value next as tmp
        
        
        prev=cur#we keep prev as the current value before we move current cursor
        
        
        
        cur=cur.next#we move current cursor
        
        if cur==None:#if current now is None there is no point in moving further
            break
        tmp=cur.next#if cur.next exit it should be tmp
    
            
    
    #head=prev   
    #return head3
def middle():
        global head

        if head == None:
            return 0

        slow=head
        fast=head

        count=1

        while (fast.next is not None) and (fast.next.next is not None):
            
            count+=1
            slow=slow.next
            fast=fast.next.next
        
        if fast.next==None:
            return slow.val

        if fast.next.next==None:
            return slow.next.val
        

def check_multiple(B):
    global head
    
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
    
        
        



insert_node(1,13)
insert_node(2,26)
insert_node(3,39)
insert_node(4,52)
insert_node(5,65)
insert_node(6,78)


print_ll()
#reverse()
check_multiple(13)
print_ll()

#print_ll()

#[ 14 -> 42 -> 98 -> 26 -> 36 -> 28 -> 57 -> 93 ]


    