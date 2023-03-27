#PROCEUDRE EXPLAINED

        # This code implements an LRU (Least Recently Used) cache,
        # which is a data structure that allows efficient access to a fixed number of recently-used 
        # items.
        # The cache has a maximum capacity, and when new items are added and the cache is full,
        # the least recently used item is evicted to make room for the new item.

        # The LRUCache class has two main methods: get and set.

        # The get method takes a key as input and returns the corresponding value
        # if it exists in the cache, otherwise it returns -1.
        # If the key exists in the cache, the corresponding ListNode is removed from its current 
        # position in the cache
        # and added to the end of the list, since it is now the most recently used item.

        # The set method takes a key-value pair as input and adds it to the cache.
        # If the key already exists in the cache, its corresponding ListNode is removed from its current 
        # position
        # and added to the end of the list. If the cache is full,
        # the least recently used item (which is at the front of the list) is evicted before adding 
        # the new item to the cache.
        # The remove and add helper methods are used to update the linked list when ListNodes are added 
        # or removed from the cache. 
        
#NOTE:
        # self.head and self.tail are dummy nodes that are used to make the implementation 
        # of the doubly linked list easier.
        # They do not represent actual cache entries, but are used as sentinels to mark the 
        # beginning and end of the linked list.

        # self.head.next refers to the first "real" node in the linked list
        # (i.e. the node immediately after the self.head sentinel),
        # while self.tail.prev refers to the last "real" node in the linked list
        #  (i.e. the node immediately before the self.tail sentinel).

        # By using dummy nodes, we can avoid having to check for special cases
        # (such as an empty list or inserting at the beginning or end of the list)
        #  and simplify the implementation of the linked list.  
        

class ListNode:
    def __init__(self,key,value):
        self.key=key#key search for the cache 
        self.value=value#value that is present corresponding value to the key
        
        self.prev=None#left pointer
        self.next=None#right pointer    
        
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity=capacity
        self.cache={}
        #head and tail are ListNode type dummy strucutures which doesnot hold any value but are
        #poiters to the first and last values in the cache
        self.head=ListNode(-1,-1)
        self.tail=ListNode(-1,-1)
        self.head.next=self.tail#connecting the head.next to tail
        self.tail.prev=self.head#connection the tail.prev to head
        
    
    

    # @return an integer
    def get(self, key):
        if key in self.cache:
            node=self.cache[key]
            self.delete_node(node)
            self.add_node(node)
            return node.value
        return -1
        
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            self.delete_node(self.cache[key])
        
        node=ListNode(key,value)
        self.cache[key]=node#update the node in the key
        self.add_node(node)
       
        
        if len(self.cache)>self.capacity:
            node=self.head.next            
            self.delete_node(node)
            del self.cache[node.key]
            
    
    def delete_node(self,node):
        prevnode=node.prev
        nextnode=node.next
        
        prevnode.next=nextnode
        nextnode.prev=prevnode
    
    
    def add_node(self,node):
        prevnode=self.tail.prev
        prevnode.next=node
        node.prev=prevnode 
        node.next=self.tail
        self.tail.prev=node
        
        