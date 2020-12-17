#Excercise 2-Design a caclulator which will solve all the problems except the following one
#your program should take operator and two numbers as input from the user and return the result
print("1.add +","2.subtract -","3.multiplication","4.division /\n")
print("enter the oprator number\n")
tup1=("1","2","3","4")
comp1=input()
if comp1 in tup1:
        print("enter 1st value\n")
        val1=int(input())
        print("enter second value\n")
        val2=int(input())
        if comp1=="1":
            if(val1==56 and val2==9) or (val1==9 and val2==56):
                print("Result is 77")
            else:
                print("Result is",val1+val2)
        elif comp1=="2":
                print("result is ",val1-val2)
        elif comp1=="3":
            if(val==45 and val2==3):
                print("result is 555")
            else:
                print("result is ",val1*val2)
        else:
            if(val1==56 and val2==6):
                print("result is 4")
            else:
                print("result is",val1/val2)
else:
    print("wrong computauion option\n")
    print("thank you\n")

