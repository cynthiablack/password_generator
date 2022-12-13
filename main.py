import random
import string

#Generate a new password
def generate_password():

  password_length = 0
  #until the password length is at least 6 characters, prompt the user to choose a length
  while password_length < 6 or password_length > 24:
    password_length = int(input("To create a password, please enter your desired password length. Length must be a number between 6 and 24: "))
  print("Your password will be " + str(password_length) + " characters long.")

  #set excluded characters
  excluded_character_types = -1
  while excluded_character_types < 0 or excluded_character_types > 4:
    excluded_character_types = int(input("Would you like to exclude any character types?\n1 UPPERCASE letters\n2 lowercase letters\n3 numbers\n4 punctuation\n0 include all character types: "))
  print("You chose " + str(excluded_character_types))

  #create empty password list
  password = []

  #populate password list
  def random_character_generator(password_length, excluded_character_types):
    while len(password) < (password_length * 2):
      #choose character set
      def choose_character_set():
        character_set = random.randrange(1, 4)
        set_length = random.randrange(1, (password_length - 2))

        #character_type corresponds to user character type menu
        if (character_set == 1):
          password.extend(random.choices(string.ascii_uppercase, k = int(set_length)))
        elif (character_set == 2):
          password.extend(random.choices(string.ascii_lowercase, k = int(set_length)))
        elif (character_set == 3):
          password.extend(random.choices(string.digits, k = int(set_length)))
        elif (character_set == 4):
          password.extend(random.choices(string.punctuation, k = int(set_length)))
        print(password)
        
      choose_character_set()

    #remove duplicate values
    new_password = list(dict.fromkeys(password))
    print(new_password)

    #shuffle generated password
    random.shuffle(new_password)
    print(new_password)

    #convert password to string and return password of desired length
    password_str = ''
    print(password_str.join(new_password[0:password_length]))

  random_character_generator(password_length, excluded_character_types)