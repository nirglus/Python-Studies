# ------- String & List exercises -------
# 1. Create a program that asks the user for their name and then prints a greeting.
name = input("Enter your name: ")
print("Hello", name, "!")

# 2. Create a program that asks the user for their first name and a nickname, 
# and then combines them to create a playful nickname. For instance, "Johnny the Rocket."
first_name = input("Enter your first name: ")
nickname = input("Enter a nickname: ")
print(first_name, "the", nickname)

# 3. Create a program that takes a user's full name and abbreviates it by displaying 
# only the first letter of their first name followed by a period and their last name. 
# For instance, "John Doe" becomes "J. Doe."
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(first_name[0] + ".", last_name)

# 4. Create a program that takes a user-entered word and displays the first and last characters of the word.
user_word = input("Enter a word: ")
print("First letter:", user_word[0], "Last letter:", user_word[-1])

# 5. Create a program that takes a user's first name and last name, and generates a username by 
# taking the first three letters of the first name and the first three letters of the last name.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
username = first_name[:3] + last_name[:3]
print(username)

# 6. Write a program that extracts and prints the domain name from a URL. 
# You can assume that the URL will always start with "http://" or "https://".
url = input("Enter a url (starts with https:// or http://)")
start_index = url.find("://") + 3
domain = url[start_index :]
print(domain)

# 7. Initialize an empty list and add a series of names to the list. 
# After each addition, display the current list and its length.
new_list = []
new_list.insert(0, "Jack")
print(new_list, len(new_list))
new_list.append("Alfonso")
print(new_list, len(new_list))
new_list.append("Michael")
print(new_list, len(new_list))

# 8. Initialize a list of numbers and insert a new number at a specified position. 
# Then, remove a number at a specific index and display the updated list.
num_list = [2, 8, 4, 88, 9, 54]
num_list.insert(-3, 69)
print(num_list)
num_list.pop(1)
print(num_list)

# 9. Initialize a list of names and capitalize the first letter of each name. 
# Display the modified list.
name_list = ["dan", "jack", "carl", "sean"]
for i in range(len(name_list)):
    name_list[i] = name_list[i].capitalize()
print(name_list)

# 10. Initialize a string and convert it to all uppercase and all lowercase.
my_string = "Have a good weekend"
print(my_string.upper())
print(my_string.lower())

# 11. Initialize an empty shopping list, add items to it, and remove items.
shop_list = []
shop_list.append("Milk")
shop_list.append("Coffee")
shop_list.append("Meat")
shop_list.append("Cups")
for i in range(len(shop_list)):
    shop_list.pop(0)
    print(shop_list)

# 12. Initialize a list of numbers and calculate the sum and average of the numbers. Display both results.
numbers_list = [5, 7, 2, 97, 23]
sum = 0
avg = 0
list_range = len(numbers_list)
for i in range(list_range):
    sum = sum + numbers_list[i]
    avg = sum / len(numbers_list)
print("Sum of number:",sum,"Avarage:", avg)

# 13. Initialize two strings and concatenate them to create a third string.
# Display the concatenated string.
string1 = "Hello"
string2 = "Mister"
string3 = string1 + " " + string2
print(string3)

# 14. Initialize a list of names and sort them alphabetically. Display the sorted list.
names = ["Jack", "Melvin", "Neta", "Patrick", "Anna"]
names.sort()
print(names)

# 15. Create a program that calculates the sum of numbers from 1 to a user-specified number using a while loop.
user_num = int(input("Enter a number:"))
i = 1
sum = 0
while(i <= user_num):
    sum = sum + i
    i = i + 1
print(sum)

# 16. Implement a program that asks the user to guess a password (e.g., "password123") and 
# keeps asking until they enter the correct password.
password = "ThisIsAPass"
user_pass = input("Enter a password: ")
while user_pass != password: 
    user_pass = input("Wrong password, try again: ")
    if user_pass == password:
       print("Access granted")

# 17. Write a program that uses a while loop to print a pattern of asterisks like this:
# *
# **
# ***
# ****
# *****
row = 1
while row <= 5:
    print("*" * row)
    row += 1

