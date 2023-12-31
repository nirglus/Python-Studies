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

#! ----------- Generators -----------
# Generators are a type of iterable, like lists or tuples.
# Unlike lists, they don't allow indexing with arbitrary indices, 
# but they can still be iterated through with for loops.
# They can be created using functions and the yield statement.
def countdown():
  i=5
  while i > 0:
    yield i
    i -= 1
    
for i in countdown():
  print(i)

# The yield statement is used to define a generator, 
# replacing the return of a function to provide a result to its caller without destroying local variables. 

# Finite generators can be converted into lists by passing them as arguments to the list function.
def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print(list(numbers(11))) # prints [0, 2, 4, 6, 8, 10]

# Using generators results in improved performance, which is the result of the lazy (on demand) generation of values,
# which translates to lower memory usage. 
# Furthermore, we do not need to wait until all the elements have been generated before we start to use them.

# ----------- Task -------------
# You need to create a generator function primeGenerator(), that will take two numbers as arguments, 
# and use the isPrime() function to output the prime numbers in the given range (between the two arguments).
# The given code takes the two arguments as input
# and passes them to the generator function, outputting the result as a list.
def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True

def primeGenerator(a, b):
    while a < b:
        if isPrime(a) == True:
            yield a
        a +=1
f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))

#! ----------- Decorators -----------
# Decorators provide a way to modify functions using other functions.
# This is ideal when you need to extend the functionality of functions that you don't want to modify.
def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

def print_text():
  print("Hello world!")

decorated = decor(print_text)
decorated()
#! We defined a function named decor that has a single parameter func. Inside decor, 
# we defined a nested function named wrap. The wrap function will print a string, then call func(), 
# and print another string. The decor function returns the wrap function as its result.
#! We could say that the variable decorated is a decorated version of print_text -- it's print_text plus something.
#! In fact, if we wrote a useful decorator we might want to replace print_text with the decorated version 
# altogether so we always got our "plus something" version of print_text.
# This is done by re-assigning the variable that contains our function:
print_text = decor(print_text)
print_text()

# You can decorate a function by pre-pending the function definition with a decorator name and the "@" symbol.
# This allows you to wrap any function with custom behavior.
@decor
def print_text():
  print("Hello world!")
print_text() # prints 'Hello world' with the decoration we set before.
# In Python, you can apply multiple decorators to a single function, 
# which gives you the flexibility to modify its behavior in various ways.

#! ----------- Recursion -----------
# Recursion is a very important concept in functional programming.
# The fundamental part of recursion is self-reference -- functions calling themselves.
# It is used to solve problems that can be broken up into easier sub-problems of the same type.

""" A classic example of a function that is implemented recursively is the factorial function, 
which finds the product of all positive integers below a specified number.
For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120). 
To implement this recursively, notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and so on. 
Generally, n! = n * (n-1)!. Furthermore, 1! = 1.
This is known as the base case, as it can be calculated without performing any more factorials.
Below is a recursive implementation of the factorial function."""
def factorial(x):
  if x == 1:
    return 1
  else: 
    return x * factorial(x-1)
    
print(factorial(4)) # prints 24
#! The base case acts as the exit condition of the recursion.
#! Not adding a base case results in infinite function calls, crashing the program.

# Recursion can also be indirect. 
# One function can call a second, which calls the first, which calls the second, and so on. 
# This can occur with any number of functions.
def is_even(x):
  if x == 0:
    return True
  else:
    return is_odd(x-1)

def is_odd(x):
  return not is_even(x)

print(is_odd(9)) # prints True
print(is_even(25)) # prints False
def fib(x):
 if x == 0 or x == 1:
  return 1
 else:
  return fib(x-1) + fib(x-2)
print(fib(4))

# ----------- Task -------------

