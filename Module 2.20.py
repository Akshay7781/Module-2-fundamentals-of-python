#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string

mystr =input("Enter string : ")

print(mystr)

print(mystr.find('not poor'))

print(mystr.replace( 'not poor', 'good'))