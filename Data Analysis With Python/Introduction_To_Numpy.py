import numpy as np
#LESSON_4
my_list = [1,2,3,4]
#Typecasting a list in an numpy array
arr = np.array(my_list)
print(type(arr))
print(type(my_list))
#This can also be done for double lists
matrix = [[1,2,32],[1,6,8],[23,7,8]]
matrix_np = np.array(matrix)
print(type(matrix))
print(type(matrix_np))
#Creation of matrices in numpy
arr1 = np.arange(0,10)#excluding the last number from 0-9
arr2 = np.arange(0,9,2)
print(arr1)
print(arr2)
#special matrices in numpy
arr3 = np.zeros((2, 3)) #creates a zero matrix with two lines and three cols
print(arr3)# the argument is a tuple with the lines,columns
arr4 = np.ones((4,4))
print(arr4)
#Linspace creates evenly points in the axis of the starting to the ending point
lin = np.linspace(0,10)
print(lin)
print(np.arange(10))
#the main concept of linspace(start,end,num_of_points) is to create num_of_points evenly distributed between the starting and the ending point
#identity matrix
eye_mat = np.eye(3)
print(eye_mat)
#arrays of random numbers
arr = np.random.rand(3,3)#uniform distribution from 0 to 1
arr1 = np.random.randn(4,4)#from a standard distribution around 0
arr2 = np.random.randint(1,100,(2,2))#random int from the high to low and then the size of the array
print(arr)
print(arr1)
print(arr2)
#Creation of a standard and a random matrix
arr = np.arange(10)
ran_arr = np.random.randint(0,45,10)
#methods
arr = arr.reshape(2,5)
print(arr)
arr = arr.reshape(5,2)
print(arr)
#please keep in mind that the product of dimensions of the reshape must be the same with the initial shape
arr_max = ran_arr.max()
arr_min = ran_arr.min()
#to get the index of the min or max use argmax/min
min_index = ran_arr.argmin()
max_index = ran_arr.argmax()
#to get the shape of the np.array use shape method
print(arr.shape)

#LESSON_5:
#The slicing of the array is the same as the lists
arr = np.array([1,2,3,4,5,7,8,9,10])
#if i slice the array and then i change its values the initial array changes also because this is not a copy but a reference
print(arr)
slice_arr = arr[2:5]
print(slice_arr)
slice_arr[:] = 20
#print(slice_arr)
print(arr)
#should we want to save it as a copy we need to use the copy method
arr_new = arr.copy()
print(arr_new)
#slicing and indexing in 2d arrays
arr_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
#printing the array
print(arr_2d)
#choosing the second row
print(arr_2d[1])
#print the two first rows 
print(arr_2d[:2])
#print a single element let's say seven
print(arr_2d[2,0])#in one bracket row,column
print(arr_2d[1: , :2])#this prints the last two rows and from them the first two cols
#the result is [4 5 7 8] with shape 2x2
print(arr_2d[1: , :2].shape)
#Conditional slicing
#we can slice tha matrix by using a condtition lets say we want the even numbers from 0 to 30
mat = np.arange(30)
evens_to_thirty = np.arange(30)%2==0#boolean matrix
print(mat[evens_to_thirty])
#alternative
print(mat[mat%2==0])
#LESSON 6
#to perform bitwise operations between np.arrays we simply use the symbols +-/* and should we want scalar
#we just perform the action and the numpy module converts it to array-array operations
#some opeartions like the division with zero may not end up in errors but in warnings like 0 / 0 is nan and log 0 is -inf
