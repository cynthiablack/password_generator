# Overview

This program generates a password on demand. Password length is chosen by the user from a range of 6 to 24 characters. Users can choose whether to include all character types or exclude a specific character type: uppercase letters, lowercase letters, numbers (0-9), and punctuation, or include all character types.

## How to Run the Program

**Start command** generate_password()

**Options**

- password length: at least 6 characters and not more than 24 characters
- excluded characters: include all or exclude one of: uppercase letters (1), lowercase letters (2), numbers (3), punctuation (4). To include all choose option 0.

## How the Program Works

The program was written in Python3. When the generate_password() function is called, the user is asked for two inputs: password length and which character types (if any) to exclude. The program validates these inputs; if the user inputs enters an invalid response, the prompt runs again until a valid response is entered.

The next steps of the program rely heavily on random number generation: two random numbers are generated for each section of the password: one to select the target character set and a second to choose how many characters to pull from the selected set. Further random-number logic is used to select the characters (via the _choices_ method built into Python's _Random_ module). The selected characters are then added to the password and the random-number steps of the progress run again untl twice the desired password length is reached.

Next, the program shuffles the generated password, checks for and replaces any duplicate values, shuffles the password again, truncates the generated password to the desired lenght, then finally displays this final version of the password.

The user is then asked if they would like to run the program again.
