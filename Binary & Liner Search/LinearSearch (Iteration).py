### Linear search Iteration Method ###

def linear_search(lst, target):      # Передаем в функцию наш список и тот объект который ищем.
    for i in range(len(lst)):        # Для каждого "i" - индекса от 0 до конца "lst"
        if lst[i] == target:         # Если объект за индексом "i" == Target
            return i                 # Возвращаем индекс объекта
    return -1                        # Иначе, возвращаем "-1"

temp = [3,1,2,5,7,8,9]               # Неотсортированный список
print(linear_search(temp, 8))  # Вызов функции.