# 18. Create a program that asks the user to enter a sentence and a word to search for.
# Use a while loop and the find() method to count and print the number of times the word appears in the sentence.
sentence = input("Enter a sentence: ")
word = input("Enter a word you want to search for: ")
count = 0
start_index = 0

while True:
    index = sentence.find(word, start_index)
    if index == -1:
        break
    count += 1
    start_index = index + len(word)

print("The word "+ word +" appears " + count + " times in the sentence.")

# 19. Create a program that asks the user for a starting number and counts down from that number to 1 
# using a while loop.
start_num = int(input("Enter a starting number: "))

while start_num >= 1:
    print(start_num)
    start_num -= 1

# 20. Write a program that calculates the sum of all even numbers from 1 to 50 using a while loop.
num = 2
sum_even = 0
while num <= 50:
    sum_even += num
    num += 2 

print("Sum of even numbers from 1 to 50:", sum_even)

# 21. Implement a program that checks if a year entered by the user is a 
# leap year or not.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It's a leap year.")
else:
    print("It's not a leap year.")

# 22. Write a program that asks the user for an integer and determines 
# whether it's even or odd.
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#! ------------ Tuple exercise -------------    

# 23. Create a tuple representing a 2D point (x, y) 
# and use tuple unpacking to extract and print the values of x and y.
point = (2, 6)
x, y = point
print("x:",x)
print("y:",y)

# 24. Combine two tuples into a single tuple, and then print the resulting tuple.
first_tuple = (3, 5)
second_tuple = (6, 8)
mix = first_tuple + second_tuple
print(mix)

# 25. Create a tuple of numbers from 1 to 10, and use slicing to print the numbers
#  from the 3rd to the 7th position.
numbers = tuple(range(1, 11))
print(numbers[2:7])
# 26. Create a tuple of the first and last names of a person. Then,
#  use tuple packing and unpacking to assign these values to separate variables.
person = ("Mister", "Fister")
f_name = person[0]
l_name = person[1]
print(f_name)
print(l_name)

# 27. Create a tuple of your favorite programming languages and use the len() function 
# to find and print the length of the tuple.
langs = ("JavaScript", "Python", "Java", "C#", "C++")
print(len(langs))

#! ------------ Tuple Unpacking exercise -------------    

# 28. Write a program that swaps the values of two variables using tuple unpacking.
x, y = 1, 2
x, y = y, x
print(x, y)

# 29. Create a function that takes two numbers as input and returns their sum and product using tuple unpacking.
def sum_product(x, y):
    return x + y, x * y
result_sum, result_product = sum_product(5, 8)
print("The sum is:", result_sum)
print("The product is:", result_product) 

# 30. Initialize a tuple with three values (e.g., a point in 3D space). Then, use tuple unpacking to assign 
# these values to three separate variables representing the x, y, and z coordinates.
point = (1, 8, 20)
x, y, z = point
print("X coordiante:",x)
print("Y coordinate:", y)
print("Z coordinate:", z)

# 31. Write a function that takes a list of numbers and returns the minimum and maximum values using tuple unpacking.
def min_max(list):
    return min(list), max(list)
num_list = [2, 9, 34, 89, 5, 1, 45]
min_result, max_result = min_max(num_list)
print("The min number is:", min_result)
print("The max number is:", max_result)

#! ------------ Sets exercise -------------  
# 32. Create two sets of your favorite colors and perform basic set operations, such as union, 
# intersection, and difference.
first_set = {"black", "brown", "red"}
second_set = {"green", "blue", "red", "grey"}
print(first_set | second_set) #! union - prints {'red', 'green', 'blue', 'brown', 'black', 'grey'}
print(first_set & second_set) #! intersection - prints 'red'
print(first_set - second_set) #! difference - prints {'brwon', 'black}
print(second_set - first_set) #! difference - prints {'blue', 'green', 'grey'}
print(first_set ^ second_set) #! symetric difference - prints {'blue', 'brown', 'black', 'green', 'grey'}

