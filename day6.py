def buffer():
    f = open("text.txt")

    x = 0
    arr = []
    arrdupl = []
    pack = 0

    for i in f:
        while x != len(i) - 4:
            while pack != 4:
                arr.append(i[x + pack])
                pack += 1
            arrdupl = list(dict.fromkeys(arr))
            if arr == arrdupl:
                print(x+4)
                break
            x += 1
            arr = []
            arrdupl = []
            pack = 0

buffer()

def buffer2():
    f = open("text.txt")

    x = 0
    arr = []
    arrdupl = []
    pack = 0

    for i in f:
        while x != len(i) - 14:
            while pack != 14:
                arr.append(i[x + pack])
                pack += 1
            arrdupl = list(dict.fromkeys(arr))
            if arr == arrdupl:
                print(x + 14)
                break
            x += 1
            arr = []
            arrdupl = []
            pack = 0


buffer2()
