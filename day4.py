import re

def cleanup1():
    f = open("text.txt")

    over = 0

    elf1 = []
    elf2 = []


    for i in f:
        elf1 = re.split(r'[,-]', i)[:(len(re.split(r'[,-]', i))//2)]
        elf2 = re.split(r'[,-]', i)[(len(re.split(r'[,-]', i))//2):]
        if int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
            over += 1
        elif int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1]):
            over += 1
        print(elf1, elf2)
        elf1 = []
        elf2 = []
    print(over)

def cleanup2():
    f = open("text.txt")

    over = 0

    elf1 = []
    elf2 = []


    for i in f:
        elf1 = re.split(r'[,-]', i)[:(len(re.split(r'[,-]', i))//2)]
        elf2 = re.split(r'[,-]', i)[(len(re.split(r'[,-]', i))//2):]
        if int(elf1[0]) < int(elf2[0]) and int(elf1[1]) < int(elf2[0]):
            over += 0
        elif int(elf1[0]) > int(elf2[1]):
            over += 0
        elif int(elf2[0]) < int(elf1[0]) and int(elf2[1]) < int(elf1[0]):
            over += 0
        elif int(elf2[0]) > int(elf1[1]):
            over += 0
        else:
            over += 1
        elf1 = []
        elf2 = []
    print(over)
