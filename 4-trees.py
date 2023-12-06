#A linked list is just a Tree that doesn't fork.
#A linked list is a form of a Tree

#A Node looks like this:
# {
#     "value": 4,
#     "next": None
# }

#BINARY TREE

#A Binary Tree Node looks like this (Could have even more nodes connecting like branches on a tree):
# {
#     "value": 4, #<-------------- PARENT NODE
#     "left": { #<---------------- CHILD NODE (SIBLING)
#                 "value": 3,
#                 "left": None,
#                 "right": None
#             },
#     "right": { #<--------------- CHILD NODE (SIBLING)
#                 "value": 23,
#                 "left": None,
#                 "right": None
#             }
# }
#Full Tree - Every Node either points to 0 Nodes or 2 Nodes
#Non-Full Tree - Tree contains a Node that points to only 1 Node
#Perfect Tree - Any level in the Tree that has any Nodes is completely filled
#Can have a Full Non-Perfect Tree
#Complete Tree - Filling the tree from left to right with no gaps (Full and/or Perfect)
#Every Node can only have ONE Parent Node
#Child Nodes can also be Parent Nodes
#A Node that doesn't have any children is called a "Leaf"

#BINARY SEARCH TREE

#ex.) We have one parent Node(47) in our Tree, we want to add a new Node(76) to the tree
#With a Binary Search Tree, if the number in the new Node(76) is less than the parent Node(47), 
#it goes to the left of parent Node(47), if it's greater, it goes to the right of parent Node(47).
#Same thing happens with child Nodes.
#Every child Node that is less than it's parent Node will be on the left of that parent Node,
#Every child Node that is greater than it's parent Node will be on the right of that parent Node.

#BST - Big O
#1 Node in a Binary Search Tree = 2^1 - 1
#2 levels of Nodes in a BST = 2^2 - 1
#3 levels of Nodes in a BST = 2^3 - 1
#when we get to large numbers, the (- 1) is insignificant, so we can drop the (- 1) = 2^1, 2^2,...
#all of these are O(logn) = VERY Efficient (Divide and conquer)

#WORST CASE SENARIO: O(n) (like a linked list)
#If we had a Node, and the next is greater, the next is greater, on and on... (like a linked list)

#Linked List efficient Big O:
#merge sort
#insert() - O(1)

#BST efficient Big O:
#iterating through a list
#lookup() - O(logn)
#remove() - O(logn)

#BST Constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    #create an empty tree instead of creating a tree with a Node
    #insert a new Node using the insert method instead
    def __init__(self):
        self.root = None #root instead of head

    #insert a new node to the Tree:
    def insert(self, value):
        #create a new node
        new_node = Node(value)
        #if tree is empty, point root to the new Node
        if self.root is None:
            self.root = new_node
            return True
        #point temp to the root of the Tree
        temp = self.root
        #break out of this while loop by returning True or False:
        while (True):
            #compare that new node to the parent(temp) Node, Less than = Left, Greater than = Right
            #if the new node is equal to a parent node, return True or False
            if new_node.value == temp.value:
                return False
            #If the new Node is less than a parent Node, insert it on the left:
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            #If the new Node is greater than a parent Node, insert it on the right:
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    #check if a tree contains a perticular value:
    def contains(self, value):
        #if root == None, return False (don't need this since if it's empty, it wont contain it)
        if self.root is None:
            return False
        #temp = self.root
        temp = self.root
        #while temp is not None
        while temp is not None:
            #if value < temp.value = left
            if value < temp.value:
                temp = temp.left
            #elif value > temp.value = right
            elif value > temp.value:
                temp = temp.right
            #else (value == temp.value) = return True
            else:
                return True
        #value is not in the Tree, so return False
        return False


#INSERT METHOD
# my_tree = BinarySearchTree()
# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)

# print(my_tree.root.value) #returns Node 2
# print(my_tree.root.left.value) #returns Node 1
# print(my_tree.root.right.value) #returns Node 3

#CONTAINS METHOD
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.contains(27))
print(my_tree.contains(17))