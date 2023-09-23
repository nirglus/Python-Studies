# ------- String exercises -------
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