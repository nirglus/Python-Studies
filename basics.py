print("Hello")

#Creating variable by giving it a name
item = "bike"
country = "Belarus"
city = "London"
device = "iPad"
message = "Level Up"

#Strings in Python need to be surrounded by quotation marks.
"The Lord of the Rings"

#Math operations
print(7 + 3)
print(10 - 5)
print(5 * 3)
print(10 / 2)

budget = 20
print(budget + 10) # equals 30

price = 10
amount = 5
print(price * amount) # equals 50

score = 7 + 8
print(score) # equals 15
#Print variables on screen
username = "Magician"
score = 50
print(username)
print(score)

#! ------- Task -------
#Fix the bugs to show the following result on the screen
#name = Anna
#score -> 96
#print name
#print score
name = "Anna"
score = 96
print (name)
print (score)

#Python is a case-sensitive language, meaning "A" and "a" are treated as different.
#The next declared variables are 3 different variables
credit = 300
Credit = 280
CREDIT = 320
print(credit , Credit , CREDIT)

#Snake case is a popular way to create variable names in a consistent way.
#Snake case uses underscores _ to separate words in a variable name.
dog_name = "Archi"
print(dog_name)

#The input() instruction is the easiest way to allow a user to insert a value into your program.
message = input()
print(message)

#Inputs and outputs help machines communicate with the outside world.
#The input() instruction allows the user to enter a value into your program.
#The input() always turns the user input to a string, even if it's a number.
#The print() instruction is used to generate an output.

#! ----- Data Types ------
# Strings - surrounded by " " or ' '
# Integers - whole numbers without a decimal point. They can be positive, negative or zero. 
# Float - data type for numbers with decimal places, they can be positive or negative.
print(3 + 5) # = 8
print("Iron" + "Man") # = "IronMan" // it's called concatenation.

name = input()
message = "Nice to meet you, " + name
print(message)

#To check a type of data, use type() instruction
car = "Peugeot"
type(car) # = class 'str'

#Division of two integers ALWAYS produce a float.
a = 9
b = 3
c = a / b
print(c) # = 3.0
print(type(c)) # = <class 'float'>

#To convert a value from any type to integer we use the int() instruction.
a = "55" 
b = int(a) # converts "55" to 55
print(b) # prints 55

user_age = int(input())
print(user_age) # prints user_age as an integer.

#To convert a value from any type to a float we use the float() instruction.
a = 8
b = float(a) # converts 8 to 8.0
print(b) # prints 8.0

#To convert a value from any type to a string we use the str() instruction.
a = 5.2
b = str(a) # converts 5.2 to "5.2"
print(b) # prints "5.2"

# Explicit conversions are conversions done by us with str(), float(), int().
# Implicit (automatic) conversions are done by by the system engine.

#! --------- Task ----------
#Complete the code to take the savings, calculate the end amount, then display a message on the screen

# Asks the user to enter the savings
savings = input()

# Convert the user input into a float value and update the variable
savings = float(savings)

# Savings grow after 1 year at a 5% annual interest rate
balance = savings * 1.05 

# Convert the balance into a string and update the variable
balance = str(balance)

# Concatenate the 2 strings to produce a message
message = "Amount in 1 year: " + balance

# Display the message
print(message)

#! ------- Comparisons -------
print(20 > 84)
print(30 < 65)
print(40 == 40)
print(type(34 > 85)) # prints <class 'bool'>
print(True and False) # prints False
print(False and True) # prints False
print(True or False) # prints True
print(False or True) # prints True
heart_rate = 60
peak_rate = heart_rate > 85
print(peak_rate) # prints False
# True and False always start with an uppercase letter.
# or & and are always lowercase letters. 
# Otherwise it will cause an error.
b = (5 > 4) or False
print(b) # prints True

#! ----------- for loop -----------
#for loop is used to execute the same instruction over and over again, a specific number of times.
#range() function creates 5 numbers in a sequence, starting from 0.
for i in range(5):
    print("Hello there")
# The code that gets repeated in the for loop must be indented. Indentation is the spaces at the beginning of lines.
# for i in range(5):
# print("Hello")  # This wont work

#! ----------- while loop -----------
# While loops repeat code whilst a condition holds true.
cars = 5
while cars > 0:
    print("Sell car")
    cars = cars - 1
