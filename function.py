"""
Title : module of function for astraline

Version : 1.0

Author : Elias De Bernardo

Date : 14/09/2023
"""
import random
import string

# Funtion that ask the lenght wanted for the password
def get_password_length():
    while True:
        try:
            length = int(input("Enter the length of the password (max 16 characters): "))

            if 1 <= length <= 16:

                if length <= 12:
                    choice = input("Password potentially vulnerable. Do you want to increase its length (Yes/No)? ").lower()

                    if choice == "yes":
                        continue  # Restart the loop to enter a new length

                    elif choice == "no":
                        return length
                    
                    else:
                        print("Please answer with 'yes' or 'no'.")

                else:
                    return length
                
            else:
                print("The length must be between 1 and 16 characters. Try again.")
                
        except ValueError:
            print("The value entered must be an integer. Try again.")


# Function that ask if the user want special characters
def get_special_characters():
    
        choice = input("Do you want to include special characters ? (Yes/No) : ").lower()

        if choice in ["yes", "no"]:
            return choice == "yes"
        
        else:
            print("Please answer by 'yes' or 'no'.")

# Function that ask if the user want numbers
def get_digits():
    
        choice = input("Do you want to include digits ? (Yes/No) : ").lower()

        if choice in ["yes", "no"]:
            return choice == "yes"
        
        else:
            print("Please answer by 'yes' or 'no'.")

# Function that print an Welcome Message 
def print_welcome_message():
    print("|Welcome on the Astraline Password Generator|")


# Main function that generate the password
def generate_password():
    print_welcome_message()
    length = get_password_length()
    include_special = get_special_characters()
    include_digits = get_digits()

    # Normal Characters
    characters = string.ascii_letters

    if include_special:

         # Add Special Characters
        characters += string.punctuation 

    if include_digits:

         # Add the digits
        characters += string.digits 

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


