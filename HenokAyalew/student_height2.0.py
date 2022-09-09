height_list = []

num = 1
while num < 11:
    height = float(input(f"Enter student {num} height in cm: "))
    height_list.append(height)
    num += 1

print(*height_list)

heightSum = sum(height_list)
heightAverage = heightSum / num
print("average of student height is", heightAverage)

aboveAverage = 0
for a in height_list:
    if a > heightAverage:
        aboveAverage +=1
print(aboveAverage, "are the number of students that are above average height")


belowaverage = 0
for b in height_list:
    if b < heightAverage:
        belowaverage += 1
print(belowaverage, "are the number of students that are below average height")