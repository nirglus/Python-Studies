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

# ------- Task -------
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

#-----Data Types ------
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

# --------- Task ----------
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

# ------- Comparisons -------
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

#for loop is used to execute the same instruction over and over again, a specific number of times.
#range() creates 5 numbers in a sequence, starting from 0.
for i in range(5):
    print("Hello there")
# The code that gets repeated in the for loop must be indented. Indentation is the spaces at the beginning of lines.
# for i in range(5):
# print("Hello")  # This wont work

# While loops repeat code whilst a condition holds true.
cars = 5
while cars > 0:
    print("Sell car")
    cars = cars - 1
# Like for loops, while loops also should contain colon : and be indented.
# Best practice is to use for loops when we know the number of iterations,
# and while loops for when there is a condition that needs to be met.

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