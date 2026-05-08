import os

with open('text.txt',"r") as f:
    while True:
        chunk=[]
        for _ in range(5):
            line=f.readline()
            if not line:
                break
            chunk.append(line.strip())
        if not chunk:
            print("No more lines to read.")
            break
        print("Processing chunk:", chunk)
    