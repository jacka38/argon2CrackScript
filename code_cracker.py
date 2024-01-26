from itertools import permutations

# Actual codes
actual_codes = ['9999710']

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
