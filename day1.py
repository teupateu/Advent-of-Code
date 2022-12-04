def calories():
    f = open("text.txt")
    maxtotal = 0
    max = 0
    top = [0, 0, 0]
    x = 3
    elf = 2
    while elf >= 0:
        for i in f:
            if i != '\n':
                max = max + int(i)
            if i == '\n':
                if max > maxtotal and elf == 2:
                    maxtotal = max
                if elf < 2 and max > maxtotal and max < top[elf + 1]:
                    maxtotal = max
                max = 0
        top[elf] = maxtotal
        elf = elf - 1
        maxtotal = 0
        max = 0
        i = 0
    print(top)

    while x!=0:
        if x == 3:
            for i in f:
                print(i + str(x))
        x-=1
        i = 0
        j = 0
        if x == 2:
            for j in f:
                print(i + str(x))


def calorie():
    f = open("text.txt")
    maxcurrent = 0
    max1 = 0
    max2 = -1
    max3 = -2

    for i in f:
        if i != '\n':
            maxcurrent = maxcurrent + int(i)
        if i == '\n':
            if maxcurrent > max1:
                aux = max2
                max3 = max2
                max2 = max1
                max1 = maxcurrent
            elif maxcurrent > max2:
                aux = max2
                max3 = max2
                max2 = maxcurrent
            elif maxcurrent > max3:
                max3 = maxcurrent
            maxcurrent = 0
    maxtotal = max1 + max2 + max3

    print(maxtotal)
