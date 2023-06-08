#Write a Python function that takes a list of words and returns the length of the longest one.

str1= input("Enter a string : ")
count=0
word=0
for i in str1:
	if(i=='  '):
		count=0
	else:
		count=count+1:
	if(word<count):
		word=count
		
print("The lenght of the longest word: ", word)


