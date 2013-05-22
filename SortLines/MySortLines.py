f = open('Lines.txt')
lines = f.readlines()
f.close()

f = open('SortedLines.txt', 'w')
sorted_lines = sorted(lines,  key=str.lower)

for i in sorted_lines:
    f.write(i)
f.close()
