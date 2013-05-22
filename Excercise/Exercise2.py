


base = wordlist[0]                      #consider the first word in the list
for word in wordlist:                 #loop through the entire list checking if
    if not word.startswith(base):     # the word we're considering starts with the base
        print base                    #If not... we have a new base, print the current
        base = word                     #  one and move to this new one
    #else word starts with base
        #don't output word, and go on to the next item in the list
print base                            #finish by printing the last base