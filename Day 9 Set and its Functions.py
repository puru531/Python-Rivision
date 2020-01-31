#Set is a collection of wel defined unique object.

#Defining a set

s = set()
print(s)
print(type(s))

#Elements of set is added in the form of list
s1 = set([1,2,3,4])
s1.add(5)
print(s1)

#It also prints the elements in ascending order

s2 = set([7,9,5,3,1])
print(s2)

#union in sets
s3 = s1.union(s2)
print(s3)
