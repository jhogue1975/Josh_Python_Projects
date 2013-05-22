import argparse, sys

parser = argparse.ArgumentParser(description='This script sorts lines by the first letter of each line in desending order .')
parser.add_argument("fileName")
parser.parse_args()

###############################################################

f = open(sys.argv[1])
wordlines = f.readlines()
f.close

###############################################################

f = open('out.txt','a')
sortedlines = sorted(wordlines, key=str.lower)
for lines in sortedlines:
    f.write(lines)
    print lines
f.close

###############################################################






		
		


	