# Like for loops, while loops also should contain colon : and be indented.
# Best practice is to use for loops when we know the number of iterations,
# and while loops for when there is a condition that needs to be met.

#! ----------- Conditional statements -----------
# Conditional statments, if-else allows the program to perform different actions based on the condition.
age = 15
if age >= 18:
    print("Access allowed")
else:
    print("Access denied")

# You can use the elif statement (short for "else if") to check for more conditions if the first condition is not met.
if age < 18: 
  print("Junior discount")
elif age >= 75: 
  print("Senior discount")
else:
  print("No discount")

# if-else statments can be nested in each other.
is_student = True
if age < 18:
   if is_student:
      print("30% discount")
   else:
      print("20% discount")  
else:
   print("Regular price")

#! -------- Task ---------
# Complete the given code to display different messages to the patient based on the blood sugar levels
# Glucose level is an input for this software
glucose_level = int(input())

# Display message if glucose level is less than 70
if glucose_level < 70:
  print("Low glucose level")

# Display message if glucose level is greater than 140
elif glucose_level > 140:
  print("High glucose level")

# Display message if none of the conditions above are met
else:
  print("Normal range")

#! ----------- Collections -----------
# Lists allow you to store a collection of multiple values in a single variable.
# Lists can store any data type, and they can contain different types in same list.
bag = ["notebook", "pen", "food", "computer"]
prices = [2.99, 0.95, 4.5, 18.99]
car_info = ["Pontiac", 1985, 5550.5]
movies = [
   "The Godfather",
   "Fast & Furious",
   "Scarface",
   "Hobbs & Shaw"
]
print(movies)
# To refer to a specific item in list, we use list index. It always starts with 0.
print(movies[0])
print(movies[2])
# Also you can store a specific item in a new variable.
my_fav_movie = movies[1]
print(my_fav_movie)
# It's also possible to change item's value in a list after it has been created.
movies[3] = "8 Mile"
print(movies[3])
#Lists can store values of variables
name = "Brian"
age = 30
country = "United Kingdom"
info = [name, age, country]
print(info) # prints the list with the variables values

#Index also works with strings.
car = "Volvo"
print(car[2]) # prints 'l'

# You can NOT change the characters in a string. If you try to do so, you'll get an error.
computer = "Lenovo"
computer[0] = "S" # returns error

# Slicing allows you to extract a portion of a list. Starting and stopping indexes are separated by a colon : 
car_brands = ["Mercedes", "BMW" , "Honda", "Ferrari", "Alfa Romeo", "Pagani"]
print(car_brands[1:4]) # Prints from the [1] index (included) till the [4] index (excluded) 
# Same works with a string
name = "Jackson"
print(name[0:4]) # Prints "Jack"
#It's also possible to omit the start point, it will just start from the 0 index.
print(name[:4]) # Prints "Jack"
#It's also possible to omit the stop index, it will end at the last index.
print(name[1:]) # Prints "ackson"

# Python supports "indexing from the end", called negative indexing.
# This means the last value of a sequence has an index of -1.
bag = ["notebook", "pen", "food", "computer"]
print(bag[-1]) # Prints "Computer", the last item in the list.
print(bag[-2]) # Prints "food"
c = ['$', '£', '€', '¥']
print(c[-2:]) # Prints the last two items ['€', '¥']
c = ['$', '£', '€', '¥']
print(c[1:-1]) # Prints the two middle items ['£', '€'] because the indexes goes like this:
# [-4(0), -3(1), -2(2) , -1(3)]
# So it starts on the 1 index and ends on the -1 (3) index (exclusively)
c = ['$', '£', '€', '¥']
c[:2] = ['₣', '฿'] # Change the values of the two first items on list.
print(c) # Prints ['₣', '฿', '€', '¥']

#! ----------- Functions -----------
# Functions perform tasks, we saw already print(), type() and input().
print("Your seat:", 4)
# NOTE: Two arguments in print func, printed with a space between them
# print() accepts any type of arguments, range() accepts only integers
# A function can be an argument for another function.

#! ----------- String Functions -----------
# The functions upper() and lower() allow you to quickly change the case of a string
# to all in uppercase or lowercase, respectively.
print("VoLkSWaGeN".upper()) # Prints "VOLKSWAGEN"
print("VoLkSWaGeN".lower()) # Prints "volkswagen"

