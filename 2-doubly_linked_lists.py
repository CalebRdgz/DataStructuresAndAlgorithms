#Doubly Linked Lists have arrows pointing the other way aswell
# {
#     "value": 7,
#     "next": None,
#     "prev": None
# }

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        #create node using Node class
        new_node = Node(value)
        #point head pointer to the new node
        self.head = new_node
        #point tail pointer to the new node
        self.tail = new_node
        #set length of linked list to 1
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        #create the new node using the input value:
        new_node = Node(value)
        #if linkedlist is empty, point head and tail to the new node:
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            #connect the tail to the new node:
            self.tail.next = new_node
            #connect the prev arrow to the tail node of the original linkedlist:
            new_node.prev = self.tail
            #connect the original linkedlist tail to the new node:
            self.tail = new_node
        #increment the length of the doublylinkedlist by i:
        self.length += 1
        #will use the append method in the insert method, so return True for now
        return True
    
    #easier to start from end of linked list because of prev arrows in doublylinkedlist
    def pop(self):
        #if we have 0 items, return None:
        if self.length == 0:
            return None
        #create temp pointer at tail of dlinkedlist
        temp = self.tail
        #if we have 1 item in dlinkedlist, point the head and tail to None:
        if self.length == 1:
            self.head = None
            self.tail = None
        #for two or more items in dlinkedlist:
        else:
            #move the tail of the dlinkedlist backwards once
            self.tail = self.tail.prev
            #pop off the tail Node by pointing the tail of the dlinkedlist to None:
            self.tail.next = None
            #remove the prev arrow by pointing it to None:
            temp.prev = None
        #decrement length by 1
        self.length -= 1
        #return the popped off Node:
        return temp
    
    def prepend(self, value):
        #create new node using Node class with input value
        new_node = Node(value)
        #is the dlinkedlist is empty, point head and tail to the new node:
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            #attatch the new Node to the dlinkedlist by connecting new node next arrow to the head
            new_node.next = self.head
            #attatch the previous arrow of the head to the new node
            self.head.prev = new_node
            #make the new node the new head of the dlinkedlist
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        #if dlinkedlist is empty, return None
        if self.length == 0:
            return None
        #temp variable holding head Node
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            #make the next Node the new head
            self.head = self.head.next
            #remove the old head by removing the prev arrow of the new head
            self.head.prev = None
            #remove the old head from the list by removing the next arrow of the old head
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        #create temp variable for head node
        temp = self.head
        #if index of node is less than half of dlinkedlist, iterate head temp to next nodes
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        #if index of node is more than half of dlinkedlist, iterate tail temp to prev nodes
        else:
            temp = self.tail
            #range(start, stop, step (-1 = step backwards))
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev


# #PRINT_LIST
# #give the doublylinkedlist a node of 7 with next and prev arrows
# my_doubly_linked_list = DoublyLinkedList(7)

# my_doubly_linked_list.print_list()

#APPEND
# #initialize the node using doublylinkedlist class:
# my_doubly_linked_list = DoublyLinkedList(1)
# #append a 2 node to the end of the doublylinkedlist:
# my_doubly_linked_list.append(2)
# #print the appended doublylinkedlist to terminal:
# my_doubly_linked_list.print_list()

#POP
# my_doubly_linked_list = DoublyLinkedList(1)
# my_doubly_linked_list.append(2)
# #print original dlinkedlist:
# my_doubly_linked_list.print_list()
# # (2) Items - Returns 2 Node
# print(my_doubly_linked_list.pop())
# # (1) Items - Returns 1 Node
# print(my_doubly_linked_list.pop())
# # (0) Items - Returns None
# print(my_doubly_linked_list.pop())

#PREPEND
# my_doubly_linked_list = DoublyLinkedList(2)
# my_doubly_linked_list.append(3)
# print("original list: ")
# my_doubly_linked_list.print_list()
# my_doubly_linked_list.prepend(1)
# print("prepended list: ")
# my_doubly_linked_list.print_list()

#POP_FIRST
# my_doubly_linked_list = DoublyLinkedList(2)
# my_doubly_linked_list.append(1)
# print("original list")
# my_doubly_linked_list.print_list()

# my_doubly_linked_list.pop_first()
# print("pop first list")
# my_doubly_linked_list.print_list()

#GET
