#hash tables explained:
#built in hash table - (dictionary) = "key": value pair
#{"nails": 1000}: "nails" is the key, 1000 is the value
#use hash function/method to perform a hash on the key to get an address which is 
#returned from the hash function
#a hash function is ONE WAY meaning once we get the address, we cant take it away
#hash is deterministic, every time we put nails in, we get 2 every time
#even though python has hash tables already, were creating our own
#ex.) Hardware Store
#"key": value pair
#{"nails": 1000} <-- run this through a hash method, perform a hash on the key, 
#and get an address(index) where we store that key value pair
#a hash is ONE WAY - pass "nails" through the hash and get 2, cant go backwards
#hash is DETERMINISTIC - every time we put "nails" through the hash, we will always get 2

#COLLISIONS
#Collision - Putting a key: value pair at an address where there already is another key: value pair
#ex.) address 2: [ ['nails', 1000], ['nuts': 1200] ]
#Linear Probing(open addressing) - keep going down the list until you find an empty spot
#Separate Chaining - more than one key: value pair in one address
#instead of lists, can have linked lists in each address, go to address 2 and iterate linked list

#HASH TABLE COMMON INTERVIEW QUESTION:
#2 lists, determine if they have an item in common
#GOOD WAY:
#when you look for an item using it's key, its O(1)
def item_in_common(list1, list2):
    # create an empty dictionary to store list1's values
    my_dict = {}
 
    # iterate through list1 and add each value to the dictionary as a key
    for i in list1:
        my_dict[i] = True
 
    # iterate through list2 and check if each value is a key in the dictionary
    for j in list2:
        # if a value in list2 is also in the dictionary, return True
        if j in my_dict:
            return True
 
    # if no values in common are found, return False
    return False

#BAD WAY:
# def item_in_common(list1, list2):
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 return True
#     return False

list1 = [1,3,5]
list2 = [2,4,5]

print(item_in_common(list1, list2))

#HASH TABLE CONSTRUCTOR
#should always have a prime number of addresses, it increases the randomness
#constructor only builds the list 0 - 6
class HashTable:
    def __init__(self, size = 7): #size is defaulted to 7 (in case size is not initialized)
        #call the list "data_map", creates list with 7 items that contain None
        self.data_map = [None] * size
    
    def __hash(self, key):
        #initialize variable "my_hash" to 0
        my_hash = 0
        #loop through the letters in the KEY, which is what we passed in the hash method
        for letter in key:
            #ord(letter) gets the ASCII of each letter, 23 is prime number, mod gives remainder
            #length is 7, so we get remainder of 1
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    #set a key: value pair in our hash table
    def set_item(self, key, value):
        #pass the key in the hash method and save that in the index variable
        index = self.__hash(key)
        #if the spot in the list is empty, store the empty array there
        if self.data_map[index] == None:
            #set the empty list in the index in "data_map" which is the list
            self.data_map[index] = []
        #if the address has an empty list, append key and value to that empty list
        self.data_map[index].append([key, value])
    
    #get an item from our list using the key of that item
    def get(self, key):
        #figure out the index for that key ("washers")
        index = self.__hash(key)
        if self.data_map[index] is not None:
            #iterate through that list inside of the index in the hash table
            for i in range(len(self.data_map[index])):
                #find a match: [i] = current iteration in the index [0] = the key
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    #take all of the keys in the hash table, put them in a list, and return that list
    def keys(self):
        #empty array to store keys
        all_keys = []
        #iterate through the data map list (0 - 6)
        for i in range(len(self.data_map)):
            #only if there is something in that spot, loop through the items in that index
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    #append the keys in that index to the all_keys array
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

#KEYS
# my_hash_table = HashTable()
# my_hash_table.set_item('bolts', 1400)
# my_hash_table.set_item('bolts', 50)
# my_hash_table.set_item('lumber', 50)
# print(my_hash_table.keys())