# capitalize() function converts the first character in a string to uppercase.
print("volkswagen".capitalize()) # Prints "Volkswagen"
print("VOLKSWAGEN".capitalize()) # Prints "Volkswagen"

# The find() function checks if a character (or a pattern of characters) is present in a string.
# find() returns the index of the given value, and if it appears more than once, the function will 
# return the first occurrence.
# find() will return -1 if the value can't be found in the string.
"Ferrari".find("r") # Returns 2
"Ferrari".find("ri") # Returns 5
"Ferrari".find("o") # Returns -1

#! ----------- List Functions -----------
# len() is one of the most useful built-in functions. 
# len means length and it returns the number of items in a list.
bands = ["Linkin Park", "AC/DC", "Beatles", "Arctic Monkeys"]
len(bands) # Returns 4
# len() can also be used on strings
print(len("Metallica")) # Prints 9
band = "Kiss"
print(len(band)) # Prints 4
print(len(bands[2])) # Prints the length of "Beatles" = 7

# The append() function adds a new item to the end of a list. 
# append() is called using dot notation because it’s specific to lists.
bands.append("Coldplay")
print(bands)

# The insert() function allows you to add an element to a list, at a specific position.
items = ["pen", "key", "notebook", "pencil"]
items.insert(2 , "ruler") # Inserting "ruler" in the place of index 2 of items.
print(items) # Prints ['pen', 'key', 'ruler', 'notebook', 'pencil']

# The pop() function removes an element from a list.
# That position indicated by the index is the only argument that the pop() function accepts.
items.pop(2) # Removes the item with index 2
print(items) # Prints ['pen', 'key', 'notebook', 'pencil'] NOTE: 'ruler' was removed.

#! ----------- Custom Functions -----------
# Use def followed by a name to define a new function
# The body of a function contains the reusable code that is executed when the function is called.
# The code for the body of a function must be indented.
# When a function is defined, you need to make sure parentheses () are added after the name. 
# A colon : must be added at the end of the definition line.
def greet(): 
  print("Hello from a function")
  print("Have a great day")
greet()
# A function might require arguments to complete its tasks. 
# Arguments are put inside the parentheses () following the function name.
def personal_greet(name): 
  print("Hello", name)
  print("Have a great day")
personal_greet("Anna")
# NOTE: Functions must be defined before they can be called. 
# The result of a function can be sent back with the return statement. 
# This is particularly helpful when you need to continue using the result value in your program.
def bmi(weight, height):
    index = weight / (height * height)
    return index
#  function can return multiple values.
def rect(length, width):
  area = length * width
  perimeter = 2 * length + 2 * width
  return area, perimeter
# When a function returns multiple values, they can be stored in multiple variables.
a,b = rect(50, 100)
# You can create mulitple variables in 1 statement.
x, y = 4, 9
print(x, y)
# Python allows function arguments to have default values. 
# If the function is called without the argument,
#  the argument gets its default value
def greet(name="Guest"):
  print("Welcome", name)

greet() # Welcome Guest
greet("John") # Welcome John
#NOTE A function can return multiple values
#NOTE Defining a function also decides the data types it can take in, handle and return
#NOTE Default values make arguments optional

# Dictionaries
# Python provides a number of built-in collection types, to store multiple values.
# Like lists, Dictionaries are another collection type and allow you to map arbitrary keys to values.
# Dictionaries can be indexed in the same way as lists, using square brackets containing keys.
ages = {
   "Sophie": 24,
   "Jonas": 32,
   "Enrique": 57
}
print(ages["Sophie"]) # prints 24
print(ages["Enrique"]) # prints 57
# Each element in a dictionary is represented by a key:value pair.

#! ----------- Task -------------
# Your program needs to take the key as input and output the corresponding value.
car = {
    'brand':'BMW',
    'year': 2018,
    'color': 'red',
    'mileage': 15000
}
def getValue(key):
    print(car[key])

#! ---------- Dictionary Functions ------------
# To determine whether a key is in a dictionary, you can use in and not in,
# just as you can for a list.
nums = {
  1: "one",
  2: "two",
  3: "three",
}
print(1 in nums) # prints True
print("three" in nums) # prints False
print(4 not in nums) # prints True

