from itertools import permutations

#Script to Crack the code from a code pad where the code is 4,5,6 or 7 digits long and used only the worn out digits [0, 1, 7, 9]

#Example: 
# 0 incorrect
# 1 incorrect
# 7 incorrect
# 9 correct
# 90 incorrect 
# 91 incorrect 
# 97 correct
# 970 incorrect
# 971 correct
# 9710 correct

# Code found: 9710
# Amount of permutations: 10

#We know this is the maximum attempts to get a correct code from the key pad since after every digit is entered we know if the entered digit was correct or not
#We know these because the 4 digits are worn out so all of those 4 NEED to have been used in the code! 

#With these in mind we can do the math using this python script.

#When the code is 
#4 digits long the maximum attempts to guranteed success is 10 tries
#5 digits long the maximum attempts to guranteed success is 14 tries
#6 digits long the maximum attempts to guranteed success is 18 tries
#7 digits long the maximum attempts to guranteed success is 22 tries

# The codes I've decided to use are the worst case scerario so I get the maximum attempts possible, but keep in mind all of the codes NEED to use all 4 of the worn out digits!
actual_codes = ['9710' ,'99710' ,'999710' ,'9999710']

# Digits that have been worn and have to be used in the code
digits = ['0', '1', '7', '9']

# Maximum length of the code
max_length = 7

# Function to generate permutations of a given length
def generate_permutations(prefix, length, allow_repeats=False):
    if allow_repeats:
        return [str(prefix) + str(digit) for digit in digits]
    else:
        return [str(prefix) + str(digit) for digit in digits if digit not in set(str(prefix))]

# Function to check if all digits are present in the code
def check_digits(code):
    return all(digit in code for digit in digits)

# Function to find the code
def find_code(actual_code):
    # Counter for the number of permutations
    counter = 0
    
    # Counter for the number of incorrect attempts
    incorrect_attempts = 0

    # Flag to break out of the outer loop
    code_found = False

    # Check if the length of the actual code is greater than the maximum length for the keypad model allows
    if len(actual_code) > max_length:
        print("Impossible code, since the length of the code is greater than the maximum length of the keypad allows the code to be!")
        return

    # Test each combination
    prefix = ''
    for _ in range(len(actual_code)):
        remaining_digits = [digit for digit in digits if digit not in set(str(prefix))]
        allow_repeats = len(remaining_digits) <= max_length - len(str(prefix))
        if len(remaining_digits) == 1 and len(prefix) < len(actual_code) - 1:
            prefix += remaining_digits[0]
            print(f"{prefix} correct")
            counter += 1
            continue
        for code in generate_permutations(prefix, len(actual_code), allow_repeats):
            counter += 1
            if code == actual_code[:len(code)]:
                print(f"{code} correct")
                prefix = code
                incorrect_attempts = 0
                if len(code) == len(actual_code) and check_digits(code):
                    print("\n" + f"Code found: {code}")
                    print(f"Amount of permutations: {counter}")
                    code_found = True
                break
            else:
                print(f"{code} incorrect")
                incorrect_attempts += 1
        if code_found:
            break
    if not code_found:
        print("\n" + "Impossible code, since not all digits have been used (0, 1, 7, 9)!" + "\n")

# Find codes for different lengths
for actual_code in actual_codes:
    find_code(actual_code)
    print("\n" + "=" * 40 + "\n")