# 33. Create a set of programming languages. 
# Then, check if a specific language is in the set, and find the number of languages in the set.
langs = {"Python", "JS", "Java", "C", "C++", "Pascal"}
lang_to_check = "JS"
if lang_to_check in langs:
    print(f"{lang_to_check} is in the set")
set_length = len(langs)
print(f"Number of programming languages in the set is{set_length}")    

# 34. Create an empty set for groceries. 
# Add items to the set, and then remove items using the add() and remove() methods.
groceries = {"milk", "tea", "bread", "butter", "cheese"}
groceries.add("meat")
print(groceries)
groceries.remove("milk")
print(groceries)

#! ------------ Lambda, map and filter exercise ------------- 
# 1. Use map() and a lambda function to square each number in a list of integers
#  and create a new list with the squared values.
integers = [2, 4, 6, 8, 10, 12]
new_list = list(map(lambda x: x**2, integers))
print(new_list)

# 2. Given a list of words, use map() and a lambda function to capitalize the first letter of each word.
words = ["apple", "banana", "cherry", "date"]
new_words = list(map(lambda x: x.capitalize(), words))
print(new_words)

# 3. Create a list of strings and use map() and a lambda function to reverse each string in the list.
strings = ["hello", "world", "python", "exercise"]
reversed_strings = list(map(lambda x: x[::-1], strings))
print("Reversed Strings:", reversed_strings)

# 4. Given a list of integers, use filter() and a lambda function 
# to create a new list containing only the even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x%2==0, numbers))
print(evens)

# 5. Create a list of names and use filter() and a lambda function to create a new list 
# with names that contain the letter 'a'.
names = ["John", "Amanda", "Anna", "Drake", "Joe", "Albert", "Angela"]
a_names = list(filter(lambda x: "a" in x.lower(), names))
print("Names with 'a':" ,a_names)

# 6. Given a list of words, use filter() and a lambda function to create a new list 
# with words that have a length of 6 or more characters.
words = ["apple", "banana", "cherry", "date", "elephant", "grape"]
long_words = list(filter(lambda x: len(x) >= 6, words))
print("Words with 6 chars or more:", long_words)

#! ------------ Generator exercise ------------- 
# 1. Write a generator function that yields numbers from 1 to n.
#  Test the generator by iterating over it and printing the numbers.
def num_print(n):
    i = 1
    while i <= n:
        yield i
        i+=1
for i in num_print(10):
    print(i)

# 2. Create a generator function to generate the Fibonacci sequence up to a given limit. 
# The generator should yield Fibonacci numbers one by one.
def fibonacci(n):
    a, b = 0 , 1
    while a <= n:
        yield a
        a, b = b, a + b

for i in fibonacci(100):
    print(i)

# 3. Write a generator function that yields numbers within a custom range, 
# similar to the built-in range() function.
def custom_range(n):
    i = 0
    while i < n:
        yield i
        i+=1
for i in custom_range(7):
    print(i)

# 4. Write a generator function that counts down from a specified number to 1, yielding each countdown value.
def countdown(n):
    while n >= 1:
        yield n
        n -= 1
for i in countdown(20):
    print(i)

# 5. Define a generator function that splits a string into words and yields each word one by one. 
# Use whitespace as the default delimiter.
def str_split(words):
    words_list = words.split()
    n = 0
    while n < len(words_list):
        yield words_list[n]
        n+=1

for i in str_split("Let's split this text"):
    print(i)
        

#! ------------ Decorator exercise ------------- 
# 1. Create a decorator that adds a greeting to the result of a function.
def decor(func):
    def wrap():
        name = func()
        return "Hello, " + name + "!"
    return wrap
@decor
def greet():
    return "Nir"
result = greet()
print(result)

# 2. Write a decorator that converts the result of a function to uppercase.
def upper(func):
    def wrap():
        text = func()
        return text.upper()
    return wrap
@upper
def convtxt():
    return "Decorators are fun"
print(convtxt())

# 3. Implement a decorator that logs the function name and result.
def decor(func):
    def wrap():
        print(f"Function name: {func.__name__}")
        result = func()
        print(f"The result is: {result}")
        return result
    return wrap
@decor
def getresult():
    return "I wonder how this function's called"
