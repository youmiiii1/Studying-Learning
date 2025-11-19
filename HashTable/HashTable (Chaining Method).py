class HashTable:
    def __init__(self):
        self.size = 8                                   # Размер таблицы (кол. ячеек)
        self.table = [[] for _ in range(self.size)]     # Переменная (self.table), в ней создаем таблицу.
        self.count = 0                                  # Переменная (self.count), в ней записываем кол. (key - value) находящихся в таблице
        self.load_factor = 0.75                         # Переменная (self.load_factor), следим за заполненностью таблицы

    def _hash(self, key):                 # Функцию (_hash), переработка в хеш и возвращает индекс для таблицы
        return hash(key) % self.size

    def _rehash(self):                                                  # Функция (_rehash), срабатывает при перегрузке таблицы
        print(f"Rehashing from size - {self.size} to {self.size * 2}")
        old_table = self.table                                          # Переменная (old_table), в ней храним текущую таблицу
        self.size *= 2                                                  # Увеличиваем размер таблицы в 2 раза
        self.table = [[] for _ in range(self.size)]                     # Обновляем переменную (self.table), создаем новую таблицу с большим (self.size)
        self.count = 0                                                  # Новая таблица пустая по-этому сбрасываем счетчик
                                                                        # << ДАЛЕЕ ИЗ СТАРОЙ ТАБЛИЦЫ ПЕРЕНОСИМ ДАННЫЕ В НОВУЮ >>
        for bucket in old_table:                                        # Для каждой ячейки в старой таблице
            for k, v in bucket:                                         # Для каждого (key - value) в каждой ячейке
                self.set(k,v)                                           # Заполняем в новую таблицу


    def set(self, key, value):                                  # Функция (set), добавляем (key, value) в таблицу
        if self.count / self.size >= self.load_factor:           # Проверка на то что таблица размером не больше чем (self.load_factor)
            self._rehash()                                      # Если таблица больше чем (self.load_factor), то вызываем ре-хеширование

        idx = self._hash(key)

        for bucket in self.table[idx]:                          # Для каждого (key - value) в ячейке по индексу (idx)
            if bucket[0] == key:                                # Если key который находится в ячейке тот же что мы добавляем
                bucket[1] = value                               # Просто заменяем у этого ключа значение на новое
                return
                                                                # Если ключ который мы пытаемся добавить еще не существует в данном bucket
        self.table[idx].append((key, value))                    # Добавляем его в данный bucket
        self.count += 1                                         # Увеличиваем счетчик на +1

    def get(self, key):                                 # Функция (get), получаем значение (value) по ключу который ищем
        idx = self._hash(key)

        for bucket in self.table[idx]:                  # Для каждого (key - value) в ячейке по индексу (idx)
            if bucket[0] == key:                        # Если key который находится в ячейке тот же что мы ищем
                return bucket[1]                        # Возвращаем (Value)

        raise KeyError("No key found.")                 # Вызываем ошибку если не нашли такой ключ

    def delete(self,key):                               # Функция (delete), удаляем (key - value) из таблицы
        idx = self._hash(key)

        for i, bucket in enumerate(self.table[idx]):    # Проходимся по каждому массиву в ячейке (self.table[idx]), индекс каждого массива храним в переменной (i)
            if bucket[0] == key:                        # Если key который находится в ячейке тот же что мы ищем
                del self.table[idx][i]                  # Удаляем массив (key - value)
                self.count -= 1                         # Счетчик -1
                return

        raise KeyError("No key found.")                  # Вызываем ошибку если не нашли такой ключ

    def __contains__(self, key):            # Функция (__contains__), проверяем есть ли ключ в таблице
        idx = self._hash(key)               # Переменная (idx), в нее записываем индекс текущего ключа

        for bucket in self.table[idx]:      # Для каждого (key - value) в ячейке по индексу (idx)
            if bucket[0] == key:            # Если key который находится в ячейке тот же что мы ищем
                return True                 # Возвращаем True

        return False                        # Возвращаем False если не нашли такой-же ключ

    def __len__(self):                  # Функция (__len__), возвращаем текущее количество (key - value) в таблице
        return self.count

    def __str__(self):
        temp = []
        for bucket in self.table:
            for k, v in bucket:
                temp.append(f"{k}: {v}")
        return "{" + ", ".join(temp) + "}"