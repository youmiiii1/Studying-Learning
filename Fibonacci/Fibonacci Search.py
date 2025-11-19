def fibonacci_search(lst, target):
    n = len(lst)                                # В переменную "n", кладём размер всего списка
    fbm1 = 1                                    # Базовое число Фибоначчи - 1
    fbm0 = 0                                    # Базовое число Фибоначчи - 0
    fbm = fbm1 + fbm0                           # Сумма двух предыдущих чисел Фибоначчи - 1

    while fbm < n:                              # Пока число Фибоначчи в переменной "fbm", меньше чем размер списка, считаем числа Фиб.
        fbm0 = fbm1
        fbm1 = fbm
        fbm = fbm0 + fbm1

    offset = -1                                 # Грань / смещение "offset" устанавливаем на -1, перед списком

    while fbm > 1:                              # Пока число Фибоначчи в переменной "fbm" БОЛЬШЕ "1"
        i = min(offset + fbm0, n - 1)           # В переменную "i" кладем index, который будем проверять

        if lst[i] < target:                     # Проверяем если объект по index'у в списке МЕНЬШЕ чем "target", значит "target" правее
            fbm = fbm1
            fbm1 = fbm0
            fbm0 = fbm - fbm1
            offset = i                          # Смещаем "offset" на "i" index, так как все что меньше этого index'а уже не будет "target"

        elif lst[i] > target:                   # Проверяем если объект по index'у в списке БОЛЬШЕ чем "target", значит "target" левее
            fbm = fbm0
            fbm1 = fbm1 - fbm0
            fbm0 = fbm - fbm1

        else:                                   # Если "lst[i] == target", возвращаем index
            return i

    if fbm1 and offset + 1 < n and lst[offset + 1] == target:    # Проверяем последний элемент в списке, если есть возвращаем его index, если нет, то -1
        return offset + 1

    return -1

temp = [100,200,300,400,500,600,700]
print(fibonacci_search(temp, 100))