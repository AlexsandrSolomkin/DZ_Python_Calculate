# Вычислить значение выражения

# Уровень 1:
# 1 действие
# 2 аргумента 12 + 15
# Уровень 2:
# Количество действий произвольное
# 12 + 15 - 4

# Уровень 3:
# Действия имеют приоритет
# 12 - 4*2 +6/3

# Уровень 4 * (дополнительная задача, сдавать не обязательно)
# Действия разделяются скобками
# (12 - 4) * 2

# =============================================================================

# Решение:

# n = "22 * 300 - 14 + 10 * 10"
# m = n.split()
# m2 = []


def print_result(start_exp: str, result: float):

    print(start_exp, result, sep=" = ")


def calc_lvl_1(a: float, b: float, ch: str) -> float:

    if ch == "+":
        return a + b
    elif ch == "-":
        return a - b
    elif ch == "/":
        return a / b
    elif ch == "*":
        return a * b


def calc_lvl_3(data_l: list) -> float:
    res = 0

    while ("*" in data_l) or ("/" in data_l):
        for i in range(1, len(data_l) - 1):
            if ("*" in data_l) or ("/" in data_l):
                if ("*" == data_l[i]) or ("/" == data_l[i]):
                    
                    res = calc_lvl_1(
                    float(data_l[i - 1]),
                    float(data_l[i + 1]),
                    data_l[i])

                    del data_l[i + 1]
                    del data_l[i]
                    del data_l[i - 1]
                    data_l.insert(i - 1, res)
                    print(data_l)

                    break

    while ("+" in data_l) or ("-" in data_l):
        for i in range(1, len(data_l) - 1):
            if ("+" in data_l) or ("-" in data_l):
                if ("+" == data_l[i]) or ("-" == data_l[i]):
                    
                    res = calc_lvl_1(
                    float(data_l[i - 1]),
                    float(data_l[i + 1]),
                    data_l[i])

                    del data_l[i + 1]
                    del data_l[i]
                    del data_l[i - 1]
                    data_l.insert(i - 1, res)
                    print(data_l)

                    break

    return res

exp = input("Пример ввода: 22 * 300 - 14 + 10 * 10\nВведите выражение: ")

m = exp.split()

if len(m) == 3:

    test_1 = calc_lvl_1(float(m[0]), float(m[2]), m[1])
    print_result(exp, test_1)

elif (len(m) > 3) and ("(" not in exp) and (")" not in exp):

    test_3 = calc_lvl_3(m)
    print_result(exp, test_3)

# =============================================================================
