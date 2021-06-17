from re import findall  # подключение регулярочек


def getAlfa():
    alpha = tuple("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
    return alpha


def preprocessing(message):
    message = message.replace('\n', '')
    message = message.replace('-', '')
    message = message.replace('?', '')
    message = message.replace('+', '')
    message = message.replace('=', '')
    message = message.replace(' ', '')
    message = message.replace(',', 'зпт')
    message = message.replace('.', 'тчк')
    message = message.upper()
    return message


# Проверка условий на ошибки
def checkErrors(key, MatrixMod):
    if len(key) != 3 or len(key[0]) != 3 and len(key[1]) != 3 and len(key[2]) != 3:
        return "размерность матрицы не 3х3. выберите другую матрицу."
    if not getDeter((key)):
        return "Определитель матрицы равен 0. выберите другую матрицу."
    elif not getDeter(key) % MatrixMod:
        # det(Key) mod len(alpha) = 0
        return "Определитель матрицы mod длина алфавита = 0. выберите другую матрицу."
    else:
        return None


# Регулярное выражение - 3 символа сообщения
def regular(text, MatrixLength):
    template = r".{%d}" % MatrixLength
    return findall(template, text)


# Кодирование символов в матрице
def encode(matrix, alpha, MatrixLength):
    for x in range(len(matrix)):
        for y in range(MatrixLength):
            matrix[x][y] = alpha.index(matrix[x][y])+1
    return matrix


# Декодирование чисел в матрице + шифрование/расшифрование
def decode(alpha, matrixM, matrixK, MatrixLength, MatrixMod, message=""):
    matrixF = []
    for z in range(len(matrixM)):
        temp = [0 for _ in range(MatrixLength)]
        for x in range(MatrixLength):
            for y in range(MatrixLength):
                temp[x] += matrixK[x][y] * matrixM[z][y]
            if mode == 1:
                temp[x] = alpha[(round(temp[x]) % MatrixMod)-1]
        matrixF.append(temp)
    for string in matrixF:
        message += "".join(str(string))
    return message


# Создаёт матрицу по три символа
def sliceto(text, alfa, MatrixLength):
    matrix = []
    for three in regular(text, MatrixLength):
        matrix.append(list(three))
    return encode(matrix, alfa, MatrixLength)


# Нахождение обратного определителя матрицы
def iDet(det):
    return (1/det)


# Алгебраические дополнения
def algebratic(key, x, y, alfa, MatrixMod):
    matrix = keyToMatrix(key)
    matrix.remove(matrix[x])
    for z in range(2):
        matrix[z].remove(matrix[z][y])
    det2x2 = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return (pow(-1, (x + 1) + (y + 1)) * det2x2)


# iDet(det, MatrixMod) % MatrixMod
#
#
# Получение определителя матрицы
def getDeter(matrix):
    return \
        (matrix[0][0] * matrix[1][1] * matrix[2][2]) + \
        (matrix[0][1] * matrix[1][2] * matrix[2][0]) + \
        (matrix[1][0] * matrix[2][1] * matrix[0][2]) - \
        (matrix[0][2] * matrix[1][1] * matrix[2][0]) - \
        (matrix[0][1] * matrix[1][0] * matrix[2][2]) - \
        (matrix[1][2] * matrix[2][1] * matrix[0][0])


# Получение алгебраических дополнений
def getAlgbr(det, alfa, MatrixLength, MatrixSquare, MatrixMod, index=0):
    algbrs = [0 for _ in range(MatrixSquare)]
    for string in range(MatrixLength):
        for column in range(MatrixLength):
            algbrs[index] = algebratic(
                key, string, column, alfa, MatrixMod)
            index += 1
    return algbrs


# Получение обратной матрицы
def getIMatr(algbr, det):
    return [
        [algbr[0]/det, algbr[3]/det, algbr[6]/det],
        [algbr[1]/det, algbr[4]/det, algbr[7]/det],
        [algbr[2]/det, algbr[5]/det, algbr[8]/det]
    ]

# Основная функция


def encryptDecrypt(mode, message, key, alfa, MatrixLength, MatrixMod, MatrixSquare):
    if mode==0:
        MatrixMessage = sliceto(message, alfa, MatrixLength)
        final = decode(alfa, MatrixMessage, key, MatrixLength, MatrixMod)
    else:
        MatrixMessage = keyToMatrix(message)
        opr = getDeter(key)
        algbr = getAlgbr(opr, alfa, MatrixLength,
                         MatrixSquare, MatrixMod)
        final = decode(alfa, MatrixMessage, getIMatr(
            algbr, opr),  MatrixLength, MatrixMod)
    return final

# перевод ключа в матрицу


def keyToMatrix(key):
    key = key.replace('[', '')
    key = key.replace(']', '')
    key = key.replace(',', '')
    key = key.split(' ')
    print('!!!')
    print(key)
    newkey = []
    for i, char in enumerate(key):
        if i % 3 == 0:
            buff = []
            buff.append(int(key[i]))
            buff.append(int(key[i + 1]))
            buff.append(int(key[i + 2]))
            newkey.append(buff)
    return newkey


def main(Mode, file, Text, Key):
    global mode
    mode = Mode
    global key
    key = Key
    global text
    text = Text
    alpha = getAlfa()
    MatrixLength = 3
    MatrixMod = len(alpha)
    MatrixSquare = MatrixLength * MatrixLength

    if file:
        name = text
        f = open(text)
        text = f.read()

    mainKey = keyToMatrix(key)

    if mode == 0:
        startMessage = preprocessing(text)
        if checkErrors(mainKey, MatrixMod):
            print(checkErrors(mainKey, MatrixMod))
            raise SystemExit
    # добавление в конец символа
        while len(startMessage) % MatrixLength != 0:
            startMessage += startMessage[-1]
    else:
        startMessage = text
    newstr = encryptDecrypt(
        mode, startMessage, mainKey, alpha, MatrixLength, MatrixMod, MatrixSquare)
    return(newstr)
    if file:
        f = open('crypt'+name, 'w')
        f.write(newstr)


if __name__ == '__main__':
    from sys import argv
    from sys import exit
    #name, mode, file, text = argv
    name, mode, key, file, text = 1, 1, '1 4 8 3 7 2 6 9 5', False, 'забава'
    main(mode, file, text, key)
