import os
import random
marks=[80,83,67,98,78,89,92,84,87]
# with open('student.txt',"a") as f:
#    for i in range(11,16):
#      f.write(f"Student {i} - Marks:{random.choice(marks)}\n")
# print('done')

with open('student.txt',"r") as f:
    count=0
    for line in f:
        count+=1
    print(f"Total number of students: {count}")   

with open('student.txt',"r") as f:
    marks=0
    student=''
    for line in f:
        a=int(line.strip().split(":")[-1])
        if a>marks:
            marks=a
            student=line.strip()
    print(f"Highest marks: {marks}")
    print(f"Student with highest marks: {student}")


with open('student.txt',"r") as f:
    marks=80
    for line in f:
        a=int(line.strip().split(":")[-1])
        if a>marks:
            print(line.strip())

with open('top_students.txt',"w") as f:
    for line in open('student.txt',"r"):
        a=int(line.strip().split(":")[-1])
        if a>85:
            f.write(line)