# The given code defines a recursive function convert(),
# which needs to convert its argument from decimal to binary.
# However, the code has an error.
# Fix the code by adding the base case for the recursion, 
# then take a number from user input and call the convert() function, to output the result.
# Sample Input : 8
# Sample Output : 1000
# The binary representation of 8 is 1000.
def convert(num):
   if num == 0:
      return 0
   else:  
     return (num % 2 + 10 * convert(num // 2)) 

print(convert(int(input())))

#! ----------- *args and **kwargs -----------
# Python allows you to have functions with varying numbers of arguments.
# Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function. 
# The arguments are then accessible as the tuple args in the body of the function.
def function(named_arg, *args):
   print(named_arg)
   print(args)

function(1, 2, 3, 4, 5) # prints 1 and then (2, 3, 4, 5)
# The parameter *args must come after the named parameters to a function.
# The name args is just a convention; you can choose to use another.
#! Another example:
def sum_numbers(*args):
    result = 0
    for num in args:
        result += num
    return result
sum_numbers(1, 2, 3)  # Returns 6

# **kwargs (standing for keyword arguments) allows you to handle named arguments
# that you have not defined in advance.
# The keyword arguments return a dictionary in which the keys are the argument names,
# and the values are the argument values.
def my_func(x, y=7, *args, **kwargs):
   print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8) # prints {'a': 7, 'b': 8}
# a and b are the names of the arguments that we passed to the function call.
# The arguments returned by **kwargs are not included in *args.
#! Another example:
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(name="Alice", age=30, city="New York")
# Outputs:
# name: Alice
# age: 30
# city: New York

#! ----------- Object Oriented Programming -----------
#!         ----------- Classes -----------
# The focal point of Object Oriented Programming (OOP) are objects, which are created using classes.

# The class describes what the object will be, but is separate from the object itself. 
# In other words, a class can be described as an object's blueprint, description, or definition.
# You can use the same class as a blueprint for creating multiple different objects.

# Classes are created using the keyword class and an indented block, 
# which contains class methods (which are functions).
# Below is an example of a simple class and its objects.
class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

# This code defines a class named Cat, which has two attributes: color and legs.
# Then the class is used to create 3 separate objects of that class.

#! ----------- __init__ -----------
"""
The __init__ method is the most important method in a class.
This is called when an instance (object) of the class is created, using the class name as a function.

All methods must have self as their first parameter, although it isn't explicitly passed, 
Python adds the self argument to the list for you; you do not need to include it when you call the methods.
 Within a method definition, self refers to the instance calling the method.

Instances of a class have attributes, which are pieces of data associated with them.
In this example, Cat instances have attributes color and legs. These can be accessed by putting a dot, 
and the attribute name after an instance.
In an __init__ method, self.attribute can therefore be used to set the initial value of an instance's attributes.
"""
class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
print(felix.color) # prints ginger
print(felix.legs) # prints 4

# In the example above, the __init__ method takes two arguments and assigns them to the object's attributes.
#  The __init__ method is called the class constructor.

#! ----------- Methods -----------
# Classes can have other methods defined to add functionality to them.
# Remember, that all methods must have self as their first parameter.
# These methods are accessed using the same dot syntax as attributes.
class Dog:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Woof!")

archik = Dog("Archik", "Black")
print(archik.name)
print(archik.color)
archik.bark()
# NOTE Class attributes are shared by all instances of the class.

# ----------- Task -----------
"""
You are making a video game! The given code declares a Player class, with its attributes and an intro() method.
Complete the code to take the name and level from user input, 
create a Player object with the corresponding values and call the intro() method of that object.
"""
class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")

#your code goes here
name = input()
level = input()
new_player = Player(name, level)
new_player.intro()

#! ----------- Inheritance -----------
"""
Inheritance provides a way to share functionality between classes.
Imagine several classes, Cat, Dog, Rabbit and so on. 
Although they may differ in some ways (only Dog might have the method bark), 
they are likely to be similar in others (all having the attributes color and name).
This similarity can be expressed by making them all inherit from a superclass Animal, which contains the shared functionality.
To inherit a class from another class, put the superclass name in parentheses after the class name.
"""
class Animal: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

class Cat(Animal):
  def purr(self):
    print("Purr...")
        
class Dog(Animal):
  def bark(self):
    print("Woof!")

archik = Dog("Archik", "Black")
print(archik.color)
archik.bark() # prints "Woof!"
archik.purr() # prints error
thomas = Cat("Thomas", "Grey")
print(thomas.color)
thomas.bark() # prints error
thomas.purr() # prints "Purr..."

"""
A class that inherits from another class is called a subclass.
A class that is inherited from is called a superclass.
If a class inherits from another with the same attributes or methods, it overrides them.
"""
class Wolf: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Awoooo")

class Dog(Wolf):
  def bark(self):
    print("Woof!")
        
husky = Dog("Mika", "grey")
husky.bark() # prints "Woof!"
wolf = Wolf("Zeev", "white")
wolf.bark() # prints "Awoooo"

#NOTE In the example above, Wolf is the superclass, Dog is the subclass.

# The function super is a useful inheritance-related function that refers to the parent class. 
# It can be used to find the method with a certain name in an object's superclass.
class A:
  def spam(self):
    print(1)

class B(A):
  def spam(self):
    print(2)
    super().spam()
            
B().spam() # prints 1, as the superclass A
#NOTE super().spam() calls the spam method of the superclass.

#! ----------- Magic Methods -----------
# Magic methods are special methods which have double underscores at the beginning and end of their names.
# They are also known as dunders. Like the __init__ that we use in classes.

# One common use of them is operator overloading.
# This means defining operators for custom classes that allow operators such as + and * to be used on them.
# An example magic method is __add__ for +.
class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)
# The __add__ method allows for the definition of a custom behavior for the + operator in our class.
# (you can also use - or * or / and it will work)
# As you can see, it adds the corresponding attributes of the objects and returns a new object,
#  containing the result.
# Once it's defined, we can add two objects of the class together.

