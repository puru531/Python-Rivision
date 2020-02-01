#If, else and elif return boolean result as true or false


age = int(input("What is your age? : "))
if age<5 or age>120:
    print("You are underage or overage.")
elif age>18:
    print("You are eligible for driving licence.")
elif age<18:
    print("You are not eligible for driving licence.")
else:
    print("I cannot decide.")
