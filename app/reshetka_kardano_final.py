import random
import numpy as np

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
    return (message)


def get_alfa():
    alphabet_lower = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4,
                      'е': 5, 'ж': 6, 'з': 7, 'и': 8, 'й': 9,
                      'к': 10, 'л': 11, 'м': 12, 'н': 13, 'о': 14,
                      'п': 15, 'р': 16, 'с': 17, 'т': 18, 'у': 19,
                      'ф': 20, 'х': 21, 'ц': 22, 'ч': 23, 'ш': 24,
                      'щ': 25, 'ъ': 26, 'ы': 27, 'ь': 28, 'э': 29,
                      'ю': 30, 'я': 31, ".": 34}
    return alphabet_lower


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def reshetka_kardano(SIZE, text, mode, key =[]):
    matrix_number = 1
    alfa = get_alfa()
    # дополняем матрицу с текстом до полной матрицы
    open_text_ = text
    if len(text) % (SIZE * SIZE) != 0:
        add_number = SIZE * SIZE - len(text) % (SIZE * SIZE)
        for i in range(add_number):
            text = text + get_key(alfa, random.randint(0, 31))
    # определяем количество матриц
    if len(text) / (SIZE * SIZE) != 1:
        matrix_number = int(len(text) / (SIZE * SIZE))
    # print(" Введите значения ячеек решётки Кардано (0 - заполнена, 1 - пустота):\n")

    # формируем решётку Кардано
    bin_matrix = [[0 for x in range(SIZE)] for y in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            # рандомизируем ячейки матрицы, либо 1, либо 0
            bin_matrix90 = np.rot90(bin_matrix, k=1)
            bin_matrix180 = np.rot90(bin_matrix, k=2)
            bin_matrix270 = np.rot90(bin_matrix, k=3)
            bin_matrix[i][j] = random.randint(0, 1)
            if bin_matrix[i][j] == 1:
                while (bin_matrix[i][j] == bin_matrix90[i][j]) and (bin_matrix[i][j] == bin_matrix180[i][j]) and (bin_matrix[i][j] == bin_matrix270[i][j]):
                    bin_matrix[i][j] = random.randint(0, 1)
            
    # формируем матрицу с текстом
    text_matrix = [[[0 for x in range(SIZE)] for y in range(
        SIZE)] for matrix in range(matrix_number)]
    counter_text = 0  # счётчик позиции символа в тексте
    for i in range(matrix_number):
        for j in range(SIZE):
            for k in range(SIZE):
                text_matrix[i][j][k] = text[counter_text]
                counter_text += 1
    if mode == 0:
        # шифрование
        # SIZE - размерность матрицы, z - номер матрицы с текстом, i - строка (Y), j - столбец (X).
        enc_text = ""
        for z in range(matrix_number):
            # прямой обход решетки
            for i in range(SIZE):
                for j in range(SIZE):
                    if bin_matrix[i][j] == 1:
                        enc_text = enc_text + text_matrix[z][i][j]
            # поворот решетки на 90 градусов по часовой стрелке
            for i in range(SIZE):
                for j in range(SIZE):
                    if bin_matrix[SIZE - j - 1][i] == 1:
                        enc_text = enc_text + text_matrix[z][i][j]
            # поворот решетки на 180 градусов по часовой стрелке
            for i in range(SIZE):
                for j in range(SIZE):
                    if bin_matrix[SIZE - i - 1][SIZE - j - 1] == 1:
                        enc_text = enc_text + text_matrix[z][i][j]
            # поворот решетки на 270 градусов по часовой стрелке
            for i in range(SIZE):
                for j in range(SIZE):
                    if bin_matrix[j][SIZE - i - 1] == 1:
                        enc_text = enc_text + text_matrix[z][i][j]
        encrypted_text = str((" {}\n".format(enc_text)))
        key = bin_matrix
        return key, encrypted_text
    # расшифрование
    # формируем матрицу с текстом
    if mode == 1:
        key = str(key)
        key =key.replace('[', '')
        key =key.replace(']', '')
        key = key.replace(',', '')
        key = key.split(' ')
        bin_matrix = [key[i:i + SIZE]
                      for i in range(0, len(key), SIZE)]
        text_matrix = [[[0 for x in range(SIZE)] for y in range(
            SIZE)] for matrix in range(matrix_number)]
        counter_text = 0  # счётчик позиции символа в тексте
        print(bin_matrix)
        print(type(bin_matrix))
        for i in range(matrix_number):
            for j in range(SIZE):
                for k in range(SIZE):
                    text_matrix[i][j][k] = text[counter_text]
                    counter_text += 1
        open_text = ""
        for z in range(matrix_number):
            # прямой обход решетки
            for i in range(SIZE):
                for j in range(SIZE):
                    if bin_matrix[i][j] == 1:
                        open_text = open_text + text_matrix[z][i][j]
            # поворот решетки на 90 градусов по часовой стрелке
            for i in range(SIZE):
                for j in range(SIZE):
                    if bin_matrix[SIZE - j - 1][i] == 1:
                        open_text = open_text + text_matrix[z][i][j]
            # поворот решетки на 180 градусов по часовой стрелке
            for i in range(SIZE):
                for j in range(SIZE):
                    if bin_matrix[SIZE - i - 1][SIZE - j - 1] == 1:
                        open_text = open_text + text_matrix[z][i][j]
            # поворот решетки на 270 градусов по часовой стрелке
            for i in range(SIZE):
                for j in range(SIZE):
                    if bin_matrix[j][SIZE - i - 1] == 1:
                        open_text = open_text + text_matrix[z][i][j]
        decrypted_text = str(" {}\n".format(open_text_))
        return 0, decrypted_text


"""size = int(input(" Введите размер матрицы (одно число): "))  # вводим размер матрицы XxY
text = input(" Введите текст: ")  # вводим текст
otvet = reshetka_kardano(size, text)
print(otvet[0], otvet[1]) """


def main(message, mode, file, key=[]):
    if file:
        name = message
        f = open(message)
        message = f.read()
    message = preprocessing(message)
    for i in range(0, 1000):
        if len(message) < i * i or len(message) == i * i:
            SIZE = i
            break 
    key, newstr = reshetka_kardano( SIZE, message, mode, key)
    return (key, newstr)
    f = open('key.txt', 'w')
    f.write(str(key))

    if file:
        f = open('crypt'+name, 'w')
        f.write(newstr)


if __name__ == '__main__':
    from sys import argv
    # name, mode, file, shift, message = argv
    name, mode, file, message = '1', 0, True, '1000char.txt'
    main(message, mode, file)
