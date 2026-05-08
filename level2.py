import os
with open('student.txt',"r") as f:
    for line in f:
        parts=line.strip().split(":")
        print(parts)

"""STRUCTURED DATA"""

with open('student.txt',"r") as f:
   structured_data=[]
   for line in f:
       a=line.strip().split(':')
       b=a[0].strip().split("-")
       structured_data.append({"name":b[0].strip(),"marks":int(a[1])})
print(structured_data)

"""AVERAGE MARKS"""
total_marks=0
for student in structured_data:
    total_marks+=(student['marks'])
average_marks=total_marks/len(structured_data)
print(f"Average marks: {average_marks}")


from collections import defaultdict
ranges=[(0,50),(51,70),(71,80),(81,90),(91,100)]
data=defaultdict(int)

for student in structured_data:
    for start,end in ranges:
       if start<=student['marks']<=end:
           data[f"{start}-{end}"]+=1
print(dict(data))

for student in structured_data:
    



