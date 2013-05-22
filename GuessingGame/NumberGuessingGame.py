import random

username = raw_input("What is your name: ")

count = 1
randomnumber = random.randint(1, 100)

print " Hi " + username + ", I am thinking of a number between 1 and 100, can you guess what it is?"

userinput = int(raw_input("Take a Guess: "))
while randomnumber != userinput:
    if userinput < randomnumber:
        count = count + 1
        userinput = float(raw_input("Nope too low, try again: "))
    else:
        userinput > randomnumber
        count = count + 1
        userinput = float(raw_input("Nope too high, try again: "))

print "Congratulations you did it! And it only took you " + str(count) + " guesses"
