def printme( str ):
   "This prints a passed string into this function"
   print str
   return

printme("I'm firt call to set difinted function!")
printme("Again second call to the same function")

def foo():
    print "hello from inside of foo"
    return 1

name = ""
main = ""
if name == main:
    print "going to call foo"
    x = foo()
    print "called foo"
    print "foo returned " + str(x)

def foo():
    print "hello from within foo"
    return 1

foo()

def bar():
  return 10 * foo()
bar()
