# Открытые числа
#p = int(input("Введите простое число N: "))
#g = int(input("Введите натуральное число A: "))
def main(p,g,ka,kb):
    if g >= p:
        return("число A должно быть меньше N")
        

    # Секретное число
    #ka = int(input("Введите натуральное (секретное) число пользователя 1 - kа: "))
    if 1 > ka or ka > p:
        return("число ka должно быть в интервале (2,..., n-1)")
        

    # a = 41
    #kb = int(input("Введите натуральное (секретное) число пользователя 2 - kb: "))
    if 1 > kb or kb > p:
        return("число kb должно быть в интервале (2,..., n-1)")
        
    # b = 12
    if ka == kb:
        return("число ka не может быть равно kb")
    # Открытый ключ
    YA = g**ka % p
    YB = g**kb % p
    print("Открытый ключ пользователя 1: ", YA,
        "\nОткрытый ключ пользователя 2: ", YB)
    Y = [YA, YB]
    # Секретный ключ
    K1 = YB**ka % p
    K2 = YA**kb % p
    print("Приватный ключ пользователя 1: ", K1,
        "\nПриватный ключ пользователя 2: ", K2)
    K = [K1,K2]
    return K1

    