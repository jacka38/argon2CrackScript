** NOTE THIS IS FOR ONLY SCHOOL PROJECT WHICH SUBJECT WAS ETHICAL HACKING AND USED FOR LEARNING ONLY **


This script is used to crack passwords that have been hashed using the Argon2 algorithm. The script reads a list of words from a file and generates passwords by combining each word with two digits in a systematic way. It then attempts to crack the hash using each generated password. If the password is found, it is printed to the console. If the password is not found, a message is printed to the console indicating that the password was not found in the given password file.

To use this script, you need to provide a hash configuration and a password file. The hash configuration is stored in the hash_config variable. The password file is read from the user input and stored in the password_file variable.

The generate_password function takes a word and an index as input and returns a password that is a combination of the word and two digits. The digits are selected in a systematic way based on the index.

The crack_passwords function takes a hash configuration and a password file as input. It reads the list of words from the password file and generates passwords for each word using the generate_password function. It then attempts to crack the hash using each generated password. If the password is found, it is printed to the console and the function returns. If the password is not found, a message is printed to the console indicating that the password was not found in the given password file.
