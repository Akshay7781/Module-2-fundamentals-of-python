#Write a Python program to test whether a passed letter is a vowel or not

list = ["a", "e", "i", "o", "u"]
character = input('Enter the character: ')

if character in list:
    print("The character is a vowel.")
else:
    print("The character is not a vowel.")
