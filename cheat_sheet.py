import sys

#contains iterable of all lines
inputs = iter(sys.stdin.readlines())

#extract first line, split to create array with entries
first_line = list(map(int, next(inputs).split()))


#iterate over testcases
for _ in range(first_line[0]):

    print(next(inputs))
    
    sys.stdout.write("test\n")