"""
More magic methods for common operators:
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |

The expression x + y is translated into x.__add__(y).
However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called.
There are equivalent r methods for all magic methods just mentioned.
"""
class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __truediv__(self, other):
    line = "=" * len(other.cont)
    return "\n".join([self.cont, line, other.cont]) # \n creates a new line

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello) 
# prints: 
"""
spam
============
Hello world!
"""

# In the example above, we defined the division operation for our class SpecialString.

"""
Python also provides magic methods for comparisons.
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

If __ne__ is not implemented, it returns the opposite of __eq__.
There are no other relationships between the other operators.
"""
class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __gt__(self, other):
    for index in range(len(other.cont)+1):
      result = other.cont[:index] + ">" + self.cont
      result += ">" + other.cont[index:]
      print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs

# As you can see, you can define any custom behavior for the overloaded operators.

"""
There are several magic methods for making classes act like containers.
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in

There are many other magic methods that we won't cover here, such as __call__ for calling objects as functions,
 and __int__, __str__, and the like, for converting objects to built-in types.
"""
import random

class VagueList:
  def __init__(self, cont):
    self.cont = cont

  def __getitem__(self, index):
    return self.cont[index + random.randint(-1, 1)]

  def __len__(self):
    return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
# We have overridden the len() function for the class VagueList to return a random number.
# The indexing function also returns a random item in a range from the list, based on the expression.

# ----------- Task -----------
"""
We are improving our drawing application.
Our application needs to support adding and comparing two Shape objects.
Add the corresponding methods to enable addition + and comparison using the greater than > operator
 for the Shape class.

The addition should return a new object with the sum of the widths and heights of the operands, 
while the comparison should return the result of comparing the areas of the objects.

The given code creates two Shape objects from user input, outputs the area() of their addition and compares them.
"""
class Shape: 
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width*self.height

    #your code goes here
    def __add__(self, other):
        return Shape(self.width + other.width, self.height + other.height)
    def __gt__(self,other):
        return self.area() > other.area()
w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)
result = s1 + s2

print(result.area())
print(s1 > s2)

#! ----------- Data Hiding -----------
"""
A key part of object-oriented programming is encapsulation, 
which involves packaging of related variables and functions into a single easy-to-use object -- an instance of a class.
A related concept is data hiding, which states that implementation details of a class should be hidden, 
and a clean standard interface be presented for those who want to use the class.
In other programming languages, this is usually done with private methods and attributes, 
which block external access to certain methods and attributes in a class.

The Python philosophy is slightly different. 
It is often stated as "we are all consenting adults here", 
meaning that you shouldn't put arbitrary restrictions on accessing parts of a class. 
Hence there are no ways of enforcing that a method or attribute be strictly private.

However, there are ways to discourage people from accessing parts of a class, such as by denoting that it is an implementation detail,
and should be used at their own risk.
"""
# Weakly private methods and attributes have a single underscore at the beginning.
# This signals that they are private, and shouldn't be used by external code. 
# However, it is mostly only a convention, and does not stop external code from accessing them.

