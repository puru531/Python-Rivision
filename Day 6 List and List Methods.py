#List is a data structure which is uesd to store hetrogenous type of data, it can also hold duplicate data

list1=[5,99,6,"Laptop","Phone",82,42,"charger",654,64,"Cable",16,6,5]#Declaring and initializing a list
print(list1)
#list slicing
print(list1[2])#will print element at index 2
print(list1[2:7])#will print elements from index 2 to 6
print(list1[1:13:2])#index 1 to 12 by skipping one element
print(list1[:10])#index zero to index 9
print(list1[3:])#print elements after index 3 to last
print(list1[::])#will print all the elements of list
print(list1[::3])#prints all the elements but by skipping 2 elements
print(list1[::-1])#It will reverse the list

#List methods
list2=[5,8,4,85,54,48,84,54,9,4,5,5,14,5,5,411,5,54,4,8,48,2,245,4,84,84,51,548]
print(len(list2))#find length of list
list2.append(12)#Adds 12 at last
print("list after appending 12 :",list2)
list2.insert(5,56454)#will insert 56454 at index 5
print("list after inserting 56454 at index 5:",list2)
list2.remove(4)#will remove 4 from the list
print("list after removing 4 :",list2)
list2.pop()#delete the last node
print("list after pop :",list2)
list2[3]=16541 #replacing the element of index 3 with another number
print("list after replacing element at index 3 with another number :",list2)
list2.sort()#will sort the list
print("list after sorting :",list2)
list2.reverse()#will reverse the list
print("list after reversing :",list2)
list3=list1+list2
print(list3)
print(" ")



#Tuples
#Tuples are immutable that means we can't insert or replace the elements in a tuple

print("---Tuple---")
print(" ")
tp=(2,)#it is necessary to give comma after the element in a one element array
print(tp)

#If we want to make an change in the tuple we need to convert it into the list

tpl=(3,69,4,9,8,8,5,56,4,95,"box","pencil","pen",65,65)
print(tpl)
#we cannot do slicing in tuple
list4 = list(tpl) #converting a tuple into a list
print(list4)
#Now we can apply all the methods of a list in this

#converting list into tuple
tpll=tuple(list4)
print(tpll)
