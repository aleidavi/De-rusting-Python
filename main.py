'''
Here's a study guide to practice core Python syntax.

For each task, beneath the comment write the code and print out the result to check it works
'''

'''LISTS'''
#
## Create a list and assign it to a variable
name = 'aleida'
arr = list(name)
#print(arr)
#
## Find the length of the list
#print(len(arr))
#
## Append an item to the list
#
last_name = 'vieyra'
last_name = list(last_name)
arr = arr + last_name
#print(arr)
#
## Find the value of an item in the list a specific index
#print(arr[-1])
## Set the value of an item at a specific index
#
#arr[-1] = '@'
#print(arr)
#
## Check whether an item is in the list
#
#print('@' in arr)
#
## Sort the list
#sorted_arr = sorted(arr)
#print(sorted_arr)
#
## Iterate over the list using range, printing out each element and the index
#
#for element in range(len(arr)):
#	print(arr[element], element)
#
## Iterate over the list without using range, printing out each element
#for char in arr:
#	print(char)
#
#i = 0
#while i < len(arr):
#	print(arr[i])
#	i += 1


'''TUPLES'''

# Create a tuple and assign it to a variable

toop = tuple(arr)

# Find the length of the tuple
print(len(toop))
print(toop)

# Find the value of an item in the tuple a specific index
print(toop[9])
# Check whether an item is in the tuple
print("a" in toop)

# Iterate over the tuple using range, printing out each element and the index

for i in range(len(toop)):
	print(toop[i], i)

# Iterate over the tuple without using range, printing out each element

for char in toop:
	print(char)

'''STRINGS'''

# Create a string and assign it to a variable
new_str = 'variable'

# Find the length of the string
len(new_str)

# Find the value of an character in the string a specific index
print(new_str[0])

# Check whether an item is in the string
print('o' in new_str)
# Concatenate (add) two strings together

add_str = 'practice'

print(new_str+" " +add_str)

# Create an f-string
f_string = f"This {new_str} is printed inside an f-string in python."
print(f_string)

# Split a string using .split
f_string = f_string.split()
print(f_string)
# Join a list of strings using .join

joined_str = " ".join(f_string)
print(joined_str)

# Iterate over the string using range, printing out each character and the index
for i in range(len(joined_str)):
	print(joined_str[i], i)

# Iterate over the string without using range, printing out each character

for char in joined_str:
	print(char)

'''DICTIONARIES'''

# Create a dictionary and assign it to a variable

# Find the length of the dictionary

# Add a new key/value pair

# Replace value for a given key

# Check whether a key is in the dictionary

# Iterate over keys, printing each key

# Iterate over over key/value pairs using .items(), printing each key and value

'''SETS'''

# Create a set and assign it to a variable

# Find the length of the set

# Add a new element

# Remove an element

# Check whether a element is in the set

# Iterate over elements, printing each one out

'''NUMBERS'''

# Add / subtract / multiply 2 numbers

# Divide two numbers using normal (float) division

# Divide two numbers using integer division

# Find the modulo (remainder) of two numbers

# Check whether a number is even/odd

# Round a float down to an int


'''FUNCTIONS'''

# Write a function that takes no arguments and call it

# Write a function that takes one or more arguments and call it

# Write a function that returns a value. Call the function and store the return value in a variable

'''LOOPS'''

# Write a while loop

# Write a for loop that loops a set number of times (e.g. 10 times)

'''CONDITIONALS'''

# Write an if/elif/else statement

# Write conditionals for the following operators:
# ==
# !=
# <
# >
# <=
# >=

'''NESTED DATA'''

# Write a nested list (a list of lists) and assign it to a variable

# Print an item at a specific position in the data structure (e.g. the item at a given row and column). HINT: row comes first, column comes second

# Iterate through the nested data structure using range

# Iterate through the nested data structure without using range 

'''REMINDER'''

# You're doing great and you got this!
