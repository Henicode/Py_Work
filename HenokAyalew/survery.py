'''A survey was carried out to 15 students in a University
where the following information was requested:
- PHOTO ID # (integer value)
- SEX (1 - Male 2 - Female)
- JOB (1 - If you work 2 - Do not work)
- SALARY (float value)
Write a python program (poll.py) that allows reading the values from
the keyboard and then then calculate and print:
- Percentage of men in the university
- Percentage of women in the university
- Percentage of men who work and average salary
- Percentage of working women and average salary'''

student_list = []
gender = "male" or "female"
work = "working" or "not working"
photo_id = int
salary = float


print("-------------------------------")
def enter_score ():
    results = []
    scores = int(input("How many students? : "))
    for i in range(scores):
        gender = (input("eneter gender of student: "))
        work = (input("currently working or not working: "))
        photo_id = (input("photo id number: "))
        salary = (input("yearly salary: "))
        print("------------------")
        results.append(gender)
        results.append(work)
        results.append(photo_id)
        results.append(salary)
        print(results)
    return results

# def calc_average(scores):
#     total = scores
#     for gender in scores:
#         if gender == "male":
#         percent = gender/scores(*100)
#     average= total/float(len(results))
#     print(average)
#     return average
# def above_average():
#   above_average=0
#   for i in range (scores):
#     if results [i] > average:
#         above_average = above_average + 1
#         print(" the above average score is ", above_average)
#     return above_average

# enter_score()
# calc_average()
# above_average()
print("--------------------------------------------")


num = 1
while num < 4:
    gender = (input("eneter gender of student: "))
    work = (input("currently working or not working: "))
    photo_id = (input("photo id number: "))
    salary = (input("yearly salary: "))
    student_list.append(gender)
    num +=1


sex = 0 
for a in student_list:
    if a == "male":
        sex +=1
        print(sex ,"% are the amount of men ")
    elif a == "female":
        sex +=1
        print(sex, "% is the amount of females ")
    else:
        print("done")











# photo_ID = int
# gender = bool
# job = bool
# salary = float

# class Survery():
#     def __init__(self, photo_ID, gender, job, salary):
#         self.photo_ID = photo_ID
#         self.gender = gender
#         self.job = job
#         self.salary = salary
#         pass


#     def questions():
#         print(input("photo id: "))
#         print(input("gender : "))
#         print(input("job : "))
#         print(input("salary : "))

#     print(questions(*3))
    