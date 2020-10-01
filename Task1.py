#QUESTION1:

x,y,z = 10, 20.5 , "kamal"
print(type(x))
print(type(y))
print(type(z))

#QUESTION2:

a = 10 +20j
print(type(a))
b = 100
print(type(b))
a = b
print(a)

#QUESTION3:

#USING VARIABLE 'RESULT'
a =10
b = 20
result = a
a = b
b = result
print(a,b)

#WITHOUT USING VARIABLE
a,b = b,a
print(a,b)

#QUESTION4:
enter_value = input("enter the value 3.x")
# enter_value = raw_input("enter the value 2.x")

#QUESTION5:
x = int(input("Enter the first no."))
y = int(input("enetr the second no."))
z = x+y
z = z+30
print(z)

#QUESTION6:
x = eval(input("enter the value"))
print(type(x))