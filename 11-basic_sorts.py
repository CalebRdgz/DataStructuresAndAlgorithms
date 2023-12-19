#BUBBLE SORT
#sort this list: [4, 2, 6, 5, 1, 3]
#Bubble-up the largest item in the list.
#compare two items next to each other, switch largest item to the right
def bubble_sort(my_list):
    #iterating through the list backwards:
    for i in range(len(my_list) - 1, 0, -1): #(5, go to 0, decrement)
        #compare all items in list for each iteration above^:
        for j in range(i):
            #if current item is greater than next item, swap them:
            if my_list[j] > my_list[j+1]:
                #store value in temp:
                temp = my_list[j]
                #make current value the next value:
                my_list[j] = my_list[j+1]
                #make the next value the stored value:
                my_list[j+1] = temp
    return my_list

print(bubble_sort([4, 2, 6, 5, 1, 3]))

#SELECTION SORT
#sort this list: [4, 2, 6, 5, 1, 3]
#need the indexes for selection sort
#look at first item, keep track of index where minimum value is
#current min_index = 0
#if next index has lowest value so far, min_index = 1
#if the actual min_index is at index 4, min_index = 4
#switch those values, so min_index is at beginning
def selection_sort(my_list):
    #loop through the list: (indexes 0-4)
    for i in range(len(my_list)-1):
        #min_index will be set to "i" for each loop:
        min_index = i
        #compare min_index to all other indexes after that:
        for j in range(i+1, len(my_list)): #(start value, end value)
            if my_list[j] < my_list[min_index]:
                min_index = j #j in the index that holds the lower value
            #dont swap if i == min_index:
            if i != min_index:
                #swap two items in the list:
                temp = my_list[i]
                my_list[i] = my_list[min_index]
                my_list[min_index] = temp
        return my_list

print(selection_sort([4,2,6,5,1,3]))

#INSERTION SORT
#always start with second item in list, and compare with item before
#if before is greater than current, swap current and before
def insertion_sort(my_list):
    for i in range(1, len(my_list)): #start at index 1, to end of list
        temp = my_list[i]
        j = i - 1 #j = index before index i
        #while temp is greater than the item before it and > -1
        while temp < my_list[j] and j > -1:
            #move the item before into the current empty spot:
            my_list[j+1] = my_list[j]
            #move the value stored in temp into the spot before
            my_list[j] = temp
            #move the j pointer to the next item in the list
            j -= 1
    return my_list

print(insertion_sort([4,2,6,5,1,3]))

#INSERTION SORT BIG O
#