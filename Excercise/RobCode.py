fileopen = open('Excercise3.txt')
linebuild = []                                         
for line in fileopen:               #open file
    linebuild.append(line)          #put lines into list
fileopen.close()                    #close file, so it's not open the whole time the script is running, duh
for line in linebuild:
    lowerline = line.lower()                           #Get lines and create base variables
    numsum = []
    totalz = ""
    numbuild = ""
    reverser = ""
    removehappy = []
    for word in line.split():                           #split string to words
            if word.lower() != "happy":                 #if the word isn't happy
                removehappy.append(word)                #re-add the word to new list
                for char in word:                       #while we're here, let's look at characters
                    reverser = char + reverser          #build reverse string just in case
                    if char.isdigit():                         #pulls ints from strings
                        numbuild = numbuild + str(char)        #adds ints to string 
                    elif numbuild != "":
                        numsum.append(int(numbuild))           #after number is built, add to list
                        numbuild = ""
            reverser = " " + reverser                          #add spaces between words for reverse string
            if numbuild != "":                                 #quick check if number was at the end of the string
                numsum.append(int(numbuild))
                numbuild = ""
    removehappy = " ".join(removehappy).strip()                #put line back together with no 'happy'
    print "ORIGINAL LINE: " + str(line.strip())                #show original line
    if  removehappy.lower() != lowerline.strip():              #was there a "happy"?
        print "Happy Removed: " + removehappy                      #build output string
    else:
        print "This line did not contain the word 'happy'"            
    if len(numsum) > 0:                                                      #were there numbers?
            for item in numsum:                                              #build output string                                    
                totalz = totalz + str(item) + " + "                          #add numbers to output string
            print "Adding Numbers: " + totalz[:(len(totalz)-2)] + "= " + str(sum(numsum))      #clean up string and add sum
    elif removehappy.lower() == lowerline.strip():                           #no numbers and no happy 
        print "This line did not include numbers either......"               #tell em why
        print "REVERSED:" + reverser                                        #print reversed string
    print


