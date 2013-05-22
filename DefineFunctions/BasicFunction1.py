############################################################
# Function with String
############################################################
def printme( str ):
   "This prints a passed string into this function"
   print str
   return

# Now you can call printme function
printme("I'm the first call to user defined function!")
printme("And the second call to the same function")

############################################################
# Function with Integer
############################################################
def printmeagain( int ):
    "This prints a passed integer into this function"
    print int
    return

# Now you can call printmeagain function
printmeagain(15)
printmeagain(10+15*3)


############################################################
# Here we are maintaining reference of the passed object and appending values in the same object.
# So this would produce following result
############################################################
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4])
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print "Values outside the function: ", mylist


############################################################
# The parameter mylist is local to the function changeme. Changing mylist within the function does not affect mylist.
# The function accomplishes nothing and finally this would produce the following result
############################################################
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4] # This would assign new reference in mylist
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print "Values outside the function: ", mylist


############################################################




