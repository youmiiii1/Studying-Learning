class Node:                         # Нода, в которой базовые две характеристики
    def __init__(self, value):
        self.value = value          # Переменная (self.value), в ней хранится значение которое мы передаем в Node'у
        self.next = None            # Переменная (self.next), в которой хранится следующая Node'а

class LinkedList:
    def __init__(self):
        self.root = None            # Переменная (self.root), в которой храним заглавную / первую Node'у

    def append(self, value):        # Функция для добавления ноды в список.
        new_node = Node(value)      # Переменная (new_node), в ней инициализируем характеристики Node'ы
        if not self.root:           # Если (sel.root = None), значит первой / заглавной Node'ы еще не существует
            self.root = new_node    # Помечаем, что главная Node'а (self.root) = new_node
            return                  # Выход из функции, выше объявили заглавную Node'у и добавили её в список, а значит больше ничего не нужно.
        else:                       # Если (self.root) изначально не None
            current_node = self.root                # Переменная (current_node), переходим в самое начало списка к первой / заглавной Node'е (self.root)
            while current_node.next:                # Пока Noda'а на которой мы находимся и её характеристика (current_node.next НЕ РАВЕН значению None)
                current_node = current_node.next    # Переходим к следующей Node'е по списку (current_node = current_node.next)
            current_node.next = new_node            # Если в while (current_node.next РАВЕН значению "None") значит мы в ней инициализируем новую Node'у

    def output(self):               # Функция для вывода всех нод в списке.
        current_node = self.root    # Переменная (current_node), переходим в самое начало списка к первой / заглавной Node'е (self.root)
        while current_node:         # "Пока (current_node НЕ РАВЕН значению "None")
            print(current_node.value, end=" -> ")    # Выводим (self.value) ноды на которой находимся (Пример: A -> B -> None)
            current_node = current_node.next         # Переходим к следующей Node'е (current_node = current_node.next)
        print("None")                                # Если (current_node РАВЕН "None"), значит Noda'а пустая, просто выводим "None"

    def search(self, target) -> bool:   # Функция для поиска объекта в списке.
        current_node = self.root        # Переменная (current_node), переходим в самое начало списка к первой / заглавной Node'е (self.root)
        while current_node:             # "Пока (current_node НЕ РАВЕН значению "None")
            if current_node.value == target:        # Если объект в данной Node'е (current_node.value) РАВЕН значению (target), значит выводим True
                return True
            current_node = current_node.next        # Если объект в данной Node'е (current_node.value) НЕ РАВЕН значению (target), значит шагаем к следующей Node'е
        return False                                # Выводим False если (target) объект не найден в списке

    def pop(self):
        if not self.root:         # Если (sel.root = None), значит первой / заглавной Node'ы еще не существует
            return None

        if not self.root.next:              # Если (sel.root.next = None), значит первая / заглавная Node'а единственная в списке
            pop_node = self.root.value      # Переменная (pop_node), в ней храним взятое значение из Node'ы (self.root.value)
            self.root = None                # Удаляем Node'у (self.root)
            return pop_node
                                            # Если (self.root и self.root.next НЕ РАВЕН значению "None"), то -->
        current_node = self.root            # Переменная (current_node), переходим в самое начало списка к первой / заглавной Node'е (self.root)

        while current_node.next.next:        # Пока у следующего узла есть ещё один next, значит что мы не в предпоследнем узле
            current_node = current_node.next # Переходим к следующей Node'е по списку (current_node = current_node.next)

        pop_node = current_node.next.value   # Переменная (pop_node), в ней хранится значение (self.value) из последней Node'ы
        current_node.next = None             # Удаляем последнюю Node'у из списка
        return pop_node                      # Возвращаем значение удалённой последней Node'ы

    def is_empty(self):                      # Функция, проверяем пустой ли список
        if self.root:                        # Если в списке что-то есть, значит он не пустой
            return False                     # Выводим False (список не пуст)
        return True                          # Если в списке пусто, выводим True

    def qsize(self):                         # Функция, проверяем сколько элементов в списке
        counter_node = 0                     # Переменная (counter_node), в ней храним число найденных Node из списка.

        if not self.root:                    # Если (sel.root = None), значит первой / заглавной Node'ы еще не существует
            return counter_node              # Возвращаем (0)

        current_node = self.root             # Переменная (current_node), переходим в самое начало списка к первой / заглавной Node'е (self.root)
        while current_node:                  # Пока (current_node) НЕ РАВНО None
            counter_node += 1                # Добавляем +1 в (counter_node)
            current_node = current_node.next    # Переходим к следующей Node'е по списку (current_node = current_node.next)
        return counter_node   # Когда список закончился, возвращаем найденное количество Node

    def index(self, target):  # Функция, возвращает индекс объекта который ищем.
        if not self.root:     # Если (sel.root = None), значит первой / заглавной Node'ы еще не существует
            return None

        node_counter = 0             # Переменная, значение (counter) = индекс на котором мы находимся (current_node).
        current_node = self.root     # Переменная (current_node), переходим в самое начало списка к первой / заглавной Node'е (self.root)

        while current_node:                         # Цикл, пока в списке есть Node'ы
            if target == current_node.value:        # Если объект который мы ищем (target) РАВЕН значению текущей Node'е (current_node)
                return node_counter                 # Возвращаем индекс
            current_node = current_node.next        # Если объект который мы ищем (target) НЕ РАВЕН значению текущей Node'е, то шагаем к следующей
            node_counter += 1                       # И увеличиваем индекс на 1

        return None     # Если target не нашли, вернём None

    def slice(self, start: int, stop: int):  # Функция, возвращает копию списка с числами по индексу (start) до (end, не включительно)
        counter = 0                          # Переменная, значение (counter) = индекс на котором мы находимся (current_node).
        temp = []                            # Временный список, в нем будем хранить скопированные объекты из основного списка
        current_node = self.root             # Переменная (current_node), переходим в самое начало списка к первой / заглавной Node'е (self.root)

        while current_node and counter < stop:  # Цикл, пока в списке есть Node'ы и значение counter не больше чем stop
            if counter >= start:                # Если (counter) больше или то же значение, что и (start), то --
                temp.append(current_node.value) # -- добавляем в список (temp) значение Node'ы на которой сейчас находимся
            current_node = current_node.next    # Иначе, если (Stroke "92": counter МЕНЬШЕ чем start) то мы шагаем к следующей Node'е и --
            counter += 1                        # -- добавляем к counter + 1
        return temp                             # Когда цикл закончится, возвращаем скопированный список

    def insert(self, index: int, value):    # Функция, добавляет объект в список
        if not self.root:                   # Если (sel.root = None), значит первой / заглавной Node'ы еще не существует
            return

        new_node = Node(value)              # Переменная (new_node), в ней инициализируем характеристики Node'ы
        counter = 0                         # Переменная, значение (counter) = индекс на котором мы находимся (current_node)
        current_node = self.root            # Переменная (current_node), переходим в самое начало списка к первой / заглавной Node'е (self.root)

        if index == 0:                      # Если index равен 0
            new_node.next = self.root       # Добавляем Node'у в самое начало списка (за index'ом 0), а Node'у (self.root) перемещаем на второе место (за index'ом 1)
            self.root = new_node            # Говорим списку, что (new_node) теперь самая первая Node'а в списке и помечаем её как (self.root)
            return

        while current_node and counter < index - 1:     # Если (index НЕ = 0) значит запускаем цикл, работает пока не пройдет каждую Node'у или пока counter меньше чем index - 1
            current_node = current_node.next            # Пока цикл работает, шагаем к следующей Node'е
            counter += 1                                # Пока цикл работает, увеличиваем counter на 1
                                                        # Если в списке закончились Node'ы или counter больше чем index ->
        new_node.next = current_node.next               # То перед индексом в наш список добавляем (new_node) и связываем её со следующей Node'ой
        current_node.next = new_node                    # А (current_node.next) указываем на (new_node), то есть на следующую Node'у

ls = LinkedList()

ls.append(10)
ls.append(20)
ls.append(30)
ls.append(40)
ls.append(50)
ls.append(60)
ls.append(70)
ls.append(80)
ls.append(90)
ls.append(100)
ls.insert(0, 55)
ls.output()
print(ls.slice(2, 5))
print(ls.index(3))
print(ls.is_empty())
print(ls.search(1))
print(ls.pop())
print(ls.pop())
print(ls.pop())
print(ls.qsize())