class Queue:
  def __init__(self, contents):
    self._hiddenlist = list(contents)

  def push(self, value):
    self._hiddenlist.insert(0, value)
   
  def pop(self):
    return self._hiddenlist.pop(-1)

  def __repr__(self):
    return "Queue({})".format(self._hiddenlist) 
  # The format() method formats the specified value(s) and insert them inside the string's placeholder.

queue = Queue([1, 2, 3])
print(queue) # prints Queue([1, 2, 3])
queue.push(0)
print(queue) # prints Queue([0, 1, 2, 3])
queue.pop() # returns 3
print(queue) # Queue([0, 1, 2])
print(queue._hiddenlist) # prints [0, 1, 2]

# In the code above, the attribute _hiddenlist is marked as private, 
# but it can still be accessed in the outside code.
# The __repr__ magic method is used for string representation of the instance.

"""
Strongly private methods and attributes have a double underscore at the beginning of their names. 
This causes their names to be mangled, which means that they can't be accessed from outside the class.
The purpose of this isn't to ensure that they are kept private,
 but to avoid bugs if there are subclasses that have methods or attributes with the same names.
Name mangled methods can still be accessed externally, but by a different name. 
The method __privatemethod of class Spam could be accessed externally with _Spam__privatemethod.
"""
class Spam:
  __egg = 7
  def print_egg(self):
    print(self.__egg)

s = Spam()
s.print_egg() # prints 7
print(s._Spam__egg) # prints 7
print(s.__egg) # prints AttributeError: 'Spam' object has no attribute '__egg'

# Basically, Python protects those members by internally changing the name to include the class name.

#! ----------- Class Methods -----------
"""
Methods of objects we've looked at so far are called by an instance of a class, 
which is then passed to the self parameter of the method.
Class methods are different -- they are called by a class, which is passed to the cls parameter of the method.
A common use of these are factory methods, which instantiate an instance of a class,
using different parameters than those usually passed to the class constructor.
Class methods are marked with a classmethod decorator.
"""
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def calculate_area(self):
    return self.width * self.height

  @classmethod
  def new_square(cls, side_length):
    return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area()) # prints 25

"""
new_square is a class method and is called on the class, rather than on an instance of the class. 
It returns a new object of the class cls.

Technically, the parameters self and cls are just conventions; they could be changed to anything else. 
However, they are universally followed, so it is wise to stick to using them.
"""

#! ----------- Static Methods -----------
"""
Static methods are similar to class methods, except they don't receive any additional arguments;
they are identical to normal functions that belong to a class.
They are marked with the staticmethod decorator.
"""
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings

  @staticmethod
  def validate_topping(topping):
    if topping == "pineapple":
      raise ValueError("No pineapples!")
    else:
      return True
    
  def __str__(self):
    return f"A delicious pizza with toppings: {', '.join(self.toppings)}"

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
  pizza = Pizza(ingredients)
  print(pizza)

# Static methods behave like plain functions, 
# except for the fact that you can call them from an instance of the class.

# ----------- Task -----------
""" 
The given code takes 2 numbers as input and calls the static area() method of the Shape class, 
to output the area of the shape, which is equal to the height multiplied by the width.
To make the code work, you need to define the Shape class, and the static area() method, 
which should return the multiplication of its two arguments.
"""
#your code goes here
class Shape:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    @staticmethod
    def area(w,h):
        return w * h

w = int(input())
h = int(input())

print(Shape.area(w, h))

#! ----------- Properties -----------
"""
Properties provide a way of customizing access to instance attributes.
They are created by putting the property decorator above a method, 
which means when the instance attribute with the same name as the method is accessed, 
the method will be called instead.
One common use of a property is to make an attribute read-only.
"""
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    
  @property
  def pineapple_allowed(self):
    return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True # returns error

"""
This code defines a Pizza class with a read-only property named pineapple_allowed, which is always False.
It demonstrates that you can't change the value of this property because it's read-only.
"""
"""
Properties can also be set by defining setter/getter functions.
The setter function sets the corresponding property's value.
The getter gets the value.
To define a setter, you need to use a decorator of the same name as the property,
followed by a dot and the setter keyword.
The same applies to defining getter functions.
"""
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    self._pineapple_allowed = False

  @property
  def pineapple_allowed(self):
    return self._pineapple_allowed

  @pineapple_allowed.setter
  def pineapple_allowed(self, value):
    if value:
      password = input("Enter the password: ")
      if password == "Sw0rdf1sh!":
        self._pineapple_allowed = value
      else:
        raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)

