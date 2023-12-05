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

