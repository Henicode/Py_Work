#Write a program that allows you to enter the height of 10 students,
# then show the average height, and how many elements are above average,
# how many are below average.

# class Average():
#     pass
stud_1 =(float(input("students height in cm: ")))
stud_2 =(float(input("students height in cm: ")))
stud_3 =(float(input("students height in cm: ")))
stud_4 =(float(input("students height in cm: ")))
stud_5 =(float(input("students height in cm: ")))
stud_6 =(float(input("students height in cm: ")))
stud_7 =(float(input("students height in cm: ")))
stud_8 =(float(input("students height in cm: ")))
stud_9 =(float(input("students height in cm: ")))
stud_10 =(float(input("students height in cm: ")))

students = [stud_1, stud_2, stud_3, stud_4, stud_5, stud_6, stud_7, stud_8, stud_9, stud_10]
total_height = stud_1+stud_2+stud_3+stud_4+stud_5+stud_6+stud_7+stud_8+stud_9+stud_10
num_students = 10
average_height = float()

average_height = total_height/num_students
print("============================================")
print("===average height of students is: ",average_height,"cm===")
print("============================================")

if stud_1 < average_height:
    print("student 1 is BELOW average height")
elif stud_1 == average_height:
    print("Student 1 is the same as average height")
else:
    print("student 1 is ABOVE average height")

print("-------------------------")

if stud_2 < average_height:
    print("student 2 is BELOW average height")
elif stud_2 == average_height:
    print("Student 2 is the same as average height")
else:
    print("student 2 is ABOVE average height")

print("-------------------------")

if stud_3 < average_height:
    print("student 3 is BELOW average height")
elif stud_3 == average_height:
    print("Student 3 is the same as average height")
else:
    print("student 3 is ABOVE average height")

print("-------------------------")

if stud_4 < average_height:
    print("student 4 is BELOW average height")
elif stud_4 == average_height:
    print("Student 4 is the same as average height")
else:
    print("student 4 is ABOVE average height")

print("-------------------------")

if stud_5 < average_height:
    print("student 5 is BELOW average height")
elif stud_5 == average_height:
    print("Student51 is the same as average height")
else:
    print("student 5 is ABOVE average height")

print("-------------------------")

if stud_6 < average_height:
    print("student 6 is BELOW average height")
elif stud_6 == average_height:
    print("Student 6 is the same as average height")
else:
    print("student 6 is ABOVE average height")

print("-------------------------")

if stud_7 < average_height:
    print("student 7 is BELOW average height")
elif stud_7 == average_height:
    print("Student 7 is the same as average height")
else:
    print("student 7 is ABOVE average height")

print("-------------------------")

if stud_8 < average_height:
    print("student 8 is BELOW average height")
elif stud_8 == average_height:
    print("Student 8 is the same as average height")
else:
    print("student 8 is ABOVE average height")

print("-------------------------")

if stud_9 < average_height:
    print("student 9 is BELOW average height")
elif stud_9 == average_height:
    print("Student 9 is the same as average height")
else:
    print("student 9 is ABOVE average height")

print("-------------------------")

if stud_10 < average_height:
    print("student 10 is BELOW average height")
elif stud_10 == average_height:
    print("Student 10 is the same as average height")
else:
    print("student 10 is ABOVE average height")

print("-------------------------")

    