#A = enemy_rock
#B = enemy_paper
#C = enemy_scissors

#X = my_rock
#Y = my_paper
#Z = my_scissor

#SCORES: +1 rock, +2 paper, +3 scissor
#        +0 loss, +3 tie, +6 win

#QUESTION 2
#X = loss ; Y = draw ; Z = loss

points = 0
f = open("text.txt")
for i in f:
    if i[2] == "X":
        points += 1
        if i[0] == "A":
            points += 3
        if i[0] == "C":
            points += 6
    if i[2] == "Y":
        points += 2
        if i[0] == "A":
            points += 6
        if i[0] == "B":
            points += 3
    if i[2] == "Z":
        points += 3
        if i[0] == "B":
            points += 6
        if i[0] == "C":
            points += 3


#A = enemy_rock
#B = enemy_paper
#C = enemy_scissors

#X = my_rock
#Y = my_paper
#Z = my_scissor

#SCORES: +1 rock, +2 paper, +3 scissor
#        +0 loss, +3 tie, +6 win

#QUESTION 2
#X = loss ; Y = draw ; Z = win

points = 0
f = open("text.txt")
for i in f:
    if i[0] == "A":
        if i[2] == "X":
            points += 3
        if i[2] == "Y":
            points += 4
        if i[2] == "Z":
            points += 8
    if i[0] == "B":
        if i[2] == "X":
            points += 1
        if i[2] == "Y":
            points += 5
        if i[2] == "Z":
            points += 9
    if i[0] == "C":
        if i[2] == "X":
            points += 2
        if i[2] == "Y":
            points += 6
        if i[2] == "Z":
            points += 7

