#Write a program to print numeral of a 4 digit number
numm = 1000
while(numm<=9999):
    thsnd={"0":"Zero", "1":"One", "2":"Two", "3":"Three", "4":"Four", "5":"Five", "6":"Six", "7":"Seven", "8":"Eight", "9":"Nine"}
    tns1={"10":"Ten", "11":"Eleven", "12":"Twelve", "13":"Thirteen", "14":"Fouteen","15":"Fifteen", "16":"Sixteen", "17":"Seventeen","18":"Eighteen", "19":"Nineteen"}
    tns2={"2":"Twenty","3":"Thirty", "4":"Forty","5":"Fifty", "6":"Sixty", "7":"Seventy", "8":"Eighty", "9":"Ninety"}
    num=str(numm)
    if num[1:4]=="000":
        print(thsnd[num[0]]," Thousand")
    elif num[1:3]=="00":
        print(thsnd[num[0]]," Thousand ",thsnd[num[3]])
    elif num[1]=="0" and num[2:4] in tns1.keys():
        print(thsnd[num[0]]," Thousand ",tns1[num[2:4]])
    elif num[1]=="0" and num[3] == "0":
        print(thsnd[num[0]]," Thousand ",tns2[num[2]])
    elif num[1]=="0":
         print(thsnd[num[0]]," Thousand ",tns2[num[2]], thsnd[num[3]])
    elif num[2:4]=="00":
         print(thsnd[num[0]]," Thousand ",thsnd[num[1]]," Hundred")
    elif num[2]=="0":
        print(thsnd[num[0]]," Thousand ",thsnd[num[1]]," Hundred ",thsnd[num[3]])
    elif num[3]=="0":
        print(thsnd[num[0]]," Thousand ",thsnd[num[1]]," Hundred ",tns2[num[2]])
    else:
        print(thsnd[num[0]]," Thousand ",thsnd[num[1]]," Hundred ",tns2[num[2]]," ",thsnd[num[3]])
    numm = numm+1
    if(numm>9999):
        break


