# Get input for rows and columns
rows = int(input())
cols = int(input())

for i in range(rows):
    line = ""
    for j in range(cols):
        line += "*"
    print(line)
