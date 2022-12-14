import random
import string

#Generate a new password
def generate_password():

  password_length = 0
  #until the password length is at least 6 characters, prompt the user to choose a length
  while password_length < 6 or password_length > 24:
    password_length = int(input("To create a password, please enter your desired password length. Length must be a number between 6 and 24: "))
  print("Your password will be " + str(password_length) + " characters long.\n")

  #set excluded characters
  excluded_character_types = -1
  character_set = [1, 2, 3, 4]
  while excluded_character_types < 0 or excluded_character_types > 4:
    excluded_character_types = int(input("Would you like to exclude any character types?\n1 UPPERCASE letters\n2 lowercase letters\n3 numbers\n4 punctuation\n0 include all character types: \n"))
    #eliminate excluded characters from list
    if (excluded_character_types == 0):
      print("You chose to use all character types.\n")
    elif(excluded_character_types == 1):
      character_set = [2, 3, 4]
      print("You chose to exclude uppercase letters.\n")
    elif(excluded_character_types == 2):
      character_set = [1, 3, 4]
      print("You chose to exclude lowercase letters.\n")
    elif(excluded_character_types == 3):
      character_set = [1, 2, 4]
      print("You chose to exclude numbers.\n")
    elif(excluded_character_types == 4):
      character_set = [1, 2, 3]
      print("You chose to exclude punctuation.\n")
    else:
      print("You did not enter a valid number.")

  #create empty password list
  password = []

  #populate password list
  def random_character_generator(password_length, excluded_character_types):
    while len(password) < (password_length * 2):
      
      def choose_character_set():
        #choose character set
        current_char_set = random.choice(character_set)
        
        #choose number of values for this iteration
        set_length = random.randrange(1, (password_length - 2))

        #character_type corresponds to user character type menu
        if (current_char_set == 1):
          password.extend(random.choices(string.ascii_uppercase, k = int(set_length)))
        elif (current_char_set == 2):
          password.extend(random.choices(string.ascii_lowercase, k = int(set_length)))
        elif (current_char_set == 3):
          password.extend(random.choices(string.digits, k = int(set_length)))
        elif (current_char_set == 4):
          password.extend(random.choices(string.punctuation, k = int(set_length)))
        print(password)
        
      choose_character_set()

    #remove duplicate values
    new_password = list(dict.fromkeys(password))

    #shuffle generated password
    random.shuffle(new_password)

    #convert password to string and return password of desired length
    password_str = ''
    print("Your new password is: " + password_str.join(new_password[0:password_length]))

    #prompt user to generate new password
    generate_new = 'N'
    while generate_new == 'N':
      generate_new = input("Would you like to create another password? Y N: ")
      
      if generate_new == 'Y' or generate_new == 'y':
        print("Let's create a new password.\n")
        generate_password()
      
  random_character_generator(password_length, excluded_character_types)