#It is a data type of Dictionary
#An ordered collection of data in key:value pair form
#Collection of pairs are enclosed in curly braces

#defining a dictionary

dict = {}
print(type(dict))

d1 = {"Pen":"Ink","Pencil":"Sharpner","Colour":{"Dark":"Balck","Light":"White"}} #We can aso insert a dictionary into a dictionary
print(d1)
print(d1["Pen"]) #dictionary slicing
print(d1["Colour"])
print(d1["Colour"]["Dark"])#printing value of a dictionary in a dictionary'

#Updating dictionary
d1["Laptop"] = "Charger"
print(d1)

#updating multiple values at one time
d1.update({"Phone":"Sim","Sony":"Speaker"})
print(d1)
d3=d1 #It will craete a reference of d1. Any change in d3 will affect d1.
print(d3)

d2=d1.copy()#it will create  a copy of d1 changes in d2 will not effect d1
del d2["Pen"]#Deleting the key and value of Pen
print(d2)
print(d1)

print(d1.keys())#printing all the keys
print(d1.values())#printing all the values
print(d2.items())#printing all key value pairs