# A useful dictionary function is get. It does the same thing as indexing, but if 
# the key is not found in the dictionary it returns another specified value instead.
pairs = {
   1: "apple",
   "orange": [2, 3, 4], 
   True: False, 
   12: "True",
}

print(pairs.get("orange")) # prints [2, 3, 4]
print(pairs.get(7, 42)) # prints 42
print(pairs.get(12345, "not found")) # prints not found
# When using the get() method with a dictionary, you can specify a default value
# to be returned if the key you're looking for is not found in the dictionary.

#! ---------- Tuples -----------
# Tuples are very similar to lists, except that they are immutable 
# (they cannot be changed).
# Also, they are created using parentheses, rather than square brackets.
words = ("spam", "eggs", "sausages")
print(words[2]) # prints "sausages"

# Tuples can be created without the parentheses by just 
# separating the values with commas.
my_tuple = "one", "two", "three"
print(my_tuple[0]) # prints "one"

tuple = (1, (1, 2, 3))
print(tuple[1])

# To create a one item tuple, add a comma after the item:
one_item_tuple = ("item" ,) # without comma it's a string
print(type(one_item_tuple)) # prints Tuple

#! ----------- Task ----------
""" 
You are given a list of contacts, where each contact is represented by a tuple, 
with the name and age of the contact.
Complete the program to get a string as input, 
search for the name in the list of contacts and output the age of the contact in the format presented below:

Sample Input
John

Sample Output
John is 31
If the contact is not found, the program should output "Not Found".
"""
contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]
def check_name(name, contacts):
    for i in contacts:
        if name == i[0]:
            name = name + " is "  + str(i[1])
            return name
    return "Not Found"        
    
print(check_name(input(), contacts))

#! ----------- Tuple Unpacking -----------
# Tuple unpacking allows you to assign each item in a collection to a variable.

numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

# This can be also used to swap variables by doing a, b = b, a , since b, 
# a on the right hand side forms the tuple (b, a) which is then unpacked.

# A variable that is prefaced with an asterisk (*) takes all values from the collection
#  that are left over from the other variables.
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a) # prints 1
print(b) # prints 2
print(c) # prints all values from 3 to 8
print(d) # prints 9

#! ----------- Sets -----------
# Sets are similar to lists or dictionaries.
# They are created using curly braces, and are unordered, which means that they can't be indexed.
# Due to the way they're stored, it's faster to check whether an item is part of a set using the in operator, 
# rather than part of a list.
num_set = {1, 2, 3, 4, 5, 6}
print(3 in num_set) # prints True
#! Sets cannot contain duplicate elements.
# You can use the add() function to add new items to the set, and remove() to delete a specific element:
nums = {1, 2, 2, 3, 2, 4, 5, 6}
print(nums)
nums.add(-8)
nums.remove(3)
print(nums)
print(len(nums))
#! Duplicate elements will automatically get removed from the set.
# NOTE - True and 1 will count as the same element.
# NOTE - False and 0 will count as the same element.
# The len() function can be used to return the number of elements of a set.
"""
Sets can be combined using mathematical operations.
The union operator | combines two sets to form a new one containing items in either.
The intersection operator & gets items only in both.
The difference operator - gets items in the first set but not in the second.
The symmetric difference operator ^ gets items in either set, but not both. """
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second) #! prints {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(first & second) #! prints {4 ,5, 6}
print(first - second) #! prints {1, 2, 3}
print(second - first) #! prints {7, 8, 9}
print(first ^ second) #! prints {1, 2, 3, 7, 8, 9}

# ------- Removing items in sets
# To remove an item in a set, use the remove(), or the discard() method.
# NOTE: If the item to remove does not exist, remove() will raise an error.
# NOTE: If the item to remove does not exist, discard() will NOT raise an error.
# You can also use the pop() method to remove an item, but this method will remove a random item, 
# so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.
# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) # prints set()

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) # error: thisset is not defines

