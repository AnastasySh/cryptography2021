def alfa():
    alphabet_lower = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4,
                      'е': 5, 'ж': 6, 'з': 7, 'и': 8, 'й': 9,
                      'к': 10, 'л': 11, 'м': 12, 'н': 13, 'о': 14,
                      'п': 15, 'р': 16, 'с': 17, 'т': 18, 'у': 19,
                      'ф': 20, 'х': 21, 'ц': 22, 'ч': 23, 'ш': 24,
                      'щ': 25, 'ъ': 26, 'ы': 27, 'ь': 28, 'э': 29,
                      'ю': 30, 'я': 31, ".": 34}
    return alphabet_lower


def preprocessing(message):
    message = message.replace('\n', '')
    message = message.replace('-', '')
    message = message.replace('?', '')
    message = message.replace('+', '')
    message = message.replace('=', '')
    message = message.replace(' ', '')
    message = message.replace(',', 'зпт')
    message = message.replace('.', 'тчк')
    message = message.lower()
    return(message)


def sortRow(keylen, badlist):
    encrypted_matrix = []
    k = keylen - 1
    while k > 0:
        ind = 0
        # находит порядковый номер самого большого индеса (самую старшую букву)
        for j in range(k + 1):
            if badlist[0][j] > badlist[0][ind]:
                ind = j  # '''если буквы одинаковые, то он берет первый столбец по порядку то есть столбцы будут идти как 3-2-1'''
        for i in range(len(badlist)):  # передвигает весь столбец на позицию k (в конец перед отсортированным)
            m = badlist[i][ind]
            badlist[i][ind] = badlist[i][k]
            badlist[i][k] = m
        k -= 1
    for i in range(len(badlist)):
        for j in range(keylen):
            print("%4d" % badlist[i][j], end='')
            encrypted_matrix.append(badlist[i][j])
        print()
    return encrypted_matrix


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def sortRowDec(key, empty_col, badlist):
    keylen = len(key)
    pure_key = list(key)
    k = keylen - 1
    key = list(key)
    # сортировка ключа
    while k > 0:
        ind = 0
        for j in range(k + 1):
            if key[j] > key[ind]:
                ind = j
        # смена местами
        m = key[ind]
        key[ind] = key[k]
        key[k] = m
        k -= 1
    # вставка символов
    row = len(badlist) // keylen
    if len(badlist) % keylen > 0:
        row += 1
    newlist = [['' for i in range(0, keylen)] for i in range(0, row)]

    key_tmp = key.copy()
    for val in empty_col:
        ind = key_tmp.index(val)
        newlist[row - 1][ind] = '.'
        key_tmp[ind] = '.'
    k = 0
    l = 0
    for i in range(row):
        for j in range(keylen):
            if newlist[i-1][j] != '.':
                newlist[i-1][j] = badlist[l]
                l += 1
                k = k + 1
    # распаковка листов и запихивание в новый
    buff = [*key]
    for stroka in newlist:
        for char in stroka:
            buff.append(char)
    newlist = [buff[i:i+keylen]
               for i in range(0, len(buff), keylen)]
    print(newlist)
    # перестановка столбцов по ключу

    bufflist = [['' for i in range(0, keylen)] for i in range(
        0, row + 1)]  # еще один новый пустой масcив
    # копия чистого ключа в котором будем отмечать переставленное
    pure_key_copy = pure_key.copy()
    for j in pure_key:
        ind = pure_key_copy.index(j)
        if key.count(j) != 1:  # если вхождений букв больше чем одно
            bf = 0
            start = 0
            # ищем последнее вхождение буквы (индекс)
            start = 0
            while j in key[start:keylen]:
                bf = key.index(j, start, keylen)
                start = bf + 1
                if start == keylen:  # проверка, т.к. когда старт и стоп одно число - валятся ошибки
                    break
            durty_ind = bf
        else:
            durty_ind = key.index(j)
        # ставит весь столбец на позицию
        for i in range(len(newlist)):
            bufflist[i][ind] = newlist[i][durty_ind]
        pure_key_copy[ind] = '.'
        key[durty_ind] = '.'
    return bufflist


