###############################################
# find a string
###############################################
def findstr(line,word):
    strlen = len(line)-len(word)+1
    found = -1
    for i in range(0,strlen):
        stra = line[i:i+len(word)]
        if stra==word:
            found = i
            break
    return found;

###############################################
# delete a
###############################################
def deletechar(line,n,length):
    sstart = line[:n]
    send = line[n+length:len(line)]
    newstr = sstart + send
    return newstr;


###############################################
# strip a word from a string
###############################################
def fixhappy(line,word):
    lowcase = line.lower()
    hadhappy = False
    n=1
    while n>-1:
        n = findstr(lowcase,word)
        if n>-1:
            line = deletechar(line,n,len(word))
            lowcase = line.lower()
            hadhappy = True
    if hadhappy:
        return line;
    else:
        return "";

###############################################
# sum numbers, skip digits next to non digits
###############################################
def sumnumbers(line):
    numsum = []
    for word in line.split():
        if word.isdigit():                             #gets multiple digit int
            numsum.append(word)                   #adds ints to list


    return numsum

def jamiesum(anum):
    x = 0
    for i in anum:
        x = x+int(i)
    return x;

###############################################
# Do some work, call some functions
###############################################
line="this code makes me ... y"
lowerline = line.lower()
happyClearedLine = fixhappy(line,"happy")
numarray = sumnumbers(line)
if len(numarray)>0:
    print  "+".join(numarray)+"="+str(jamiesum(numarray))
elif len(happyClearedLine) >0:
    print happyClearedLine
else:
    print line[::-1]