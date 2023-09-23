# dillon, kaden, sarah



dillon_age = 13
kaden_age = 14
sarah_age = 13


# Birthday
dillon_age = dillon_age + 1
kaden_age = kaden_age + 1
sarah_age = sarah_age + 1
dillon_age = dillon_age + 1
kaden_age = kaden_age + 1
sarah_age = sarah_age + 1
dillon_age = dillon_age + 1
kaden_age = kaden_age + 1
sarah_age = sarah_age + 1
dillon_age = dillon_age + 1
kaden_age = kaden_age + 1
sarah_age = sarah_age + 1


# sum of 2 numbers

def sum2(num1, num2):
  sum = num1 + num2
  return sum

sum = sum2(1, 2)
print(sum)




def birthday(age):
  new_age = age + 1
  return new_age

birthday(dillon_age)
birthday(kaden_age)
birthday(sarah_age)




























# Let's say you have a group of friends

# How would you traditionally represent their ages?

dillon_age = 12
kaden_age = 13
sarah_age = 11

# What if it was dillon's birthday?
# We know that his age would increase by 1 year right?

dillon_age = dillon_age + 1

# However, it can become more complicated as everyone else begins to have birthdays, especially if you have more people

kaden_age = kaden_age + 1
sarah_age = sarah_age + 1
dillon_age = dillon_age + 1
kaden_age = kaden_age + 1
sarah_age = sarah_age + 1
dillon_age = dillon_age + 1
kaden_age = kaden_age + 1
sarah_age = sarah_age + 1
dillon_age = dillon_age + 1

# How can we simplify this code down?

# We can create what is called a function

# Functions are designed to perform specific tasks

# Functions can take in data, called arguments, which can be accessed within

# A function will only run when it is called

# Lets look at an example of a template for a function

def my_function(arguments):
  # Code goes here
  return ...

# Let's break this down

# the "def" keyword means "define", so you're defining a new function

# the "my_function" phrase is the name of the function, much like how you would name variables

# the "arguments" within the parenthesis is the data you pass into a function (I'll show you an example of this later!)

# the "return" keyword means that the function terminates at the value that is returned

# Let's look at a simple example by defining a function called "sum" that takes in 2 numbers

def sum(num1, num2):
  sum = num1 + num2
  return sum

# but how do you actually run this function? Remember, functions only run when they are called by the user!

# "num1" and "num2" can be defined by the user below

answer = sum(1, 2)
print(answer)

# here 1 and 2 are passed as "num1" and "num2", respectively

# the "return" returns 3, and the result is stored in the "answer" variable

# when it prints, it will display 3

# pretty cool, right?

# Let's get back to our initial problem with birthdays

# How can we use our newfound knowledge of functions to age the friend group?

def birthday(person_age):
  new_age = person_age + 1
  return new_age

# now, we can write this differently

birthday(dillon_age)
birthday(sarah_age)
birthday(kaden_age)
birthday(dillon_age)
birthday(sarah_age)
birthday(kaden_age)

# Looks much better, right?

# Now, we don't have to keep using the same equation every time they get a year older!

# Let's say you wanted to create a function that performs a mathematical operation to two numbers

# For example, if you put in 2, 3, "multiply", the function would multiply the numbers and return the result

# We want this function to be able to add, subtract, multiply, and divide these two numbers

# How would we do this?

def mathematics(num1, num2, operator):
  if operator == 'add':
    return num1 + num2
  elif operator == 'subtract':
    return num1 - num2
  elif operator == 'multiply':
    return num1 * num2
  elif operator == 'divide':
    return num1 / num2
  else:
    return 'Operation Invalid :('


# How would we run this function?

a = mathematics(10, 5, 'add') # returns 15
s = mathematics(4, 2, 'subtract') # returns 2
m = mathematics(2, 3, 'multiply') # returns 6
d = mathematics(36, 6, 'divide') # returns 6
o = mathematics(0, 1, 'square') # returns 'Operation Invalid :('

# Congratulations! You have now learned the basics of functions in Python!

# Functions can get very complicated the more you use them, so it is good to get a lot of practice with them beforehand

# Now, I want you all to create your own function.

# Let's say you are planning a birthday party

# I want you to make 3 functions to aid yourself in planning this party

# The first function must:
#   Add items to a shopping list (such as 'party hats', or 'cake', or 'decorations')
#  Return this list

def party_list():
  shopping_list = []
  while True:
    item = input('What do you want to add to your list? ')
    if item == 'done':
      break
    else:
      shopping_list.append(item)
  return shopping_list

party_list()

# The second function must:
#   Display a list of choices of the venue (such as 'house', 'Disneyland', 'Go-Kart Track')
#   Ask the user to choose one
#   Return the venue the user chose

# Here is some starter code to get you going:

def venue():
  print('Choose your venue below! ')
  print('Go-Kart Track')
  print('Disneyland')
  ...
  # Get the user input for the venue
  return ...

# The third function must:
#   Ask the user for a theme
#   Ask the user for a list of decorations for that them stored in a list
#   Return the list

def theme():
  decorations = []
  theme = input('What theme would you like your party to be? ')
  while True:
    ...
    # Get the user input of the decorations to add
    decorations.append(...)
  return ...