def encrypt(key, msg):
    alphabet_lower = alfa()
    key_len = len(key)
    row = len(message) // len(key)
    if len(message) % len(key) > 0:
        row += 1
    print("Длина ключа:", key_len)
    if len(msg) % key_len != 0:
        empty_col_num = key_len - (len(msg) % key_len)
    else:
        empty_col_num = 0
    print("Количество неполных столбцов:", empty_col_num)
    if row % 2 == 0:
        empty_col = key[:empty_col_num]
    else:
        empty_col = key[len(key) - empty_col_num:]

    print(empty_col)
    list_msg = list(msg)
    decrypted_matrix = sortRowDec(key, empty_col, list_msg)
    newstr = ''
    for i in range(1, len(decrypted_matrix)):
        if i % 2 != 0:
            for j in range(0, len(decrypted_matrix[i])):
                newstr += decrypted_matrix[i][j]
        else:
            for j in range(len(decrypted_matrix[i])-1, -1, - 1):
                newstr += decrypted_matrix[i][j]
    newstr = newstr.replace('.', '')
    print("\nРасшифровка:")
    return newstr


def crypt(key, msg):
    alphabet_lower = alfa()
    key_len = len(key)
    print("Длина ключа:", key_len)
    # добавление символов пока сообщение не станет кратно длине ключа
    print("Длина фразы до добавления символов:", len(msg))
    while len(msg) % key_len != 0:
        msg += '.'
    print("Длина фразы после добавления символов:", len(msg))
    # преобразование ключа + сообщения в массив
    msg_pl_key = key + msg
    list_msg = list(msg_pl_key)
    split_msg = [list_msg[i:i + key_len]
                 for i in range(0, len(list_msg), key_len)]
    buff = []
    for i in range(0, len(split_msg)):
        if i == 0:
            buff.append(split_msg[i])
            continue
        if i % 2 == 1:
            buff.append(split_msg[i])
        else:
            row_buff = []
            for char in reversed(split_msg[i]):
                row_buff.append(char)
            buff.append(row_buff)
    # вывод матрицы на экран
    split_msg = buff
    for i in range(len(split_msg)):
        for j in range(len(split_msg[i])):
            print(split_msg[i][j], end=" ")
        print()
    coded = list()
    # переделывание букв в числа (порядковые по нашему словарю)
    for i in range(len(split_msg)):
        for j in range(len(split_msg[i])):
            print(int(alphabet_lower.get(split_msg[i][j])), end=" ")
            coded.append(int(alphabet_lower.get(split_msg[i][j])))
        print()
    split_coded = [coded[i:i + key_len] for i in range(0, len(coded), key_len)]
    # сортировка ключа и шифрование таблицы
    encrypted_matrix = list()
    print("\nЗашифрованная матрица: ")
    encrypted_matrix = sortRow(key_len, split_coded)
    print("\nЗашифрованная матрица в буквах: ")
    encrypted_matrix = sortRow(key_len, split_coded)
    split_encrypted = [encrypted_matrix[i:i + key_len]
                       for i in range(0, len(encrypted_matrix), key_len)]

    for i in range(0, len(split_encrypted)):
        for j in range(0, len(split_encrypted[1])):
            print(get_key(alphabet_lower, split_encrypted[i][j]), end=' ')
        print()
    print("\nЗашифрованный текст: ")
    newstr = ''
    for i in range(0, len(split_encrypted[0])):
        for j in range(1, len(split_encrypted)):
            newstr += get_key(alphabet_lower, split_encrypted[j][i])
    newstr = newstr.replace('.', '')
    return newstr


def main(Key, Message, mode, file):
    global message
    message = Message
    global key
    key = Key
    if file:
        name = message
        f = open(message)
        message = f.read()

    message = preprocessing(message)
    if mode == 0:
        newstr = crypt(key, message)
        return(newstr)
    else:
        newstr = encrypt(key, message)
        return(newstr)

    print(newstr)
    if file:
        f = open('crypt'+name, 'w')
        f.write(newstr)


if __name__ == '__main__':
    from sys import argv
    # name, mode, file, shift, message = argv
    name, mode, file, key, message = '1', 1, False, 'алла', 'ос'
    main(key, message, mode, file)
