#For loop is used to iterate the elements of list or sets or any collection of data.

list1 = ["Rohit","Mohit","Lohith","Raunit"]
for i in list1:
    print(i)
print("\n")
#In case of list of lists for loop prints the lists inside the list

list2 = [["Rohit",1],["Mohit",20],["Lohith",3],["Raunit",10]]
for it in list2:
    print(it)
print("\n")
#But if we use two variables then we will not get the lists.

for j,k in list2:
    print(j," has ",k," chocolates.")

#we can also convert the list into dictionary and access it using for loop.
print("\n")
dict1 = dict(list2)
for l,m in dict1.items():
    print(l,"is having",m,"chocolates.")

print("\n")

for n in dict1:   #It is printing only keys not the values.
    print(n)

print("\n")
# We can also generate sequence numbers using for loop.

for o in range(1,21):
    print(o, end=" ")

print(" ")

#create a list and print the numbers which is less than 10.

list5 = [5, 9, 7, 5, 48, 54, 84, 51, 8, 5, 14, 8, 51, 4, 48, 7, 8, 45, 8, 4, 5, 8, 5, 7]
for pq in list5:
    if pq < 10:
        print(pq, end=" ")
 