print(getresult())

#! ------------ Recursion exercise ------------- 
# 1. Write a recursive function to calculate the factorial of a non-negative integer n.
def factor(n):
    if n == 0:
        return 1
    else:
        return n * factor(n-1)
    
print(factor(4))
# 2. Create a recursive function to find the nth term in the Fibonacci sequence.
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)
print(fib(9))    

# 3. Write a recursive function that calculates the sum of the digits of a positive integer.
def sumup(n):
    if n < 10:
        return n
    else:
        return n % 10 + sumup(n // 10)
    
print(sumup(123))
    
# 4. Create a recursive function that calculates the result of raising a number x to a non-negative integer power n.
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

result = power(2, 3)
print("2^3:", result)

#! ----------- *args and **kwargs exercise -----------
# 1. Write a function that takes any number of arguments and returns their sum.
def num_sum(*args):
    result = 0
    for i in args:
        result += i
    return result
num_sum(3,7,10)

# 2. Create a function that takes any number of string arguments and returns their concatenation.
def num_conc(*args):
    result = " ".join(args)
    return result
num_conc("This", "will", "be", "concated")

# 3. Implement a function that accepts a variable number of arguments and returns the maximum value among them.
def find_max(*args):
    return max(args)
print(find_max(2,7,8,5,4,9,1))

# 4. Write a function that creates a dictionary using keyword arguments.
def new_dictionary(**kargs):
    return kargs
result = new_dictionary(name="Max", age=26, city="Amsterdam", country="Netherlands")
print(result) 

#! ----------- Classes exercise -----------
# 1. Create a class called Person with attributes for name and age, and a method to print the person's information.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_person(self):
        print(f"Name: {self.name}, Age: {self.age}")
anna = Person("Anna", 23)
anna.show_person()

# 2. Create a subclass Student that inherits from the Person class and adds an attribute for student_id. 
# Override the display_info method to include the student's ID.
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def show_person(self):
          print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")

alex = Student("Alex", 18, 34786)
alex.show_person()

# 3. Define a base class Shape with methods for calculating area and perimeter. Create two subclasses, Rectangle and Circle, 
# each with its own implementations of area and perimeter calculation methods. 
# NOTE use the pass keyword
# (The pass statement is used as a placeholder for future code.)
import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius ** 2 * math.pi
    def perimeter(self):
        return 2 * math.pi * self.radius
    
rectangle = Rectangle(10, 5)
circle = Circle(9)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

# 4. Define a base class Vehicle with attributes for make, model, and year, and a method to display vehicle information. 
# Create subclasses Car and Motorcycle that inherit from the base class and provide their own implementations.
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Brand: {self.make}, Model: {self.model}, Year: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
    def display_info(self):
        print(f"Brand: {self.make}, Model: {self.model}, Year: {self.year}, Doors: {self.doors}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, cc):
        super().__init__(make, model, year)
        self.cc = cc
    def display_info(self):
        print(f"Brand: {self.make}, Model: {self.model}, Year: {self.year}, CC: {self.cc}")

gsxr = Motorcycle("Suzuki", "GSXR", 2019, 600)
gsxr.display_info()
enzo = Car("Ferrari", "Enzo", "2004", 2)
enzo.display_info()

# 5. Create a class called Employee with attributes for name, employee_id, and salary. 
# Add methods to display employee information and give a raise to the employee.
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    def display_info(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Salary: ${self.salary}")
    def raise_sal(self, raise_am):
        self.salary += raise_am

james = Employee("James", 38745, 5000) 
james.display_info()
james.raise_sal(2000)
james.display_info()   

# 6. Define a class BankAccount with attributes for account_number, account_holder, and balance.
#  Create methods for depositing and withdrawing money from the account.
class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Balance after deposit: ${self.balance}")
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"Balance after withdraw: ${self.balance}")
        else:
            print("You can not withdraw so much money!")
james = BankAccount(88888, "James Jameson", 20000)
print(james.balance)
james.deposit(2000)
james.withdraw(22000)
james.withdraw(1000)

# 7. Create a class Book with attributes for title, author, and publication_year. 
# Then, create a class Library that manages a collection of books, including methods to add, remove, and list books.
class Book: 
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

class Library:
    def __init__(self):
        self.books = []
    def add(self, book):
        self.books.append(book)
    def remove(self, title):
        self.books = [book for book in self.books if book.title != title]
    def list_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

book1 = Book("The Godfather", "Mario Puzo", 1972)
book2 = Book("Harry Poter", "J.K Rawling", 1984)
library = Library()
library.add(book1)
library.add(book2)
library.list_books()
library.remove("Harry Poter")
library.list_books()

# 8. Create a class Student with magic methods __init__ and __str__. 
# The __init__ method initializes a student's name and age, 
# and the __str__ method returns a custom string representation.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

frank = Student("Frank", 21)
print(frank)

# 9. Define a class Point with magic methods __init__, __str__, and __add__ to represent 2D points. 
# The __add__ method should allow you to add two points element-wise.
class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"x: {self.x}, y: {self.y}"
    def __add__(self, other):
        return Point(self.x + other.x , self.y + other.y)
point1 = Point(2, 1)
point2 = Point(5, 4)
result = point1 + point2
print(result)

# 10. Create a class MyList with magic methods __init__, __str__, __len__, and __getitem__ to simulate a simple list.
class MyList:
    def __init__(self, *elems):
        self.elems = list(elems)
    def __str__(self):
        return self.elems
    def __len__(self):
        return len(self.elems)
    def __getitem__(self,index):
        return self.elems[index]
my_list = MyList(1, 7, 4, 2, 8 ,22)
print(my_list)
print(len(my_list))
print(my_list[3])

# 11. Create a class Person with a private variable _ssn to represent a Social Security Number. 
# Add methods to set and get the SSN with data hiding, ensuring that the SSN is stored privately.
class Person: 
    def __init__(self, name, ssn):
        self.name = name
        self._ssn = ssn
    def set_ssn(self, ssn):
        self._ssn = ssn
    def get_ssn(self):
        return self._ssn
    
person1 = Person("Alex", "1-234-567-89")
print("Name:", person1.name)
print("SSN (Hidden):", person1.get_ssn())
    

# 12. Create a class Calculator with a private method _add to add two numbers. 
# Use a public method to access the private method.
class Calculator: 
    def _add(self, x , y):
        return x + y
    def add_nums(self, x , y):
        return self._add(x, y)

calc = Calculator()
calc._add(2, 3) # prints 5
calc.add_nums(2 ,3) # prints 5

# 13. Define a class Circle with a private variable _radius.
# Implement a method to calculate the area of the circle while keeping _radius hidden.
import math
class Circle:
    def __init__ (self, radius):
        self._radius = radius
    def _area(self):
        return self._radius ** 2 * math.pi
    def display_area(self):
        return self._area()

circle1 = Circle(2)
area = circle1.display_area()
print("Circle Area:", area)

# 14. Create a class Counter with a class variable count and a class method increment that increments the count.
# Implement a class method get_count to retrieve the current count.
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


Counter.increment()
Counter.increment()
print("Count:", Counter.get_count())

# 15. Create a class StringSplitter with a class method split_string that splits a string into a list of words. 
# Use the @classmethod decorator to provide an alternative constructor.
class StringSplitter:
    def __init__(self, text):
        self.text = text

    @classmethod
    def split_string(cls, text):
        words = text.split(", ")
        return cls(" ".join(words))

    def get_text(self):
        return self.text

text = "Hello, World"
split_text = StringSplitter.split_string(text)
print("Original Text:", text)
print("Split Text:", split_text.get_text())

#! ----------- Exceptions exercise -----------
# 1. Write a program that takes two numbers as input and handles a ZeroDivisionError if the second number is zero.
try:
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Can't divide by 0!")
    
# 2. Create a program that attempts to open a file and handles a FileNotFoundError if the file does not exist.

# 3. Write a program that handles an IndexError when accessing an element of a list that is out of bounds.

# 4. Create a program that handles a NameError when attempting to access an undefined variable.

# 5. Write a program that handles a TypeError when trying to concatenate a string and an integer.