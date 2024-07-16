import numpy
#LESSON_1
#basic arithmetic operations
#addition
print(1+3)#it will print the result of the addition of two int64 numbers
#multiplication
print(7*9)
#division
print(45/8)#floating result
#exponential
print(2 ** 4)
#modulo
print(7 % 3)
#formatting the output of the text in the console
name = "Nikos"#string, can also be declared with ''
age = 12
print("Hello my name is {} and I am {} years old".format(name, age))
#an alternative is the following
print("Hello my name is "+name+" and I am "+str(age)+" years old")
#indexing slicing
string = "Camouflage"
#print the first letter of the string is like getting its first element starting at 0
print(string[0])
#print the last one its index is -1
print(string[-1])
#print the substring from the 2nd to the 5th letter
print(string[1:4+1])
#we can also reverse the string
print(string[::-1])
#the most general form is start:end:step and the end is excluding, meaning that the last element is not included
print(string[5:8+1])
#print all the string
print(string[0:])
print(string[:5])#it will print every letter from the start to 5-1=4th letter
list_1 = []#create an empty list
#a list contains whatever it wants
#we can use .append to add an element to the end of it
list_1.append("Apple")
print(list_1)
list_1.append("Banana")
print(list_1)
list_1.append("Peach")
print(list_1)
#we can slice the list like doing with every other way we did in the strings
#we can also change an element in a list
list_1[1] = "Mango"
print(list_1)
new_list =  ["Blueberry","Raspberry", list_1]
print(new_list)
#to grab an element from it we need to grasp that the object in second index is a list and if we want an inner component of that list we need to index again inside it
print(new_list[2])#the result is a list 
print(new_list[2][:2])#print(apple,mango)
#simple exercise find and print the target
example = ["Pete", "Maria", ["Nikos", "Jake", ["Thomas", "Target"]]]
#print(example[2][2][-1])
answer = example[2][2][-1]
if answer == "Target":
	print("You correctly found the target!")
else:
	print("Try again!")
#LESSON_2
#dictionaries
dict = {'key1':'value1', 'key2':'Value2'}
#this is a structure which is addressible by keys so if we want the second value we would like to grab the value for the second key
print(dict['key2'])
#the value can be everything you want maybe a list 
new_d  = {'Animals':['Elephant', 'Cat', 'Dog'], 'Fruits':list}
print(new_d['Animals'])
print(new_d['Fruits'][2])#print the third fruit
#a more complex example
#customers name,age,country
customers = {'name':['Nikos', 'Thomas', 'Jenny'],'age':[35, 58, 22], 'country':['Greece', 'Thailand', 'Italy']}
print("The second customer is named {} and he is {} years old and he is coming from {}".format(customers['name'][1], customers['age'][1], customers['country'][1]))
outer_dict = {'Key1':{'InnerKey1':[4,7,0]}, 'Key2':{"InnerKey2":[5, 8 ,9]}}
#the above is a dictionary of dictionaries
#we want to print 8
answer1 = outer_dict['Key2']['InnerKey2'][1]
if answer1 == 8:
	print('Success')
else:
	print("Try again!")
#Boolean values are True and False
#Tuples and Sets
#For the tuple we use parentheses instead of []
#The main difference of tuples and lists is that the ;atter is mutable meaning that we can change its contents but tuples are not
tup = (1,2,4,5)
#the indexing is the same but tup[1]=7 is not allowed
#Lists->mutable tuples->immutable
#Set is a collection for unique elements
example_set = {1,4,7,8,9}
dummy_set = {1,12,1,1,1,12}
#we can also grab the unique elements from a list and transfer them in to a set
dummy_list = [1,1,1,1,1,1,2,2,2,2,2,4,4,4,4]
new_set = set(dummy_list)
#new_set = set([1,1,1,1,2,2,2])  
print(dummy_list)
print(new_set)
#we can add an element by using the add method
new_set.add(9)
print(new_set)
#Comparisons have as a result a boolean output meaning True or False
#For and while loops
sequence = [1,2,3,4,5,6,7,8,9]
for seq in sequence:
    print(seq)
#simple example with dictionaries
squares = {}
for seq in sequence:
    #print("-----------------------------")
    squares[seq] = seq**2
print(squares)
#Range function(if the first parameter is omitted then it is 0)
list_sq = []
for x in range(1,9+1):
    list_sq.append(x**2)
print(list_sq)
#List Comprehension
sq_list = [x**2 for x in range(1,9+1)]
print(sq_list)
#Foruth power
fourth_sq_list = [x**2 for x in sq_list]
print(fourth_sq_list)
#Function
def square(x):
    return x**2
alternative_sq_list = [square(x) for x in fourth_sq_list]
print(alternative_sq_list)
#To pass a default value parameter in the function we can write def square(x=2)andinside the main body of it we can change it 
#fibonacci
def fibonacci(n):
    """
    This is a fibonacci function
    """
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for x in range(10):
    print(fibonacci(x))
    print("##################")
#map function creates an iterator in order a function to be applied in a sequence
print(list(map(fibonacci,sequence)))
#lambda expression instead of a function(anonymous function)
third_pow = lambda x : x**3
print(third_pow(5))
#lambda can also be used with map
print(list(map(lambda x: x**3,sequence)))
#Filter method about filtering elemnts from a sequence
print(list(filter(lambda num: num%2==0, sequence)))
#LESSON_3
#String methods
string.lower()#makes everything lowercase
string.split()#creates a list with every word split by a " "
#as an argument we can decide which character is the delimiter of the message
string.upper()#uppercase all the letters
#Methods of dictionaries
dict_keys = dict.keys()#keys of the dictionary
dict_items = dict.items()#the pairs of the dictionary
dict_values = dict.values()#returns the values of the key
#Methods of lists
lst = [1,2,3,4,5,6]
lst.pop()#removes the last item of the list
for x in range(5):
    print("The element popped is {}".format(lst.pop()))
print("The list is finally empty!")
#as an argument in pop we can pop the index of the element we want to remove
tuple_list = [(1,2,4), (3,4,5), (1,5,8)]
for a,b,c in tuple_list:
    print(a+b+c)
