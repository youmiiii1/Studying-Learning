class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None       # Переменная, будем использовать как ссылку на предыдущую Node'у

class LinkedList:
    def __init__(self):
        self.root = None
        self.tail = None           # Переменная (self.tail), в которой храним последнюю Node'у в списке

    def append(self, value):
        new_node = Node(value)     # Переменная (new_node), в ней инициализируем характеристики Node'ы
        if not self.root:          # Если (sel.root = None), значит первой / заглавной Node'ы еще не существует
            self.root = new_node   # Помечаем, что заглавная / первая Node'а (self.root) = new_node
            self.tail = new_node   # Помечаем, что последняя Node'а (self.tail) = new_node
            return
                                   # Если (self.root) Node'а уже существует, тогда далее ->
        self.tail.next = new_node  # Добавляем в список новую Node'у (new_node) и подключаем её в (self.tail.next)
        new_node.prev = self.tail  # Тут в созданной Node'е (new_node.prev), подключаем её в self.tail, то есть указали стрелку в обратную сторону
        self.tail = new_node       # Говорим списку, что последняя Node'а (self.tail) теперь та которую мы добавили (new_node)

    def output(self):
        current_node = self.root
        print(f"ROOT -> ({self.root.value})")
        print(f"TAIL -> ({self.tail.value})")
        print("None <- ", end="")
        while current_node:
            print(f"[{current_node.value}]", end=" <-> ")
            current_node = current_node.next
        print("None")

    def search(self, target) -> bool:
        current_node = self.root
        while current_node:
            if current_node.value == target:
                return True
            current_node = current_node.next
        return False

    def pop(self):
        if not self.tail:                # Если (self.tail) Noda'а не существует, значит список пуст
            return None

        pop_node = self.tail.value       # В переменную (pop_node) кладем значение последней Node'ы (self.tail.value)

        if self.root == self.tail:       # Если в нашем списке одна Node'а, значит self.root == self.tail
            self.root = None             # Удаляем единственную Node'у в списке
            self.tail = None             # Удаляем единственную Node'у в списке
        else:                            # Если (self.root НЕ РАВЕН self.tail) значит Node'а НЕ единственная в списке
            self.tail = self.tail.prev   # Говорим списку что (self.tail) указатель теперь на предпоследней Node'е в списке
            self.tail.next = None        # Говорим списку что (self.tail.next), то есть последняя Node'а в списке удалена (None)

        return pop_node

    def is_empty(self):
        if self.root:
            return False
        return True

    def qsize(self):
        counter_node = 0

        if not self.root:
            return counter_node

        current_node = self.root
        while current_node:
            counter_node += 1
            current_node = current_node.next
        return counter_node

    def index(self, target):
        if not self.root:
            return None

        node_counter = 0
        current_node = self.root

        while current_node:
            if target == current_node.value:
                return node_counter
            current_node = current_node.next
            node_counter += 1

        return None

    def slice(self, start: int, stop: int):
        counter = 0
        temp = []
        current_node = self.root

        while current_node and counter < stop:
            if counter >= start:
                temp.append(current_node.value)
            current_node = current_node.next
            counter += 1
        return temp

    def insert(self, index: int, value):
        new_node = Node(value)

        if index == 0:                              # Если вставляем Node'у в самое начало списка
            new_node.next = self.root               # Помещаем Node'у на самое начало списка

            if self.root:                           # Если (index == 0) и при этом начальная Node'а (self.root) уже в списке
                self.root.prev = new_node           # Направляем стрелку (self.root.prev) в левую сторону на первую Node'у в списке
            self.root = new_node                    # Говорим списку, что новая Noda'а (new_node), теперь является первой / заглавной (self.root)

            if not self.tail:                       # Проверяет: есть ли уже "конечная" нода (tail) в списке?
                self.tail = new_node                # Если нет, значит (new_node) — и голова (self.root) и (self.tail) — единственная нода.
            return

        current_node = self.root
        counter = 0

        while current_node and counter < index - 1: # Если (index НЕ = 0) значит запускаем цикл, работает пока не пройдет каждую Node'у или пока counter меньше чем index - 1
            current_node = current_node.next
            counter += 1

        if not current_node:                        # Защита от ошибки, если index больше чем сам список
            return
                                                    # Когда мы дошли до нужного нам index'а, мы останавливаемся перед ним (current_node) и выполняем ->
        new_node.next = current_node.next           # Вставляем Node'у в список и подключаем в правую сторону списка
        new_node.prev = current_node                # Подключаем Node'у в левую сторону списка
        current_node.next = new_node                # Подключаем (current_node) Node'у в правую сторону списка

        if new_node.next:                           # Проверяем что Noda'а (new_node) НЕ последняя в списке (self.next не None)
            new_node.next.prev = new_node           # Говорим Node'е, которая стоит после (new_node), что её (node.prev) указывает на Node'у (new_node)
        else:                                       # Если (new_node.next) = None (то-есть new_node последняя в списке)
            self.tail = new_node                    # Говорим списку что, Noda'а которую мы вставили (new_node) была последней в списке (self.tail)




ls = LinkedList()

ls.append(10)
ls.append(20)
ls.append(30)
ls.append(40)
ls.append(50)
ls.append(60)
ls.append(70)
ls.append(80)
ls.insert(8, 55)
ls.output()
