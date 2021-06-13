# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# 180 124 165 173 189 169 146
#Write your code below this row 👇

ticker = 0
student = 0

for height in student_heights:
    ticker += 1
    student += height

total = student / ticker
print(int(total))