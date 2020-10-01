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



#QUESTION3:
a=10
b=20
c=30
avg=(a+b+c)/3
print("Avg=", avg)
if avg>a and avg>b and avg>c:
    print("Avg is higher than a,b,c")
elif avg>a and avg>b:
    print("Avg greater than a and b")
elif avg>a and avg>c:
     print("Avg is higher than a,c")
elif avg>b and avg>c:
    print("Avg is higher than b,c")
elif avg>a:
    print("avg is just greater than a")
elif avg>b:
    print("avg is just greater than b")
elif avg>c:
    print("avh is just greater than c")

#QUESTION4:
while True:
    x = int(input("Enter the VALUE, (-1) TO EXIT"))
    if x<0:
        print("Its over")
        break
    else:
        print("Good Going")
        continue

#QUESTION5:
for i in range(2000,3201):
    if i%5!=0:
        if i%7==0:
            print(i)

#QUESTION6:
#1  Error: int' object is not iterable

#2) 0
#   error
#   1
#   error
#   2
#   error

#3)  0
#    1
#    2
#    3
#    4

#QUESTION7:
i = 0
while i < 7:
    if i==0:
        print(i)
        i = i+1
    elif i%3!=0:
        print(i)
        i = i+1
    else:
        i = i+1
        continue

#QUESTION8:
s=input("Enter the string")
d={'D':0, 'L':0}
for i in s:
    if i.isalpha():
        d['L']=d['L']+1
    elif i.isdigit():
        d['D']=d['D']+1
    else:
        pass
print(d)
    
#QUESTION9:
#a)
import random
while True:
    y = random.randint(1,10)    
    x = int(input("Enter the lucky no. b/w 1-10"))
    print("lucky no was", y)
    if x==y:
        break
    else:
        continue

print("Lucky no was,", x)

#b)
import random
while True:
    y = random.randint(1,10)    
    x = int(input("Enter the lucky no. b/w 1-10"))
    print("lucky no was", y)
    if x==y:
        print("Do you want to continue? YES/NO")
        number = input("YES/NO")
        if number=='no':
             break
        else:
            continue
    else:
        continue

print("Lucky no was,", x)


#QUESTION10:
counter = 0
import random
while counter<5:
    x=int(input("Enter the lucky no between 1-100"))
    y=random.randint(1,100)
    counter+=1
    if x==y:
        print("Good Guess)")
    else:
        print("Try again!")

print("5 Guess finished")

#QUESTION11:
counter = 0
import random
while counter<5:
    x=int(input("Enter the lucky no between 1-100"))
    y=random.randint(1,100)
    counter+=1
    if x==y:
        print("Good Guess)")
        break
    else:
        print("Try again!")
    print("sorry that was not very successful")

print("5 guess completed")