class Fibonacci:
    def __init__(self, n: int):
        self.n = n                      # "self.n" - До какого числа[индекса] строим Фибоначчи.
        self.a = 0                      # "self.a" - Первое число списка Фибоначчи = 0
        self.b = 1                      # "self.b" - Второе число списка Фибоначчи = 1
        self.count = 0                  # Счетчик итераций.

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.n:         # Если итераций больше чем число "self.n".
            raise StopIteration         # Заканчиваем цикл.
        val = self.a                    # "Val" = self.a, будем сохранять сумму двух чисел в этой переменной.
        self.a, self.b = self.b, self.a + self.b    # 0 , 1 = 1 , 1
        self.count += 1                             # Так как теперь - "val = 1", значит "self.count = 1" выполнили одну итерацию.
        return val                                  # Возвращаем результат.

for item in Fibonacci(5):
    print(item)



