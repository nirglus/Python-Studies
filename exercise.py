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

# 9. Initialize a list of names and capitalize the first letter of each name. 
# Display the modified list.

# 10. Initialize a string and convert it to all uppercase and all lowercase.

# 11. Initialize an empty shopping list, add items to it, and remove items.