#! ----------- List Comprehensions -----------
# List comprehensions are a useful way of quickly creating lists whose contents obey a rule.
cubes = [i**3 for i in range(5)]
print(cubes) #! prints [0, 1, 8, 27, 64]
# List comprehensions are inspired by set-builder notation in mathematics.
# A list comprehension can also contain an if statement to enforce a condition on values in the list.
evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens) #! prints [0, 4, 16, 36, 64]
# evens is a list created by a list comprehension. For every item in the range of 0 to 9, the item is squared. 
# However, we only add that item to the list if the item to the power of 2 
# (squared item) divided by 2 has a remainder of 0.

#! ----------- Data Types Conclusion -----------
# Python supports the following collection types: Lists, Dictionaries, Tuples, Sets.

#! When to use a dictionary:
# - When you need a logical association between a key:value pair.
# - When you need fast lookup for your data, based on a custom key.
# - When your data is being constantly modified. Remember, dictionaries are mutable.

#! When to use the other types:
# - Use lists if you have a collection of data that does not need random access. 
# Try to choose lists when you need a simple, iterable collection that is modified frequently.
# - Use a set if you need uniqueness for the elements.
# - Use tuples when your data cannot/should not change.

#! Many times, a tuple is used in combination with a dictionary, 
#! for example, a tuple might represent a key, because it's immutable.
nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42))) # prints 44

#! ----------- Functional Programming -----------
# Functional programming is a style of programming that 
# (as the name suggests) is based around functions.
# A key part of functional programming is higher-order functions. 
# Higher-order functions take other functions as arguments, or return them as results.
def apply_twice(func, arg):
   return func(func(arg))

def add_five(x):
   return x + 5

print(apply_twice(add_five, 10)) # prints 20
# The function apply_twice takes another function as its argument, and calls it twice inside its body.

# In Python, and in programming in general, functions are categorized as either pure or impure based 
# on their behavior.
# Pure Functions:
#! Pure Functions
#!  - A pure function is a function that always returns the same output for the same input.
#!  - It doesn't have any side effects, meaning it doesn't modify any external state or variables.
#!  - Pure functions are predictable and easy to test because they don't rely on external factors.
#!  - They are ideal for functional programming paradigms.
#!  - Examples of pure functions in Python include mathematical operations, string manipulation, and functions that only use their input parameters.
   
#!  Impure Function

#! - An impure function is a function that can produce different outputs for the same input or has side effects.
#! - Side effects can include modifying global variables, printing to the console, or performing I/O operations.
#! - Impure functions might depend on external state that can change.
#! - They are less predictable and harder to test in isolation.
#! - Many real-world functions, such as those interacting with databases or user interfaces, are impure.
# ------------ Example ------------
# Pure Function
def add(a, b):
    return a + b

# Impure Function
total = 0  # External state

def add_to_total(value):
    global total  # Modifies an external variable
    total += value

# Pure functions are called with the same arguments and produce the same results.
result1 = add(2, 3)  # Result is always 5
result2 = add(2, 3)  # Result is still 5

# Impure functions can have side effects and might produce different results.
add_to_total(5)  # Modifies 'total' variable
add_to_total(3)  # Modifies 'total' variable differently

#! ----------- Lambda -----------
# Lambda functions in Python are small, anonymous functions used for simple tasks. 
# They are created with the lambda keyword, typically for one-line operations, 
# and often used in functional programming constructs like map, filter, and reduce. 
# They are best suited for short, single-expression tasks.
# ------------ Example ------------

# Regular function
def add(x, y):
    return x + y

# Equivalent lambda function
add_lambda = lambda x, y: x + y

result = add(3, 5)
result_lambda = add_lambda(3, 5)

print(result)         # Output: 8
print(result_lambda)  # Output: 8

#! ----------- Map -----------
# The built-in functions map and filter are very useful higher-order functions that operate
# on lists (or similar objects called iterables).

# The function map takes a function and an iterable as arguments, 
# and returns a new iterable with the function applied to each argument.
def add_five(x):
  return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result) # prints [16, 27, 38, 49, 60]

# We could have achieved the same result more easily by using lambda syntax.
nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x+5, nums))
print(result)
# To convert the result into a list, we used list explicitly.

#! ----------- Filter -----------
# The function filter filters an iterable by leaving only 
# the items that match a condition (also called a predicate).

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res) # prints [22, 44]
# Like map, the result has to be explicitly converted to a list if you want to print it.