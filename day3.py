import string
# len//2
def total1():
    f = open("text.txt")

    half1 = []
    half2 = []

    alf = list(string.ascii_lowercase)
    ALF = list(string.ascii_uppercase)

    total = 0

    group = 3

    for i in f:
        x = 0
        while x < len(i)//2:
            half1.append(i[x])
            x += 1
        y = len(i)//2
        while y < len(i):
            half2.append(i[y])
            y += 1
        inter = list(set(half1).intersection(half2))
        if inter[0] >= 'a' and inter[0] <= 'z':
            total += alf.index(inter[0]) + 1
        if inter[0] >= 'A' and inter[0] <= 'Z':
            total += ALF.index(inter[0]) + 1 + 26
        half1 = []
        half2 = []
    print(total)


def total2():
    elf1 = []
    elf2 = []
    elf3 = []
    alf = list(string.ascii_lowercase)
    ALF = list(string.ascii_uppercase)

    total = 0
    elf = 3

    f = open("text.txt")

    for i in f:
        if elf == 0:
            inter1 = list(set(elf1).intersection(elf2))
            inter = list(set(inter1).intersection(elf3))
            inter.remove('\n')
            if inter[0] >= 'a' and inter[0] <= 'z':
                total += alf.index(inter[0]) + 1
            if inter[0] >= 'A' and inter[0] <= 'Z':
                total += ALF.index(inter[0]) + 1 + 26
            elf1 = []
            elf2 = []
            elf3 = []
            elf = 3
        if elf != 0:
            if elf == 3:
                elf1 = i
            if elf == 2:
                elf2 = i
            if elf == 1:
                elf3 = i
        elf -= 1
    inter1 = list(set(elf1).intersection(elf2))
    inter = list(set(inter1).intersection(elf3))
    if inter[0] >= 'a' and inter[0] <= 'z':
        total += alf.index(inter[0]) + 1
    if inter[0] >= 'A' and inter[0] <= 'Z':
        total += ALF.index(inter[0]) + 1 + 26
    print(total)
