with open('text.txt',"a") as f:
    for i in range(1,101):
        f.write(f"\nLine {i}: This is sample log data")