import sys

#contains iterable of all lines
inputs = iter(sys.stdin.readlines())

#extract first line, split to create array with entries
first_line = list(map(int, next(inputs).split()))

playerwins = []
player = 0

#iterate over testcases
for i in range(first_line[0]):

    results = list(next(inputs))

    match_counter = 0
    sum_win = 0
    sum_losses = 0

    for num in results:

        match_counter += 1
        
        if(num == "W"):
            sum_win += 1
        else:
            sum_losses += 1

        if(sum_losses == 3):
            sum_losses = 0
            sum_win = 0

        
    playerwins[player] = match_counter
    player += 1

print(playerwins)


#sys.stdout.write("test\n")
