name = 'Joshua I. Hogue'
age = 38 # not a lie
height = 71 # inches
weight = 200 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Blonde'
truck = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "And %s drives a %s truck." % (name, truck)

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)