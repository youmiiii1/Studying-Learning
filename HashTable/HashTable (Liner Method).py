class HashTable:
    def __init__(self):                             # Создаем характеристики таблицы
        self.size = 8
        self.table = [None] * self.size             # Таблица содержит пустые ячейки с вложенным None
        self.count = 0
        self.load_factor = 0.75
        self.DELETED = object()                     # Переменная (self.DELETED), помечаем ей удаленные ячейки

    def _hash(self, key):
        return hash(key) % self.size

    def _rehash(self):
        print(f"Rehashing from size - {self.size} to {self.size * 2}")
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0

        for bucket in old_table:                                        # Для каждой ячейки в старой таблице
            if bucket is not None and bucket is not self.DELETED:       # Если ячейка не None и не была ранее удалена, то добавляем ее (key - value) в таблицу
                self.set(bucket[0],bucket[1])

    def set(self, key, value):
        if self.count / self.size >= self.load_factor:
            self._rehash()

        idx = self._hash(key)


        while True:
            if self.table[idx] is None:                 # Если ячейка по данному индексу равна None, значит нашли место для вставки
                self.table[idx] = (key,value)           # Вставляем в данную ячейку наш (key - value)
                self.count += 1                         # Добавляем счетчик
                return

            elif self.table[idx] is self.DELETED:       # Если ячейка по данному индексу была ранее удалена, мы просто шагаем дальше
                pass
                                                        # << НИЖЕ ИЗБАВЛЯЕМСЯ ОТ ПОВТОРЕНИЙ В ТАБЛИЦЕ >>
            elif self.table[idx][0] == key:             # Если у данной ячейки (key) тот же что мы пытаемся вставить
                self.table[idx] = (key,value)           # Заменяем у данной ячейки (value)"
                return

            idx = (idx + 1) % self.size                 # Шагаем по ячейкам таблицы на 1 шаг вперед

    def get(self, key):
        idx = self._hash(key)
        start_idx = idx                                 # Переменная (start_idx), помечаем начальный индекс "боремся с бесконечным циклом"

        while True:
            if self.table[idx] is None:                 # Если ячейка по данному индексу равна None, то вызываем ошибку "Такого ключа в таблице нет"
                raise KeyError("No key found")

            elif self.table[idx] is self.DELETED:       # Если ячейка по данному индексу была ранее удалена, просто пропускаем её
                pass

            elif self.table[idx][0] == key:             # Если ключ в ячейке по данному индексу тот же ключ, что мы ищем, то возвращаем (value) "Значит ключ нашли"
                return self.table[idx][1]

            idx = (idx + 1) % self.size
                                                        # << НИЖЕ УХОДИМ ОТ БЕСКОНЕЧНОГО ЦИКЛА >>
            if idx == start_idx:                        # Если текущий индекс тот же что и индекс в переменной (start_idx), значит мы вернулись в начало и прошли всю таблицу
                raise KeyError("No key found")          # Вызываем ошибку, что-бы закончить цикл

    def delete(self, key):
        idx = self._hash(key)
        start_idx = idx

        while True:
            if self.table[idx] is None:                 # Если ячейка по данному индексу равна None, то вызываем ошибку "Такого ключа в таблице нет"
                raise KeyError("No key found")

            elif self.table[idx] == self.DELETED:       # Если ячейка по данному индексу была ранее удалена, просто пропускаем её
                pass

            elif self.table[idx][0] == key:             # Если ключ в ячейке по данному индексу тот же ключ, что мы ищем, то помечаем данную ячейка (self.DELETED)
                self.table[idx] = self.DELETED
                self.count -= 1                         # Счетчик -1 "так как удалили ячейку"
                return

            idx = (idx + 1) % self.size

            if idx == start_idx:
                raise KeyError("No key found")

    def __contains__(self, key):
        idx = self._hash(key)
        start_idx = idx

        while True:
            if self.table[idx] is None:
                return False                        # Если ячейка None, значит в таблице не было ключа который мы ищем "возвращаем false"

            elif self.table[idx] is self.DELETED:
                pass

            elif self.table[idx][0] == key:         # Если ячейка по этому индексу содержит тот же ключ, что мы ищем, то возвращаем True
                return True

            idx = (idx + 1) % self.size

            if idx == start_idx:
                return False

    def __len__(self):
        return self.count

    def __str__(self):
        temp = []
        for bucket in self.table:
            if bucket is not None:
                if bucket is self.DELETED:
                    continue
                k, v = bucket
                temp.append(f"{k}: {v}")
        return "{" + ", ".join(temp) + "}"


