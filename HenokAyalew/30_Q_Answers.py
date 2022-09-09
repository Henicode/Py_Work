#8 - Write a program in Python that prints the numbers 1 to 3 on the screen.

for a in range(1,4):
    print(a)
print("xxxxxxxNUM_8xxxxxxxxx")

#9 - Write a program in Python that prints the numbers 1 to 9 on the screen.

for a in range(1,10):
    print(a)
print("xxxxxxxNUM_9xxxxxxxxx")

#10 - Write a program in Python that prints on the screen the numbers from 1 to 10,000.

'''for a in range(1,10001):
    print(a)'''
print("xxxxxxxNUM_10xxxxxxxxx")

#11 - Write a program in Python that prints the numbers from 5 to 10 on the screen.

for a in range(5,11):
    print(a)
print("xxxxxxxNUM_11xxxxxxxxx")

#12 - Write a program in Python that prints the numbers from 5 to 15 on the screen.

for a in range(5,16):
    print(a)
print("xxxxxxxNUM_12xxxxxxxxx")
#13 - Write a program in Python that prints on the screen the numbers from 5 to 15,000.

'''for a in range(5,15001):
    print(a)'''
print("xxxxxxxNUM_13xxxxxxxxx")

#14 - Write a program in Python that prints 200 times the word "hello". Note: in the source code that you write you must only enter once the word "hello".

'''print("Hello" * 4)'''

str = "Hello"
for a in range(200):
    print(str)
print("xxxxxxxNUM_14xxxxxxxxx")

#15 - Write a program in Python that prints the squares of the first 30 natural numbers on the screen.

for a in range(31):
    print(a **2)
print("xxxxxxxNUM_15xxxxxxxxx")

#16 - Write a program in Python that reads an integer from the keyboard and makes the sum of the next 100 numbers, showing the result on screen.

<<<<<<< HEAD
n1 = int(input("Enter number:\n "))
=======
i=2
j=i+1
n=100

sum=n*(j+i+n)/2
print(sum)
xxxxxxxxxxxxxxxxxxxxxxx
n1 = int(input("enter number: "))
>>>>>>> ae69012d8e09b47a6f1d42bb6262c95c415572a7
for x in range(n1 + 1 ,n1+102):
    print('sum of the next 100 numbers', x)
print("xxxxxxxNEXTLINExxxxxxxxx")

#17 - Write a program in Python that converts from canadian dollars to US dollars. You will receive a decimal number corresponding to the amount in CAD and will answer with the corresponding amount in US dollars. Take the quotation of the dollar today.

x = int (input("Canadian $$ ??: \n "))
calc = x * 1.21

print(calc , "in USD")
print("xxxxxxxNUM_17xxxxxxxxx")

#18 - Write a program in Python that reads two numbers on the keyboard and say which is the largest and which is the smallest.

x = int(input("Pick a Number:\n "))
y = int(input("Pick a Number:\n "))

if x > y:
    print(f'{x} is largest,{y} is the smallest')
elif x < y:
    print(f'{y} is the largest,{x} is the smallet')
elif x == y:
    print("they are equal")
else:
    print("done")

print("xxxxxxxNUM_18xxxxxxxxx")

#19 - Write a Python program that does the following: declare a variable N of type int, a variable A of type double and a variable C of type char and assign to each one a value. The following screen displays:
#The value of each variable. The sum of N + A. And A - N

<<<<<<< HEAD
print ("xxxxxxxNUM_19xxxxxxxxx")
N = int(input("Enter an integer: "))
A = float(input("Enter an float: "))
C = str(input("Enter a string: "))

print ("int + float",N + A)
print ("float - float",N - A)
=======

N = int(input("Enter an integer: "))
A = float(input("Enter an float: "))
C = str(input("Enter a string: "))
>>>>>>> ae69012d8e09b47a6f1d42bb6262c95c415572a7

print ("int + float",N + A)
print ("float - float",N - A)


print ("xxxxxxxNUM_19xxxxxxxxx")

#20 - Write a Python program that declares an integer variable B and assign it a value. It then displays a message indicating whether the value of B is positive or negative. We will consider 0 as positive.
#If for example B = 1 the output will be 1 is positive. If for example B = -1 the output will be: -1 is negative.

b = int(input("Number:\n "))

if b < 0:
    print("Your number is negative")
elif b >= 0:
    print("Your number is positive")
else:
    print("done")

print("xxxxxxxNum_20xxxxxxxxx")

#21 - Make a program in Python such that given as data the enrolment and 5 grades of a student; Print the enrolment, the average and the word "approved" if the student has an average greater than or equal to 6, and the word "not approved" otherwise. Data: MAT, CAL1, CAL2, CAL3, CAL4, CAL5 Where: MAT is an integer variable that represents the student's enrolment. CAL1, CAL2, CAL3, CAL4 and CAL5 are real-type variables representing the student's 5 grades.


#22 - Make the program in Python such that given as a worker's salary, apply a 15% increase if your salary is less than $ 1000 and 12% otherwise. Print the new salary of the worker. Fact: SUE (variable of real type that represents the salary of the worker).
#23 - Make a program that prints the 10 multiplication tables.

for a in range(11):
    print(a * 10)
print("xxxxxxxNum_23xxxxxxxxx")

#24 - Make a calculator.

num1 = float(input("Enter the first number:\n "))
num2 = float(input("Enter the second number:\n "))

print("Enter the operation you would like to perform")

A = input("+ , - ,* , / : ")

if A == "+":
    result = num1 + num2
elif A == "-":
    result = num1 - num2
elif A == "*":
    result = num1 * num2
elif A == "/":
    result = num1 / num2
else:
    print("value not readable")

print(num1, A, num2, ":", result)

print("xxxxxxxNum_24xxxxxxxxx")


#25 - Calculate the salary increase for a group of employees of a company considering the following criteria: If the salary is less than $ 1,000.00: Increase 15% If the salary is greater than or equal to $ 1,000.00: Increase 12% The program must do The following: - Save the new salaries in the arrangement - Calculate the payroll - Print the salaries from the settlement
#26 - Make a program that asks for the salary of N workers (first you must ask how many workers there are) and print the one with the highest salary.
#27 - Write an algorithm that calls another, and the call prints a value.
#28 - Write an algorithm that calls another name "add", which receives 2 numbers. The summation algorithm must add its parameters. The algorithm you invoke must receive that value and display it on the screen.
#29 - Write an algorithm and a sub-algorithm. Write two variables with the same name and the compiler does not show error.
#30 - Write a program that asks for a numerical password and allows three attempts. If the user enters the correct password, it shows "Correct!" And run any program, after the message. Otherwise the program should display "Wrong password". Then finish the program immediately.
