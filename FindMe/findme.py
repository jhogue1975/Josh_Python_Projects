f = open("names.txt")

lines_counter = 0
searchterm = "Josh"
words = f.read()
freqs = words.split()

for names in freqs:
	if searchterm in names:
    		lines_counter += 1
f.close()

lines_string = str(lines_counter)

print "Found the name", searchterm + " " + lines_string + " times"

		
		


	
