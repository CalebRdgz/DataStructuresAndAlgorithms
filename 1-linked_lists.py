#Linked list doesnt have indexes
#all items are right next to eachother in memory
#a linked list has a head(points to the first node in list)
#a linked list has a tail(points to the last node in list)
#each node points to the next node (nodes are placed in random areas)
#iterating through a list = O(n)
#easier O(1) to remove an item from the beginning or the end using linked lists instead of indexed lists

# (head) -> 11 -> 3 -> 23 -> 7 -> (tail) -> 4 ->

#LINKED LISTS - UNDER THE HOOD

# Node = value and pointer
# a Node is a dictionary:
# 4 ->
# {
#     "value": 4,
#     "next": None
# }

# 7 -> 4 -> (none)
# {
#     "value": 7,
#     "next": {
#                 "value": 4,
#                 "next": None
#             }
# }

# (head) -> 11 -> 3 -> 23 -> 7 -> (tail) -> 4 ->
# head = {
#             "value": 11,
#             "next": {
#                         "value": 3,
#                         "next": {
#                                     "value": 23,
#                                     "next": {
#                                                 "value": 7,
#                                                 "next": {
#                                                             "value": 4, #tail
#                                                             "next": None 
#                                                         }
#                                             }
#                                 }
#                     }
#         }
# print(head['next']['next']['value']) # prints 23 in terminal
# # This will only run with a Linked List:
# # print(my_linked_list.head.next.next.value)

# # LINKED LISTS - CONSTRUCTOR
# class LinkedList: #capitalize the class name
#     def __init__(self, value): # self = this is a method inside of a class instead of a function
#         # use the value parameter to create the first node at the time we initialize the linked list
#         # __init__ creates a new Node
#     def append(self, value):
#         # append creates a Node and adds Node to end
    
#     def prepend(self, value):
#         # prepend create a Node and adds Node to beginning
    
#     def insert(self, value):
#         # insert create a Node and inserts Node where you want it


#^ DO NOT WANT TO CREATE A NEW NODE EVERY TIME, SO USE A CLASS TO CREATE NODES:
class Node:
    # The only thing the Node class contains is the constructor:
    def __init__(self, value):
        # {
        #     "value": 4,
        #     "next": None
        # } vvv
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value) #Node(value) calls the Node class and passes the value and create the node
        self.head = new_node # head points to the new node
        self.tail = new_node # tail also points to the new node
        self.length = 1

    def print_list(self):
        temp = self.head #temporary pointer points at head node
        while temp is not None:
            print(temp.value)
            temp = temp.next #moves the temp pointer to the next node, until the end (temp = none)
    
    def append(self, value): # self = method inside of a class vs standalone function
        new_node = Node(value)
        #if linked list is empty, point head and tail to the new value:
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #if there are nodes existing in the linked list:
        else:
            #assign "next" to the new node (adding the new node to the linked list):
            self.tail.next = new_node
            #move the tail to the new node:
            self.tail = new_node
        #increase the linked list length by 1:
        self.length += 1
        #(optional): return true (not necessary as a standalone method for the append method):
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head #temp points to the head of the linked list
        pre = self.head #pre also points to the head of the linked list (also head and tail)
        while (temp.next): # or while temp.next is not None:
            #pre pointer points to current node:
            pre = temp
            #move temp pointer to the next node:
            temp = temp.next
        #point pre to the tail of the linked list:
        self.tail = pre
        #break the node after pre off of the end of the linked list:
        self.tail.next = None
        #decrement the length of the linked list by 1:
        self.length -= 1
        #if the length of the linked list becomes 0 after only having length of 1:
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value #returns the node we just removed
    
    def prepend(self, value):
        #create the new node using the value input in the method using the Node class:
        new_node = Node(value)
        #if the linked list is empty, point the head and tail to the new node being prepended:
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            #point the new node to the head of the existing linked list:
            new_node.next = self.head
            #move the head pointer to the new node:
            self.head = new_node
        #increment the length of the linked list py 1
        self.length += 1
        #if you are using another method like append in this method, you have to return True:
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        #create temp pointer to point at the original head of the linked list:
        temp = self.head
        #move the head pointer to the next node:
        self.head = self.head.next
        #remove the old head from the linked list:
        temp.next = None
        #decrement the linked list by 1:
        self.length -= 1
        #after decrementing by 1, if length is 0, set the tail to point to None:
        if self.length == 0:
            self.tail = None
        #return the item we removed from the linked list (to test if we got the right values):
        return temp.value
    
    def get(self, index):
        #if index is out of range:
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        #iterate through the linked list using the input index:
        #"_" is used because were not using that variable in the for loop
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp: #or: if temp is not None:
            temp.value = value
            return True
        #if the if statement doesnt run, it returns False because the index is out of range
        return False
    
    def insert(self, index, value):
        #if index is out of range
        if index < 0 or index > self.length:
            return False
        #if adding to beginning of linked list:
        if index == 0:
            return self.prepend(value)
        #if adding to end of linked list:
        if index == self.length:
            return self.append(value)
        #create a new node using the Node class:
        new_node = Node(value)
        #get the index before the current and save it in the temp variable:
        temp = self.get(index - 1)
        #make the new node point to the next node in the linked list:
        new_node.next = temp.next
        #point the current temp node to the new node being inserted into the linked list:
        temp.next = new_node
        #increment the length of the linked list by 1:
        self.length += 1
        #return True because we are using methods inside of this method:
        return True
    
    def remove(self, index):
        #if index is out of range
        if index < 0 or index >= self.length:
            #return None instead of False because were not returning a Node.
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        #create a prev variable that points to the Node before the current Node:
        prev = self.get(index - 1)
        #get the current Node using the prev variable (more optimized)
        temp = prev.next
        #point the previous Node to the current Node:
        prev.next = temp.next
        #break off the original temp Node from the Linked List:
        temp.next = None
        self.length -= 1
        #using ".value" only here to test if we removed the right Node:
        return temp.value
    
    #switch the head and tail, and move the next arrows the other way one by one
    def reverse(self):
        #save self.head inside of temp:
        temp = self.head
        #move self.head to self.tail:
        self.head = self.tail
        #set self.tail to the self.head saved inside of temp:
        self.tail = temp
        #variable "after" pointing to Node right after temp:
        after = temp.next
        #variable "before" pointing to "Node" right before temp (which is None):
        before = None
        #iterate through the linked list:
        for _ in range(self.length):
            #move "after" to the next Node in the linked list:
            after = temp.next
            #this makes the "next" pointer to point backwards (before the head to begin with (None))
            temp.next = before
            #move "before" to the current Node (temp) in the linked list:
            before = temp
            #move "temp" to the next Node in the linked list:
            temp = after

