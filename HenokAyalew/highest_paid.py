#Make a program (highest_paid.py) that asks for the salary of N workers
# (first you must ask how many workers there are) and print the one with the highest salary.

salary = []
n = 0
n = int(input("how many workers: "))

for i in range(0,n):
    salary.append(int(input(f"salary for employee : ")))
    print(salary)
    print ("the highest paid is ",max(salary))