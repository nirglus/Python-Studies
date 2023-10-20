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

# 3. Create a list of strings and use map() and a lambda function to reverse each string in the list.

# 4. Given a list of integers, use filter() and a lambda function 
# to create a new list containing only the even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 5. Create a list of names and use filter() and a lambda function to create a new list 
# with names that contain the letter 'a'.

# 6. Given a list of words, use filter() and a lambda function to create a new list 
# with words that have a length of 6 or more characters.
words = ["apple", "banana", "cherry", "date", "elephant", "grape"]
