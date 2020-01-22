#String ia a collection of characters

myString="My name is Purushottam Kumar"
#Accessing and printing the string variable.
print(myString)

#String slicing

#Index of string starts from zero
print(myString[5])#it will return 5th letter counting from zero

print(myString[2:6])#it will print the characters from 2 to 5 counting form zero (6 is excluded but 2 is included)
print(myString[2:10:3])#It will start printing from 2 and will print up-to 10 but will print every 3rd element only(leaving 2 characters)
print(myString[2:])#will print all the characters starting from index 2
print(myString[:10])#will print elements up-to index 9 starting from index 0
print(myString[:])#will print all the elements from beginning to last.
print(myString[::2])#will print all the characters from beginning to end by skipping one character.

#negative indexing
print(myString[-18:])#it will print the characters from index 18 counting from back side or last character
print(myString[-18:-6])#counting from back side charcaters from 18 to 7 will be printed
print(myString[-29:])


print(myString[::-1])#will reverse the string


#String methods
urString="your name is Purushottam Kumar"
print("Length of strng is", len(urString))#will print the length of the string.
print(urString.isalpha()) #is there any space and only alphabet letters?
print(urString.isalnum())#is there any space and letters and numbers only?
print(urString.endswith("Kumar"))#does the string ends with Kumar?
print(urString.count("m"))#will count how many times m is written
print(urString.capitalize())#will capitalize the first letter
print(urString.lower())#convert all into lowercase
print(urString.upper())#convert all into uppercase.
print(urString.find("m"))#will print index  of m wherever it occurs
print(urString.replace("m","p"))#will convert all m into p
