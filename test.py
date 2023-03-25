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
    
    if head ==None or head.next==None:
        return head
    
    prev=None
    cur=head
    tmp=cur.next
    
    while cur is not None and tmp is not None:
        #prev=cur
        cur.next=tmp.next
        tmp.next=cur
        if prev is None:
            head=tmp
        else:
            prev.next=tmp
        
        
        prev=cur
        
        
        
        cur=cur.next
        
        if cur==None:
            break
        tmp=cur.next
    
            
    
    #head=prev   
    #return head3


insert_node(1,17)
insert_node(2,4)
insert_node(3,12)
insert_node(4,10)
insert_node(5,5)


print_ll()
reverse()
print_ll()

#print_ll()




    