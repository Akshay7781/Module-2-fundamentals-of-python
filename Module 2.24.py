#Write a Python function to insert a string in the middle of a string

str= input("Enter a string: ")
x = input("Enter a sub string: ")
y = int(input ("Enter position: "))

words = str.split()
words.insert(y,x)
strnew = '  '.join(words)
print(strnew)


