#Stack analogy:
#vertical can of tennis balls, when you push two tennis balls in the can,
#you cant get to the first one without first removing the second one
#same for three tennis balls, cant take the second one out without first removing the third
#LIFO - Last In, First Out

#ex. web browser, go to facebook, then youtube, then instagram, then email
#hit the back button to go back to each website

#O(n) (worse) when removing from left (beginning of list), 
#O(1) (better) when removing from right (end of list)

#with a stack, instead of head and tail, use top and bottom. (dont really use bottom)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        #with a stack, only removing from the top and not tracking whats happening at the bottom
        # self.bottom = new_node
        self.height = 1
    
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
    
    def push(self, value):
        #create new node using Node class and input value
        new_node = Node(value)
        #if stack is empty, point top to the new node
        if self.height == 0:
            self.top = new_node
        else:
            #point the new node to the current top:
            new_node.next = self.top
            #make the new node we created into the new top in the stack:
            self.top = new_node
        self.height += 1
    #remove top Node, point to to next node, detach old node from stack:
    def pop(self):
        if self.height == 0:
            return None
        #store top Node in temp:
        temp = self.top
        #make the next Node after top the new top of stack:
        self.top = self.top.next
        #detach old top from popped stack:
        temp.next = None
        #decrement stack height by 1
        self.height -= 1
        return temp


#CONSTRUCTOR
# my_stack = Stack(4)
# my_stack.print_stack()

#PUSH
# my_stack = Stack(2)
# my_stack.push(1)
# my_stack.print_stack()

#POP
my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)
print("original stack: ")
my_stack.print_stack()

my_stack.pop()
print("popped stack: ")
my_stack.print_stack()