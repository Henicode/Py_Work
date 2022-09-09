

#students = []
#question_rep = range(1,3)


def enter_score ():
    results = []
    scores = int(input("How many students? : "))
    gender = "male" or "female"
    work = "working" or "not working"
    salary = float
    photo_id = int
    for i in range(scores):
        gender = (input("eneter gender of student: "))
        work = (input("currently working or not working: "))
        photo_id = (input("photo id number: "))
        salary = (input("yearly salary: "))
        results.append(gender)
        results.append(work)
        results.append(photo_id)
        results.append(salary)
        print(results)
    return results

def percent_of_students():
    total = 0    total=total+student_score
    average= total/scores
    print("the average is ", average)
    return
def above_average():
  above_average=0
  for i in range (scores):
    if results [i] > average:
        above_average = above_average + 1
        print(" the above average score is ", above_average)
    return above_average

enter_score()
#calc_average()
above_average()
