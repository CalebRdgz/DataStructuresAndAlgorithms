#Heap example
#Looks like a Binary Search Tree and it IS a Binary Search Tree, but the numbers are not
#distributed in the same way

#Each node has a number that is HIGHER than it's children
#Highest number will always be at the top

#A Heap is a complete tree
#Complete = Fill from left to right at each level with no gaps
#Height of a tree is O(logn)

#Heaps are NOT good for searching
#Heaps ARE GOOD for keeping track of the largest number at the top to quickly remove it

#Huge difference in how to store Heap vs Binary Search Tree
#Heap is stored in a list (No Node class), only stores integers
#Store top heap node first in list, then go next level, then store left to right in list, and so on
#Common to make the first index of the heap the index of 1 instead of index of 0
#left_child = 2 * parent_index
#right_child = 2 * parent_index + 1
#better to make heaps start at index 1 instead of index 0 to make
#the math easier to understand

#Insert a value into a Heap
#The tree needs to be Complete, so put a node into an empty spot
#Insterting 100 into a heap:
#Add it to the end of the list, compare it to its parent
#(divide it's index by 2 to find its parent) swap the values if the
#parent is less than 100, same thing for the next parent node

#Helper Methods - Make code cleaner when we write insert and remove methods

#Instead of making the 0 index spot open, move the list over to the left
class MaxHeap:
    def __init__(self):
        #create empty list that is called "heap"
        self.heap = []
    
    #Helper Method: Gives us index of left child of a particular node
    #returns index of left child
    def _left_child(self, index):
        return 2 * index + 1
        
    #Helper Method: right child is always one more than the left child
    #returns the index of the right child
    def _right_child(self, index):
        return 2 * index + 2
    
    #Helper Method: parent is index / 2 with integer division
    #returns the index of the parent node
    def _parent(self, index):
        return (index - 1) // 2
    
    #Helper Method: swaps the values at index1 and index2
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    #Helper Method: sink down the node to the appropriate place in heap
    def _sink_down(self, index):
        #point max index to the input index
        max_index = index
        #break out of this while loop with a return statement
        while True:
            #left and right child nodes of the max_index input index:
            left_index = self._left_child(index)
            #this does NOT determine if its a valid number at right index
            right_index = self._right_child(index)
            #if left child index is greater than input index, make left child the parent
            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
                max_index = left_index
            #if right child index is greater than input index, make right child the parent
            #and if right_index is greater than the length of indexes in the heap
            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]):
                max_index = right_index
            #if max index is not equal to the input index, swap them:
            if max_index != index:
                self._swap(index, max_index)
                #set index to be equal to be max_index, moving the index pointer to max_index aswell
                index = max_index
            else:
                #break out of the method
                return


    
    def insert(self, value):
        #insert the new value to the end of the list:
        self.heap.append(value)
        #create current pointer at the new value:
        current = len(self.heap) - 1

        #while current index is greater than 0 and the value at 
        #current index is greater than value at parent of current
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            #swap the value at current index and parent of current
            self._swap(current, self._parent(current))
            #move current pointer to the parent of current(new value)
            current = self._parent(current)

    #cant have a complete heap if empty spot, so rearrange the heap
    #put something at the top and sink it down to its appropriate spot
    def remove(self):
        #empty heap
        if len(self.heap) == 0:
            return None
        #1 item in heap list
        if len(self.heap) == 1:
            #pops the 1 item in the heap and returns it
            return self.heap.pop()
        #get the max value in the heap which is at index 0:
        max_value = self.heap[0]
        #pop last item in the heap and move it to the first position
        self.heap[0] = self.heap.pop()
        #sink down that item we put at the top and put it at the
        #appropriate location in the heap
        self._sink_down(0)
        #return the max_value we removed
        return max_value

#INSERT METHOD
# myheap = MaxHeap()
# myheap.insert(99)
# myheap.insert(72)
# myheap.insert(61)
# myheap.insert(58)

# print("ORIGINAL HEAP")
# print(myheap.heap)

# myheap.insert(100)
# print("INSERT 100 TO HEAP")
# print(myheap.heap)

# myheap.insert(75)
# print("INSERT 75 TO HEAP")
# print(myheap.heap)

#REMOVE METHOD
# myheap = MaxHeap()
# myheap.insert(95)
# myheap.insert(75)
# myheap.insert(80)
# myheap.insert(55)
# myheap.insert(60)
# myheap.insert(50)
# myheap.insert(65)

# print("ORIGINAL HEAP")
# print(myheap.heap)

# myheap.remove()
# print("REMOVE FROM HEAP")
# print(myheap.heap)

# myheap.remove()
# print("REMOVE FROM HEAP AGAIN")
# print(myheap.heap)

#PRIORITY QUEUES
#If highest value is the highest priority, and always want to
#remove the highest value from a queue, then a heap is the best
#Could have a priority queue in a linked list, but will be much less
#efficient than a heap. Heap is only good for efficient Big O
#Heap will always be balanced because it will be complete
#BSTs will not always be balanced
