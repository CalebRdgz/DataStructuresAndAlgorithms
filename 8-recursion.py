#Topic that takes a few times looking at this before understanding
#Recursion - A function that calls itself, until it doesn't
#ex.) A method that opens a gift box, that contains another gift box, the method opens that gift
#box, which contains another gift box, the method opens that gift box that contains a basketball
#Pseudo Code:
# def open_gift_box(): #Create the function
#     if ball: #If when we open the box, it contains a ball, return that ball. If not, open_gift_box()
#         return ball #Returning the ball that was in the box
#     open_gift_box() #This is where the open_gift_box() function calls itself if ball not found

#The process of opening each new box is the same
#Each time we open a box, we make the problem smaller
#If there is no if/return statement or the if statement will never be true, stack overflow error

#Call Stack
#explanation using non-recursive functions:
#After funcThree prints out 'Three', funcTwo will print 'Two', and THEN funcOne will print 'One'
# def funcThree():
#     print('Three') # 4 - funcThree added to call stack (printing 'Three' next)

# #funcTwo prints out 'Two' ONLY AFTER funcThree is finished printing 'Three'
# def funcTwo():
#     funcThree() # 3 - funcTwo added to call stack (calling funcThree() in funcTwo)
#     # 5 - funcThree popped from call stack AND 'Three' printed to console
#     print('Two') # 6 - printing 'Two' next

# #funcOne prints out 'One' ONLY AFTER funcTwo is finished printing 'Two'
# def funcOne():
#     funcTwo() # 2 - funcOne added to call stack (calling funcTwo() inside funcOne)
#     # 7 - funcTwo popped from call stack AND 'Two' printed to console
#     print('One') # 8 - printing 'One' next
#     # 9 - funcOne popped from call stack AND 'One' printed to console

# # 1 - Calling funcOne to kick all of this off
# funcOne()

#FACTORIAL example to teach RECURSION
# 4! = 4 * 3 * 2 * 1
# 3 * 2 * 1 = 3!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1

#Recursive function for factorial:
#Passing 4 as 'n'
def factorial(n):
    #if 4 == 1, return 1
    if n == 1:
        return 1
    # 4 != 1, so return 4 * factorial(4-1) (4 * 3!)
    return n * factorial(n-1)

print(factorial(4))