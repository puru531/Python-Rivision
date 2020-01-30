#Create a dictionary and take input from the user to find its value.

d1 = {"Immutable":"The which cannot be changed.","Mutable":"That which cannot be changed","String":"Collection of characters","Integer":"Number"}
print("Enter any word (Immutable, Mutable, String, Integer) : ")
p=input()
print(p +": "+d1[p])