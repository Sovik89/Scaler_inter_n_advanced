class ListNode:
    def __init__(self, key, value):
        self.key = key  # the key for the cache entry
        self.value = value  # the value for the cache entry
        self.prev = None  # a reference to the previous ListNode in the linked list
        self.next = None  # a reference to the next ListNode in the linked list

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity  # the maximum number of items the cache can hold
        self.cache = {}  # a dictionary to store the cache entries, with keys mapping to ListNodes
        self.head = ListNode(-1, -1)  # a dummy ListNode at the front of the linked list
        self.tail = ListNode(-1, -1)  # a dummy ListNode at the end of the linked list
        self.head.next = self.tail  # link the head to the tail
        self.tail.prev = self.head  # link the tail to the head
       

    # @return an integer
    def get(self, key):
        if key in self.cache:  # if the key is in the cache
            node = self.cache[key]  # get the ListNode associated with the key
            self.remove(node)  # remove the ListNode from its current position
            self.add(node)  # add the ListNode to the end of the linked list (since it is now the most recently used)
            return node.value  # return the value associated with the key
        return -1  # if the key is not in the cache, return -1
   
    #get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:  # if the key is already in the cache
            self.remove(self.cache[key])  # remove the ListNode associated with the key from its current position

        node = ListNode(key, value)  # create a new ListNode for the new cache entry
        self.cache[key] = node  # add the ListNode to the cache dictionary
        self.add(node)  # add the new ListNode to the end of the linked list

        if len(self.cache) > self.capacity:  # if the cache is now over capacity
            node = self.head.next  # get the ListNode at the front of the linked list (i.e. the least recently used)
            self.remove(node)  # remove the ListNode from the linked list and the cache
            del self.cache[node.key]

    def remove(self,node):
        prevnode = node.prev  # get the previous ListNode in the linked list
        nextnode = node.next  # get the next ListNode in the linked list
        prevnode.next = nextnode  # link the previous node to the next node
        nextnode.prev = prevnode  # link the next node to the previous node

    def add(self,node):
        prevnode = self.tail.prev  # get the ListNode currently at the end of the linked list
        prevnode.next = node  # link the previous node to the new node
        node.prev = prevnode  # link the new node to the previous node

        node.next = self.tail  # link the new node to the dummy tail
        self.tail.prev = node  # link the dummy tail to the new node      

        #NOTE:
        # self.head and self.tail are dummy nodes that are used to make the implementation of the doubly linked list easier.
        # They do not represent actual cache entries, but are used as sentinels to mark the beginning and end of the linked list.

        # self.head.next refers to the first "real" node in the linked list
        # (i.e. the node immediately after the self.head sentinel),
        # while self.tail.prev refers to the last "real" node in the linked list
        #  (i.e. the node immediately before the self.tail sentinel).

        # By using dummy nodes, we can avoid having to check for special cases
        # (such as an empty list or inserting at the beginning or end of the list)
        #  and simplify the implementation of the linked list.      



        #PROCEUDRE EXPLAINED

        # This code implements an LRU (Least Recently Used) cache,
        # which is a data structure that allows efficient access to a fixed number of recently-used items.
        # The cache has a maximum capacity, and when new items are added and the cache is full,
        # the least recently used item is evicted to make room for the new item.

        # The LRUCache class has two main methods: get and set.

        # The get method takes a key as input and returns the corresponding value
        # if it exists in the cache, otherwise it returns -1.
        # If the key exists in the cache, the corresponding ListNode is removed from its current position in the cache
        # and added to the end of the list, since it is now the most recently used item.

        # The set method takes a key-value pair as input and adds it to the cache.
        # If the key already exists in the cache, its corresponding ListNode is removed from its current position
        # and added to the end of the list. If the cache is full,
        # the least recently used item (which is at the front of the list) is evicted before adding the new item to the cache.
        # The remove and add helper methods are used to update the linked list when ListNodes are added or removed from the cache.  

