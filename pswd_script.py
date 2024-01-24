import argon2
from argon2 import PasswordHasher

#Script to Crack passwords that are from the 200 most used password list and have been hashed using argon2 algorithm. 
#The script takes in a hash config from the user's hash config needs to be known.
#It tests digit + word + digit so it finds the matching hashed password.
#Example: 
#0passWord0 --> false
#0passWord1
#0passWord2 --> true and then prints: "Password found: 0passWord1"

def generate_password(word, index):
    # Select one digit in a systematic way
    digit1 = str((index // 10) % 10)
    digit2 = str(index % 10)

    # Combine the components to form the password
    password = digit1 + word + digit2
    return password

def crack_passwords(hash_config, password_file):
    ph = PasswordHasher()

    with open(password_file, 'r') as file:
        word_list = file.readlines()

    for word in word_list:
        word = word.strip()

        # Try all digit combinations around the current word
        for i in range(100):  # Trying all two-digit combinations
            # Generate a password based on the given criteria
            candidate_password = generate_password(word, i)
            print(candidate_password)

            # Attempt to crack the hash with the generated password
            try:
                if ph.verify(hash_config, candidate_password):
                    print(f"Password found: {candidate_password}")
                    return
            except argon2.exceptions.VerifyMismatchError:
                pass

    print("Password not found in the given password file.")

if __name__ == "__main__":
    hash_config = ""
    password_file = input("Enter the path to the password file: ")

    crack_passwords(hash_config, password_file)