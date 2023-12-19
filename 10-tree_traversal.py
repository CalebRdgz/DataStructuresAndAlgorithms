#Recursive Binary Search Trees

#Contains
#double underscore because user wont call this directly
def __r_contains(self, current_node, value):
    #empty BST:
    if current_node == None:
        return False
    #value is in the tree:
    if value == current_node.value:
        return True
    #value we looking for < current_node, return __r_contains
    #on current_node.left and pass the value we looking for
    if value < current_node.value:
        return self.__r_contains(current_node.left, value)

#user will call this method directly instead:
def r_contains(self, value):
    return self.__r_contains(self.root, value)