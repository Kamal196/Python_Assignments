#QUESTION1:
x=[1, 2, 3, 3.5, 5.6, 7, 10+7j, "kamal", "abc", 34]
print(len(x))

#QUESTION2:
x=[1, 2, 3, 4, 5]
print(x[:])
print(x[:4])
print(x[1:])
print(x[::2])

#QUESTION3:
sum = 0
multiply=1
x=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(x)):
    sum+=x[i]
    multiply=multiply*x[i]

print(sum)
print(multiply)

#QUESTION4:
x=[1,2,4,5,67,8,90,1,55,0]
print(max(x))
print(min(x))

#QUESTION5:
x=[1,2,4,5,6,7,8,9,4,32,56,7,8,9,4,32,6,89,5,3,2]
y=[]
for i in range(len(x)):
    if x[i]%2!=0:
        y.append(x[i])
    else:
        pass

print(y)

#QUESTION6:
x=[]
for i in range(1,31):
    if i>=1 and i<=5:
        i=i*i
        x.append(i)
    if i>25 and i<=30:
        i=i*i
        x.append(i)

print(x)

#QUESTION7:
x=[[1,3,5,7,9,10],[2,4,6,8]]
x[0][5:]=x[1]
print(x[0])

#QUESTION8;
a={1:10, 2:20}
b={3:30, 4:40}
a.update(b)
print(a)

#QUESTION9:
x={}
for i in range(1,6):
    x[i]=i*i

print(x)

#QUESTION10:
x=input("enter the no:")
print(x)
list1=x.split(" ")
print(list1)
print(tuple(list1))

#QUESTION11 AND QUESTION12 = QUESTION1 AND QUESTION2

#QUESTION13:
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[5][:4])
print(x[6:8])
print(x[::-1])
print(x[5][5][0])

#QUESTION14:
#In python 3 VERSION 'Xrange' doesnt exit. 
#xrange in python2 returns xrange object and not a list of objects.

x=range(1,1001)
for i in x:
    print(i)

#QUESTION15:
#When we dont want data values to get changed(immutable) then  tuple is imp than list. 
#For eg: Customer ID at amazon is fixed from one login credentials. Then its good to use tuple as its not changing.
#Whereas ProductID customer is ordering changes everytime so its good to use list at that time.

#QUESTION16:
for i in range(1,101):
    if i%2==0 and i%3==0:
        print(i)

#QUESTION17:
x="consulntadd123"
y=x[::-1]
print(y)
for i in y:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        print(i,y.index(i))

#QUESTION18:
x='hello my name is abcde'
even=[]
y=x.split(" ")
for i in y:
    z=len(i)
    if z%2==0:
         even.append(i)
res = " ".join(even)
print(res)

#QUESTION19:
x=[1,2,3,4,5,6,7,8,9,-1]
y=[]
for i in x:
    for j in x:
        if i+j==8:
            print(i,j)
            
#question20:
even_list=[]
odd_list=[]
while True:
    number=int(input("enter the no in range of 1-50"))
    if number%2==0:
        even_list.append(number)
        if len(even_list)==5:
            break
    else:
        odd_list.append(number)
        if len(odd_list)==5:
            break

    
print(even_list)
print("Sum of even list is", sum(even_list))
print("Max o list is", max(even_list))

print(odd_list)
print("Sume of odd list is", sum(odd_list))
print("Max o list is", max(odd_list))

#QUESTION21:
x="2abcbacbaba344ab"
d={}
for i in x:
    if i.isalpha():
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    else:
        pass

print(d)

#QUESTION22:
x= (1,2,3,4,5,6,7,8,9,10)
y=[]
for i in x:
    if i%2==0:
        y.append(i)

z=tuple(y)
print(z)








