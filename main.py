# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# Note:Replicating the (sum function),in loop instead of using this:👇 
# total_height = sum(student_heights)
# print(total_height)
  
# Use this instead:👇 
total_height = 0
for height in student_heights:
  total_height += 0 + height
print(total_height)
  
# Note: Replicating the (len) function in (for loop) so, instead of using this:  
# Number_of_students = len(student_heights )
# print(Number_of_students)

# Use this instead;👇
Number_of_students = 0
for height in student_heights:
  Number_of_students += 1
print(Number_of_students)

average_height = (total_height / Number_of_students)
print(round(average_height))