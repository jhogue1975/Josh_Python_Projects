import random

randomnumber = random.randint(1, 1000)
username = raw_input("What is your name")
counter = 1

print "Hi " + username + " I am thinking of a number between 1 and 1000, let's see how many times it takes you to guess my number"

while randomnumber != userinput:
    if userinput < randomnumber:
        print "The number your chose is too low, try again: "
        count += 1
        userinput = float(raw_input("Nope too low, try again: "))
    else:
        print "that sucks doesnt it"
