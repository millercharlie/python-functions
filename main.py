# In this project, we will practice functions by manipulating Strings

# The user will put in a String as input and then call various functions to change the String

# For instance:
#   If the user wrote "Jacob" and called the function multiply_string(3)
#      It would print JacobJacobJacob

# Let's begin

user_input = input('Type in anything you wish here! ')

def multiply(user_string, num):
  global user_input
  user_input = user_string * int(num)
  print('Your new String is: ' + user_input)

def concatenate(user_string, another_string):
  global user_input
  user_input = user_string + another_string
  print('Your new String is: ' + user_input)

def capitalize(user_string):
  global user_input
  user_input = user_string.upper()
  print('Your new String is: ' + user_input)

def swapcase(user_string):
  global user_input
  user_input = user_string.swapcase()
  print('Your new String is: ' + user_input)

while True:
  print('These are your choices to manipulate the String!')
  
  print('multiply') # multiplies the String by a given number
  print('concatenate') # will take in another String to add to the end of this String
  print('capitalize') # Capitalizes all letters in a String
  print('swapcase') # Switches the case of each letter in the String

  # Feel free to add any others you wish!

  choice = input('How would you like to manipulate this String? (Type "exit" to Exit the manipulation) ')

  if choice == 'multiply':
    print('You have chosen to multiply the String!')
    number = input('How much would you like to multiply by? ')
    multiply(user_input, number)
    
  elif choice == 'concatenate':
    print('You have chosen to concatenate the String!')
    other_string = input('What String would you like to add? ')
    concatenate(user_input, other_string)

  elif choice == 'capitalize':
    print('You have chosen to capitalize the String!')
    capitalize(user_input)

  elif choice == 'swapcase':
    print('You have chosen to swap the cases of the String!')
    swapcase(user_input)

  elif choice == 'exit':
    break
  
  else:
    print('This is not a valid operation. Please try again!')

print('Your final String is: ' + user_input)




