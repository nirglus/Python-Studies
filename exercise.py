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
