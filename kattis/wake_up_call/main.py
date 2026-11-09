import sys

#contains iterable of all lines
inputs = iter(sys.stdin.readlines())

#extract first line, split to create array with entries
first_line = next(inputs).split()


l1 = sum(map(int, next(inputs).split()))
l2 = sum(map(int, next(inputs).split()))

if(l1 > l2):
    sys.stdout.write("Button 1\n")
elif (l2 > l1):
    sys.stdout.write("Button 2\n")
else:
    sys.stdout.write("Oh no\n")