#! ----------- Exceptions -----------
"""
Exceptions occur when something goes wrong, due to incorrect code or input.
When an exception occurs, the program immediately stops.
"""
# The following code produces the ZeroDivisionError exception by trying to divide 7 by 0:
num1 = 7
num2 = 0
print(num1/num2) # prints ZeroDivisionError: division by zero

"""
Different exceptions are raised for different reasons.
Common exceptions:
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly;
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.
"""
# Python has several other built-in exceptions, such as ZeroDivisionError and OSError. 
# Third-party libraries also often define their own exceptions.

#! ----------- Exception Handling -----------
"""
When an exception occurs, the program stops executing.
To handle exceptions, and to call code when an exception occurs, you can use a try/except statement.
The try block contains code that might throw an exception. 
If that exception occurs, the code in the try block stops being executed, and the code in the except block is run. 
If no error occurs, the code in the except block doesn't run.
"""
try:
   num1 = 7
   num2 = 0
   print (num1 / num2)
   print("Done calculation")
except ZeroDivisionError:
   print("An error occurred")
   print("due to zero division")

# As the code produces a ZeroDivisionError exception, the code in the except block is run.
# In the code above, the except statement defines the type of exception to handle (in our case, the ZeroDivisionError).

# A try statement can have multiple different except blocks to handle different exceptions.
# Multiple exceptions can also be put into a single except block using parentheses, to have the except block handle all of them.
try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred")

# NOTE You can handle as many exceptions in the except statement as you need.
"""
An except statement without any exception specified will catch all errors. These should be used sparingly, 
as they can catch unexpected errors and hide programming mistakes.
"""
try:
   word = "spam"
   print(word / 0)
except:
   print("An error occurred")

# Exception handling is particularly useful when dealing with user input.
"""
If you want to print the details of the error that occurred without specifying a specific exception type 
(i.e., using an empty except block), you can use the sys.exc_info() function to access the exception information. 
Here's how you can do it:
"""
import sys

try:
    word = "spam"
    print(word / 0)
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(f"An error occurred: {exc_type.__name__} - {exc_value}")
#! prints: An error occurred: TypeError - unsupported operand type(s) for /: 'str' and 'int'   

# ----------- Task -----------
"""
An ATM machine takes the amount to be withdrawn as input and calls the corresponding withdrawal method.
In case the input is not a number, the machine should output "Please enter a number".
Use exception handling to take a number as input, call the withdraw() method with the input as its argument, 
and output "Please enter a number", in case the input is not a number.
"""
# A ValueError is raised when you try to convert a non-integer to an integer using int().
def withdraw(amount):
   print(str(amount) + " withdrawn!")

#your code goes here
try: 
   amount = int(input())
   withdraw(amount)
except ValueError:
   print("Please enter a number")

#! ----------- Finally/Else -----------
#! Finally
# After a try/except statement, a finally block can follow. 
# It will execute after the try/except block, no matter if an exception occurred or not.
try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")
# Prints:
# Hello
# Divided by zero
# This code will run no matter what
"""
The finally block is useful, for example, when working with files and resources: 
it can be used to make sure files or resources are closed or released regardless of whether an exception occurs.
"""
#! Else
# The else statement can also be used with try/except statements.
# In this case, the code within it is only executed if no error occurs in the try statement.
try:
   print(1)
except ZeroDivisionError:
   print(2)
else:
   print(3)

#! prints 1 and 3 (try and else)

try:
   print(1/0)
except ZeroDivisionError:
   print(4)
else:
   print(5)
#! prints only 4 (only except)

#! ----------- Raising Exceptions -----------
"""
You can throw (or raise) exceptions when some condition occurs.
For example, when you take user input that needs to be in a specific format, you can throw an exception when it does not meet the requirements.
This is done using the raise statement.
"""
num = 102
if num > 100:
  raise ValueError

# NOTE You need to specify the type of the exception raised. In the code above, we raise a ValueError.

# Exceptions can be raised with arguments that give detail about them.
  name = "123"
  raise NameError("Invalid name!") # returns "NameError: Invalid name!"

