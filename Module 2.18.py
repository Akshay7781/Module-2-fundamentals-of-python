#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string

str1=input("Enter a string : ")
str2=input("Enter a string : ")

#swap the first two character of each strings

N_str1 = str2[ : 2] + str1[ 2: ]
N_str2 = str1[ : 2] + str2[ 2: ]

#concatenate N_str1 and N_str2

result = N_str1 + "  " + N_str2

print(result)