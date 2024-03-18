# LR2 z1
nums = []
def z1():
    try:
        while True:
            n1 = input("Введите число для добавления в список (прекратить ввод - stop): ")
            if n1 == "stop":
                break
            else:
                nums.append(int(n1))
        for i in range(0, len(nums)):
            print(nums[i])
        sum = 0
        mp = 1
        for i in range(len(nums)):
            sum += nums[i]
            mp *= nums[i]
        print("Сумма:", sum, "Произведение:", mp)
    except ValueError as e:
        print("e")
    finally:
        nums.clear()

# LR2 z2
def z2():
    try:
        while True:
            n1 = input("Введите число для добавления в список (прекратить ввод - stop): ")
            if n1 == "stop":
                break
            else:
                nums.append(n1)
        for i in range(0, len(nums)):
            print(nums[i])
        b = 0
        for i in range(len(nums)):
            if b < nums[i]:
                b = nums[i]
        print("Наибольший элемент:", b)
    except ValueError as e:
        print("e")
    finally:
        nums.clear()

# LR2 Z3
# 20 30 50 50 100
#
def z3():
    try:
        while True:
            n1 = input("Введите число для добавления в список (прекратить ввод - stop): ")
            if n1 == "stop":
                break
            else:
                nums.append(int(n1))

        a = 0

        while a < len(nums):
            r = nums[a]
            counter = 0
            for i in range(0, len(nums)):
                if r == nums[i]:
                    counter += 1
            if counter > 1:
                print("Число", r, "повторяется", counter, "раз(-а)")
                a += counter
            a += 1
    except ValueError as e:
        print("e")
    finally:
        nums.clear()

#LR 2 Z4
def z4():
    try:
        while True:
            n1 = input("Введите число для добавления в список (прекратить ввод - stop): ")
            if n1 == "stop":
                break
            else:
                nums.append(int(n1))
        print("Введенный список:")
        print(nums)
        print("-------")

        biggest = nums[0]
        biggest_index = 0
        smallest = nums[0]
        smallest_index = 0
        for i in range(0, len(nums)):
            if nums[i] > biggest:
                biggest = nums[i]
                biggest_index = i
            if nums[i] < smallest:
                smallest = nums[i]
                smallest_index = i
    # list.insert(nums, biggest_index, smallest)
    # list.pop(nums, biggest_index + 1)
    # list.insert(smallest_index, biggest)
    # list.pop(nums, smallest_index + 1)
        nums[biggest_index], nums[smallest_index] = nums[smallest_index], biggest

        print("Обновленный список:")
        print(nums)
    except ValueError as e:
        print("e")

    finally:
        nums.clear()

# LR 2 z5
# if мин1 + мин2 >= макс -> оставляем всех
# иначе удаляем мин1 и проверяем заново до тех пор, пока мин1+мин2>=макс


def z5():
    try:
        while True:
            n1 = input("Введите ПП для каждого игрока (прекратить ввод - stop): ")
            if n1 == "stop":
                break
            else:
                nums.append(int(n1))
        print("Все игроки:")
        print(nums)
        print("-------")
        list.sort(nums)
        # print("сортировка")
        # print(nums)

        # сортируем массив по возрастанию
        # берем двух с минимальным пп
        # 20 80 85 89 90 95 100 400 500
        # 20 80 85 89 90 95 100
        # сравниваем их, начиная с максимального
        # в момент, когда найдется игрок с пп <=, прекращаем сравнение
        # получаем новый массив
        dreamteam = [nums[0], nums[1]]
        for i in range(2, len(nums) - 1):
            if nums[0] + nums[1] >= nums[i]:
                dreamteam.insert(i, nums[i])
        print("Команда с лучшей сыгранностью:")
        print(dreamteam)
    except ValueError as e:
        print("e")
    finally:
        nums.clear()

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