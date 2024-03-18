#LR1 Z1
def z1():
    try:
        word=str(input("Введите слово: "))
        if (len(word) == 0):
            print("Вы ничего не ввели")
        else:
            symbol = str(input("Введите символ: "))
            counter = 0
            for i in range(len(word)):
                if symbol == word[i]:
                    print(i + 1)
                    counter = counter + 1
            print("Всего символов: ", counter)
    except ValueError as e:
        print("Ошибка:", e)


#LR1 Z2 fibonacci

def z2():
    try:
        number = int(input("Введите количество в последовательности: "))
        last = 1
        prelast = 0
        sum = 0
        if(number == 0):
            print("Число не может быть меньше 1")
        if(number > 0):
            print(0)
        if(number > 1):
            print(1)
            for i in range(number - 2):
                sum = prelast + last
                prelast = last
                last = sum
                print(last)
    except ValueError as e:
        print("Ошибка:", e)

# LR1 Z3 factorial
def z3():
    try:
        number = int(input("Введите число: "))
        factorial = 1
        for i in range(1, number + 1):
            factorial = factorial * i
            print(factorial)
    except ValueError as e:
        print("Ошибка:", e)

# LR1 Z4 1
def z4():
    try:
        number1 = int(input("Введите число в десятичной записи: "))
        number = number1
        counter = 0
        num = ""
        while number >= 1:
            if number % 2 == 1:
                counter += 1
            num += str(number % 2)
            number //= 2
        num_s = num[::-1]
        print("Число в двоичной записи:", num_s)
        print(counter, "единиц(-ы) в двоичной записи числа", number1)
    except ValueError as e:
        print("Ошибка:", e)

# LR1 Z5 calculator
def z5():
    try:
        action = input("Введите выполняемое действие (+, -, /, *):")
        if action == "+":
            n1 = int(input("Введите первое слагаемое:"))
            n2 = int(input("Введите второе слагаемое:"))
            print("Результат:", n1 + n2)
        if action == "-":
            n1 = int(input("Введите уменьшаемое:"))
            n2 = int(input("Введите вычитаемое:"))
            print(n1 - n2)
        if action == "/":
            n1 = int(input("Введите делимое:"))
            n2 = int(input("Введите делитель:"))
            print(n1 / n2)
        if action == "*":
            n1 = int(input("Введите первый множитель:"))
            n2 = int(input("Введите второй множитель:"))
            print(n1 * n2)
    except ValueError as e:
        print("Ошибка:", e)


while True:
    z = input("Введите номер задания (z1 - z5):")
    if z == "exit":
        exit()
    elif z == "z1":
        z1()
    elif z == "z2":
        z2()
    elif z == "z3":
        z3()
    elif z == "z4":
        z4()
    elif z == "z5":
        z5()
    else:
        print("Номер задания введен некорректно")