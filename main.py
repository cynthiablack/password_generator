import string
# Create variables for each character type
char_1 = string.ascii_uppercase
char_2 = string.ascii_lowercase
char_3 = string.digits
char_4 = string.punctuation

#Generate a new password
def generate_password():
    password_length = 0
    #until the password length is at least 6 characters and no more than 24 characters, prompt the user to choose a length
    while password_length < 6 or password length < 24:
        password_length = int(input("To create a password, please enter your desired password length. Length must be a number between 6 and 24: "))



# Until user enters a number less than 6 or greater than 24
# Remind user to enter a number that is between 6 and 24
# Prompt user to enter a number between 6 and 24
# When user enters a number between 6 and 24
# Store entered number in password_length variable

# Prompt user for excluded character types:
# “Would you like to exclude any character types?
# 1 UPPERCASE letters
# 2 lowercase letters
# 3 numbers
# 4 punctuation
# 0 include all character types”

# Until user enters 0, 1, 2, 3, 4
# Remind user to enter 0, 1, 2, 3, or 4
# Prompt user to enter a valid number
# When user enters 0, 1, 2, 3, or 4
# Store entered number in excluded_character_types variable

# Function random_character_generator(password_length, excluded_character_types)

# set password = []
# loop until len(password) == password_length
# function choose_character_set()
# set character_set = 0
# loop until random_number != excluded_character_types
# choose random_number from 1, 2, 3, 4
# when excluded_character_types != random_number
# update character_set = random_number

# function choose_set_length()
# set set_length = 0
# set temp_list = []
# choose random_set_length > 1
# update set_length = random_set_length
# if set_length <= password_length
# update temp_list = random.choices(character_set, k = set_length)
# password.extend(temp_list)
# when len(password) == password_length
# print(password)
# function request_new_password()
# Prompt user:
# “Would you like to generate another password? Y N”
# if user enters Y
# generate_password()
# else
# pass
