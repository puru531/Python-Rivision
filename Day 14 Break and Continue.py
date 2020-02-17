print("Break method")
i=0
while True:
    print(i+1, end=' ')
    if (i==44):
        break
    i=i+1
print("\n")
print("Continue method")
j=0
while True:
    if(j+1<5):
        j=j+1
        continue
    print(j+1, end=' ')
    if(j==44):
        break
    j=j+1

print("\n")