# This makes it easier for other developers to understand why you raised the exception.

# ----------- Task -----------
"""
You are making a program to post tweets. Each tweet must not exceed 42 characters.
Complete the program to raise an exception, in case the length of the tweet is more than 42 characters.
"""
# You can use the len() function to calculate the length of the string.
tweet = input()

try:
    #your code goes here
        if len(tweet) > 42:
        raise ValueError 
    
except:
    print("Error")
else:
    print("Posted")

#! ----------- Working with files -----------
#! ----------- Opening files -----------
"""
You can use Python to read and write the contents of files.
This is particularly useful when you need to work with a lot of data that is saved in a file.
For example, in data science and analytics, the data is commonly in CSV (comma-separated values) files.

Let's start by working with text files, as they are the easiest to manipulate.
Before a file can be edited, it must be opened, using the open function.
"""
myfile = open(filename.txt)
# The argument of the open function is the path to the file. 
# If the file is in the current working directory of the program, you can specify only its name.

"""
You can specify the mode used to open a file by applying a second argument to the open function.
Sending "r" means open in read mode, which is the default.
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.

Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).
"""
# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")

# You can combine modes, for example, wb from the code above opens the file in binary write mode.

# Once a file has been opened and used, you should close it.
# This is done with the close method of the file object.
file = open("filename.txt", "w")
# do stuff to the file
file.close()

#! ----------- Reading files -----------
# The contents of a file that has been opened in text mode can be read using the read method.
file = open("books.txt")
cont = file.read()
print(cont) # prints the content of books.txt
file.close()

# To read only a certain amount of a file, you can provide the number of bytes to read as an argument to the read function.
# Each ASCII character is 1 byte:
file = open("books.txt")
print(file.read(5)) # prints the first 5 characters of the file
print(file.read(7)) # prints the next 7 characters of the file
print(file.read()) # prints the rest of the file
file.close()

# NOTE Calling the read() method without an argument will return the rest of the file content.

# To retrieve each line in a file, 
# you can use the readlines() method to return a list in which each element is a line in the file.
file = open("books.txt")

for line in file.readlines():
    print(line)
    
file.close()

# ----------- Task -----------
# You need to make a program to read the given number of characters of a file.
# Take a number N as input and output the first N characters of the books.txt file.
file = open("/usercode/files/books.txt")
#your code goes here
n = int(input())
print(file.read(n))

#! ----------- Writing files -----------
# To write to files you use the write method.
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()
# This will create a new file called "newfile.txt" and write the content to it.
# NOTE In case the file already exists, its entire content will be replaced when you open it in write mode using "w".

# If you want to add content to an existing file, you can open it using the "a" mode, which stand for "append":
file = open("/books.txt", "a")
file.write("\nThe Da Vinci Code") #! \n stands for a new line
file.close()
# This will add a new line with a new book title to the file.

# The write method returns the number of bytes written to a file, if successful.
msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written) # prints 12
file.close()

# NOTE To write something other than a string, it needs to be converted to a string first.

#! ----------- Working with files -----------
# It is good practice to avoid wasting resources by making sure that files are always closed after they have been used. 
# One way of doing this is to use try and finally.
try:
  f = open("/usercode/files/books.txt")
  cont = f.read()
  print(cont)
finally:
 f.close()
# NOTE This ensures that the file is always closed, even if an error occurs.

"""
An alternative way of doing this is by using with statements.This creates a temporary variable (often called f), 
which is only accessible in the indented block of the with statement.
"""
with open("/usercode/files/books.txt") as f:
  print(f.read())

# The file is automatically closed at the end of the with statement, even if exceptions occur within it.

# ----------- Task -----------
"""
You are given a books.txt file, which includes book titles, each on a separate line.
Create a program to output how many words each title contains, in the following format:
Line 1: 3 words
Line 2: 5 words
...

Make sure to match the above mentioned format in the output.

To count the number of words in a given string, you can use the split() function, or, alternatively, 
count the number of spaces (for example, if a string contains 2 spaces, then it contains 3 words).
"""
with open("/usercode/files/books.txt") as f:
   #your code goes here
   line_num = 1
   for line in f.readlines():
      words = line.count(" ") + 1
      print(f"Line {line_num}: {words} words")
      line_num += 1