import random

pass_lower = 'abcdefghijklmnoprstuvwxyz'
pass_upper = pass_lower.upper()
pass_symbols = '!@#$%^&*()_+=-.,;:'
pass_digit = '0123456789'

#pass_lower, pass_upper, pass_symbols, pass_digit = True, True, True, True
all_characters = ''

if pass_lower:
    all_characters += pass_lower

if pass_upper:
    all_characters += pass_upper

if pass_symbols:
    all_characters += pass_symbols

if pass_digit:
    all_characters += pass_digit

UPPER = 0
SYMBOL = 0
DIGIT = 0

while True:
    choice = input('Do you wanna play or not: ').lower()
    if choice != 'yes':
        quit()
    else:
        PASSWORD = ''.join(random.sample(all_characters, k=10))
        for i in pass_upper:
            if i in PASSWORD:
                UPPER += 1
                if UPPER >= 2:
                    pass
                else:
                    continue
            else:
                continue

        for j in pass_symbols:
            if j in PASSWORD:
                SYMBOL += 1
                if SYMBOL >= 1:
                    pass
                else:
                    continue
            else:
                continue

        for k in pass_digit:
            if k in PASSWORD:
                DIGIT += 1
                if DIGIT >= 1:
                    pass
                else:
                    continue
            else:
                pass

        print(f'Your password is: {PASSWORD}')
        print('')
