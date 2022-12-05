import re

def stacks1():

    stack1 = ['F', 'G', 'V', 'R', 'J', 'L', 'D']
    stack2 = ['S', 'J', 'H', 'V', 'B', 'M', 'P', 'T']
    stack3 = ['C', 'P', 'G', 'D', 'F', 'M', 'H', 'V']
    stack4 = ['Q', 'G', 'N', 'P', 'D', 'M']
    stack5 = ['F', 'N', 'H', 'L', 'J']
    stack6 = ['Z', 'T', 'G', 'D', 'Q', 'V', 'F', 'N']
    stack7 = ['L', 'B', 'D', 'F']
    stack8 = ['N', 'D', 'V', 'S', 'B', 'J', 'M']
    stack9 = ['D', 'L', 'G']

    stack1.reverse()
    stack2.reverse()
    stack3.reverse()
    stack4.reverse()
    stack5.reverse()
    stack6.reverse()
    stack7.reverse()
    stack8.reverse()
    stack9.reverse()

    f = open("text.txt")

    for i in f:
        instruction = i.split(' ')
        boxes = int(instruction[1])
        source = int(instruction[3])
        dest = int(instruction[5])
        while boxes != 0:
            if source == 1:
                if dest == 2:
                    stack2.append(stack1[len(stack1) - 1])
                    stack1.pop()
                elif dest == 3:
                    stack3.append(stack1[len(stack1) - 1])
                    stack1.pop()
                elif dest == 4:
                    stack4.append(stack1[len(stack1) - 1])
                    stack1.pop()
                elif dest == 5:
                    stack5.append(stack1[len(stack1) - 1])
                    stack1.pop()
                elif dest == 6:
                    stack6.append(stack1[len(stack1) - 1])
                    stack1.pop()
                elif dest == 7:
                    stack7.append(stack1[len(stack1) - 1])
                    stack1.pop()
                elif dest == 8:
                    stack8.append(stack1[len(stack1) - 1])
                    stack1.pop()
                else:
                    stack9.append(stack1[len(stack1) - 1])
                    stack1.pop()
            if source == 2:
                if dest == 1:
                    stack1.append(stack2[len(stack2) - 1])
                    stack2.pop()
                elif dest == 3:
                    stack3.append(stack2[len(stack2) - 1])
                    stack2.pop()
                elif dest == 4:
                    stack4.append(stack2[len(stack2) - 1])
                    stack2.pop()
                elif dest == 5:
                    stack5.append(stack2[len(stack2) - 1])
                    stack2.pop()
                elif dest == 6:
                    stack6.append(stack2[len(stack2) - 1])
                    stack2.pop()
                elif dest == 7:
                    stack7.append(stack2[len(stack2) - 1])
                    stack2.pop()
                elif dest == 8:
                    stack8.append(stack2[len(stack2) - 1])
                    stack2.pop()
                else:
                    stack9.append(stack2[len(stack2) - 1])
                    stack2.pop()
            if source == 3:
                if dest == 1:
                    stack1.append(stack3[len(stack3) - 1])
                    stack3.pop()
                elif dest == 2:
                    stack2.append(stack3[len(stack3) - 1])
                    stack3.pop()
                elif dest == 4:
                    stack4.append(stack3[len(stack3) - 1])
                    stack3.pop()
                elif dest == 5:
                    stack5.append(stack3[len(stack3) - 1])
                    stack3.pop()
                elif dest == 6:
                    stack6.append(stack3[len(stack3) - 1])
                    stack3.pop()
                elif dest == 7:
                    stack7.append(stack3[len(stack3) - 1])
                    stack3.pop()
                elif dest == 8:
                    stack8.append(stack3[len(stack3) - 1])
                    stack3.pop()
                else:
                    stack9.append(stack3[len(stack3) - 1])
                    stack3.pop()
            if source == 4:
                if dest == 1:
                    stack1.append(stack4[len(stack4) - 1])
                    stack4.pop()
                elif dest == 2:
                    stack2.append(stack4[len(stack4) - 1])
                    stack4.pop()
                elif dest == 3:
                    stack3.append(stack4[len(stack4) - 1])
                    stack4.pop()
                elif dest == 5:
                    stack5.append(stack4[len(stack4) - 1])
                    stack4.pop()
                elif dest == 6:
                    stack6.append(stack4[len(stack4) - 1])
                    stack4.pop()
                elif dest == 7:
                    stack7.append(stack4[len(stack4) - 1])
                    stack4.pop()
                elif dest == 8:
                    stack8.append(stack4[len(stack4) - 1])
                    stack4.pop()
                else:
                    stack9.append(stack4[len(stack4) - 1])
                    stack4.pop()
            if source == 5:
                if dest == 1:
                    stack1.append(stack5[len(stack5) - 1])
                    stack5.pop()
                elif dest == 2:
                    stack2.append(stack5[len(stack5) - 1])
                    stack5.pop()
                elif dest == 3:
                    stack3.append(stack5[len(stack5) - 1])
                    stack5.pop()
                elif dest == 4:
                    stack4.append(stack5[len(stack5) - 1])
                    stack5.pop()
                elif dest == 6:
                    stack6.append(stack5[len(stack5) - 1])
                    stack5.pop()
                elif dest == 7:
                    stack7.append(stack5[len(stack5) - 1])
                    stack5.pop()
                elif dest == 8:
                    stack8.append(stack5[len(stack5) - 1])
                    stack5.pop()
                else:
                    stack9.append(stack5[len(stack5) - 1])
                    stack5.pop()
            if source == 6:
                if dest == 1:
                    stack1.append(stack6[len(stack6) - 1])
                    stack6.pop()
                elif dest == 2:
                    stack2.append(stack6[len(stack6) - 1])
                    stack6.pop()
                elif dest == 3:
                    stack3.append(stack6[len(stack6) - 1])
                    stack6.pop()
                elif dest == 4:
                    stack4.append(stack6[len(stack6) - 1])
                    stack6.pop()
                elif dest == 5:
                    stack5.append(stack6[len(stack6) - 1])
                    stack6.pop()
                elif dest == 7:
                    stack7.append(stack6[len(stack6) - 1])
                    stack6.pop()
                elif dest == 8:
                    stack8.append(stack6[len(stack6) - 1])
                    stack6.pop()
                else:
                    stack9.append(stack6[len(stack6) - 1])
                    stack6.pop()
            if source == 7:
                if dest == 1:
                    stack1.append(stack7[len(stack7) - 1])
                    stack7.pop()
                elif dest == 2:
                    stack2.append(stack7[len(stack7) - 1])
                    stack7.pop()
                elif dest == 3:
                    stack3.append(stack7[len(stack7) - 1])
                    stack7.pop()
                elif dest == 4:
                    stack4.append(stack7[len(stack7) - 1])
                    stack7.pop()
                elif dest == 5:
                    stack5.append(stack7[len(stack7) - 1])
                    stack7.pop()
                elif dest == 6:
                    stack6.append(stack7[len(stack7) - 1])
                    stack7.pop()
                elif dest == 8:
                    stack8.append(stack7[len(stack7) - 1])
                    stack7.pop()
                else:
                    stack9.append(stack7[len(stack7) - 1])
                    stack7.pop()
            if source == 8:
                if dest == 1:
                    stack1.append(stack8[len(stack8) - 1])
                    stack8.pop()
                elif dest == 2:
                    stack2.append(stack8[len(stack8) - 1])
                    stack8.pop()
                elif dest == 3:
                    stack3.append(stack8[len(stack8) - 1])
                    stack8.pop()
                elif dest == 4:
                    stack4.append(stack8[len(stack8) - 1])
                    stack8.pop()
                elif dest == 5:
                    stack5.append(stack8[len(stack8) - 1])
                    stack8.pop()
                elif dest == 6:
                    stack6.append(stack8[len(stack8) - 1])
                    stack8.pop()
                elif dest == 9:
                    stack9.append(stack8[len(stack8) - 1])
                    stack8.pop()
                else:
                    stack7.append(stack8[len(stack8) - 1])
                    stack8.pop()
            if source == 9:
                if dest == 1:
                    stack1.append(stack9[len(stack9) - 1])
                    stack9.pop()
                elif dest == 2:
                    stack2.append(stack9[len(stack9) - 1])
                    stack9.pop()
                elif dest == 3:
                    stack3.append(stack9[len(stack9) - 1])
                    stack9.pop()
                elif dest == 4:
                    stack4.append(stack9[len(stack9) - 1])
                    stack9.pop()
                elif dest == 5:
                    stack5.append(stack9[len(stack9) - 1])
                    stack9.pop()
                elif dest == 6:
                    stack6.append(stack9[len(stack9) - 1])
                    stack9.pop()
                elif dest == 7:
                    stack7.append(stack9[len(stack9) - 1])
                    stack9.pop()
                else:
                    stack8.append(stack9[len(stack9) - 1])
                    stack9.pop()
            boxes -= 1
    print(stack1[len(stack1) - 1])
    print(stack2[len(stack2) - 1])
    print(stack3[len(stack3) - 1])
    print(stack4[len(stack4) - 1])
    print(stack5[len(stack5) - 1])
    print(stack6[len(stack6) - 1])
    print(stack7[len(stack7) - 1])
    print(stack8[len(stack8) - 1])
    print(stack9[len(stack9) - 1])


#stacks1()

def stacks2():
    stacks = [['F', 'G', 'V', 'R', 'J', 'L', 'D'],
              ['S', 'J', 'H', 'V', 'B', 'M', 'P', 'T'],
              ['C', 'P', 'G', 'D', 'F', 'M', 'H', 'V'],
              ['Q', 'G', 'N', 'P', 'D', 'M'],
              ['F', 'N', 'H', 'L', 'J'],
              ['Z', 'T', 'G', 'D', 'Q', 'V', 'F', 'N'],
              ['L', 'B', 'D', 'F'],
              ['N', 'D', 'V', 'S', 'B', 'J', 'M'],
              ['D', 'L', 'G']]
    aux = []

    for j in stacks:
        j.reverse()

    f = open("text.txt")
    for i in f:
        instruction = i.split(' ')
        box = int(instruction[1])
        origin = int(instruction[3])
        destination = int(instruction[5])
        while box != 0:
            aux.append(stacks[origin - 1][len(stacks[origin - 1]) - 1])
            stacks[origin - 1].pop()
            box -= 1
        aux.reverse()
        stacks[destination - 1].extend(aux)
        aux = []
    for x in stacks:
        print(x[len(x) - 1])


stacks2()