#PRINT_LIST
# my_linked_list = LinkedList(4) # this does all of that above^
# # ^creates a head, creates a tail, points to the new node, assigns 4 to the node, and gives length of 1
# print(my_linked_list.head.value) #prints the node to terminal

#APPEND
# #create a linked list with a node of 1:
# my_linked_list = LinkedList(1)
# #append a node of 2 to the linked list:
# my_linked_list.append(2)
# #prints "12" because 2 is appended to the list
# my_linked_list.print_list()

#POP
# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# #(2) Items scenario - Returns 2 Node
# print(my_linked_list.pop())
# #(1) Item scenario - Returns 1 Node
# print(my_linked_list.pop())
# #(0) Items scenario - Returns None
# print(my_linked_list.pop())

#PREPEND
# #create a linked list with a node of 2:
# my_linked_list = LinkedList(2)
# #append a node of 3 to the linked list:
# my_linked_list.append(3)
# #prepend a node of 1 to the linked list:
# my_linked_list.prepend(1)
# #prints "123" because 1 is prepended to the list:
# my_linked_list.print_list()

#POP FIRST
# my_linked_list = LinkedList(2)
# my_linked_list.append(1)
# # (2) Items - Returns 2 Node
# print(my_linked_list.pop_first())
# # (1) Item - Returns 1 Node
# print(my_linked_list.pop_first())
# # (0) Items - Returns None
# print(my_linked_list.pop_first())

#GET
# my_linked_list = LinkedList(0)
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)

# print(my_linked_list.get(2))

#SET
# my_linked_list = LinkedList(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)
# #print the original linked list before using set method:
# my_linked_list.print_list()
# #change the value at index 1 to value of 4:
# my_linked_list.set_value(1,4)
# print("UPDATED LIST USING SET:")
# #print that updated linked list using set method:
# my_linked_list.print_list()

#INSERT
# my_linked_list = LinkedList(0)
# my_linked_list.append(2)
# #insert a node at index of 1 with a value of 1:
# my_linked_list.insert(1,1)
# my_linked_list.print_list()

# #REMOVE
# my_linked_list = LinkedList(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)
# #print the original linked list before using the remove method
# my_linked_list.print_list()
# print("THE REMOVED NODE USING REMOVE METHOD:")
# print(my_linked_list.remove(2), '\n')
# #print the updated linked list after using the remove method
# print("UPDATED LINKED LIST AFTER USING REMOVE METHOD:")
# my_linked_list.print_list()

#REVERSE
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
#print the original linked list before using the reverse method
print("ORIGINAL LINKED LIST BEFORE REVERSE METHOD:")
my_linked_list.print_list()
#print the updated linked list after using the remove method
print("UPDATED LINKED LIST AFTER REVERSE METHOD:")
my_linked_list.reverse()
my_linked_list.print_list()