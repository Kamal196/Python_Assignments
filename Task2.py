#QUESTION1:
x = eval(input("ENTER THE NUMBER"))
if x%3==0 and x%5==0:
    print("Consultadd Python Training")
elif x%3==0:
    print("Consultadd")
elif x%5==0:
    print("c")

#QUESTION2:
x= int(input("ENTER THE CHOICE 1(ADDITION), 2(SUBTRACTION), 3(DIVISION), 4(MULTIPLICATION), 5(AVERAGE)"))
if x==1 or x==2 or x==3 or x==4:
    first=eval(input("Enter the first no."))
    second=eval(input("Enter the second no."))
    if x==1:
        print(first+second)
    if x==2:
        print(first-second)
    if x==3:
        print(first*second)
    if x==4:
        print(first/second)
elif x==5:
    first1=eval(input("Enter the first1 no."))
    second1=eval(input("Enter the second2 no."))
    avg = (first1+second1)/2
    print(avg)
elif x<0:
    print("NEGATIVE")
