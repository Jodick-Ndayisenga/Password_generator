# Password generator

This code generates a password based on certain character requirements. Here's how it works:

    The code imports the random module.

    Strings pass_lower, pass_upper, pass_symbols, and pass_digit are defined, representing lowercase letters, uppercase letters, symbols, and digits, respectively.

    An empty string named all_characters is initialized to store all the possible characters for the password.

    The code checks each of the character requirements (lowercase letters, uppercase letters, symbols, and digits) and adds the corresponding characters to all_characters.

    Three counters (UPPER, SYMBOL, and DIGIT) are initialized to keep track of the number of uppercase letters, symbols, and digits in the generated password.

    The code enters a while loop, prompting the user to choose whether to generate a password or not. If the user does not choose to play (enters anything other than "yes"), the program quits.

    If the user chooses to play, a password of length 10 is generated using random.sample() on all_characters. The generated password is stored in the variable PASSWORD.

    The generated password is then checked for the specified character requirements using for loops:
        Each character in pass_upper is checked in the generated password. If a character is found, the UPPER counter is incremented.