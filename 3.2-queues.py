#we join a queue when we join a line
#if you were there first, you are the first one out of the line
#FIFO - First In, First Out
#when adding people to queue, use the term "EnQueue"
#when removing people from queue, use the term "DeQueue"
#ex. list: add on one end, remove on other end. 
#indexed list: removing/adding from the START = O(n) & removing/adding from the END = O(1)
#linked list: removing from END=O(n) adding to END=O(1) removing from START=O(1) adding to START=O(n)
#^Better to DeQueue from START of linked list and EnQueue from END of linked list (both O(1))

#instead of HEAD and TAIL, use FIRST and LAST

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
    
    def enqueue(self, value):
        #create new node:
        new_node = Node(value)
        #if empty queue, point the FIRST and LAST to the new node
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            #connect the new node to the end of the queue:
            self.last.next = new_node
            #make the new node the new last of the queue:
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        #store the first Node in temp:
        temp = self.first
        #if the queue only has 1 Node that we're removing, point first and last to None:
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            #make the next node the new first of the queue:
            self.first = self.first.next
            #detach the old first Node by pointing it to None:
            temp.next = None
        self.length -= 1
        return temp.value



#STACK CONSTRUCTOR
# my_queue = Queue(4)
# my_queue.print_queue()

#ENQUEUE:
# my_queue = Queue(1)
# my_queue.enqueue(2)
# my_queue.print_queue()

#DEQUEUE:
# my_queue = Queue(1)
# my_queue.enqueue(2)
# #TESTS:
# # (2) Items - returns 2 Nodes
# print(my_queue.dequeue())
# # (1) Items - returns 1 Node
# print(my_queue.dequeue())
# # (0) Items - returns None
# print(my_queue.dequeue())

