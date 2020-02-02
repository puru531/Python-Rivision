#Craete a faulty calculator which does all the calculation correct but gives wrong output for 45*3 which should be 555, 56+9 which should be 77 and 56/6 which should be 4.
def faultyCalculator():
    opr = input("Input the any operator(+,-,*,/,%,**,//) for calculation : ")
    fst = int(input("Input first number : "))
    scnd = int(input("Input the second number : "))
    if(opr == "*"):
        if(fst==45 and scnd==3):
            print(555)
        else:
            print(fst,"*",scnd," : =",fst*scnd)
    elif(opr == "+"):
        if(fst==56 and scnd==9):
            print(77)
        else:
            print(fst,"+",scnd," : =",fst+scnd)
    elif(opr == "/"):
        if(fst==56 and scnd==6):
            print(4)
        else:
            print(fst,"/",scnd," : =",fst/scnd)
    elif(opr == "-"):
            print(fst,"-",scnd," : =",fst-scnd)
    elif(opr == "**"):
            print(fst,"**",scnd," : =",fst**scnd)
    elif(opr == "%"):
            print(fst,"%",scnd," : =",fst%scnd)
    elif(opr == "//"):
            print(fst,"//",scnd," : =",fst//scnd)
    else:
        print("Out of range.")
    again()

def again():
    nxt = input("Do you want to calculate again? (y or n) : ")
    if (nxt == "y"):
        faultyCalculator()
    elif (nxt == "n"):
        print("Goodbye!")
    else:
        again()

faultyCalculator()
