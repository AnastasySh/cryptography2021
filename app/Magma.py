import random

str1 = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя.,-?!: "
# РЕЖИМ ИМИТОВСТАВКА/////////////////////////////////////////////////////////////////////////


def imitovstavka(s):
    np = len(s)
    while len(s) < 16:
        randd = random.randint(0, 65)
        s2 = str1[randd]
        s = s + s2
    while len(s) % 8 != 0:
        randd = random.randint(0, 65)
        s2 = str1[randd]
        s = s + s2
    dva = [0]*1100
    shifr = [0]*1100

    for i in range(0, 1100):
        dva[i] = 0
        shifr[i] = 0
    key = [0]*64

    for i in range(0, 64):
        key[i] = random.randint(0, 16)

    for i in range(0, len(s)):
        pos = str1.find(s[i])
        dva[i * 2] = pos // 16
        dva[i * 2 + 1] = pos % 16

    for i in range(0, len(s)*2):
        dlina = i + 1

    la = [0]*8
    r = [0]*8
    message_16code = ""
    print("16-ричное сообщение:")
    for i in range(0, dlina):
        message_16code += str(dva[i])
    print(message_16code)
    for i in range(0, 8):
        la[i] = dva[i]
        r[i] = dva[i + 8]

    dvadva = [0]*32
    for i in range(0, 32):
        dvadva[i] = 0

    for x in range(1, int(dlina//16)):
        for h in range(0, 16):
            for i in range(0, 8):
                l_zap = la[i]
                la[i] = int(la[i]) + int(key[i + ((h * 8) % 64)]) % (2 ** 32)

                # Начало S-блока замены
                if i % 8 == 0:
                    if la[i] == 0:
                        la[i] = 12
                    else:
                        if la[i] == 1:
                            la[i] = 4
                        else:
                            if la[i] == 2:
                                la[i] = 6
                            else:
                                if la[i] == 3:
                                    la[i] = 2
                                else:
                                    if la[i] == 4:
                                        la[i] = 10
                                    else:
                                        if la[i] == 5:
                                            la[i] = 5
                                        else:
                                            if la[i] == 6:
                                                la[i] = 11
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 9
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 14
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 8
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 13
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 7
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 0
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 3
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 15
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 1
                if i % 8 == 1:
                    if la[i] == 0:
                        la[i] = 6
                    else:
                        if la[i] == 1:
                            la[i] = 8
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 3
                                else:
                                    if la[i] == 4:
                                        la[i] = 9
                                    else:
                                        if la[i] == 5:
                                            la[i] = 10
                                        else:
                                            if la[i] == 6:
                                                la[i] = 5
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 12
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 1
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 14
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 4
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 7
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 11
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 13
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 0
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 15
                if i % 8 == 2:
                    if la[i] == 0:
                        la[i] = 11
                    else:
                        if la[i] == 1:
                            la[i] = 3
                        else:
                            if la[i] == 2:
                                la[i] = 5
                            else:
                                if la[i] == 3:
                                    la[i] = 8
                                else:
                                    if la[i] == 4:
                                        la[i] = 2
                                    else:
                                        if la[i] == 5:
                                            la[i] = 15
                                        else:
                                            if la[i] == 6:
                                                la[i] = 10
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 13
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 14
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 1
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 7
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 4
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 12
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 9
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 6
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 0
                if i % 8 == 3:
                    if la[i] == 0:
                        la[i] = 12
                    else:
                        if la[i] == 1:
                            la[i] = 8
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 1
                                else:
                                    if la[i] == 4:
                                        la[i] = 13
                                    else:
                                        if la[i] == 5:
                                            la[i] = 4
                                        else:
                                            if la[i] == 6:
                                                la[i] = 15
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 6
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 7
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 0
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 10
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 5
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 3
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 14
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 9
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 11
                if i % 8 == 4:
                    if la[i] == 0:
                        la[i] = 7
                    else:
                        if la[i] == 1:
                            la[i] = 15
                        else:
                            if la[i] == 2:
                                la[i] = 5
                            else:
                                if la[i] == 3:
                                    la[i] = 10
                                else:
                                    if la[i] == 4:
                                        la[i] = 8
                                    else:
                                        if la[i] == 5:
                                            la[i] = 1
                                        else:
                                            if la[i] == 6:
                                                la[i] = 6
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 13
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 0
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 9
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 3
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 14
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 11
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 4
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 2
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 12
                if i % 8 == 5:
                    if la[i] == 0:
                        la[i] = 5
                    else:
                        if la[i] == 1:
                            la[i] = 13
                        else:
                            if la[i] == 2:
                                la[i] = 15
                            else:
                                if la[i] == 3:
                                    la[i] = 6
                                else:
                                    if la[i] == 4:
                                        la[i] = 9
                                    else:
                                        if la[i] == 5:
                                            la[i] = 2
                                        else:
                                            if la[i] == 6:
                                                la[i] = 12
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 10
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 11
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 7
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 8
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 1
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 4
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 3
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 14
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 0
                if i % 8 == 6:
                    if la[i] == 0:
                        la[i] = 8
                    else:
                        if la[i] == 1:
                            la[i] = 14
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 5
                                else:
                                    if la[i] == 4:
                                        la[i] = 6
                                    else:
                                        if la[i] == 5:
                                            la[i] = 9
                                        else:
                                            if la[i] == 6:
                                                la[i] = 1
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 12
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 15
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 4
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 11
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 0
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 13
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 10
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 3
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 7
                if i % 8 == 7:
                    if la[i] == 0:
                        la[i] = 1
                    else:
                        if la[i] == 1:
                            la[i] = 7
                        else:
                            if la[i] == 2:
                                la[i] = 14
                            else:
                                if la[i] == 3:
                                    la[i] = 13
                                else:
                                    if la[i] == 4:
                                        la[i] = 0
                                    else:
                                        if la[i] == 5:
                                            la[i] = 5
                                        else:
                                            if la[i] == 6:
                                                la[i] = 8
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 3
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 4
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 15
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 10
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 6
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 9
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 12
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 11
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 2
                # Конец S-блока замены

                for v in range(0, 4):
                    if la[2 * v] >= 8:
                        dvadva[0 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 8
                    if la[2 * v] >= 4:
                        dvadva[1 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 4
                    if la[2 * v] >= 2:
                        dvadva[2 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 2
                    if la[2 * v] >= 1:
                        dvadva[3 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 1
                    if la[2 * v + 1] >= 8:
                        dvadva[4 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 8
                    if la[2 * v + 1] >= 4:
                        dvadva[5 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 4
                    if la[2 * v + 1] >= 2:
                        dvadva[6 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 2
                    if la[2 * v + 1] >= 1:
                        dvadva[7 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 1

                # Сдвиг на на 11 шагов в сторону старшего разряда
                for v in range(0, 11):
                    dvadva_zam = dvadva[0]
                    for j in range(1, 32):
                        dvadva[j - 1] = dvadva[j]
                    dvadva[31] = dvadva_zam

                for v in range(0, 4):
                    if dvadva[0 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 8
                    if dvadva[1 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 4
                    if dvadva[2 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 2
                    if dvadva[3 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 1
                    if dvadva[4 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 8
                    if dvadva[5 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 4
                    if dvadva[6 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 2
                    if dvadva[7 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 1

                for v in range(0, 32):
                    dvadva[v] = 0

                la[i] = int(la[i]) ^ int(r[i])
                r[i] = l_zap

        for ii in range(0, 8):
            la[ii] = int(la[ii]) ^ int(dva[ii + 16 * x])
            r[ii] = int(r[ii]) ^ int(dva[ii + 8 + 16 * x])

    # РЕЗУЛЬТАТ ИМИТОВСТАВКИ
    otvet_imitovstavka = ""
    for i in range(0, 8):
        if la[i] == 10:
            otvet_imitovstavka += "A"
            # print("A")
        else:
            if la[i] == 11:
                otvet_imitovstavka += "B"
                # print("B")
            else:
                if la[i] == 12:
                    otvet_imitovstavka += "C"
                    # print("C")
                else:
                    if la[i] == 13:
                        otvet_imitovstavka += "D"
                        # print("D")
                    else:
                        if la[i] == 14:
                            otvet_imitovstavka += "E"
                            # print("E")
                        else:
                            if la[i] == 15:
                                otvet_imitovstavka += "F"
                                # print("F")
                            else:
                                otvet_imitovstavka += str(la[i])
                                # print(la[i])
    for i in range(0, 8):
        if r[i] == 10:
            otvet_imitovstavka += "A"
            # print("A")
        else:
            if r[i] == 11:
                otvet_imitovstavka += "B"
                # print("B")
            else:
                if r[i] == 12:
                    otvet_imitovstavka += "C"
                    # print("C")
                else:
                    if r[i] == 13:
                        otvet_imitovstavka += "D"
                        # print("D")
                    else:
                        if r[i] == 14:
                            otvet_imitovstavka += "E"
                            # print("E")
                        else:
                            if r[i] == 15:
                                otvet_imitovstavka += "F"
                                # print("F")
                            else:
                                otvet_imitovstavka += str(r[i])
                                # print(r[i])
    print("Имитовставка:", otvet_imitovstavka)

# РЕЖИМ ПРОСТОЙ ЗАМЕНЫ///////////////////////////////////////////////////////////////////////////


def prZamena(s):
    np = len(s)

    while len(s) % 8 != 0:
        randd = random.randint(0, 65)
        s2 = str1[randd]
        s = s + s2

    dva = [0]*1100
    shifr = [0]*1100
    for i in range(0, 1100):
        dva[i] = 0
        shifr[i] = 0

    key = [0]*64
    for i in range(0, 64):
        key[i] = random.randint(0, 16)

    for i in range(0, len(s)):
        pos = str1.find(s[i])
        dva[i * 2] = pos // 16
        dva[i * 2 + 1] = pos % 16

    for i in range(0, len(s)*2):
        dlina = int(i + 1)
    la = [0]*8
    r = [0]*8
    for i in range(0, 8):
        la[i] = 0
        r[i] = 0

    message16x = ""
    for i in range(0, int(dlina)):
        message16x += str(dva[i])
    print("16-ричное сообщение:", message16x)
    dvadva = [0]*32
    for i in range(0, 32):
        dvadva[i] = 0

    for x in range(0, int(dlina//16)):
        for ii in range(0, 8):
            la[ii] = dva[ii + 16 * x]
            r[ii] = dva[ii + 8 + 16 * x]
        for h in range(0, 32):
            for i in range(0, 8):
                l_zap = la[i]
                if h < 24:
                    la[i] = int(la[i]) + \
                        int(key[i + ((h * 8) % 64)]) % (2 ** 32)
                else:
                    la[i] = int(la[i]) + \
                        int(key[56 + i - ((h * 8) % 64)]) % (2 ** 32)

                # Начало S-блока замены
                if i % 8 == 0:
                    if la[i] == 0:
                        la[i] = 12
                    else:
                        if la[i] == 1:
                            la[i] = 4
                        else:
                            if la[i] == 2:
                                la[i] = 6
                            else:
                                if la[i] == 3:
                                    la[i] = 2
                                else:
                                    if la[i] == 4:
                                        la[i] = 10
                                    else:
                                        if la[i] == 5:
                                            la[i] = 5
                                        else:
                                            if la[i] == 6:
                                                la[i] = 11
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 9
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 14
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 8
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 13
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 7
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 0
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 3
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 15
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 1
                if i % 8 == 1:
                    if la[i] == 0:
                        la[i] = 6
                    else:
                        if la[i] == 1:
                            la[i] = 8
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 3
                                else:
                                    if la[i] == 4:
                                        la[i] = 9
                                    else:
                                        if la[i] == 5:
                                            la[i] = 10
                                        else:
                                            if la[i] == 6:
                                                la[i] = 5
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 12
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 1
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 14
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 4
                                                            else:
                                                                if (la[i] == 11):
                                                                    la[i] = 7
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 11
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 13
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 0
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 15
                if i % 8 == 2:
                    if la[i] == 0:
                        la[i] = 11
                    else:
                        if la[i] == 1:
                            la[i] = 3
                        else:
                            if la[i] == 2:
                                la[i] = 5
                            else:
                                if la[i] == 3:
                                    la[i] = 8
                                else:
                                    if la[i] == 4:
                                        la[i] = 2
                                    else:
                                        if la[i] == 5:
                                            la[i] = 15
                                        else:
                                            if la[i] == 6:
                                                la[i] = 10
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 13
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 14
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 1
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 7
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 4
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 12
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 9
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 6
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 0
                if i % 8 == 3:
                    if la[i] == 0:
                        la[i] = 12
                    else:
                        if la[i] == 1:
                            la[i] = 8
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 1
                                else:
                                    if la[i] == 4:
                                        la[i] = 13
                                    else:
                                        if la[i] == 5:
                                            la[i] = 4
                                        else:
                                            if la[i] == 6:
                                                la[i] = 15
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 6
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 7
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 0
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 10
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 5
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 3
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 14
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 9
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 11
                if i % 8 == 4:
                    if la[i] == 0:
                        la[i] = 7
                    else:
                        if la[i] == 1:
                            la[i] = 15
                        else:
                            if la[i] == 2:
                                la[i] = 5
                            else:
                                if la[i] == 3:
                                    la[i] = 10
                                else:
                                    if la[i] == 4:
                                        la[i] = 8
                                    else:
                                        if la[i] == 5:
                                            la[i] = 1
                                        else:
                                            if la[i] == 6:
                                                la[i] = 6
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 13
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 0
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 9
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 3
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 14
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 11
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 4
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 2
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 12

                if i % 8 == 5:
                    if la[i] == 0:
                        la[i] = 5
                    else:
                        if la[i] == 1:
                            la[i] = 13
                        else:
                            if la[i] == 2:
                                la[i] = 15
                            else:
                                if la[i] == 3:
                                    la[i] = 6
                                else:
                                    if la[i] == 4:
                                        la[i] = 9
                                    else:
                                        if la[i] == 5:
                                            la[i] = 2
                                        else:
                                            if la[i] == 6:
                                                la[i] = 12
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 10
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 11
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 7
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 8
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 1
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 4
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 3
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 14
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 0

                if i % 8 == 6:
                    if la[i] == 0:
                        la[i] = 8
                    else:
                        if la[i] == 1:
                            la[i] = 14
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 5
                                else:
                                    if la[i] == 4:
                                        la[i] = 6
                                    else:
                                        if la[i] == 5:
                                            la[i] = 9
                                        else:
                                            if la[i] == 6:
                                                la[i] = 1
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 12
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 15
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 4
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 11
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 0
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 13
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 10
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 3
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 7

                if i % 8 == 7:
                    if la[i] == 0:
                        la[i] = 1
                    else:
                        if la[i] == 1:
                            la[i] = 7
                        else:
                            if la[i] == 2:
                                la[i] = 14
                            else:
                                if la[i] == 3:
                                    la[i] = 13
                                else:
                                    if la[i] == 4:
                                        la[i] = 0
                                    else:
                                        if la[i] == 5:
                                            la[i] = 5
                                        else:
                                            if la[i] == 6:
                                                la[i] = 8
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 3
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 4
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 15
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 10
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 6
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 9
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 12
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 11
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 2
                # Конец S-блока замены

                la[i] = int(la[i]) ^ int(r[i])
                r[i] = l_zap

        for z in range(0, 8):
            shifr[z + 16 * x] = la[z]
            shifr[z + 8 + 16 * x] = r[z]

    encode = ""
    for i in range(0, dlina):
        encode += str(shifr[i])
    print("Зашифрованное сообщение:", encode)

    for x in range(0, int(dlina//16)):
        for ii in range(0, 8):
            r[ii] = shifr[ii + 16 * x]
            la[ii] = shifr[ii + 8 + 16 * x]

        for h in range(0, 32):
            for i in range(0, 8):
                l_zap = la[i]

                if h < 8:
                    la[i] = la[i] ^ key[i + ((h * 8) % 64)]
                else:
                    la[i] = la[i] ^ key[56 + i - ((h * 8) % 64)]

                # Начало S-блока замены
                if i % 8 == 0:
                    if la[i] == 0:
                        la[i] = 12
                    else:
                        if la[i] == 1:
                            la[i] = 4
                        else:
                            if la[i] == 2:
                                la[i] = 6
                            else:
                                if la[i] == 3:
                                    la[i] = 2
                                else:
                                    if la[i] == 4:
                                        la[i] = 10
                                    else:
                                        if la[i] == 5:
                                            la[i] = 5
                                        else:
                                            if la[i] == 6:
                                                la[i] = 11
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 9
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 14
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 8
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 13
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 7
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 0
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 3
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 15
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 1

                if i % 8 == 1:
                    if la[i] == 0:
                        la[i] = 6
                    else:
                        if la[i] == 1:
                            la[i] = 8
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 3
                                else:
                                    if la[i] == 4:
                                        la[i] = 9
                                    else:
                                        if la[i] == 5:
                                            la[i] = 10
                                        else:
                                            if la[i] == 6:
                                                la[i] = 5
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 12
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 1
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 14
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 4
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 7
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 11
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 13
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 0
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 15

                if i % 8 == 2:
                    if la[i] == 0:
                        la[i] = 11
                    else:
                        if la[i] == 1:
                            la[i] = 3
                        else:
                            if la[i] == 2:
                                la[i] = 5
                            else:
                                if la[i] == 3:
                                    la[i] = 8
                                else:
                                    if la[i] == 4:
                                        la[i] = 2
                                    else:
                                        if la[i] == 5:
                                            la[i] = 15
                                        else:
                                            if la[i] == 6:
                                                la[i] = 10
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 13
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 14
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 1
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 7
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 4
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 12
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 9
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 6
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 0

                if i % 8 == 3:
                    if la[i] == 0:
                        la[i] = 12
                    else:
                        if la[i] == 1:
                            la[i] = 8
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 1
                                else:
                                    if la[i] == 4:
                                        la[i] = 13
                                    else:
                                        if la[i] == 5:
                                            la[i] = 4
                                        else:
                                            if la[i] == 6:
                                                la[i] = 15
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 6
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 7
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 0
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 10
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 5
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 3
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 14
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 9
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 11

                if i % 8 == 4:
                    if la[i] == 0:
                        la[i] = 7
                    else:
                        if la[i] == 1:
                            la[i] = 15
                        else:
                            if la[i] == 2:
                                la[i] = 5
                            else:
                                if la[i] == 3:
                                    la[i] = 10
                                else:
                                    if la[i] == 4:
                                        la[i] = 8
                                    else:
                                        if la[i] == 5:
                                            la[i] = 1
                                        else:
                                            if la[i] == 6:
                                                la[i] = 6
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 13
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 0
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 9
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 3
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 14
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 11
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 4
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 2
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 12

                if i % 8 == 5:
                    if la[i] == 0:
                        la[i] = 5
                    else:
                        if la[i] == 1:
                            la[i] = 13
                        else:
                            if la[i] == 2:
                                la[i] = 15
                            else:
                                if la[i] == 3:
                                    la[i] = 6
                                else:
                                    if la[i] == 4:
                                        la[i] = 9
                                    else:
                                        if la[i] == 5:
                                            la[i] = 2
                                        else:
                                            if la[i] == 6:
                                                la[i] = 12
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 10
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 11
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 7
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 8
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 1
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 4
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 3
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 14
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 0

                if i % 8 == 6:
                    if la[i] == 0:
                        la[i] = 8
                    else:
                        if la[i] == 1:
                            la[i] = 14
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 5
                                else:
                                    if la[i] == 4:
                                        la[i] = 6
                                    else:
                                        if la[i] == 5:
                                            la[i] = 9
                                        else:
                                            if la[i] == 6:
                                                la[i] = 1
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 12
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 15
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 4
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 11
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 0
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 13
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 10
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 3
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 7
                if i % 8 == 7:
                    if la[i] == 0:
                        la[i] = 1
                    else:
                        if la[i] == 1:
                            la[i] = 7
                        else:
                            if la[i] == 2:
                                la[i] = 14
                            else:
                                if la[i] == 3:
                                    la[i] = 13
                                else:
                                    if la[i] == 4:
                                        la[i] = 0
                                    else:
                                        if la[i] == 5:
                                            la[i] = 5
                                        else:
                                            if la[i] == 6:
                                                la[i] = 8
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 3
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 4
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 15
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 10
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 6
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 9
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 12
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 11
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 2
                # Конец S-блока замены

                la[i] = la[i] ^ r[i]
                r[i] = l_zap

        for z in range(0, 8):
            dva[z + 8 + 16 * x] = la[z]
            dva[z + 16 * x] = r[z]

    decode16x = ""

    for i in range(0, dlina):
        decode16x += str(dva[i])
    print("Расшифрованное 16-ричное сообщение:", decode16x)

    decode = ""
    for i in range(0, np):
        decode += str1[dva[i * 2] * 16 + dva[i * 2 + 1]]
    print("Расшифрованное сообщение:", decode)

# Гаммирование////////////////////////////////////////////////////////////////////////////////////////////////


def Gamma(s):
    posi1ka = [0] * 8  # восьмибитовый массив
    enc_s = ""
    dec_s = ""
    consts = [0]*8  # тоже восьмибитовый массив
    consts[0] = 4  # добавляем в начало 4ку
    for i in range(1, 8):  # остальное заполняем единицами
        consts[i] = 1

    while len(s) % 8 != 0:  # дополняем сообщение рандомными символами из словаря
        randd = random.randint(0, 65)  # 65 размер словаря
        s2 = str1[randd]
        s = s + s2
# шифрование
    print("Дополненное сообщение: ", s)
    posilka = [0] * 8
    posilka_zap = [0] * 8
    for i in range(0, 8):  # массив с рандомными значениями
        # почему 71 потому что длина алфавита 71
        posilka[i] = random.randint(0, 71)
    for i in range(0, 8):
        posilka_zap[i] = posilka[i]  # копирование
    zzz = 0
    kost = [0]*5000
    for i in range(0, 5000):  # заполнение очень огромного массива нулями
        kost[i] = 0
    dva = [0]*16
    for i in range(0, 16):
        dva[i] = 0
    la = [0] * 8
    r = [0] * 8
    for i in range(0, 8):
        la[i] = 0
        r[i] = 0
        # 16ричное число = 4 бита
        # key - ключ 64 разрядный (64*4=256 бит)
        # dva - 16 разрядная двоичная последовательность, преобразованная в 16 ричный формат СИНХРОПОСЫЛКА 16*4 = 64бит (т.к. изначально у нас генерит числа от 0 до 71)
        # posilka - НЕДОсинхропосылка тут в этом шифре 8 разрядная двоичная последовательность (8*4 = 32 бит)
        # la - лквая часть, накопитель N1 8 разрядный
        # r - накопитель N2 8 разрядный
        # в S-блоках идет отчет от 0 до 15 потому что буквы в HEX это для слабаков
        # создание массива "под ключ"(хыхы) быстро, недорого, без регистрации и смс
    key = [0]*64
    for i in range(0, 64):
        key[i] = random.randint(0, 16)  # рандомные значения тоже под ключ
    dvadva = [0]*32
    for i in range(0, 32):
        dvadva[i] = 0
    # каждая 16 число это 4 бита следовательно 8*4 = 32 бита отсчет по блокам
    for j in range(0, len(s) // 8):
        # НАЧАЛО шифрования синхропосылки в режиме простой замены
        # преобразование числа из алфавита в 71 в 16ричную
        # сама функция F posilka массив с рандомными значениями, синхропосылка 64-разрядная
        for i in range(0, 8):
            # двоичная последовательность (цитата взята из лекции но предполагаю что это ***. т.к. далее все должно
            # шифроваться в режиме простой замены, а режим простой замены оперирует блоками по 64 бита) далее идет
            # преобразование посылки в 16ричную штуку
            dva[i * 2] = posilka[i] // 16  # целочисленное деление
            dva[i * 2 + 1] = posilka[i] % 16  # и за ним сразу же модуль
    # разделение на левую и правую часть , никопители N1 N2
        for ii in range(0, 8):
            la[ii] = dva[ii]  # левая часть накопитель N1
            r[ii] = dva[ii + 8]  # правая часть накопитель N2
            # синхропосылка зашифровывается в режиме простой замены
    # 32 раунда
        for h in range(0, 32):
            # каждая левая часть преобразуется при помощи итерационного ключа. для каждой итерации используется итерационный ключ взятый из нашего 256 битного
            # после преобразований - прогоняется по S-блоку замен. После - сдвиг на 11 разрядов
            for i in range(0, 8):
                l_zap = la[i]
                if h < 24:
                    la[i] = la[i] ^ key[i + ((h * 8) % 64)]
                else:
                    la[i] = la[i] ^ key[56 + i - ((h * 8) % 64)]
            # Начало S-блока замены
                if i % 8 == 0:
                    if la[i] == 0:
                        la[i] = 12
                    else:
                        if la[i] == 1:
                            la[i] = 4
                        else:
                            if la[i] == 2:
                                la[i] = 6
                            else:
                                if la[i] == 3:
                                    la[i] = 2
                                else:
                                    if la[i] == 4:
                                        la[i] = 10
                                    else:
                                        if la[i] == 5:
                                            la[i] = 5
                                        else:
                                            if la[i] == 6:
                                                la[i] = 11
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 9
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 14
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 8
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 13
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 7
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 0
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 3
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 15
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 1

                if i % 8 == 1:
                    if la[i] == 0:
                        la[i] = 6
                    else:
                        if la[i] == 1:
                            la[i] = 8
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 3
                                else:
                                    if la[i] == 4:
                                        la[i] = 9
                                    else:
                                        if la[i] == 5:
                                            la[i] = 10
                                        else:
                                            if la[i] == 6:
                                                la[i] = 5
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 12
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 1
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 14
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 4
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 7
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 11
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 13
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 0
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 15

                if i % 8 == 2:
                    if la[i] == 0:
                        la[i] = 11
                    else:
                        if la[i] == 1:
                            la[i] = 3
                        else:
                            if la[i] == 2:
                                la[i] = 5
                            else:
                                if la[i] == 3:
                                    la[i] = 8
                                else:
                                    if la[i] == 4:
                                        la[i] = 2
                                    else:
                                        if la[i] == 5:
                                            la[i] = 15
                                        else:
                                            if la[i] == 6:
                                                la[i] = 10
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 13
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 14
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 1
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 7
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 4
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 12
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 9
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 6
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 0
                if i % 8 == 3:
                    if la[i] == 0:
                        la[i] = 12
                    else:
                        if la[i] == 1:
                            la[i] = 8
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 1
                                else:
                                    if la[i] == 4:
                                        la[i] = 13
                                    else:
                                        if la[i] == 5:
                                            la[i] = 4
                                        else:
                                            if la[i] == 6:
                                                la[i] = 15
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 6
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 7
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 0
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 10
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 5
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 3
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 14
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 9
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 11

                if i % 8 == 4:
                    if la[i] == 0:
                        la[i] = 7
                    else:
                        if la[i] == 1:
                            la[i] = 15
                        else:
                            if la[i] == 2:
                                la[i] = 5
                            else:
                                if la[i] == 3:
                                    la[i] = 10
                                else:
                                    if la[i] == 4:
                                        la[i] = 8
                                    else:
                                        if la[i] == 5:
                                            la[i] = 1
                                        else:
                                            if la[i] == 6:
                                                la[i] = 6
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 13
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 0
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 9
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 3
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 14
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 11
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 4
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 2
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 12
                if i % 8 == 5:
                    if la[i] == 0:
                        la[i] = 5
                    else:
                        if la[i] == 1:
                            la[i] = 13
                        else:
                            if la[i] == 2:
                                la[i] = 15
                            else:
                                if la[i] == 3:
                                    la[i] = 6
                                else:
                                    if la[i] == 4:
                                        la[i] = 9
                                    else:
                                        if la[i] == 5:
                                            la[i] = 2
                                        else:
                                            if la[i] == 6:
                                                la[i] = 12
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 10
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 11
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 7
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 8
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 1
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 4
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 3
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 14
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 0
                if i % 8 == 6:
                    if la[i] == 0:
                        la[i] = 8
                    else:
                        if la[i] == 1:
                            la[i] = 14
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 5
                                else:
                                    if la[i] == 4:
                                        la[i] = 6
                                    else:
                                        if la[i] == 5:
                                            la[i] = 9
                                        else:
                                            if la[i] == 6:
                                                la[i] = 1
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 12
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 15
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 4
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 11
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 0
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 13
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 10
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 3
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 7
                if i % 8 == 7:
                    if la[i] == 0:
                        la[i] = 1
                    else:
                        if la[i] == 1:
                            la[i] = 7
                        else:
                            if la[i] == 2:
                                la[i] = 14
                            else:
                                if la[i] == 3:
                                    la[i] = 13
                                else:
                                    if la[i] == 4:
                                        la[i] = 0
                                    else:
                                        if la[i] == 5:
                                            la[i] = 5
                                        else:
                                            if la[i] == 6:
                                                la[i] = 8
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 3
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 4
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 15
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 10
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 6
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 9
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 12
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 11
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 2
                # Конец S-блока замены
            # далее происходит преобразование 16 чисел в двоичное формата 0000 на число т.к. 16 ричная = 4 бита
                print(la)
                for v in range(0, 4):
                    if la[2 * v] >= 8:
                        dvadva[0 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 8

                    if la[2 * v] >= 4:
                        dvadva[1 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 4

                    if la[2 * v] >= 2:
                        dvadva[2 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 2

                    if la[2 * v] >= 1:
                        dvadva[3 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 1

                    if la[2 * v + 1] >= 8:
                        dvadva[4 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 8

                    if la[2 * v + 1] >= 4:
                        dvadva[5 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 4

                    if la[2 * v + 1] >= 2:
                        dvadva[6 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 2

                    if la[2 * v + 1] >= 1:
                        dvadva[7 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 1
                print(dvadva)
            # циклический сдвиг на на 11 шагов в сторону старшего разряда
                for v in range(0, 11):
                    dvadva_zam = dvadva[0]
                    for kek in range(1, 32):
                        dvadva[kek - 1] = dvadva[kek]
                    dvadva[31] = dvadva_zam
            # преобразование обратно в 16чную систему
                for v in range(0, 4):
                    if dvadva[0 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 8
                    if dvadva[1 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 4
                    if dvadva[2 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 2
                    if dvadva[3 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 1
                    if dvadva[4 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 8
                    if dvadva[5 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 4
                    if dvadva[6 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 2
                    if dvadva[7 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 1
            # обнуление буффера для двоичных чисел
                for v in range(0, 32):
                    dvadva[v] = 0
            # ксор левой и правой части и смена местами
                la[i] = la[i] ^ r[i]
                r[i] = l_zap
        # конец 32 раундов
    # сбор посылки обратно в эту срань где числа от 0 до 71, чтобы гамма могла быть в рамках нашего алфавита
        for i in range(0, 4):
            posilka[i] = la[i * 2] * 16 + la[i * 2 + 1]
            posilka[i + 4] = r[i * 2] * 16 + r[i * 2 + 1]
    # Конец шифрования синхропосылки в режиме простой замены

# преобразования посылки, ксор их с константой
        for i in range(0, 8):
            posilka[i] = posilka[i] ^ consts[i]
            if i == 3:
                posilka[i] = posilka[i] - 1
    # черновой вариант
        for i in range(0, 8):
            posi1ka[i] = (posilka[i] + consts[i]) % 2 ** 32
            if i == 3:
                posi1ka[i] = posilka[i] - 1

# НАЧАЛО второго преобразования синхропосылки в режиме простой замены
    # преобразование в 16ю систему
        for i in range(0, 8):
            dva[i * 2] = posilka[i] // 16
            dva[i * 2 + 1] = posilka[i] % 16
    # разделения на накопители N1 N2
        for ii in range(0, 8):
            la[ii] = dva[ii]
            r[ii] = dva[ii + 8]
    # 32 раунда преобразования при помощи итерационного ключа
        for h in range(0, 32):
            for i in range(0, 8):
                l_zap = la[i]
                if h < 24:
                    la[i] = la[i] ^ key[i + ((h * 8) % 64)]
                else:
                    la[i] = la[i] ^ key[56 + i - ((h * 8) % 64)]

        # Начало S-блока замены
                if i % 8 == 0:
                    if la[i] == 0:
                        la[i] = 12
                    else:
                        if la[i] == 1:
                            la[i] = 4
                        else:
                            if la[i] == 2:
                                la[i] = 6
                            else:
                                if la[i] == 3:
                                    la[i] = 2
                                else:
                                    if la[i] == 4:
                                        la[i] = 10
                                    else:
                                        if la[i] == 5:
                                            la[i] = 5
                                        else:
                                            if la[i] == 6:
                                                la[i] = 11
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 9
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 14
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 8
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 13
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 7
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 0
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 3
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 15
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 1
                if i % 8 == 1:
                    if la[i] == 0:
                        la[i] = 6
                    else:
                        if la[i] == 1:
                            la[i] = 8
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 3
                                else:
                                    if la[i] == 4:
                                        la[i] = 9
                                    else:
                                        if la[i] == 5:
                                            la[i] = 10
                                        else:
                                            if la[i] == 6:
                                                la[i] = 5
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 12
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 1
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 14
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 4
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 7
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 11
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 13
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 0
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 15
                if i % 8 == 2:
                    if la[i] == 0:
                        la[i] = 11
                    else:
                        if la[i] == 1:
                            la[i] = 3
                        else:
                            if la[i] == 2:
                                la[i] = 5
                            else:
                                if la[i] == 3:
                                    la[i] = 8
                                else:
                                    if la[i] == 4:
                                        la[i] = 2
                                    else:
                                        if la[i] == 5:
                                            la[i] = 15
                                        else:
                                            if la[i] == 6:
                                                la[i] = 10
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 13
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 14
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 1
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 7
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 4
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 12
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 9
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 6
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 0
                if i % 8 == 3:
                    if la[i] == 0:
                        la[i] = 12
                    else:
                        if la[i] == 1:
                            la[i] = 8
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 1
                                else:
                                    if la[i] == 4:
                                        la[i] = 13
                                    else:
                                        if la[i] == 5:
                                            la[i] = 4
                                        else:
                                            if la[i] == 6:
                                                la[i] = 15
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 6
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 7
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 0
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 10
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 5
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 3
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 14
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 9
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 11
                if i % 8 == 4:
                    if la[i] == 0:
                        la[i] = 7
                    else:
                        if la[i] == 1:
                            la[i] = 15
                        else:
                            if la[i] == 2:
                                la[i] = 5
                            else:
                                if la[i] == 3:
                                    la[i] = 10
                                else:
                                    if la[i] == 4:
                                        la[i] = 8
                                    else:
                                        if la[i] == 5:
                                            la[i] = 1
                                        else:
                                            if la[i] == 6:
                                                la[i] = 6
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 13
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 0
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 9
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 3
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 14
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 11
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 4
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 2
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 12
                if i % 8 == 5:
                    if la[i] == 0:
                        la[i] = 5
                    else:
                        if la[i] == 1:
                            la[i] = 13
                        else:
                            if la[i] == 2:
                                la[i] = 15
                            else:
                                if la[i] == 3:
                                    la[i] = 6
                                else:
                                    if la[i] == 4:
                                        la[i] = 9
                                    else:
                                        if la[i] == 5:
                                            la[i] = 2
                                        else:
                                            if la[i] == 6:
                                                la[i] = 12
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 10
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 11
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 7
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 8
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 1
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 4
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 3
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 14
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 0
                if i % 8 == 6:
                    if la[i] == 0:
                        la[i] = 8
                    else:
                        if la[i] == 1:
                            la[i] = 14
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 5
                                else:
                                    if la[i] == 4:
                                        la[i] = 6
                                    else:
                                        if la[i] == 5:
                                            la[i] = 9
                                        else:
                                            if la[i] == 6:
                                                la[i] = 1
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 12
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 15
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 4
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 11
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 0
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 13
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 10
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 3
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 7
                if i % 8 == 7:
                    if la[i] == 0:
                        la[i] = 1
                    else:
                        if la[i] == 1:
                            la[i] = 7
                        else:
                            if la[i] == 2:
                                la[i] = 14
                            else:
                                if la[i] == 3:
                                    la[i] = 13
                                else:
                                    if la[i] == 4:
                                        la[i] = 0
                                    else:
                                        if la[i] == 5:
                                            la[i] = 5
                                        else:
                                            if la[i] == 6:
                                                la[i] = 8
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 3
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 4
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 15
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 10
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 6
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 9
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 12
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 11
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 2
                # Конец S-блока замены
        # преобразование bp 16ричн в 2ю
                for v in range(0, 4):
                    if la[2 * v] >= 8:
                        dvadva[0 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 8

                    if la[2 * v] >= 4:
                        dvadva[1 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 4

                    if la[2 * v] >= 2:
                        dvadva[2 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 2

                    if la[2 * v] >= 1:
                        dvadva[3 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 1

                    if la[2 * v + 1] >= 8:
                        dvadva[4 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 8

                    if la[2 * v + 1] >= 4:
                        dvadva[5 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 4

                    if la[2 * v + 1] >= 2:
                        dvadva[6 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 2

                    if la[2 * v + 1] >= 1:
                        dvadva[7 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 1
        # Сдвиг на на 11 шагов в сторону старшего разряда
                for v in range(0, 11):
                    dvadva_zam = dvadva[0]
                    for kek in range(1, 32):
                        dvadva[kek - 1] = dvadva[kek]
                    dvadva[31] = dvadva_zam
        # преобразование обратно
                for v in range(0, 4):
                    if dvadva[0 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 8
                    if dvadva[1 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 4
                    if dvadva[2 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 2
                    if dvadva[3 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 1
                    if dvadva[4 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 8
                    if dvadva[5 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 4
                    if dvadva[6 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 2
                    if dvadva[7 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 1

                for v in range(0, 32):
                    dvadva[v] = 0
        # ксор левой и правой части
                la[i] = la[i] ^ r[i]
                r[i] = l_zap
    # преобразование обратно в систему по 71 (по алфавиту)
        for i in range(0, 4):
            posilka[i] = la[i * 2] * 16 + la[i * 2 + 1]
            posilka[i + 4] = r[i * 2] * 16 + r[i * 2 + 1]
    # КОНЕЦ второго режима простого шифрования

# блок для корректного определения индексов
        for i in range(int(8 * j), int(8 + (8 * j))):
            pos = str1.find(s[i])
            xx = pos ^ posilka[zzz]
            if xx >= 71:  # костыль для правильной расшифровки, как я поняла указывается ближайший круг алфавита
                kost[i] = 71
            if xx >= 142:
                kost[i] = 142
            if xx >= 213:
                kost[i] = 213

# наложение гезультирующей гаммы на сообщение
            # шифровка это текущая буква в 16ричке ксорнутая на соответствующее число из посылки по модулю алфавита
            enc_s += str1[(pos ^ posilka[zzz]) % 71]
            zzz += 1
        zzz = 0

    print("Зашифрованное сообщение:\n", enc_s)


# РАСШИФРОВАНИЕ
    for j in range(0, len(enc_s) // 8):
        j2 = j
    # начало преобразования синхропосылки по режиму простой замены
        for i in range(0, 8):
            dva[i * 2] = posilka_zap[i] // 16
            dva[i * 2 + 1] = posilka_zap[i] % 16

        for ii in range(0, 8):
            la[ii] = dva[ii]
            r[ii] = dva[ii + 8]

        for h in range(0, 32):
            for i in range(0, 8):
                l_zap = la[i]
                if h < 24:
                    la[i] = int(la[i]) + \
                        int(key[i + ((h * 8) % 64)]) % (2 ** 32)
                else:
                    la[i] = int(la[i]) + \
                        int(key[56 + i - ((h * 8) % 64)]) % (2 ** 32)

            # Начало S-блока замены
                if i % 8 == 0:
                    if la[i] == 0:
                        la[i] = 12
                    else:
                        if la[i] == 1:
                            la[i] = 4
                        else:
                            if la[i] == 2:
                                la[i] = 6
                            else:
                                if la[i] == 3:
                                    la[i] = 2
                                else:
                                    if la[i] == 4:
                                        la[i] = 10
                                    else:
                                        if la[i] == 5:
                                            la[i] = 5
                                        else:
                                            if la[i] == 6:
                                                la[i] = 11
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 9
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 14
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 8
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 13
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 7
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 0
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 3
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 15
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 1

                if i % 8 == 1:
                    if la[i] == 0:
                        la[i] = 6
                    else:
                        if la[i] == 1:
                            la[i] = 8
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 3
                                else:
                                    if la[i] == 4:
                                        la[i] = 9
                                    else:
                                        if la[i] == 5:
                                            la[i] = 10
                                        else:
                                            if la[i] == 6:
                                                la[i] = 5
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 12
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 1
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 14
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 4
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 7
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 11
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 13
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 0
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 15

                if i % 8 == 2:
                    if la[i] == 0:
                        la[i] = 11
                    else:
                        if la[i] == 1:
                            la[i] = 3
                        else:
                            if la[i] == 2:
                                la[i] = 5
                            else:
                                if la[i] == 3:
                                    la[i] = 8
                                else:
                                    if la[i] == 4:
                                        la[i] = 2
                                    else:
                                        if la[i] == 5:
                                            la[i] = 15
                                        else:
                                            if la[i] == 6:
                                                la[i] = 10
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 13
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 14
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 1
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 7
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 4
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 12
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 9
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 6
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 0
                if i % 8 == 3:
                    if la[i] == 0:
                        la[i] = 12
                    else:
                        if la[i] == 1:
                            la[i] = 8
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 1
                                else:
                                    if la[i] == 4:
                                        la[i] = 13
                                    else:
                                        if la[i] == 5:
                                            la[i] = 4
                                        else:
                                            if la[i] == 6:
                                                la[i] = 15
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 6
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 7
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 0
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 10
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 5
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 3
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 14
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 9
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 11

                if i % 8 == 4:
                    if la[i] == 0:
                        la[i] = 7
                    else:
                        if la[i] == 1:
                            la[i] = 15
                        else:
                            if la[i] == 2:
                                la[i] = 5
                            else:
                                if la[i] == 3:
                                    la[i] = 10
                                else:
                                    if la[i] == 4:
                                        la[i] = 8
                                    else:
                                        if la[i] == 5:
                                            la[i] = 1
                                        else:
                                            if la[i] == 6:
                                                la[i] = 6
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 13
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 0
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 9
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 3
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 14
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 11
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 4
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 2
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 12
                if i % 8 == 5:
                    if la[i] == 0:
                        la[i] = 5
                    else:
                        if la[i] == 1:
                            la[i] = 13
                        else:
                            if la[i] == 2:
                                la[i] = 15
                            else:
                                if la[i] == 3:
                                    la[i] = 6
                                else:
                                    if la[i] == 4:
                                        la[i] = 9
                                    else:
                                        if la[i] == 5:
                                            la[i] = 2
                                        else:
                                            if la[i] == 6:
                                                la[i] = 12
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 10
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 11
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 7
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 8
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 1
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 4
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 3
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 14
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 0
                if i % 8 == 6:
                    if la[i] == 0:
                        la[i] = 8
                    else:
                        if la[i] == 1:
                            la[i] = 14
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 5
                                else:
                                    if la[i] == 4:
                                        la[i] = 6
                                    else:
                                        if la[i] == 5:
                                            la[i] = 9
                                        else:
                                            if la[i] == 6:
                                                la[i] = 1
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 12
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 15
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 4
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 11
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 0
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 13
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 10
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 3
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 7
                if i % 8 == 7:
                    if la[i] == 0:
                        la[i] = 1
                    else:
                        if la[i] == 1:
                            la[i] = 7
                        else:
                            if la[i] == 2:
                                la[i] = 14
                            else:
                                if la[i] == 3:
                                    la[i] = 13
                                else:
                                    if la[i] == 4:
                                        la[i] = 0
                                    else:
                                        if la[i] == 5:
                                            la[i] = 5
                                        else:
                                            if la[i] == 6:
                                                la[i] = 8
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 3
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 4
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 15
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 10
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 6
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 9
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 12
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 11
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 2
                # Конец S-блока замены

                for v in range(0, 4):
                    if la[2 * v] >= 8:
                        dvadva[0 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 8

                    if la[2 * v] >= 4:
                        dvadva[1 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 4

                    if la[2 * v] >= 2:
                        dvadva[2 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 2

                    if la[2 * v] >= 1:
                        dvadva[3 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 1

                    if la[2 * v + 1] >= 8:
                        dvadva[4 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 8

                    if la[2 * v + 1] >= 4:
                        dvadva[5 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 4

                    if la[2 * v + 1] >= 2:
                        dvadva[6 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 2

                    if la[2 * v + 1] >= 1:
                        dvadva[7 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 1

                # Сдвиг на на 11 шагов в сторону старшего разряда
                for v in range(0, 11):
                    dvadva_zam = dvadva[0]
                    for j in range(1, 32):
                        dvadva[j - 1] = dvadva[j]
                    dvadva[31] = dvadva_zam

                for v in range(0, 4):
                    if dvadva[0 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 8
                    if dvadva[1 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 4
                    if dvadva[2 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 2
                    if dvadva[3 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 1
                    if dvadva[4 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 8
                    if dvadva[5 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 4
                    if dvadva[6 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 2
                    if dvadva[7 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 1

                for v in range(0, 32):
                    dvadva[v] = 0

                la[i] = la[i] ^ r[i]
                r[i] = l_zap

        for i in range(0, 4):
            posilka_zap[i] = la[i * 2] * 16 + la[i * 2 + 1]
            posilka_zap[i + 4] = r[i * 2] * 16 + r[i * 2 + 1]
        # КОНЕЦ первого преобразования по режиму простой замены

    # сложение посылки с константой
        for i in range(0, 8):
            posilka_zap[i] = posilka_zap[i] ^ consts[i]
            if i == 3:
                posilka_zap[i] = posilka_zap[i] - 1

    # НАЧАЛО второго преобразования в режиме простой замены
        for i in range(0, 8):
            dva[i * 2] = posilka_zap[i] // 16
            dva[i * 2 + 1] = posilka_zap[i] % 16

        for ii in range(0, 8):
            la[ii] = dva[ii]
            r[ii] = dva[ii + 8]

        for h in range(0, 32):
            for i in range(0, 8):
                l_zap = la[i]
                if h < 24:
                    la[i] = la[i] ^ key[i + ((h * 8) % 64)]
                else:
                    la[i] = la[i] ^ key[56 + i - ((h * 8) % 64)]

        # Начало S-блока замены
                if i % 8 == 0:
                    if la[i] == 0:
                        la[i] = 12
                    else:
                        if la[i] == 1:
                            la[i] = 4
                        else:
                            if la[i] == 2:
                                la[i] = 6
                            else:
                                if la[i] == 3:
                                    la[i] = 2
                                else:
                                    if la[i] == 4:
                                        la[i] = 10
                                    else:
                                        if la[i] == 5:
                                            la[i] = 5
                                        else:
                                            if la[i] == 6:
                                                la[i] = 11
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 9
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 14
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 8
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 13
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 7
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 0
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 3
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 15
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 1

                if i % 8 == 1:
                    if la[i] == 0:
                        la[i] = 6
                    else:
                        if la[i] == 1:
                            la[i] = 8
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 3
                                else:
                                    if la[i] == 4:
                                        la[i] = 9
                                    else:
                                        if la[i] == 5:
                                            la[i] = 10
                                        else:
                                            if la[i] == 6:
                                                la[i] = 5
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 12
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 1
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 14
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 4
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 7
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 11
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 13
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 0
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 15

                if i % 8 == 2:
                    if la[i] == 0:
                        la[i] = 11
                    else:
                        if la[i] == 1:
                            la[i] = 3
                        else:
                            if la[i] == 2:
                                la[i] = 5
                            else:
                                if la[i] == 3:
                                    la[i] = 8
                                else:
                                    if la[i] == 4:
                                        la[i] = 2
                                    else:
                                        if la[i] == 5:
                                            la[i] = 15
                                        else:
                                            if la[i] == 6:
                                                la[i] = 10
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 13
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 14
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 1
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 7
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 4
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 12
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 9
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 6
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 0
                if i % 8 == 3:
                    if la[i] == 0:
                        la[i] = 12
                    else:
                        if la[i] == 1:
                            la[i] = 8
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 1
                                else:
                                    if la[i] == 4:
                                        la[i] = 13
                                    else:
                                        if la[i] == 5:
                                            la[i] = 4
                                        else:
                                            if la[i] == 6:
                                                la[i] = 15
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 6
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 7
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 0
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 10
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 5
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 3
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 14
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 9
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 11

                if i % 8 == 4:
                    if la[i] == 0:
                        la[i] = 7
                    else:
                        if la[i] == 1:
                            la[i] = 15
                        else:
                            if la[i] == 2:
                                la[i] = 5
                            else:
                                if la[i] == 3:
                                    la[i] = 10
                                else:
                                    if la[i] == 4:
                                        la[i] = 8
                                    else:
                                        if la[i] == 5:
                                            la[i] = 1
                                        else:
                                            if la[i] == 6:
                                                la[i] = 6
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 13
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 0
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 9
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 3
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 14
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 11
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 4
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 2
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 12
                if i % 8 == 5:
                    if la[i] == 0:
                        la[i] = 5
                    else:
                        if la[i] == 1:
                            la[i] = 13
                        else:
                            if la[i] == 2:
                                la[i] = 15
                            else:
                                if la[i] == 3:
                                    la[i] = 6
                                else:
                                    if la[i] == 4:
                                        la[i] = 9
                                    else:
                                        if la[i] == 5:
                                            la[i] = 2
                                        else:
                                            if la[i] == 6:
                                                la[i] = 12
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 10
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 11
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 7
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 8
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 1
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 4
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 3
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 14
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 0
                if i % 8 == 6:
                    if la[i] == 0:
                        la[i] = 8
                    else:
                        if la[i] == 1:
                            la[i] = 14
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 5
                                else:
                                    if la[i] == 4:
                                        la[i] = 6
                                    else:
                                        if la[i] == 5:
                                            la[i] = 9
                                        else:
                                            if la[i] == 6:
                                                la[i] = 1
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 12
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 15
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 4
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 11
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 0
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 13
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 10
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 3
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 7
                if i % 8 == 7:
                    if la[i] == 0:
                        la[i] = 1
                    else:
                        if la[i] == 1:
                            la[i] = 7
                        else:
                            if la[i] == 2:
                                la[i] = 14
                            else:
                                if la[i] == 3:
                                    la[i] = 13
                                else:
                                    if la[i] == 4:
                                        la[i] = 0
                                    else:
                                        if la[i] == 5:
                                            la[i] = 5
                                        else:
                                            if la[i] == 6:
                                                la[i] = 8
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 3
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 4
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 15
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 10
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 6
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 9
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 12
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 11
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 2
            # Конец S-блока замены

                for v in range(0, 4):
                    if la[2 * v] >= 8:
                        dvadva[0 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 8

                    if la[2 * v] >= 4:
                        dvadva[1 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 4

                    if la[2 * v] >= 2:
                        dvadva[2 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 2

                    if la[2 * v] >= 1:
                        dvadva[3 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 1

                    if la[2 * v + 1] >= 8:
                        dvadva[4 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 8

                    if la[2 * v + 1] >= 4:
                        dvadva[5 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 4

                    if la[2 * v + 1] >= 2:
                        dvadva[6 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 2

                    if la[2 * v + 1] >= 1:
                        dvadva[7 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 1

        # Сдвиг на на 11 шагов в сторону старшего разряда
                for v in range(0, 11):
                    dvadva_zam = dvadva[0]
                    for j in range(1, 32):
                        dvadva[j - 1] = dvadva[j]
                    dvadva[31] = dvadva_zam

                for v in range(0, 4):
                    if dvadva[0 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 8
                    if dvadva[1 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 4
                    if dvadva[2 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 2
                    if dvadva[3 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 1
                    if dvadva[4 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 8
                    if dvadva[5 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 4
                    if dvadva[6 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 2
                    if dvadva[7 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 1

                for v in range(0, 32):
                    dvadva[v] = 0

                la[i] = la[i] ^ r[i]
                r[i] = l_zap

        for i in range(0, 4):
            posilka_zap[i] = la[i * 2] * 16 + la[i * 2 + 1]
            posilka_zap[i + 4] = r[i * 2] * 16 + r[i * 2 + 1]
        # конец второго преобразования

    # расшифровка сообщения методом ксора
        for i in range(int(8 * j2), int(8 + (8 * j2))):
            pos = str1.find(enc_s[i])
            pos = pos + kost[i]
            dec_s += str1[(pos ^ posilka_zap[zzz]) % 71]
            zzz += 1
        zzz = 0
    print("Расшифрованное сообщение:\n", dec_s)

# Обратное Гаммирование//////////////////////////////////////////////////////////////////////////////////////////


def GammaOBR(s):
    encrypted_message = ""
    decrypted_message = ""

    while len(s) % 8 != 0:
        randd = random.randint(0, 65)
        s2 = str1[randd]
        s = s + s2

    print("Дополненное сообщение: ", s)

    posilka = [0] * 8
    posilka_zap = [0] * 8
    for i in range(0, 8):
        posilka[i] = random.randint(0, 71)

    for i in range(0, 8):
        posilka_zap[i] = posilka[i]

    zzz = 0
    kost = [0] * 5000
    for i in range(0, 5000):
        kost[i] = 0
    dva = [0] * 16
    for i in range(0, 16):
        dva[i] = 0
    la = [0] * 8
    r = [0] * 8
    for i in range(0, 8):
        la[i] = 0
        r[i] = 0

    key = [0] * 64
    for i in range(0, 64):
        key[i] = random.randint(0, 16)

    dvadva = [0] * 32
    for i in range(0, 32):
        dvadva[i] = 0

    for j in range(0, len(s) // 8):
        j2 = j
        # НАЧАЛО СЕТИ ФЕЙСТЕЛЯ/////////////////////////////////////////////////////////////////////////////
        for i in range(0, 8):
            dva[i * 2] = posilka[i] // 16
            dva[i * 2 + 1] = posilka[i] % 16

        for ii in range(0, 8):
            la[ii] = dva[ii]
            r[ii] = dva[ii + 8]

        for h in range(0, 32):
            for i in range(0, 8):
                l_zap = la[i]
                if h < 24:
                    la[i] = la[i] ^ key[i + ((h * 8) % 64)]
                else:
                    la[i] = la[i] ^ key[56 + i - ((h * 8) % 64)]

                # Начало S-блока замены
                if i % 8 == 0:
                    if la[i] == 0:
                        la[i] = 12
                    else:
                        if la[i] == 1:
                            la[i] = 4
                        else:
                            if la[i] == 2:
                                la[i] = 6
                            else:
                                if la[i] == 3:
                                    la[i] = 2
                                else:
                                    if la[i] == 4:
                                        la[i] = 10
                                    else:
                                        if la[i] == 5:
                                            la[i] = 5
                                        else:
                                            if la[i] == 6:
                                                la[i] = 11
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 9
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 14
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 8
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 13
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 7
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 0
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 3
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 15
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 1

                if i % 8 == 1:
                    if la[i] == 0:
                        la[i] = 6
                    else:
                        if la[i] == 1:
                            la[i] = 8
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 3
                                else:
                                    if la[i] == 4:
                                        la[i] = 9
                                    else:
                                        if la[i] == 5:
                                            la[i] = 10
                                        else:
                                            if la[i] == 6:
                                                la[i] = 5
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 12
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 1
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 14
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 4
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 7
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 11
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 13
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 0
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 15

                if i % 8 == 2:
                    if la[i] == 0:
                        la[i] = 11
                    else:
                        if la[i] == 1:
                            la[i] = 3
                        else:
                            if la[i] == 2:
                                la[i] = 5
                            else:
                                if la[i] == 3:
                                    la[i] = 8
                                else:
                                    if la[i] == 4:
                                        la[i] = 2
                                    else:
                                        if la[i] == 5:
                                            la[i] = 15
                                        else:
                                            if la[i] == 6:
                                                la[i] = 10
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 13
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 14
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 1
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 7
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 4
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 12
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 9
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 6
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 0
                if i % 8 == 3:
                    if la[i] == 0:
                        la[i] = 12
                    else:
                        if la[i] == 1:
                            la[i] = 8
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 1
                                else:
                                    if la[i] == 4:
                                        la[i] = 13
                                    else:
                                        if la[i] == 5:
                                            la[i] = 4
                                        else:
                                            if la[i] == 6:
                                                la[i] = 15
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 6
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 7
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 0
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 10
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 5
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 3
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 14
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 9
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 11

                if i % 8 == 4:
                    if la[i] == 0:
                        la[i] = 7
                    else:
                        if la[i] == 1:
                            la[i] = 15
                        else:
                            if la[i] == 2:
                                la[i] = 5
                            else:
                                if la[i] == 3:
                                    la[i] = 10
                                else:
                                    if la[i] == 4:
                                        la[i] = 8
                                    else:
                                        if la[i] == 5:
                                            la[i] = 1
                                        else:
                                            if la[i] == 6:
                                                la[i] = 6
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 13
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 0
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 9
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 3
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 14
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 11
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 4
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 2
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 12
                if i % 8 == 5:
                    if la[i] == 0:
                        la[i] = 5
                    else:
                        if la[i] == 1:
                            la[i] = 13
                        else:
                            if la[i] == 2:
                                la[i] = 15
                            else:
                                if la[i] == 3:
                                    la[i] = 6
                                else:
                                    if la[i] == 4:
                                        la[i] = 9
                                    else:
                                        if la[i] == 5:
                                            la[i] = 2
                                        else:
                                            if la[i] == 6:
                                                la[i] = 12
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 10
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 11
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 7
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 8
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 1
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 4
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 3
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 14
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 0
                if i % 8 == 6:
                    if la[i] == 0:
                        la[i] = 8
                    else:
                        if la[i] == 1:
                            la[i] = 14
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 5
                                else:
                                    if la[i] == 4:
                                        la[i] = 6
                                    else:
                                        if la[i] == 5:
                                            la[i] = 9
                                        else:
                                            if la[i] == 6:
                                                la[i] = 1
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 12
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 15
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 4
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 11
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 0
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 13
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 10
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 3
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 7
                if i % 8 == 7:
                    if la[i] == 0:
                        la[i] = 1
                    else:
                        if la[i] == 1:
                            la[i] = 7
                        else:
                            if la[i] == 2:
                                la[i] = 14
                            else:
                                if la[i] == 3:
                                    la[i] = 13
                                else:
                                    if la[i] == 4:
                                        la[i] = 0
                                    else:
                                        if la[i] == 5:
                                            la[i] = 5
                                        else:
                                            if la[i] == 6:
                                                la[i] = 8
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 3
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 4
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 15
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 10
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 6
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 9
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 12
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 11
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 2
                # Конец S-блока замены

                for v in range(0, 4):
                    if la[2 * v] >= 8:
                        dvadva[0 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 8

                    if la[2 * v] >= 4:
                        dvadva[1 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 4

                    if la[2 * v] >= 2:
                        dvadva[2 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 2

                    if la[2 * v] >= 1:
                        dvadva[3 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 1

                    if la[2 * v + 1] >= 8:
                        dvadva[4 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 8

                    if la[2 * v + 1] >= 4:
                        dvadva[5 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 4

                    if la[2 * v + 1] >= 2:
                        dvadva[6 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 2

                    if la[2 * v + 1] >= 1:
                        dvadva[7 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 1

                # Сдвиг на на 11 шагов в сторону старшего разряда
                for v in range(0, 11):
                    dvadva_zam = dvadva[0]
                    for kryak in range(1, 32):
                        dvadva[kryak - 1] = dvadva[kryak]
                    dvadva[31] = dvadva_zam

                for v in range(0, 4):
                    if dvadva[0 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 8
                    if dvadva[1 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 4
                    if dvadva[2 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 2
                    if dvadva[3 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 1
                    if dvadva[4 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 8
                    if dvadva[5 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 4
                    if dvadva[6 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 2
                    if dvadva[7 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 1

                for v in range(0, 32):
                    dvadva[v] = 0

                la[i] = la[i] ^ r[i]
                r[i] = l_zap

        for i in range(0, 4):
            posilka[i] = la[i * 2] * 16 + la[i * 2 + 1]
            posilka[i + 4] = r[i * 2] * 16 + r[i * 2 + 1]
        # КОНЕЦ СЕТИ ФЕЙСТЕЛЯ

        for i in range(8 * j2, 8 + 8 * j2):
            pos = str1.find(s[i])
            xx = pos ^ posilka[zzz]
            if xx >= 71:
                kost[i] = 71
            if xx >= 142:
                kost[i] = 142
            if xx >= 213:
                kost[i] = 213
            encrypted_message += str1[(pos ^ posilka[zzz]) % 71]
            zzz += 1
        zzz = 0

    print("Зашифрованное сообщение:\n", encrypted_message)

    # РАСШИФРОВАНИЕ

    for j in range(0, len(s) // 8):
        j2 = j
        # НАЧАЛО СЕТИ ФЕЙСТЕЛЯ/////////////////////////////////////////////////////////////////////////////
        for i in range(0, 8):
            dva[i * 2] = posilka_zap[i] // 16
            dva[i * 2 + 1] = posilka_zap[i] % 16

        for ii in range(0, 8):
            la[ii] = dva[ii]
            r[ii] = dva[ii + 8]

        for h in range(0, 32):
            for i in range(0, 8):
                l_zap = la[i]
                if h < 24:
                    la[i] = la[i] ^ key[i + ((h * 8) % 64)]
                else:
                    la[i] = la[i] ^ key[56 + i - ((h * 8) % 64)]

                # Начало S-блока замены
                if i % 8 == 0:
                    if la[i] == 0:
                        la[i] = 12
                    else:
                        if la[i] == 1:
                            la[i] = 4
                        else:
                            if la[i] == 2:
                                la[i] = 6
                            else:
                                if la[i] == 3:
                                    la[i] = 2
                                else:
                                    if la[i] == 4:
                                        la[i] = 10
                                    else:
                                        if la[i] == 5:
                                            la[i] = 5
                                        else:
                                            if la[i] == 6:
                                                la[i] = 11
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 9
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 14
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 8
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 13
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 7
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 0
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 3
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 15
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 1

                if i % 8 == 1:
                    if la[i] == 0:
                        la[i] = 6
                    else:
                        if la[i] == 1:
                            la[i] = 8
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 3
                                else:
                                    if la[i] == 4:
                                        la[i] = 9
                                    else:
                                        if la[i] == 5:
                                            la[i] = 10
                                        else:
                                            if la[i] == 6:
                                                la[i] = 5
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 12
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 1
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 14
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 4
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 7
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 11
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 13
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 0
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 15

                if i % 8 == 2:
                    if la[i] == 0:
                        la[i] = 11
                    else:
                        if la[i] == 1:
                            la[i] = 3
                        else:
                            if la[i] == 2:
                                la[i] = 5
                            else:
                                if la[i] == 3:
                                    la[i] = 8
                                else:
                                    if la[i] == 4:
                                        la[i] = 2
                                    else:
                                        if la[i] == 5:
                                            la[i] = 15
                                        else:
                                            if la[i] == 6:
                                                la[i] = 10
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 13
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 14
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 1
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 7
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 4
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 12
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 9
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 6
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 0
                if i % 8 == 3:
                    if la[i] == 0:
                        la[i] = 12
                    else:
                        if la[i] == 1:
                            la[i] = 8
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 1
                                else:
                                    if la[i] == 4:
                                        la[i] = 13
                                    else:
                                        if la[i] == 5:
                                            la[i] = 4
                                        else:
                                            if la[i] == 6:
                                                la[i] = 15
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 6
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 7
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 0
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 10
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 5
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 3
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 14
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 9
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 11

                if i % 8 == 4:
                    if la[i] == 0:
                        la[i] = 7
                    else:
                        if la[i] == 1:
                            la[i] = 15
                        else:
                            if la[i] == 2:
                                la[i] = 5
                            else:
                                if la[i] == 3:
                                    la[i] = 10
                                else:
                                    if la[i] == 4:
                                        la[i] = 8
                                    else:
                                        if la[i] == 5:
                                            la[i] = 1
                                        else:
                                            if la[i] == 6:
                                                la[i] = 6
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 13
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 0
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 9
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 3
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 14
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 11
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 4
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 2
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 12
                if i % 8 == 5:
                    if la[i] == 0:
                        la[i] = 5
                    else:
                        if la[i] == 1:
                            la[i] = 13
                        else:
                            if la[i] == 2:
                                la[i] = 15
                            else:
                                if la[i] == 3:
                                    la[i] = 6
                                else:
                                    if la[i] == 4:
                                        la[i] = 9
                                    else:
                                        if la[i] == 5:
                                            la[i] = 2
                                        else:
                                            if la[i] == 6:
                                                la[i] = 12
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 10
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 11
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 7
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 8
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 1
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 4
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 3
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 14
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 0
                if i % 8 == 6:
                    if la[i] == 0:
                        la[i] = 8
                    else:
                        if la[i] == 1:
                            la[i] = 14
                        else:
                            if la[i] == 2:
                                la[i] = 2
                            else:
                                if la[i] == 3:
                                    la[i] = 5
                                else:
                                    if la[i] == 4:
                                        la[i] = 6
                                    else:
                                        if la[i] == 5:
                                            la[i] = 9
                                        else:
                                            if la[i] == 6:
                                                la[i] = 1
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 12
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 15
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 4
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 11
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 0
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 13
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 10
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 3
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 7
                if i % 8 == 7:
                    if la[i] == 0:
                        la[i] = 1
                    else:
                        if la[i] == 1:
                            la[i] = 7
                        else:
                            if la[i] == 2:
                                la[i] = 14
                            else:
                                if la[i] == 3:
                                    la[i] = 13
                                else:
                                    if la[i] == 4:
                                        la[i] = 0
                                    else:
                                        if la[i] == 5:
                                            la[i] = 5
                                        else:
                                            if la[i] == 6:
                                                la[i] = 8
                                            else:
                                                if la[i] == 7:
                                                    la[i] = 3
                                                else:
                                                    if la[i] == 8:
                                                        la[i] = 4
                                                    else:
                                                        if la[i] == 9:
                                                            la[i] = 15
                                                        else:
                                                            if la[i] == 10:
                                                                la[i] = 10
                                                            else:
                                                                if la[i] == 11:
                                                                    la[i] = 6
                                                                else:
                                                                    if la[i] == 12:
                                                                        la[i] = 9
                                                                    else:
                                                                        if la[i] == 13:
                                                                            la[i] = 12
                                                                        else:
                                                                            if la[i] == 14:
                                                                                la[i] = 11
                                                                            else:
                                                                                if la[i] == 15:
                                                                                    la[i] = 2
                # Конец S-блока замены

                for v in range(0, 4):
                    if la[2 * v] >= 8:
                        dvadva[0 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 8

                    if la[2 * v] >= 4:
                        dvadva[1 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 4

                    if la[2 * v] >= 2:
                        dvadva[2 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 2

                    if la[2 * v] >= 1:
                        dvadva[3 + 8 * v] = 1
                        la[2 * v] = la[2 * v] - 1

                    if la[2 * v + 1] >= 8:
                        dvadva[4 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 8

                    if la[2 * v + 1] >= 4:
                        dvadva[5 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 4

                    if la[2 * v + 1] >= 2:
                        dvadva[6 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 2

                    if la[2 * v + 1] >= 1:
                        dvadva[7 + 8 * v] = 1
                        la[2 * v + 1] = la[2 * v + 1] - 1

                # Сдвиг на на 11 шагов в сторону старшего разряда
                for v in range(0, 11):
                    dvadva_zam = dvadva[0]
                    for j in range(1, 32):
                        dvadva[j - 1] = dvadva[j]
                    dvadva[31] = dvadva_zam

                for v in range(0, 4):
                    if dvadva[0 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 8
                    if dvadva[1 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 4
                    if dvadva[2 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 2
                    if dvadva[3 + 8 * v] == 1:
                        la[2 * v] = la[2 * v] + 1
                    if dvadva[4 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 8
                    if dvadva[5 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 4
                    if dvadva[6 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 2
                    if dvadva[7 + 8 * v] == 1:
                        la[2 * v + 1] = la[2 * v + 1] + 1

                for v in range(0, 32):
                    dvadva[v] = 0

                la[i] = la[i] ^ r[i]
                r[i] = l_zap

        for i in range(0, 4):
            posilka_zap[i] = la[i * 2] * 16 + la[i * 2 + 1]
            posilka_zap[i + 4] = r[i * 2] * 16 + r[i * 2 + 1]
        # КОНЕЦ СЕТИ ФЕЙСТЕЛЯ

        for i in range(8 * j2, 8 + 8 * j2):
            pos = str1.find(encrypted_message[i])
            pos = pos + kost[i]
            decrypted_message += str1[(pos ^ posilka_zap[zzz]) % 71]
            zzz += 1
        zzz = 0

    print("Расшифрованное сообщение:\n", decrypted_message)


while True:
    message = input("Введите сообщение:\n")   # ввод сообщения
    vibor = int(input(
        "Введите номер нужного режима:\n1. Простая замена\n2. Гаммирование\n3. Гаммирование с обратной связью\n4. Имитовставка\n"))
    if vibor == 1:
        prZamena(message)
    if vibor == 2:
        Gamma(message)
    if vibor == 3:
        GammaOBR(message)
    if vibor == 4:
        imitovstavka(message)
